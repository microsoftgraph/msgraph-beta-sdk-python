from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
health_state = lazy_import('msgraph.generated.models.health_state')

class WindowsManagementAppHealthState(entity.Entity):
    """
    Windows management app health state entity.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new windowsManagementAppHealthState and sets the default values.
        """
        super().__init__()
        # Name of the device on which Windows management app is installed.
        self._device_name: Optional[str] = None
        # Windows 10 OS version of the device on which Windows management app is installed.
        self._device_o_s_version: Optional[str] = None
        # Indicates health state of the Windows management app.
        self._health_state: Optional[health_state.HealthState] = None
        # Windows management app installed version.
        self._installed_version: Optional[str] = None
        # Windows management app last check-in time.
        self._last_check_in_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsManagementAppHealthState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsManagementAppHealthState
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsManagementAppHealthState()
    
    @property
    def device_name(self,) -> Optional[str]:
        """
        Gets the deviceName property value. Name of the device on which Windows management app is installed.
        Returns: Optional[str]
        """
        return self._device_name
    
    @device_name.setter
    def device_name(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceName property value. Name of the device on which Windows management app is installed.
        Args:
            value: Value to set for the deviceName property.
        """
        self._device_name = value
    
    @property
    def device_o_s_version(self,) -> Optional[str]:
        """
        Gets the deviceOSVersion property value. Windows 10 OS version of the device on which Windows management app is installed.
        Returns: Optional[str]
        """
        return self._device_o_s_version
    
    @device_o_s_version.setter
    def device_o_s_version(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceOSVersion property value. Windows 10 OS version of the device on which Windows management app is installed.
        Args:
            value: Value to set for the deviceOSVersion property.
        """
        self._device_o_s_version = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "device_name": lambda n : setattr(self, 'device_name', n.get_str_value()),
            "device_o_s_version": lambda n : setattr(self, 'device_o_s_version', n.get_str_value()),
            "health_state": lambda n : setattr(self, 'health_state', n.get_enum_value(health_state.HealthState)),
            "installed_version": lambda n : setattr(self, 'installed_version', n.get_str_value()),
            "last_check_in_date_time": lambda n : setattr(self, 'last_check_in_date_time', n.get_datetime_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def health_state(self,) -> Optional[health_state.HealthState]:
        """
        Gets the healthState property value. Indicates health state of the Windows management app.
        Returns: Optional[health_state.HealthState]
        """
        return self._health_state
    
    @health_state.setter
    def health_state(self,value: Optional[health_state.HealthState] = None) -> None:
        """
        Sets the healthState property value. Indicates health state of the Windows management app.
        Args:
            value: Value to set for the healthState property.
        """
        self._health_state = value
    
    @property
    def installed_version(self,) -> Optional[str]:
        """
        Gets the installedVersion property value. Windows management app installed version.
        Returns: Optional[str]
        """
        return self._installed_version
    
    @installed_version.setter
    def installed_version(self,value: Optional[str] = None) -> None:
        """
        Sets the installedVersion property value. Windows management app installed version.
        Args:
            value: Value to set for the installedVersion property.
        """
        self._installed_version = value
    
    @property
    def last_check_in_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastCheckInDateTime property value. Windows management app last check-in time.
        Returns: Optional[datetime]
        """
        return self._last_check_in_date_time
    
    @last_check_in_date_time.setter
    def last_check_in_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastCheckInDateTime property value. Windows management app last check-in time.
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
        writer.write_str_value("deviceName", self.device_name)
        writer.write_str_value("deviceOSVersion", self.device_o_s_version)
        writer.write_enum_value("healthState", self.health_state)
        writer.write_str_value("installedVersion", self.installed_version)
        writer.write_datetime_value("lastCheckInDateTime", self.last_check_in_date_time)
    

