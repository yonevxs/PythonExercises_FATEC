import locale
locale.setlocale(locale.LC_ALL, 'pt-BR.UTF-8')

class Funcionario():
    def __init__(self, codigo, nome, valorHora, horasTrabalhadas):
        self.codigo = codigo
        self.nome = nome
        self.valorHora = float(valorHora)
        self.horasTrabalhadas = int(horasTrabalhadas)
    
    def exibirFuncionario(self):
        print(f"Código: {self.codigo} | Nome: {self.nome} | Valor p/hora: {locale.currency(self.valorHora, symbol=True, grouping=True)} | Salário: {locale.currency(((self.horasTrabalhadas * self.valorHora) * 24), symbol=True, grouping=True)}")
    def calcularSalario(self):
        return (self.horasTrabalhadas * self.valorHora) * 24

#f = Funcionario(1, 'Fulano', 5.75, 8)
#print(f.calcularSalario())
#f.exibirFuncionario()