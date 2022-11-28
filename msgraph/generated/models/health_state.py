from enum import Enum

class HealthState(Enum):
    # Unknown state.
    Unknown = "unknown",
    # Healthy state.
    Healthy = "healthy",
    # Unhealthy state.
    Unhealthy = "unhealthy",

