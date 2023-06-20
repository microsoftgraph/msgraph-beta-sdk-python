from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_management_configuration_application_setting_applicability, device_management_configuration_device_mode, device_management_configuration_exchange_online_setting_applicability, device_management_configuration_platforms, device_management_configuration_technologies, device_management_configuration_windows_setting_applicability

@dataclass
class DeviceManagementConfigurationSettingApplicability(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # description of the setting
    description: Optional[str] = None
    # Describes applicability for the mode the device is in
    device_mode: Optional[device_management_configuration_device_mode.DeviceManagementConfigurationDeviceMode] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Supported platform types.
    platform: Optional[device_management_configuration_platforms.DeviceManagementConfigurationPlatforms] = None
    # Describes which technology this setting can be deployed with
    technologies: Optional[device_management_configuration_technologies.DeviceManagementConfigurationTechnologies] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementConfigurationSettingApplicability:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationSettingApplicability
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementConfigurationApplicationSettingApplicability".casefold():
            from . import device_management_configuration_application_setting_applicability

            return device_management_configuration_application_setting_applicability.DeviceManagementConfigurationApplicationSettingApplicability()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementConfigurationExchangeOnlineSettingApplicability".casefold():
            from . import device_management_configuration_exchange_online_setting_applicability

            return device_management_configuration_exchange_online_setting_applicability.DeviceManagementConfigurationExchangeOnlineSettingApplicability()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementConfigurationWindowsSettingApplicability".casefold():
            from . import device_management_configuration_windows_setting_applicability

            return device_management_configuration_windows_setting_applicability.DeviceManagementConfigurationWindowsSettingApplicability()
        return DeviceManagementConfigurationSettingApplicability()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_management_configuration_application_setting_applicability, device_management_configuration_device_mode, device_management_configuration_exchange_online_setting_applicability, device_management_configuration_platforms, device_management_configuration_technologies, device_management_configuration_windows_setting_applicability

        from . import device_management_configuration_application_setting_applicability, device_management_configuration_device_mode, device_management_configuration_exchange_online_setting_applicability, device_management_configuration_platforms, device_management_configuration_technologies, device_management_configuration_windows_setting_applicability

        fields: Dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "deviceMode": lambda n : setattr(self, 'device_mode', n.get_enum_value(device_management_configuration_device_mode.DeviceManagementConfigurationDeviceMode)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "platform": lambda n : setattr(self, 'platform', n.get_enum_value(device_management_configuration_platforms.DeviceManagementConfigurationPlatforms)),
            "technologies": lambda n : setattr(self, 'technologies', n.get_enum_value(device_management_configuration_technologies.DeviceManagementConfigurationTechnologies)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("description", self.description)
        writer.write_enum_value("deviceMode", self.device_mode)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("platform", self.platform)
        writer.write_enum_value("technologies", self.technologies)
        writer.write_additional_data_value(self.additional_data)
    

