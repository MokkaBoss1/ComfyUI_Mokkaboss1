# https://github.com/MokkaBoss1/ComfyUI-Mokkaboss1/wiki/Documentation-for-the-ComfyUI-Nodes-in-this-Node-Pack

from PIL import Image, ImageDraw, ImageFont, ImageColor, ImageFilter




class ImageDimensions:
    
    def __init__(self):
        pass
    
    
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE",),
            }
        }

    RETURN_TYPES = ("INT", "INT", "FLOAT", "FLOAT","STRING")
    RETURN_NAMES = ("width", "height", "ratio", "megapixels","parameters")
    FUNCTION = "im_dim"
    CATEGORY = "👑 MokkaBoss1/Image"

    def im_dim(self, image):
        
        ratio = round((image.shape[2] / image.shape[1]),3)
        megapixels = round((( image.shape[2] * image.shape[1] ) / 1048576),3)
        parameters = f"Width: {image.shape[2]}\nHeight: {image.shape[1]}\nAspect Ratio: {ratio}\nMegapixels: {megapixels}"

        
        
        return (image.shape[2], image.shape[1], ratio, megapixels, parameters)
    
NODE_CLASS_MAPPINGS = {"ImageDimensions": ImageDimensions}
NODE_DISPLAY_NAME_MAPPINGS = {"ImageDimensions": "👑 ImageDimensions"}