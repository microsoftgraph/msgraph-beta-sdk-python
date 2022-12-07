from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
security_baseline_compliance_state = lazy_import('msgraph.generated.models.security_baseline_compliance_state')

class SecurityBaselineDeviceState(entity.Entity):
    """
    The security baseline compliance state summary of the security baseline for a device.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new securityBaselineDeviceState and sets the default values.
        """
        super().__init__()
        # Display name of the device
        self._device_display_name: Optional[str] = None
        # Last modified date time of the policy report
        self._last_reported_date_time: Optional[datetime] = None
        # Intune device id
        self._managed_device_id: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Security Baseline Compliance State
        self._state: Optional[security_baseline_compliance_state.SecurityBaselineComplianceState] = None
        # User Principal Name
        self._user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SecurityBaselineDeviceState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SecurityBaselineDeviceState
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SecurityBaselineDeviceState()
    
    @property
    def device_display_name(self,) -> Optional[str]:
        """
        Gets the deviceDisplayName property value. Display name of the device
        Returns: Optional[str]
        """
        return self._device_display_name
    
    @device_display_name.setter
    def device_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceDisplayName property value. Display name of the device
        Args:
            value: Value to set for the deviceDisplayName property.
        """
        self._device_display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "device_display_name": lambda n : setattr(self, 'device_display_name', n.get_str_value()),
            "last_reported_date_time": lambda n : setattr(self, 'last_reported_date_time', n.get_datetime_value()),
            "managed_device_id": lambda n : setattr(self, 'managed_device_id', n.get_str_value()),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(security_baseline_compliance_state.SecurityBaselineComplianceState)),
            "user_principal_name": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_reported_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastReportedDateTime property value. Last modified date time of the policy report
        Returns: Optional[datetime]
        """
        return self._last_reported_date_time
    
    @last_reported_date_time.setter
    def last_reported_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastReportedDateTime property value. Last modified date time of the policy report
        Args:
            value: Value to set for the lastReportedDateTime property.
        """
        self._last_reported_date_time = value
    
    @property
    def managed_device_id(self,) -> Optional[str]:
        """
        Gets the managedDeviceId property value. Intune device id
        Returns: Optional[str]
        """
        return self._managed_device_id
    
    @managed_device_id.setter
    def managed_device_id(self,value: Optional[str] = None) -> None:
        """
        Sets the managedDeviceId property value. Intune device id
        Args:
            value: Value to set for the managedDeviceId property.
        """
        self._managed_device_id = value
    
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
        writer.write_datetime_value("lastReportedDateTime", self.last_reported_date_time)
        writer.write_str_value("managedDeviceId", self.managed_device_id)
        writer.write_enum_value("state", self.state)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
    
    @property
    def state(self,) -> Optional[security_baseline_compliance_state.SecurityBaselineComplianceState]:
        """
        Gets the state property value. Security Baseline Compliance State
        Returns: Optional[security_baseline_compliance_state.SecurityBaselineComplianceState]
        """
        return self._state
    
    @state.setter
    def state(self,value: Optional[security_baseline_compliance_state.SecurityBaselineComplianceState] = None) -> None:
        """
        Sets the state property value. Security Baseline Compliance State
        Args:
            value: Value to set for the state property.
        """
        self._state = value
    
    @property
    def user_principal_name(self,) -> Optional[str]:
        """
        Gets the userPrincipalName property value. User Principal Name
        Returns: Optional[str]
        """
        return self._user_principal_name
    
    @user_principal_name.setter
    def user_principal_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userPrincipalName property value. User Principal Name
        Args:
            value: Value to set for the userPrincipalName property.
        """
        self._user_principal_name = value
    

