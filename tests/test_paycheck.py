import unittest
from paycheckpy.src.paycheck import PayCheckPy as payc


class test_paycheck(unittest.TestCase):

    def test_calcular_inss(self):
        valor_inss = payc.inss(salario_base=3000)
        self.assertEqual(valor, 300)

    def test_calcular_fgts(self):
        valor_fgts = payc.fgts(salario_base=3000)
        self.assertEqual(valor_fgts, 240)

    def test_calcular_dependentes(self):
        valor_dependentes = payc.dependentes(2)
        self.assertEqual(valor_dependentes, 379.18)
    
    def test_calcular_irrf(self):
        valor_inss = payc.inss(salario_base=3000)
        valor_irrf = payc.irrf(inss=valor_inss, salario_base=3000)
        self.assertEqual(valor_irrf, 29.01)

    def test_calcular_dsr(self):
        valor_dsr = payc.dsr(val_total_horas_extras=104.55,
            dias_uteis_trabalhados=24, dsr=5)
        self.assertEqual(valor_dsr, 21.78)

    def test_calcular_vale_transporte(self):
        # taxa será melhor utilizada se for uma constante
        valor_vale_transporte = payc.vale_transporte(salario_base=3000, taxa=0.06)
        self.assertEqual(valor_vale_transporte, 180)

    def test_calcular_adicional_noturno(self):
        salario_base = 3000
        qtd_horas_trabalhadas_mes = 220
        valor_hora_trabalhada = 3000 / 220
        valor_adicional_noturno = payc.adicional_noturno(
            valor_hora_trabalhada=valor_hora_trabalhada, qtd_horas_extras=10)
        self.assertEqual(valor_adicional_noturno, 10)

    def test_calcular_adicional_insalubridade(self):
        valor_insalubridade = payc.insalubridade(grau_insalubridade=20)
        self.assertEqual(valor_insalubridade, 199.60)

    def test_calcular_salario_liquido(self):
        salario_base = 3000
        salario_liquido = payc.salario_liquido(salario_base=salario_base)
        self.assertEqual(salario_liquido, 2760.8)