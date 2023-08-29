from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .android_device_owner_kiosk_mode_folder_item import AndroidDeviceOwnerKioskModeFolderItem

from .android_device_owner_kiosk_mode_folder_item import AndroidDeviceOwnerKioskModeFolderItem

@dataclass
class AndroidDeviceOwnerKioskModeWeblink(AndroidDeviceOwnerKioskModeFolderItem):
    """
    A weblink on the Android Device Owner Managed Home Screen
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.androidDeviceOwnerKioskModeWeblink"
    # Display name for weblink
    label: Optional[str] = None
    # Link for weblink
    link: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AndroidDeviceOwnerKioskModeWeblink:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AndroidDeviceOwnerKioskModeWeblink
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AndroidDeviceOwnerKioskModeWeblink()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .android_device_owner_kiosk_mode_folder_item import AndroidDeviceOwnerKioskModeFolderItem

        from .android_device_owner_kiosk_mode_folder_item import AndroidDeviceOwnerKioskModeFolderItem

        fields: Dict[str, Callable[[Any], None]] = {
            "label": lambda n : setattr(self, 'label', n.get_str_value()),
            "link": lambda n : setattr(self, 'link', n.get_str_value()),
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
        writer.write_str_value("label", self.label)
        writer.write_str_value("link", self.link)
    

