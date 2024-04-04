class IntStringDict:

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

    RETURN_TYPES = ("STRING",)  # Change return type to combo
    RETURN_NAMES = ("string_value",)  # Change return name to string_value
    

    FUNCTION = "int_string"
    
    CATEGORY = "👑 MokkaBoss1/Other"

    def int_string(self, integer_value, text_value):

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
                    value = parts[1]  # Store the value as string
                    result_dict[key] = value
                except ValueError:
                    pass  # Ignore lines that cannot be converted to int and float
        print(f"resulting dictionary {result_dict}")
    
        # Look up the integer_value in the dictionary and return corresponding value
        string_value = result_dict.get(integer_value, "")

        return (string_value,)  # Return as a tuple to match RETURN_NAMES


NODE_CLASS_MAPPINGS = {"IntStringDict": IntStringDict}
NODE_DISPLAY_NAME_MAPPINGS = {"IntStringDict": "👑 IntStringDict"}
