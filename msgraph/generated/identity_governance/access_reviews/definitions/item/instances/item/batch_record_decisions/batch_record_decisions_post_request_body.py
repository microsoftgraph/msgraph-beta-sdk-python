from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class BatchRecordDecisionsPostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The decision property
    decision: Optional[str] = None
    # The justification property
    justification: Optional[str] = None
    # The principalId property
    principal_id: Optional[str] = None
    # The resourceId property
    resource_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> BatchRecordDecisionsPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BatchRecordDecisionsPostRequestBody
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return BatchRecordDecisionsPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "decision": lambda n : setattr(self, 'decision', n.get_str_value()),
            "justification": lambda n : setattr(self, 'justification', n.get_str_value()),
            "principalId": lambda n : setattr(self, 'principal_id', n.get_str_value()),
            "resourceId": lambda n : setattr(self, 'resource_id', n.get_str_value()),
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
        writer.write_str_value("decision", self.decision)
        writer.write_str_value("justification", self.justification)
        writer.write_str_value("principalId", self.principal_id)
        writer.write_str_value("resourceId", self.resource_id)
        writer.write_additional_data_value(self.additional_data)
    

