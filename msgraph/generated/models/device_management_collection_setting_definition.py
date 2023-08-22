from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_management_setting_definition import DeviceManagementSettingDefinition

from .device_management_setting_definition import DeviceManagementSettingDefinition

@dataclass
class DeviceManagementCollectionSettingDefinition(DeviceManagementSettingDefinition):
    """
    Entity representing the defintion for a collection setting
    """
    # The Setting Definition ID that describes what each element of the collection looks like
    element_definition_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementCollectionSettingDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementCollectionSettingDefinition
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return DeviceManagementCollectionSettingDefinition()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .device_management_setting_definition import DeviceManagementSettingDefinition

        from .device_management_setting_definition import DeviceManagementSettingDefinition

        fields: Dict[str, Callable[[Any], None]] = {
            "elementDefinitionId": lambda n : setattr(self, 'element_definition_id', n.get_str_value()),
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
        writer.write_str_value("elementDefinitionId", self.element_definition_id)
    

