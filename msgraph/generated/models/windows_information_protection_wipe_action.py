from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

action_state = lazy_import('msgraph.generated.models.action_state')
entity = lazy_import('msgraph.generated.models.entity')

class WindowsInformationProtectionWipeAction(entity.Entity):
    """
    Represents wipe requests issued by tenant admin for Bring-Your-Own-Device(BYOD) Windows devices.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new windowsInformationProtectionWipeAction and sets the default values.
        """
        super().__init__()
        # Last checkin time of the device that was targeted by this wipe action.
        self._last_check_in_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The status property
        self._status: Optional[action_state.ActionState] = None
        # Targeted device Mac address.
        self._targeted_device_mac_address: Optional[str] = None
        # Targeted device name.
        self._targeted_device_name: Optional[str] = None
        # The DeviceRegistrationId being targeted by this wipe action.
        self._targeted_device_registration_id: Optional[str] = None
        # The UserId being targeted by this wipe action.
        self._targeted_user_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsInformationProtectionWipeAction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsInformationProtectionWipeAction
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsInformationProtectionWipeAction()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "last_check_in_date_time": lambda n : setattr(self, 'last_check_in_date_time', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(action_state.ActionState)),
            "targeted_device_mac_address": lambda n : setattr(self, 'targeted_device_mac_address', n.get_str_value()),
            "targeted_device_name": lambda n : setattr(self, 'targeted_device_name', n.get_str_value()),
            "targeted_device_registration_id": lambda n : setattr(self, 'targeted_device_registration_id', n.get_str_value()),
            "targeted_user_id": lambda n : setattr(self, 'targeted_user_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_check_in_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastCheckInDateTime property value. Last checkin time of the device that was targeted by this wipe action.
        Returns: Optional[datetime]
        """
        return self._last_check_in_date_time
    
    @last_check_in_date_time.setter
    def last_check_in_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastCheckInDateTime property value. Last checkin time of the device that was targeted by this wipe action.
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
        writer.write_datetime_value("lastCheckInDateTime", self.last_check_in_date_time)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("targetedDeviceMacAddress", self.targeted_device_mac_address)
        writer.write_str_value("targetedDeviceName", self.targeted_device_name)
        writer.write_str_value("targetedDeviceRegistrationId", self.targeted_device_registration_id)
        writer.write_str_value("targetedUserId", self.targeted_user_id)
    
    @property
    def status(self,) -> Optional[action_state.ActionState]:
        """
        Gets the status property value. The status property
        Returns: Optional[action_state.ActionState]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[action_state.ActionState] = None) -> None:
        """
        Sets the status property value. The status property
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    
    @property
    def targeted_device_mac_address(self,) -> Optional[str]:
        """
        Gets the targetedDeviceMacAddress property value. Targeted device Mac address.
        Returns: Optional[str]
        """
        return self._targeted_device_mac_address
    
    @targeted_device_mac_address.setter
    def targeted_device_mac_address(self,value: Optional[str] = None) -> None:
        """
        Sets the targetedDeviceMacAddress property value. Targeted device Mac address.
        Args:
            value: Value to set for the targetedDeviceMacAddress property.
        """
        self._targeted_device_mac_address = value
    
    @property
    def targeted_device_name(self,) -> Optional[str]:
        """
        Gets the targetedDeviceName property value. Targeted device name.
        Returns: Optional[str]
        """
        return self._targeted_device_name
    
    @targeted_device_name.setter
    def targeted_device_name(self,value: Optional[str] = None) -> None:
        """
        Sets the targetedDeviceName property value. Targeted device name.
        Args:
            value: Value to set for the targetedDeviceName property.
        """
        self._targeted_device_name = value
    
    @property
    def targeted_device_registration_id(self,) -> Optional[str]:
        """
        Gets the targetedDeviceRegistrationId property value. The DeviceRegistrationId being targeted by this wipe action.
        Returns: Optional[str]
        """
        return self._targeted_device_registration_id
    
    @targeted_device_registration_id.setter
    def targeted_device_registration_id(self,value: Optional[str] = None) -> None:
        """
        Sets the targetedDeviceRegistrationId property value. The DeviceRegistrationId being targeted by this wipe action.
        Args:
            value: Value to set for the targetedDeviceRegistrationId property.
        """
        self._targeted_device_registration_id = value
    
    @property
    def targeted_user_id(self,) -> Optional[str]:
        """
        Gets the targetedUserId property value. The UserId being targeted by this wipe action.
        Returns: Optional[str]
        """
        return self._targeted_user_id
    
    @targeted_user_id.setter
    def targeted_user_id(self,value: Optional[str] = None) -> None:
        """
        Sets the targetedUserId property value. The UserId being targeted by this wipe action.
        Args:
            value: Value to set for the targetedUserId property.
        """
        self._targeted_user_id = value
    

