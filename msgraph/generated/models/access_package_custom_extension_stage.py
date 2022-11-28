from enum import Enum

class AccessPackageCustomExtensionStage(Enum):
    AssignmentRequestCreated = "assignmentRequestCreated",
    AssignmentRequestApproved = "assignmentRequestApproved",
    AssignmentRequestGranted = "assignmentRequestGranted",
    AssignmentRequestRemoved = "assignmentRequestRemoved",
    AssignmentFourteenDaysBeforeExpiration = "assignmentFourteenDaysBeforeExpiration",
    AssignmentOneDayBeforeExpiration = "assignmentOneDayBeforeExpiration",
    UnknownFutureValue = "unknownFutureValue",

