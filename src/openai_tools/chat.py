from .common import Usage
import copy


class Message:
    def __init__(self, message: dict[str, str]) -> None:
        """Messages that make up a conversation

        :param message: {"role": "user", "content": "Hello!"}.
        role must be one of "user", "system" or "assistant".
        """
        self.role: str = message["role"]
        self.content: str = message["content"]

    def get_role(self):
        """Get the role of the message"""
        return self.role

    def get_content(self):
        """Get the content of the message"""
        return self.content

    def to_dict(self) -> dict[str, str]:
        """Converts the message to a dictionary

        :return: A dictionary representation of the message. example is {"role": "user", "content": "Hello!"}
        """
        return {
            "role": self.role,
            "content": self.content
        }


class UserMessage(Message):

    def __init__(self, content: str):
        super().__init__({"role": "user", "content": content})


class AssistantMessage(Message):

    def __init__(self, content: str):
        super().__init__({"role": "assistant", "content": content})


class SystemMessage(Message):

    def __init__(self, content: str):
        super().__init__({"role": "system", "content": content})


class MessageList:
    def __init__(self, messages: list[Message] = None) -> None:
        """A list of Message.

        :param messages: A list of Message.
        """
        self.messages: list[Message] = []
        if messages is None:
            self.messages: list[Message] = []
        else:
            for message in messages:
                if not isinstance(message, Message):
                    raise TypeError(f"Expected Message, got {type(message)}")
                self.messages = []
                self.messages.append(copy.copy(message))

    def append(self, message: Message) -> None:
        """Append a message to the list of messages

        :param message: The message to append
        """
        self.messages.append(copy.copy(message))

    def get(self, index: int) -> Message:
        """Get a message at the specified index

        :param index: index of this object to get.
        :return: The message at the specified index
        """
        return self.messages[index]

    def get_latest(self) -> Message:
        """Get the latest message"""
        if self.is_empty():
            raise IndexError("MessageList is empty")
        return self.messages[-1]

    def clear(self) -> None:
        self.messages.clear()

    def set(self, index: int, message: Message) -> None:
        """Inserts a Message at the specified index.

        :param index: index at which the Message is inserted
        :param message: Message to be inserted
        """
        if self.is_empty():
            self.messages.append(message)
        else:
            self.messages[index] = message

    def is_empty(self):
        return len(self.messages) == 0

    def to_dict(self) -> list[dict[str, str]]:
        """Converts the message list to a dictionary

        :return: A dictionary representation of the message list. example is [{"role": "user", "content": "Hello!"}].
        """
        return [message.to_dict() for message in self.messages]


class ChatUsage(Usage):

    def __init__(self, usage: dict[str, int]):
        super().__init__(usage)
        self.completion_tokens: int = usage["completion_tokens"]

    def get_completion_tokens(self):
        """Get the number of tokens used for the completion"""
        return self.completion_tokens


class ChatResponse:

    def __init__(self, response: any) -> None:
        """Convert openai api response to ChatResponse object

        :parameter response: openai api response
        """
        self.message: Message = Message(response['choices'][0]['message'])
        self.usage: ChatUsage = ChatUsage(response['usage'])

    def get_message(self) -> Message:
        return self.message

    def get_usage(self) -> ChatUsage:
        return self.usage
