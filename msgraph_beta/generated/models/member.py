from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .recipient_type import RecipientType

@dataclass
class Member(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The ID of the referenced contact, if applicable. Optional.
    contact_id: Optional[str] = None
    # The display name of the member. Optional.
    display_name: Optional[str] = None
    # The email address or routing key of the member. Required.
    key: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The recipientType property
    recipient_type: Optional[RecipientType] = None
    # The routing type for the member, for example, SMTP. Optional.
    routing_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Member:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Member
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Member()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .recipient_type import RecipientType

        from .recipient_type import RecipientType

        fields: dict[str, Callable[[Any], None]] = {
            "contactId": lambda n : setattr(self, 'contact_id', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "key": lambda n : setattr(self, 'key', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "recipientType": lambda n : setattr(self, 'recipient_type', n.get_enum_value(RecipientType)),
            "routingType": lambda n : setattr(self, 'routing_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("contactId", self.contact_id)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("key", self.key)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("recipientType", self.recipient_type)
        writer.write_str_value("routingType", self.routing_type)
        writer.write_additional_data_value(self.additional_data)
    

