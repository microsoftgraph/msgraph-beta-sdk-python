from enum import Enum

class AppleDeploymentChannel(Enum):
    # Send payload down over Device Channel.
    DeviceChannel = "deviceChannel",
    # Send payload down over User Channel.
    UserChannel = "userChannel",

