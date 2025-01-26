from .sml_prompt_exp.base_node import PromptGeneratorNode

NODE_CLASS_MAPPINGS = {
    "SML_Prompt_Generator": PromptGeneratorNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SML_Prompt_Generator": "SML Prompt Generator"
}

WEB_DIRECTORY = "./js"

__all__ = [
    "NODE_CLASS_MAPPINGS",
    "NODE_DISPLAY_NAME_MAPPINGS",
    "WEB_DIRECTORY",
]
