from enum import Enum

class DriverApprovalAction(str, Enum):
    # This indicates the action to approve single or list of drivers.
    Approve = "approve",
    # This indicates the action to approve single or list of drivers.
    Decline = "decline",
    # This indicates the action to suspend single or list of drivers.
    Suspend = "suspend",

