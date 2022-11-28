from enum import Enum

class DeviceManagementTemplateLifecycleState(Enum):
    # Invalid
    Invalid = "invalid",
    # Draft
    Draft = "draft",
    # Active
    Active = "active",
    # Superseded
    Superseded = "superseded",
    # Deprecated
    Deprecated = "deprecated",
    # Retired
    Retired = "retired",

