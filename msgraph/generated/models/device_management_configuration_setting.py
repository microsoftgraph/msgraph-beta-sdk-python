from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_management_configuration_setting_definition = lazy_import('msgraph.generated.models.device_management_configuration_setting_definition')
device_management_configuration_setting_instance = lazy_import('msgraph.generated.models.device_management_configuration_setting_instance')
entity = lazy_import('msgraph.generated.models.entity')

class DeviceManagementConfigurationSetting(entity.Entity):
    """
    Setting instance within policy
    """
    def __init__(self,) -> None:
        """
        Instantiates a new deviceManagementConfigurationSetting and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # List of related Setting Definitions. This property is read-only.
        self._setting_definitions: Optional[List[device_management_configuration_setting_definition.DeviceManagementConfigurationSettingDefinition]] = None
        # Setting instance within policy
        self._setting_instance: Optional[device_management_configuration_setting_instance.DeviceManagementConfigurationSettingInstance] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementConfigurationSetting:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationSetting
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementConfigurationSetting()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "setting_definitions": lambda n : setattr(self, 'setting_definitions', n.get_collection_of_object_values(device_management_configuration_setting_definition.DeviceManagementConfigurationSettingDefinition)),
            "setting_instance": lambda n : setattr(self, 'setting_instance', n.get_object_value(device_management_configuration_setting_instance.DeviceManagementConfigurationSettingInstance)),
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
        writer.write_collection_of_object_values("settingDefinitions", self.setting_definitions)
        writer.write_object_value("settingInstance", self.setting_instance)
    
    @property
    def setting_definitions(self,) -> Optional[List[device_management_configuration_setting_definition.DeviceManagementConfigurationSettingDefinition]]:
        """
        Gets the settingDefinitions property value. List of related Setting Definitions. This property is read-only.
        Returns: Optional[List[device_management_configuration_setting_definition.DeviceManagementConfigurationSettingDefinition]]
        """
        return self._setting_definitions
    
    @setting_definitions.setter
    def setting_definitions(self,value: Optional[List[device_management_configuration_setting_definition.DeviceManagementConfigurationSettingDefinition]] = None) -> None:
        """
        Sets the settingDefinitions property value. List of related Setting Definitions. This property is read-only.
        Args:
            value: Value to set for the settingDefinitions property.
        """
        self._setting_definitions = value
    
    @property
    def setting_instance(self,) -> Optional[device_management_configuration_setting_instance.DeviceManagementConfigurationSettingInstance]:
        """
        Gets the settingInstance property value. Setting instance within policy
        Returns: Optional[device_management_configuration_setting_instance.DeviceManagementConfigurationSettingInstance]
        """
        return self._setting_instance
    
    @setting_instance.setter
    def setting_instance(self,value: Optional[device_management_configuration_setting_instance.DeviceManagementConfigurationSettingInstance] = None) -> None:
        """
        Sets the settingInstance property value. Setting instance within policy
        Args:
            value: Value to set for the settingInstance property.
        """
        self._setting_instance = value
    

