from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import android_device_owner_kiosk_mode_home_screen_item

from . import android_device_owner_kiosk_mode_home_screen_item

@dataclass
class AndroidDeviceOwnerKioskModeManagedFolderReference(android_device_owner_kiosk_mode_home_screen_item.AndroidDeviceOwnerKioskModeHomeScreenItem):
    odata_type = "#microsoft.graph.androidDeviceOwnerKioskModeManagedFolderReference"
    # Unique identifier for the folder
    folder_identifier: Optional[str] = None
    # Name of the folder
    folder_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AndroidDeviceOwnerKioskModeManagedFolderReference:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AndroidDeviceOwnerKioskModeManagedFolderReference
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AndroidDeviceOwnerKioskModeManagedFolderReference()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import android_device_owner_kiosk_mode_home_screen_item

        fields: Dict[str, Callable[[Any], None]] = {
            "folderIdentifier": lambda n : setattr(self, 'folder_identifier', n.get_str_value()),
            "folderName": lambda n : setattr(self, 'folder_name', n.get_str_value()),
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
        writer.write_str_value("folderIdentifier", self.folder_identifier)
        writer.write_str_value("folderName", self.folder_name)
    

