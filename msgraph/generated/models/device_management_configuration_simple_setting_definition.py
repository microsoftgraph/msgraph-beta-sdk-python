from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_management_configuration_dependent_on = lazy_import('msgraph.generated.models.device_management_configuration_dependent_on')
device_management_configuration_setting_definition = lazy_import('msgraph.generated.models.device_management_configuration_setting_definition')
device_management_configuration_setting_depended_on_by = lazy_import('msgraph.generated.models.device_management_configuration_setting_depended_on_by')
device_management_configuration_setting_value = lazy_import('msgraph.generated.models.device_management_configuration_setting_value')
device_management_configuration_setting_value_definition = lazy_import('msgraph.generated.models.device_management_configuration_setting_value_definition')

class DeviceManagementConfigurationSimpleSettingDefinition(device_management_configuration_setting_definition.DeviceManagementConfigurationSettingDefinition):
    def __init__(self,) -> None:
        """
        Instantiates a new DeviceManagementConfigurationSimpleSettingDefinition and sets the default values.
        """
        super().__init__()
        # Default setting value for this setting
        self._default_value: Optional[device_management_configuration_setting_value.DeviceManagementConfigurationSettingValue] = None
        # list of child settings that depend on this setting
        self._depended_on_by: Optional[List[device_management_configuration_setting_depended_on_by.DeviceManagementConfigurationSettingDependedOnBy]] = None
        # list of parent settings this setting is dependent on
        self._dependent_on: Optional[List[device_management_configuration_dependent_on.DeviceManagementConfigurationDependentOn]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Definition of the value for this setting
        self._value_definition: Optional[device_management_configuration_setting_value_definition.DeviceManagementConfigurationSettingValueDefinition] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementConfigurationSimpleSettingDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationSimpleSettingDefinition
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementConfigurationSimpleSettingDefinition()
    
    @property
    def default_value(self,) -> Optional[device_management_configuration_setting_value.DeviceManagementConfigurationSettingValue]:
        """
        Gets the defaultValue property value. Default setting value for this setting
        Returns: Optional[device_management_configuration_setting_value.DeviceManagementConfigurationSettingValue]
        """
        return self._default_value
    
    @default_value.setter
    def default_value(self,value: Optional[device_management_configuration_setting_value.DeviceManagementConfigurationSettingValue] = None) -> None:
        """
        Sets the defaultValue property value. Default setting value for this setting
        Args:
            value: Value to set for the defaultValue property.
        """
        self._default_value = value
    
    @property
    def depended_on_by(self,) -> Optional[List[device_management_configuration_setting_depended_on_by.DeviceManagementConfigurationSettingDependedOnBy]]:
        """
        Gets the dependedOnBy property value. list of child settings that depend on this setting
        Returns: Optional[List[device_management_configuration_setting_depended_on_by.DeviceManagementConfigurationSettingDependedOnBy]]
        """
        return self._depended_on_by
    
    @depended_on_by.setter
    def depended_on_by(self,value: Optional[List[device_management_configuration_setting_depended_on_by.DeviceManagementConfigurationSettingDependedOnBy]] = None) -> None:
        """
        Sets the dependedOnBy property value. list of child settings that depend on this setting
        Args:
            value: Value to set for the dependedOnBy property.
        """
        self._depended_on_by = value
    
    @property
    def dependent_on(self,) -> Optional[List[device_management_configuration_dependent_on.DeviceManagementConfigurationDependentOn]]:
        """
        Gets the dependentOn property value. list of parent settings this setting is dependent on
        Returns: Optional[List[device_management_configuration_dependent_on.DeviceManagementConfigurationDependentOn]]
        """
        return self._dependent_on
    
    @dependent_on.setter
    def dependent_on(self,value: Optional[List[device_management_configuration_dependent_on.DeviceManagementConfigurationDependentOn]] = None) -> None:
        """
        Sets the dependentOn property value. list of parent settings this setting is dependent on
        Args:
            value: Value to set for the dependentOn property.
        """
        self._dependent_on = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "default_value": lambda n : setattr(self, 'default_value', n.get_object_value(device_management_configuration_setting_value.DeviceManagementConfigurationSettingValue)),
            "depended_on_by": lambda n : setattr(self, 'depended_on_by', n.get_collection_of_object_values(device_management_configuration_setting_depended_on_by.DeviceManagementConfigurationSettingDependedOnBy)),
            "dependent_on": lambda n : setattr(self, 'dependent_on', n.get_collection_of_object_values(device_management_configuration_dependent_on.DeviceManagementConfigurationDependentOn)),
            "value_definition": lambda n : setattr(self, 'value_definition', n.get_object_value(device_management_configuration_setting_value_definition.DeviceManagementConfigurationSettingValueDefinition)),
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
        writer.write_object_value("defaultValue", self.default_value)
        writer.write_collection_of_object_values("dependedOnBy", self.depended_on_by)
        writer.write_collection_of_object_values("dependentOn", self.dependent_on)
        writer.write_object_value("valueDefinition", self.value_definition)
    
    @property
    def value_definition(self,) -> Optional[device_management_configuration_setting_value_definition.DeviceManagementConfigurationSettingValueDefinition]:
        """
        Gets the valueDefinition property value. Definition of the value for this setting
        Returns: Optional[device_management_configuration_setting_value_definition.DeviceManagementConfigurationSettingValueDefinition]
        """
        return self._value_definition
    
    @value_definition.setter
    def value_definition(self,value: Optional[device_management_configuration_setting_value_definition.DeviceManagementConfigurationSettingValueDefinition] = None) -> None:
        """
        Sets the valueDefinition property value. Definition of the value for this setting
        Args:
            value: Value to set for the valueDefinition property.
        """
        self._value_definition = value
    

