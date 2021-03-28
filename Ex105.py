def notas(*num, sit=False):
    '''
    -> Função para analisar notas e situação de vários alunos
    :param num: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    '''


    media = soma = maior = menor = total = 0
    aluno = {}
    situacao = ''
    for i in num:
        total += 1
        if total == 1:
            maior = i
            menor = maior
        else:
            if maior < i:
                maior = i
            if menor > i:
                menor = i
        soma += i
    media = soma / total
    aluno['total'] = total
    aluno['maior'] = maior
    aluno['menor'] = menor
    aluno['média'] = media
    if sit == True:
        if media < 5:
            situacao = 'RUIM'
        elif media < 7:
            situacao = 'RAZOÁVEL'
        else:
            situacao = 'BOA'
        aluno['situação'] = situacao
    print(aluno)

resp = notas(2.7, 5, 7.4, 6.2, 5, sit=True)
help(notas)
