#Bilheteria de evento com apenas 1 evento
#1. Cadastrar nome do evento.
#2. Vender ingressos (verificar se há ingressos suficientes).
#3. Repor ingressos (quantidade > 0).
 #4. Ver ingressos disponíveis.

def menu_bilheteria():
    print('\n---Bilheteria de Evento---')
    print('1 - Cadastrar um evento')
    print('2 - Vender ingressos')
    print('3 - Repor ingressos disponivéis')
    print('4 - Ver ingressos disponiveis')
    print('0 - Sair')
    opcao = input('Escolha uma opção: ')
    return opcao

evento = None
ingressos = 0

while True:
    opcao = menu_bilheteria()
    if opcao == '1':
        evento = input('\nDigite o nome do evento: ')
        ingressos = 0
        print(f'Evento {evento} cadastrado com sucesso! ')

    elif opcao == '2':
        if evento is None :
            print('Nenhum evnto cadastrado foi encontrado!')
        else:
            vender = int(input('Digite a quantidade de ingressos: '))
            if vender <= 0:
                print('A quantidade deve ser maior que zero!')
            elif vender > ingressos:
                print('Ingressos insuficientes!')
            else:
                print(f'Vendidos(a) {vender} ingresso(s). Restam ingresso(s).')
    elif opcao == '3':
        if evento is None :
            print('Nenhum evento cadastrado foi encontrado!')
        else:
            repor = int(input('Digite a quantidade de ingressos a repor: '))
            if repor <= 0:
                print('A quantidade deve ser maior que zero!')
            else:
                ingressos += repor
                print(f'Repor(s) {repor} ingresso(s).Total disponível(s): {ingressos}.')
    elif opcao == '4':
        if evento is None :
            print('Nenhum evento cadastrado foi encontrado!')
        else:
            print(f'Evento: {evento}.Ingressos diponíveis: {ingressos}.')
    elif opcao == '0':
        print('Saindo...')
        break
    else:
        print('Opção inválida! Tente novamente!')