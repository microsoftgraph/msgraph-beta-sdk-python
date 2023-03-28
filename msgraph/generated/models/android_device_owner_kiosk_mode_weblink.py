from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import android_device_owner_kiosk_mode_folder_item

from . import android_device_owner_kiosk_mode_folder_item

class AndroidDeviceOwnerKioskModeWeblink(android_device_owner_kiosk_mode_folder_item.AndroidDeviceOwnerKioskModeFolderItem):
    def __init__(self,) -> None:
        """
        Instantiates a new AndroidDeviceOwnerKioskModeWeblink and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.androidDeviceOwnerKioskModeWeblink"
        # Display name for weblink
        self._label: Optional[str] = None
        # Link for weblink
        self._link: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AndroidDeviceOwnerKioskModeWeblink:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AndroidDeviceOwnerKioskModeWeblink
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AndroidDeviceOwnerKioskModeWeblink()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import android_device_owner_kiosk_mode_folder_item

        fields: Dict[str, Callable[[Any], None]] = {
            "label": lambda n : setattr(self, 'label', n.get_str_value()),
            "link": lambda n : setattr(self, 'link', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def label(self,) -> Optional[str]:
        """
        Gets the label property value. Display name for weblink
        Returns: Optional[str]
        """
        return self._label
    
    @label.setter
    def label(self,value: Optional[str] = None) -> None:
        """
        Sets the label property value. Display name for weblink
        Args:
            value: Value to set for the label property.
        """
        self._label = value
    
    @property
    def link(self,) -> Optional[str]:
        """
        Gets the link property value. Link for weblink
        Returns: Optional[str]
        """
        return self._link
    
    @link.setter
    def link(self,value: Optional[str] = None) -> None:
        """
        Sets the link property value. Link for weblink
        Args:
            value: Value to set for the link property.
        """
        self._link = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("label", self.label)
        writer.write_str_value("link", self.link)
    

