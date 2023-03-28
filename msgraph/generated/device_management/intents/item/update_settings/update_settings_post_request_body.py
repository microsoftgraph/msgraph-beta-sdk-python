from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....models import device_management_setting_instance

class UpdateSettingsPostRequestBody(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new updateSettingsPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The settings property
        self._settings: Optional[List[device_management_setting_instance.DeviceManagementSettingInstance]] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UpdateSettingsPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UpdateSettingsPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UpdateSettingsPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .....models import device_management_setting_instance

        fields: Dict[str, Callable[[Any], None]] = {
            "settings": lambda n : setattr(self, 'settings', n.get_collection_of_object_values(device_management_setting_instance.DeviceManagementSettingInstance)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_object_values("settings", self.settings)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def settings(self,) -> Optional[List[device_management_setting_instance.DeviceManagementSettingInstance]]:
        """
        Gets the settings property value. The settings property
        Returns: Optional[List[device_management_setting_instance.DeviceManagementSettingInstance]]
        """
        return self._settings
    
    @settings.setter
    def settings(self,value: Optional[List[device_management_setting_instance.DeviceManagementSettingInstance]] = None) -> None:
        """
        Sets the settings property value. The settings property
        Args:
            value: Value to set for the settings property.
        """
        self._settings = value
    

