#Olá, eu tenho uma barbearia há 15 anos e está ficando difícil controlar tudo no papel. Preciso de um sistema para organizar minha vida #aqui.
#Olha, eu tenho 3 barbeiros trabalhando comigo, incluindo eu. Cada um tem seus horários diferentes eu trabalho de segunda a sábado, o Carlos #só de terça a sexta, e o Miguel nos finais de semana. Os clientes sempre ligam perguntando se tem horário livre e eu fico perdido olhando #na #agenda de papel.
#Queria que os clientes pudessem agendar pelo computador, sabe? Escolher o barbeiro, o dia, o horário... Mas também preciso que eles vejam #os preços dos serviços. Aqui fazemos corte simples (R$ 25), corte + barba (R$ 35), barba completa (R$ 20), e corte social (R$ 30).
#Ah, e tem uma coisa importante: alguns clientes são meio esquecidos, então seria bom mandar um lembrete por WhatsApp ou email no dia #anterior.
#Também preciso ver quanto cada barbeiro está faturando no mês, porque pago comissão para eles. E seria legal ter um histórico dos #clientes - quando vieram pela última vez, qual serviço fizeram...
#Às vezes cancelam em cima da hora também, aí o horário fica perdido. Preciso conseguir reagendar rápido.

import datetime

SERVICOS = {
    "1": {"nome": "Corte Simples", "preco": 25.00},
    "2": {"nome": "Corte + Barba", "preco": 35.00},
    "3": {"nome": "Barba Completa", "preco": 20.00},
    "4": {"nome": "Corte Social", "preco": 30.00}
}

BARBEIROS = {
    "1": {"nome": "João", "dias_trabalho": ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]},
    "2": {"nome": "Carlos", "dias_trabalho": ["Terça", "Quarta", "Quinta", "Sexta"]},
    "3": {"nome": "Miguel", "dias_trabalho": ["Sábado", "Domingo"]}
}

agendamentos = {}
clientes = {}
faturamento_barbeiros = {
    "João": 0.0,
    "Carlos": 0.0,
    "Miguel": 0.0
}
agendamento_id_counter = 1


def mostrar_menu():
    print("\n--- BARBEARIA DO JOE ---")
    print("1. Agendar um serviço")
    print("2. Ver serviços e preços")
    print("3. Ver barbeiros disponíveis")
    print("4. Ver faturamento de barbeiros")
    print("5. Sair do aplicativo")


def obter_dia_da_semana(data_str):
    try:
        data_obj = datetime.datetime.strptime(data_str, "%Y-%m-%d")
        dias_da_semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
        return dias_da_semana[data_obj.weekday()]
    except ValueError:
        return None


def agendar_servico():
    global agendamento_id_counter

    print("\n--- Agendar Serviço ---")

    cliente_nome = input("Digite seu nome: ")
    cliente_contato = input("Digite seu telefone/email para o lembrete: ")

    print("Barbeiros:")
    for id_b, barbeiro in BARBEIROS.items():
        print(f"{id_b}. {barbeiro['nome']}")
    barbeiro_id = input("Escolha o número do barbeiro: ")

    if barbeiro_id not in BARBEIROS:
        print("Barbeiro não encontrado. Por favor, tente novamente.")
        return

    barbeiro_nome = BARBEIROS[barbeiro_id]["nome"]

    data = input("Digite a data (ex: 2025-05-15): ")

    dia_da_semana = obter_dia_da_semana(data)
    if not dia_da_semana:
        print("Formato de data inválido. Por favor, use YYYY-MM-DD.")
        return

    if dia_da_semana not in BARBEIROS[barbeiro_id]["dias_trabalho"]:
        print(f"{barbeiro_nome} não trabalha em {dia_da_semana}. Por favor, escolha outro dia ou barbeiro.")
        return

    hora = input("Digite a hora (ex: 14:30): ")

    print("\nServiços:")
    for id_s, servico in SERVICOS.items():
        print(f"{id_s}. {servico['nome']} (R${servico['preco']:.2f})")
    servico_id = input("Escolha o número do serviço: ")

    if servico_id not in SERVICOS:
        print("Serviço não encontrado. Por favor, tente novamente.")
        return

    agendamento_id = agendamento_id_counter
    agendamentos[agendamento_id] = {
        "cliente_nome": cliente_nome,
        "cliente_contato": cliente_contato,
        "barbeiro_id": barbeiro_id,
        "servico_id": servico_id,
        "data": data,
        "hora": hora
    }
    agendamento_id_counter += 1

    servico_preco = SERVICOS[servico_id]["preco"]
    faturamento_barbeiros[barbeiro_nome] += servico_preco

    if cliente_nome not in clientes:
        clientes[cliente_nome] = {"contato": cliente_contato, "historico": []}

    clientes[cliente_nome]["historico"].append({
        "data": data,
        "servico": SERVICOS[servico_id]["nome"],
        "barbeiro": barbeiro_nome
    })

    print("\nAgendamento realizado com sucesso!")
    print(f"Detalhes do agendamento:")
    print(f"Barbeiro: {barbeiro_nome}")
    print(f"Serviço: {SERVICOS[servico_id]['nome']}")
    print(f"Data e Hora: {data} às {hora}")
    print("\nUm lembrete será enviado 24h antes!")


def mostrar_servicos():
    print("\n--- Serviços e Preços ---")
    for servico in SERVICOS.values():
        print(f"- {servico['nome']}: R${servico['preco']:.2f}")


def mostrar_barbeiros():
    print("\n--- Barbeiros ---")
    for barbeiro in BARBEIROS.values():
        dias = ", ".join(barbeiro["dias_trabalho"])
        print(f"- {barbeiro['nome']}: Trabalha de {dias}")


def mostrar_faturamento():
    print("\n--- Faturamento de Barbeiros (Mês) ---")
    for nome, valor in faturamento_barbeiros.items():
        print(f"{nome}: R${valor:.2f}")


def rodar_aplicativo():
    while True:
        mostrar_menu()
        escolha = input("Digite sua opção: ")

        if escolha == "1":
            agendar_servico()
        elif escolha == "2":
            mostrar_servicos()
        elif escolha == "3":
            mostrar_barbeiros()
        elif escolha == "4":
            mostrar_faturamento()
        elif escolha == "5":
            print("Obrigado por usar o sistema da Barbearia do Joe! Até mais.")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")


if __name__ == "__main__
    rodar_aplicativo()