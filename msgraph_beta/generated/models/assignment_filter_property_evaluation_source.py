from enum import Enum

class AssignmentFilterPropertyEvaluationSource(str, Enum):
    # The property is evaluated when the device checks in.
    DeviceCheckIn = "deviceCheckIn",
    # The property is evaluated from device inventory.
    DeviceInventory = "deviceInventory",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

