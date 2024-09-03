from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .picture import Picture
    from .postal_address_type import PostalAddressType

@dataclass
class Employee(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The address property
    address: Optional[PostalAddressType] = None
    # The birthDate property
    birth_date: Optional[datetime.date] = None
    # The displayName property
    display_name: Optional[str] = None
    # The email property
    email: Optional[str] = None
    # The employmentDate property
    employment_date: Optional[datetime.date] = None
    # The givenName property
    given_name: Optional[str] = None
    # The id property
    id: Optional[UUID] = None
    # The jobTitle property
    job_title: Optional[str] = None
    # The lastModifiedDateTime property
    last_modified_date_time: Optional[datetime.datetime] = None
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
    picture: Optional[List[Picture]] = None
    # The statisticsGroupCode property
    statistics_group_code: Optional[str] = None
    # The status property
    status: Optional[str] = None
    # The surname property
    surname: Optional[str] = None
    # The terminationDate property
    termination_date: Optional[datetime.date] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Employee:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Employee
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Employee()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .picture import Picture
        from .postal_address_type import PostalAddressType

        from .picture import Picture
        from .postal_address_type import PostalAddressType

        fields: Dict[str, Callable[[Any], None]] = {
            "address": lambda n : setattr(self, 'address', n.get_object_value(PostalAddressType)),
            "birthDate": lambda n : setattr(self, 'birth_date', n.get_date_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "employmentDate": lambda n : setattr(self, 'employment_date', n.get_date_value()),
            "givenName": lambda n : setattr(self, 'given_name', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_uuid_value()),
            "jobTitle": lambda n : setattr(self, 'job_title', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "middleName": lambda n : setattr(self, 'middle_name', n.get_str_value()),
            "mobilePhone": lambda n : setattr(self, 'mobile_phone', n.get_str_value()),
            "number": lambda n : setattr(self, 'number', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "personalEmail": lambda n : setattr(self, 'personal_email', n.get_str_value()),
            "phoneNumber": lambda n : setattr(self, 'phone_number', n.get_str_value()),
            "picture": lambda n : setattr(self, 'picture', n.get_collection_of_object_values(Picture)),
            "statisticsGroupCode": lambda n : setattr(self, 'statistics_group_code', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
            "surname": lambda n : setattr(self, 'surname', n.get_str_value()),
            "terminationDate": lambda n : setattr(self, 'termination_date', n.get_date_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_object_value("address", self.address)
        writer.write_date_value("birthDate", self.birth_date)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("email", self.email)
        writer.write_date_value("employmentDate", self.employment_date)
        writer.write_str_value("givenName", self.given_name)
        writer.write_uuid_value("id", self.id)
        writer.write_str_value("jobTitle", self.job_title)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("middleName", self.middle_name)
        writer.write_str_value("mobilePhone", self.mobile_phone)
        writer.write_str_value("number", self.number)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("personalEmail", self.personal_email)
        writer.write_str_value("phoneNumber", self.phone_number)
        writer.write_collection_of_object_values("picture", self.picture)
        writer.write_str_value("statisticsGroupCode", self.statistics_group_code)
        writer.write_str_value("status", self.status)
        writer.write_str_value("surname", self.surname)
        writer.write_date_value("terminationDate", self.termination_date)
        writer.write_additional_data_value(self.additional_data)
    

