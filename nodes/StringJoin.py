# Node to combine cliptextencode for positive and negative and allow the positive text and negative text to be output
# Written by MokkaBoss1 9th March 2024
# https://github.com/MokkaBoss1/ComfyUI-Mokkaboss1/wiki/Documentation-for-the-ComfyUI-Nodes-in-this-Node-Pack

# ███████╗████████╗██████╗ ██╗███╗   ██╗ ██████╗      ██╗ ██████╗ ██╗███╗   ██╗
# ██╔════╝╚══██╔══╝██╔══██╗██║████╗  ██║██╔════╝      ██║██╔═══██╗██║████╗  ██║
# ███████╗   ██║   ██████╔╝██║██╔██╗ ██║██║  ███╗     ██║██║   ██║██║██╔██╗ ██║
# ╚════██║   ██║   ██╔══██╗██║██║╚██╗██║██║   ██║██   ██║██║   ██║██║██║╚██╗██║
# ███████║   ██║   ██║  ██║██║██║ ╚████║╚██████╔╝╚█████╔╝╚██████╔╝██║██║ ╚████║
# ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝  ╚════╝  ╚═════╝ ╚═╝╚═╝  ╚═══╝
                                                                             
import re

def remove_consecutive_separators(input_string, separator):
    # Escape the separator for use in the regular expression
    escaped_separator = re.escape(separator)
    # Create the regular expression pattern for consecutive separators
    pattern = escaped_separator + r'+'
    # Use re.sub() to replace consecutive separators with a single separator
    result = re.sub(pattern, separator, input_string)
    return result


class StringJoin:

    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "separator": ("STRING", {"default": ","}),
                "required_string1":   ("STRING", {"forceInput": True}),
                "required_string2":   ("STRING", {"forceInput": True}),
                "optional_string3":   ("STRING", {"forceInput": False}),
                "optional_string4":   ("STRING", {"forceInput": False}),
                "optional_string5":   ("STRING", {"forceInput": False}),
                "optional_string6":   ("STRING", {"forceInput": False}),
                "optional_string7":   ("STRING", {"forceInput": False}),
                "optional_string8":   ("STRING", {"forceInput": False}),                
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("output",)
    FUNCTION = "stringjoin"
    CATEGORY = "👑 MokkaBoss1/Text"

    def stringjoin(self, separator, required_string1, required_string2, optional_string3, optional_string4, optional_string5, optional_string6, optional_string7, optional_string8):
        output = required_string1 + separator + required_string2 + separator + optional_string3 +  separator + optional_string4 + separator + optional_string5 + separator + optional_string6 + separator + optional_string7 + separator + optional_string8 
        
       
        output = remove_consecutive_separators(output, separator)
        if output.endswith(","):
            output = output[:-1]        
        return (output,)

NODE_CLASS_MAPPINGS = {"StringJoin": StringJoin}
NODE_DISPLAY_NAME_MAPPINGS = {"StringJoin": "👑 StringJoin"}
