from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

windows_device_usage_type = lazy_import('msgraph.generated.models.windows_device_usage_type')
windows_user_type = lazy_import('msgraph.generated.models.windows_user_type')

class OutOfBoxExperienceSettings(AdditionalDataHolder, Parsable):
    """
    Out of box experience setting
    """
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new outOfBoxExperienceSettings and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The deviceUsageType property
        self._device_usage_type: Optional[windows_device_usage_type.WindowsDeviceUsageType] = None
        # If set to true, then the user can't start over with different account, on company sign-in
        self._hide_escape_link: Optional[bool] = None
        # Show or hide EULA to user
        self._hide_e_u_l_a: Optional[bool] = None
        # Show or hide privacy settings to user
        self._hide_privacy_settings: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # If set, then skip the keyboard selection page if Language and Region are set
        self._skip_keyboard_selection_page: Optional[bool] = None
        # The userType property
        self._user_type: Optional[windows_user_type.WindowsUserType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OutOfBoxExperienceSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OutOfBoxExperienceSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return OutOfBoxExperienceSettings()
    
    @property
    def device_usage_type(self,) -> Optional[windows_device_usage_type.WindowsDeviceUsageType]:
        """
        Gets the deviceUsageType property value. The deviceUsageType property
        Returns: Optional[windows_device_usage_type.WindowsDeviceUsageType]
        """
        return self._device_usage_type
    
    @device_usage_type.setter
    def device_usage_type(self,value: Optional[windows_device_usage_type.WindowsDeviceUsageType] = None) -> None:
        """
        Sets the deviceUsageType property value. The deviceUsageType property
        Args:
            value: Value to set for the deviceUsageType property.
        """
        self._device_usage_type = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "device_usage_type": lambda n : setattr(self, 'device_usage_type', n.get_enum_value(windows_device_usage_type.WindowsDeviceUsageType)),
            "hide_escape_link": lambda n : setattr(self, 'hide_escape_link', n.get_bool_value()),
            "hide_e_u_l_a": lambda n : setattr(self, 'hide_e_u_l_a', n.get_bool_value()),
            "hide_privacy_settings": lambda n : setattr(self, 'hide_privacy_settings', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "skip_keyboard_selection_page": lambda n : setattr(self, 'skip_keyboard_selection_page', n.get_bool_value()),
            "user_type": lambda n : setattr(self, 'user_type', n.get_enum_value(windows_user_type.WindowsUserType)),
        }
        return fields
    
    @property
    def hide_escape_link(self,) -> Optional[bool]:
        """
        Gets the hideEscapeLink property value. If set to true, then the user can't start over with different account, on company sign-in
        Returns: Optional[bool]
        """
        return self._hide_escape_link
    
    @hide_escape_link.setter
    def hide_escape_link(self,value: Optional[bool] = None) -> None:
        """
        Sets the hideEscapeLink property value. If set to true, then the user can't start over with different account, on company sign-in
        Args:
            value: Value to set for the hideEscapeLink property.
        """
        self._hide_escape_link = value
    
    @property
    def hide_e_u_l_a(self,) -> Optional[bool]:
        """
        Gets the hideEULA property value. Show or hide EULA to user
        Returns: Optional[bool]
        """
        return self._hide_e_u_l_a
    
    @hide_e_u_l_a.setter
    def hide_e_u_l_a(self,value: Optional[bool] = None) -> None:
        """
        Sets the hideEULA property value. Show or hide EULA to user
        Args:
            value: Value to set for the hideEULA property.
        """
        self._hide_e_u_l_a = value
    
    @property
    def hide_privacy_settings(self,) -> Optional[bool]:
        """
        Gets the hidePrivacySettings property value. Show or hide privacy settings to user
        Returns: Optional[bool]
        """
        return self._hide_privacy_settings
    
    @hide_privacy_settings.setter
    def hide_privacy_settings(self,value: Optional[bool] = None) -> None:
        """
        Sets the hidePrivacySettings property value. Show or hide privacy settings to user
        Args:
            value: Value to set for the hidePrivacySettings property.
        """
        self._hide_privacy_settings = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_enum_value("deviceUsageType", self.device_usage_type)
        writer.write_bool_value("hideEscapeLink", self.hide_escape_link)
        writer.write_bool_value("hideEULA", self.hide_e_u_l_a)
        writer.write_bool_value("hidePrivacySettings", self.hide_privacy_settings)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_bool_value("skipKeyboardSelectionPage", self.skip_keyboard_selection_page)
        writer.write_enum_value("userType", self.user_type)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def skip_keyboard_selection_page(self,) -> Optional[bool]:
        """
        Gets the skipKeyboardSelectionPage property value. If set, then skip the keyboard selection page if Language and Region are set
        Returns: Optional[bool]
        """
        return self._skip_keyboard_selection_page
    
    @skip_keyboard_selection_page.setter
    def skip_keyboard_selection_page(self,value: Optional[bool] = None) -> None:
        """
        Sets the skipKeyboardSelectionPage property value. If set, then skip the keyboard selection page if Language and Region are set
        Args:
            value: Value to set for the skipKeyboardSelectionPage property.
        """
        self._skip_keyboard_selection_page = value
    
    @property
    def user_type(self,) -> Optional[windows_user_type.WindowsUserType]:
        """
        Gets the userType property value. The userType property
        Returns: Optional[windows_user_type.WindowsUserType]
        """
        return self._user_type
    
    @user_type.setter
    def user_type(self,value: Optional[windows_user_type.WindowsUserType] = None) -> None:
        """
        Sets the userType property value. The userType property
        Args:
            value: Value to set for the userType property.
        """
        self._user_type = value
    

