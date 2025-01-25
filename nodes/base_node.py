from nodes.config import Config


class PromptGeneratorNode:
    api_token: str = None

    RETURN_TYPES = ("STRING",)
    FUNCTION = "expand_prompt"
    CATEGORY = "😃 SML"

    def __init__(self):
        self.config = Config()

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
            },
        }

    def expand_prompt(
            self,
            prompt: str
    ):
        from openai import OpenAI

        client = OpenAI(api_key=self.config.api_token, base_url="https://api.deepseek.com")

        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "You are a creative writer tasked to turn basic stable diffusion prompts into something expressive and beautiful. "},
                {"role": "user", "content": f"Please expand this prompt: \"{prompt}\""},
            ],
            stream=False
        )

        output = response.choices[0].message.content
        return output

def test_node():
    node = PromptGeneratorNode()
    s = node.expand_prompt("a man lounging at the beach")
    print(s)

if __name__ == '__main__':
    test_node()


