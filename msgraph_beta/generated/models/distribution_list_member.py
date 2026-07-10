from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .contact import Contact
    from .entity import Entity
    from .recipient_type import RecipientType

from .entity import Entity

@dataclass
class DistributionListMember(Entity, Parsable):
    # The contact property
    contact: Optional[Contact] = None
    # The ID of the referenced contact, if applicable. Read-only.
    contact_id: Optional[str] = None
    # The display name of the member. Read-only.
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The recipientType property
    recipient_type: Optional[RecipientType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DistributionListMember:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DistributionListMember
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DistributionListMember()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .contact import Contact
        from .entity import Entity
        from .recipient_type import RecipientType

        from .contact import Contact
        from .entity import Entity
        from .recipient_type import RecipientType

        fields: dict[str, Callable[[Any], None]] = {
            "contact": lambda n : setattr(self, 'contact', n.get_object_value(Contact)),
            "contactId": lambda n : setattr(self, 'contact_id', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "recipientType": lambda n : setattr(self, 'recipient_type', n.get_enum_value(RecipientType)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_object_value("contact", self.contact)
        writer.write_str_value("contactId", self.contact_id)
        writer.write_str_value("displayName", self.display_name)
        writer.write_enum_value("recipientType", self.recipient_type)
    

