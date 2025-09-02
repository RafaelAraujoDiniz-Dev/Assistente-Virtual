# Arquivo de execução do assistente — ponto de entrada para iniciar a aplicação
# Importa o módulo sys (pode ser usado para argumentos de linha de comando ou saída)
import sys  # importa funcionalidades do sistema operacional (argv, exit, etc.)

# Importa a classe Assistant do módulo principal do assistente
from src.assistant.main import Assistant  # caminho para a classe principal que controla o assistente

# Define a função main, que inicia o assistente quando o script for executado
def main():
    # Cria uma instância da classe Assistant
    assistant = Assistant()  # instancia o assistente virtual
    # Chama o método que inicia o comportamento principal do assistente
    assistant.start()  # inicia o loop / rotina do assistente

# Verifica se o script está sendo executado diretamente (não importado como módulo)
if __name__ == "__main__":
    # Executa a função main para iniciar a aplicação
    main()  # inicia o assistente ao