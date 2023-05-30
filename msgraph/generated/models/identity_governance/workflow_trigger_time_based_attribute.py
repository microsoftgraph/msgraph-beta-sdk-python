from enum import Enum

class WorkflowTriggerTimeBasedAttribute(Enum):
    EmployeeHireDate = "employeeHireDate",
    EmployeeLeaveDateTime = "employeeLeaveDateTime",
    UnknownFutureValue = "unknownFutureValue",
    CreatedDateTime = "createdDateTime",

