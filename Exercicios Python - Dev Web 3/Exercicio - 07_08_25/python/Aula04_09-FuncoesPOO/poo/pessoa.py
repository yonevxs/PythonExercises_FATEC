class Pessoa:
    #pass #ignora a classe vazia
    #CONSTRUTOR 
    def __init__(self, id, nome): # self - Serve para acessar o atributo, similar ao this
        # Caso não tenha self, o primeiro parametro fará esse papel
        self.id = id
        self.nome = nome

    # Utiliza-se o self dentro de funções para acessar parâmetros
    def exibir(self):
        print(f"ID: {self.id} - Nome: {self.nome}")


# Instanciando objeto
# p1 = Pessoa(1, 'Lucas')

# print(p1)
# print(p1.id)
# print(p1.nome)
# p1.exibir()