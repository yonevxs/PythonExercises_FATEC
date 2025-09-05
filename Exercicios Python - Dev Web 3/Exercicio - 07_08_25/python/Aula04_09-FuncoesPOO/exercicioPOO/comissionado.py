import locale
locale.setlocale(locale.LC_ALL, 'pt-BR.UTF-8')
from funcionario import Funcionario

class Comissionado(Funcionario):
    def __init__(self, codigo, nome, valorHora, horasTrabalhadas, vendas):
        super().__init__(codigo, nome, valorHora, horasTrabalhadas)
        self.vendas = float(vendas)

    def calcularSalario(self):
         return ((self.horasTrabalhadas * self.valorHora) * 24) + (self.vendas * 0.15)
    def exibirComissionado(self):
        salario_comissao = self.calcularSalario()
        salario = (self.horasTrabalhadas * self.valorHora) * 24
        print(f"Código: {self.codigo} | Nome: {self.nome} | Valor p/hora: {self.valorHora} | Vendas: {locale.currency(self.vendas, symbol=True, grouping=True)} | Salário: {locale.currency(salario, symbol=True, grouping=True)} | Salário com % de Vendas: {locale.currency(salario_comissao, symbol=True, grouping=True)}")

#c = Comissionado(55, "Ciclano", 7.50, 9, 500)
#print(c.calcularSalario())
#c.exibirComissionado()