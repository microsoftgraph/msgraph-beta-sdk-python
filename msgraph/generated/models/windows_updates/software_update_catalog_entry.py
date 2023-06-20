from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import catalog_entry, driver_update_catalog_entry, feature_update_catalog_entry, quality_update_catalog_entry

from . import catalog_entry

@dataclass
class SoftwareUpdateCatalogEntry(catalog_entry.CatalogEntry):
    odata_type = "#microsoft.graph.windowsUpdates.softwareUpdateCatalogEntry"
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SoftwareUpdateCatalogEntry:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SoftwareUpdateCatalogEntry
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsUpdates.driverUpdateCatalogEntry".casefold():
            from . import driver_update_catalog_entry

            return driver_update_catalog_entry.DriverUpdateCatalogEntry()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsUpdates.featureUpdateCatalogEntry".casefold():
            from . import feature_update_catalog_entry

            return feature_update_catalog_entry.FeatureUpdateCatalogEntry()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsUpdates.qualityUpdateCatalogEntry".casefold():
            from . import quality_update_catalog_entry

            return quality_update_catalog_entry.QualityUpdateCatalogEntry()
        return SoftwareUpdateCatalogEntry()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import catalog_entry, driver_update_catalog_entry, feature_update_catalog_entry, quality_update_catalog_entry

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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
    

