from enum import Enum

class OperationApprovalSource(str, Enum):
    # Default. Indicates the source of the action on the approval request is unknown.
    Unknown = "unknown",
    # Indicates the source of the action on the approval request is from an interactive session using the Intune Admin Console.
    AdminConsole = "adminConsole",
    # Indicates the source of the action on the approval request is from an email based form.
    Email = "email",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

