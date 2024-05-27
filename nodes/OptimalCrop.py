# https://github.com/MokkaBoss1/ComfyUI_Mokkaboss1/wiki/Documentation-for-the-ComfyUI-Nodes-in-this-Node-Pack
# MokkaBoss1 April 2024

#  ██████╗ ██████╗ ████████╗██╗███╗   ███╗ █████╗ ██╗      ██████╗██████╗  ██████╗ ██████╗ 
# ██╔═══██╗██╔══██╗╚══██╔══╝██║████╗ ████║██╔══██╗██║     ██╔════╝██╔══██╗██╔═══██╗██╔══██╗
# ██║   ██║██████╔╝   ██║   ██║██╔████╔██║███████║██║     ██║     ██████╔╝██║   ██║██████╔╝
# ██║   ██║██╔═══╝    ██║   ██║██║╚██╔╝██║██╔══██║██║     ██║     ██╔══██╗██║   ██║██╔═══╝ 
# ╚██████╔╝██║        ██║   ██║██║ ╚═╝ ██║██║  ██║███████╗╚██████╗██║  ██║╚██████╔╝██║     
#  ╚═════╝ ╚═╝        ╚═╝   ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝     

oc_aspectratios = [
    "9:21 640x1536 (0.42)",
    "9:19 704x1472 (0.48)",
    "9:16 768x1344 (0.57)",
    "5:8 768x1216 (0.63)",
    "2:3 832x1216 (0.68)",
    "3:4 896x1152 (0.78)",
    "1:1 1024x1024 (1.00)",
    "4:3 1152x896 (1.29)",
    "3:2 1216x832 (1.46)",
    "8:5 1216x768 (1.58)",
    "16:9 1344x768 (1.75)",
    "19:9 1472x704 (2.09)",
    "21:9 1536x640 (2.40)"
]

class OptimalCrop:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {
            "input_image": ("IMAGE", ),
            "rounding": ("INT", {"default": 1, "min": 1, "max": 64, "step": 1}),
            "aspect_ratio": ("STRING", {"default": "2:3 832x1216 (0.68)", "options": oc_aspectratios}),
            "x_offset": ("INT", {"default": 0, "min": -9999, "max": 9999, "step": 1}),
            "y_offset": ("INT", {"default": 0, "min": -9999, "max": 9999, "step": 1}),
        }}

    RETURN_TYPES = ("IMAGE", )
    RETURN_NAMES = ("crop_image", )
    FUNCTION = "Optimal_Crop"
    CATEGORY = "👑 MokkaBoss1/Image"

    def Optimal_Crop(self, input_image, rounding, aspect_ratio, x_offset, y_offset):
        width = 0
        height = 0

        if aspect_ratio == "1:1 1024x1024 (1.00)":
            width, height = 1024, 1024
        elif aspect_ratio == "2:3 832x1216 (0.68)":
            width, height = 832, 1216
        elif aspect_ratio == "3:4 896x1152 (0.78)":
            width, height = 896, 1152
        elif aspect_ratio == "5:8 768x1216 (0.63)":
            width, height = 768, 1216
        elif aspect_ratio == "9:16 768x1344 (0.57)":
            width, height = 768, 1344
        elif aspect_ratio == "9:19 704x1472 (0.48)":
            width, height = 704, 1472
        elif aspect_ratio == "9:21 640x1536 (0.42)":
            width, height = 640, 1536
        elif aspect_ratio == "3:2 1216x832 (1.46)":
            width, height = 1216, 832
        elif aspect_ratio == "4:3 1152x896 (1.29)":
            width, height = 1152, 896
        elif aspect_ratio == "8:5 1216x768 (1.58)":
            width, height = 1216, 768
        elif aspect_ratio == "16:9 1344x768 (1.75)":
            width, height = 1344, 768
        elif aspect_ratio == "19:9 1472x704 (2.09)":
            width, height = 1472, 704
        elif aspect_ratio == "21:9 1536x640 (2.40)":
            width, height = 1536, 640
        else:
            width, height = 1024, 1024

        ratio = float(width / height)

        _, input_height, input_width, _ = input_image.shape

        # Calculate output width based on input width and aspect ratio
        output_width = int(min(input_width, input_height * ratio))

        # Calculate output height based on output width and aspect ratio
        output_height = int(output_width / ratio)

        # Ensure both width and height are divisible by the rounding value
        output_width = output_width - (output_width % rounding)
        output_height = output_height - (output_height % rounding)

        # Calculate delta to x_offset and y_offset
        x_offset = int((input_width - output_width) * 0.5) - x_offset
        y_offset = y_offset + int((input_height - output_height) * 0.5)

        # Calculate the actual cropping area based on the aspect ratio and offsets
        crop_x1 = max(0, min(input_width - output_width, x_offset))
        crop_y1 = max(0, min(input_height - output_height, y_offset))
        crop_x2 = min(input_width, crop_x1 + output_width)
        crop_y2 = min(input_height, crop_y1 + output_height)

        print(f"crop_x1: {crop_x1} crop_x2: {crop_x2} crop_y1: {crop_y1} crop_y2: {crop_y2}")

        crop_image = input_image[:, crop_y1:crop_y2, crop_x1:crop_x2, :]

        return (crop_image,)

NODE_CLASS_MAPPINGS = {"OptimalCrop": OptimalCrop}
NODE_DISPLAY_NAME_MAPPINGS = {"OptimalCrop": "👑 OptimalCrop"}
