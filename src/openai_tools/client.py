from .chat import Message, UserMessage, SystemMessage, MessageList, ChatResponse
from .embedding import EmbeddingResponse
import openai
import os

DOCUMENTS_PATH = os.environ.get('DOCUMENTS_PATH')
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

openai.api_key = OPENAI_API_KEY

DEFAULT_BEHAVIOR = "You are useful assistant and response in English."


class ChatClient:

    def __init__(self, model: str = "gpt-3.5-turbo", behavior: str = None) -> None:
        self.model: str = model
        self.messages: MessageList = MessageList([])
        if behavior is None:
            self.set_behavior(DEFAULT_BEHAVIOR)

    def set_behavior(self, behavior: str) -> 'ChatClient':
        self.messages.set(0, SystemMessage(behavior))
        return self

    def add_user_message(self, content: str) -> 'ChatClient':
        self.messages.append(UserMessage(content))
        return self

    def add_message(self, message: Message) -> 'ChatClient':
        self.messages.append(message)
        return self

    def latest_message(self) -> Message:
        return self.messages.get_latest()

    def simple_request(self) -> ChatResponse:
        """Send a stateless request.
        Not holding a response, it cannot be used for conversation.
        :return: Response
        """
        response: ChatResponse = ChatResponse(
            openai.ChatCompletion.create(
                model=self.model,
                messages=self.messages.to_dict()
            )
        )
        self.messages.clear()
        self.set_behavior(DEFAULT_BEHAVIOR)
        return response

    def conversational_request(self) -> ChatResponse:
        """Send a statefull request.
        Holding a response, it can be used for conversation.
        :return: Response
        """
        # TODO Need to implement a mechanism to delete old messages when usage approaches the limit
        response: ChatResponse = ChatResponse(
            openai.ChatCompletion.create(
                model=self.model,
                messages=self.messages.to_dict()
            )
        )
        self.add_message(response.get_message())
        return response


class EmbeddingClient:
    def __init__(self, model: str = "text-embedding-ada-002") -> None:
        self.model: str = model

    def request(self, text: str) -> EmbeddingResponse:
        return EmbeddingResponse(
            openai.Embedding.create(input=[text], model=self.model)
        )
