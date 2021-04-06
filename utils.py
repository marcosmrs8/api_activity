from models import Pessoas


def insere_pessoas():
    pessoa = Pessoas(nome='Rodrigo', idade=22)
    print(pessoa)
    pessoa.save()


def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)
    pessoa = Pessoas.query.filter_by(nome='Rodrigo').first()
    print(pessoa.idade)


def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Rafael').first()
    pessoa.nome = 'Roberto'
    pessoa.save()


def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Rodrigo').first()
    pessoa.delete()


if __name__ == '__main__':
    # insere_pessoas()
    # altera_pessoa()
    exclui_pessoa()
    consulta_pessoas()
