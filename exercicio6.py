#Nossa empresa, a TechFix, trabalha com manutenção de computadores há 8 anos. Estamos crescendo muito e o controle manual não dá mais conta.
#A coisa funciona assim: o cliente chega com o computador com problema, a gente faz um orçamento primeiro. Se ele aprovar, fazemos o #serviço. Se não aprovar, cobramos uma taxa de avaliação de R$ 30.
#Temos vários tipos de serviço: formatação (R$ 80), limpeza geral (R$ 50), troca de peças (preço varia), remoção de vírus (R$ 60), #instalação de programas (R$ 40). Quando é troca de peça, além da mão de obra cobramos a peça com 30% de lucro em cima do preço de custo.
#Nosso estoque tem: memórias RAM, HDs, SSDs, fontes, placas de video... Preciso controlar o que entra e sai, e saber quando está acabando #para comprar mais.
#O maior problema é o acompanhamento dos equipamentos. O cliente quer saber: 'Em que fase está meu computador?'. Pode estar em análise, #aguardando orçamento, aguardando peça, em manutenção, testando, ou pronto para retirar.
#Também preciso de relatórios: quanto vendemos no mês, quais os defeitos mais comuns, qual técnico está mais produtivo, tempo médio de #reparo...
#Ah, e tem cliente que esquece de buscar o equipamento. Depois de 30 dias sem buscar, cobramos uma taxa de armazenamento de R$ 10 por dia.
#Os técnicos são eu, meu marido e mais dois funcionários. Cada um tem suas especialidades - alguns são melhores com hardware, outros com #software.
import datetime
from collections import defaultdict

SERVICOS = {
    "1": {"nome": "Formatação", "preco": 80.00, "tipo": "software"},
    "2": {"nome": "Limpeza Geral", "preco": 50.00, "tipo": "hardware"},
    "3": {"nome": "Troca de Peças", "preco_mao_obra": 40.00, "tipo": "hardware"},
    "4": {"nome": "Remoção de Vírus", "preco": 60.00, "tipo": "software"},
    "5": {"nome": "Instalação de Programas", "preco": 40.00, "tipo": "software"}
}

ESTOQUE = {
    "RAM_8GB": {"descricao": "Memória RAM 8GB", "preco_custo": 150.00, "quantidade": 10, "limite_min": 2},
    "HD_1TB": {"descricao": "HD 1TB", "preco_custo": 200.00, "quantidade": 5, "limite_min": 1},
    "SSD_500GB": {"descricao": "SSD 500GB", "preco_custo": 250.00, "quantidade": 8, "limite_min": 2},
    "FONTE_500W": {"descricao": "Fonte 500W", "preco_custo": 180.00, "quantidade": 3, "limite_min": 1},
    "PLACA_VIDEO": {"descricao": "Placa de Vídeo GTX 1650", "preco_custo": 800.00, "quantidade": 2, "limite_min": 1}
}

TECNICOS = {
    "1": {"nome": "Ana (Dona)", "especialidades": ["hardware", "software"]},
    "2": {"nome": "João (Marido)", "especialidades": ["hardware"]},
    "3": {"nome": "Pedro", "especialidades": ["software"]},
    "4": {"nome": "Maria", "especialidades": ["hardware", "software"]}
}

ESTADOS = ["analise", "aguardando_orcamento", "aguardando_peca", "em_manutencao", "testando", "pronto_retirada"]

ordens_servico = {}
clientes = {}
faturamento = defaultdict(float)
defeitos_comuns = defaultdict(int)
ordem_id_counter = 1

def mostrar_menu():
    print("\n--- TECHFIX - Manutenção de Computadores ---")
    print("1. Registrar novo equipamento (entrada de cliente)")
    print("2. Atualizar status de uma ordem")
    print("3. Ver status de uma ordem")
    print("4. Fazer/Aprovar orçamento")
    print("5. Gerenciar estoque (entrada/saída)")
    print("6. Ver relatórios")
    print("7. Sair")


def obter_data_atual():
    return datetime.datetime.now().strftime("%Y-%m-%d")


