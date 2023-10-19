from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .key_value import KeyValue

@dataclass
class OathTokenMetadata(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The enabled property
    enabled: Optional[bool] = None
    # The manufacturer property
    manufacturer: Optional[str] = None
    # The manufacturerProperties property
    manufacturer_properties: Optional[List[KeyValue]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The serialNumber property
    serial_number: Optional[str] = None
    # The tokenType property
    token_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OathTokenMetadata:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OathTokenMetadata
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return OathTokenMetadata()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .key_value import KeyValue

        from .key_value import KeyValue

        fields: Dict[str, Callable[[Any], None]] = {
            "enabled": lambda n : setattr(self, 'enabled', n.get_bool_value()),
            "manufacturer": lambda n : setattr(self, 'manufacturer', n.get_str_value()),
            "manufacturerProperties": lambda n : setattr(self, 'manufacturer_properties', n.get_collection_of_object_values(KeyValue)),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "serialNumber": lambda n : setattr(self, 'serial_number', n.get_str_value()),
            "tokenType": lambda n : setattr(self, 'token_type', n.get_str_value()),
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
        writer.write_bool_value("enabled", self.enabled)
        writer.write_str_value("manufacturer", self.manufacturer)
        writer.write_collection_of_object_values("manufacturerProperties", self.manufacturer_properties)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_str_value("serialNumber", self.serial_number)
        writer.write_str_value("tokenType", self.token_type)
        writer.write_additional_data_value(self.additional_data)
    

