# Node to combine cliptextencode for positive and negative and allow the positive text and negative text to be output
# Written by MokkaBoss1 9th March 2024
# https://github.com/MokkaBoss1/ComfyUI-Mokkaboss1/wiki/Documentation-for-the-ComfyUI-Nodes-in-this-Node-Pack

                                                                                                                                                                 


class QuadClipTextEncode:

    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "clip": ("CLIP",),
                "pos_prompt1": ("STRING", {"forceInput":True},),
                "neg_prompt1": ("STRING", {"forceInput":True},),
                "pos_prompt2": ("STRING", {"forceInput":True},),
                "neg_prompt2": ("STRING", {"forceInput":True},),
            }
        }

    RETURN_TYPES = ("CONDITIONING","CONDITIONING","CONDITIONING","CONDITIONING",)
    RETURN_NAMES = ("Pos Conditioning1","Neg Conditioning1","Pos Conditioning2","Neg Conditioning2",)
    

    FUNCTION = "quad_encode"
    
    CATEGORY = "👑 MokkaBoss1/Text"

    def quad_encode(self, clip, pos_prompt1, neg_prompt1, pos_prompt2, neg_prompt2):

        tokens_pos = clip.tokenize(pos_prompt1)
        cond_pos1, pooled = clip.encode_from_tokens(tokens_pos, return_pooled=True)
        
        tokens_neg = clip.tokenize(neg_prompt1)
        cond_neg1, pooled = clip.encode_from_tokens(tokens_neg, return_pooled=True)
        
        tokens_pos = clip.tokenize(pos_prompt2)
        cond_pos2, pooled = clip.encode_from_tokens(tokens_pos, return_pooled=True)
        
        tokens_neg = clip.tokenize(neg_prompt2)
        cond_neg2, pooled = clip.encode_from_tokens(tokens_neg, return_pooled=True)


        return (
            [[cond_pos1, {"pooled_output": pooled}]],
            [[cond_neg1, {"pooled_output": pooled}]],
            [[cond_pos2, {"pooled_output": pooled}]],
            [[cond_neg2, {"pooled_output": pooled}]],
            )

NODE_CLASS_MAPPINGS = {"QuadClipTextEncode": QuadClipTextEncode}
NODE_DISPLAY_NAME_MAPPINGS = {"QuadClipTextEncode": "👑 QuadClipTextEncode"}
