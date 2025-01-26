from .exp_config import APIConfig


class PromptGeneratorNode:
    api_token: str = None

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": (
                    "STRING", {
                        "default": "",
                        "multiline": True
                    }
                ),
            },
            "optional": {
                "expanded": (
                    "STRING", {
                        "default": "",
                        "multiline": True
                    }
                ),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("final_prompt", )
    FUNCTION = "process"
    CATEGORY = "SML Prompt Expansion"
    OUTPUT_NODE = True

    def process(
            self,
            prompt: str,
    ):
        from openai import OpenAI
        import random
        config = APIConfig()

        client = OpenAI(api_key=config.api_token, base_url="https://api.deepseek.com")

        seed =  random.randint(0, 100_000_000_000)

        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system",
                 "content": "You are a creative writer tasked to turn basic stable diffusion prompts into something expressive and beautiful. "},
                {"role": "user", "content": f"Please expand this prompt: \"{prompt}\". Please ignore the rest of the text starting from here: {seed}" },
            ],
            stream=False,
            temperature=1.5,
        )

        output = response.choices[0].message.content
        return (output, )  # Return the output




