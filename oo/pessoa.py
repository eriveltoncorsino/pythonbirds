class Pessoa:
    olhos = 2
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
    Silvana.olhos = 1
    del Silvana.olhos
    print(Silvana.sobrenome)
    print(Silvana.__dict__) # mostra quais são os atributos de instância de cada objeto
    print(Lorenzo.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(Silvana.olhos)
    print(Lorenzo.olhos)
    print(id(Pessoa.olhos), id(Silvana.olhos), id(Lorenzo.olhos))




