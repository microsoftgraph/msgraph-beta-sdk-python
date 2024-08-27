from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .content_filter import ContentFilter
    from .driver_update_filter import DriverUpdateFilter
    from .quality_update_filter import QualityUpdateFilter
    from .windows_update_filter import WindowsUpdateFilter

from .content_filter import ContentFilter

@dataclass
class SoftwareUpdateFilter(ContentFilter):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.windowsUpdates.softwareUpdateFilter"
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SoftwareUpdateFilter:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SoftwareUpdateFilter
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsUpdates.driverUpdateFilter".casefold():
            from .driver_update_filter import DriverUpdateFilter

            return DriverUpdateFilter()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsUpdates.qualityUpdateFilter".casefold():
            from .quality_update_filter import QualityUpdateFilter

            return QualityUpdateFilter()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsUpdates.windowsUpdateFilter".casefold():
            from .windows_update_filter import WindowsUpdateFilter

            return WindowsUpdateFilter()
        return SoftwareUpdateFilter()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .content_filter import ContentFilter
        from .driver_update_filter import DriverUpdateFilter
        from .quality_update_filter import QualityUpdateFilter
        from .windows_update_filter import WindowsUpdateFilter

        from .content_filter import ContentFilter
        from .driver_update_filter import DriverUpdateFilter
        from .quality_update_filter import QualityUpdateFilter
        from .windows_update_filter import WindowsUpdateFilter

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
    

