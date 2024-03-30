# https://github.com/MokkaBoss1/ComfyUI_Mokkaboss1/wiki/Documentation-for-the-ComfyUI-Nodes-in-this-Node-Pack


class OptimalCrop:

    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):        
        return {"required": {
            "input_image": ("IMAGE", ),
            "rounding": ("INT", {"default": 1, "min": 1, "max": 64, "step": 1}),
            "aspect_ratio": ("FLOAT", {"default": 1.0, "min": 0, "max": 3.0, "step": 0.01}),
            "x_offset": ("INT", {"default": 0, "min": -9999, "max": 9999, "step": 1}),
            "y_offset": ("INT", {"default": 0, "min": -9999, "max": 9999, "step": 1}),
        }}

    RETURN_TYPES = ("IMAGE", )
    RETURN_NAMES = ("crop_image", )
    FUNCTION = "Optimal_Crop"
    CATEGORY = "👑 MokkaBoss1"

    def Optimal_Crop(self, input_image, rounding, aspect_ratio, x_offset, y_offset):

        _, input_height, input_width, _ = input_image.shape
    
        # Calculate output width based on input width and aspect ratio
        output_width = int(min(input_width, input_height * aspect_ratio))
        
#        print(f"input_width: {input_width}")
#        print(f"input_height: {input_height}")
        
#        print(f"output width: {output_width}")        
        
        # Calculate output height based on output width and aspect ratio
        output_height = int(output_width / aspect_ratio)
        
#        print(f"output height: {output_height}")
        
        # Ensure both width and height are divisible by 16
        output_width = output_width - (output_width % rounding)
        output_height = output_height - (output_height % rounding)
        
#        print("After Rounding")
#        print(f"output width: {output_width}") 
#        print(f"output height: {output_height}")

        # calculate delta to x_offset and y_offset
        x_offset = x_offset + int((input_width-output_width)*0.5)
        y_offset = y_offset + int((input_height - output_height)*0.5)
 
#        print(f"new x_offset: {x_offset}, new y_offset: {y_offset}")
 
        # Calculate the actual cropping area based on the aspect ratio and offsets
        crop_x1 = max(0, min(input_width - output_width, x_offset))
        crop_y1 = max(0, min(input_height - output_height, y_offset))
        crop_x2 = min(input_width, crop_x1 + output_width)
        crop_y2 = min(input_height, crop_y1 + output_height)
        
        print(f"crop_x1: {crop_x1} crop_x2: {crop_x2} crop_y1: {crop_y1} crop_y2: {crop_y2}") 
        
        crop_image = input_image[:, crop_y1:crop_y2, crop_x1:crop_x2, :]

        return (crop_image, )

NODE_CLASS_MAPPINGS = {"OptimalCrop": OptimalCrop}
NODE_DISPLAY_NAME_MAPPINGS = {"OptimalCrop": "👑 OptimalCrop"}
