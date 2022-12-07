from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_management_setting_category = lazy_import('msgraph.generated.models.device_management_setting_category')
device_management_setting_instance = lazy_import('msgraph.generated.models.device_management_setting_instance')

class DeviceManagementTemplateSettingCategory(device_management_setting_category.DeviceManagementSettingCategory):
    def __init__(self,) -> None:
        """
        Instantiates a new DeviceManagementTemplateSettingCategory and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The settings this category contains
        self._recommended_settings: Optional[List[device_management_setting_instance.DeviceManagementSettingInstance]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementTemplateSettingCategory:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementTemplateSettingCategory
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementTemplateSettingCategory()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "recommended_settings": lambda n : setattr(self, 'recommended_settings', n.get_collection_of_object_values(device_management_setting_instance.DeviceManagementSettingInstance)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def recommended_settings(self,) -> Optional[List[device_management_setting_instance.DeviceManagementSettingInstance]]:
        """
        Gets the recommendedSettings property value. The settings this category contains
        Returns: Optional[List[device_management_setting_instance.DeviceManagementSettingInstance]]
        """
        return self._recommended_settings
    
    @recommended_settings.setter
    def recommended_settings(self,value: Optional[List[device_management_setting_instance.DeviceManagementSettingInstance]] = None) -> None:
        """
        Sets the recommendedSettings property value. The settings this category contains
        Args:
            value: Value to set for the recommendedSettings property.
        """
        self._recommended_settings = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("recommendedSettings", self.recommended_settings)
    

