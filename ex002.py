## %d valor numerico já o %s é uma string ##
nome = input("Digite seu nome: ")
sobren = input("Digite seu sobrenome: ")

## Solução 1

print("Seja Bem Vindo %s %s !" % (nome, sobren))

##solução 2

print("Seja Bem Vindo", nome, sobren)

##Solução 3

print("Seja Bem {} {}".format(nome, sobren))
