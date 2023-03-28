from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import group_policy_presentation_value

from . import group_policy_presentation_value

class GroupPolicyPresentationValueMultiText(group_policy_presentation_value.GroupPolicyPresentationValue):
    def __init__(self,) -> None:
        """
        Instantiates a new GroupPolicyPresentationValueMultiText and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # A collection of non-empty strings for the associated presentation.
        self._values: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> GroupPolicyPresentationValueMultiText:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: GroupPolicyPresentationValueMultiText
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return GroupPolicyPresentationValueMultiText()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import group_policy_presentation_value

        fields: Dict[str, Callable[[Any], None]] = {
            "values": lambda n : setattr(self, 'values', n.get_collection_of_primitive_values(str)),
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
        writer.write_collection_of_primitive_values("values", self.values)
    
    @property
    def values(self,) -> Optional[List[str]]:
        """
        Gets the values property value. A collection of non-empty strings for the associated presentation.
        Returns: Optional[List[str]]
        """
        return self._values
    
    @values.setter
    def values(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the values property value. A collection of non-empty strings for the associated presentation.
        Args:
            value: Value to set for the values property.
        """
        self._values = value
    

