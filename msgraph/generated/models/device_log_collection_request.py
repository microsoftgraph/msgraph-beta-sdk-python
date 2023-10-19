from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_log_collection_template_type import DeviceLogCollectionTemplateType

@dataclass
class DeviceLogCollectionRequest(AdditionalDataHolder, BackedModel, Parsable):
    """
    Windows Log Collection request entity.
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The unique identifier
    id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Enum for the template type used for collecting logs
    template_type: Optional[DeviceLogCollectionTemplateType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceLogCollectionRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceLogCollectionRequest
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return DeviceLogCollectionRequest()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .device_log_collection_template_type import DeviceLogCollectionTemplateType

        from .device_log_collection_template_type import DeviceLogCollectionTemplateType

        fields: Dict[str, Callable[[Any], None]] = {
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "templateType": lambda n : setattr(self, 'template_type', n.get_enum_value(DeviceLogCollectionTemplateType)),
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
        writer.write_str_value("id", self.id)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_enum_value("templateType", self.template_type)
        writer.write_additional_data_value(self.additional_data)
    

