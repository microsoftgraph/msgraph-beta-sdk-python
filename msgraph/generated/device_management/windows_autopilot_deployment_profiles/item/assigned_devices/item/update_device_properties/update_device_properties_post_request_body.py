from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

class UpdateDevicePropertiesPostRequestBody(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new updateDevicePropertiesPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The addressableUserName property
        self._addressable_user_name: Optional[str] = None
        # The deviceAccountPassword property
        self._device_account_password: Optional[str] = None
        # The deviceAccountUpn property
        self._device_account_upn: Optional[str] = None
        # The deviceFriendlyName property
        self._device_friendly_name: Optional[str] = None
        # The displayName property
        self._display_name: Optional[str] = None
        # The groupTag property
        self._group_tag: Optional[str] = None
        # The userPrincipalName property
        self._user_principal_name: Optional[str] = None
    
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
    
    @property
    def addressable_user_name(self,) -> Optional[str]:
        """
        Gets the addressableUserName property value. The addressableUserName property
        Returns: Optional[str]
        """
        return self._addressable_user_name
    
    @addressable_user_name.setter
    def addressable_user_name(self,value: Optional[str] = None) -> None:
        """
        Sets the addressableUserName property value. The addressableUserName property
        Args:
            value: Value to set for the addressable_user_name property.
        """
        self._addressable_user_name = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UpdateDevicePropertiesPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UpdateDevicePropertiesPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UpdateDevicePropertiesPostRequestBody()
    
    @property
    def device_account_password(self,) -> Optional[str]:
        """
        Gets the deviceAccountPassword property value. The deviceAccountPassword property
        Returns: Optional[str]
        """
        return self._device_account_password
    
    @device_account_password.setter
    def device_account_password(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceAccountPassword property value. The deviceAccountPassword property
        Args:
            value: Value to set for the device_account_password property.
        """
        self._device_account_password = value
    
    @property
    def device_account_upn(self,) -> Optional[str]:
        """
        Gets the deviceAccountUpn property value. The deviceAccountUpn property
        Returns: Optional[str]
        """
        return self._device_account_upn
    
    @device_account_upn.setter
    def device_account_upn(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceAccountUpn property value. The deviceAccountUpn property
        Args:
            value: Value to set for the device_account_upn property.
        """
        self._device_account_upn = value
    
    @property
    def device_friendly_name(self,) -> Optional[str]:
        """
        Gets the deviceFriendlyName property value. The deviceFriendlyName property
        Returns: Optional[str]
        """
        return self._device_friendly_name
    
    @device_friendly_name.setter
    def device_friendly_name(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceFriendlyName property value. The deviceFriendlyName property
        Args:
            value: Value to set for the device_friendly_name property.
        """
        self._device_friendly_name = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The displayName property
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The displayName property
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "addressableUserName": lambda n : setattr(self, 'addressable_user_name', n.get_str_value()),
            "deviceAccountPassword": lambda n : setattr(self, 'device_account_password', n.get_str_value()),
            "deviceAccountUpn": lambda n : setattr(self, 'device_account_upn', n.get_str_value()),
            "deviceFriendlyName": lambda n : setattr(self, 'device_friendly_name', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "groupTag": lambda n : setattr(self, 'group_tag', n.get_str_value()),
            "userPrincipalName": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
        }
        return fields
    
    @property
    def group_tag(self,) -> Optional[str]:
        """
        Gets the groupTag property value. The groupTag property
        Returns: Optional[str]
        """
        return self._group_tag
    
    @group_tag.setter
    def group_tag(self,value: Optional[str] = None) -> None:
        """
        Sets the groupTag property value. The groupTag property
        Args:
            value: Value to set for the group_tag property.
        """
        self._group_tag = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("addressableUserName", self.addressable_user_name)
        writer.write_str_value("deviceAccountPassword", self.device_account_password)
        writer.write_str_value("deviceAccountUpn", self.device_account_upn)
        writer.write_str_value("deviceFriendlyName", self.device_friendly_name)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("groupTag", self.group_tag)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def user_principal_name(self,) -> Optional[str]:
        """
        Gets the userPrincipalName property value. The userPrincipalName property
        Returns: Optional[str]
        """
        return self._user_principal_name
    
    @user_principal_name.setter
    def user_principal_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userPrincipalName property value. The userPrincipalName property
        Args:
            value: Value to set for the user_principal_name property.
        """
        self._user_principal_name = value
    

