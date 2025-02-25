from enum import Enum

class IngestionSource(str, Enum):
    # Indicates unknown category
    Unknown = "unknown",
    # Indicates the category is ingested by IT admin with sufficient permissions through custom ingestion process
    Custom = "custom",
    # Indicates the category is ingested through system ingestion process
    BuiltIn = "builtIn",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

