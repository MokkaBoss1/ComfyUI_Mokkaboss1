# https://github.com/MokkaBoss1/ComfyUI-Mokkaboss1/wiki/Documentation-for-the-ComfyUI-Nodes-in-this-Node-Pack
from datetime import datetime

class TimeStamp:

    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {
            "format": ("STRING", {"default": "(%Y-%m-%d)(%H-%M-%S)", "multiline": False}),
        }}

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("timestamp",)
    FUNCTION = "date_string"
    CATEGORY = "👑 MokkaBoss1/Other"

    def date_string(self, format): 
        
        
        now = datetime.now()
        return (now.strftime(format),)
        


NODE_CLASS_MAPPINGS = {"TimeStamp": TimeStamp}
NODE_DISPLAY_NAME_MAPPINGS = {"TimeStamp": "👑 TimeStamp"}
