from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ........models.json import Json

@dataclass
class Norm_S_DistPostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The cumulative property
    cumulative: Optional[Json] = None
    # The z property
    z: Optional[Json] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Norm_S_DistPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Norm_S_DistPostRequestBody
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Norm_S_DistPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ........models.json import Json

        from ........models.json import Json

        fields: Dict[str, Callable[[Any], None]] = {
            "cumulative": lambda n : setattr(self, 'cumulative', n.get_object_value(Json)),
            "z": lambda n : setattr(self, 'z', n.get_object_value(Json)),
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
        writer.write_object_value("cumulative", self.cumulative)
        writer.write_object_value("z", self.z)
        writer.write_additional_data_value(self.additional_data)
    

