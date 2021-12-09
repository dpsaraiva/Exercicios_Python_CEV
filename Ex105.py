#Desafio: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
# Quantidade de notas;
# A maior nota;
# A menor nota;
# A média da turma;
# A situação(opcional).
# Adicione também as docstrings da função.

def notas(*num, sit=False):
    '''
    -> Função para analisar notas e situação de vários alunos
    :param num: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    '''

    aluno = {}
    situacao = ''
    aluno['total'] = len(num)
    aluno['maior'] = max(num)
    aluno['menor'] = min(num)
    aluno['média'] = sum(num) / len(num)
    if sit == True:
        if aluno['média'] < 5:
            aluno['situação'] = 'RUIM'
        elif aluno['média'] < 7:
            aluno['situação'] = 'RAZOÁVEL'
        else:
            aluno['situação'] = 'BOA'
    return aluno


#Programa Principal
resp = notas(2.7, 5, 7.4, 6.2, 5, sit=True)
print(resp)
help(notas)
