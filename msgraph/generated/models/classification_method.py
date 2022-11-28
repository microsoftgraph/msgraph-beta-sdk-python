from enum import Enum

class ClassificationMethod(Enum):
    PatternMatch = "patternMatch",
    ExactDataMatch = "exactDataMatch",
    Fingerprint = "fingerprint",
    MachineLearning = "machineLearning",

