from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, windows_feature_update_catalog_item, windows_quality_update_catalog_item

from . import entity

@dataclass
class WindowsUpdateCatalogItem(entity.Entity):
    """
    Windows update catalog item entity
    """
    # The display name for the catalog item.
    display_name: Optional[str] = None
    # The last supported date for a catalog item
    end_of_support_date: Optional[datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The date the catalog item was released
    release_date_time: Optional[datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsUpdateCatalogItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsUpdateCatalogItem
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.windowsFeatureUpdateCatalogItem":
                from . import windows_feature_update_catalog_item

                return windows_feature_update_catalog_item.WindowsFeatureUpdateCatalogItem()
            if mapping_value == "#microsoft.graph.windowsQualityUpdateCatalogItem":
                from . import windows_quality_update_catalog_item

                return windows_quality_update_catalog_item.WindowsQualityUpdateCatalogItem()
        return WindowsUpdateCatalogItem()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, windows_feature_update_catalog_item, windows_quality_update_catalog_item

        fields: Dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "endOfSupportDate": lambda n : setattr(self, 'end_of_support_date', n.get_datetime_value()),
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
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("endOfSupportDate", self.end_of_support_date)
        writer.write_datetime_value("releaseDateTime", self.release_date_time)
    

