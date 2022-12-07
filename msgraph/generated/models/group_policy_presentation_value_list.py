from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

group_policy_presentation_value = lazy_import('msgraph.generated.models.group_policy_presentation_value')
key_value_pair = lazy_import('msgraph.generated.models.key_value_pair')

class GroupPolicyPresentationValueList(group_policy_presentation_value.GroupPolicyPresentationValue):
    def __init__(self,) -> None:
        """
        Instantiates a new GroupPolicyPresentationValueList and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # A list of pairs for the associated presentation.
        self._values: Optional[List[key_value_pair.KeyValuePair]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> GroupPolicyPresentationValueList:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: GroupPolicyPresentationValueList
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return GroupPolicyPresentationValueList()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "values": lambda n : setattr(self, 'values', n.get_collection_of_object_values(key_value_pair.KeyValuePair)),
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
        writer.write_collection_of_object_values("values", self.values)
    
    @property
    def values(self,) -> Optional[List[key_value_pair.KeyValuePair]]:
        """
        Gets the values property value. A list of pairs for the associated presentation.
        Returns: Optional[List[key_value_pair.KeyValuePair]]
        """
        return self._values
    
    @values.setter
    def values(self,value: Optional[List[key_value_pair.KeyValuePair]] = None) -> None:
        """
        Sets the values property value. A list of pairs for the associated presentation.
        Args:
            value: Value to set for the values property.
        """
        self._values = value
    

