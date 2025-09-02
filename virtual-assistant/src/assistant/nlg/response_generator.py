from typing import List, Dict  # Importa tipos para anotações
import re  # Importa expressões regulares para busca de palavras

# Classe responsável por identificar intenções a partir do texto do usuário
class IntentParser:
    def __init__(self):
        # Dicionário de intenções com palavras-chave em Português
        self.intents = {
            "saudacao": ["olá", "ola", "oi", "bom dia", "boa tarde", "boa noite"],  # Intenção de saudação
            "despedida": ["tchau", "adeus", "até logo", "até mais"],  # Intenção de despedida
            "agradecimento": ["obrigado", "obrigada", "valeu", "agradeço"],  # Intenção de agradecimento
            "ajuda": ["ajuda", "socorro", "pode me ajudar", "como faço", "como posso"]  # Intenção de pedido de ajuda
        }

    # Método para identificar a intenção a partir do texto do usuário
    def parse_intent(self, user_input: str) -> str:
        user_input = user_input.lower()  # Converte o texto para minúsculas
        for intent, keywords in self.intents.items():  # Itera sobre as intenções e palavras-chave
            for keyword in keywords:  # Itera sobre cada palavra-chave
                # Verifica se a palavra-chave está presente no texto do usuário
                if re.search(r'\b' + re.escape(keyword) + r'\b', user_input):
                    return intent  # Retorna a intenção correspondente
        return "desconhecido"  # Retorna "desconhecido" se nenhuma intenção for encontrada

    # Retorna a lista de intenções conhecidas
    def get_intents(self) -> List[str]:
        return list(self.intents.keys())  # Retorna as chaves do dicionário como lista

    # Adiciona uma nova intenção ou atualiza uma existente
    def add_intent(self, intent: str, keywords: List[str]) -> None:
        self.intents[intent] = keywords  # Adiciona ou atualiza a intenção no dicionário

    # Remove uma intenção existente
    def remove_intent(self, intent: str) -> None:
        if intent in self.intents:  # Verifica se a intenção existe
            del self.intents[intent]  # Remove a intenção do dicionário