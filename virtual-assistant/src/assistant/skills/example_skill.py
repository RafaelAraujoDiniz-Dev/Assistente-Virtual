from assistant.core import Assistant

# Define a classe ExampleSkill, que representa uma habilidade do assistente
class ExampleSkill:
    def __init__(self):
        # Define o nome da habilidade
        self.name = "Habilidade Exemplo"

    # Método principal que executa a habilidade com base no comando recebido
    def execute(self, command):
        # Normaliza o comando para minúsculas
        command = command.lower()

        # Verifica se o comando é uma saudação
        if command in ["olá", "ola", "oi"]:
            return "Olá! Como posso ajudar você hoje?"  # Retorna uma saudação
        # Verifica se o comando é uma despedida
        elif command in ["tchau", "adeus"]:
            return "Tchau! Tenha um ótimo dia!"  # Retorna uma despedida
        # Caso o comando não seja reconhecido
        else:
            return "Desculpe, não entendi o que você quis dizer."  # Resposta padrão para comandos desconhecidos