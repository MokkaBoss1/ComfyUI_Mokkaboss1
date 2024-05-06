# Node to wrap text into 7 lines based on a long text and integer representing the width

class WrapText:

    def __init__(self):
        pass

    CATEGORY = "MokkaBoss1"
    
    @classmethod
    def INPUT_TYPES(cls):        
        return {"required": {
            "text": ("STRING", {"default": "prompt", "multiline": True}),
            "width": ("INT", {"default": 50, "min": 1, "max": 300, "step": 1}),
        }}

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)
    FUNCTION = "wrap_text"
    CATEGORY = "👑 MokkaBoss1/Text"

    def wrap_text(self, text, width): 
        wrapped_lines = []
        words = text.split()
        current_line = ''
            
        for word in words:
            if len(current_line) + len(word) + 1 <= width:  # +1 for space
                current_line += word + ' '
            else:
                wrapped_lines.append(current_line.strip())
                current_line = word + ' '
            
        # Append the remaining text
        if current_line:
            wrapped_lines.append(current_line.strip())

        # Dynamically create the output with line breaks
        text = "\n".join(wrapped_lines)

        return (text, )

NODE_CLASS_MAPPINGS = {"WrapText": WrapText}
NODE_DISPLAY_NAME_MAPPINGS = {"WrapText": "👑 WrapText"}