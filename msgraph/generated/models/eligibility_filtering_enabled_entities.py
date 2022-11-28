from enum import Enum

class EligibilityFilteringEnabledEntities(Enum):
    None_escaped = "none",
    SwapRequest = "swapRequest",
    OfferShiftRequest = "offerShiftRequest",
    UnknownFutureValue = "unknownFutureValue",

