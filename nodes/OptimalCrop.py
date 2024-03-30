# # # https://github.com/MokkaBoss1/ComfyUI-Mokkaboss1/wiki/Documentation-for-the-ComfyUI-Nodes-in-this-Node-Pack
# # # Node to calculate the optimal output width and height based on an input width and height AND aspect ratio
# # class TestOptimalCrop:

# class OptimalCrop:

    # def __init__(self):
        # pass
    
    # @classmethod
    # def INPUT_TYPES(cls):        
        # return {"required": {
            # "input_image": ("IMAGE", ),
            # "rounding": ("INT", {"default": 1, "min": 1, "max": 64, "step": 1}),
            # "aspect_ratio": ("FLOAT", {"default": 1.0, "min": 0, "max": 3.0, "step": 0.01}),
            # "x_offset": ("INT", {"default": 0, "min": 0, "max": 9999, "step": 1}),
            # "y_offset": ("INT", {"default": 0, "min": 0, "max": 9999, "step": 1}),
        # }}

    # RETURN_TYPES = ("IMAGE", )
    # RETURN_NAMES = ("crop_image", )
    # FUNCTION = "Optimal_Crop"
    # CATEGORY = "👑 MokkaBoss1"

    # def Optimal_Crop(self, input_image, rounding, aspect_ratio, x_offset, y_offset):
    
        # # get the width and the height of the input image
        # _, input_height, input_width, _ = input_image.shape
    
        # # Calculate output width based on input width and aspect ratio
        # output_width = int(min(input_width, input_height * aspect_ratio))
        
        # # Calculate output height based on output width and aspect ratio
        # output_height = int(output_width / aspect_ratio)
        
        # # Ensure both width and height are divisible by the rounding value
        # output_width = output_width - (output_width % rounding)
        # output_height = output_height - (output_height % rounding)
        
        # # Calculate the actual cropping area based on the aspect ratio and offsets
        # crop_x1 = max(0, min(input_width - output_width, x_offset))
        # crop_y1 = max(0, min(input_height - output_height, y_offset))
        # crop_x2 = min(input_width, crop_x1 + output_width)
        # crop_y2 = min(input_height, crop_y1 + output_height)
        
        # crop_image = input_image[:, crop_y1:crop_y2, crop_x1:crop_x2, :]

        # return (crop_image, )

# NODE_CLASS_MAPPINGS = {"OptimalCrop": OptimalCrop}
# NODE_DISPLAY_NAME_MAPPINGS = {"OptimalCrop": "👑 OptimalCrop"}



class OptimalCrop:

    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):        
        return {"required": {
            "input_image": ("IMAGE", ),
            "rounding": ("INT", {"default": 1, "min": 1, "max": 64, "step": 1}),
            "aspect_ratio": ("FLOAT", {"default": 1.0, "min": 0, "max": 3.0, "step": 0.01}),
            "x_offset": ("INT", {"default": 0, "min": 0, "max": 9999, "step": 1}),
            "y_offset": ("INT", {"default": 0, "min": 0, "max": 9999, "step": 1}),
            "crop_factor": ("FLOAT", {"default": 1.0, "min": 1.0, "max": 3.0, "step": 0.01}),
        }}

    RETURN_TYPES = ("IMAGE", )
    RETURN_NAMES = ("crop_image", )
    FUNCTION = "Optimal_Crop"
    CATEGORY = "👑 MokkaBoss1"

    def Optimal_Crop(self, input_image, rounding, aspect_ratio, x_offset, y_offset, crop_factor):

        _, input_height, input_width, _ = input_image.shape
    
        # Calculate output width based on input width and aspect ratio
        output_width = int(min(input_width, input_height * aspect_ratio))
        
        # Calculate output height based on output width and aspect ratio
        output_height = int(output_width / aspect_ratio)
        
        print(f"The rounding value is {rounding}")
        
        # Ensure both width and height are divisible by 16
        output_width = output_width - (output_width % rounding)
        output_height = output_height - (output_height % rounding)
        
        # Calculate the actual cropping area based on the aspect ratio and offsets
        crop_x1 = max(0, min(input_width - output_width, x_offset))
        crop_y1 = max(0, min(input_height - output_height, y_offset))
        crop_x2 = min(input_width, crop_x1 + output_width)
        crop_y2 = min(input_height, crop_y1 + output_height)
        
        # Adjust cropping area based on the crop factor
        crop_width = crop_x2 - crop_x1
        crop_height = crop_y2 - crop_y1
        crop_width = max(1, int(crop_width / crop_factor))
        crop_height = max(1, int(crop_height / crop_factor))
        
        crop_image = input_image[:, crop_y1:crop_y1+crop_height, crop_x1:crop_x1+crop_width, :]

        return (crop_image, )

NODE_CLASS_MAPPINGS = {"OptimalCrop": OptimalCrop}
NODE_DISPLAY_NAME_MAPPINGS = {"OptimalCrop": "👑 OptimalCrop"}
