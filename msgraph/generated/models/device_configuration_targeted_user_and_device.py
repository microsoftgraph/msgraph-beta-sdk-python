from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class DeviceConfigurationTargetedUserAndDevice(AdditionalDataHolder, Parsable):
    """
    Conflict summary for a set of device configuration policies.
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
        Instantiates a new deviceConfigurationTargetedUserAndDevice and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The id of the device in the checkin.
        self._device_id: Optional[str] = None
        # The name of the device in the checkin.
        self._device_name: Optional[str] = None
        # Last checkin time for this user/device pair.
        self._last_checkin_date_time: Optional[datetime] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The display name of the user in the checkin
        self._user_display_name: Optional[str] = None
        # The id of the user in the checkin.
        self._user_id: Optional[str] = None
        # The UPN of the user in the checkin.
        self._user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceConfigurationTargetedUserAndDevice:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceConfigurationTargetedUserAndDevice
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceConfigurationTargetedUserAndDevice()
    
    @property
    def device_id(self,) -> Optional[str]:
        """
        Gets the deviceId property value. The id of the device in the checkin.
        Returns: Optional[str]
        """
        return self._device_id
    
    @device_id.setter
    def device_id(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceId property value. The id of the device in the checkin.
        Args:
            value: Value to set for the deviceId property.
        """
        self._device_id = value
    
    @property
    def device_name(self,) -> Optional[str]:
        """
        Gets the deviceName property value. The name of the device in the checkin.
        Returns: Optional[str]
        """
        return self._device_name
    
    @device_name.setter
    def device_name(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceName property value. The name of the device in the checkin.
        Args:
            value: Value to set for the deviceName property.
        """
        self._device_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "device_id": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "device_name": lambda n : setattr(self, 'device_name', n.get_str_value()),
            "last_checkin_date_time": lambda n : setattr(self, 'last_checkin_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "user_display_name": lambda n : setattr(self, 'user_display_name', n.get_str_value()),
            "user_id": lambda n : setattr(self, 'user_id', n.get_str_value()),
            "user_principal_name": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
        }
        return fields
    
    @property
    def last_checkin_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastCheckinDateTime property value. Last checkin time for this user/device pair.
        Returns: Optional[datetime]
        """
        return self._last_checkin_date_time
    
    @last_checkin_date_time.setter
    def last_checkin_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastCheckinDateTime property value. Last checkin time for this user/device pair.
        Args:
            value: Value to set for the lastCheckinDateTime property.
        """
        self._last_checkin_date_time = value
    
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
        writer.write_str_value("deviceId", self.device_id)
        writer.write_str_value("deviceName", self.device_name)
        writer.write_datetime_value("lastCheckinDateTime", self.last_checkin_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("userDisplayName", self.user_display_name)
        writer.write_str_value("userId", self.user_id)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def user_display_name(self,) -> Optional[str]:
        """
        Gets the userDisplayName property value. The display name of the user in the checkin
        Returns: Optional[str]
        """
        return self._user_display_name
    
    @user_display_name.setter
    def user_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userDisplayName property value. The display name of the user in the checkin
        Args:
            value: Value to set for the userDisplayName property.
        """
        self._user_display_name = value
    
    @property
    def user_id(self,) -> Optional[str]:
        """
        Gets the userId property value. The id of the user in the checkin.
        Returns: Optional[str]
        """
        return self._user_id
    
    @user_id.setter
    def user_id(self,value: Optional[str] = None) -> None:
        """
        Sets the userId property value. The id of the user in the checkin.
        Args:
            value: Value to set for the userId property.
        """
        self._user_id = value
    
    @property
    def user_principal_name(self,) -> Optional[str]:
        """
        Gets the userPrincipalName property value. The UPN of the user in the checkin.
        Returns: Optional[str]
        """
        return self._user_principal_name
    
    @user_principal_name.setter
    def user_principal_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userPrincipalName property value. The UPN of the user in the checkin.
        Args:
            value: Value to set for the userPrincipalName property.
        """
        self._user_principal_name = value
    

