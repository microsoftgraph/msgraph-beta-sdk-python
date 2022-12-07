from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

windows_kiosk_user = lazy_import('msgraph.generated.models.windows_kiosk_user')

class WindowsKioskActiveDirectoryGroup(windows_kiosk_user.WindowsKioskUser):
    def __init__(self,) -> None:
        """
        Instantiates a new WindowsKioskActiveDirectoryGroup and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windowsKioskActiveDirectoryGroup"
        # The name of the AD group that will be locked to this kiosk configuration
        self._group_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsKioskActiveDirectoryGroup:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsKioskActiveDirectoryGroup
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsKioskActiveDirectoryGroup()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "group_name": lambda n : setattr(self, 'group_name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def group_name(self,) -> Optional[str]:
        """
        Gets the groupName property value. The name of the AD group that will be locked to this kiosk configuration
        Returns: Optional[str]
        """
        return self._group_name
    
    @group_name.setter
    def group_name(self,value: Optional[str] = None) -> None:
        """
        Sets the groupName property value. The name of the AD group that will be locked to this kiosk configuration
        Args:
            value: Value to set for the groupName property.
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
    

