a = 'A'
b = 'B'
c = 1.1
string = 'a{} b{} c={:.2f}'
formato = string.format(a,b,nome3=c)

print(formato)


#obs1

#se vc quiser puxar duas vezes ou mais o valor de cada variavel, pode usar indices e nao 
# e nao depender de da sequncia ja estipulada a,b,c. Como por exemplo

#a = 'A'
#b = 'B'
#c = 1.1
#string = 'a{0} b{1} c={2:.2f}'
#formato = string.format(a,b,c)
#print(formato)

# agora, colocando as sequencias de 0,1 e 2, vc pode colocar quantas vezes quiser o valor de A, b OU C
# string = 'a{0} a{0} a{0} b{1} c{2:.2f}
# isso vai mostrar o valor de a 3 vezes


#obs 2 

# em python se chama parametro nomeado, quando eu dou uym nome para as coisas da criacao das funcoes
# string = 'a{} b{} c={nome3:.2f}'
# formato = string.format(a,b,nome3=c), o nome3 eh o parametro nomeado e o valor c eh o argumento
# e detalhe tudo que tiver depois do parametro nomeado tambem deve ser nomeado
# como por ex: formato = string.format(a,nome2=b,nome3=c, nesse caso se nomear o 2 tem que nomear tbm o 3

#obs3
#tudo em py eh um objeto e quando uma funcao esta dentro de um objeto ela eh chamada de metodo