from .exp_config import APIConfig
from openai import OpenAI
import random


class PromptGeneratorNode:
    api_token: str = None
    previous_output: str = None
    use_char_limit: bool = True

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
                "seed": ("INT", {"default": 0, "min": 0, "max": 100_000_000_000}),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("final_prompt",)
    FUNCTION = "process"
    CATEGORY = "SML Prompt Expansion"
    OUTPUT_NODE = True

    def process(
            self,
            prompt: str,
            seed: int,
    ):
        config = APIConfig()

        client = OpenAI(api_key=config.api_token, base_url="https://api.deepseek.com")

        if not seed or seed == -1:
            seed = random.randint(0, 100_000_000_000)

        prompt = self.construct_prompt(prompt)

        user_content = f"Please expand this prompt: \"{prompt}\"."

        if self.use_char_limit:
            char_count = random.randint(1000, 3000)
            user_content = f"{user_content} Please expand this prompt to {char_count} characters."

        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system",
                 "content": "You are a creative writer tasked to turn basic stable diffusion prompts into something expressive, succinct, and beautiful. "},
                {"role": "user", "content": user_content},
            ],
            stream=False,
            temperature=1.5,
            seed=seed,
        )

        output = response.choices[0].message.content
        self.previous_output = output

        # print(f"{output=}")

        return (output,)  # Return the output

    def get_random_sentences(self, paragraph):
        sentences = paragraph.split(".")
        sentences = [s for s in sentences if s.strip()]

        num = len(sentences)
        count = int(num / 4)

        count = min(count, 3) # not more than 3 random sentences

        if count <= 1:
            count = 1

        return random.sample(sentences, count)

    def construct_prompt(self, input: str):
        p = input
        if self.previous_output is not None:
            rs = self.get_random_sentences(self.previous_output)
            r = '. '.join(rs)
            p = f"{p}. {r}."

        return p
