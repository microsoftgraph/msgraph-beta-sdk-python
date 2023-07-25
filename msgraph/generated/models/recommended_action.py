from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class RecommendedAction(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Web URL to the recommended action.
    action_web_url: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Potential improvement in the tenant security score from the recommended action.
    potential_score_impact: Optional[float] = None
    # Title of the recommended action.
    title: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RecommendedAction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RecommendedAction
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return RecommendedAction()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "actionWebUrl": lambda n : setattr(self, 'action_web_url', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "potentialScoreImpact": lambda n : setattr(self, 'potential_score_impact', n.get_float_value()),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
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
        writer.write_str_value("actionWebUrl", self.action_web_url)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_float_value("potentialScoreImpact", self.potential_score_impact)
        writer.write_str_value("title", self.title)
        writer.write_additional_data_value(self.additional_data)
    

