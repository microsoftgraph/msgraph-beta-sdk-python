from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .applicable_content_device_match import ApplicableContentDeviceMatch
    from .catalog_entry import CatalogEntry

@dataclass
class ApplicableContent(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The catalogEntry property
    catalog_entry: Optional[CatalogEntry] = None
    # Collection of devices and recommendations for applicable catalog content.
    matched_devices: Optional[List[ApplicableContentDeviceMatch]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ApplicableContent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ApplicableContent
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ApplicableContent()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .applicable_content_device_match import ApplicableContentDeviceMatch
        from .catalog_entry import CatalogEntry

        from .applicable_content_device_match import ApplicableContentDeviceMatch
        from .catalog_entry import CatalogEntry

        fields: Dict[str, Callable[[Any], None]] = {
            "catalogEntry": lambda n : setattr(self, 'catalog_entry', n.get_object_value(CatalogEntry)),
            "matchedDevices": lambda n : setattr(self, 'matched_devices', n.get_collection_of_object_values(ApplicableContentDeviceMatch)),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_object_value("catalogEntry", self.catalog_entry)
        writer.write_collection_of_object_values("matchedDevices", self.matched_devices)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

