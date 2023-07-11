from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ......models.assignment_order import AssignmentOrder

@dataclass
class SetOrderPostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The newAssignmentOrder property
    new_assignment_order: Optional[AssignmentOrder] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SetOrderPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SetOrderPostRequestBody
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return SetOrderPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ......models.assignment_order import AssignmentOrder

        from ......models.assignment_order import AssignmentOrder

        fields: Dict[str, Callable[[Any], None]] = {
            "newAssignmentOrder": lambda n : setattr(self, 'new_assignment_order', n.get_object_value(AssignmentOrder)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_object_value("newAssignmentOrder", self.new_assignment_order)
        writer.write_additional_data_value(self.additional_data)
    

