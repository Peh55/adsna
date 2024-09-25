login = input('Login: ').strip()
senha = input('Senha: ').strip()

acesso = False

if login == 'admin' and senha == 'admin':
    acesso = True


if acesso:
    print("Bem vindo ao seu perfil")