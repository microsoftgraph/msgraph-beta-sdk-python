from enum import Enum

class AssignmentFilterEvaluationResult(Enum):
    # Unknown.
    Unknown = "unknown",
    # Match.
    Match = "match",
    # NotMatch.
    NotMatch = "notMatch",
    # Inconclusive.
    Inconclusive = "inconclusive",
    # Failure.
    Failure = "failure",
    # NotEvaluated.
    NotEvaluated = "notEvaluated",

