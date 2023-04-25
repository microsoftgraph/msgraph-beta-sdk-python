from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

class SmsLogRow(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new smsLogRow and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Amount of money or cost of the SMS that is charged.
        self._call_charge: Optional[float] = None
        # Currency used to calculate the cost of the call. For details, see ISO 4217.
        self._currency: Optional[str] = None
        # Indicates whether the SMS was Domestic (within a country or region) or International (outside a country or region) based on the user's location.
        self._destination_context: Optional[str] = None
        # Country or region of a phone number that received the SMS.
        self._destination_name: Optional[str] = None
        # Partially obfuscated phone number that received the SMS. For details, see E.164.
        self._destination_number: Optional[str] = None
        # Unique identifier (GUID) for the SMS.
        self._id: Optional[str] = None
        # The license used for the SMS.
        self._license_capability: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # For an outbound SMS, the country code of the receiver; otherwise (inbound SMS) the country code of the sender. For details, see ISO 3166-1 alpha-2.
        self._other_party_country_code: Optional[str] = None
        # The date and time when the SMS was sent.
        self._sent_date_time: Optional[datetime] = None
        # SMS identifier. Not guaranteed to be unique.
        self._sms_id: Optional[str] = None
        # Type of SMS such as outbound or inbound.
        self._sms_type: Optional[str] = None
        # Number of SMS units sent/received.
        self._sms_units: Optional[int] = None
        # Partially obfuscated phone number that sent the SMS. For details, see E.164.
        self._source_number: Optional[str] = None
        # Country code of the tenant. For details, see ISO 3166-1 alpha-2.
        self._tenant_country_code: Optional[str] = None
        # Country code of the user. For details, see ISO 3166-1 alpha-2.
        self._user_country_code: Optional[str] = None
        # Display name of the user.
        self._user_display_name: Optional[str] = None
        # The unique identifier (GUID) of the user in Azure Active Directory.
        self._user_id: Optional[str] = None
        # The user principal name (sign-in name) in Azure Active Directory. This is usually the same as the user's SIP address, and can be same as the user's e-mail address.
        self._user_principal_name: Optional[str] = None
    
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
    def call_charge(self,) -> Optional[float]:
        """
        Gets the callCharge property value. Amount of money or cost of the SMS that is charged.
        Returns: Optional[float]
        """
        return self._call_charge
    
    @call_charge.setter
    def call_charge(self,value: Optional[float] = None) -> None:
        """
        Sets the callCharge property value. Amount of money or cost of the SMS that is charged.
        Args:
            value: Value to set for the call_charge property.
        """
        self._call_charge = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SmsLogRow:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SmsLogRow
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SmsLogRow()
    
    @property
    def currency(self,) -> Optional[str]:
        """
        Gets the currency property value. Currency used to calculate the cost of the call. For details, see ISO 4217.
        Returns: Optional[str]
        """
        return self._currency
    
    @currency.setter
    def currency(self,value: Optional[str] = None) -> None:
        """
        Sets the currency property value. Currency used to calculate the cost of the call. For details, see ISO 4217.
        Args:
            value: Value to set for the currency property.
        """
        self._currency = value
    
    @property
    def destination_context(self,) -> Optional[str]:
        """
        Gets the destinationContext property value. Indicates whether the SMS was Domestic (within a country or region) or International (outside a country or region) based on the user's location.
        Returns: Optional[str]
        """
        return self._destination_context
    
    @destination_context.setter
    def destination_context(self,value: Optional[str] = None) -> None:
        """
        Sets the destinationContext property value. Indicates whether the SMS was Domestic (within a country or region) or International (outside a country or region) based on the user's location.
        Args:
            value: Value to set for the destination_context property.
        """
        self._destination_context = value
    
    @property
    def destination_name(self,) -> Optional[str]:
        """
        Gets the destinationName property value. Country or region of a phone number that received the SMS.
        Returns: Optional[str]
        """
        return self._destination_name
    
    @destination_name.setter
    def destination_name(self,value: Optional[str] = None) -> None:
        """
        Sets the destinationName property value. Country or region of a phone number that received the SMS.
        Args:
            value: Value to set for the destination_name property.
        """
        self._destination_name = value
    
    @property
    def destination_number(self,) -> Optional[str]:
        """
        Gets the destinationNumber property value. Partially obfuscated phone number that received the SMS. For details, see E.164.
        Returns: Optional[str]
        """
        return self._destination_number
    
    @destination_number.setter
    def destination_number(self,value: Optional[str] = None) -> None:
        """
        Sets the destinationNumber property value. Partially obfuscated phone number that received the SMS. For details, see E.164.
        Args:
            value: Value to set for the destination_number property.
        """
        self._destination_number = value
    
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
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
    
    @property
    def id(self,) -> Optional[str]:
        """
        Gets the id property value. Unique identifier (GUID) for the SMS.
        Returns: Optional[str]
        """
        return self._id
    
    @id.setter
    def id(self,value: Optional[str] = None) -> None:
        """
        Sets the id property value. Unique identifier (GUID) for the SMS.
        Args:
            value: Value to set for the id property.
        """
        self._id = value
    
    @property
    def license_capability(self,) -> Optional[str]:
        """
        Gets the licenseCapability property value. The license used for the SMS.
        Returns: Optional[str]
        """
        return self._license_capability
    
    @license_capability.setter
    def license_capability(self,value: Optional[str] = None) -> None:
        """
        Sets the licenseCapability property value. The license used for the SMS.
        Args:
            value: Value to set for the license_capability property.
        """
        self._license_capability = value
    
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
            value: Value to set for the odata_type property.
        """
        self._odata_type = value
    
    @property
    def other_party_country_code(self,) -> Optional[str]:
        """
        Gets the otherPartyCountryCode property value. For an outbound SMS, the country code of the receiver; otherwise (inbound SMS) the country code of the sender. For details, see ISO 3166-1 alpha-2.
        Returns: Optional[str]
        """
        return self._other_party_country_code
    
    @other_party_country_code.setter
    def other_party_country_code(self,value: Optional[str] = None) -> None:
        """
        Sets the otherPartyCountryCode property value. For an outbound SMS, the country code of the receiver; otherwise (inbound SMS) the country code of the sender. For details, see ISO 3166-1 alpha-2.
        Args:
            value: Value to set for the other_party_country_code property.
        """
        self._other_party_country_code = value
    
    @property
    def sent_date_time(self,) -> Optional[datetime]:
        """
        Gets the sentDateTime property value. The date and time when the SMS was sent.
        Returns: Optional[datetime]
        """
        return self._sent_date_time
    
    @sent_date_time.setter
    def sent_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the sentDateTime property value. The date and time when the SMS was sent.
        Args:
            value: Value to set for the sent_date_time property.
        """
        self._sent_date_time = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_float_value("callCharge", self.call_charge)
        writer.write_str_value("currency", self.currency)
        writer.write_str_value("destinationContext", self.destination_context)
        writer.write_str_value("destinationName", self.destination_name)
        writer.write_str_value("destinationNumber", self.destination_number)
        writer.write_str_value("id", self.id)
        writer.write_str_value("licenseCapability", self.license_capability)
        writer.write_str_value("@odata.type", self.odata_type)
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
    
    @property
    def sms_id(self,) -> Optional[str]:
        """
        Gets the smsId property value. SMS identifier. Not guaranteed to be unique.
        Returns: Optional[str]
        """
        return self._sms_id
    
    @sms_id.setter
    def sms_id(self,value: Optional[str] = None) -> None:
        """
        Sets the smsId property value. SMS identifier. Not guaranteed to be unique.
        Args:
            value: Value to set for the sms_id property.
        """
        self._sms_id = value
    
    @property
    def sms_type(self,) -> Optional[str]:
        """
        Gets the smsType property value. Type of SMS such as outbound or inbound.
        Returns: Optional[str]
        """
        return self._sms_type
    
    @sms_type.setter
    def sms_type(self,value: Optional[str] = None) -> None:
        """
        Sets the smsType property value. Type of SMS such as outbound or inbound.
        Args:
            value: Value to set for the sms_type property.
        """
        self._sms_type = value
    
    @property
    def sms_units(self,) -> Optional[int]:
        """
        Gets the smsUnits property value. Number of SMS units sent/received.
        Returns: Optional[int]
        """
        return self._sms_units
    
    @sms_units.setter
    def sms_units(self,value: Optional[int] = None) -> None:
        """
        Sets the smsUnits property value. Number of SMS units sent/received.
        Args:
            value: Value to set for the sms_units property.
        """
        self._sms_units = value
    
    @property
    def source_number(self,) -> Optional[str]:
        """
        Gets the sourceNumber property value. Partially obfuscated phone number that sent the SMS. For details, see E.164.
        Returns: Optional[str]
        """
        return self._source_number
    
    @source_number.setter
    def source_number(self,value: Optional[str] = None) -> None:
        """
        Sets the sourceNumber property value. Partially obfuscated phone number that sent the SMS. For details, see E.164.
        Args:
            value: Value to set for the source_number property.
        """
        self._source_number = value
    
    @property
    def tenant_country_code(self,) -> Optional[str]:
        """
        Gets the tenantCountryCode property value. Country code of the tenant. For details, see ISO 3166-1 alpha-2.
        Returns: Optional[str]
        """
        return self._tenant_country_code
    
    @tenant_country_code.setter
    def tenant_country_code(self,value: Optional[str] = None) -> None:
        """
        Sets the tenantCountryCode property value. Country code of the tenant. For details, see ISO 3166-1 alpha-2.
        Args:
            value: Value to set for the tenant_country_code property.
        """
        self._tenant_country_code = value
    
    @property
    def user_country_code(self,) -> Optional[str]:
        """
        Gets the userCountryCode property value. Country code of the user. For details, see ISO 3166-1 alpha-2.
        Returns: Optional[str]
        """
        return self._user_country_code
    
    @user_country_code.setter
    def user_country_code(self,value: Optional[str] = None) -> None:
        """
        Sets the userCountryCode property value. Country code of the user. For details, see ISO 3166-1 alpha-2.
        Args:
            value: Value to set for the user_country_code property.
        """
        self._user_country_code = value
    
    @property
    def user_display_name(self,) -> Optional[str]:
        """
        Gets the userDisplayName property value. Display name of the user.
        Returns: Optional[str]
        """
        return self._user_display_name
    
    @user_display_name.setter
    def user_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userDisplayName property value. Display name of the user.
        Args:
            value: Value to set for the user_display_name property.
        """
        self._user_display_name = value
    
    @property
    def user_id(self,) -> Optional[str]:
        """
        Gets the userId property value. The unique identifier (GUID) of the user in Azure Active Directory.
        Returns: Optional[str]
        """
        return self._user_id
    
    @user_id.setter
    def user_id(self,value: Optional[str] = None) -> None:
        """
        Sets the userId property value. The unique identifier (GUID) of the user in Azure Active Directory.
        Args:
            value: Value to set for the user_id property.
        """
        self._user_id = value
    
    @property
    def user_principal_name(self,) -> Optional[str]:
        """
        Gets the userPrincipalName property value. The user principal name (sign-in name) in Azure Active Directory. This is usually the same as the user's SIP address, and can be same as the user's e-mail address.
        Returns: Optional[str]
        """
        return self._user_principal_name
    
    @user_principal_name.setter
    def user_principal_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userPrincipalName property value. The user principal name (sign-in name) in Azure Active Directory. This is usually the same as the user's SIP address, and can be same as the user's e-mail address.
        Args:
            value: Value to set for the user_principal_name property.
        """
        self._user_principal_name = value
    

