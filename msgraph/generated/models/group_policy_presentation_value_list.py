from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .group_policy_presentation_value import GroupPolicyPresentationValue
    from .key_value_pair import KeyValuePair

from .group_policy_presentation_value import GroupPolicyPresentationValue

@dataclass
class GroupPolicyPresentationValueList(GroupPolicyPresentationValue):
    """
    The entity represents a collection of name/value pairs of a list box presentation on a policy definition.
    """
    # The OdataType property
    odata_type: Optional[str] = None
    # A list of pairs for the associated presentation.
    values: Optional[List[KeyValuePair]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> GroupPolicyPresentationValueList:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: GroupPolicyPresentationValueList
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return GroupPolicyPresentationValueList()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .group_policy_presentation_value import GroupPolicyPresentationValue
        from .key_value_pair import KeyValuePair

        from .group_policy_presentation_value import GroupPolicyPresentationValue
        from .key_value_pair import KeyValuePair

        fields: Dict[str, Callable[[Any], None]] = {
            "values": lambda n : setattr(self, 'values', n.get_collection_of_object_values(KeyValuePair)),
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
        writer.write_collection_of_object_values("values", self.values)
    

