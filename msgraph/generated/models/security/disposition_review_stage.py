from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .. import entity

from .. import entity

@dataclass
class DispositionReviewStage(entity.Entity):
    # Name representing each stage within a collection.
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # A collection of reviewers at each stage.
    reviewers_email_addresses: Optional[List[str]] = None
    # The sequence number for each stage of the disposition review.
    stage_number: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DispositionReviewStage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DispositionReviewStage
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DispositionReviewStage()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .. import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "reviewersEmailAddresses": lambda n : setattr(self, 'reviewers_email_addresses', n.get_collection_of_primitive_values(str)),
            "stageNumber": lambda n : setattr(self, 'stage_number', n.get_int_value()),
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
        writer.write_str_value("name", self.name)
        writer.write_collection_of_primitive_values("reviewersEmailAddresses", self.reviewers_email_addresses)
        writer.write_int_value("stageNumber", self.stage_number)
    

