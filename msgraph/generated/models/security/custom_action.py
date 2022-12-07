from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

information_protection_action = lazy_import('msgraph.generated.models.security.information_protection_action')
key_value_pair = lazy_import('msgraph.generated.models.security.key_value_pair')

class CustomAction(information_protection_action.InformationProtectionAction):
    def __init__(self,) -> None:
        """
        Instantiates a new CustomAction and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.security.customAction"
        # Name of the custom action.
        self._name: Optional[str] = None
        # Properties, in key-value pair format, of the action.
        self._properties: Optional[List[key_value_pair.KeyValuePair]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CustomAction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CustomAction
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CustomAction()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "properties": lambda n : setattr(self, 'properties', n.get_collection_of_object_values(key_value_pair.KeyValuePair)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def name(self,) -> Optional[str]:
        """
        Gets the name property value. Name of the custom action.
        Returns: Optional[str]
        """
        return self._name
    
    @name.setter
    def name(self,value: Optional[str] = None) -> None:
        """
        Sets the name property value. Name of the custom action.
        Args:
            value: Value to set for the name property.
        """
        self._name = value
    
    @property
    def properties(self,) -> Optional[List[key_value_pair.KeyValuePair]]:
        """
        Gets the properties property value. Properties, in key-value pair format, of the action.
        Returns: Optional[List[key_value_pair.KeyValuePair]]
        """
        return self._properties
    
    @properties.setter
    def properties(self,value: Optional[List[key_value_pair.KeyValuePair]] = None) -> None:
        """
        Sets the properties property value. Properties, in key-value pair format, of the action.
        Args:
            value: Value to set for the properties property.
        """
        self._properties = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("name", self.name)
        writer.write_collection_of_object_values("properties", self.properties)
    