def calcular_taxa_armazenamento(data_entrada, data_atual):
    try:
        data_ent = datetime.datetime.strptime(data_entrada, "%Y-%m-%d")
        data_atu = datetime.datetime.strptime(data_atual, "%Y-%m-%d")
        dias = (data_atu - data_ent).days
        if dias > 30:
            return (dias - 30) * 10.00
        return 0.00
    except ValueError:
        return 0.00


def registrar_equipamento():
    global ordem_id_counter

    print("\n--- Registrar Novo Equipamento ---")

    cliente_nome = input("Nome do cliente: ")
    cliente_contato = input("Telefone/email do cliente: ")
    defeito = input("Descreva o defeito relatado: ")
    data_entrada = obter_data_atual()

    ordem_id = ordem_id_counter
    ordens_servico[ordem_id] = {
        "cliente_nome": cliente_nome,
        "cliente_contato": cliente_contato,
        "defeito": defeito,
        "data_entrada": data_entrada,
        "estado": "analise",
        "tecnico_id": None,
        "servicos": [],
        "pecas_usadas": [],
        "orcamento_total": 0.00,
        "aprovado": False,
        "data_aprovacao": None,
        "data_conclusao": None,
        "taxa_avaliacao": 0.00
    }
    ordem_id_counter += 1

    defeitos_comuns[defeito] += 1

    if cliente_nome not in clientes:
        clientes[cliente_nome] = []
    clientes[cliente_nome].append(ordem_id)

    print(f"\nEquipamento registrado com ID: {ordem_id}")
    print(f"Estado inicial: Análise")
    print("O técnico fará a análise e orçamento em breve.")


def atualizar_status(ordem_id):
    if ordem_id not in ordens_servico:
        print("Ordem não encontrada.")
        return

    ordem = ordens_servico[ordem_id]
    print(f"\nStatus atual: {ordem['estado']}")
    print("Novos estados possíveis:")
    for i, estado in enumerate(ESTADOS, 1):
        if estado != ordem['estado']:
            print(f"{i}. {estado.replace('_', ' ').title()}")

    try:
        escolha = int(input("Escolha o novo estado (número): "))
        novo_estado = ESTADOS[escolha - 1]
        if novo_estado == ordem['estado']:
            print("Estado já é o atual.")
            return
        ordem['estado'] = novo_estado

        if novo_estado == "pronto_retirada":
            ordem['data_conclusao'] = obter_data_atual()
            if ordem['aprovado']:
                total = ordem['orcamento_total']
                if ordem['tecnico_id']:
                    tecnico_nome = TECNICOS[ordem['tecnico_id']]['nome']
                    faturamento[tecnico_nome] += total
                print(f"Faturamento registrado: R${total:.2f}")

        taxa = calcular_taxa_armazenamento(ordem['data_entrada'], obter_data_atual())
        if taxa > 0:
            print(f"Aviso: Taxa de armazenamento devida: R${taxa:.2f}")

        print(f"Status atualizado para: {novo_estado.replace('_', ' ').title()}")
    except (ValueError, IndexError):
        print("Escolha inválida.")


def ver_status(ordem_id):
    if ordem_id not in ordens_servico:
        print("Ordem não encontrada.")
        return

    ordem = ordens_servico[ordem_id]
    data_atual = obter_data_atual()
    taxa = calcular_taxa_armazenamento(ordem['data_entrada'], data_atual)

    print(f"\n--- Status da Ordem {ordem_id} ---")
    print(f"Cliente: {ordem['cliente_nome']} ({ordem['cliente_contato']})")
    print(f"Defeito: {ordem['defeito']}")
    print(f"Data de Entrada: {ordem['data_entrada']}")
    print(f"Estado Atual: {ordem['estado'].replace('_', ' ').title()}")
    if ordem['tecnico_id']:
        tecnico_nome = TECNICOS[ordem['tecnico_id']]['nome']
        print(f"Técnico Atribuído: {tecnico_nome}")
    if ordem['aprovado']:
        print(f"Orçamento Aprovado: R${ordem['orcamento_total']:.2f}")
        print(f"Data de Aprovação: {ordem['data_aprovacao']}")
    else:
        print(f"Taxa de Avaliação (se rejeitado): R$30.00")
    if ordem['data_conclusao']:
        print(f"Data de Conclusão: {ordem['data_conclusao']}")
    if taxa > 0:
        print(f"Taxa de Armazenamento: R${taxa:.2f} (devido a mais de 30 dias)")
    print("Serviços/ Peças:")
    for serv in ordem['servicos']:
        print(f"- {serv['nome']}: R${serv['preco']:.2f}")
    for peca in ordem['pecas_usadas']:
        print(f"- {peca['nome']}: R${peca['preco']:.2f}")


