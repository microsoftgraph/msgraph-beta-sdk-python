from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_management_configuration_choice_setting_value_template = lazy_import('msgraph.generated.models.device_management_configuration_choice_setting_value_template')
device_management_configuration_setting_instance_template = lazy_import('msgraph.generated.models.device_management_configuration_setting_instance_template')

class DeviceManagementConfigurationChoiceSettingCollectionInstanceTemplate(device_management_configuration_setting_instance_template.DeviceManagementConfigurationSettingInstanceTemplate):
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
    
    @property
    def choice_setting_collection_value_template(self,) -> Optional[List[device_management_configuration_choice_setting_value_template.DeviceManagementConfigurationChoiceSettingValueTemplate]]:
        """
        Gets the choiceSettingCollectionValueTemplate property value. Choice Setting Collection Value Template
        Returns: Optional[List[device_management_configuration_choice_setting_value_template.DeviceManagementConfigurationChoiceSettingValueTemplate]]
        """
        return self._choice_setting_collection_value_template
    
    @choice_setting_collection_value_template.setter
    def choice_setting_collection_value_template(self,value: Optional[List[device_management_configuration_choice_setting_value_template.DeviceManagementConfigurationChoiceSettingValueTemplate]] = None) -> None:
        """
        Sets the choiceSettingCollectionValueTemplate property value. Choice Setting Collection Value Template
        Args:
            value: Value to set for the choiceSettingCollectionValueTemplate property.
        """
        self._choice_setting_collection_value_template = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new DeviceManagementConfigurationChoiceSettingCollectionInstanceTemplate and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.deviceManagementConfigurationChoiceSettingCollectionInstanceTemplate"
        # Linked policy may append values which are not present in the template.
        self._allow_unmanaged_values: Optional[bool] = None
        # Choice Setting Collection Value Template
        self._choice_setting_collection_value_template: Optional[List[device_management_configuration_choice_setting_value_template.DeviceManagementConfigurationChoiceSettingValueTemplate]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementConfigurationChoiceSettingCollectionInstanceTemplate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationChoiceSettingCollectionInstanceTemplate
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementConfigurationChoiceSettingCollectionInstanceTemplate()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "allow_unmanaged_values": lambda n : setattr(self, 'allow_unmanaged_values', n.get_bool_value()),
            "choice_setting_collection_value_template": lambda n : setattr(self, 'choice_setting_collection_value_template', n.get_collection_of_object_values(device_management_configuration_choice_setting_value_template.DeviceManagementConfigurationChoiceSettingValueTemplate)),
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
        writer.write_collection_of_object_values("choiceSettingCollectionValueTemplate", self.choice_setting_collection_value_template)
    

