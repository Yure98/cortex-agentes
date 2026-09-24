import copy
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]

def module(path, name):
    spec = importlib.util.spec_from_file_location(name, ROOT / path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod

core = module('core/cortex.py', 'cortex')
mat = module('skills/cortex-maternidade/scripts/diagnostico.py', 'mater')
ins = module('scripts/install.py', 'installer')
pen = module('skills/pensao-por-morte/scripts/score_prontidao.py', 'scorepen')
acc = module('skills/auxilio-acidente/scripts/score_prontidao.py', 'scoreacc')
inc = module('skills/beneficios-incapacidade/scripts/cenarios.py', 'incapacidade')
bpc = module('skills/bpc-loas/scripts/renda.py', 'bpc_renda')

class CoreTests(unittest.TestCase):
    def test_pcd_coefficients(self):
        self.assertEqual(core.coeficiente('pcd-idade', 15, 'F'), core.Decimal('.85'))
        self.assertEqual(core.coeficiente('pcd-tempo', 15, 'F'), 1)
        self.assertEqual(core.coeficiente('pcd-idade', 40, 'M'), 1)
        self.assertEqual(core.coeficiente('geral-ec103', 20, 'F'), core.Decimal('.70'))
    def test_bad_numbers(self):
        for v in ('NaN', 'Infinity', -1, True):
            with self.assertRaises(ValueError): core.numero(v)
    def test_dossier(self):
        d = json.loads((ROOT/'core/dossie.exemplo.json').read_text())
        self.assertEqual(core.validar(d), [])
        self.assertTrue(core.validar(d, True))
        d['revisao'] = dict.fromkeys(d['revisao'], 'aprovado')
        self.assertTrue(core.validar(d, True)) # states cannot bypass missing evidence
    def test_dates(self):
        self.assertEqual(core.soma_meses(date(2024,2,29), 12), date(2025,2,28))
        self.assertEqual(core.soma_meses(date(2025,1,31), 4), date(2025,5,31))
    def scenarios(self):
        return {'unidade':'reais-constantes','taxa_real_mensal':0,'horizonte_meses':200,
                'cenarios':[{'nome':'A','rmi':2000,'espera_meses':0,'contribuicao_adicional_mensal':0,'elegibilidade_confirmada':True,'fonte_calculo':'x'},
                            {'nome':'B','rmi':2600,'espera_meses':24,'contribuicao_adicional_mensal':0,'elegibilidade_confirmada':True,'fonte_calculo':'y'}]}
    def test_payback_consistent_13(self):
        self.assertEqual(core.comparar(self.scenarios())['equilibrio'],104)
    def test_equal_rmi_no_payback(self):
        d=self.scenarios(); d['cenarios'][1]['rmi']=2000
        self.assertIsNone(core.comparar(d)['equilibrio'])
    def test_unknown_eligibility(self):
        d=self.scenarios(); d['cenarios'][1]['elegibilidade_confirmada']=None
        with self.assertRaises(ValueError): core.comparar(d)

class ScoresTests(unittest.TestCase):
    def test_unknown_blocks(self):
        self.assertTrue(all(v is None for v in pen.template()['bloqueios'].values()))
    def test_essential_not_na(self):
        d=pen.template(); d['itens']['A1']='na';d['justificativas_na']['A1']='teste'
        with self.assertRaises(ValueError):pen.pontuar(d)
    def test_string_false_rejected(self):
        d=pen.template(); d['bloqueios']['fraude_ou_simulacao']='false'
        with self.assertRaises(ValueError):pen.pontuar(d)
    def test_common_accident_no_cat_penalty(self):
        d=acc.template();d['natureza']='comum';d['itens']=dict.fromkeys(d['itens'],'cheio')
        d['itens']['B1']='zero';d['itens']['B2']='zero'
        self.assertEqual(acc.pontuar(d)[0],100)

class MaternityTests(unittest.TestCase):
    def case(self):
        return {'fato_gerador':'2026-08-15','categoria':'facultativa','data_referencia':'2026-09-23','salario_minimo':1621,'teto_rgps':8475.55,'ultima_contribuicao':'2026-01-31','desemprego_involuntario':True}
    def test_facultative_grace(self):
        r=mat.calcular_periodo_graca(mat.Caso.de_dict(self.case()))
        self.assertEqual(r['meses_totais'],6)
        self.assertEqual(r['limite_com_extensao_art_30_II'],'2026-09-15')
    def test_bool_string(self):
        d=self.case(); d['desemprego_involuntario']='false'
        with self.assertRaises(ValueError):mat.Caso.de_dict(d)
    def test_missing_category(self):
        d=self.case(); del d['categoria']
        with self.assertRaises(ValueError):mat.Caso.de_dict(d)
    def test_full_salary_not_rgps_cap(self):
        d=self.case();d.update(categoria='empregada',remuneracao_mensal=12000)
        self.assertEqual(mat.calcular_rmi(mat.Caso.de_dict(d))['rmi'],12000)
    def test_salary_without_competence_blocks(self):
        d=self.case();d['salarios_contribuicao']=[1621]*12
        self.assertIsNone(mat.calcular_rmi(mat.Caso.de_dict(d))['rmi'])
    def test_no_total_prescription_assertion(self):
        self.assertIsNone(mat.calcular_prescricao(mat.Caso.de_dict(self.case()))['prescrito'])

class CLITests(unittest.TestCase):
    def pension(self,*args):
        return subprocess.run([sys.executable,str(ROOT/'skills/pensao-por-morte/scripts/calculadora_pensao.py'),*args],text=True,capture_output=True)
    def test_2018_dib_90(self):
        r=self.pension('dib','--obito','2018-01-01','--der','2018-03-01','--idade-dependente','40')
        self.assertEqual(r.returncode,0,r.stderr);self.assertIn('DATA DO OBITO',r.stdout)
    def test_unknown_filters(self):
        r=self.pension('duracao','--obito','2025-01-31','--idade-dependente','40')
        self.assertNotEqual(r.returncode,0)
    def test_four_calendar_months(self):
        r=self.pension('duracao','--obito','2025-01-31','--idade-dependente','40','--contribuicoes','2','--uniao-meses','1')
        self.assertIn('31/05/2025',r.stdout)
    def test_zero_dependents(self):
        r=self.pension('rmi','--obito','2026-01-01','--base','4000','--dependentes','0','--salario-minimo','1621','--teto','8475.55')
        self.assertNotEqual(r.returncode,0)
    def test_child_only_180(self):
        args=['dib','--obito','2026-01-01','--der','2026-05-01','--idade-dependente','15']
        self.assertIn('DATA DO REQUERIMENTO',self.pension(*args).stdout)
        self.assertIn('DATA DO OBITO',self.pension(*args,'--filho').stdout)

class InstallTests(unittest.TestCase):
    def test_install_reinstall_restore_preserves_custom_and_third_party(self):
        with tempfile.TemporaryDirectory() as temp:
            dest=Path(temp)/'claude';third=dest/'skills/terceiro/SKILL.md';third.parent.mkdir(parents=True);third.write_text('terceiro')
            backup=ins.install(dest)
            custom=dest/'skills/raio-x-cnis/custom.txt';custom.write_text('pessoal')
            second=ins.install(dest)
            self.assertFalse(custom.exists());ins.restore(dest,second)
            self.assertEqual(custom.read_text(),'pessoal');self.assertEqual(third.read_text(),'terceiro')
            ins.restore(dest,backup);self.assertFalse(custom.parent.exists());self.assertTrue(third.exists())
    def test_rollback_after_copy_failure(self):
        with tempfile.TemporaryDirectory() as temp:
            dest=Path(temp)/'claude';ins.install(dest)
            target=dest/'skills/raio-x-cnis/custom.txt';target.write_text('preservar')
            original=ins.copy;failed=False
            def fail_once(src,dst):
                nonlocal failed
                if not failed and any(part.startswith('cortex-stage-') for part in src.parts) and dst==dest/'skills/auxilio-acidente':
                    failed=True;raise OSError('falha simulada')
                return original(src,dst)
            with patch.object(ins,'copy',side_effect=fail_once):
                with self.assertRaises(OSError):ins.install(dest)
            self.assertTrue(failed);self.assertEqual(target.read_text(),'preservar')
    def test_core_copies(self):
        r=subprocess.run([sys.executable,str(ROOT/'scripts/sync_core.py'),'--check'],capture_output=True)
        self.assertEqual(r.returncode,0,r.stderr)

if __name__=='__main__':unittest.main()

class AdditionalBoundaries(unittest.TestCase):
    def test_pedagio_exact_33_excluded(self):
        self.assertFalse(core.pedagio50(33,38,'M',200)['acesso_regra'])
        self.assertTrue(core.pedagio50('33.01',38,'M',200)['requisitos_numericos'])
    def test_ifbra_two_forms(self):
        self.assertEqual(core.ifbra({'medica':[100]*41,'social':[100]*41})['total_bruto'],8200)
        with self.assertRaises(ValueError):core.ifbra({'medica':[100]*41})
        with self.assertRaises(ValueError):core.ifbra({'medica':[100]*40,'social':[100]*41})

class CoordinatorInstallTests(unittest.TestCase):
    def test_prev_and_specialists_installed_together(self):
        with tempfile.TemporaryDirectory() as temp:
            dest=Path(temp)/'claude'
            ins.install(dest)
            self.assertTrue((dest/'commands/prev.md').is_file())
            self.assertEqual(len(list((dest/'skills').glob('*/SKILL.md'))),14)
            self.assertTrue((dest/'commands/incapacidade.md').is_file())
            for name in ('bpc','especial','rural'):
                self.assertTrue((dest/'commands'/f'{name}.md').is_file())
            for name in ('prev','aposentadoria-pcd','recurso-inss','estagiario-peticoes','beneficios-incapacidade','bpc-loas','aposentadoria-especial','segurado-especial-rural'):
                self.assertTrue((dest/'skills'/name/'.cortex/protocolo.md').is_file())

class IncapacidadeTests(unittest.TestCase):
    def caso(self):
        return json.loads((ROOT/'skills/beneficios-incapacidade/assets/casos-exemplo.json').read_text())
    def test_aposentadoria_comum_20_anos_mulher(self):
        r=inc.calcular(self.caso())
        self.assertEqual(r['coeficiente'],'0.70')
        self.assertEqual(r['base_teorica_antes_piso_teto'],'2800.00')
    def test_acidente_comum_nao_gera_cem_porcento(self):
        d=self.caso(); d['nexo_ocupacional_comprovado']=False
        self.assertEqual(inc.calcular(d)['coeficiente'],'0.70')
        d['nexo_ocupacional_comprovado']=True
        self.assertEqual(inc.calcular(d)['coeficiente'],'1')
    def test_auxilio_limitado_media_12(self):
        d={k:v for k,v in self.caso().items() if k not in ('sexo_regra','anos_completos','nexo_ocupacional_comprovado')}
        d.update(especie='temporaria',media_ultimos_ate_12='3000.00',fonte_media_12='media auditada ficticia',quantidade_salarios=12,regra_2015_aplicavel=True)
        self.assertEqual(inc.calcular(d)['base_teorica_antes_piso_teto'],'3000.00')
        d['media_ultimos_ate_12']='5000.00'
        self.assertEqual(inc.calcular(d)['base_teorica_antes_piso_teto'],'3640.00')
    def test_bloqueios_de_entradas(self):
        d=self.caso(); d['nexo_ocupacional_comprovado']='false'
        with self.assertRaises(ValueError):inc.calcular(d)
        d=self.caso();d['data_inicio']='2018-01-01'
        with self.assertRaises(ValueError):inc.calcular(d)
        d=self.caso();d['salario_beneficio']='NaN'
        with self.assertRaises(ValueError):inc.calcular(d)
        d=self.caso();d['anos_completos']=20.5
        with self.assertRaises(ValueError):inc.calcular(d)
    def test_cli_example(self):
        r=subprocess.run([sys.executable,str(ROOT/'skills/beneficios-incapacidade/scripts/cenarios.py'),'--exemplo'],capture_output=True,text=True)
        self.assertEqual(r.returncode,0,r.stderr)
        self.assertEqual(json.loads(r.stdout)['limites_e_direito'].split(':')[0],'pendentes')

class BpcRendaTests(unittest.TestCase):
    def exemplo(self):
        return json.loads((ROOT/'skills/bpc-loas/assets/caso-ficticio.json').read_text(encoding='utf-8'))
    def test_fronteira_por_competencia_e_grupo_legal(self):
        d=self.exemplo()
        d['pessoas'][1]['rendimentos'][0]['valor']='810.50'
        d['pessoas'].append({'id':'visitante','grupo_legal':False,'fonte_grupo':'não integra grupo, exemplo fictício',
            'rendimentos':[{'valor':'10000.00','inclui':True,'fonte_classificacao':'renda contabilizável se membro',
                            'fonte_valor':'exemplo fictício'}]})
        r=bpc.calcular(d)
        self.assertEqual(r['renda_per_capita'],'405.25')
        self.assertEqual(r['comparacao_puramente_aritmetica'],'ate_1_4')
        d['pessoas'][1]['rendimentos'][0]['valor']='810.51'
        self.assertEqual(bpc.calcular(d)['comparacao_puramente_aritmetica'],'acima_1_4')
    def test_exclusao_e_deducao_exigem_fonte(self):
        d=self.exemplo();item=d['pessoas'][1]['rendimentos'][0]
        item['inclui']=False
        self.assertEqual(bpc.calcular(d)['renda_bruta_incluida'],'0.00')
        del item['fonte_classificacao']
        with self.assertRaises(ValueError):bpc.calcular(d)
        d=self.exemplo();d['deducoes']=[{'valor':'100.00','fonte_classificacao':'hipótese fictícia validada pelo advogado',
                                           'fonte_valor':'comprovante fictício'}]
        self.assertEqual(bpc.calcular(d)['renda_per_capita'],'350.00')
        d['deducoes'][0]['valor']='801.00'
        with self.assertRaises(ValueError):bpc.calcular(d)
    def test_entrada_incompleta_bloqueia(self):
        d=self.exemplo();d['pessoas'][0]['grupo_legal']=None
        with self.assertRaises(ValueError):bpc.calcular(d)
        d=self.exemplo();d['pessoas'][0]['rendimentos'][0]['valor']=float('nan')
        with self.assertRaises(ValueError):bpc.calcular(d)
        d=self.exemplo();d['pessoas'][1]['rendimentos']=[]
        with self.assertRaises(ValueError):bpc.calcular(d)

class UpdatePackageTests(unittest.TestCase):
    def test_obsolete_cortex_files_removed_and_license_installed(self):
        with tempfile.TemporaryDirectory() as temp:
            dest=Path(temp)/'claude'
            old=dest/'skills/cortex-maternidade/references/antigo.md'
            old.parent.mkdir(parents=True);old.write_text('antigo')
            backup=ins.install(dest)
            self.assertFalse(old.exists())
            self.assertTrue((backup/'anterior/skills/cortex-maternidade/references/antigo.md').exists())
            for skill in (dest/'skills').iterdir():
                self.assertIn('Yure Digital',(skill/'.cortex/LICENSE').read_text())
    def test_concurrent_install_blocked(self):
        with tempfile.TemporaryDirectory() as temp:
            dest=Path(temp);(dest/'.cortex-install.lock').write_text('ocupado')
            with self.assertRaises(ValueError):ins.install(dest)
            self.assertFalse((dest/'skills').exists())

class ReadOnlyUpdateTests(unittest.TestCase):
    def test_retry_readonly_git_object(self):
        import os
        import stat
        with tempfile.TemporaryDirectory() as temp:
            path=Path(temp)/'object';path.write_text('git object')
            path.chmod(stat.S_IREAD)
            error=PermissionError(13,'access denied',str(path))
            ins.retry_readonly(os.unlink,str(path),(PermissionError,error,None))
            self.assertFalse(path.exists())
    def test_writable_permission_denial_not_bypassed(self):
        from unittest.mock import Mock
        with tempfile.TemporaryDirectory() as temp:
            path=Path(temp)/'locked';path.write_text('locked')
            retry=Mock();error=PermissionError(13,'locked',str(path))
            with self.assertRaises(PermissionError):
                ins.retry_readonly(retry,str(path),(PermissionError,error,None))
            retry.assert_not_called();self.assertTrue(path.exists())
    def test_upgrade_old_skill_with_readonly_git_objects(self):
        import stat
        with tempfile.TemporaryDirectory() as temp:
            dest=Path(temp)/'claude'
            obj=dest/'skills/aposentadoria-pcd/.git/objects/11/object'
            obj.parent.mkdir(parents=True);obj.write_text('original');obj.chmod(stat.S_IREAD)
            backup=ins.install(dest)
            self.assertFalse(obj.exists())
            saved=backup/'anterior/skills/aposentadoria-pcd/.git/objects/11/object'
            self.assertEqual(saved.read_text(),'original')
            ins.restore(dest,backup)
            self.assertEqual(obj.read_text(),'original')
