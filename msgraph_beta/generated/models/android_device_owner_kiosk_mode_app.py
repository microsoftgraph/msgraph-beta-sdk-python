from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .android_device_owner_kiosk_mode_folder_item import AndroidDeviceOwnerKioskModeFolderItem

from .android_device_owner_kiosk_mode_folder_item import AndroidDeviceOwnerKioskModeFolderItem

@dataclass
class AndroidDeviceOwnerKioskModeApp(AndroidDeviceOwnerKioskModeFolderItem):
    """
    An application on the Android Device Owner Managed Home Screen
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.androidDeviceOwnerKioskModeApp"
    # Class name of application
    class_name: Optional[str] = None
    # Package name of application
    package: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AndroidDeviceOwnerKioskModeApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AndroidDeviceOwnerKioskModeApp
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AndroidDeviceOwnerKioskModeApp()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .android_device_owner_kiosk_mode_folder_item import AndroidDeviceOwnerKioskModeFolderItem

        from .android_device_owner_kiosk_mode_folder_item import AndroidDeviceOwnerKioskModeFolderItem

        fields: Dict[str, Callable[[Any], None]] = {
            "className": lambda n : setattr(self, 'class_name', n.get_str_value()),
            "package": lambda n : setattr(self, 'package', n.get_str_value()),
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
        writer.write_str_value("className", self.class_name)
        writer.write_str_value("package", self.package)
    

