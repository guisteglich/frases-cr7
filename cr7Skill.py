import logging
from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import (
    AbstractRequestHandler, AbstractExceptionHandler)
from ask_sdk_core.utils import is_request_type
from ask_sdk_model import Response

# Configure o URL do seu áudio MP3 aqui
audio_url = 'URL_DO_SEU_AUDIO.mp3'

# Configurar o logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Define um manipulador de lançamento para acionar a skill
class LaunchRequestHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        speak_output = "Bem-vindo à minha skill de áudio. Diga 'Reproduzir' para ouvir o áudio."
        return (
            handler_input.response_builder
            .speak(speak_output)
            .response
        )

# Define um manipulador de intenção para reproduzir o áudio
class PlayAudioIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_request_type("IntentRequest")(handler_input) and \
            handler_input.request_envelope.request.intent.name == "PlayAudioIntent"

    def handle(self, handler_input):
        speak_output = "Reproduzindo o áudio."

        # Use a diretiva AudioPlayer para reproduzir o áudio
        return (
            handler_input.response_builder
            .speak(speak_output)
            .add_audio_player_play_directive(
                "REPLACE_ALL", audio_url, audio_url, 0)
            .response
        )

# Define um manipulador de exceção para lidar com erros
class ErrorHandler(AbstractExceptionHandler):
    def can_handle(self, handler_input, exception):
        return True

    def handle(self, handler_input, exception):
        logger.error(f"Exceção ocorrida: {exception}")
        speak_output = "Desculpe, houve um erro. Por favor, tente novamente."

        return (
            handler_input.response_builder
            .speak(speak_output)
            .response
        )

# Inicializa o SkillBuilder
sb = Skill
