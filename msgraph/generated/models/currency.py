from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity

from . import entity

@dataclass
class Currency(entity.Entity):
    # The amountDecimalPlaces property
    amount_decimal_places: Optional[str] = None
    # The amountRoundingPrecision property
    amount_rounding_precision: Optional[float] = None
    # The code property
    code: Optional[str] = None
    # The displayName property
    display_name: Optional[str] = None
    # The lastModifiedDateTime property
    last_modified_date_time: Optional[datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The symbol property
    symbol: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Currency:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Currency
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Currency()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "amountDecimalPlaces": lambda n : setattr(self, 'amount_decimal_places', n.get_str_value()),
            "amountRoundingPrecision": lambda n : setattr(self, 'amount_rounding_precision', n.get_float_value()),
            "code": lambda n : setattr(self, 'code', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "symbol": lambda n : setattr(self, 'symbol', n.get_str_value()),
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
        writer.write_str_value("amountDecimalPlaces", self.amount_decimal_places)
        writer.write_float_value("amountRoundingPrecision", self.amount_rounding_precision)
        writer.write_str_value("code", self.code)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("symbol", self.symbol)
    

