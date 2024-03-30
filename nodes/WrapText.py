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

    RETURN_TYPES = ("STRING","STRING","STRING","STRING","STRING","STRING","STRING",)
    RETURN_NAMES = ("Line1","Line2","Line3","Line4","Line5","Line6","Line7",)
    FUNCTION = "test"
    CATEGORY = "👑 MokkaBoss1/Text"

    def test(self, text, width): 

        print ("Wrap Text Node")
        print (text)
        print (width)

        line_one = ""
        line_two = ""
        line_three = ""
        line_four = ""
        line_five = ""
        line_six = ""
        line_seven = ""

        wrapped_lines = []
        words = text.split()
        current_line = ''
            
        for word in words:
            if len(current_line) + len(word) <= width:
                current_line += word + ' '
            else:
                wrapped_lines.append(current_line.strip())
                current_line = word + ' '
            
        # Append the remaining text
        if current_line:
             wrapped_lines.append(current_line.strip())

        # Assign wrapped lines if they exist
        if len(wrapped_lines) >= 1:
            line_one = wrapped_lines[0]
        if len(wrapped_lines) >= 2:
            line_two = wrapped_lines[1]
        if len(wrapped_lines) >= 3:
            line_three = wrapped_lines[2]
        if len(wrapped_lines) >= 4:
            line_four = wrapped_lines[3]
        if len(wrapped_lines) >= 5:
            line_five = wrapped_lines[4]
        if len(wrapped_lines) >= 6:
            line_six = wrapped_lines[5]
        if len(wrapped_lines) >= 7:
            line_seven = wrapped_lines[6]

        # Print the lines
        print("start")
        print(line_one)
        print(line_two)
        print(line_three)
        print(line_four)
        print(line_five)
        print(line_six)
        print(line_seven)
        print("End")

        return (line_one, line_two, line_three, line_four, line_five, line_six, line_seven)

NODE_CLASS_MAPPINGS = {"WrapText": WrapText}
NODE_DISPLAY_NAME_MAPPINGS = {"WrapText": "👑 WrapText"}



# 👑


