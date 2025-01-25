from nodes.config import Config


class PromptGeneratorNode:
    api_token: str = None

    def __init__(self):
        self.config = Config()
