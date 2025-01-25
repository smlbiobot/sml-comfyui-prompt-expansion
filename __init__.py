from nodes.base_node import PromptGeneratorNode

NODE_DISPLAY_NAME_MAPPINGS = {
    "SML_Prompt_Generator": PromptGeneratorNode,
}

NODE_CLASS_MAPPINGS = {
    "SML_Prompt_Generator": "😃 SML Prompt Generator"
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
