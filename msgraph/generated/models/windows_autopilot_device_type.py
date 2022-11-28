from enum import Enum

class WindowsAutopilotDeviceType(Enum):
    # Windows PC
    WindowsPc = "windowsPc",
    # Surface Hub 2
    SurfaceHub2 = "surfaceHub2",
    # HoloLens
    HoloLens = "holoLens",
    # SurfaceHub2S
    SurfaceHub2S = "surfaceHub2S",
    # VirtualMachine
    VirtualMachine = "virtualMachine",
    # Placeholder for evolvable enum, but this enum is never returned to the caller, so it shouldn't be necessary.         
    UnknownFutureValue = "unknownFutureValue",

