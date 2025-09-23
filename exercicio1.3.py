#Aplicação de vacina
#1. Cadastrar nome da vacina.
#2. Aplicar dose (retirar 1; checar disponibilidade).
#3. Receber lote de doses (quantidade > 0).
#4. Ver doses em estoque.

def menu_vacina():
    print('\n---Aplicação de vacina---')
    print('1 - Cadastrar vacina')
    print('2 - Aplicar dose')
    print('3 - Receber lote de doses')
    print('4 - Ver doses em estoque')
    print('0 - Sair')
    return input('Escolha uma opção: ')

vacina = None
doses = 0

while True:
    opcao = menu_vacina()
    if opcao == '1':
        vacina = input('Digite o nome do vacina: ')
        doses = 0
        print('Vacina Cadastrada com sucesso!')

    elif opcao == '2':
        if vacina is None:
            print('Nenhum vacina cadastrada ainda!')
        elif doses <= 0:
            print('Não há doses disponívies para aplicação')
        else:
            doses -= 1
            print('Dose aplicada com sucesso!')

    elif opcao == '3':
        if vacina is None:
            print('Nenhum vacina cadastrada ainda!')
        else:
            recebidas = int(input('Digite a quantidade de doses recebidas: '))
            if recebidas <= 0:
                print('A quantidade deve ser maior que zero!')
            else:
                doses += recebidas
                print(f'lote recebido: {recebidas} doses')

    elif opcao == '4':
        if vacina is None:
            print('Nenhum vacina cadastrada ainda!')
        else:
            print(f'Vacina: {vacina}. Doses em estoque: {doses}')

    elif opcao == '0':
        print('Saindo...')
        break

    else:
        print('Digite uma opção válida!')