class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=55): # * filhos quer dizer uma quantidade variável de filhos
        self.idade = idade
        self.nome = nome
        self.filhos = list (filhos)

    def cumprimentar(self):
        return f'Olá, meu nome é {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 43

    @classmethod
    def nome_e_atributo_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

class Homem(Pessoa): # Herança: herda todos os atributos ou métodos
    def cumprimentar(self): # sobrescrita de método
        cumprimentar_da_classe = super().cumprimentar()
        return f'{cumprimentar_da_classe}. Aperto de mão'

class Mutante(Pessoa): # Herança: herda todos os atributos ou métodos
    olhos = 3 # sobrepõe o atributo na classe mutante com relação a Classe Py Pessoa
    # (sobrescrita de atributos de dados)

if __name__ == '__main__':
    Lorenzo = Mutante(nome = 'Lorenzo') # o objeto complexo "lorenzo" é do tipo pessoa,
    Silvana = Homem(Lorenzo, nome = 'Silvana') # e está passando ele para o atributo "Silvana"
    print(Pessoa.cumprimentar(Silvana)) # ao executar o "cumprimentar" pela classe "Pessoa" somos obrigados a passar o objeto como parâmetro, o que não acontece no método estático
    print(id(Silvana))
    print(Silvana.cumprimentar())
    print(Silvana.nome)
    print(Silvana.idade)
    for filho in Silvana.filhos: # para cada filho nos filhos deste objeto "Luciano" vou imprimir o filho.nome
        print(filho.nome)
    Silvana.sobrenome = 'Moreira'
    del Silvana.filhos
    Silvana.olhos = 1
    del Silvana.olhos
    print(Silvana.sobrenome)
    print(Silvana.__dict__) # mostra quais são os atributos de instância de cada objeto
    print(Lorenzo.__dict__)
    print(Pessoa.olhos)
    print(Silvana.olhos)
    print(Lorenzo.olhos)
    print(id(Pessoa.olhos), id(Silvana.olhos), id(Lorenzo.olhos))
    print(Pessoa.metodo_estatico(), Silvana.metodo_estatico())
    print(Pessoa.nome_e_atributo_de_classe(), Silvana.nome_e_atributo_de_classe())
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa)) #Objeto pessoa é uma instancia da classe Pessoa
    print(isinstance(pessoa, Homem))
    print(isinstance(Lorenzo, Pessoa))
    print(isinstance(Lorenzo, Homem)) # Homem pertence o tipo Pessoa
    print(Silvana.olhos)
    print(Silvana.cumprimentar())
    print(Lorenzo.cumprimentar())