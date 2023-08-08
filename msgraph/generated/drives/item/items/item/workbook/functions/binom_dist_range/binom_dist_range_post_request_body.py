from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ........models.json import Json

@dataclass
class Binom_Dist_RangePostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The numberS property
    number_s: Optional[Json] = None
    # The numberS2 property
    number_s2: Optional[Json] = None
    # The probabilityS property
    probability_s: Optional[Json] = None
    # The trials property
    trials: Optional[Json] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Binom_Dist_RangePostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Binom_Dist_RangePostRequestBody
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Binom_Dist_RangePostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ........models.json import Json

        from ........models.json import Json

        fields: Dict[str, Callable[[Any], None]] = {
            "numberS": lambda n : setattr(self, 'number_s', n.get_object_value(Json)),
            "numberS2": lambda n : setattr(self, 'number_s2', n.get_object_value(Json)),
            "probabilityS": lambda n : setattr(self, 'probability_s', n.get_object_value(Json)),
            "trials": lambda n : setattr(self, 'trials', n.get_object_value(Json)),
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
        writer.write_object_value("numberS", self.number_s)
        writer.write_object_value("numberS2", self.number_s2)
        writer.write_object_value("probabilityS", self.probability_s)
        writer.write_object_value("trials", self.trials)
        writer.write_additional_data_value(self.additional_data)
    

