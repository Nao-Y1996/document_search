from .common import Usage


class EmbeddingResponse:

    def __init__(self, response: any) -> None:
        self.embedding: list[float] = response["data"][0]["embedding"]
        self.usage = Usage(response['usage'])

    def get_embedding(self) -> list[float]:
        return self.embedding

    def get_usage(self) -> Usage:
        return self.usage
