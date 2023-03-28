from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import android_device_owner_kiosk_mode_app, android_device_owner_kiosk_mode_home_screen_item, android_device_owner_kiosk_mode_weblink

from . import android_device_owner_kiosk_mode_home_screen_item

class AndroidDeviceOwnerKioskModeFolderItem(android_device_owner_kiosk_mode_home_screen_item.AndroidDeviceOwnerKioskModeHomeScreenItem):
    def __init__(self,) -> None:
        """
        Instantiates a new AndroidDeviceOwnerKioskModeFolderItem and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.androidDeviceOwnerKioskModeFolderItem"
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AndroidDeviceOwnerKioskModeFolderItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AndroidDeviceOwnerKioskModeFolderItem
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.androidDeviceOwnerKioskModeApp":
                from . import android_device_owner_kiosk_mode_app

                return android_device_owner_kiosk_mode_app.AndroidDeviceOwnerKioskModeApp()
            if mapping_value == "#microsoft.graph.androidDeviceOwnerKioskModeWeblink":
                from . import android_device_owner_kiosk_mode_weblink

                return android_device_owner_kiosk_mode_weblink.AndroidDeviceOwnerKioskModeWeblink()
        return AndroidDeviceOwnerKioskModeFolderItem()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import android_device_owner_kiosk_mode_app, android_device_owner_kiosk_mode_home_screen_item, android_device_owner_kiosk_mode_weblink

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
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
    

