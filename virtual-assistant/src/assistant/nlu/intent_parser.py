# Importa tipos e módulos necessários
from typing import List, Dict  # anotações de tipo para listas e dicionários
import re  # expressões regulares para busca de palavras
import unicodedata  # utilitário para normalizar/accentuação

# Classe que faz o parse da intenção a partir do texto do usuário
class IntentParser:  # definicao da classe IntentParser
    def __init__(self):  # construtor chamado ao instanciar a classe
        # Dicionário de intenções com palavras-chave em Português
        self.intents: Dict[str, List[str]] = {  # mapeia nome_da_intencao -> lista de palavras-chave
            "saudacao": ["olá", "ola", "oi", "bom dia", "boa tarde", "boa noite"],  # saudações
            "despedida": ["tchau", "adeus", "até logo", "até mais", "ate"],  # despedidas
            "agradecimento": ["obrigado", "obrigada", "valeu", "agradeço"],  # agradecimentos
            "ajuda": ["ajuda", "socorro", "pode me ajudar", "como faço", "como posso"]  # pedidos de ajuda
        }

    # Normaliza texto removendo acentos para tornar as buscas mais robustas
    def _normalize(self, text: str) -> str:  # método interno para normalização
        nfkd = unicodedata.normalize("NFD", text)  # separa caracteres e marcas diacríticas
        without_accents = "".join(ch for ch in nfkd if unicodedata.category(ch) != "Mn")  # remove marcas
        return without_accents.lower()  # retorna tudo em minúsculas

    # Faz a identificação da intenção a partir do input do usuário
    def parse_intent(self, user_input: str) -> str:  # recebe texto do usuário e retorna o nome da intenção
        if not user_input:  # se entrada vazia
            return "desconhecido"  # retorna desconhecido
        normalized_input = self._normalize(user_input)  # normaliza entrada (remove acentos, minúsculas)
        # Percorre as intenções e suas palavras-chave normalizadas
        for intent, keywords in self.intents.items():  # itera sobre itens do dicionário de intenções
            for keyword in keywords:  # itera sobre cada palavra-chave da intenção
                kw_norm = self._normalize(keyword)  # normaliza a palavra-chave
                # usa regex com bordas de palavra para evitar correspondências parciais indevidas
                if re.search(r"\b" + re.escape(kw_norm) + r"\b", normalized_input):
                    return intent  # retorna a intenção correspondente ao encontrar correspondência
        return "desconhecido"  # se nada corresponder, retorna 'desconhecido'

    # Retorna a lista de nomes de intenções conhecidas
    def get_intents(self) -> List[str]:  # método auxiliar para listar intenções
        return list(self.intents.keys())  # converte chaves do dicionário em lista

    # Adiciona ou atualiza uma intenção com suas palavras-chave
    def add_intent(self, intent: str, keywords: List[str]) -> None:  # adiciona nova intenção
        self.intents[intent] = keywords  # insere/atualiza entrada no dicionário

    # Remove uma intenção existente pelo nome
    def remove_intent(self, intent: str) -> None:  # remove intenção se existir
        if intent in self.intents:  # checa existência
            del self.intents[intent]  # deleta a intenção