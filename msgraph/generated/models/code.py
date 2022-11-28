from enum import Enum

class Code(Enum):
    # None error.
    None_escaped = "none",
    # Json file invalid error.
    JsonFileInvalid = "jsonFileInvalid",
    # Json file missing error.
    JsonFileMissing = "jsonFileMissing",
    # Json file too large error.
    JsonFileTooLarge = "jsonFileTooLarge",
    # Rules missing error.
    RulesMissing = "rulesMissing",
    # Duplicate rules error.
    DuplicateRules = "duplicateRules",
    # Too many rules specified error.
    TooManyRulesSpecified = "tooManyRulesSpecified",
    # Operator missing error.
    OperatorMissing = "operatorMissing",
    # Operator not supported error.
    OperatorNotSupported = "operatorNotSupported",
    # Data type missing error.
    DatatypeMissing = "datatypeMissing",
    # Data type not supported error.
    DatatypeNotSupported = "datatypeNotSupported",
    # Operator data type combination not supported error.
    OperatorDataTypeCombinationNotSupported = "operatorDataTypeCombinationNotSupported",
    # More info urlmissing error.
    MoreInfoUriMissing = "moreInfoUriMissing",
    # More info url invalid error.
    MoreInfoUriInvalid = "moreInfoUriInvalid",
    # More info ur ltoo large error.
    MoreInfoUriTooLarge = "moreInfoUriTooLarge",
    # Description missing error.
    DescriptionMissing = "descriptionMissing",
    # Description invalid error.
    DescriptionInvalid = "descriptionInvalid",
    # Description too large error.
    DescriptionTooLarge = "descriptionTooLarge",
    # Title missing error.
    TitleMissing = "titleMissing",
    # Title invalid error.
    TitleInvalid = "titleInvalid",
    # Title too large error.
    TitleTooLarge = "titleTooLarge",
    # Operand missing error.
    OperandMissing = "operandMissing",
    # Operand invalid error.
    OperandInvalid = "operandInvalid",
    # Operand too large error.
    OperandTooLarge = "operandTooLarge",
    # Setting name missing error.
    SettingNameMissing = "settingNameMissing",
    # Setting name invalid error.
    SettingNameInvalid = "settingNameInvalid",
    # Setting name too large error.
    SettingNameTooLarge = "settingNameTooLarge",
    # English locale missing error.
    EnglishLocaleMissing = "englishLocaleMissing",
    # Duplicate locales error.
    DuplicateLocales = "duplicateLocales",
    # Unrecognized locale error.
    UnrecognizedLocale = "unrecognizedLocale",
    # Unknown error.
    Unknown = "unknown",
    # Remediation strings missing error.
    RemediationStringsMissing = "remediationStringsMissing",

