from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_enrollment_configuration

from . import device_enrollment_configuration

class DeviceComanagementAuthorityConfiguration(device_enrollment_configuration.DeviceEnrollmentConfiguration):
    def __init__(self,) -> None:
        """
        Instantiates a new DeviceComanagementAuthorityConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.deviceComanagementAuthorityConfiguration"
        # CoManagement Authority configuration ConfigurationManagerAgentCommandLineArgument
        self._configuration_manager_agent_command_line_argument: Optional[str] = None
        # CoManagement Authority configuration InstallConfigurationManagerAgent
        self._install_configuration_manager_agent: Optional[bool] = None
        # CoManagement Authority configuration ManagedDeviceAuthority
        self._managed_device_authority: Optional[int] = None
    
    @property
    def configuration_manager_agent_command_line_argument(self,) -> Optional[str]:
        """
        Gets the configurationManagerAgentCommandLineArgument property value. CoManagement Authority configuration ConfigurationManagerAgentCommandLineArgument
        Returns: Optional[str]
        """
        return self._configuration_manager_agent_command_line_argument
    
    @configuration_manager_agent_command_line_argument.setter
    def configuration_manager_agent_command_line_argument(self,value: Optional[str] = None) -> None:
        """
        Sets the configurationManagerAgentCommandLineArgument property value. CoManagement Authority configuration ConfigurationManagerAgentCommandLineArgument
        Args:
            value: Value to set for the configuration_manager_agent_command_line_argument property.
        """
        self._configuration_manager_agent_command_line_argument = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceComanagementAuthorityConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceComanagementAuthorityConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceComanagementAuthorityConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_enrollment_configuration

        fields: Dict[str, Callable[[Any], None]] = {
            "configurationManagerAgentCommandLineArgument": lambda n : setattr(self, 'configuration_manager_agent_command_line_argument', n.get_str_value()),
            "installConfigurationManagerAgent": lambda n : setattr(self, 'install_configuration_manager_agent', n.get_bool_value()),
            "managedDeviceAuthority": lambda n : setattr(self, 'managed_device_authority', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def install_configuration_manager_agent(self,) -> Optional[bool]:
        """
        Gets the installConfigurationManagerAgent property value. CoManagement Authority configuration InstallConfigurationManagerAgent
        Returns: Optional[bool]
        """
        return self._install_configuration_manager_agent
    
    @install_configuration_manager_agent.setter
    def install_configuration_manager_agent(self,value: Optional[bool] = None) -> None:
        """
        Sets the installConfigurationManagerAgent property value. CoManagement Authority configuration InstallConfigurationManagerAgent
        Args:
            value: Value to set for the install_configuration_manager_agent property.
        """
        self._install_configuration_manager_agent = value
    
    @property
    def managed_device_authority(self,) -> Optional[int]:
        """
        Gets the managedDeviceAuthority property value. CoManagement Authority configuration ManagedDeviceAuthority
        Returns: Optional[int]
        """
        return self._managed_device_authority
    
    @managed_device_authority.setter
    def managed_device_authority(self,value: Optional[int] = None) -> None:
        """
        Sets the managedDeviceAuthority property value. CoManagement Authority configuration ManagedDeviceAuthority
        Args:
            value: Value to set for the managed_device_authority property.
        """
        self._managed_device_authority = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("configurationManagerAgentCommandLineArgument", self.configuration_manager_agent_command_line_argument)
        writer.write_bool_value("installConfigurationManagerAgent", self.install_configuration_manager_agent)
        writer.write_int_value("managedDeviceAuthority", self.managed_device_authority)
    

