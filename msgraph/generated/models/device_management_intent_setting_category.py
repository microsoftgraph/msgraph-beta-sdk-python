from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_management_setting_category, device_management_setting_instance

from . import device_management_setting_category

@dataclass
class DeviceManagementIntentSettingCategory(device_management_setting_category.DeviceManagementSettingCategory):
    # The OdataType property
    odata_type: Optional[str] = None
    # The settings this category contains
    settings: Optional[List[device_management_setting_instance.DeviceManagementSettingInstance]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementIntentSettingCategory:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementIntentSettingCategory
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return DeviceManagementIntentSettingCategory()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_management_setting_category, device_management_setting_instance

        from . import device_management_setting_category, device_management_setting_instance

        fields: Dict[str, Callable[[Any], None]] = {
            "settings": lambda n : setattr(self, 'settings', n.get_collection_of_object_values(device_management_setting_instance.DeviceManagementSettingInstance)),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("settings", self.settings)
    

