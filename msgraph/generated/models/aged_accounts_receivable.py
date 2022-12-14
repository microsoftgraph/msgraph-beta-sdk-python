from __future__ import annotations
from datetime import date
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class AgedAccountsReceivable(entity.Entity):
    @property
    def aged_as_of_date(self,) -> Optional[Date]:
        """
        Gets the agedAsOfDate property value. The agedAsOfDate property
        Returns: Optional[Date]
        """
        return self._aged_as_of_date
    
    @aged_as_of_date.setter
    def aged_as_of_date(self,value: Optional[Date] = None) -> None:
        """
        Sets the agedAsOfDate property value. The agedAsOfDate property
        Args:
            value: Value to set for the agedAsOfDate property.
        """
        self._aged_as_of_date = value
    
    @property
    def balance_due(self,) -> Optional[float]:
        """
        Gets the balanceDue property value. The balanceDue property
        Returns: Optional[float]
        """
        return self._balance_due
    
    @balance_due.setter
    def balance_due(self,value: Optional[float] = None) -> None:
        """
        Sets the balanceDue property value. The balanceDue property
        Args:
            value: Value to set for the balanceDue property.
        """
        self._balance_due = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new AgedAccountsReceivable and sets the default values.
        """
        super().__init__()
        # The agedAsOfDate property
        self._aged_as_of_date: Optional[Date] = None
        # The balanceDue property
        self._balance_due: Optional[float] = None
        # The currencyCode property
        self._currency_code: Optional[str] = None
        # The currentAmount property
        self._current_amount: Optional[float] = None
        # The customerNumber property
        self._customer_number: Optional[str] = None
        # The name property
        self._name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The period1Amount property
        self._period1_amount: Optional[float] = None
        # The period2Amount property
        self._period2_amount: Optional[float] = None
        # The period3Amount property
        self._period3_amount: Optional[float] = None
        # The periodLengthFilter property
        self._period_length_filter: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AgedAccountsReceivable:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AgedAccountsReceivable
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AgedAccountsReceivable()
    
    @property
    def currency_code(self,) -> Optional[str]:
        """
        Gets the currencyCode property value. The currencyCode property
        Returns: Optional[str]
        """
        return self._currency_code
    
    @currency_code.setter
    def currency_code(self,value: Optional[str] = None) -> None:
        """
        Sets the currencyCode property value. The currencyCode property
        Args:
            value: Value to set for the currencyCode property.
        """
        self._currency_code = value
    
    @property
    def current_amount(self,) -> Optional[float]:
        """
        Gets the currentAmount property value. The currentAmount property
        Returns: Optional[float]
        """
        return self._current_amount
    
    @current_amount.setter
    def current_amount(self,value: Optional[float] = None) -> None:
        """
        Sets the currentAmount property value. The currentAmount property
        Args:
            value: Value to set for the currentAmount property.
        """
        self._current_amount = value
    
    @property
    def customer_number(self,) -> Optional[str]:
        """
        Gets the customerNumber property value. The customerNumber property
        Returns: Optional[str]
        """
        return self._customer_number
    
    @customer_number.setter
    def customer_number(self,value: Optional[str] = None) -> None:
        """
        Sets the customerNumber property value. The customerNumber property
        Args:
            value: Value to set for the customerNumber property.
        """
        self._customer_number = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "aged_as_of_date": lambda n : setattr(self, 'aged_as_of_date', n.get_object_value(Date)),
            "balance_due": lambda n : setattr(self, 'balance_due', n.get_float_value()),
            "currency_code": lambda n : setattr(self, 'currency_code', n.get_str_value()),
            "current_amount": lambda n : setattr(self, 'current_amount', n.get_float_value()),
            "customer_number": lambda n : setattr(self, 'customer_number', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "period1_amount": lambda n : setattr(self, 'period1_amount', n.get_float_value()),
            "period2_amount": lambda n : setattr(self, 'period2_amount', n.get_float_value()),
            "period3_amount": lambda n : setattr(self, 'period3_amount', n.get_float_value()),
            "period_length_filter": lambda n : setattr(self, 'period_length_filter', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def name(self,) -> Optional[str]:
        """
        Gets the name property value. The name property
        Returns: Optional[str]
        """
        return self._name
    
    @name.setter
    def name(self,value: Optional[str] = None) -> None:
        """
        Sets the name property value. The name property
        Args:
            value: Value to set for the name property.
        """
        self._name = value
    
    @property
    def period1_amount(self,) -> Optional[float]:
        """
        Gets the period1Amount property value. The period1Amount property
        Returns: Optional[float]
        """
        return self._period1_amount
    
    @period1_amount.setter
    def period1_amount(self,value: Optional[float] = None) -> None:
        """
        Sets the period1Amount property value. The period1Amount property
        Args:
            value: Value to set for the period1Amount property.
        """
        self._period1_amount = value
    
    @property
    def period2_amount(self,) -> Optional[float]:
        """
        Gets the period2Amount property value. The period2Amount property
        Returns: Optional[float]
        """
        return self._period2_amount
    
    @period2_amount.setter
    def period2_amount(self,value: Optional[float] = None) -> None:
        """
        Sets the period2Amount property value. The period2Amount property
        Args:
            value: Value to set for the period2Amount property.
        """
        self._period2_amount = value
    
    @property
    def period3_amount(self,) -> Optional[float]:
        """
        Gets the period3Amount property value. The period3Amount property
        Returns: Optional[float]
        """
        return self._period3_amount
    
    @period3_amount.setter
    def period3_amount(self,value: Optional[float] = None) -> None:
        """
        Sets the period3Amount property value. The period3Amount property
        Args:
            value: Value to set for the period3Amount property.
        """
        self._period3_amount = value
    
    @property
    def period_length_filter(self,) -> Optional[str]:
        """
        Gets the periodLengthFilter property value. The periodLengthFilter property
        Returns: Optional[str]
        """
        return self._period_length_filter
    
    @period_length_filter.setter
    def period_length_filter(self,value: Optional[str] = None) -> None:
        """
        Sets the periodLengthFilter property value. The periodLengthFilter property
        Args:
            value: Value to set for the periodLengthFilter property.
        """
        self._period_length_filter = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("agedAsOfDate", self.aged_as_of_date)
        writer.write_float_value("balanceDue", self.balance_due)
        writer.write_str_value("currencyCode", self.currency_code)
        writer.write_float_value("currentAmount", self.current_amount)
        writer.write_str_value("customerNumber", self.customer_number)
        writer.write_str_value("name", self.name)
        writer.write_float_value("period1Amount", self.period1_amount)
        writer.write_float_value("period2Amount", self.period2_amount)
        writer.write_float_value("period3Amount", self.period3_amount)
        writer.write_str_value("periodLengthFilter", self.period_length_filter)
    

