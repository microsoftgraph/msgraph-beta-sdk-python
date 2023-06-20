from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import applicable_content_device_match, catalog_entry

@dataclass
class ApplicableContent(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The catalogEntry property
    catalog_entry: Optional[catalog_entry.CatalogEntry] = None
    # Collection of devices and recommendations for applicable catalog content.
    matched_devices: Optional[List[applicable_content_device_match.ApplicableContentDeviceMatch]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ApplicableContent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
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
        from . import applicable_content_device_match, catalog_entry

        from . import applicable_content_device_match, catalog_entry

        fields: Dict[str, Callable[[Any], None]] = {
            "catalogEntry": lambda n : setattr(self, 'catalog_entry', n.get_object_value(catalog_entry.CatalogEntry)),
            "matchedDevices": lambda n : setattr(self, 'matched_devices', n.get_collection_of_object_values(applicable_content_device_match.ApplicableContentDeviceMatch)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_object_value("catalogEntry", self.catalog_entry)
        writer.write_collection_of_object_values("matchedDevices", self.matched_devices)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

