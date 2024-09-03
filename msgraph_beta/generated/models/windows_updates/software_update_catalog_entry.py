from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .catalog_entry import CatalogEntry
    from .driver_update_catalog_entry import DriverUpdateCatalogEntry
    from .feature_update_catalog_entry import FeatureUpdateCatalogEntry
    from .quality_update_catalog_entry import QualityUpdateCatalogEntry

from .catalog_entry import CatalogEntry

@dataclass
class SoftwareUpdateCatalogEntry(CatalogEntry):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.windowsUpdates.softwareUpdateCatalogEntry"
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SoftwareUpdateCatalogEntry:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SoftwareUpdateCatalogEntry
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsUpdates.driverUpdateCatalogEntry".casefold():
            from .driver_update_catalog_entry import DriverUpdateCatalogEntry

            return DriverUpdateCatalogEntry()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsUpdates.featureUpdateCatalogEntry".casefold():
            from .feature_update_catalog_entry import FeatureUpdateCatalogEntry

            return FeatureUpdateCatalogEntry()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsUpdates.qualityUpdateCatalogEntry".casefold():
            from .quality_update_catalog_entry import QualityUpdateCatalogEntry

            return QualityUpdateCatalogEntry()
        return SoftwareUpdateCatalogEntry()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .catalog_entry import CatalogEntry
        from .driver_update_catalog_entry import DriverUpdateCatalogEntry
        from .feature_update_catalog_entry import FeatureUpdateCatalogEntry
        from .quality_update_catalog_entry import QualityUpdateCatalogEntry

        from .catalog_entry import CatalogEntry
        from .driver_update_catalog_entry import DriverUpdateCatalogEntry
        from .feature_update_catalog_entry import FeatureUpdateCatalogEntry
        from .quality_update_catalog_entry import QualityUpdateCatalogEntry

        fields: Dict[str, Callable[[Any], None]] = {
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
    

