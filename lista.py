# Definir uma classe para armazenar os dados dos eventos
class Evento:
    def __init__(self, descricao, gravidade):
        self.descricao = descricao
        self.gravidade = gravidade


# Função principal
def encontrar_eventos_criticos(eventos):
    # Criar uma lista para armazenar os eventos críticos encontrados
    eventos_criticos = []

    # Iterar sobre a lista de eventos
    for evento in eventos:
        # Verificar se o evento é de segurança e tem gravidade "CRÍTICO"
        if evento.gravidade == "CRÍTICO":
            # Adicionar o evento à lista de eventos críticos
            eventos_criticos.append(evento)

    # Exibir os eventos críticos encontrados
    if len(eventos_criticos) > 0:
        print("Eventos de Segurança com Gravidade CRÍTICO:\n")
        for evento in eventos_criticos:
            print(f"Descrição: {evento.descricao}")
    else:
        print("Nenhum evento de segurança com gravidade CRÍTICO encontrado.")

# Exemplo de uso
if __name__ == "__main__":
    # Definir uma lista de eventos (simulada)
    eventos = [
        Evento("Evento 1", "ALTO"),
        Evento("Evento 2", "CRÍTICO"),
        Evento("Evento 3", "MÉDIO"),
        Evento("Evento 4", "CRÍTICO"),
        Evento("Evento 5", "BAIXO")
    ]

    # Chamar a função para encontrar e exibir eventos críticos
    encontrar_eventos_criticos(eventos)
