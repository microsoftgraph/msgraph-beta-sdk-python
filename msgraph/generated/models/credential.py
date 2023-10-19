from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class Credential(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The name of the field for this credential. e.g, username or password or phoneNumber. This is defined by the application. Must match what is in the html field on singleSignOnSettings/password object.
    field_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The type for this credential. Valid values: username, password, or other.
    type: Optional[str] = None
    # The value for this credential. e.g, mysuperhiddenpassword. Note the value for passwords is write-only, the value can never be read back.
    value: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Credential:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Credential
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Credential()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "fieldId": lambda n : setattr(self, 'field_id', n.get_str_value()),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
            "value": lambda n : setattr(self, 'value', n.get_str_value()),
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
        writer.write_str_value("fieldId", self.field_id)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_str_value("type", self.type)
        writer.write_str_value("value", self.value)
        writer.write_additional_data_value(self.additional_data)
    

