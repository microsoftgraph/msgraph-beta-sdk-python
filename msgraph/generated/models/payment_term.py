from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity

from . import entity

@dataclass
class PaymentTerm(entity.Entity):
    # The calculateDiscountOnCreditMemos property
    calculate_discount_on_credit_memos: Optional[bool] = None
    # The code property
    code: Optional[str] = None
    # The discountDateCalculation property
    discount_date_calculation: Optional[str] = None
    # The discountPercent property
    discount_percent: Optional[float] = None
    # The displayName property
    display_name: Optional[str] = None
    # The dueDateCalculation property
    due_date_calculation: Optional[str] = None
    # The lastModifiedDateTime property
    last_modified_date_time: Optional[datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PaymentTerm:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PaymentTerm
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PaymentTerm()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "calculateDiscountOnCreditMemos": lambda n : setattr(self, 'calculate_discount_on_credit_memos', n.get_bool_value()),
            "code": lambda n : setattr(self, 'code', n.get_str_value()),
            "discountDateCalculation": lambda n : setattr(self, 'discount_date_calculation', n.get_str_value()),
            "discountPercent": lambda n : setattr(self, 'discount_percent', n.get_float_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "dueDateCalculation": lambda n : setattr(self, 'due_date_calculation', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
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
        writer.write_bool_value("calculateDiscountOnCreditMemos", self.calculate_discount_on_credit_memos)
        writer.write_str_value("code", self.code)
        writer.write_str_value("discountDateCalculation", self.discount_date_calculation)
        writer.write_float_value("discountPercent", self.discount_percent)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("dueDateCalculation", self.due_date_calculation)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
    

