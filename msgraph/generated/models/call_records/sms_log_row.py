from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class SmsLogRow(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Amount of money or cost of the SMS that is charged.
    call_charge: Optional[float] = None
    # Currency used to calculate the cost of the call. For details, see ISO 4217.
    currency: Optional[str] = None
    # Indicates whether the SMS was Domestic (within a country or region) or International (outside a country or region) based on the user's location.
    destination_context: Optional[str] = None
    # Country or region of a phone number that received the SMS.
    destination_name: Optional[str] = None
    # Partially obfuscated phone number that received the SMS. For details, see E.164.
    destination_number: Optional[str] = None
    # Unique identifier (GUID) for the SMS.
    id: Optional[str] = None
    # The license used for the SMS.
    license_capability: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # For an outbound SMS, the country code of the receiver; otherwise (inbound SMS) the country code of the sender. For details, see ISO 3166-1 alpha-2.
    other_party_country_code: Optional[str] = None
    # The date and time when the SMS was sent.
    sent_date_time: Optional[datetime.datetime] = None
    # SMS identifier. Not guaranteed to be unique.
    sms_id: Optional[str] = None
    # Type of SMS such as outbound or inbound.
    sms_type: Optional[str] = None
    # Number of SMS units sent/received.
    sms_units: Optional[int] = None
    # Partially obfuscated phone number that sent the SMS. For details, see E.164.
    source_number: Optional[str] = None
    # Country code of the tenant. For details, see ISO 3166-1 alpha-2.
    tenant_country_code: Optional[str] = None
    # Country code of the user. For details, see ISO 3166-1 alpha-2.
    user_country_code: Optional[str] = None
    # Display name of the user.
    user_display_name: Optional[str] = None
    # The unique identifier (GUID) of the user in Microsoft Entra ID.
    user_id: Optional[str] = None
    # The user principal name (sign-in name) in Microsoft Entra ID. This is usually the same as the user's SIP address, and can be same as the user's e-mail address.
    user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SmsLogRow:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SmsLogRow
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return SmsLogRow()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "callCharge": lambda n : setattr(self, 'call_charge', n.get_float_value()),
            "currency": lambda n : setattr(self, 'currency', n.get_str_value()),
            "destinationContext": lambda n : setattr(self, 'destination_context', n.get_str_value()),
            "destinationName": lambda n : setattr(self, 'destination_name', n.get_str_value()),
            "destinationNumber": lambda n : setattr(self, 'destination_number', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "licenseCapability": lambda n : setattr(self, 'license_capability', n.get_str_value()),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "otherPartyCountryCode": lambda n : setattr(self, 'other_party_country_code', n.get_str_value()),
            "sentDateTime": lambda n : setattr(self, 'sent_date_time', n.get_datetime_value()),
            "smsId": lambda n : setattr(self, 'sms_id', n.get_str_value()),
            "smsType": lambda n : setattr(self, 'sms_type', n.get_str_value()),
            "smsUnits": lambda n : setattr(self, 'sms_units', n.get_int_value()),
            "sourceNumber": lambda n : setattr(self, 'source_number', n.get_str_value()),
            "tenantCountryCode": lambda n : setattr(self, 'tenant_country_code', n.get_str_value()),
            "userCountryCode": lambda n : setattr(self, 'user_country_code', n.get_str_value()),
            "userDisplayName": lambda n : setattr(self, 'user_display_name', n.get_str_value()),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
            "userPrincipalName": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_float_value("callCharge", self.call_charge)
        writer.write_str_value("currency", self.currency)
        writer.write_str_value("destinationContext", self.destination_context)
        writer.write_str_value("destinationName", self.destination_name)
        writer.write_str_value("destinationNumber", self.destination_number)
        writer.write_str_value("id", self.id)
        writer.write_str_value("licenseCapability", self.license_capability)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_str_value("otherPartyCountryCode", self.other_party_country_code)
        writer.write_datetime_value("sentDateTime", self.sent_date_time)
        writer.write_str_value("smsId", self.sms_id)
        writer.write_str_value("smsType", self.sms_type)
        writer.write_int_value("smsUnits", self.sms_units)
        writer.write_str_value("sourceNumber", self.source_number)
        writer.write_str_value("tenantCountryCode", self.tenant_country_code)
        writer.write_str_value("userCountryCode", self.user_country_code)
        writer.write_str_value("userDisplayName", self.user_display_name)
        writer.write_str_value("userId", self.user_id)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
        writer.write_additional_data_value(self.additional_data)
    

