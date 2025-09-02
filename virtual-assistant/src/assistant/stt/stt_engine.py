from speech_recognition import Recognizer, Microphone, WaitTimeoutError, UnknownValueError, RequestError

class SpeechToTextEngine:
    def __init__(self):
        # Inicializa o reconhecedor de fala
        self.recognizer = Recognizer()

    def listen(self, timeout=5, phrase_time_limit=10):
        """
        Captura o áudio do microfone.
        :param timeout: Tempo máximo para começar a falar (em segundos).
        :param phrase_time_limit: Tempo máximo de duração da fala (em segundos).
        :return: Objeto de áudio capturado.
        """
        with Microphone() as source:
            print("Ajustando para o ruído ambiente... Aguarde.")
            self.recognizer.adjust_for_ambient_noise(source, duration=1)  # Ajusta para ruído ambiente
            print("Pronto! Você pode falar agora.")
            try:
                audio = self.recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
                return audio
            except WaitTimeoutError:
                print("Tempo esgotado ao aguardar fala.")
                return None

    def recognize(self, audio):
        """
        Converte o áudio capturado em texto.
        :param audio: Objeto de áudio capturado.
        :return: Texto reconhecido ou None em caso de erro.
        """
        if audio is None:
            return None
        try:
            # Reconhece o áudio usando o Google Web Speech API (idioma: Português do Brasil)
            text = self.recognizer.recognize_google(audio, language="pt-BR")
            print(f"Você disse: {text}")
            return text
        except UnknownValueError:
            print("Desculpe, não consegui entender o que você disse.")
            return None
        except RequestError as e:
            print(f"Erro ao se conectar ao serviço de reconhecimento: {e}")
            return None
        except Exception as e:
            print(f"Erro inesperado: {e}")
            return None

    def run(self):
        """
        Captura e processa o áudio em uma única chamada.
        :return: Texto reconhecido ou None em caso de erro.
        """
        print("Iniciando o reconhecimento de fala...")
        audio = self.listen()
        return self.recognize(audio)