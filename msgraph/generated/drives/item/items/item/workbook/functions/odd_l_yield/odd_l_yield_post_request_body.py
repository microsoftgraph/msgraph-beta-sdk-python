from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ........models.json import Json

@dataclass
class OddLYieldPostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The basis property
    basis: Optional[Json] = None
    # The frequency property
    frequency: Optional[Json] = None
    # The lastInterest property
    last_interest: Optional[Json] = None
    # The maturity property
    maturity: Optional[Json] = None
    # The pr property
    pr: Optional[Json] = None
    # The rate property
    rate: Optional[Json] = None
    # The redemption property
    redemption: Optional[Json] = None
    # The settlement property
    settlement: Optional[Json] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OddLYieldPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OddLYieldPostRequestBody
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return OddLYieldPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ........models.json import Json

        from ........models.json import Json

        fields: Dict[str, Callable[[Any], None]] = {
            "basis": lambda n : setattr(self, 'basis', n.get_object_value(Json)),
            "frequency": lambda n : setattr(self, 'frequency', n.get_object_value(Json)),
            "lastInterest": lambda n : setattr(self, 'last_interest', n.get_object_value(Json)),
            "maturity": lambda n : setattr(self, 'maturity', n.get_object_value(Json)),
            "pr": lambda n : setattr(self, 'pr', n.get_object_value(Json)),
            "rate": lambda n : setattr(self, 'rate', n.get_object_value(Json)),
            "redemption": lambda n : setattr(self, 'redemption', n.get_object_value(Json)),
            "settlement": lambda n : setattr(self, 'settlement', n.get_object_value(Json)),
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
        writer.write_object_value("basis", self.basis)
        writer.write_object_value("frequency", self.frequency)
        writer.write_object_value("lastInterest", self.last_interest)
        writer.write_object_value("maturity", self.maturity)
        writer.write_object_value("pr", self.pr)
        writer.write_object_value("rate", self.rate)
        writer.write_object_value("redemption", self.redemption)
        writer.write_object_value("settlement", self.settlement)
        writer.write_additional_data_value(self.additional_data)
    

