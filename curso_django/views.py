'''
Favor colocar os nomes das importações em ordem alfabética para uma melhor organização
'''

from django.http import HttpResponse

def hello(request):
    return HttpResponse('Hello, World!')

def articles(request, year=None):
    return HttpResponse('O ano enviado foi {}'.format(year))

def ler_do_banco(nome):
    lista_nomes = [
        {'nome': 'Ana', 'idade': 20},
        {'nome': 'Pedro', 'idade': 25},
        {'nome': 'João', 'idade': 37},
        {'nome': 'Maria', 'idade': 37},
    ]

    for pessoa in lista_nomes:
        if pessoa['nome'] == nome:
            return pessoa
    
    return {'nome': 'Não encontrado', 'idade': 0}

def fname(request, nome):
    result = ler_do_banco(nome)
    if result['idade'] > 0:
        return HttpResponse('A pessoa foi encontrada, ela tem {} anos.'.format(result['idade']))
    else:
        return HttpResponse('Pessoa não encontrada')