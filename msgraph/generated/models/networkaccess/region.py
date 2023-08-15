from enum import Enum

class Region(str, Enum):
    EastUS = "eastUS",
    EastUS2 = "eastUS2",
    WestUS = "westUS",
    WestUS2 = "westUS2",
    WestUS3 = "westUS3",
    CentralUS = "centralUS",
    NorthCentralUS = "northCentralUS",
    SouthCentralUS = "southCentralUS",
    NorthEurope = "northEurope",
    WestEurope = "westEurope",
    FranceCentral = "franceCentral",
    GermanyWestCentral = "germanyWestCentral",
    SwitzerlandNorth = "switzerlandNorth",
    UkSouth = "ukSouth",
    CanadaEast = "canadaEast",
    CanadaCentral = "canadaCentral",
    SouthAfricaWest = "southAfricaWest",
    SouthAfricaNorth = "southAfricaNorth",
    UaeNorth = "uaeNorth",
    UnknownFutureValue = "unknownFutureValue",

