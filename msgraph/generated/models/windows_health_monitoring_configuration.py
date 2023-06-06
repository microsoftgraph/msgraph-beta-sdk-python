from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_configuration, enablement, windows_health_monitoring_scope

from . import device_configuration

@dataclass
class WindowsHealthMonitoringConfiguration(device_configuration.DeviceConfiguration):
    odata_type = "#microsoft.graph.windowsHealthMonitoringConfiguration"
    # Possible values of a property
    allow_device_health_monitoring: Optional[enablement.Enablement] = None
    # Specifies custom set of events collected from the device where health monitoring is enabled
    config_device_health_monitoring_custom_scope: Optional[str] = None
    # Device health monitoring scope
    config_device_health_monitoring_scope: Optional[windows_health_monitoring_scope.WindowsHealthMonitoringScope] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsHealthMonitoringConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsHealthMonitoringConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsHealthMonitoringConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_configuration, enablement, windows_health_monitoring_scope

        fields: Dict[str, Callable[[Any], None]] = {
            "allowDeviceHealthMonitoring": lambda n : setattr(self, 'allow_device_health_monitoring', n.get_enum_value(enablement.Enablement)),
            "configDeviceHealthMonitoringCustomScope": lambda n : setattr(self, 'config_device_health_monitoring_custom_scope', n.get_str_value()),
            "configDeviceHealthMonitoringScope": lambda n : setattr(self, 'config_device_health_monitoring_scope', n.get_enum_value(windows_health_monitoring_scope.WindowsHealthMonitoringScope)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("allowDeviceHealthMonitoring", self.allow_device_health_monitoring)
        writer.write_str_value("configDeviceHealthMonitoringCustomScope", self.config_device_health_monitoring_custom_scope)
        writer.write_enum_value("configDeviceHealthMonitoringScope", self.config_device_health_monitoring_scope)
    