def fazer_orcamento(ordem_id):
    if ordem_id not in ordens_servico:
        print("Ordem não encontrada.")
        return

    ordem = ordens_servico[ordem_id]
    if ordem['estado'] != "analise":
        print("Orçamento só pode ser feito na fase de análise.")
        return

    print("\nTécnicos disponíveis:")
    for id_t, tecnico in TECNICOS.items():
        espec = ", ".join(tecnico['especialidades'])
        print(f"{id_t}. {tecnico['nome']} (Especialidades: {espec})")
    tecnico_id = input("Escolha o técnico (número): ")
    if tecnico_id not in TECNICOS:
        print("Técnico inválido.")
        return
    ordem['tecnico_id'] = tecnico_id

    orcamento = 0.00
    while True:
        print("\nServiços disponíveis:")
        for id_s, serv in SERVICOS.items():
            print(f"{id_s}. {serv['nome']} (R${serv['preco']:.2f})" if 'preco' in serv else f"{id_s}. {serv['nome']} (Mão de obra R${serv['preco_mao_obra']:.2f} + peça)")
        escolha = input("Escolha serviço (ou 'fim' para finalizar): ")
        if escolha.lower() == 'fim':
            break
        if escolha in SERVICOS:
            serv = SERVICOS[escolha]
            if serv['nome'] == "Troca de Peças":
                print("\nEstoque disponível:")
                for id_e, item in ESTOQUE.items():
                    if item['quantidade'] > 0:
                        preco_venda = item['preco_custo'] * 1.30
                        print(f"{id_e}. {item['descricao']} (Custo: R${item['preco_custo']:.2f}, Venda: R${preco_venda:.2f}, Qtd: {item['quantidade']})")
                peca_id = input("Escolha a peça (ID): ")
                if peca_id in ESTOQUE and ESTOQUE[peca_id]['quantidade'] > 0:
                    peca = ESTOQUE[peca_id]
                    preco_peca = peca['preco_custo'] * 1.30
                    total_peca = preco_peca + serv['preco_mao_obra']
                    ordem['pecas_usadas'].append({"nome": peca['descricao'], "preco": total_peca})
                    peca['quantidade'] -= 1
                    if peca['quantidade'] <= peca['limite_min']:
                        print(f"Aviso: Estoque baixo para {peca['descricao']}!")
                    orcamento += total_peca
                else:
                    print("Peça inválida ou sem estoque.")
                    continue
            else:
                ordem['servicos'].append({"nome": serv['nome'], "preco": serv['preco']})
                orcamento += serv['preco']
        else:
            print("Serviço inválido.")

    ordem['orcamento_total'] = orcamento
    ordem['estado'] = "aguardando_orcamento"
    print(f"\nOrçamento total: R${orcamento:.2f}")
    print("Aguardando aprovação do cliente.")


def aprovar_orcamento(ordem_id):
    if ordem_id not in ordens_servico:
        print("Ordem não encontrada.")
        return

    ordem = ordens_servico[ordem_id]
    if ordem['estado'] != "aguardando_orcamento":
        print("Aprovação só na fase aguardando orçamento.")
        return

    aprovacao = input("O cliente aprovou? (s/n): ").lower()
    if aprovacao == 's':
        ordem['aprovado'] = True
        ordem['data_aprovacao'] = obter_data_atual()
        ordem['estado'] = "em_manutencao"
        print("Serviço aprovado! Iniciando manutenção.")
    else:
        ordem['taxa_avaliacao'] = 30.00
        ordem['estado'] = "pronto_retirada"
        ordem['data_conclusao'] = obter_data_atual()
        faturamento["Taxa Avaliação"] += 30.00
        print("Serviço rejeitado. Taxa de avaliação de R$30 cobrada.")


