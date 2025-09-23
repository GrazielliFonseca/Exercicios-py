#Criar Usuário:
#Nome do usuário.
#E-mail do usuário (único).
#Cada usuário pode criar várias publicações.
#Criar Publicação (associada a um usuário):
#Conteúdo da publicação (somente texto por #enquanto).
#Descrição (opcional).
#Autor da publicação (usuário que criou).
#Data e hora da publicação.
#Contador de curtidas.
#Lista de comentários associados.
#Curtir Publicação:
#Incrementar contador de curtidas.
#Checar se o usuário já curtiu (não permitir #duplicidade)
#Comentar Publicação:
#Usuário autor do comentário.
#Texto do comentário.
#Data e hora do comentário.
#Associar comentário à publicação escolhida.
#Visualizar Feed (com relacionamentos): 1.
#Exibir todas as publicações disponíveis.
#Mostrar: autor, conteúdo, curtidas, e número de #comentar
#Ordenar pelas mais recentes.
#Visualizar Publicação Individual:
#Exibir todo o conteúdo da publicação.
#Mostrar autor, descrição, data/hora, número de #curtidas,
#lista detalhada de comentários.
#Mostrar detalhes dos autores dos comentários.
#Visualizar Perfil de Usuário:
#Exibir informações básicas do usuário.
#Listar todas as publicações criadas por ele.
#Mostrar total de curtidas em suas publicações.

from datetime import datetime

class Usuario:
    def __init__(self,nome, email):
        self.nome = nome
        self.email = email
        self.publicacoes = []

class Publicacao:
    def __init__(self, autor, conteudo, descricao=None ):
        self.autor = autor
        self.conteudo = conteudo
        self.descricao = descricao
        self.data_hora = datetime.now()
        self.curtidas = 0
        self.comentarios = []
        self.usuarios_que_curtiram = set()

class Comentario:
    def __init__(self,autor, texto ):
        self.autor = autor
        self.texto = texto
        self.data_hora = datetime.now()

def criar_publicacao(usuario, conteudo, descricao):
    pub = Publicacao(usuario, conteudo, descricao)
    usuario.publicacoes.append(pub)
    return pub

def curtir_publicacao(usuario, publicacao):
    if usuario.email in publicacao.usuarios_que_curtiram:
        print(f'{usuario.nome} já curtiu esta publicação.')
        return
    publicacao.curtidas += 1
    publicacao.usuarios_que_curtiram.add(usuario.email)
    print(f'{usuario.nome} curtiu a publicação.')

def comentar_publicacao(usuario, publicacao, texto):
    comentario = Comentario(usuario, texto)
    publicacao.comentarios.append(comentario)
    print(f'{usuario.nome} coementou na publicação.')

def visualizar_feed(publicacoes):
    if not publicacoes:
        print('Nenhuma publicação disponível.')
        return
    publicacoes_ordenadas = sorted(publicacoes, key=lambda publicacao: publicacao.data_hora, reverse=True)
    for i, pub in enumerate(publicacoes_ordenadas, 1):
        print(f'{i}. Autor: {pub.autor.nome}')
        print(f'Conteudo: {pub.conteudo}')
        print(f'Curtidas: {pub.curtidas}')

        if pub.comentarios:
            print('Comentários:')
            for comentario in pub.comentarios:
                print(f'- {comentario.autor.nome}: {comentario.texto}')
                print(f'Data hora: {comentario.data_hora.strftime("%d/%m/%Y %H:%M:%S")}')
        else:
            print('Nenhum comentário foi feito.')

    print(f'Data da Publicação: {pub.data_hora.strftime('%d/%m/%Y %H:%M:%S')}')
    print('-' * 30)

def visualizar_publicacao(publicacao):
    print(f'Autor: {publicacao.autor.nome}')
    if publicacao.descricao:
        print(f'Descrição: {publicacao.descricao}')
    print(f'Conteúdo: {publicacao.conteudo}')
    print(f'Data/Hora: {publicacao.data_hora.strftime('%d/%m/%Y %H:%M:%S')}')
    print(f'Curtidas: {publicacao.curtidas}')
    if publicacao.comentarios:
         print('Comentários:')
         for c in publicacao.comentarios:
            print(f'- {c.autor.nome} ({c.data_hora.strftime('%d/%m/%Y %H:%M:%S')}): {c.texto}')
    else:
        print('Nenhum comentário foi feito.')

