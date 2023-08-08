from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .education_item_body import EducationItemBody

@dataclass
class RubricQualityFeedbackModel(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Specific feedback for one quality of this rubric.
    feedback: Optional[EducationItemBody] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The ID of the rubricQuality that this feedback is related to.
    quality_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RubricQualityFeedbackModel:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RubricQualityFeedbackModel
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return RubricQualityFeedbackModel()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .education_item_body import EducationItemBody

        from .education_item_body import EducationItemBody

        fields: Dict[str, Callable[[Any], None]] = {
            "feedback": lambda n : setattr(self, 'feedback', n.get_object_value(EducationItemBody)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "qualityId": lambda n : setattr(self, 'quality_id', n.get_str_value()),
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
        writer.write_object_value("feedback", self.feedback)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("qualityId", self.quality_id)
        writer.write_additional_data_value(self.additional_data)
    

