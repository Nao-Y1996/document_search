from openai_tools.chat import Message, MessageList, ChatResponse


def test_create_message():
    message: Message = Message({"role": "user", "content": "hello!"})
    assert message.get_content() == "hello!"
    assert message.get_role() == "user"
    assert message.to_dict() == {"role": "user", "content": "hello!"}


def test_message_list_init__is_empty():
    message_list: MessageList = MessageList()
    assert message_list.is_empty()


def test_message_list_init_with_argument():
    message: Message = Message({"role": "user", "content": "hello"})
    message_list: MessageList = MessageList([message])
    assert not message_list.is_empty()

    # 元のオブジェクトを変更してもMessageListは変更されないこと
    message.role = "assistant"
    message.content = "hi"
    assert message_list.get(0).get_role() == "user"
    assert message_list.get(0).get_content() == "hello"


def test_message_list_get__append():
    message_list: MessageList = MessageList()
    assert message_list.is_empty()

    # appendのテスト
    message1: Message = Message({"role": "user", "content": "hello"})
    message_list.append(message1)
    assert not message_list.is_empty()
    assert message_list.get_latest().get_role() == "user"
    assert message_list.get_latest().get_content() == "hello"

    message2: Message = Message({"role": "assistant", "content": "hi"})
    message_list.append(message2)
    assert message_list.get_latest().get_role() == "assistant"
    assert message_list.get_latest().get_content() == "hi"

    # 元のオブジェクトを変更してもMessageListは変更されないこと
    message1.role = "assistant"
    message1.content = "good morning"
    message2.role = "user"
    message2.content = "hey"
    assert message_list.get(0).get_role() == "user"
    assert message_list.get(0).get_content() == "hello"
    assert message_list.get_latest().get_role() == "assistant"
    assert message_list.get_latest().get_content() == "hi"


def test_message_list_clear():
    message1: Message = Message({"role": "user", "content": "hello"})
    message2: Message = Message({"role": "assistant", "content": "hi"})
    message_list: MessageList = MessageList([message1, message2])
    assert not message_list.is_empty()
    message_list.clear()
    assert message_list.is_empty()


def test_chat_response():
    response = {
        "choices": [
            {
                "finish_reason": "stop",
                "index": 0,
                "message": {
                    "content": "This is assistant.",
                    "role": "assistant"
                }
            }
        ],
        "created": 1677664795,
        "id": "chatcmpl-7QyqpwdfhqwajicIEznoc6Q47XAyW",
        "model": "gpt-3.5-turbo-0613",
        "object": "chat.completion",
        "usage": {
            "completion_tokens": 17,
            "prompt_tokens": 57,
            "total_tokens": 74
        }
    }
    chat_response: ChatResponse = ChatResponse(response)
    assert chat_response.get_message().get_content() == "This is assistant."
    assert chat_response.get_message().get_role() == "assistant"
    assert chat_response.get_usage().get_completion_tokens() == 17
    assert chat_response.get_usage().get_prompt_tokens() == 57
    assert chat_response.get_usage().get_total_tokens() == 74
