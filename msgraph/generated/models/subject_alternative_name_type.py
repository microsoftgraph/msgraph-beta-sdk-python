from enum import Enum

class SubjectAlternativeNameType(Enum):
    # No subject alternative name.
    None_escaped = "none",
    # Email address.
    EmailAddress = "emailAddress",
    # User Principal Name (UPN).
    UserPrincipalName = "userPrincipalName",
    # Custom Azure AD Attribute.
    CustomAzureADAttribute = "customAzureADAttribute",
    # Domain Name Service (DNS).
    DomainNameService = "domainNameService",
    # Universal Resource Identifier (URI).
    UniversalResourceIdentifier = "universalResourceIdentifier",

