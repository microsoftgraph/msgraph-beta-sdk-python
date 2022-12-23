from __future__ import annotations
from datetime import date, datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
picture = lazy_import('msgraph.generated.models.picture')
postal_address_type = lazy_import('msgraph.generated.models.postal_address_type')

class Employee(entity.Entity):
    """
    Provides operations to manage the collection of accessReview entities.
    """
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
    
    @property
    def birth_date(self,) -> Optional[Date]:
        """
        Gets the birthDate property value. The birthDate property
        Returns: Optional[Date]
        """
        return self._birth_date
    
    @birth_date.setter
    def birth_date(self,value: Optional[Date] = None) -> None:
        """
        Sets the birthDate property value. The birthDate property
        Args:
            value: Value to set for the birthDate property.
        """
        self._birth_date = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new employee and sets the default values.
        """
        super().__init__()
        # The address property
        self._address: Optional[postal_address_type.PostalAddressType] = None
        # The birthDate property
        self._birth_date: Optional[Date] = None
        # The displayName property
        self._display_name: Optional[str] = None
        # The email property
        self._email: Optional[str] = None
        # The employmentDate property
        self._employment_date: Optional[Date] = None
        # The givenName property
        self._given_name: Optional[str] = None
        # The jobTitle property
        self._job_title: Optional[str] = None
        # The lastModifiedDateTime property
        self._last_modified_date_time: Optional[datetime] = None
        # The middleName property
        self._middle_name: Optional[str] = None
        # The mobilePhone property
        self._mobile_phone: Optional[str] = None
        # The number property
        self._number: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The personalEmail property
        self._personal_email: Optional[str] = None
        # The phoneNumber property
        self._phone_number: Optional[str] = None
        # The picture property
        self._picture: Optional[List[picture.Picture]] = None
        # The statisticsGroupCode property
        self._statistics_group_code: Optional[str] = None
        # The status property
        self._status: Optional[str] = None
        # The surname property
        self._surname: Optional[str] = None
        # The terminationDate property
        self._termination_date: Optional[Date] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Employee:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Employee
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Employee()
    
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
    def employment_date(self,) -> Optional[Date]:
        """
        Gets the employmentDate property value. The employmentDate property
        Returns: Optional[Date]
        """
        return self._employment_date
    
    @employment_date.setter
    def employment_date(self,value: Optional[Date] = None) -> None:
        """
        Sets the employmentDate property value. The employmentDate property
        Args:
            value: Value to set for the employmentDate property.
        """
        self._employment_date = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "address": lambda n : setattr(self, 'address', n.get_object_value(postal_address_type.PostalAddressType)),
            "birth_date": lambda n : setattr(self, 'birth_date', n.get_object_value(Date)),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "employment_date": lambda n : setattr(self, 'employment_date', n.get_object_value(Date)),
            "given_name": lambda n : setattr(self, 'given_name', n.get_str_value()),
            "job_title": lambda n : setattr(self, 'job_title', n.get_str_value()),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "middle_name": lambda n : setattr(self, 'middle_name', n.get_str_value()),
            "mobile_phone": lambda n : setattr(self, 'mobile_phone', n.get_str_value()),
            "number": lambda n : setattr(self, 'number', n.get_str_value()),
            "personal_email": lambda n : setattr(self, 'personal_email', n.get_str_value()),
            "phone_number": lambda n : setattr(self, 'phone_number', n.get_str_value()),
            "picture": lambda n : setattr(self, 'picture', n.get_collection_of_object_values(picture.Picture)),
            "statistics_group_code": lambda n : setattr(self, 'statistics_group_code', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
            "surname": lambda n : setattr(self, 'surname', n.get_str_value()),
            "termination_date": lambda n : setattr(self, 'termination_date', n.get_object_value(Date)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def given_name(self,) -> Optional[str]:
        """
        Gets the givenName property value. The givenName property
        Returns: Optional[str]
        """
        return self._given_name
    
    @given_name.setter
    def given_name(self,value: Optional[str] = None) -> None:
        """
        Sets the givenName property value. The givenName property
        Args:
            value: Value to set for the givenName property.
        """
        self._given_name = value
    
    @property
    def job_title(self,) -> Optional[str]:
        """
        Gets the jobTitle property value. The jobTitle property
        Returns: Optional[str]
        """
        return self._job_title
    
    @job_title.setter
    def job_title(self,value: Optional[str] = None) -> None:
        """
        Sets the jobTitle property value. The jobTitle property
        Args:
            value: Value to set for the jobTitle property.
        """
        self._job_title = value
    
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
    
    @property
    def middle_name(self,) -> Optional[str]:
        """
        Gets the middleName property value. The middleName property
        Returns: Optional[str]
        """
        return self._middle_name
    
    @middle_name.setter
    def middle_name(self,value: Optional[str] = None) -> None:
        """
        Sets the middleName property value. The middleName property
        Args:
            value: Value to set for the middleName property.
        """
        self._middle_name = value
    
    @property
    def mobile_phone(self,) -> Optional[str]:
        """
        Gets the mobilePhone property value. The mobilePhone property
        Returns: Optional[str]
        """
        return self._mobile_phone
    
    @mobile_phone.setter
    def mobile_phone(self,value: Optional[str] = None) -> None:
        """
        Sets the mobilePhone property value. The mobilePhone property
        Args:
            value: Value to set for the mobilePhone property.
        """
        self._mobile_phone = value
    
    @property
    def number(self,) -> Optional[str]:
        """
        Gets the number property value. The number property
        Returns: Optional[str]
        """
        return self._number
    
    @number.setter
    def number(self,value: Optional[str] = None) -> None:
        """
        Sets the number property value. The number property
        Args:
            value: Value to set for the number property.
        """
        self._number = value
    
    @property
    def personal_email(self,) -> Optional[str]:
        """
        Gets the personalEmail property value. The personalEmail property
        Returns: Optional[str]
        """
        return self._personal_email
    
    @personal_email.setter
    def personal_email(self,value: Optional[str] = None) -> None:
        """
        Sets the personalEmail property value. The personalEmail property
        Args:
            value: Value to set for the personalEmail property.
        """
        self._personal_email = value
    
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
            value: Value to set for the phoneNumber property.
        """
        self._phone_number = value
    
    @property
    def picture(self,) -> Optional[List[picture.Picture]]:
        """
        Gets the picture property value. The picture property
        Returns: Optional[List[picture.Picture]]
        """
        return self._picture
    
    @picture.setter
    def picture(self,value: Optional[List[picture.Picture]] = None) -> None:
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
        writer.write_object_value("birthDate", self.birth_date)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("email", self.email)
        writer.write_object_value("employmentDate", self.employment_date)
        writer.write_str_value("givenName", self.given_name)
        writer.write_str_value("jobTitle", self.job_title)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("middleName", self.middle_name)
        writer.write_str_value("mobilePhone", self.mobile_phone)
        writer.write_str_value("number", self.number)
        writer.write_str_value("personalEmail", self.personal_email)
        writer.write_str_value("phoneNumber", self.phone_number)
        writer.write_collection_of_object_values("picture", self.picture)
        writer.write_str_value("statisticsGroupCode", self.statistics_group_code)
        writer.write_str_value("status", self.status)
        writer.write_str_value("surname", self.surname)
        writer.write_object_value("terminationDate", self.termination_date)
    
    @property
    def statistics_group_code(self,) -> Optional[str]:
        """
        Gets the statisticsGroupCode property value. The statisticsGroupCode property
        Returns: Optional[str]
        """
        return self._statistics_group_code
    
    @statistics_group_code.setter
    def statistics_group_code(self,value: Optional[str] = None) -> None:
        """
        Sets the statisticsGroupCode property value. The statisticsGroupCode property
        Args:
            value: Value to set for the statisticsGroupCode property.
        """
        self._statistics_group_code = value
    
    @property
    def status(self,) -> Optional[str]:
        """
        Gets the status property value. The status property
        Returns: Optional[str]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[str] = None) -> None:
        """
        Sets the status property value. The status property
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    
    @property
    def surname(self,) -> Optional[str]:
        """
        Gets the surname property value. The surname property
        Returns: Optional[str]
        """
        return self._surname
    
    @surname.setter
    def surname(self,value: Optional[str] = None) -> None:
        """
        Sets the surname property value. The surname property
        Args:
            value: Value to set for the surname property.
        """
        self._surname = value
    
    @property
    def termination_date(self,) -> Optional[Date]:
        """
        Gets the terminationDate property value. The terminationDate property
        Returns: Optional[Date]
        """
        return self._termination_date
    
    @termination_date.setter
    def termination_date(self,value: Optional[Date] = None) -> None:
        """
        Sets the terminationDate property value. The terminationDate property
        Args:
            value: Value to set for the terminationDate property.
        """
        self._termination_date = value
    

