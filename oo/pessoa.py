class Pessoa:
    def __init__(self, *filhos, nome=None, idade=55): # * filhos quer dizer uma quantidade variável de filhos
        self.idade = idade
        self.nome = nome
        self.filhos = list (filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    Lorenzo = Pessoa(nome ='Lorenzo') # o objeto complexo "lorenzo" é do tipo pessoa,
    Silvana = Pessoa(Lorenzo, nome='Silvana') # e está passando ele para o atributo "Silvana"
    print(Pessoa.cumprimentar(Silvana))
    print(id(Silvana))
    print(Silvana.cumprimentar())
    print(Silvana.nome)
    print(Silvana.idade)
    for filho in Silvana.filhos: # para cada filho nos filhos deste objeto "Luciano" vou imprimir o filho.nome
        print(filho.nome)
    Silvana.sobrenome = 'Moreira'
    del Silvana.filhos
    print(Silvana.sobrenome)
    print(Silvana.__dict__)
    print(Lorenzo.__dict__)


