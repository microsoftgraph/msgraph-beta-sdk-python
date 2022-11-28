from enum import Enum

class UserSignInRecommendationScope(Enum):
    Tenant = "tenant",
    Application = "application",
    UnknownFutureValue = "unknownFutureValue",

