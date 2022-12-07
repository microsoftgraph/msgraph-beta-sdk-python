from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_management_configuration_group_setting_value_template = lazy_import('msgraph.generated.models.device_management_configuration_group_setting_value_template')
device_management_configuration_setting_instance_template = lazy_import('msgraph.generated.models.device_management_configuration_setting_instance_template')

class DeviceManagementConfigurationGroupSettingCollectionInstanceTemplate(device_management_configuration_setting_instance_template.DeviceManagementConfigurationSettingInstanceTemplate):
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
        Instantiates a new DeviceManagementConfigurationGroupSettingCollectionInstanceTemplate and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.deviceManagementConfigurationGroupSettingCollectionInstanceTemplate"
        # Linked policy may append values which are not present in the template.
        self._allow_unmanaged_values: Optional[bool] = None
        # Group Setting Collection Value Template
        self._group_setting_collection_value_template: Optional[List[device_management_configuration_group_setting_value_template.DeviceManagementConfigurationGroupSettingValueTemplate]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementConfigurationGroupSettingCollectionInstanceTemplate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationGroupSettingCollectionInstanceTemplate
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementConfigurationGroupSettingCollectionInstanceTemplate()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "allow_unmanaged_values": lambda n : setattr(self, 'allow_unmanaged_values', n.get_bool_value()),
            "group_setting_collection_value_template": lambda n : setattr(self, 'group_setting_collection_value_template', n.get_collection_of_object_values(device_management_configuration_group_setting_value_template.DeviceManagementConfigurationGroupSettingValueTemplate)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def group_setting_collection_value_template(self,) -> Optional[List[device_management_configuration_group_setting_value_template.DeviceManagementConfigurationGroupSettingValueTemplate]]:
        """
        Gets the groupSettingCollectionValueTemplate property value. Group Setting Collection Value Template
        Returns: Optional[List[device_management_configuration_group_setting_value_template.DeviceManagementConfigurationGroupSettingValueTemplate]]
        """
        return self._group_setting_collection_value_template
    
    @group_setting_collection_value_template.setter
    def group_setting_collection_value_template(self,value: Optional[List[device_management_configuration_group_setting_value_template.DeviceManagementConfigurationGroupSettingValueTemplate]] = None) -> None:
        """
        Sets the groupSettingCollectionValueTemplate property value. Group Setting Collection Value Template
        Args:
            value: Value to set for the groupSettingCollectionValueTemplate property.
        """
        self._group_setting_collection_value_template = value
    
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
        writer.write_collection_of_object_values("groupSettingCollectionValueTemplate", self.group_setting_collection_value_template)
    

