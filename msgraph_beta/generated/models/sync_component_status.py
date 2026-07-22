from enum import Enum

class SyncComponentStatus(str, Enum):
    # Default. The component has not yet started reporting status. This is a schema default and will not typically appear in responses, as components only appear once they begin executing.
    None_ = "none",
    # Indicates the component is currently executing. For infrastructure components (PNSv1, DCI, SCGW), this means the notification or check-in is in flight. For policies, this means the policy is being applied to the device.
    InProgress = "inProgress",
    # Indicates the component completed successfully. The component has finished its work and reported a successful outcome.
    Success = "success",
    # Indicates the stage encountered an error. When this value is set, the moreInfo property on the syncComponent will contain additional diagnostic details about the failure.
    Failure = "failure",
    # Indicates the stage completed but not all items succeeded. For example, some policies applied successfully while others failed. The moreInfo property may contain details on the partial outcome.
    PartialSuccess = "partialSuccess",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

