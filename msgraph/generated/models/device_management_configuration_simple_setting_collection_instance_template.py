from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_management_configuration_setting_instance_template = lazy_import('msgraph.generated.models.device_management_configuration_setting_instance_template')
device_management_configuration_simple_setting_value_template = lazy_import('msgraph.generated.models.device_management_configuration_simple_setting_value_template')

class DeviceManagementConfigurationSimpleSettingCollectionInstanceTemplate(device_management_configuration_setting_instance_template.DeviceManagementConfigurationSettingInstanceTemplate):
    @property
    def allow_unmanaged_values(self,) -> Optional[bool]:
        """
        Gets the allowUnmanagedValues property value. Linked policy may append values which are not present in the template.
        Returns: Optional[bool]
        """
        return self._allow_unmanaged_values
    
    @allow_unmanaged_values.setter
    def allow_unmanaged_values(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowUnmanagedValues property value. Linked policy may append values which are not present in the template.
        Args:
            value: Value to set for the allowUnmanagedValues property.
        """
        self._allow_unmanaged_values = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new DeviceManagementConfigurationSimpleSettingCollectionInstanceTemplate and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.deviceManagementConfigurationSimpleSettingCollectionInstanceTemplate"
        # Linked policy may append values which are not present in the template.
        self._allow_unmanaged_values: Optional[bool] = None
        # Simple Setting Collection Value Template
        self._simple_setting_collection_value_template: Optional[List[device_management_configuration_simple_setting_value_template.DeviceManagementConfigurationSimpleSettingValueTemplate]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementConfigurationSimpleSettingCollectionInstanceTemplate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationSimpleSettingCollectionInstanceTemplate
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementConfigurationSimpleSettingCollectionInstanceTemplate()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "allow_unmanaged_values": lambda n : setattr(self, 'allow_unmanaged_values', n.get_bool_value()),
            "simple_setting_collection_value_template": lambda n : setattr(self, 'simple_setting_collection_value_template', n.get_collection_of_object_values(device_management_configuration_simple_setting_value_template.DeviceManagementConfigurationSimpleSettingValueTemplate)),
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
        writer.write_bool_value("allowUnmanagedValues", self.allow_unmanaged_values)
        writer.write_collection_of_object_values("simpleSettingCollectionValueTemplate", self.simple_setting_collection_value_template)
    
    @property
    def simple_setting_collection_value_template(self,) -> Optional[List[device_management_configuration_simple_setting_value_template.DeviceManagementConfigurationSimpleSettingValueTemplate]]:
        """
        Gets the simpleSettingCollectionValueTemplate property value. Simple Setting Collection Value Template
        Returns: Optional[List[device_management_configuration_simple_setting_value_template.DeviceManagementConfigurationSimpleSettingValueTemplate]]
        """
        return self._simple_setting_collection_value_template
    
    @simple_setting_collection_value_template.setter
    def simple_setting_collection_value_template(self,value: Optional[List[device_management_configuration_simple_setting_value_template.DeviceManagementConfigurationSimpleSettingValueTemplate]] = None) -> None:
        """
        Sets the simpleSettingCollectionValueTemplate property value. Simple Setting Collection Value Template
        Args:
            value: Value to set for the simpleSettingCollectionValueTemplate property.
        """
        self._simple_setting_collection_value_template = value
    

