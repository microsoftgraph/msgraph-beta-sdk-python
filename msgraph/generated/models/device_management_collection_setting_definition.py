from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_management_setting_definition

from . import device_management_setting_definition

class DeviceManagementCollectionSettingDefinition(device_management_setting_definition.DeviceManagementSettingDefinition):
    def __init__(self,) -> None:
        """
        Instantiates a new DeviceManagementCollectionSettingDefinition and sets the default values.
        """
        super().__init__()
        # The Setting Definition ID that describes what each element of the collection looks like
        self._element_definition_id: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementCollectionSettingDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementCollectionSettingDefinition
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementCollectionSettingDefinition()
    
    @property
    def element_definition_id(self,) -> Optional[str]:
        """
        Gets the elementDefinitionId property value. The Setting Definition ID that describes what each element of the collection looks like
        Returns: Optional[str]
        """
        return self._element_definition_id
    
    @element_definition_id.setter
    def element_definition_id(self,value: Optional[str] = None) -> None:
        """
        Sets the elementDefinitionId property value. The Setting Definition ID that describes what each element of the collection looks like
        Args:
            value: Value to set for the element_definition_id property.
        """
        self._element_definition_id = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_management_setting_definition

        fields: Dict[str, Callable[[Any], None]] = {
            "elementDefinitionId": lambda n : setattr(self, 'element_definition_id', n.get_str_value()),
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
        writer.write_str_value("elementDefinitionId", self.element_definition_id)
    

