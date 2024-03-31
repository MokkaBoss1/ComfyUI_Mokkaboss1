# https://github.com/MokkaBoss1/ComfyUI_Mokkaboss1/wiki/Documentation-for-the-ComfyUI-Nodes-in-this-Node-Pack

class IntFloatDict:

#    def __init__(self):
#        pass
    
    @classmethod
    def INPUT_TYPES(s):

        return {
            "required": {
                "integer_value": ("INT", {"default": 0, "min": -9999, "max": 9999, "step": 1}),
                "text_value": ("STRING", {"multiline": True, "default": ""}),
            }
        }

    RETURN_TYPES = ("FLOAT",)
    RETURN_NAMES = ("float_value",)
    

    FUNCTION = "int_float"
    
    CATEGORY = "👑 MokkaBoss1/Other"

    def int_float(self, integer_value, text_value):

        print (f"integer_value = {integer_value}")
        print (f"text_value = {text_value}")

        multi_line_string = text_value
        result_dict = {}
        lines = multi_line_string.strip().split('\n')
        for line in lines:
            parts = line.strip().split(',')
            if len(parts) == 2:
                try:
                    key = int(parts[0])
                    value = float(parts[1])
                    result_dict[key] = value
                except ValueError:
                    pass  # Ignore lines that cannot be converted to int and float
        print(f"resulting dictionary {result_dict}")
    
        # Look up the integer_value in the dictionary and return corresponding value
        float_value = result_dict.get(integer_value, 0.0)

        return (float_value,)


NODE_CLASS_MAPPINGS = {"IntFloatDict": IntFloatDict}
NODE_DISPLAY_NAME_MAPPINGS = {"IntFloatDict": "👑 IntFloatDict"}
