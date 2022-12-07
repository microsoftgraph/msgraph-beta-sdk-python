from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

windows_kiosk_app_base = lazy_import('msgraph.generated.models.windows_kiosk_app_base')
windows_kiosk_app_configuration = lazy_import('msgraph.generated.models.windows_kiosk_app_configuration')

class WindowsKioskMultipleApps(windows_kiosk_app_configuration.WindowsKioskAppConfiguration):
    @property
    def allow_access_to_downloads_folder(self,) -> Optional[bool]:
        """
        Gets the allowAccessToDownloadsFolder property value. This setting allows access to Downloads folder in file explorer.
        Returns: Optional[bool]
        """
        return self._allow_access_to_downloads_folder
    
    @allow_access_to_downloads_folder.setter
    def allow_access_to_downloads_folder(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowAccessToDownloadsFolder property value. This setting allows access to Downloads folder in file explorer.
        Args:
            value: Value to set for the allowAccessToDownloadsFolder property.
        """
        self._allow_access_to_downloads_folder = value
    
    @property
    def apps(self,) -> Optional[List[windows_kiosk_app_base.WindowsKioskAppBase]]:
        """
        Gets the apps property value. These are the only Windows Store Apps that will be available to launch from the Start menu. This collection can contain a maximum of 128 elements.
        Returns: Optional[List[windows_kiosk_app_base.WindowsKioskAppBase]]
        """
        return self._apps
    
    @apps.setter
    def apps(self,value: Optional[List[windows_kiosk_app_base.WindowsKioskAppBase]] = None) -> None:
        """
        Sets the apps property value. These are the only Windows Store Apps that will be available to launch from the Start menu. This collection can contain a maximum of 128 elements.
        Args:
            value: Value to set for the apps property.
        """
        self._apps = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new WindowsKioskMultipleApps and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windowsKioskMultipleApps"
        # This setting allows access to Downloads folder in file explorer.
        self._allow_access_to_downloads_folder: Optional[bool] = None
        # These are the only Windows Store Apps that will be available to launch from the Start menu. This collection can contain a maximum of 128 elements.
        self._apps: Optional[List[windows_kiosk_app_base.WindowsKioskAppBase]] = None
        # This setting indicates that desktop apps are allowed. Default to true.
        self._disallow_desktop_apps: Optional[bool] = None
        # This setting allows the admin to specify whether the Task Bar is shown or not.
        self._show_task_bar: Optional[bool] = None
        # Allows admins to override the default Start layout and prevents the user from changing it. The layout is modified by specifying an XML file based on a layout modification schema. XML needs to be in Binary format.
        self._start_menu_layout_xml: Optional[bytes] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsKioskMultipleApps:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsKioskMultipleApps
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsKioskMultipleApps()
    
    @property
    def disallow_desktop_apps(self,) -> Optional[bool]:
        """
        Gets the disallowDesktopApps property value. This setting indicates that desktop apps are allowed. Default to true.
        Returns: Optional[bool]
        """
        return self._disallow_desktop_apps
    
    @disallow_desktop_apps.setter
    def disallow_desktop_apps(self,value: Optional[bool] = None) -> None:
        """
        Sets the disallowDesktopApps property value. This setting indicates that desktop apps are allowed. Default to true.
        Args:
            value: Value to set for the disallowDesktopApps property.
        """
        self._disallow_desktop_apps = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "allow_access_to_downloads_folder": lambda n : setattr(self, 'allow_access_to_downloads_folder', n.get_bool_value()),
            "apps": lambda n : setattr(self, 'apps', n.get_collection_of_object_values(windows_kiosk_app_base.WindowsKioskAppBase)),
            "disallow_desktop_apps": lambda n : setattr(self, 'disallow_desktop_apps', n.get_bool_value()),
            "show_task_bar": lambda n : setattr(self, 'show_task_bar', n.get_bool_value()),
            "start_menu_layout_xml": lambda n : setattr(self, 'start_menu_layout_xml', n.get_bytes_value()),
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
        writer.write_bool_value("allowAccessToDownloadsFolder", self.allow_access_to_downloads_folder)
        writer.write_collection_of_object_values("apps", self.apps)
        writer.write_bool_value("disallowDesktopApps", self.disallow_desktop_apps)
        writer.write_bool_value("showTaskBar", self.show_task_bar)
        writer.write_object_value("startMenuLayoutXml", self.start_menu_layout_xml)
    
    @property
    def show_task_bar(self,) -> Optional[bool]:
        """
        Gets the showTaskBar property value. This setting allows the admin to specify whether the Task Bar is shown or not.
        Returns: Optional[bool]
        """
        return self._show_task_bar
    
    @show_task_bar.setter
    def show_task_bar(self,value: Optional[bool] = None) -> None:
        """
        Sets the showTaskBar property value. This setting allows the admin to specify whether the Task Bar is shown or not.
        Args:
            value: Value to set for the showTaskBar property.
        """
        self._show_task_bar = value
    
    @property
    def start_menu_layout_xml(self,) -> Optional[bytes]:
        """
        Gets the startMenuLayoutXml property value. Allows admins to override the default Start layout and prevents the user from changing it. The layout is modified by specifying an XML file based on a layout modification schema. XML needs to be in Binary format.
        Returns: Optional[bytes]
        """
        return self._start_menu_layout_xml
    
    @start_menu_layout_xml.setter
    def start_menu_layout_xml(self,value: Optional[bytes] = None) -> None:
        """
        Sets the startMenuLayoutXml property value. Allows admins to override the default Start layout and prevents the user from changing it. The layout is modified by specifying an XML file based on a layout modification schema. XML needs to be in Binary format.
        Args:
            value: Value to set for the startMenuLayoutXml property.
        """
        self._start_menu_layout_xml = value
    

