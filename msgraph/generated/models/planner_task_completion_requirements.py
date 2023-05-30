from enum import Enum

class PlannerTaskCompletionRequirements(Enum):
    None_ = "none",
    ChecklistCompletion = "checklistCompletion",
    UnknownFutureValue = "unknownFutureValue",

