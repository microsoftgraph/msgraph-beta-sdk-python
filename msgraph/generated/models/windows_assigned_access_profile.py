from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class WindowsAssignedAccessProfile(entity.Entity):
    @property
    def app_user_model_ids(self,) -> Optional[List[str]]:
        """
        Gets the appUserModelIds property value. These are the only Windows Store Apps that will be available to launch from the Start menu.
        Returns: Optional[List[str]]
        """
        return self._app_user_model_ids
    
    @app_user_model_ids.setter
    def app_user_model_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the appUserModelIds property value. These are the only Windows Store Apps that will be available to launch from the Start menu.
        Args:
            value: Value to set for the appUserModelIds property.
        """
        self._app_user_model_ids = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new WindowsAssignedAccessProfile and sets the default values.
        """
        super().__init__()
        # These are the only Windows Store Apps that will be available to launch from the Start menu.
        self._app_user_model_ids: Optional[List[str]] = None
        # These are the paths of the Desktop Apps that will be available on the Start menu and the only apps the user will be able to launch.
        self._desktop_app_paths: Optional[List[str]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # This is a friendly name used to identify a group of applications, the layout of these apps on the start menu and the users to whom this kiosk configuration is assigned.
        self._profile_name: Optional[str] = None
        # This setting allows the admin to specify whether the Task Bar is shown or not.
        self._show_task_bar: Optional[bool] = None
        # Allows admins to override the default Start layout and prevents the user from changing it. The layout is modified by specifying an XML file based on a layout modification schema. XML needs to be in Binary format.
        self._start_menu_layout_xml: Optional[bytes] = None
        # The user accounts that will be locked to this kiosk configuration.
        self._user_accounts: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsAssignedAccessProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsAssignedAccessProfile
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsAssignedAccessProfile()
    
    @property
    def desktop_app_paths(self,) -> Optional[List[str]]:
        """
        Gets the desktopAppPaths property value. These are the paths of the Desktop Apps that will be available on the Start menu and the only apps the user will be able to launch.
        Returns: Optional[List[str]]
        """
        return self._desktop_app_paths
    
    @desktop_app_paths.setter
    def desktop_app_paths(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the desktopAppPaths property value. These are the paths of the Desktop Apps that will be available on the Start menu and the only apps the user will be able to launch.
        Args:
            value: Value to set for the desktopAppPaths property.
        """
        self._desktop_app_paths = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "app_user_model_ids": lambda n : setattr(self, 'app_user_model_ids', n.get_collection_of_primitive_values(str)),
            "desktop_app_paths": lambda n : setattr(self, 'desktop_app_paths', n.get_collection_of_primitive_values(str)),
            "profile_name": lambda n : setattr(self, 'profile_name', n.get_str_value()),
            "show_task_bar": lambda n : setattr(self, 'show_task_bar', n.get_bool_value()),
            "start_menu_layout_xml": lambda n : setattr(self, 'start_menu_layout_xml', n.get_bytes_value()),
            "user_accounts": lambda n : setattr(self, 'user_accounts', n.get_collection_of_primitive_values(str)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def profile_name(self,) -> Optional[str]:
        """
        Gets the profileName property value. This is a friendly name used to identify a group of applications, the layout of these apps on the start menu and the users to whom this kiosk configuration is assigned.
        Returns: Optional[str]
        """
        return self._profile_name
    
    @profile_name.setter
    def profile_name(self,value: Optional[str] = None) -> None:
        """
        Sets the profileName property value. This is a friendly name used to identify a group of applications, the layout of these apps on the start menu and the users to whom this kiosk configuration is assigned.
        Args:
            value: Value to set for the profileName property.
        """
        self._profile_name = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_primitive_values("appUserModelIds", self.app_user_model_ids)
        writer.write_collection_of_primitive_values("desktopAppPaths", self.desktop_app_paths)
        writer.write_str_value("profileName", self.profile_name)
        writer.write_bool_value("showTaskBar", self.show_task_bar)
        writer.write_object_value("startMenuLayoutXml", self.start_menu_layout_xml)
        writer.write_collection_of_primitive_values("userAccounts", self.user_accounts)
    
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
    
    @property
    def user_accounts(self,) -> Optional[List[str]]:
        """
        Gets the userAccounts property value. The user accounts that will be locked to this kiosk configuration.
        Returns: Optional[List[str]]
        """
        return self._user_accounts
    
    @user_accounts.setter
    def user_accounts(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the userAccounts property value. The user accounts that will be locked to this kiosk configuration.
        Args:
            value: Value to set for the userAccounts property.
        """
        self._user_accounts = value
    

