import random
import re

class AspectRatioCondition:

    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
            "image": ("IMAGE", ),
            "min": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 3.0, "step": 0.01}),
            "max": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 3.0, "step": 0.01})
        }}

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("Image",)
    FUNCTION = "test4"
    CATEGORY = "👑 MokkaBoss1"

    def test4(self, image, min, max): 
        _, height, width, _ = image.shape
        ar = width/height
        if min <= ar <= max:
            return (image, )
        else:

            raise ValueError("Workflow terminated because the aspect ratio is not within the specified range. See Node AspectRatioCondition min and max values.")

NODE_CLASS_MAPPINGS = {"AspectRatioCondition": AspectRatioCondition}
NODE_DISPLAY_NAME_MAPPINGS = {"AspectRatioCondition": "👑 AspectRatioCondition"}
