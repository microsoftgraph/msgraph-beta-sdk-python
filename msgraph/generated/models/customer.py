from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

currency = lazy_import('msgraph.generated.models.currency')
entity = lazy_import('msgraph.generated.models.entity')
payment_method = lazy_import('msgraph.generated.models.payment_method')
payment_term = lazy_import('msgraph.generated.models.payment_term')
picture = lazy_import('msgraph.generated.models.picture')
postal_address_type = lazy_import('msgraph.generated.models.postal_address_type')
shipment_method = lazy_import('msgraph.generated.models.shipment_method')

class Customer(entity.Entity):
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
    def blocked(self,) -> Optional[str]:
        """
        Gets the blocked property value. The blocked property
        Returns: Optional[str]
        """
        return self._blocked
    
    @blocked.setter
    def blocked(self,value: Optional[str] = None) -> None:
        """
        Sets the blocked property value. The blocked property
        Args:
            value: Value to set for the blocked property.
        """
        self._blocked = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new customer and sets the default values.
        """
        super().__init__()
        # The address property
        self._address: Optional[postal_address_type.PostalAddressType] = None
        # The blocked property
        self._blocked: Optional[str] = None
        # The currency property
        self._currency: Optional[currency.Currency] = None
        # The currencyCode property
        self._currency_code: Optional[str] = None
        # The currencyId property
        self._currency_id: Optional[Guid] = None
        # The displayName property
        self._display_name: Optional[str] = None
        # The email property
        self._email: Optional[str] = None
        # The lastModifiedDateTime property
        self._last_modified_date_time: Optional[datetime] = None
        # The number property
        self._number: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The paymentMethod property
        self._payment_method: Optional[payment_method.PaymentMethod] = None
        # The paymentMethodId property
        self._payment_method_id: Optional[Guid] = None
        # The paymentTerm property
        self._payment_term: Optional[payment_term.PaymentTerm] = None
        # The paymentTermsId property
        self._payment_terms_id: Optional[Guid] = None
        # The phoneNumber property
        self._phone_number: Optional[str] = None
        # The picture property
        self._picture: Optional[List[picture.Picture]] = None
        # The shipmentMethod property
        self._shipment_method: Optional[shipment_method.ShipmentMethod] = None
        # The shipmentMethodId property
        self._shipment_method_id: Optional[Guid] = None
        # The taxAreaDisplayName property
        self._tax_area_display_name: Optional[str] = None
        # The taxAreaId property
        self._tax_area_id: Optional[Guid] = None
        # The taxLiable property
        self._tax_liable: Optional[bool] = None
        # The taxRegistrationNumber property
        self._tax_registration_number: Optional[str] = None
        # The type property
        self._type: Optional[str] = None
        # The website property
        self._website: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Customer:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Customer
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Customer()
    
    @property
    def currency(self,) -> Optional[currency.Currency]:
        """
        Gets the currency property value. The currency property
        Returns: Optional[currency.Currency]
        """
        return self._currency
    
    @currency.setter
    def currency(self,value: Optional[currency.Currency] = None) -> None:
        """
        Sets the currency property value. The currency property
        Args:
            value: Value to set for the currency property.
        """
        self._currency = value
    
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
            value: Value to set for the currencyCode property.
        """
        self._currency_code = value
    
    @property
    def currency_id(self,) -> Optional[Guid]:
        """
        Gets the currencyId property value. The currencyId property
        Returns: Optional[Guid]
        """
        return self._currency_id
    
    @currency_id.setter
    def currency_id(self,value: Optional[Guid] = None) -> None:
        """
        Sets the currencyId property value. The currencyId property
        Args:
            value: Value to set for the currencyId property.
        """
        self._currency_id = value
    
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
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "address": lambda n : setattr(self, 'address', n.get_object_value(postal_address_type.PostalAddressType)),
            "blocked": lambda n : setattr(self, 'blocked', n.get_str_value()),
            "currency": lambda n : setattr(self, 'currency', n.get_object_value(currency.Currency)),
            "currency_code": lambda n : setattr(self, 'currency_code', n.get_str_value()),
            "currency_id": lambda n : setattr(self, 'currency_id', n.get_object_value(Guid)),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "number": lambda n : setattr(self, 'number', n.get_str_value()),
            "payment_method": lambda n : setattr(self, 'payment_method', n.get_object_value(payment_method.PaymentMethod)),
            "payment_method_id": lambda n : setattr(self, 'payment_method_id', n.get_object_value(Guid)),
            "payment_term": lambda n : setattr(self, 'payment_term', n.get_object_value(payment_term.PaymentTerm)),
            "payment_terms_id": lambda n : setattr(self, 'payment_terms_id', n.get_object_value(Guid)),
            "phone_number": lambda n : setattr(self, 'phone_number', n.get_str_value()),
            "picture": lambda n : setattr(self, 'picture', n.get_collection_of_object_values(picture.Picture)),
            "shipment_method": lambda n : setattr(self, 'shipment_method', n.get_object_value(shipment_method.ShipmentMethod)),
            "shipment_method_id": lambda n : setattr(self, 'shipment_method_id', n.get_object_value(Guid)),
            "tax_area_display_name": lambda n : setattr(self, 'tax_area_display_name', n.get_str_value()),
            "tax_area_id": lambda n : setattr(self, 'tax_area_id', n.get_object_value(Guid)),
            "tax_liable": lambda n : setattr(self, 'tax_liable', n.get_bool_value()),
            "tax_registration_number": lambda n : setattr(self, 'tax_registration_number', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
            "website": lambda n : setattr(self, 'website', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
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
    def payment_method(self,) -> Optional[payment_method.PaymentMethod]:
        """
        Gets the paymentMethod property value. The paymentMethod property
        Returns: Optional[payment_method.PaymentMethod]
        """
        return self._payment_method
    
    @payment_method.setter
    def payment_method(self,value: Optional[payment_method.PaymentMethod] = None) -> None:
        """
        Sets the paymentMethod property value. The paymentMethod property
        Args:
            value: Value to set for the paymentMethod property.
        """
        self._payment_method = value
    
    @property
    def payment_method_id(self,) -> Optional[Guid]:
        """
        Gets the paymentMethodId property value. The paymentMethodId property
        Returns: Optional[Guid]
        """
        return self._payment_method_id
    
    @payment_method_id.setter
    def payment_method_id(self,value: Optional[Guid] = None) -> None:
        """
        Sets the paymentMethodId property value. The paymentMethodId property
        Args:
            value: Value to set for the paymentMethodId property.
        """
        self._payment_method_id = value
    
    @property
    def payment_term(self,) -> Optional[payment_term.PaymentTerm]:
        """
        Gets the paymentTerm property value. The paymentTerm property
        Returns: Optional[payment_term.PaymentTerm]
        """
        return self._payment_term
    
    @payment_term.setter
    def payment_term(self,value: Optional[payment_term.PaymentTerm] = None) -> None:
        """
        Sets the paymentTerm property value. The paymentTerm property
        Args:
            value: Value to set for the paymentTerm property.
        """
        self._payment_term = value
    
    @property
    def payment_terms_id(self,) -> Optional[Guid]:
        """
        Gets the paymentTermsId property value. The paymentTermsId property
        Returns: Optional[Guid]
        """
        return self._payment_terms_id
    
    @payment_terms_id.setter
    def payment_terms_id(self,value: Optional[Guid] = None) -> None:
        """
        Sets the paymentTermsId property value. The paymentTermsId property
        Args:
            value: Value to set for the paymentTermsId property.
        """
        self._payment_terms_id = value
    
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
        writer.write_str_value("blocked", self.blocked)
        writer.write_object_value("currency", self.currency)
        writer.write_str_value("currencyCode", self.currency_code)
        writer.write_object_value("currencyId", self.currency_id)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("email", self.email)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("number", self.number)
        writer.write_object_value("paymentMethod", self.payment_method)
        writer.write_object_value("paymentMethodId", self.payment_method_id)
        writer.write_object_value("paymentTerm", self.payment_term)
        writer.write_object_value("paymentTermsId", self.payment_terms_id)
        writer.write_str_value("phoneNumber", self.phone_number)
        writer.write_collection_of_object_values("picture", self.picture)
        writer.write_object_value("shipmentMethod", self.shipment_method)
        writer.write_object_value("shipmentMethodId", self.shipment_method_id)
        writer.write_str_value("taxAreaDisplayName", self.tax_area_display_name)
        writer.write_object_value("taxAreaId", self.tax_area_id)
        writer.write_bool_value("taxLiable", self.tax_liable)
        writer.write_str_value("taxRegistrationNumber", self.tax_registration_number)
        writer.write_str_value("type", self.type)
        writer.write_str_value("website", self.website)
    
    @property
    def shipment_method(self,) -> Optional[shipment_method.ShipmentMethod]:
        """
        Gets the shipmentMethod property value. The shipmentMethod property
        Returns: Optional[shipment_method.ShipmentMethod]
        """
        return self._shipment_method
    
    @shipment_method.setter
    def shipment_method(self,value: Optional[shipment_method.ShipmentMethod] = None) -> None:
        """
        Sets the shipmentMethod property value. The shipmentMethod property
        Args:
            value: Value to set for the shipmentMethod property.
        """
        self._shipment_method = value
    
    @property
    def shipment_method_id(self,) -> Optional[Guid]:
        """
        Gets the shipmentMethodId property value. The shipmentMethodId property
        Returns: Optional[Guid]
        """
        return self._shipment_method_id
    
    @shipment_method_id.setter
    def shipment_method_id(self,value: Optional[Guid] = None) -> None:
        """
        Sets the shipmentMethodId property value. The shipmentMethodId property
        Args:
            value: Value to set for the shipmentMethodId property.
        """
        self._shipment_method_id = value
    
    @property
    def tax_area_display_name(self,) -> Optional[str]:
        """
        Gets the taxAreaDisplayName property value. The taxAreaDisplayName property
        Returns: Optional[str]
        """
        return self._tax_area_display_name
    
    @tax_area_display_name.setter
    def tax_area_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the taxAreaDisplayName property value. The taxAreaDisplayName property
        Args:
            value: Value to set for the taxAreaDisplayName property.
        """
        self._tax_area_display_name = value
    
    @property
    def tax_area_id(self,) -> Optional[Guid]:
        """
        Gets the taxAreaId property value. The taxAreaId property
        Returns: Optional[Guid]
        """
        return self._tax_area_id
    
    @tax_area_id.setter
    def tax_area_id(self,value: Optional[Guid] = None) -> None:
        """
        Sets the taxAreaId property value. The taxAreaId property
        Args:
            value: Value to set for the taxAreaId property.
        """
        self._tax_area_id = value
    
    @property
    def tax_liable(self,) -> Optional[bool]:
        """
        Gets the taxLiable property value. The taxLiable property
        Returns: Optional[bool]
        """
        return self._tax_liable
    
    @tax_liable.setter
    def tax_liable(self,value: Optional[bool] = None) -> None:
        """
        Sets the taxLiable property value. The taxLiable property
        Args:
            value: Value to set for the taxLiable property.
        """
        self._tax_liable = value
    
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
            value: Value to set for the taxRegistrationNumber property.
        """
        self._tax_registration_number = value
    
    @property
    def type(self,) -> Optional[str]:
        """
        Gets the type property value. The type property
        Returns: Optional[str]
        """
        return self._type
    
    @type.setter
    def type(self,value: Optional[str] = None) -> None:
        """
        Sets the type property value. The type property
        Args:
            value: Value to set for the type property.
        """
        self._type = value
    
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
    

