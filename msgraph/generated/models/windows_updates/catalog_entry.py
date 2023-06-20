from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import driver_update_catalog_entry, feature_update_catalog_entry, quality_update_catalog_entry, software_update_catalog_entry
    from .. import entity

from .. import entity

@dataclass
class CatalogEntry(entity.Entity):
    # The date on which the content is no longer available to deploy using the service. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
    deployable_until_date_time: Optional[datetime] = None
    # The display name of the content. Read-only.
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The release date for the content. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
    release_date_time: Optional[datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CatalogEntry:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CatalogEntry
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
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsUpdates.softwareUpdateCatalogEntry".casefold():
            from . import software_update_catalog_entry

            return software_update_catalog_entry.SoftwareUpdateCatalogEntry()
        return CatalogEntry()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import driver_update_catalog_entry, feature_update_catalog_entry, quality_update_catalog_entry, software_update_catalog_entry
        from .. import entity

        from . import driver_update_catalog_entry, feature_update_catalog_entry, quality_update_catalog_entry, software_update_catalog_entry
        from .. import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "deployableUntilDateTime": lambda n : setattr(self, 'deployable_until_date_time', n.get_datetime_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "releaseDateTime": lambda n : setattr(self, 'release_date_time', n.get_datetime_value()),
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
        writer.write_datetime_value("deployableUntilDateTime", self.deployable_until_date_time)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("releaseDateTime", self.release_date_time)
    

