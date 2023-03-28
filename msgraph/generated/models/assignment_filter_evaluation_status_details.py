from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity

from . import entity

class AssignmentFilterEvaluationStatusDetails(entity.Entity):
    """
    A class containing information about the payloads on which filter has been applied.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new assignmentFilterEvaluationStatusDetails and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # PayloadId on which filter has been applied.
        self._payload_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AssignmentFilterEvaluationStatusDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AssignmentFilterEvaluationStatusDetails
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AssignmentFilterEvaluationStatusDetails()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "payloadId": lambda n : setattr(self, 'payload_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def payload_id(self,) -> Optional[str]:
        """
        Gets the payloadId property value. PayloadId on which filter has been applied.
        Returns: Optional[str]
        """
        return self._payload_id
    
    @payload_id.setter
    def payload_id(self,value: Optional[str] = None) -> None:
        """
        Sets the payloadId property value. PayloadId on which filter has been applied.
        Args:
            value: Value to set for the payload_id property.
        """
        self._payload_id = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("payloadId", self.payload_id)
    

