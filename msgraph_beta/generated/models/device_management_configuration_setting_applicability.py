from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_management_configuration_application_setting_applicability import DeviceManagementConfigurationApplicationSettingApplicability
    from .device_management_configuration_device_mode import DeviceManagementConfigurationDeviceMode
    from .device_management_configuration_exchange_online_setting_applicability import DeviceManagementConfigurationExchangeOnlineSettingApplicability
    from .device_management_configuration_platforms import DeviceManagementConfigurationPlatforms
    from .device_management_configuration_technologies import DeviceManagementConfigurationTechnologies
    from .device_management_configuration_windows_setting_applicability import DeviceManagementConfigurationWindowsSettingApplicability

@dataclass
class DeviceManagementConfigurationSettingApplicability(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # description of the setting
    description: Optional[str] = None
    # Describes applicability for the mode the device is in
    device_mode: Optional[DeviceManagementConfigurationDeviceMode] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Supported platform types.
    platform: Optional[DeviceManagementConfigurationPlatforms] = None
    # Describes which technology this setting can be deployed with
    technologies: Optional[DeviceManagementConfigurationTechnologies] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceManagementConfigurationSettingApplicability:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationSettingApplicability
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementConfigurationApplicationSettingApplicability".casefold():
            from .device_management_configuration_application_setting_applicability import DeviceManagementConfigurationApplicationSettingApplicability

            return DeviceManagementConfigurationApplicationSettingApplicability()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementConfigurationExchangeOnlineSettingApplicability".casefold():
            from .device_management_configuration_exchange_online_setting_applicability import DeviceManagementConfigurationExchangeOnlineSettingApplicability

            return DeviceManagementConfigurationExchangeOnlineSettingApplicability()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementConfigurationWindowsSettingApplicability".casefold():
            from .device_management_configuration_windows_setting_applicability import DeviceManagementConfigurationWindowsSettingApplicability

            return DeviceManagementConfigurationWindowsSettingApplicability()
        return DeviceManagementConfigurationSettingApplicability()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .device_management_configuration_application_setting_applicability import DeviceManagementConfigurationApplicationSettingApplicability
        from .device_management_configuration_device_mode import DeviceManagementConfigurationDeviceMode
        from .device_management_configuration_exchange_online_setting_applicability import DeviceManagementConfigurationExchangeOnlineSettingApplicability
        from .device_management_configuration_platforms import DeviceManagementConfigurationPlatforms
        from .device_management_configuration_technologies import DeviceManagementConfigurationTechnologies
        from .device_management_configuration_windows_setting_applicability import DeviceManagementConfigurationWindowsSettingApplicability

        from .device_management_configuration_application_setting_applicability import DeviceManagementConfigurationApplicationSettingApplicability
        from .device_management_configuration_device_mode import DeviceManagementConfigurationDeviceMode
        from .device_management_configuration_exchange_online_setting_applicability import DeviceManagementConfigurationExchangeOnlineSettingApplicability
        from .device_management_configuration_platforms import DeviceManagementConfigurationPlatforms
        from .device_management_configuration_technologies import DeviceManagementConfigurationTechnologies
        from .device_management_configuration_windows_setting_applicability import DeviceManagementConfigurationWindowsSettingApplicability

        fields: Dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "deviceMode": lambda n : setattr(self, 'device_mode', n.get_enum_value(DeviceManagementConfigurationDeviceMode)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "platform": lambda n : setattr(self, 'platform', n.get_collection_of_enum_values(DeviceManagementConfigurationPlatforms)),
            "technologies": lambda n : setattr(self, 'technologies', n.get_collection_of_enum_values(DeviceManagementConfigurationTechnologies)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("description", self.description)
        writer.write_enum_value("deviceMode", self.device_mode)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("platform", self.platform)
        writer.write_enum_value("technologies", self.technologies)
        writer.write_additional_data_value(self.additional_data)
    

