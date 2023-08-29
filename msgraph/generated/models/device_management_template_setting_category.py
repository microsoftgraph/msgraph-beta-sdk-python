from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_management_setting_category import DeviceManagementSettingCategory
    from .device_management_setting_instance import DeviceManagementSettingInstance

from .device_management_setting_category import DeviceManagementSettingCategory

@dataclass
class DeviceManagementTemplateSettingCategory(DeviceManagementSettingCategory):
    """
    Entity representing a template setting category
    """
    # The OdataType property
    odata_type: Optional[str] = None
    # The settings this category contains
    recommended_settings: Optional[List[DeviceManagementSettingInstance]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementTemplateSettingCategory:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementTemplateSettingCategory
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return DeviceManagementTemplateSettingCategory()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .device_management_setting_category import DeviceManagementSettingCategory
        from .device_management_setting_instance import DeviceManagementSettingInstance

        from .device_management_setting_category import DeviceManagementSettingCategory
        from .device_management_setting_instance import DeviceManagementSettingInstance

        fields: Dict[str, Callable[[Any], None]] = {
            "recommendedSettings": lambda n : setattr(self, 'recommended_settings', n.get_collection_of_object_values(DeviceManagementSettingInstance)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("recommendedSettings", self.recommended_settings)
    

