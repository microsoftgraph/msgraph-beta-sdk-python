from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

windows_kiosk_app_base = lazy_import('msgraph.generated.models.windows_kiosk_app_base')

class WindowsKioskDesktopApp(windows_kiosk_app_base.WindowsKioskAppBase):
    def __init__(self,) -> None:
        """
        Instantiates a new WindowsKioskDesktopApp and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windowsKioskDesktopApp"
        # Define the DesktopApplicationID of the app
        self._desktop_application_id: Optional[str] = None
        # Define the DesktopApplicationLinkPath of the app
        self._desktop_application_link_path: Optional[str] = None
        # Define the path of a desktop app
        self._path: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsKioskDesktopApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsKioskDesktopApp
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsKioskDesktopApp()
    
    @property
    def desktop_application_id(self,) -> Optional[str]:
        """
        Gets the desktopApplicationId property value. Define the DesktopApplicationID of the app
        Returns: Optional[str]
        """
        return self._desktop_application_id
    
    @desktop_application_id.setter
    def desktop_application_id(self,value: Optional[str] = None) -> None:
        """
        Sets the desktopApplicationId property value. Define the DesktopApplicationID of the app
        Args:
            value: Value to set for the desktopApplicationId property.
        """
        self._desktop_application_id = value
    
    @property
    def desktop_application_link_path(self,) -> Optional[str]:
        """
        Gets the desktopApplicationLinkPath property value. Define the DesktopApplicationLinkPath of the app
        Returns: Optional[str]
        """
        return self._desktop_application_link_path
    
    @desktop_application_link_path.setter
    def desktop_application_link_path(self,value: Optional[str] = None) -> None:
        """
        Sets the desktopApplicationLinkPath property value. Define the DesktopApplicationLinkPath of the app
        Args:
            value: Value to set for the desktopApplicationLinkPath property.
        """
        self._desktop_application_link_path = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "desktop_application_id": lambda n : setattr(self, 'desktop_application_id', n.get_str_value()),
            "desktop_application_link_path": lambda n : setattr(self, 'desktop_application_link_path', n.get_str_value()),
            "path": lambda n : setattr(self, 'path', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def path(self,) -> Optional[str]:
        """
        Gets the path property value. Define the path of a desktop app
        Returns: Optional[str]
        """
        return self._path
    
    @path.setter
    def path(self,value: Optional[str] = None) -> None:
        """
        Sets the path property value. Define the path of a desktop app
        Args:
            value: Value to set for the path property.
        """
        self._path = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("desktopApplicationId", self.desktop_application_id)
        writer.write_str_value("desktopApplicationLinkPath", self.desktop_application_link_path)
        writer.write_str_value("path", self.path)
    

