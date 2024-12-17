from enum import Enum

class RoadmapItemDeliveryStage(str, Enum):
    PrivatePreview = "privatePreview",
    PublicPreview = "publicPreview",
    Ga = "ga",
    UnknownFutureValue = "unknownFutureValue",

