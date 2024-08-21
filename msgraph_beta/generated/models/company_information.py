from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .postal_address_type import PostalAddressType

@dataclass
class CompanyInformation(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The address property
    address: Optional[PostalAddressType] = None
    # The currencyCode property
    currency_code: Optional[str] = None
    # The currentFiscalYearStartDate property
    current_fiscal_year_start_date: Optional[datetime.date] = None
    # The displayName property
    display_name: Optional[str] = None
    # The email property
    email: Optional[str] = None
    # The faxNumber property
    fax_number: Optional[str] = None
    # The id property
    id: Optional[UUID] = None
    # The industry property
    industry: Optional[str] = None
    # The lastModifiedDateTime property
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The phoneNumber property
    phone_number: Optional[str] = None
    # The picture property
    picture: Optional[bytes] = None
    # The taxRegistrationNumber property
    tax_registration_number: Optional[str] = None
    # The website property
    website: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CompanyInformation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CompanyInformation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CompanyInformation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .postal_address_type import PostalAddressType

        from .postal_address_type import PostalAddressType

        fields: Dict[str, Callable[[Any], None]] = {
            "address": lambda n : setattr(self, 'address', n.get_object_value(PostalAddressType)),
            "currencyCode": lambda n : setattr(self, 'currency_code', n.get_str_value()),
            "currentFiscalYearStartDate": lambda n : setattr(self, 'current_fiscal_year_start_date', n.get_date_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "faxNumber": lambda n : setattr(self, 'fax_number', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_uuid_value()),
            "industry": lambda n : setattr(self, 'industry', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "phoneNumber": lambda n : setattr(self, 'phone_number', n.get_str_value()),
            "picture": lambda n : setattr(self, 'picture', n.get_bytes_value()),
            "taxRegistrationNumber": lambda n : setattr(self, 'tax_registration_number', n.get_str_value()),
            "website": lambda n : setattr(self, 'website', n.get_str_value()),
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
        writer.write_str_value("currencyCode", self.currency_code)
        writer.write_date_value("currentFiscalYearStartDate", self.current_fiscal_year_start_date)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("email", self.email)
        writer.write_str_value("faxNumber", self.fax_number)
        writer.write_uuid_value("id", self.id)
        writer.write_str_value("industry", self.industry)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("phoneNumber", self.phone_number)
        writer.write_bytes_value("picture", self.picture)
        writer.write_str_value("taxRegistrationNumber", self.tax_registration_number)
        writer.write_str_value("website", self.website)
        writer.write_additional_data_value(self.additional_data)
    

