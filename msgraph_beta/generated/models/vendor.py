from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .currency import Currency
    from .payment_method import PaymentMethod
    from .payment_term import PaymentTerm
    from .picture import Picture
    from .postal_address_type import PostalAddressType

@dataclass
class Vendor(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The address property
    address: Optional[PostalAddressType] = None
    # The balance property
    balance: Optional[float] = None
    # The blocked property
    blocked: Optional[str] = None
    # The currency property
    currency: Optional[Currency] = None
    # The currencyCode property
    currency_code: Optional[str] = None
    # The currencyId property
    currency_id: Optional[UUID] = None
    # The displayName property
    display_name: Optional[str] = None
    # The email property
    email: Optional[str] = None
    # The id property
    id: Optional[UUID] = None
    # The lastModifiedDateTime property
    last_modified_date_time: Optional[datetime.datetime] = None
    # The number property
    number: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The paymentMethod property
    payment_method: Optional[PaymentMethod] = None
    # The paymentMethodId property
    payment_method_id: Optional[UUID] = None
    # The paymentTerm property
    payment_term: Optional[PaymentTerm] = None
    # The paymentTermsId property
    payment_terms_id: Optional[UUID] = None
    # The phoneNumber property
    phone_number: Optional[str] = None
    # The picture property
    picture: Optional[List[Picture]] = None
    # The taxLiable property
    tax_liable: Optional[bool] = None
    # The taxRegistrationNumber property
    tax_registration_number: Optional[str] = None
    # The website property
    website: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Vendor:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Vendor
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Vendor()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .currency import Currency
        from .payment_method import PaymentMethod
        from .payment_term import PaymentTerm
        from .picture import Picture
        from .postal_address_type import PostalAddressType

        from .currency import Currency
        from .payment_method import PaymentMethod
        from .payment_term import PaymentTerm
        from .picture import Picture
        from .postal_address_type import PostalAddressType

        fields: Dict[str, Callable[[Any], None]] = {
            "address": lambda n : setattr(self, 'address', n.get_object_value(PostalAddressType)),
            "balance": lambda n : setattr(self, 'balance', n.get_float_value()),
            "blocked": lambda n : setattr(self, 'blocked', n.get_str_value()),
            "currency": lambda n : setattr(self, 'currency', n.get_object_value(Currency)),
            "currencyCode": lambda n : setattr(self, 'currency_code', n.get_str_value()),
            "currencyId": lambda n : setattr(self, 'currency_id', n.get_uuid_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_uuid_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "number": lambda n : setattr(self, 'number', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "paymentMethod": lambda n : setattr(self, 'payment_method', n.get_object_value(PaymentMethod)),
            "paymentMethodId": lambda n : setattr(self, 'payment_method_id', n.get_uuid_value()),
            "paymentTerm": lambda n : setattr(self, 'payment_term', n.get_object_value(PaymentTerm)),
            "paymentTermsId": lambda n : setattr(self, 'payment_terms_id', n.get_uuid_value()),
            "phoneNumber": lambda n : setattr(self, 'phone_number', n.get_str_value()),
            "picture": lambda n : setattr(self, 'picture', n.get_collection_of_object_values(Picture)),
            "taxLiable": lambda n : setattr(self, 'tax_liable', n.get_bool_value()),
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
        writer.write_float_value("balance", self.balance)
        writer.write_str_value("blocked", self.blocked)
        writer.write_object_value("currency", self.currency)
        writer.write_str_value("currencyCode", self.currency_code)
        writer.write_uuid_value("currencyId", self.currency_id)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("email", self.email)
        writer.write_uuid_value("id", self.id)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("number", self.number)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("paymentMethod", self.payment_method)
        writer.write_uuid_value("paymentMethodId", self.payment_method_id)
        writer.write_object_value("paymentTerm", self.payment_term)
        writer.write_uuid_value("paymentTermsId", self.payment_terms_id)
        writer.write_str_value("phoneNumber", self.phone_number)
        writer.write_collection_of_object_values("picture", self.picture)
        writer.write_bool_value("taxLiable", self.tax_liable)
        writer.write_str_value("taxRegistrationNumber", self.tax_registration_number)
        writer.write_str_value("website", self.website)
        writer.write_additional_data_value(self.additional_data)
    

