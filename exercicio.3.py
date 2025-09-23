#sistema de login
#não tinha mais o enunciado


class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

lista_de_usuarios = []


def criar_usuario(nome, email, senha):
    for usuario in lista_de_usuarios:
        if usuario.email == email:
            print('Erro: O e-mail já está em uso.')
            return None

    return Usuario(nome, email, senha)


def adicionar_usuario():
    nome = input("Digite seu nome: ")
    email = input("Digite o email: ")
    senha = input("Digite a senha: ")

    novo_usuario = criar_usuario(nome, email, senha)
    if novo_usuario:
        lista_de_usuarios.append(novo_usuario)
        print('Usuário adicionado com sucesso!')
    else:
        print('Falha ao adicionar usuário.')


def pesquisar_nome_por_email():
    email_pesquisa = input('Digite o e-mail que deseja pesquisar: ')
    for usuario in lista_de_usuarios:
        if usuario.email == email_pesquisa:
            print(f'Nome encontrado: {usuario.nome}.')
            return
    print('Nenhum nome encontrado.')


def fazer_login():
    email_login = input('Digite o e-mail para login: ')
    senha_login = input('Digite a senha para login: ')
    for usuario in lista_de_usuarios:
        if usuario.email == email_login and usuario.senha == senha_login:
            print(f'Login bem sucedido! Bem vindo(a), {usuario.nome}.')
            return True
    print('E-mail ou senha incorretos.')
    return False


def menu():
    while True:
        print("\n--- Menu ---")
        print("1 - Criar usuário")
        print("2 - Fazer login")
        print("3 - Pesquisar nome por e-mail")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_usuario()
        elif opcao == '2':
            fazer_login()
        elif opcao == '3':
            pesquisar_nome_por_email()
        elif opcao == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")
menu()