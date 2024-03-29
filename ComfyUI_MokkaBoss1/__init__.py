from ComfyUI_MokkaBoss1.nodes.DoubleClipTextEncode import DoubleClipTextEncode
from ComfyUI_MokkaBoss1.nodes.HashText import HashText
from ComfyUI_MokkaBoss1.nodes.IndoorBackgrounds import IndoorBackgrounds
from ComfyUI_MokkaBoss1.nodes.LandscapeBackgrounds import LandscapeBackgrounds
from ComfyUI_MokkaBoss1.nodes.NatureColours import NatureColours
from ComfyUI_MokkaBoss1.nodes.OptimalCrop import OptimalCrop
from ComfyUI_MokkaBoss1.nodes.seveninabox import seveninabox
from ComfyUI_MokkaBoss1.nodes.UrbanColours import UrbanColours
from ComfyUI_MokkaBoss1.nodes.X_In_a_Dress import X_In_a_Dress
from ComfyUI_MokkaBoss1.nodes.X_In_a_Suit import X_In_a_Suit
from ComfyUI_MokkaBoss1.nodes.WrapText import WrapText
from ComfyUI_MokkaBoss1.nodes.AspectRatioCondition import AspectRatioCondition

NODE_CLASS_MAPPINGS = {
    "DoubleClipTextEncode": DoubleClipTextEncode,
    "HashText": HashText,
    "IndoorBackgrounds": IndoorBackgrounds,   
    "LandscapeBackgrounds": LandscapeBackgrounds,
    "NatureColours": NatureColours,
    "OptimalCrop": OptimalCrop,
    "seveninabox": seveninabox,
    "UrbanColours": UrbanColours,
    "X_In_a_Dress": X_In_a_Dress,
    "X_In_a_Suit": X_In_a_Suit,
    "WrapText": WrapText,
    "AspectRatioCondition": AspectRatioCondition,
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "DoubleClipTextEncode": "👑 DoubleClipTextEncode",
    "HashText": "👑 HashText",
    "IndoorBackgrounds": "👑 IndoorBackgrounds",
    "LandscapeBackgrounds": "👑 LandscapeBackgrounds",
    "NatureColours": "👑 NatureColours",
    "OptimalCrop": "👑 OptimalCrop",
    "seveninabox": "👑 seveninabox",
    "UrbanColours": "👑 UrbanColours",
    "X_In_a_Dress": "👑 X_In_a_Dress",
    "X_In_a_Suit": "👑 X_In_a_Suit",
    "WrapText": "👑 WrapText"
    "AspectRatioCondition": "👑 AspectRatioCondition"
}
print ("Mokkaboss1 Custom Nodes: Loaded")