# https://github.com/MokkaBoss1/ComfyUI_Mokkaboss1/wiki/Documentation-for-the-ComfyUI-Nodes-in-this-Node-Pack


# ███████╗████████╗ ██████╗ ██████╗ ██╗    ██╗ ██████╗ ██████╗ ██╗  ██╗███████╗██╗      ██████╗ ██╗    ██╗
# ██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗██║    ██║██╔═══██╗██╔══██╗██║ ██╔╝██╔════╝██║     ██╔═══██╗██║    ██║
# ███████╗   ██║   ██║   ██║██████╔╝██║ █╗ ██║██║   ██║██████╔╝█████╔╝ █████╗  ██║     ██║   ██║██║ █╗ ██║
# ╚════██║   ██║   ██║   ██║██╔═══╝ ██║███╗██║██║   ██║██╔══██╗██╔═██╗ ██╔══╝  ██║     ██║   ██║██║███╗██║
# ███████║   ██║   ╚██████╔╝██║     ╚███╔███╔╝╚██████╔╝██║  ██║██║  ██╗██║     ███████╗╚██████╔╝╚███╔███╔╝
# ╚══════╝   ╚═╝    ╚═════╝ ╚═╝      ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚══════╝ ╚═════╝  ╚══╝╚══╝ 
                                                                                                        
                                                                                                                                                          


import random
import re
from comfy.model_management import InterruptProcessingException

class StopWorkflow:

    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
            "image": ("IMAGE", ),
            "choice": ("STRING", {"default": "Yes", "options": ("Yes", "No")})
        }}

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("Image",)
    FUNCTION = "test5"
    CATEGORY = "👑 MokkaBoss1/Image"

    def test5(self, image, choice): 
        _, height, width, _ = image.shape
        ar = width/height
        if choice == "Yes":
            return (image, )
        else:
            raise InterruptProcessingException()
#            raise ValueError("Workflow terminated because the aspect ratio is not within the specified range. See Node AspectRatioCondition min and max values.")

NODE_CLASS_MAPPINGS = {"StopWorkflow": StopWorkflow}
NODE_DISPLAY_NAME_MAPPINGS = {"StopWorkflow": "👑 StopWorkflow"}

