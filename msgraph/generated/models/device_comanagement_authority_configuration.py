from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_enrollment_configuration import DeviceEnrollmentConfiguration

from .device_enrollment_configuration import DeviceEnrollmentConfiguration

@dataclass
class DeviceComanagementAuthorityConfiguration(DeviceEnrollmentConfiguration):
    """
    Windows 10 Co-Management Authority Page Configuration
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.deviceComanagementAuthorityConfiguration"
    # CoManagement Authority configuration ConfigurationManagerAgentCommandLineArgument
    configuration_manager_agent_command_line_argument: Optional[str] = None
    # CoManagement Authority configuration InstallConfigurationManagerAgent
    install_configuration_manager_agent: Optional[bool] = None
    # CoManagement Authority configuration ManagedDeviceAuthority
    managed_device_authority: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceComanagementAuthorityConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceComanagementAuthorityConfiguration
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return DeviceComanagementAuthorityConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .device_enrollment_configuration import DeviceEnrollmentConfiguration

        from .device_enrollment_configuration import DeviceEnrollmentConfiguration

        fields: Dict[str, Callable[[Any], None]] = {
            "configurationManagerAgentCommandLineArgument": lambda n : setattr(self, 'configuration_manager_agent_command_line_argument', n.get_str_value()),
            "installConfigurationManagerAgent": lambda n : setattr(self, 'install_configuration_manager_agent', n.get_bool_value()),
            "managedDeviceAuthority": lambda n : setattr(self, 'managed_device_authority', n.get_int_value()),
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
        writer.write_str_value("configurationManagerAgentCommandLineArgument", self.configuration_manager_agent_command_line_argument)
        writer.write_bool_value("installConfigurationManagerAgent", self.install_configuration_manager_agent)
        writer.write_int_value("managedDeviceAuthority", self.managed_device_authority)
    

