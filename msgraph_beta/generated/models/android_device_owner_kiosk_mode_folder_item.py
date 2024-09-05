from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .android_device_owner_kiosk_mode_app import AndroidDeviceOwnerKioskModeApp
    from .android_device_owner_kiosk_mode_home_screen_item import AndroidDeviceOwnerKioskModeHomeScreenItem
    from .android_device_owner_kiosk_mode_weblink import AndroidDeviceOwnerKioskModeWeblink

from .android_device_owner_kiosk_mode_home_screen_item import AndroidDeviceOwnerKioskModeHomeScreenItem

@dataclass
class AndroidDeviceOwnerKioskModeFolderItem(AndroidDeviceOwnerKioskModeHomeScreenItem):
    """
    Represents an item that can be added to Android Device Owner folder (application or weblink)
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.androidDeviceOwnerKioskModeFolderItem"
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AndroidDeviceOwnerKioskModeFolderItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AndroidDeviceOwnerKioskModeFolderItem
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidDeviceOwnerKioskModeApp".casefold():
            from .android_device_owner_kiosk_mode_app import AndroidDeviceOwnerKioskModeApp

            return AndroidDeviceOwnerKioskModeApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidDeviceOwnerKioskModeWeblink".casefold():
            from .android_device_owner_kiosk_mode_weblink import AndroidDeviceOwnerKioskModeWeblink

            return AndroidDeviceOwnerKioskModeWeblink()
        return AndroidDeviceOwnerKioskModeFolderItem()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .android_device_owner_kiosk_mode_app import AndroidDeviceOwnerKioskModeApp
        from .android_device_owner_kiosk_mode_home_screen_item import AndroidDeviceOwnerKioskModeHomeScreenItem
        from .android_device_owner_kiosk_mode_weblink import AndroidDeviceOwnerKioskModeWeblink

        from .android_device_owner_kiosk_mode_app import AndroidDeviceOwnerKioskModeApp
        from .android_device_owner_kiosk_mode_home_screen_item import AndroidDeviceOwnerKioskModeHomeScreenItem
        from .android_device_owner_kiosk_mode_weblink import AndroidDeviceOwnerKioskModeWeblink

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
    

