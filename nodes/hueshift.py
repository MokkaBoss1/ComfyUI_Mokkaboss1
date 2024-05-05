import cv2
import numpy as np
from PIL import Image
import torch


def tensor2pil(image):
    return Image.fromarray(np.clip(255. * image.cpu().numpy().squeeze(), 0, 255).astype(np.uint8))


def pil2tensor(image):
    return torch.from_numpy(np.array(image).astype(np.float32) / 255.0).unsqueeze(0)


def pil2opencv(image_pil):
    if image_pil is None:
        print("Received None as input PIL image.")
        return None
    image_np = np.array(image_pil)
    return image_np[:, :, ::-1]  # Reverse RGB to BGR


class HueShift:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),
                "degrees": ("INT", {"default": 0, "min": 0, "max": 360})
            }
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("output_image",)
    FUNCTION = "hue_shift"
    CATEGORY = "👑 MokkaBoss1/Image"

    @staticmethod
    def hue_shift(image, degrees):
        image_pil = tensor2pil(image)
        if image_pil is None:
            return None
        image_cv = pil2opencv(image_pil)
        if image_cv is None:
            print("Failed to convert PIL image to OpenCV format.")
            return None
        try:
            hsv_image = cv2.cvtColor(image_cv, cv2.COLOR_BGR2HSV)
            hue_shift = int((degrees / 360.0) * 180)
            hsv_image[:, :, 0] = (hsv_image[:, :, 0] + hue_shift) % 180
            bgr_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)
            rgb_image = bgr_image[:, :, ::-1]

            image_tensor = pil2tensor(rgb_image)

            return (image_tensor,)
        except cv2.error as e:
            print(f"OpenCV error in cvtColor or hue adjustment: {e}")
            return None


NODE_CLASS_MAPPINGS = {"HueShift": HueShift}
NODE_DISPLAY_NAME_MAPPINGS = {"HueShift": "👑 Hue Shift"}
