from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

compliance_status = lazy_import('msgraph.generated.models.compliance_status')
entity = lazy_import('msgraph.generated.models.entity')

class DeviceManagementIntentDeviceState(entity.Entity):
    """
    Entity that represents device state for an intent
    """
    def __init__(self,) -> None:
        """
        Instantiates a new deviceManagementIntentDeviceState and sets the default values.
        """
        super().__init__()
        # Device name that is being reported
        self._device_display_name: Optional[str] = None
        # Device id that is being reported
        self._device_id: Optional[str] = None
        # Last modified date time of an intent report
        self._last_reported_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The state property
        self._state: Optional[compliance_status.ComplianceStatus] = None
        # The user name that is being reported on a device
        self._user_name: Optional[str] = None
        # The user principal name that is being reported on a device
        self._user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementIntentDeviceState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementIntentDeviceState
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementIntentDeviceState()
    
    @property
    def device_display_name(self,) -> Optional[str]:
        """
        Gets the deviceDisplayName property value. Device name that is being reported
        Returns: Optional[str]
        """
        return self._device_display_name
    
    @device_display_name.setter
    def device_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceDisplayName property value. Device name that is being reported
        Args:
            value: Value to set for the deviceDisplayName property.
        """
        self._device_display_name = value
    
    @property
    def device_id(self,) -> Optional[str]:
        """
        Gets the deviceId property value. Device id that is being reported
        Returns: Optional[str]
        """
        return self._device_id
    
    @device_id.setter
    def device_id(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceId property value. Device id that is being reported
        Args:
            value: Value to set for the deviceId property.
        """
        self._device_id = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "device_display_name": lambda n : setattr(self, 'device_display_name', n.get_str_value()),
            "device_id": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "last_reported_date_time": lambda n : setattr(self, 'last_reported_date_time', n.get_datetime_value()),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(compliance_status.ComplianceStatus)),
            "user_name": lambda n : setattr(self, 'user_name', n.get_str_value()),
            "user_principal_name": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_reported_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastReportedDateTime property value. Last modified date time of an intent report
        Returns: Optional[datetime]
        """
        return self._last_reported_date_time
    
    @last_reported_date_time.setter
    def last_reported_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastReportedDateTime property value. Last modified date time of an intent report
        Args:
            value: Value to set for the lastReportedDateTime property.
        """
        self._last_reported_date_time = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("deviceDisplayName", self.device_display_name)
        writer.write_str_value("deviceId", self.device_id)
        writer.write_datetime_value("lastReportedDateTime", self.last_reported_date_time)
        writer.write_enum_value("state", self.state)
        writer.write_str_value("userName", self.user_name)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
    
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
    def user_name(self,) -> Optional[str]:
        """
        Gets the userName property value. The user name that is being reported on a device
        Returns: Optional[str]
        """
        return self._user_name
    
    @user_name.setter
    def user_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userName property value. The user name that is being reported on a device
        Args:
            value: Value to set for the userName property.
        """
        self._user_name = value
    
    @property
    def user_principal_name(self,) -> Optional[str]:
        """
        Gets the userPrincipalName property value. The user principal name that is being reported on a device
        Returns: Optional[str]
        """
        return self._user_principal_name
    
    @user_principal_name.setter
    def user_principal_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userPrincipalName property value. The user principal name that is being reported on a device
        Args:
            value: Value to set for the userPrincipalName property.
        """
        self._user_principal_name = value
    

