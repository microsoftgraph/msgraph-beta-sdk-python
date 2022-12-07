from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class PaymentTerm(entity.Entity):
    @property
    def calculate_discount_on_credit_memos(self,) -> Optional[bool]:
        """
        Gets the calculateDiscountOnCreditMemos property value. The calculateDiscountOnCreditMemos property
        Returns: Optional[bool]
        """
        return self._calculate_discount_on_credit_memos
    
    @calculate_discount_on_credit_memos.setter
    def calculate_discount_on_credit_memos(self,value: Optional[bool] = None) -> None:
        """
        Sets the calculateDiscountOnCreditMemos property value. The calculateDiscountOnCreditMemos property
        Args:
            value: Value to set for the calculateDiscountOnCreditMemos property.
        """
        self._calculate_discount_on_credit_memos = value
    
    @property
    def code(self,) -> Optional[str]:
        """
        Gets the code property value. The code property
        Returns: Optional[str]
        """
        return self._code
    
    @code.setter
    def code(self,value: Optional[str] = None) -> None:
        """
        Sets the code property value. The code property
        Args:
            value: Value to set for the code property.
        """
        self._code = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new paymentTerm and sets the default values.
        """
        super().__init__()
        # The calculateDiscountOnCreditMemos property
        self._calculate_discount_on_credit_memos: Optional[bool] = None
        # The code property
        self._code: Optional[str] = None
        # The discountDateCalculation property
        self._discount_date_calculation: Optional[str] = None
        # The discountPercent property
        self._discount_percent: Optional[float] = None
        # The displayName property
        self._display_name: Optional[str] = None
        # The dueDateCalculation property
        self._due_date_calculation: Optional[str] = None
        # The lastModifiedDateTime property
        self._last_modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
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
    
    @property
    def discount_date_calculation(self,) -> Optional[str]:
        """
        Gets the discountDateCalculation property value. The discountDateCalculation property
        Returns: Optional[str]
        """
        return self._discount_date_calculation
    
    @discount_date_calculation.setter
    def discount_date_calculation(self,value: Optional[str] = None) -> None:
        """
        Sets the discountDateCalculation property value. The discountDateCalculation property
        Args:
            value: Value to set for the discountDateCalculation property.
        """
        self._discount_date_calculation = value
    
    @property
    def discount_percent(self,) -> Optional[float]:
        """
        Gets the discountPercent property value. The discountPercent property
        Returns: Optional[float]
        """
        return self._discount_percent
    
    @discount_percent.setter
    def discount_percent(self,value: Optional[float] = None) -> None:
        """
        Sets the discountPercent property value. The discountPercent property
        Args:
            value: Value to set for the discountPercent property.
        """
        self._discount_percent = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The displayName property
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The displayName property
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def due_date_calculation(self,) -> Optional[str]:
        """
        Gets the dueDateCalculation property value. The dueDateCalculation property
        Returns: Optional[str]
        """
        return self._due_date_calculation
    
    @due_date_calculation.setter
    def due_date_calculation(self,value: Optional[str] = None) -> None:
        """
        Sets the dueDateCalculation property value. The dueDateCalculation property
        Args:
            value: Value to set for the dueDateCalculation property.
        """
        self._due_date_calculation = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "calculate_discount_on_credit_memos": lambda n : setattr(self, 'calculate_discount_on_credit_memos', n.get_bool_value()),
            "code": lambda n : setattr(self, 'code', n.get_str_value()),
            "discount_date_calculation": lambda n : setattr(self, 'discount_date_calculation', n.get_str_value()),
            "discount_percent": lambda n : setattr(self, 'discount_percent', n.get_float_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "due_date_calculation": lambda n : setattr(self, 'due_date_calculation', n.get_str_value()),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. The lastModifiedDateTime property
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. The lastModifiedDateTime property
        Args:
            value: Value to set for the lastModifiedDateTime property.
        """
        self._last_modified_date_time = value
    
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
    

