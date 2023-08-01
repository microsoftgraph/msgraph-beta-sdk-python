from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ........models.json import Json

@dataclass
class Gamma_InvPostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The alpha property
    alpha: Optional[Json] = None
    # The beta property
    beta: Optional[Json] = None
    # The probability property
    probability: Optional[Json] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Gamma_InvPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Gamma_InvPostRequestBody
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Gamma_InvPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ........models.json import Json

        from ........models.json import Json

        fields: Dict[str, Callable[[Any], None]] = {
            "alpha": lambda n : setattr(self, 'alpha', n.get_object_value(Json)),
            "beta": lambda n : setattr(self, 'beta', n.get_object_value(Json)),
            "probability": lambda n : setattr(self, 'probability', n.get_object_value(Json)),
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
        writer.write_object_value("alpha", self.alpha)
        writer.write_object_value("beta", self.beta)
        writer.write_object_value("probability", self.probability)
        writer.write_additional_data_value(self.additional_data)
    

