from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .health_state import HealthState

from .entity import Entity

@dataclass
class WindowsManagementAppHealthState(Entity):
    """
    Windows management app health state entity.
    """
    # Name of the device on which Windows management app is installed.
    device_name: Optional[str] = None
    # Windows 10 OS version of the device on which Windows management app is installed.
    device_o_s_version: Optional[str] = None
    # Indicates health state of the Windows management app.
    health_state: Optional[HealthState] = None
    # Windows management app installed version.
    installed_version: Optional[str] = None
    # Windows management app last check-in time.
    last_check_in_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsManagementAppHealthState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsManagementAppHealthState
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return WindowsManagementAppHealthState()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .health_state import HealthState

        from .entity import Entity
        from .health_state import HealthState

        fields: Dict[str, Callable[[Any], None]] = {
            "deviceName": lambda n : setattr(self, 'device_name', n.get_str_value()),
            "deviceOSVersion": lambda n : setattr(self, 'device_o_s_version', n.get_str_value()),
            "healthState": lambda n : setattr(self, 'health_state', n.get_enum_value(HealthState)),
            "installedVersion": lambda n : setattr(self, 'installed_version', n.get_str_value()),
            "lastCheckInDateTime": lambda n : setattr(self, 'last_check_in_date_time', n.get_datetime_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("deviceName", self.device_name)
        writer.write_str_value("deviceOSVersion", self.device_o_s_version)
        writer.write_enum_value("healthState", self.health_state)
        writer.write_str_value("installedVersion", self.installed_version)
        writer.write_datetime_value("lastCheckInDateTime", self.last_check_in_date_time)
    

