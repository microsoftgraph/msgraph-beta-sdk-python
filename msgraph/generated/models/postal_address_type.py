from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class PostalAddressType(AdditionalDataHolder, Parsable):
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
    def city(self,) -> Optional[str]:
        """
        Gets the city property value. The city property
        Returns: Optional[str]
        """
        return self._city
    
    @city.setter
    def city(self,value: Optional[str] = None) -> None:
        """
        Sets the city property value. The city property
        Args:
            value: Value to set for the city property.
        """
        self._city = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new postalAddressType and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The city property
        self._city: Optional[str] = None
        # The countryLetterCode property
        self._country_letter_code: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The postalCode property
        self._postal_code: Optional[str] = None
        # The state property
        self._state: Optional[str] = None
        # The street property
        self._street: Optional[str] = None
    
    @property
    def country_letter_code(self,) -> Optional[str]:
        """
        Gets the countryLetterCode property value. The countryLetterCode property
        Returns: Optional[str]
        """
        return self._country_letter_code
    
    @country_letter_code.setter
    def country_letter_code(self,value: Optional[str] = None) -> None:
        """
        Sets the countryLetterCode property value. The countryLetterCode property
        Args:
            value: Value to set for the countryLetterCode property.
        """
        self._country_letter_code = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PostalAddressType:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PostalAddressType
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PostalAddressType()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "city": lambda n : setattr(self, 'city', n.get_str_value()),
            "country_letter_code": lambda n : setattr(self, 'country_letter_code', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "postal_code": lambda n : setattr(self, 'postal_code', n.get_str_value()),
            "state": lambda n : setattr(self, 'state', n.get_str_value()),
            "street": lambda n : setattr(self, 'street', n.get_str_value()),
        }
        return fields
    
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
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def postal_code(self,) -> Optional[str]:
        """
        Gets the postalCode property value. The postalCode property
        Returns: Optional[str]
        """
        return self._postal_code
    
    @postal_code.setter
    def postal_code(self,value: Optional[str] = None) -> None:
        """
        Sets the postalCode property value. The postalCode property
        Args:
            value: Value to set for the postalCode property.
        """
        self._postal_code = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("city", self.city)
        writer.write_str_value("countryLetterCode", self.country_letter_code)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("postalCode", self.postal_code)
        writer.write_str_value("state", self.state)
        writer.write_str_value("street", self.street)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def state(self,) -> Optional[str]:
        """
        Gets the state property value. The state property
        Returns: Optional[str]
        """
        return self._state
    
    @state.setter
    def state(self,value: Optional[str] = None) -> None:
        """
        Sets the state property value. The state property
        Args:
            value: Value to set for the state property.
        """
        self._state = value
    
    @property
    def street(self,) -> Optional[str]:
        """
        Gets the street property value. The street property
        Returns: Optional[str]
        """
        return self._street
    
    @street.setter
    def street(self,value: Optional[str] = None) -> None:
        """
        Sets the street property value. The street property
        Args:
            value: Value to set for the street property.
        """
        self._street = value
    

