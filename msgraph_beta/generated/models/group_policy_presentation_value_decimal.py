from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .group_policy_presentation_value import GroupPolicyPresentationValue

from .group_policy_presentation_value import GroupPolicyPresentationValue

@dataclass
class GroupPolicyPresentationValueDecimal(GroupPolicyPresentationValue, Parsable):
    """
    The entity represents an unsigned integer value of a decimal text box presentation on a policy definition.
    """
    # The OdataType property
    odata_type: Optional[str] = None
    # An unsigned integer value for the associated presentation.
    value: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> GroupPolicyPresentationValueDecimal:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: GroupPolicyPresentationValueDecimal
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return GroupPolicyPresentationValueDecimal()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .group_policy_presentation_value import GroupPolicyPresentationValue

        from .group_policy_presentation_value import GroupPolicyPresentationValue

        fields: dict[str, Callable[[Any], None]] = {
            "value": lambda n : setattr(self, 'value', n.get_int_value()),
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
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_int_value("value", self.value)
    

