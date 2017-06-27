#registro
logr = input("Digite nome de Login: ")
passr= input("Digite uma senha: ")

#login
print("Cadastro realizado com suceso")
a = int(input("Digite 1 para continuar: "))

if(a ==1):
    print("Digite login e senha")
    print()
    logl= input("Digite seu Login: ")
    passl= input("digite sua Senha:")
    while logr != logl:
        print("login incorreto, tente novamente")
        logl = input("Digite seu novamente Login: ")
    while passr!= passl:
        print("senha incorreta, tente Novamente")
        passl = input("digite sua novamente Senha: ")
    print()
    print("Logado com sucesso")
else:
    print("Você fechou o sistema")


