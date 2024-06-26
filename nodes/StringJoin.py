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
    if not separator:
        return input_string
    escaped_separator = re.escape(separator)
    if escaped_separator == '':
        return input_string
    pattern = escaped_separator + r'+'
    result = re.sub(pattern, separator, input_string)
    return result

def remove_trailing_spaces_and_punctuation(input_string):
    result = re.sub(r'[\s\.,;!?]+$', '', input_string)
    return result

class StringJoin:

    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "separator": ("STRING", {"default": ","}),
                "required_string1": ("STRING", {"forceInput": True}),
                "required_string2": ("STRING", {"forceInput": True}),
                "optional_string3": ("STRING", {"forceInput": False}),
                "optional_string4": ("STRING", {"forceInput": False}),
                "optional_string5": ("STRING", {"forceInput": False}),
                "optional_string6": ("STRING", {"forceInput": False}),
                "optional_string7": ("STRING", {"forceInput": False}),
                "optional_string8": ("STRING", {"forceInput": False}),                
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("output",)
    FUNCTION = "stringjoin"
    CATEGORY = "👑 MokkaBoss1/Text"

    def stringjoin(self, separator, required_string1, required_string2, optional_string3=None, optional_string4=None, optional_string5=None, optional_string6=None, optional_string7=None, optional_string8=None):
        strings = [required_string1, required_string2, optional_string3, optional_string4, optional_string5, optional_string6, optional_string7, optional_string8]
        strings = [s for s in strings if s is not None]
        if separator:
            output = separator.join(strings)
            output = remove_consecutive_separators(output, separator)
        else:
            output = ''.join(strings)
        output = remove_trailing_spaces_and_punctuation(output)
        return (output,)

NODE_CLASS_MAPPINGS = {"StringJoin": StringJoin}
NODE_DISPLAY_NAME_MAPPINGS = {"StringJoin": "👑 StringJoin"}



