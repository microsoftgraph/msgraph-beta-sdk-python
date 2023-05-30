from enum import Enum

class AuthenticationAttributeCollectionInputType(Enum):
    Text = "text",
    RadioSingleSelect = "radioSingleSelect",
    CheckboxMultiSelect = "checkboxMultiSelect",
    Boolean = "boolean",
    UnknownFutureValue = "unknownFutureValue",

