from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, windows_privacy_data_access_level, windows_privacy_data_category

from . import entity

class WindowsPrivacyDataAccessControlItem(entity.Entity):
    """
    Specify access control level per privacy data category
    """
    def __init__(self,) -> None:
        """
        Instantiates a new windowsPrivacyDataAccessControlItem and sets the default values.
        """
        super().__init__()
        # Determine the access level to specific Windows privacy data category.
        self._access_level: Optional[windows_privacy_data_access_level.WindowsPrivacyDataAccessLevel] = None
        # The Package Family Name of a Windows app. When set, the access level applies to the specified application.
        self._app_display_name: Optional[str] = None
        # The Package Family Name of a Windows app. When set, the access level applies to the specified application.
        self._app_package_family_name: Optional[str] = None
        # Windows privacy data category specifier for privacy data access.
        self._data_category: Optional[windows_privacy_data_category.WindowsPrivacyDataCategory] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @property
    def access_level(self,) -> Optional[windows_privacy_data_access_level.WindowsPrivacyDataAccessLevel]:
        """
        Gets the accessLevel property value. Determine the access level to specific Windows privacy data category.
        Returns: Optional[windows_privacy_data_access_level.WindowsPrivacyDataAccessLevel]
        """
        return self._access_level
    
    @access_level.setter
    def access_level(self,value: Optional[windows_privacy_data_access_level.WindowsPrivacyDataAccessLevel] = None) -> None:
        """
        Sets the accessLevel property value. Determine the access level to specific Windows privacy data category.
        Args:
            value: Value to set for the access_level property.
        """
        self._access_level = value
    
    @property
    def app_display_name(self,) -> Optional[str]:
        """
        Gets the appDisplayName property value. The Package Family Name of a Windows app. When set, the access level applies to the specified application.
        Returns: Optional[str]
        """
        return self._app_display_name
    
    @app_display_name.setter
    def app_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the appDisplayName property value. The Package Family Name of a Windows app. When set, the access level applies to the specified application.
        Args:
            value: Value to set for the app_display_name property.
        """
        self._app_display_name = value
    
    @property
    def app_package_family_name(self,) -> Optional[str]:
        """
        Gets the appPackageFamilyName property value. The Package Family Name of a Windows app. When set, the access level applies to the specified application.
        Returns: Optional[str]
        """
        return self._app_package_family_name
    
    @app_package_family_name.setter
    def app_package_family_name(self,value: Optional[str] = None) -> None:
        """
        Sets the appPackageFamilyName property value. The Package Family Name of a Windows app. When set, the access level applies to the specified application.
        Args:
            value: Value to set for the app_package_family_name property.
        """
        self._app_package_family_name = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsPrivacyDataAccessControlItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsPrivacyDataAccessControlItem
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsPrivacyDataAccessControlItem()
    
    @property
    def data_category(self,) -> Optional[windows_privacy_data_category.WindowsPrivacyDataCategory]:
        """
        Gets the dataCategory property value. Windows privacy data category specifier for privacy data access.
        Returns: Optional[windows_privacy_data_category.WindowsPrivacyDataCategory]
        """
        return self._data_category
    
    @data_category.setter
    def data_category(self,value: Optional[windows_privacy_data_category.WindowsPrivacyDataCategory] = None) -> None:
        """
        Sets the dataCategory property value. Windows privacy data category specifier for privacy data access.
        Args:
            value: Value to set for the data_category property.
        """
        self._data_category = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, windows_privacy_data_access_level, windows_privacy_data_category

        fields: Dict[str, Callable[[Any], None]] = {
            "accessLevel": lambda n : setattr(self, 'access_level', n.get_enum_value(windows_privacy_data_access_level.WindowsPrivacyDataAccessLevel)),
            "appDisplayName": lambda n : setattr(self, 'app_display_name', n.get_str_value()),
            "appPackageFamilyName": lambda n : setattr(self, 'app_package_family_name', n.get_str_value()),
            "dataCategory": lambda n : setattr(self, 'data_category', n.get_enum_value(windows_privacy_data_category.WindowsPrivacyDataCategory)),
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
        writer.write_enum_value("accessLevel", self.access_level)
        writer.write_str_value("appDisplayName", self.app_display_name)
        writer.write_str_value("appPackageFamilyName", self.app_package_family_name)
        writer.write_enum_value("dataCategory", self.data_category)
    

