from __future__ import annotations
from datetime import date, datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, postal_address_type

from . import entity

class CompanyInformation(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new companyInformation and sets the default values.
        """
        super().__init__()
        # The address property
        self._address: Optional[postal_address_type.PostalAddressType] = None
        # The currencyCode property
        self._currency_code: Optional[str] = None
        # The currentFiscalYearStartDate property
        self._current_fiscal_year_start_date: Optional[date] = None
        # The displayName property
        self._display_name: Optional[str] = None
        # The email property
        self._email: Optional[str] = None
        # The faxNumber property
        self._fax_number: Optional[str] = None
        # The industry property
        self._industry: Optional[str] = None
        # The lastModifiedDateTime property
        self._last_modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The phoneNumber property
        self._phone_number: Optional[str] = None
        # The picture property
        self._picture: Optional[bytes] = None
        # The taxRegistrationNumber property
        self._tax_registration_number: Optional[str] = None
        # The website property
        self._website: Optional[str] = None
    
    @property
    def address(self,) -> Optional[postal_address_type.PostalAddressType]:
        """
        Gets the address property value. The address property
        Returns: Optional[postal_address_type.PostalAddressType]
        """
        return self._address
    
    @address.setter
    def address(self,value: Optional[postal_address_type.PostalAddressType] = None) -> None:
        """
        Sets the address property value. The address property
        Args:
            value: Value to set for the address property.
        """
        self._address = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CompanyInformation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CompanyInformation
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CompanyInformation()
    
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
            value: Value to set for the currency_code property.
        """
        self._currency_code = value
    
    @property
    def current_fiscal_year_start_date(self,) -> Optional[date]:
        """
        Gets the currentFiscalYearStartDate property value. The currentFiscalYearStartDate property
        Returns: Optional[date]
        """
        return self._current_fiscal_year_start_date
    
    @current_fiscal_year_start_date.setter
    def current_fiscal_year_start_date(self,value: Optional[date] = None) -> None:
        """
        Sets the currentFiscalYearStartDate property value. The currentFiscalYearStartDate property
        Args:
            value: Value to set for the current_fiscal_year_start_date property.
        """
        self._current_fiscal_year_start_date = value
    
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
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    @property
    def email(self,) -> Optional[str]:
        """
        Gets the email property value. The email property
        Returns: Optional[str]
        """
        return self._email
    
    @email.setter
    def email(self,value: Optional[str] = None) -> None:
        """
        Sets the email property value. The email property
        Args:
            value: Value to set for the email property.
        """
        self._email = value
    
    @property
    def fax_number(self,) -> Optional[str]:
        """
        Gets the faxNumber property value. The faxNumber property
        Returns: Optional[str]
        """
        return self._fax_number
    
    @fax_number.setter
    def fax_number(self,value: Optional[str] = None) -> None:
        """
        Sets the faxNumber property value. The faxNumber property
        Args:
            value: Value to set for the fax_number property.
        """
        self._fax_number = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, postal_address_type

        fields: Dict[str, Callable[[Any], None]] = {
            "address": lambda n : setattr(self, 'address', n.get_object_value(postal_address_type.PostalAddressType)),
            "currencyCode": lambda n : setattr(self, 'currency_code', n.get_str_value()),
            "currentFiscalYearStartDate": lambda n : setattr(self, 'current_fiscal_year_start_date', n.get_date_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "faxNumber": lambda n : setattr(self, 'fax_number', n.get_str_value()),
            "industry": lambda n : setattr(self, 'industry', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "phoneNumber": lambda n : setattr(self, 'phone_number', n.get_str_value()),
            "picture": lambda n : setattr(self, 'picture', n.get_bytes_value()),
            "taxRegistrationNumber": lambda n : setattr(self, 'tax_registration_number', n.get_str_value()),
            "website": lambda n : setattr(self, 'website', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def industry(self,) -> Optional[str]:
        """
        Gets the industry property value. The industry property
        Returns: Optional[str]
        """
        return self._industry
    
    @industry.setter
    def industry(self,value: Optional[str] = None) -> None:
        """
        Sets the industry property value. The industry property
        Args:
            value: Value to set for the industry property.
        """
        self._industry = value
    
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
            value: Value to set for the last_modified_date_time property.
        """
        self._last_modified_date_time = value
    
    @property
    def phone_number(self,) -> Optional[str]:
        """
        Gets the phoneNumber property value. The phoneNumber property
        Returns: Optional[str]
        """
        return self._phone_number
    
    @phone_number.setter
    def phone_number(self,value: Optional[str] = None) -> None:
        """
        Sets the phoneNumber property value. The phoneNumber property
        Args:
            value: Value to set for the phone_number property.
        """
        self._phone_number = value
    
    @property
    def picture(self,) -> Optional[bytes]:
        """
        Gets the picture property value. The picture property
        Returns: Optional[bytes]
        """
        return self._picture
    
    @picture.setter
    def picture(self,value: Optional[bytes] = None) -> None:
        """
        Sets the picture property value. The picture property
        Args:
            value: Value to set for the picture property.
        """
        self._picture = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("address", self.address)
        writer.write_str_value("currencyCode", self.currency_code)
        writer.write_date_value("currentFiscalYearStartDate", self.current_fiscal_year_start_date)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("email", self.email)
        writer.write_str_value("faxNumber", self.fax_number)
        writer.write_str_value("industry", self.industry)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("phoneNumber", self.phone_number)
        writer.write_object_value("picture", self.picture)
        writer.write_str_value("taxRegistrationNumber", self.tax_registration_number)
        writer.write_str_value("website", self.website)
    
    @property
    def tax_registration_number(self,) -> Optional[str]:
        """
        Gets the taxRegistrationNumber property value. The taxRegistrationNumber property
        Returns: Optional[str]
        """
        return self._tax_registration_number
    
    @tax_registration_number.setter
    def tax_registration_number(self,value: Optional[str] = None) -> None:
        """
        Sets the taxRegistrationNumber property value. The taxRegistrationNumber property
        Args:
            value: Value to set for the tax_registration_number property.
        """
        self._tax_registration_number = value
    
    @property
    def website(self,) -> Optional[str]:
        """
        Gets the website property value. The website property
        Returns: Optional[str]
        """
        return self._website
    
    @website.setter
    def website(self,value: Optional[str] = None) -> None:
        """
        Sets the website property value. The website property
        Args:
            value: Value to set for the website property.
        """
        self._website = value
    

