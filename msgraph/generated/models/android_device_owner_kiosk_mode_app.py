from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

android_device_owner_kiosk_mode_folder_item = lazy_import('msgraph.generated.models.android_device_owner_kiosk_mode_folder_item')

class AndroidDeviceOwnerKioskModeApp(android_device_owner_kiosk_mode_folder_item.AndroidDeviceOwnerKioskModeFolderItem):
    @property
    def class_name(self,) -> Optional[str]:
        """
        Gets the className property value. Class name of application
        Returns: Optional[str]
        """
        return self._class_name
    
    @class_name.setter
    def class_name(self,value: Optional[str] = None) -> None:
        """
        Sets the className property value. Class name of application
        Args:
            value: Value to set for the className property.
        """
        self._class_name = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new AndroidDeviceOwnerKioskModeApp and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.androidDeviceOwnerKioskModeApp"
        # Class name of application
        self._class_name: Optional[str] = None
        # Package name of application
        self._package: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AndroidDeviceOwnerKioskModeApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AndroidDeviceOwnerKioskModeApp
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AndroidDeviceOwnerKioskModeApp()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "class_name": lambda n : setattr(self, 'class_name', n.get_str_value()),
            "package": lambda n : setattr(self, 'package', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def package(self,) -> Optional[str]:
        """
        Gets the package property value. Package name of application
        Returns: Optional[str]
        """
        return self._package
    
    @package.setter
    def package(self,value: Optional[str] = None) -> None:
        """
        Sets the package property value. Package name of application
        Args:
            value: Value to set for the package property.
        """
        self._package = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("className", self.class_name)
        writer.write_str_value("package", self.package)
    

