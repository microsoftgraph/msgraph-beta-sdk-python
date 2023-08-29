from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .windows_kiosk_user import WindowsKioskUser

from .windows_kiosk_user import WindowsKioskUser

@dataclass
class WindowsKioskLocalGroup(WindowsKioskUser):
    """
    The class used to identify a local group for the kiosk configuration
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.windowsKioskLocalGroup"
    # The name of the local group that will be locked to this kiosk configuration
    group_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsKioskLocalGroup:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsKioskLocalGroup
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return WindowsKioskLocalGroup()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .windows_kiosk_user import WindowsKioskUser

        from .windows_kiosk_user import WindowsKioskUser

        fields: Dict[str, Callable[[Any], None]] = {
            "groupName": lambda n : setattr(self, 'group_name', n.get_str_value()),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("groupName", self.group_name)
    

