from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class Currency(entity.Entity):
    @property
    def amount_decimal_places(self,) -> Optional[str]:
        """
        Gets the amountDecimalPlaces property value. The amountDecimalPlaces property
        Returns: Optional[str]
        """
        return self._amount_decimal_places
    
    @amount_decimal_places.setter
    def amount_decimal_places(self,value: Optional[str] = None) -> None:
        """
        Sets the amountDecimalPlaces property value. The amountDecimalPlaces property
        Args:
            value: Value to set for the amountDecimalPlaces property.
        """
        self._amount_decimal_places = value
    
    @property
    def amount_rounding_precision(self,) -> Optional[float]:
        """
        Gets the amountRoundingPrecision property value. The amountRoundingPrecision property
        Returns: Optional[float]
        """
        return self._amount_rounding_precision
    
    @amount_rounding_precision.setter
    def amount_rounding_precision(self,value: Optional[float] = None) -> None:
        """
        Sets the amountRoundingPrecision property value. The amountRoundingPrecision property
        Args:
            value: Value to set for the amountRoundingPrecision property.
        """
        self._amount_rounding_precision = value
    
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
        Instantiates a new currency and sets the default values.
        """
        super().__init__()
        # The amountDecimalPlaces property
        self._amount_decimal_places: Optional[str] = None
        # The amountRoundingPrecision property
        self._amount_rounding_precision: Optional[float] = None
        # The code property
        self._code: Optional[str] = None
        # The displayName property
        self._display_name: Optional[str] = None
        # The lastModifiedDateTime property
        self._last_modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The symbol property
        self._symbol: Optional[str] = None
    
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
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "amount_decimal_places": lambda n : setattr(self, 'amount_decimal_places', n.get_str_value()),
            "amount_rounding_precision": lambda n : setattr(self, 'amount_rounding_precision', n.get_float_value()),
            "code": lambda n : setattr(self, 'code', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "symbol": lambda n : setattr(self, 'symbol', n.get_str_value()),
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
        writer.write_str_value("amountDecimalPlaces", self.amount_decimal_places)
        writer.write_float_value("amountRoundingPrecision", self.amount_rounding_precision)
        writer.write_str_value("code", self.code)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("symbol", self.symbol)
    
    @property
    def symbol(self,) -> Optional[str]:
        """
        Gets the symbol property value. The symbol property
        Returns: Optional[str]
        """
        return self._symbol
    
    @symbol.setter
    def symbol(self,value: Optional[str] = None) -> None:
        """
        Sets the symbol property value. The symbol property
        Args:
            value: Value to set for the symbol property.
        """
        self._symbol = value
    

