from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import windows_kiosk_user

from . import windows_kiosk_user

class WindowsKioskLocalGroup(windows_kiosk_user.WindowsKioskUser):
    def __init__(self,) -> None:
        """
        Instantiates a new WindowsKioskLocalGroup and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windowsKioskLocalGroup"
        # The name of the local group that will be locked to this kiosk configuration
        self._group_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsKioskLocalGroup:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsKioskLocalGroup
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsKioskLocalGroup()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import windows_kiosk_user

        fields: Dict[str, Callable[[Any], None]] = {
            "groupName": lambda n : setattr(self, 'group_name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def group_name(self,) -> Optional[str]:
        """
        Gets the groupName property value. The name of the local group that will be locked to this kiosk configuration
        Returns: Optional[str]
        """
        return self._group_name
    
    @group_name.setter
    def group_name(self,value: Optional[str] = None) -> None:
        """
        Sets the groupName property value. The name of the local group that will be locked to this kiosk configuration
        Args:
            value: Value to set for the group_name property.
        """
        self._group_name = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("groupName", self.group_name)
    

