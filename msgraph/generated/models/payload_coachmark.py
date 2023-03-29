from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import coachmark_location

class PayloadCoachmark(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new payloadCoachmark and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The coachmark location.
        self._coachmark_location: Optional[coachmark_location.CoachmarkLocation] = None
        # The description about the coachmark.
        self._description: Optional[str] = None
        # The coachmark indicator.
        self._indicator: Optional[str] = None
        # Indicates whether the coachmark is valid or not.
        self._is_valid: Optional[bool] = None
        # The coachmark language.
        self._language: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The coachmark order.
        self._order: Optional[str] = None
    
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def coachmark_location(self,) -> Optional[coachmark_location.CoachmarkLocation]:
        """
        Gets the coachmarkLocation property value. The coachmark location.
        Returns: Optional[coachmark_location.CoachmarkLocation]
        """
        return self._coachmark_location
    
    @coachmark_location.setter
    def coachmark_location(self,value: Optional[coachmark_location.CoachmarkLocation] = None) -> None:
        """
        Sets the coachmarkLocation property value. The coachmark location.
        Args:
            value: Value to set for the coachmark_location property.
        """
        self._coachmark_location = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PayloadCoachmark:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PayloadCoachmark
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PayloadCoachmark()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. The description about the coachmark.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. The description about the coachmark.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import coachmark_location

        fields: Dict[str, Callable[[Any], None]] = {
            "coachmarkLocation": lambda n : setattr(self, 'coachmark_location', n.get_object_value(coachmark_location.CoachmarkLocation)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "indicator": lambda n : setattr(self, 'indicator', n.get_str_value()),
            "isValid": lambda n : setattr(self, 'is_valid', n.get_bool_value()),
            "language": lambda n : setattr(self, 'language', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "order": lambda n : setattr(self, 'order', n.get_str_value()),
        }
        return fields
    
    @property
    def indicator(self,) -> Optional[str]:
        """
        Gets the indicator property value. The coachmark indicator.
        Returns: Optional[str]
        """
        return self._indicator
    
    @indicator.setter
    def indicator(self,value: Optional[str] = None) -> None:
        """
        Sets the indicator property value. The coachmark indicator.
        Args:
            value: Value to set for the indicator property.
        """
        self._indicator = value
    
    @property
    def is_valid(self,) -> Optional[bool]:
        """
        Gets the isValid property value. Indicates whether the coachmark is valid or not.
        Returns: Optional[bool]
        """
        return self._is_valid
    
    @is_valid.setter
    def is_valid(self,value: Optional[bool] = None) -> None:
        """
        Sets the isValid property value. Indicates whether the coachmark is valid or not.
        Args:
            value: Value to set for the is_valid property.
        """
        self._is_valid = value
    
    @property
    def language(self,) -> Optional[str]:
        """
        Gets the language property value. The coachmark language.
        Returns: Optional[str]
        """
        return self._language
    
    @language.setter
    def language(self,value: Optional[str] = None) -> None:
        """
        Sets the language property value. The coachmark language.
        Args:
            value: Value to set for the language property.
        """
        self._language = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the odata_type property.
        """
        self._odata_type = value
    
    @property
    def order(self,) -> Optional[str]:
        """
        Gets the order property value. The coachmark order.
        Returns: Optional[str]
        """
        return self._order
    
    @order.setter
    def order(self,value: Optional[str] = None) -> None:
        """
        Sets the order property value. The coachmark order.
        Args:
            value: Value to set for the order property.
        """
        self._order = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("coachmarkLocation", self.coachmark_location)
        writer.write_str_value("description", self.description)
        writer.write_str_value("indicator", self.indicator)
        writer.write_bool_value("isValid", self.is_valid)
        writer.write_str_value("language", self.language)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("order", self.order)
        writer.write_additional_data_value(self.additional_data)
    

