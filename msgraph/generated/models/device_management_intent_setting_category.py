from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_management_setting_category, device_management_setting_instance

from . import device_management_setting_category

class DeviceManagementIntentSettingCategory(device_management_setting_category.DeviceManagementSettingCategory):
    def __init__(self,) -> None:
        """
        Instantiates a new DeviceManagementIntentSettingCategory and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The settings this category contains
        self._settings: Optional[List[device_management_setting_instance.DeviceManagementSettingInstance]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementIntentSettingCategory:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementIntentSettingCategory
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementIntentSettingCategory()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
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
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("settings", self.settings)
    
    @property
    def settings(self,) -> Optional[List[device_management_setting_instance.DeviceManagementSettingInstance]]:
        """
        Gets the settings property value. The settings this category contains
        Returns: Optional[List[device_management_setting_instance.DeviceManagementSettingInstance]]
        """
        return self._settings
    
    @settings.setter
    def settings(self,value: Optional[List[device_management_setting_instance.DeviceManagementSettingInstance]] = None) -> None:
        """
        Sets the settings property value. The settings this category contains
        Args:
            value: Value to set for the settings property.
        """
        self._settings = value
    

