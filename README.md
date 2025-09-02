# Assistente Virtual

Este projeto é um sistema de Assistente Virtual desenvolvido em Python, utilizando bibliotecas de Processamento de Linguagem Natural (PLN) e reconhecimento de fala. O assistente é capaz de ouvir comandos de voz, identificar intenções e responder de forma apropriada.

---

## **Funcionalidades**
- **Reconhecimento de Fala (STT)**: Converte comandos de voz em texto usando a biblioteca `speech_recognition`.
- **Síntese de Fala (TTS)**: Responde ao usuário convertendo texto em áudio com a biblioteca `pyttsx3`.
- **Análise de Intenções (NLU)**: Identifica a intenção do comando do usuário com base em palavras-chave.
- **Geração de Respostas (NLG)**: Gera respostas apropriadas para as intenções identificadas.
- **Habilidades Automatizadas**:
  - Pesquisar na Wikipedia.
  - Abrir vídeos no YouTube.
  - Localizar farmácias próximas no Google Maps.

---

## **Pré-requisitos**
Antes de começar, certifique-se de ter os seguintes itens instalados:
- **Python 3.8+**
- **Bibliotecas Python**:
  - `speech_recognition`
  - `pyttsx3`
  - `wikipedia`
  - `pyaudio` (no Windows, instale via `pipwin`)

---

## **Instalação**
1. Clone este repositório:
   ```bash
   git clone https://github.com/RafaelAraujoDiniz-Dev/assistente-virtual.git
   cd assistente-virtual

2. Crie um ambiente virtual (recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   
4. No Windows, instale o PyAudio com o pipwin:
    ```bash
   pip install pipwin
   pipwin install pyaudio

---

 ##  **Como Usar**
1. Execute o assistente:
   ```bash
   python src/assistant/core.py

2. O assistente irá:
- Ajustar-se ao ruído ambiente.
- Ouvir seu comando de voz.
- Identificar a intenção do comando.
- Responder com uma mensagem de voz.   

---
##  **Exemplo de Comandos**
- **Saudações:**
  - `"Olá", "Oi", "Bom dia"`
- **Despedidas:**
  - `Tchau", "Adeus", "Até logo`
- **Agradecimentos:**
  - `Obrigado", "Valeu`
- **Ajuda:**
  - `Pode me ajudar?", "Como faço para pesquisar?`

---

##  **Estrutura do Projeto**
```
assistente-virtual/
├── src/
│   ├── assistant/
│   │   ├── core.py          # Integração dos componentes principais
│   │   ├── stt/             # Reconhecimento de fala (Speech-to-Text)
│   │   ├── tts/             # Síntese de fala (Text-to-Speech)
│   │   ├── nlu/             # Análise de intenções (Natural Language Understanding)
│   │   ├── nlg/             # Geração de respostas (Natural Language Generation)
│   │   ├── skills/          # Habilidades adicionais (ex.: Wikipedia, YouTube)
│   ├── tests/               # Testes unitários
├── requirements.txt         # Dependências do projeto
├── [README.md](http://_vscodecontentref_/3)                # Documentação do projeto

```
---


##  **Testes**
1. Instale o pytest:
   ```bash
    pip install pytest

1. Execute os testes:
   ```bash
   pytest

 ---

##  **Licença**

Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para mais informações.