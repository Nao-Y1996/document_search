from openai_tools.chat import ChatResponse
from openai_tools.embedding import EmbeddingResponse
from openai_tools.client import ChatClient, EmbeddingClient

if __name__ == '__main__':

    client: ChatClient = ChatClient()

    embeddingClient: EmbeddingClient = EmbeddingClient()

    while True:
        # 入力を受け付ける
        input_text = input("You: ")
        if input_text == "exit":
            break

        response: ChatResponse = client.add_user_message(input_text).simple_request()
        # response: ChatResponse = client.add_user_message(input_text).conversational_request()
        print(response.get_message().get_content() + f"  (total token usage: {response.usage.get_total_tokens()}）")

        embedding_response: EmbeddingResponse = embeddingClient.request(input_text)
        print(f"(embedding total token usage: {embedding_response.get_usage().get_total_tokens()}）")
        print("embedding = ", embedding_response.get_embedding())