def visualizar_perfil(usuario):
    print(f'Usuário: {usuario.nome}')
    print(f'Email: {usuario.email}')
    print(f'Publicações: ({len(usuario.publicacoes)}):')
    total_curtidas = 0
    for pub in usuario.publicacoes:
        print(f'- {pub.conteudo} (curtidas: {pub.curtidas}, comentarios: {len(pub.comentarios)}):')
        total_curtidas += pub.curtidas
    print(f'- Total de curtidas em todas as publicações: {total_curtidas}')

def encontrar_usuario_por_email(usuarios, email):
    for u in usuarios:
        if u.email == email:
            return u
    return None

def encontrar_usuario_por_nome(usuarios, nome):
    for u in usuarios:
        if u.nome.lower() == nome.lower():
            return u
    return None

def escolher_publicacao(publicacoes):
    if not publicacoes:
        print('Nenhuma publicação disponível.')
        return None
    print('Escolha uma publicação pelo número: ')
    for i, pub in enumerate(publicacoes, 1):
        print(f'{i}. Autor: {pub.autor.nome}')
    try:
        escolha = int(input())
        if 1 <= escolha <= len(publicacoes):
            return publicacoes[escolha - 1]
        else:
            print('Número invalido.')
            return None
    except ValueError:
        print('Entrada invalida.')
        return None

def menu():
    usuarios = []
    publicacoes = []

    while True:
        print('\n--- MENU ---')
        print('1. Criar usuário')
        print('2. Criar Publicação')
        print('3. Curtir publicação')
        print('4. Comentar Publicação')
        print('5. Visualizar feed')
        print('6. Visualizar publicação individual')
        print('7. Visualizar perfil de usuário')
        print('0. Sair')
        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            nome = input('Nome do usuário: ').strip()
            email = input('E-mail do usuário: ').strip()
            if encontrar_usuario_por_email(usuarios, email):
                print('E-mail já cadastrado.')
            else:
                usuarios.append(Usuario(nome, email))
                print(f'Usuário {nome} criado com sucesso.')

        elif opcao == '2':
            nome_autor = input('Nome do autor da publicação: ').strip()
            usuario = encontrar_usuario_por_nome(usuarios, nome_autor)
            if not usuario:
                print('Usuário não encontrado.')
                continue
            conteudo = input('Conteúdo da publicação: ').strip()
            descricao = input('Descrição: ').strip()
            descricao = descricao if descricao else None
            pub = criar_publicacao(usuario, conteudo, descricao)
            publicacoes.append(pub)
            print('Publicação criada com sucesso.')

        elif opcao == "3":
            nome_curtiu = input("Nome do usuário que vai curtir: ").strip()
            usuario = encontrar_usuario_por_nome(usuarios, nome_curtiu)
            if not usuario:
                print("Usuário não encontrado.")
                continue
            pub = escolher_publicacao(publicacoes)
            if pub:
                curtir_publicacao(usuario, pub)

        elif opcao == "4":
            nome_comentou = input("Nome do usuário que vai comentar: ").strip()
            usuario = encontrar_usuario_por_nome(usuarios, nome_comentou)
            if not usuario:
                print("Usuário não encontrado.")
                continue
            pub = escolher_publicacao(publicacoes)
            if pub:
                texto = input("Texto do comentário: ").strip()
                comentar_publicacao(usuario, pub, texto)

        elif opcao == "5":
            visualizar_feed(publicacoes)

        elif opcao == "6":
            pub = escolher_publicacao(publicacoes)
            if pub:
                visualizar_publicacao(pub)

        elif opcao == "7":
            nome_perfil = input("Nome do usuário: ").strip()
            usuario = encontrar_usuario_por_nome(usuarios, nome_perfil)
            if usuario:
                print(f'\nUsuário: {usuario.nome}')
                print(f'Publicações: ({len(usuario.publicacoes)}):')
                total_curtidas = 0
                for pub in usuario.publicacoes:
                    print(f'- {pub.conteudo} (curtidas: {pub.curtidas}, comentários: {len(pub.comentarios)})')
                    total_curtidas += pub.curtidas
                print(f'Total de curtidas em todas as publicações: {total_curtidas}')
            else:
                print("Usuário não encontrado.")

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == '__main__':
    menu()