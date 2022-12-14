from enum import Enum

class HorizontalSectionLayoutType(Enum):
    None_escaped = "none",
    OneColumn = "oneColumn",
    TwoColumns = "twoColumns",
    ThreeColumns = "threeColumns",
    OneThirdLeftColumn = "oneThirdLeftColumn",
    OneThirdRightColumn = "oneThirdRightColumn",
    FullWidth = "fullWidth",
    UnknownFutureValue = "unknownFutureValue",

