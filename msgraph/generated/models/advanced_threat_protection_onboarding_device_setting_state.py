from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import compliance_status, device_type, entity

from . import entity

class AdvancedThreatProtectionOnboardingDeviceSettingState(entity.Entity):
    """
    ATP onboarding State for a given device.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new advancedThreatProtectionOnboardingDeviceSettingState and sets the default values.
        """
        super().__init__()
        # The DateTime when device compliance grace period expires
        self._compliance_grace_period_expiration_date_time: Optional[datetime] = None
        # The Device Id that is being reported
        self._device_id: Optional[str] = None
        # The device model that is being reported
        self._device_model: Optional[str] = None
        # The Device Name that is being reported
        self._device_name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Device type.
        self._platform_type: Optional[device_type.DeviceType] = None
        # The setting class name and property name.
        self._setting: Optional[str] = None
        # The Setting Name that is being reported
        self._setting_name: Optional[str] = None
        # The state property
        self._state: Optional[compliance_status.ComplianceStatus] = None
        # The User email address that is being reported
        self._user_email: Optional[str] = None
        # The user Id that is being reported
        self._user_id: Optional[str] = None
        # The User Name that is being reported
        self._user_name: Optional[str] = None
        # The User PrincipalName that is being reported
        self._user_principal_name: Optional[str] = None
    
    @property
    def compliance_grace_period_expiration_date_time(self,) -> Optional[datetime]:
        """
        Gets the complianceGracePeriodExpirationDateTime property value. The DateTime when device compliance grace period expires
        Returns: Optional[datetime]
        """
        return self._compliance_grace_period_expiration_date_time
    
    @compliance_grace_period_expiration_date_time.setter
    def compliance_grace_period_expiration_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the complianceGracePeriodExpirationDateTime property value. The DateTime when device compliance grace period expires
        Args:
            value: Value to set for the compliance_grace_period_expiration_date_time property.
        """
        self._compliance_grace_period_expiration_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AdvancedThreatProtectionOnboardingDeviceSettingState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AdvancedThreatProtectionOnboardingDeviceSettingState
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AdvancedThreatProtectionOnboardingDeviceSettingState()
    
    @property
    def device_id(self,) -> Optional[str]:
        """
        Gets the deviceId property value. The Device Id that is being reported
        Returns: Optional[str]
        """
        return self._device_id
    
    @device_id.setter
    def device_id(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceId property value. The Device Id that is being reported
        Args:
            value: Value to set for the device_id property.
        """
        self._device_id = value
    
    @property
    def device_model(self,) -> Optional[str]:
        """
        Gets the deviceModel property value. The device model that is being reported
        Returns: Optional[str]
        """
        return self._device_model
    
    @device_model.setter
    def device_model(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceModel property value. The device model that is being reported
        Args:
            value: Value to set for the device_model property.
        """
        self._device_model = value
    
    @property
    def device_name(self,) -> Optional[str]:
        """
        Gets the deviceName property value. The Device Name that is being reported
        Returns: Optional[str]
        """
        return self._device_name
    
    @device_name.setter
    def device_name(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceName property value. The Device Name that is being reported
        Args:
            value: Value to set for the device_name property.
        """
        self._device_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import compliance_status, device_type, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "complianceGracePeriodExpirationDateTime": lambda n : setattr(self, 'compliance_grace_period_expiration_date_time', n.get_datetime_value()),
            "deviceId": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "deviceModel": lambda n : setattr(self, 'device_model', n.get_str_value()),
            "deviceName": lambda n : setattr(self, 'device_name', n.get_str_value()),
            "platformType": lambda n : setattr(self, 'platform_type', n.get_enum_value(device_type.DeviceType)),
            "setting": lambda n : setattr(self, 'setting', n.get_str_value()),
            "settingName": lambda n : setattr(self, 'setting_name', n.get_str_value()),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(compliance_status.ComplianceStatus)),
            "userEmail": lambda n : setattr(self, 'user_email', n.get_str_value()),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
            "userName": lambda n : setattr(self, 'user_name', n.get_str_value()),
            "userPrincipalName": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def platform_type(self,) -> Optional[device_type.DeviceType]:
        """
        Gets the platformType property value. Device type.
        Returns: Optional[device_type.DeviceType]
        """
        return self._platform_type
    
    @platform_type.setter
    def platform_type(self,value: Optional[device_type.DeviceType] = None) -> None:
        """
        Sets the platformType property value. Device type.
        Args:
            value: Value to set for the platform_type property.
        """
        self._platform_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_datetime_value("complianceGracePeriodExpirationDateTime", self.compliance_grace_period_expiration_date_time)
        writer.write_str_value("deviceId", self.device_id)
        writer.write_str_value("deviceModel", self.device_model)
        writer.write_str_value("deviceName", self.device_name)
        writer.write_enum_value("platformType", self.platform_type)
        writer.write_str_value("setting", self.setting)
        writer.write_str_value("settingName", self.setting_name)
        writer.write_enum_value("state", self.state)
        writer.write_str_value("userEmail", self.user_email)
        writer.write_str_value("userId", self.user_id)
        writer.write_str_value("userName", self.user_name)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
    
    @property
    def setting(self,) -> Optional[str]:
        """
        Gets the setting property value. The setting class name and property name.
        Returns: Optional[str]
        """
        return self._setting
    
    @setting.setter
    def setting(self,value: Optional[str] = None) -> None:
        """
        Sets the setting property value. The setting class name and property name.
        Args:
            value: Value to set for the setting property.
        """
        self._setting = value
    
    @property
    def setting_name(self,) -> Optional[str]:
        """
        Gets the settingName property value. The Setting Name that is being reported
        Returns: Optional[str]
        """
        return self._setting_name
    
    @setting_name.setter
    def setting_name(self,value: Optional[str] = None) -> None:
        """
        Sets the settingName property value. The Setting Name that is being reported
        Args:
            value: Value to set for the setting_name property.
        """
        self._setting_name = value
    
    @property
    def state(self,) -> Optional[compliance_status.ComplianceStatus]:
        """
        Gets the state property value. The state property
        Returns: Optional[compliance_status.ComplianceStatus]
        """
        return self._state
    
    @state.setter
    def state(self,value: Optional[compliance_status.ComplianceStatus] = None) -> None:
        """
        Sets the state property value. The state property
        Args:
            value: Value to set for the state property.
        """
        self._state = value
    
    @property
    def user_email(self,) -> Optional[str]:
        """
        Gets the userEmail property value. The User email address that is being reported
        Returns: Optional[str]
        """
        return self._user_email
    
    @user_email.setter
    def user_email(self,value: Optional[str] = None) -> None:
        """
        Sets the userEmail property value. The User email address that is being reported
        Args:
            value: Value to set for the user_email property.
        """
        self._user_email = value
    
    @property
    def user_id(self,) -> Optional[str]:
        """
        Gets the userId property value. The user Id that is being reported
        Returns: Optional[str]
        """
        return self._user_id
    
    @user_id.setter
    def user_id(self,value: Optional[str] = None) -> None:
        """
        Sets the userId property value. The user Id that is being reported
        Args:
            value: Value to set for the user_id property.
        """
        self._user_id = value
    
    @property
    def user_name(self,) -> Optional[str]:
        """
        Gets the userName property value. The User Name that is being reported
        Returns: Optional[str]
        """
        return self._user_name
    
    @user_name.setter
    def user_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userName property value. The User Name that is being reported
        Args:
            value: Value to set for the user_name property.
        """
        self._user_name = value
    
    @property
    def user_principal_name(self,) -> Optional[str]:
        """
        Gets the userPrincipalName property value. The User PrincipalName that is being reported
        Returns: Optional[str]
        """
        return self._user_principal_name
    
    @user_principal_name.setter
    def user_principal_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userPrincipalName property value. The User PrincipalName that is being reported
        Args:
            value: Value to set for the user_principal_name property.
        """
        self._user_principal_name = value
    

