from __future__ import annotations
from dataclasses import dataclass, field
from datetime import date, datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, picture, postal_address_type

from . import entity

@dataclass
class Employee(entity.Entity):
    # The address property
    address: Optional[postal_address_type.PostalAddressType] = None
    # The birthDate property
    birth_date: Optional[date] = None
    # The displayName property
    display_name: Optional[str] = None
    # The email property
    email: Optional[str] = None
    # The employmentDate property
    employment_date: Optional[date] = None
    # The givenName property
    given_name: Optional[str] = None
    # The jobTitle property
    job_title: Optional[str] = None
    # The lastModifiedDateTime property
    last_modified_date_time: Optional[datetime] = None
    # The middleName property
    middle_name: Optional[str] = None
    # The mobilePhone property
    mobile_phone: Optional[str] = None
    # The number property
    number: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The personalEmail property
    personal_email: Optional[str] = None
    # The phoneNumber property
    phone_number: Optional[str] = None
    # The picture property
    picture: Optional[List[picture.Picture]] = None
    # The statisticsGroupCode property
    statistics_group_code: Optional[str] = None
    # The status property
    status: Optional[str] = None
    # The surname property
    surname: Optional[str] = None
    # The terminationDate property
    termination_date: Optional[date] = None
    
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
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, picture, postal_address_type

        fields: Dict[str, Callable[[Any], None]] = {
            "address": lambda n : setattr(self, 'address', n.get_object_value(postal_address_type.PostalAddressType)),
            "birthDate": lambda n : setattr(self, 'birth_date', n.get_date_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "employmentDate": lambda n : setattr(self, 'employment_date', n.get_date_value()),
            "givenName": lambda n : setattr(self, 'given_name', n.get_str_value()),
            "jobTitle": lambda n : setattr(self, 'job_title', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "middleName": lambda n : setattr(self, 'middle_name', n.get_str_value()),
            "mobilePhone": lambda n : setattr(self, 'mobile_phone', n.get_str_value()),
            "number": lambda n : setattr(self, 'number', n.get_str_value()),
            "personalEmail": lambda n : setattr(self, 'personal_email', n.get_str_value()),
            "phoneNumber": lambda n : setattr(self, 'phone_number', n.get_str_value()),
            "picture": lambda n : setattr(self, 'picture', n.get_collection_of_object_values(picture.Picture)),
            "statisticsGroupCode": lambda n : setattr(self, 'statistics_group_code', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
            "surname": lambda n : setattr(self, 'surname', n.get_str_value()),
            "terminationDate": lambda n : setattr(self, 'termination_date', n.get_date_value()),
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
        writer.write_object_value("address", self.address)
        writer.write_date_value("birthDate", self.birth_date)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("email", self.email)
        writer.write_date_value("employmentDate", self.employment_date)
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
        writer.write_date_value("terminationDate", self.termination_date)
    

