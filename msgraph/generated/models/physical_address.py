from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

physical_address_type = lazy_import('msgraph.generated.models.physical_address_type')

class PhysicalAddress(AdditionalDataHolder, Parsable):
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
        Gets the city property value. The city.
        Returns: Optional[str]
        """
        return self._city
    
    @city.setter
    def city(self,value: Optional[str] = None) -> None:
        """
        Sets the city property value. The city.
        Args:
            value: Value to set for the city property.
        """
        self._city = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new physicalAddress and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The city.
        self._city: Optional[str] = None
        # The country or region. It's a free-format string value, for example, 'United States'.
        self._country_or_region: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The postal code.
        self._postal_code: Optional[str] = None
        # The post office box number.
        self._post_office_box: Optional[str] = None
        # The state.
        self._state: Optional[str] = None
        # The street.
        self._street: Optional[str] = None
        # The type of address. Possible values are: unknown, home, business, other.
        self._type: Optional[physical_address_type.PhysicalAddressType] = None
    
    @property
    def country_or_region(self,) -> Optional[str]:
        """
        Gets the countryOrRegion property value. The country or region. It's a free-format string value, for example, 'United States'.
        Returns: Optional[str]
        """
        return self._country_or_region
    
    @country_or_region.setter
    def country_or_region(self,value: Optional[str] = None) -> None:
        """
        Sets the countryOrRegion property value. The country or region. It's a free-format string value, for example, 'United States'.
        Args:
            value: Value to set for the countryOrRegion property.
        """
        self._country_or_region = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PhysicalAddress:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PhysicalAddress
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PhysicalAddress()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "city": lambda n : setattr(self, 'city', n.get_str_value()),
            "country_or_region": lambda n : setattr(self, 'country_or_region', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "postal_code": lambda n : setattr(self, 'postal_code', n.get_str_value()),
            "post_office_box": lambda n : setattr(self, 'post_office_box', n.get_str_value()),
            "state": lambda n : setattr(self, 'state', n.get_str_value()),
            "street": lambda n : setattr(self, 'street', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(physical_address_type.PhysicalAddressType)),
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
        Gets the postalCode property value. The postal code.
        Returns: Optional[str]
        """
        return self._postal_code
    
    @postal_code.setter
    def postal_code(self,value: Optional[str] = None) -> None:
        """
        Sets the postalCode property value. The postal code.
        Args:
            value: Value to set for the postalCode property.
        """
        self._postal_code = value
    
    @property
    def post_office_box(self,) -> Optional[str]:
        """
        Gets the postOfficeBox property value. The post office box number.
        Returns: Optional[str]
        """
        return self._post_office_box
    
    @post_office_box.setter
    def post_office_box(self,value: Optional[str] = None) -> None:
        """
        Sets the postOfficeBox property value. The post office box number.
        Args:
            value: Value to set for the postOfficeBox property.
        """
        self._post_office_box = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("city", self.city)
        writer.write_str_value("countryOrRegion", self.country_or_region)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("postalCode", self.postal_code)
        writer.write_str_value("postOfficeBox", self.post_office_box)
        writer.write_str_value("state", self.state)
        writer.write_str_value("street", self.street)
        writer.write_enum_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def state(self,) -> Optional[str]:
        """
        Gets the state property value. The state.
        Returns: Optional[str]
        """
        return self._state
    
    @state.setter
    def state(self,value: Optional[str] = None) -> None:
        """
        Sets the state property value. The state.
        Args:
            value: Value to set for the state property.
        """
        self._state = value
    
    @property
    def street(self,) -> Optional[str]:
        """
        Gets the street property value. The street.
        Returns: Optional[str]
        """
        return self._street
    
    @street.setter
    def street(self,value: Optional[str] = None) -> None:
        """
        Sets the street property value. The street.
        Args:
            value: Value to set for the street property.
        """
        self._street = value
    
    @property
    def type(self,) -> Optional[physical_address_type.PhysicalAddressType]:
        """
        Gets the type property value. The type of address. Possible values are: unknown, home, business, other.
        Returns: Optional[physical_address_type.PhysicalAddressType]
        """
        return self._type
    
    @type.setter
    def type(self,value: Optional[physical_address_type.PhysicalAddressType] = None) -> None:
        """
        Sets the type property value. The type of address. Possible values are: unknown, home, business, other.
        Args:
            value: Value to set for the type property.
        """
        self._type = value
    

