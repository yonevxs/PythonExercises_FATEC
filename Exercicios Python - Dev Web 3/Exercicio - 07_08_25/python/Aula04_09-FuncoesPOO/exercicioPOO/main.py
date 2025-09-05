import funcionario
import comissionado

# f = funcionario.Funcionario(1, "Fulano", 6.20, 8)
# c = comissionado.Comissionado(2, "Ciclano", 7.50, 8, 1500)
print("Cadastro de Funcionario")
cd = input("Digite o código do funcionário: ")
nm = input("Digite o nome do funcionário: ")
vl_hr = input("Digite o valor/hora: ")
hr_tb = input("Digite a carga horaria: ")

print("\n")

print("Cadastro de Vendedor")
f = funcionario.Funcionario(cd, nm, vl_hr, hr_tb)
cd = input("Digite o código do funcionário: ")
nm = input("Digite o nome do funcionário: ")
vl_hr = input("Digite o valor/hora: ")
hr_tb = input("Digite a carga horaria: ")
vd = input("Digite a comissão de vendas: ")
c = comissionado.Comissionado(cd, nm, vl_hr, hr_tb, vd)

f.exibirFuncionario()
c.exibirComissionado()