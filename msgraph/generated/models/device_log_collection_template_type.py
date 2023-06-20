from enum import Enum

class DeviceLogCollectionTemplateType(str, Enum):
    # Predefined template for what will be collected
    Predefined = "predefined",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

