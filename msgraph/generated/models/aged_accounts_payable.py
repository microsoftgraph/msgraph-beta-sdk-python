from __future__ import annotations
from dataclasses import dataclass, field
from datetime import date
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity

from . import entity

@dataclass
class AgedAccountsPayable(entity.Entity):
    # The agedAsOfDate property
    aged_as_of_date: Optional[date] = None
    # The balanceDue property
    balance_due: Optional[float] = None
    # The currencyCode property
    currency_code: Optional[str] = None
    # The currentAmount property
    current_amount: Optional[float] = None
    # The name property
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The periodLengthFilter property
    period_length_filter: Optional[str] = None
    # The period1Amount property
    period1_amount: Optional[float] = None
    # The period2Amount property
    period2_amount: Optional[float] = None
    # The period3Amount property
    period3_amount: Optional[float] = None
    # The vendorNumber property
    vendor_number: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AgedAccountsPayable:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AgedAccountsPayable
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AgedAccountsPayable()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "agedAsOfDate": lambda n : setattr(self, 'aged_as_of_date', n.get_date_value()),
            "balanceDue": lambda n : setattr(self, 'balance_due', n.get_float_value()),
            "currencyCode": lambda n : setattr(self, 'currency_code', n.get_str_value()),
            "currentAmount": lambda n : setattr(self, 'current_amount', n.get_float_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "period1Amount": lambda n : setattr(self, 'period1_amount', n.get_float_value()),
            "period2Amount": lambda n : setattr(self, 'period2_amount', n.get_float_value()),
            "period3Amount": lambda n : setattr(self, 'period3_amount', n.get_float_value()),
            "periodLengthFilter": lambda n : setattr(self, 'period_length_filter', n.get_str_value()),
            "vendorNumber": lambda n : setattr(self, 'vendor_number', n.get_str_value()),
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
        writer.write_date_value("agedAsOfDate", self.aged_as_of_date)
        writer.write_float_value("balanceDue", self.balance_due)
        writer.write_str_value("currencyCode", self.currency_code)
        writer.write_float_value("currentAmount", self.current_amount)
        writer.write_str_value("name", self.name)
        writer.write_float_value("period1Amount", self.period1_amount)
        writer.write_float_value("period2Amount", self.period2_amount)
        writer.write_float_value("period3Amount", self.period3_amount)
        writer.write_str_value("periodLengthFilter", self.period_length_filter)
        writer.write_str_value("vendorNumber", self.vendor_number)
    

