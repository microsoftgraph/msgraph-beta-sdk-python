from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class IpReferenceData(AdditionalDataHolder, Parsable):
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
    def asn(self,) -> Optional[int]:
        """
        Gets the asn property value. The asn property
        Returns: Optional[int]
        """
        return self._asn
    
    @asn.setter
    def asn(self,value: Optional[int] = None) -> None:
        """
        Sets the asn property value. The asn property
        Args:
            value: Value to set for the asn property.
        """
        self._asn = value
    
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
        Instantiates a new ipReferenceData and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The asn property
        self._asn: Optional[int] = None
        # The city property
        self._city: Optional[str] = None
        # The countryOrRegionCode property
        self._country_or_region_code: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The organization property
        self._organization: Optional[str] = None
        # The state property
        self._state: Optional[str] = None
        # The vendor property
        self._vendor: Optional[str] = None
    
    @property
    def country_or_region_code(self,) -> Optional[str]:
        """
        Gets the countryOrRegionCode property value. The countryOrRegionCode property
        Returns: Optional[str]
        """
        return self._country_or_region_code
    
    @country_or_region_code.setter
    def country_or_region_code(self,value: Optional[str] = None) -> None:
        """
        Sets the countryOrRegionCode property value. The countryOrRegionCode property
        Args:
            value: Value to set for the countryOrRegionCode property.
        """
        self._country_or_region_code = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IpReferenceData:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IpReferenceData
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return IpReferenceData()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "asn": lambda n : setattr(self, 'asn', n.get_int_value()),
            "city": lambda n : setattr(self, 'city', n.get_str_value()),
            "country_or_region_code": lambda n : setattr(self, 'country_or_region_code', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "organization": lambda n : setattr(self, 'organization', n.get_str_value()),
            "state": lambda n : setattr(self, 'state', n.get_str_value()),
            "vendor": lambda n : setattr(self, 'vendor', n.get_str_value()),
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
    def organization(self,) -> Optional[str]:
        """
        Gets the organization property value. The organization property
        Returns: Optional[str]
        """
        return self._organization
    
    @organization.setter
    def organization(self,value: Optional[str] = None) -> None:
        """
        Sets the organization property value. The organization property
        Args:
            value: Value to set for the organization property.
        """
        self._organization = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_int_value("asn", self.asn)
        writer.write_str_value("city", self.city)
        writer.write_str_value("countryOrRegionCode", self.country_or_region_code)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("organization", self.organization)
        writer.write_str_value("state", self.state)
        writer.write_str_value("vendor", self.vendor)
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
    def vendor(self,) -> Optional[str]:
        """
        Gets the vendor property value. The vendor property
        Returns: Optional[str]
        """
        return self._vendor
    
    @vendor.setter
    def vendor(self,value: Optional[str] = None) -> None:
        """
        Sets the vendor property value. The vendor property
        Args:
            value: Value to set for the vendor property.
        """
        self._vendor = value
    

