from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class UserAccount(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The displayed name of the user account.
    account_name: Optional[str] = None
    # The user object identifier in Azure Active Directory (Azure AD).
    azure_ad_user_id: Optional[str] = None
    # The user display name in Azure AD.
    display_name: Optional[str] = None
    # The name of the Active Directory domain of which the user is a member.
    domain_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The user principal name of the account in Azure AD.
    user_principal_name: Optional[str] = None
    # The local security identifier of the user account.
    user_sid: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserAccount:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserAccount
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return UserAccount()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "accountName": lambda n : setattr(self, 'account_name', n.get_str_value()),
            "azureAdUserId": lambda n : setattr(self, 'azure_ad_user_id', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "domainName": lambda n : setattr(self, 'domain_name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "userPrincipalName": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
            "userSid": lambda n : setattr(self, 'user_sid', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("accountName", self.account_name)
        writer.write_str_value("azureAdUserId", self.azure_ad_user_id)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("domainName", self.domain_name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
        writer.write_str_value("userSid", self.user_sid)
        writer.write_additional_data_value(self.additional_data)
    

