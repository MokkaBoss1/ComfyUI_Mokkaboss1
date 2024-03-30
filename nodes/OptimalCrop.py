# https://github.com/MokkaBoss1/ComfyUI-Mokkaboss1/wiki/Documentation-for-the-ComfyUI-Nodes-in-this-Node-Pack
# Node to calculate the optimal output width and height based on an input width and height AND aspect ratio
class OptimalCrop:

    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):        
        return {"required": {
            "image": ("IMAGE", ),
            "rounding": ("INT", {"default": 1, "min": 1, "max": 64, "step": 1}),
            "aspect_ratio": ("FLOAT", {"default": 1.0, "min": 0, "max": 3.0, "step": 0.01}),
        }}

    RETURN_TYPES = ("INT","INT",)
    RETURN_NAMES = ("output_width", "output_height")
    FUNCTION = "Optimal_Crop"
    CATEGORY = "👑 MokkaBoss1"

    def Optimal_Crop(self, image, rounding, aspect_ratio):

        _, input_height, input_width, _ = image.shape
    
        # Calculate output width based on input width and aspect ratio
        output_width = int(min(input_width, input_height * aspect_ratio))
        
        # Calculate output height based on output width and aspect ratio
        output_height = int(output_width / aspect_ratio)
        
        print (f"The rounding value is {rounding}")
        
        # Ensure both width and height are divisible by 16
        output_width = output_width - (output_width % rounding)
        output_height = output_height - (output_height % rounding)

        return (output_width, output_height)

NODE_CLASS_MAPPINGS = {"OptimalCrop": OptimalCrop}
NODE_DISPLAY_NAME_MAPPINGS = {"OptimalCrop": "👑 OptimalCrop"}
