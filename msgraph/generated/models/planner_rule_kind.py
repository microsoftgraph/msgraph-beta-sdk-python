from enum import Enum

class PlannerRuleKind(Enum):
    TaskRule = "taskRule",
    BucketRule = "bucketRule",
    PlanRule = "planRule",
    UnknownFutureValue = "unknownFutureValue",

