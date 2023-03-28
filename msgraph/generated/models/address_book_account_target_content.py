from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import account_target_content

from . import account_target_content

class AddressBookAccountTargetContent(account_target_content.AccountTargetContent):
    def __init__(self,) -> None:
        """
        Instantiates a new AddressBookAccountTargetContent and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.addressBookAccountTargetContent"
        # List of user emails targeted for an attack simulation training campaign.
        self._account_target_emails: Optional[List[str]] = None
    
    @property
    def account_target_emails(self,) -> Optional[List[str]]:
        """
        Gets the accountTargetEmails property value. List of user emails targeted for an attack simulation training campaign.
        Returns: Optional[List[str]]
        """
        return self._account_target_emails
    
    @account_target_emails.setter
    def account_target_emails(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the accountTargetEmails property value. List of user emails targeted for an attack simulation training campaign.
        Args:
            value: Value to set for the account_target_emails property.
        """
        self._account_target_emails = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AddressBookAccountTargetContent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AddressBookAccountTargetContent
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AddressBookAccountTargetContent()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import account_target_content

        fields: Dict[str, Callable[[Any], None]] = {
            "accountTargetEmails": lambda n : setattr(self, 'account_target_emails', n.get_collection_of_primitive_values(str)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_primitive_values("accountTargetEmails", self.account_target_emails)
    

