usuario = "python"
senha  = "123"

usuarioDigitado = input("Digite seu usário: ")
senhaDigitada = input("Digite sua senha: ")

if usuarioDigitado == usuario and senhaDigitada == senha:
    print("Login realizado com sucesso!")
else:
    if usuarioDigitado == usuario and senhaDigitada != senha:
        print("Sua senha está incorreta!")
    elif usuarioDigitado != usuario and senhaDigitada == senha:
        print("Usuário incorreto!")
    else:
        print("Usuário e senha incorretos.")