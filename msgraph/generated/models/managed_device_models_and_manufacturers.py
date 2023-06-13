from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class ManagedDeviceModelsAndManufacturers(AdditionalDataHolder, Parsable):
    """
    Models and Manufactures meatadata for managed devices in the account
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # List of Manufactures for managed devices in the account
    device_manufacturers: Optional[List[str]] = None
    # List of Models for managed devices in the account
    device_models: Optional[List[str]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ManagedDeviceModelsAndManufacturers:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ManagedDeviceModelsAndManufacturers
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ManagedDeviceModelsAndManufacturers()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "deviceManufacturers": lambda n : setattr(self, 'device_manufacturers', n.get_collection_of_primitive_values(str)),
            "deviceModels": lambda n : setattr(self, 'device_models', n.get_collection_of_primitive_values(str)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_primitive_values("deviceManufacturers", self.device_manufacturers)
        writer.write_collection_of_primitive_values("deviceModels", self.device_models)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

