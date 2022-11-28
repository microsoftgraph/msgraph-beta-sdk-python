from enum import Enum

class SynchronizationJobRestartScope(Enum):
    None_escaped = "None",
    ConnectorDataStore = "ConnectorDataStore",
    Escrows = "Escrows",
    Watermark = "Watermark",
    QuarantineState = "QuarantineState",
    Full = "Full",
    ForceDeletes = "ForceDeletes",

