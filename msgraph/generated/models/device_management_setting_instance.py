from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class DeviceManagementSettingInstance(entity.Entity):
    """
    Base type for a setting instance
    """
    def __init__(self,) -> None:
        """
        Instantiates a new deviceManagementSettingInstance and sets the default values.
        """
        super().__init__()
        # The ID of the setting definition for this instance
        self._definition_id: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # JSON representation of the value
        self._value_json: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementSettingInstance:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementSettingInstance
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementSettingInstance()
    
    @property
    def definition_id(self,) -> Optional[str]:
        """
        Gets the definitionId property value. The ID of the setting definition for this instance
        Returns: Optional[str]
        """
        return self._definition_id
    
    @definition_id.setter
    def definition_id(self,value: Optional[str] = None) -> None:
        """
        Sets the definitionId property value. The ID of the setting definition for this instance
        Args:
            value: Value to set for the definitionId property.
        """
        self._definition_id = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "definition_id": lambda n : setattr(self, 'definition_id', n.get_str_value()),
            "value_json": lambda n : setattr(self, 'value_json', n.get_str_value()),
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
        writer.write_str_value("definitionId", self.definition_id)
        writer.write_str_value("valueJson", self.value_json)
    
    @property
    def value_json(self,) -> Optional[str]:
        """
        Gets the valueJson property value. JSON representation of the value
        Returns: Optional[str]
        """
        return self._value_json
    
    @value_json.setter
    def value_json(self,value: Optional[str] = None) -> None:
        """
        Sets the valueJson property value. JSON representation of the value
        Args:
            value: Value to set for the valueJson property.
        """
        self._value_json = value
    

