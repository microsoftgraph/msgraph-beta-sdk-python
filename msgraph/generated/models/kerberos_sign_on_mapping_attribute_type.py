from enum import Enum

class KerberosSignOnMappingAttributeType(Enum):
    UserPrincipalName = "userPrincipalName",
    OnPremisesUserPrincipalName = "onPremisesUserPrincipalName",
    UserPrincipalUsername = "userPrincipalUsername",
    OnPremisesUserPrincipalUsername = "onPremisesUserPrincipalUsername",
    OnPremisesSAMAccountName = "onPremisesSAMAccountName",