def gerenciar_estoque():
    print("\n--- Gerenciar Estoque ---")
    acao = input("1. Adicionar entrada | 2. Ver estoque | Escolha: ")
    if acao == "1":
        print("\nItens no estoque:")
        for id_e, item in ESTOQUE.items():
            print(f"{id_e}. {item['descricao']} (Atual: {item['quantidade']})")
        item_id = input("ID do item para adicionar: ")
        if item_id in ESTOQUE:
            qtd = int(input("Quantidade a adicionar: "))
            ESTOQUE[item_id]['quantidade'] += qtd
            print(f"Estoque atualizado: {ESTOQUE[item_id]['quantidade']}")
        else:
            print("Item inválido.")
    elif acao == "2":
        print("\n--- Estoque Atual ---")
        for item in ESTOQUE.values():
            status = "BAIXO" if item['quantidade'] <= item['limite_min'] else "OK"
            print(f"- {item['descricao']}: {item['quantidade']} unid. (Status: {status}) | Custo: R${item['preco_custo']:.2f}")


def relatorios():
    print("\n--- Relatórios ---")
    relatorio = input("1. Faturamento mensal | 2. Defeitos comuns | 3. Técnico mais produtivo | 4. Tempo médio de reparo | Escolha: ")

    mes_atual = datetime.datetime.now().month
    if relatorio == "1":
        total_mes = 0.00
        for tecnico, valor in faturamento.items():
            if "Taxa" not in tecnico:
                print(f"{tecnico}: R${valor:.2f}")
                total_mes += valor
        print(f"Total do Mês: R${total_mes:.2f}")
    elif relatorio == "2":
        print("\nDefeitos mais comuns:")
        for defeito, cont in sorted(defeitos_comuns.items(), key=lambda x: x[1], reverse=True):
            print(f"- {defeito}: {cont} casos")
    elif relatorio == "3":
        produtivo = max(faturamento, key=faturamento.get) if faturamento else "Nenhum"
        print(f"Técnico mais produtivo: {produtivo} (R${faturamento[produtivo]:.2f})")
    elif relatorio == "4":
        tempos = []
        for ordem in ordens_servico.values():
            if ordem['data_conclusao']:
                try:
                    ent = datetime.datetime.strptime(ordem['data_entrada'], "%Y-%m-%d")
                    conc = datetime.datetime.strptime(ordem['data_conclusao'], "%Y-%m-%d")
                    dias = (conc - ent).days
                    tempos.append(dias)
                except ValueError:
                    pass
        if tempos:
            media = sum(tempos) / len(tempos)
            print(f"Tempo médio de reparo: {media:.1f} dias ({len(tempos)} reparos)")
        else:
            print("Nenhum reparo concluído.")


def rodar_aplicativo():
    while True:
        mostrar_menu()
        escolha = input("Digite sua opção: ")

        if escolha == "1":
            registrar_equipamento()
        elif escolha == "2":
            try:
                oid = int(input("ID da ordem: "))
                atualizar_status(oid)
            except ValueError:
                print("ID inválido.")
        elif escolha == "3":
            try:
                oid = int(input("ID da ordem: "))
                ver_status(oid)
            except ValueError:
                print("ID inválido.")
        elif escolha == "4":
            sub = input("1. Fazer orçamento | 2. Aprovar orçamento | Escolha: ")
            try:
                oid = int(input("ID da ordem: "))
                if sub == "1":
                    fazer_orcamento(oid)
                elif sub == "2":
                    aprovar_orcamento(oid)
            except ValueError:
                print("ID inválido.")
        elif escolha == "5":
            gerenciar_estoque()
        elif escolha == "6":
            relatorios()
        elif escolha == "7":
            print("Obrigado por usar o sistema da TechFix! Até mais.")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")


if __name__ == "__main__":
    rodar_aplicativo()
