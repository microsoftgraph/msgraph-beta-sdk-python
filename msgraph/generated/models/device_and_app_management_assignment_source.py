from enum import Enum

class DeviceAndAppManagementAssignmentSource(Enum):
    # Direct indicates a direct assignment.
    Direct = "direct",
    # PolicySets indicates assignment was made via PolicySet assignment.
    PolicySets = "policySets",

