admin =(input("Digite o nome do administrador: "))
senha =(input("Digite a senha: "))

if admin == "João" or admin == "Maria" or admin == "Pedro":
    print("Bem-vindo, ", admin)
    if senha == "1234":
        print("Acesso concedido.")  

    else:
        print("Senha ou Administrador incorretos. Acesso negado.")

else:
    print("Senha ou Administrador incorretos. Acesso negado.")