#Desafio: Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado.
#Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função input(), 
#mas com uma validação de dados para aceitar apenas valores que sejam monetários.

from utilidadecev import moedas, dados
p = dados.leiaDinheiro('Digite o preço: R$ ')
moedas.resumo(p, 80, 35)
