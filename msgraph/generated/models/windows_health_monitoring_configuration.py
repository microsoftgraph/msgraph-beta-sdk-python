from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_configuration = lazy_import('msgraph.generated.models.device_configuration')
enablement = lazy_import('msgraph.generated.models.enablement')
windows_health_monitoring_scope = lazy_import('msgraph.generated.models.windows_health_monitoring_scope')

class WindowsHealthMonitoringConfiguration(device_configuration.DeviceConfiguration):
    @property
    def allow_device_health_monitoring(self,) -> Optional[enablement.Enablement]:
        """
        Gets the allowDeviceHealthMonitoring property value. Possible values of a property
        Returns: Optional[enablement.Enablement]
        """
        return self._allow_device_health_monitoring
    
    @allow_device_health_monitoring.setter
    def allow_device_health_monitoring(self,value: Optional[enablement.Enablement] = None) -> None:
        """
        Sets the allowDeviceHealthMonitoring property value. Possible values of a property
        Args:
            value: Value to set for the allowDeviceHealthMonitoring property.
        """
        self._allow_device_health_monitoring = value
    
    @property
    def config_device_health_monitoring_custom_scope(self,) -> Optional[str]:
        """
        Gets the configDeviceHealthMonitoringCustomScope property value. Specifies custom set of events collected from the device where health monitoring is enabled
        Returns: Optional[str]
        """
        return self._config_device_health_monitoring_custom_scope
    
    @config_device_health_monitoring_custom_scope.setter
    def config_device_health_monitoring_custom_scope(self,value: Optional[str] = None) -> None:
        """
        Sets the configDeviceHealthMonitoringCustomScope property value. Specifies custom set of events collected from the device where health monitoring is enabled
        Args:
            value: Value to set for the configDeviceHealthMonitoringCustomScope property.
        """
        self._config_device_health_monitoring_custom_scope = value
    
    @property
    def config_device_health_monitoring_scope(self,) -> Optional[windows_health_monitoring_scope.WindowsHealthMonitoringScope]:
        """
        Gets the configDeviceHealthMonitoringScope property value. Device health monitoring scope
        Returns: Optional[windows_health_monitoring_scope.WindowsHealthMonitoringScope]
        """
        return self._config_device_health_monitoring_scope
    
    @config_device_health_monitoring_scope.setter
    def config_device_health_monitoring_scope(self,value: Optional[windows_health_monitoring_scope.WindowsHealthMonitoringScope] = None) -> None:
        """
        Sets the configDeviceHealthMonitoringScope property value. Device health monitoring scope
        Args:
            value: Value to set for the configDeviceHealthMonitoringScope property.
        """
        self._config_device_health_monitoring_scope = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new WindowsHealthMonitoringConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windowsHealthMonitoringConfiguration"
        # Possible values of a property
        self._allow_device_health_monitoring: Optional[enablement.Enablement] = None
        # Specifies custom set of events collected from the device where health monitoring is enabled
        self._config_device_health_monitoring_custom_scope: Optional[str] = None
        # Device health monitoring scope
        self._config_device_health_monitoring_scope: Optional[windows_health_monitoring_scope.WindowsHealthMonitoringScope] = None
    
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
        fields = {
            "allow_device_health_monitoring": lambda n : setattr(self, 'allow_device_health_monitoring', n.get_enum_value(enablement.Enablement)),
            "config_device_health_monitoring_custom_scope": lambda n : setattr(self, 'config_device_health_monitoring_custom_scope', n.get_str_value()),
            "config_device_health_monitoring_scope": lambda n : setattr(self, 'config_device_health_monitoring_scope', n.get_enum_value(windows_health_monitoring_scope.WindowsHealthMonitoringScope)),
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
    

