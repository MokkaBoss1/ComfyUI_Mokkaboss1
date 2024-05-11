# https://github.com/MokkaBoss1/ComfyUI_Mokkaboss1/wiki/Documentation-for-the-ComfyUI-Nodes-in-this-Node-Pack


# ███████╗ ██████╗  ██████╗ ███╗   ███╗ ██████╗██████╗  ██████╗ ██████╗ 
# ╚══███╔╝██╔═══██╗██╔═══██╗████╗ ████║██╔════╝██╔══██╗██╔═══██╗██╔══██╗
#   ███╔╝ ██║   ██║██║   ██║██╔████╔██║██║     ██████╔╝██║   ██║██████╔╝
#  ███╔╝  ██║   ██║██║   ██║██║╚██╔╝██║██║     ██╔══██╗██║   ██║██╔═══╝ 
# ███████╗╚██████╔╝╚██████╔╝██║ ╚═╝ ██║╚██████╗██║  ██║╚██████╔╝██║     
# ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝     ╚═╝ ╚═════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝     
                                                                      


class ZoomCrop:

    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):        
        return {"required": {
            "input_image": ("IMAGE", ),
            "rounding": ("INT", {"default": 1, "min": 1, "max": 64, "step": 1}),
            "zoom": ("FLOAT", {"default": 1.0, "min": 1, "max": 10.0, "step": 0.01}),
            "x_offset": ("INT", {"default": 0, "min": -9999, "max": 9999, "step": 1}),
            "y_offset": ("INT", {"default": 0, "min": -9999, "max": 9999, "step": 1}),
        }}

    RETURN_TYPES = ("IMAGE", )
    RETURN_NAMES = ("crop_image", )
    FUNCTION = "Zoom_Crop"
    CATEGORY = "👑 MokkaBoss1/Image"

    def Zoom_Crop(self, input_image, rounding, zoom, x_offset, y_offset):

        # dimensions of source image
        _, input_height, input_width, _ = input_image.shape

        # calculate output_width and output_height
        
        output_width = int(input_width / zoom)
        output_height = int(input_height / zoom)
        
        #calculate x and y coordinates for top left corner
        
        x = int((input_width - output_width) / 2)
        y = int((input_height - output_height) / 2)
        
        x_new = x - x_offset
        y_new = y + y_offset
        
        # now we have all the inputs for the crop: x_new, y_new, output_width & output_height

        # Calculate the actual cropping area based on the aspect ratio and offsets
        
        crop_x1 = max(0, min(input_width - output_width, x_new))
        crop_y1 = max(0, min(input_height - output_height, y_new))
        crop_x2 = min(input_width, crop_x1 + output_width)
        crop_y2 = min(input_height, crop_y1 + output_height)

        crop_image = input_image[:, crop_y1:crop_y2, crop_x1:crop_x2, :]

        return (crop_image, )

NODE_CLASS_MAPPINGS = {"ZoomCrop": ZoomCrop}
NODE_DISPLAY_NAME_MAPPINGS = {"ZoomCrop": "👑 ZoomCrop"}

