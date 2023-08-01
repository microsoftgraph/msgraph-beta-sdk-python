from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .education_item_body import EducationItemBody
    from .rubric_criterion import RubricCriterion

@dataclass
class RubricQuality(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The collection of criteria for this rubric quality.
    criteria: Optional[List[RubricCriterion]] = None
    # The description of this rubric quality.
    description: Optional[EducationItemBody] = None
    # The name of this rubric quality.
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The ID of this resource.
    quality_id: Optional[str] = None
    # If present, a numerical weight for this quality.  Weights must add up to 100.
    weight: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RubricQuality:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RubricQuality
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return RubricQuality()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .education_item_body import EducationItemBody
        from .rubric_criterion import RubricCriterion

        from .education_item_body import EducationItemBody
        from .rubric_criterion import RubricCriterion

        fields: Dict[str, Callable[[Any], None]] = {
            "criteria": lambda n : setattr(self, 'criteria', n.get_collection_of_object_values(RubricCriterion)),
            "description": lambda n : setattr(self, 'description', n.get_object_value(EducationItemBody)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "qualityId": lambda n : setattr(self, 'quality_id', n.get_str_value()),
            "weight": lambda n : setattr(self, 'weight', n.get_float_value()),
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
        writer.write_collection_of_object_values("criteria", self.criteria)
        writer.write_object_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("qualityId", self.quality_id)
        writer.write_float_value("weight", self.weight)
        writer.write_additional_data_value(self.additional_data)
    

