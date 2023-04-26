from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_management_configuration_application_setting_applicability, device_management_configuration_device_mode, device_management_configuration_exchange_online_setting_applicability, device_management_configuration_platforms, device_management_configuration_technologies, device_management_configuration_windows_setting_applicability

class DeviceManagementConfigurationSettingApplicability(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new deviceManagementConfigurationSettingApplicability and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # description of the setting
        self._description: Optional[str] = None
        # Describes applicability for the mode the device is in
        self._device_mode: Optional[device_management_configuration_device_mode.DeviceManagementConfigurationDeviceMode] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Supported platform types.
        self._platform: Optional[device_management_configuration_platforms.DeviceManagementConfigurationPlatforms] = None
        # Describes which technology this setting can be deployed with
        self._technologies: Optional[device_management_configuration_technologies.DeviceManagementConfigurationTechnologies] = None
    
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementConfigurationSettingApplicability:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationSettingApplicability
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.deviceManagementConfigurationApplicationSettingApplicability":
                from . import device_management_configuration_application_setting_applicability

                return device_management_configuration_application_setting_applicability.DeviceManagementConfigurationApplicationSettingApplicability()
            if mapping_value == "#microsoft.graph.deviceManagementConfigurationExchangeOnlineSettingApplicability":
                from . import device_management_configuration_exchange_online_setting_applicability

                return device_management_configuration_exchange_online_setting_applicability.DeviceManagementConfigurationExchangeOnlineSettingApplicability()
            if mapping_value == "#microsoft.graph.deviceManagementConfigurationWindowsSettingApplicability":
                from . import device_management_configuration_windows_setting_applicability

                return device_management_configuration_windows_setting_applicability.DeviceManagementConfigurationWindowsSettingApplicability()
        return DeviceManagementConfigurationSettingApplicability()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. description of the setting
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. description of the setting
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def device_mode(self,) -> Optional[device_management_configuration_device_mode.DeviceManagementConfigurationDeviceMode]:
        """
        Gets the deviceMode property value. Describes applicability for the mode the device is in
        Returns: Optional[device_management_configuration_device_mode.DeviceManagementConfigurationDeviceMode]
        """
        return self._device_mode
    
    @device_mode.setter
    def device_mode(self,value: Optional[device_management_configuration_device_mode.DeviceManagementConfigurationDeviceMode] = None) -> None:
        """
        Sets the deviceMode property value. Describes applicability for the mode the device is in
        Args:
            value: Value to set for the device_mode property.
        """
        self._device_mode = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_management_configuration_application_setting_applicability, device_management_configuration_device_mode, device_management_configuration_exchange_online_setting_applicability, device_management_configuration_platforms, device_management_configuration_technologies, device_management_configuration_windows_setting_applicability

        fields: Dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "deviceMode": lambda n : setattr(self, 'device_mode', n.get_enum_value(device_management_configuration_device_mode.DeviceManagementConfigurationDeviceMode)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "platform": lambda n : setattr(self, 'platform', n.get_enum_value(device_management_configuration_platforms.DeviceManagementConfigurationPlatforms)),
            "technologies": lambda n : setattr(self, 'technologies', n.get_enum_value(device_management_configuration_technologies.DeviceManagementConfigurationTechnologies)),
        }
        return fields
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the odata_type property.
        """
        self._odata_type = value
    
    @property
    def platform(self,) -> Optional[device_management_configuration_platforms.DeviceManagementConfigurationPlatforms]:
        """
        Gets the platform property value. Supported platform types.
        Returns: Optional[device_management_configuration_platforms.DeviceManagementConfigurationPlatforms]
        """
        return self._platform
    
    @platform.setter
    def platform(self,value: Optional[device_management_configuration_platforms.DeviceManagementConfigurationPlatforms] = None) -> None:
        """
        Sets the platform property value. Supported platform types.
        Args:
            value: Value to set for the platform property.
        """
        self._platform = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("description", self.description)
        writer.write_enum_value("deviceMode", self.device_mode)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("platform", self.platform)
        writer.write_enum_value("technologies", self.technologies)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def technologies(self,) -> Optional[device_management_configuration_technologies.DeviceManagementConfigurationTechnologies]:
        """
        Gets the technologies property value. Describes which technology this setting can be deployed with
        Returns: Optional[device_management_configuration_technologies.DeviceManagementConfigurationTechnologies]
        """
        return self._technologies
    
    @technologies.setter
    def technologies(self,value: Optional[device_management_configuration_technologies.DeviceManagementConfigurationTechnologies] = None) -> None:
        """
        Sets the technologies property value. Describes which technology this setting can be deployed with
        Args:
            value: Value to set for the technologies property.
        """
        self._technologies = value
    

