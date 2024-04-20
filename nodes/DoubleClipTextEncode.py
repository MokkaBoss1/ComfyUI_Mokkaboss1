# Node to combine cliptextencode for positive and negative and allow the positive text and negative text to be output
# Written by MokkaBoss1 9th March 2024
# https://github.com/MokkaBoss1/ComfyUI-Mokkaboss1/wiki/Documentation-for-the-ComfyUI-Nodes-in-this-Node-Pack

class DoubleClipTextEncode:

    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "clip": ("CLIP",),
                "positive_prompt": ("STRING", {"forceInput":True},),
                "negative_prompt": ("STRING", {"forceInput":True},),
            }
        }

    RETURN_TYPES = ("CONDITIONING","CONDITIONING","STRING","STRING")
    RETURN_NAMES = ("Positive Conditioning","Negative Conditioning","Positive Prompt","Negative Prompt",)
    

    FUNCTION = "double_encode"
    
    CATEGORY = "👑 MokkaBoss1/Text"

    def double_encode(self, clip, positive_prompt, negative_prompt):

        tokens_pos = clip.tokenize(positive_prompt)
        cond_pos, pooled = clip.encode_from_tokens(tokens_pos, return_pooled=True)
        
        tokens_neg = clip.tokenize(negative_prompt)
        cond_neg, pooled = clip.encode_from_tokens(tokens_neg, return_pooled=True)


        return (
            [[cond_pos, {"pooled_output": pooled}]],
            [[cond_neg, {"pooled_output": pooled}]],
            [positive_prompt],
            [negative_prompt],
            )

NODE_CLASS_MAPPINGS = {"DoubleClipTextEncode": DoubleClipTextEncode}
NODE_DISPLAY_NAME_MAPPINGS = {"DoubleClipTextEncode": "👑 DoubleClipTextEncode"}
