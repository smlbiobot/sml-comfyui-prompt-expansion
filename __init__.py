# from .sml_prompt_exp.base_node import NODE_DISPLAY_NAME_MAPPINGS as _NODE_DISPLAY_NAME_MAPPINGS
# from .sml_prompt_exp.base_node import NODE_CLASS_MAPPINGS as _NODE_CLASS_MAPPINGS
from .sml_prompt_exp.base_node import PromptGeneratorNode

NODE_CLASS_MAPPINGS = {
    "SML_Prompt_Generator": PromptGeneratorNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SML_Prompt_Generator": "😃 SML Prompt Generator"
}


__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
