from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import content_filter, driver_update_filter, windows_update_filter

from . import content_filter

@dataclass
class SoftwareUpdateFilter(content_filter.ContentFilter):
    odata_type = "#microsoft.graph.windowsUpdates.softwareUpdateFilter"
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SoftwareUpdateFilter:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SoftwareUpdateFilter
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsUpdates.driverUpdateFilter".casefold():
            from . import driver_update_filter

            return driver_update_filter.DriverUpdateFilter()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsUpdates.windowsUpdateFilter".casefold():
            from . import windows_update_filter

            return windows_update_filter.WindowsUpdateFilter()
        return SoftwareUpdateFilter()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import content_filter, driver_update_filter, windows_update_filter

        from . import content_filter, driver_update_filter, windows_update_filter

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
    

