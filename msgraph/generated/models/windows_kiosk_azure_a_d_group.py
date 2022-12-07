from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

windows_kiosk_user = lazy_import('msgraph.generated.models.windows_kiosk_user')

class WindowsKioskAzureADGroup(windows_kiosk_user.WindowsKioskUser):
    def __init__(self,) -> None:
        """
        Instantiates a new WindowsKioskAzureADGroup and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windowsKioskAzureADGroup"
        # The display name of the AzureAD group that will be locked to this kiosk configuration
        self._display_name: Optional[str] = None
        # The ID of the AzureAD group that will be locked to this kiosk configuration
        self._group_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsKioskAzureADGroup:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsKioskAzureADGroup
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsKioskAzureADGroup()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The display name of the AzureAD group that will be locked to this kiosk configuration
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display name of the AzureAD group that will be locked to this kiosk configuration
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "group_id": lambda n : setattr(self, 'group_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def group_id(self,) -> Optional[str]:
        """
        Gets the groupId property value. The ID of the AzureAD group that will be locked to this kiosk configuration
        Returns: Optional[str]
        """
        return self._group_id
    
    @group_id.setter
    def group_id(self,value: Optional[str] = None) -> None:
        """
        Sets the groupId property value. The ID of the AzureAD group that will be locked to this kiosk configuration
        Args:
            value: Value to set for the groupId property.
        """
        self._group_id = value
    
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
        writer.write_str_value("groupId", self.group_id)
    

