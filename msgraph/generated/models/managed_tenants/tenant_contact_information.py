from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class TenantContactInformation(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The email address for the contact. Optional
    email: Optional[str] = None
    # The name for the contact. Required.
    name: Optional[str] = None
    # The notes associated with the contact. Optional
    notes: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The phone number for the contact. Optional.
    phone: Optional[str] = None
    # The title for the contact. Required.
    title: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TenantContactInformation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TenantContactInformation
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return TenantContactInformation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "notes": lambda n : setattr(self, 'notes', n.get_str_value()),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "phone": lambda n : setattr(self, 'phone', n.get_str_value()),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("email", self.email)
        writer.write_str_value("name", self.name)
        writer.write_str_value("notes", self.notes)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_str_value("phone", self.phone)
        writer.write_str_value("title", self.title)
        writer.write_additional_data_value(self.additional_data)
    

