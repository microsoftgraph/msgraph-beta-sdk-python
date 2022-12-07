from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_management_configuration_string_setting_value = lazy_import('msgraph.generated.models.device_management_configuration_string_setting_value')

class DeviceManagementConfigurationReferenceSettingValue(device_management_configuration_string_setting_value.DeviceManagementConfigurationStringSettingValue):
    def __init__(self,) -> None:
        """
        Instantiates a new DeviceManagementConfigurationReferenceSettingValue and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.deviceManagementConfigurationReferenceSettingValue"
        # A note that admin can use to put some contextual information
        self._note: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementConfigurationReferenceSettingValue:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationReferenceSettingValue
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementConfigurationReferenceSettingValue()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "note": lambda n : setattr(self, 'note', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def note(self,) -> Optional[str]:
        """
        Gets the note property value. A note that admin can use to put some contextual information
        Returns: Optional[str]
        """
        return self._note
    
    @note.setter
    def note(self,value: Optional[str] = None) -> None:
        """
        Sets the note property value. A note that admin can use to put some contextual information
        Args:
            value: Value to set for the note property.
        """
        self._note = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("note", self.note)
    

