from enum import Enum

class EligibilityFilteringEnabledEntities(Enum):
    None_ = "none",
    SwapRequest = "swapRequest",
    OfferShiftRequest = "offerShiftRequest",
    UnknownFutureValue = "unknownFutureValue",
    TimeOffReason = "timeOffReason",

