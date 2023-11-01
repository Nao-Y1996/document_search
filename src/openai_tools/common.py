class Usage:
    def __init__(self, usage: dict[str, int]) -> None:
        """Usage of the API call

        :param usage: {"prompt_tokens": 12, "completion_tokens": 23, "total_tokens": 35}
        """
        self.prompt_tokens: int = usage["prompt_tokens"]
        self.total_tokens = usage["total_tokens"]

    def get_prompt_tokens(self):
        """Get the number of tokens used for the prompt"""
        return self.prompt_tokens

    def get_total_tokens(self):
        """Get the total number of tokens used"""
        return self.total_tokens
