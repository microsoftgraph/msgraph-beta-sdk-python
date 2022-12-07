from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

android_device_owner_kiosk_mode_home_screen_item = lazy_import('msgraph.generated.models.android_device_owner_kiosk_mode_home_screen_item')

class AndroidDeviceOwnerKioskModeManagedFolderReference(android_device_owner_kiosk_mode_home_screen_item.AndroidDeviceOwnerKioskModeHomeScreenItem):
    def __init__(self,) -> None:
        """
        Instantiates a new AndroidDeviceOwnerKioskModeManagedFolderReference and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.androidDeviceOwnerKioskModeManagedFolderReference"
        # Unique identifier for the folder
        self._folder_identifier: Optional[str] = None
        # Name of the folder
        self._folder_name: Optional[str] = None
    
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
    
    @property
    def folder_identifier(self,) -> Optional[str]:
        """
        Gets the folderIdentifier property value. Unique identifier for the folder
        Returns: Optional[str]
        """
        return self._folder_identifier
    
    @folder_identifier.setter
    def folder_identifier(self,value: Optional[str] = None) -> None:
        """
        Sets the folderIdentifier property value. Unique identifier for the folder
        Args:
            value: Value to set for the folderIdentifier property.
        """
        self._folder_identifier = value
    
    @property
    def folder_name(self,) -> Optional[str]:
        """
        Gets the folderName property value. Name of the folder
        Returns: Optional[str]
        """
        return self._folder_name
    
    @folder_name.setter
    def folder_name(self,value: Optional[str] = None) -> None:
        """
        Sets the folderName property value. Name of the folder
        Args:
            value: Value to set for the folderName property.
        """
        self._folder_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "folder_identifier": lambda n : setattr(self, 'folder_identifier', n.get_str_value()),
            "folder_name": lambda n : setattr(self, 'folder_name', n.get_str_value()),
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
    

