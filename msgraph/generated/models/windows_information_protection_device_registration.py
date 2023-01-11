from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class WindowsInformationProtectionDeviceRegistration(entity.Entity):
    """
    Represents device registration records for Bring-Your-Own-Device(BYOD) Windows devices.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new windowsInformationProtectionDeviceRegistration and sets the default values.
        """
        super().__init__()
        # Device Mac address.
        self._device_mac_address: Optional[str] = None
        # Device name.
        self._device_name: Optional[str] = None
        # Device identifier for this device registration record.
        self._device_registration_id: Optional[str] = None
        # Device type, for example, Windows laptop VS Windows phone.
        self._device_type: Optional[str] = None
        # Last checkin time of the device.
        self._last_check_in_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # UserId associated with this device registration record.
        self._user_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsInformationProtectionDeviceRegistration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsInformationProtectionDeviceRegistration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsInformationProtectionDeviceRegistration()
    
    @property
    def device_mac_address(self,) -> Optional[str]:
        """
        Gets the deviceMacAddress property value. Device Mac address.
        Returns: Optional[str]
        """
        return self._device_mac_address
    
    @device_mac_address.setter
    def device_mac_address(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceMacAddress property value. Device Mac address.
        Args:
            value: Value to set for the deviceMacAddress property.
        """
        self._device_mac_address = value
    
    @property
    def device_name(self,) -> Optional[str]:
        """
        Gets the deviceName property value. Device name.
        Returns: Optional[str]
        """
        return self._device_name
    
    @device_name.setter
    def device_name(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceName property value. Device name.
        Args:
            value: Value to set for the deviceName property.
        """
        self._device_name = value
    
    @property
    def device_registration_id(self,) -> Optional[str]:
        """
        Gets the deviceRegistrationId property value. Device identifier for this device registration record.
        Returns: Optional[str]
        """
        return self._device_registration_id
    
    @device_registration_id.setter
    def device_registration_id(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceRegistrationId property value. Device identifier for this device registration record.
        Args:
            value: Value to set for the deviceRegistrationId property.
        """
        self._device_registration_id = value
    
    @property
    def device_type(self,) -> Optional[str]:
        """
        Gets the deviceType property value. Device type, for example, Windows laptop VS Windows phone.
        Returns: Optional[str]
        """
        return self._device_type
    
    @device_type.setter
    def device_type(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceType property value. Device type, for example, Windows laptop VS Windows phone.
        Args:
            value: Value to set for the deviceType property.
        """
        self._device_type = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "device_mac_address": lambda n : setattr(self, 'device_mac_address', n.get_str_value()),
            "device_name": lambda n : setattr(self, 'device_name', n.get_str_value()),
            "device_registration_id": lambda n : setattr(self, 'device_registration_id', n.get_str_value()),
            "device_type": lambda n : setattr(self, 'device_type', n.get_str_value()),
            "last_check_in_date_time": lambda n : setattr(self, 'last_check_in_date_time', n.get_datetime_value()),
            "user_id": lambda n : setattr(self, 'user_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_check_in_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastCheckInDateTime property value. Last checkin time of the device.
        Returns: Optional[datetime]
        """
        return self._last_check_in_date_time
    
    @last_check_in_date_time.setter
    def last_check_in_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastCheckInDateTime property value. Last checkin time of the device.
        Args:
            value: Value to set for the lastCheckInDateTime property.
        """
        self._last_check_in_date_time = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("deviceMacAddress", self.device_mac_address)
        writer.write_str_value("deviceName", self.device_name)
        writer.write_str_value("deviceRegistrationId", self.device_registration_id)
        writer.write_str_value("deviceType", self.device_type)
        writer.write_datetime_value("lastCheckInDateTime", self.last_check_in_date_time)
        writer.write_str_value("userId", self.user_id)
    
    @property
    def user_id(self,) -> Optional[str]:
        """
        Gets the userId property value. UserId associated with this device registration record.
        Returns: Optional[str]
        """
        return self._user_id
    
    @user_id.setter
    def user_id(self,value: Optional[str] = None) -> None:
        """
        Sets the userId property value. UserId associated with this device registration record.
        Args:
            value: Value to set for the userId property.
        """
        self._user_id = value
    

