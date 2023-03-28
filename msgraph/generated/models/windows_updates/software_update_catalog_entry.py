from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import catalog_entry, driver_update_catalog_entry, feature_update_catalog_entry, quality_update_catalog_entry

from . import catalog_entry

class SoftwareUpdateCatalogEntry(catalog_entry.CatalogEntry):
    def __init__(self,) -> None:
        """
        Instantiates a new SoftwareUpdateCatalogEntry and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windowsUpdates.softwareUpdateCatalogEntry"
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SoftwareUpdateCatalogEntry:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SoftwareUpdateCatalogEntry
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.windowsUpdates.driverUpdateCatalogEntry":
                from . import driver_update_catalog_entry

                return driver_update_catalog_entry.DriverUpdateCatalogEntry()
            if mapping_value == "#microsoft.graph.windowsUpdates.featureUpdateCatalogEntry":
                from . import feature_update_catalog_entry

                return feature_update_catalog_entry.FeatureUpdateCatalogEntry()
            if mapping_value == "#microsoft.graph.windowsUpdates.qualityUpdateCatalogEntry":
                from . import quality_update_catalog_entry

                return quality_update_catalog_entry.QualityUpdateCatalogEntry()
        return SoftwareUpdateCatalogEntry()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import catalog_entry, driver_update_catalog_entry, feature_update_catalog_entry, quality_update_catalog_entry

        fields: Dict[str, Callable[[Any], None]] = {
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
    

