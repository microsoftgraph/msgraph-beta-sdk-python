from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

class PstnOnlineMeetingDialoutReport(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new pstnOnlineMeetingDialoutReport and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Currency used to calculate the cost of the call. For details, see ISO 4217.
        self._currency: Optional[str] = None
        # Indicates whether the call was Domestic (within a country or region) or International (outside a country or region) based on the user's location.
        self._destination_context: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Total costs of all the calls within the selected time range, including call charges and connection fees.
        self._total_call_charge: Optional[float] = None
        # Total duration of all the calls within the selected time range, in seconds.
        self._total_call_seconds: Optional[int] = None
        # Total number of dial-out calls within the selected time range.
        self._total_calls: Optional[int] = None
        # Country code of the user. For details, see ISO 3166-1 alpha-2.
        self._usage_location: Optional[str] = None
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
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PstnOnlineMeetingDialoutReport:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PstnOnlineMeetingDialoutReport
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PstnOnlineMeetingDialoutReport()
    
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
        Gets the destinationContext property value. Indicates whether the call was Domestic (within a country or region) or International (outside a country or region) based on the user's location.
        Returns: Optional[str]
        """
        return self._destination_context
    
    @destination_context.setter
    def destination_context(self,value: Optional[str] = None) -> None:
        """
        Sets the destinationContext property value. Indicates whether the call was Domestic (within a country or region) or International (outside a country or region) based on the user's location.
        Args:
            value: Value to set for the destination_context property.
        """
        self._destination_context = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "currency": lambda n : setattr(self, 'currency', n.get_str_value()),
            "destinationContext": lambda n : setattr(self, 'destination_context', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "totalCalls": lambda n : setattr(self, 'total_calls', n.get_int_value()),
            "totalCallCharge": lambda n : setattr(self, 'total_call_charge', n.get_float_value()),
            "totalCallSeconds": lambda n : setattr(self, 'total_call_seconds', n.get_int_value()),
            "usageLocation": lambda n : setattr(self, 'usage_location', n.get_str_value()),
            "userDisplayName": lambda n : setattr(self, 'user_display_name', n.get_str_value()),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
            "userPrincipalName": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
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
            value: Value to set for the odata_type property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("currency", self.currency)
        writer.write_str_value("destinationContext", self.destination_context)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("totalCalls", self.total_calls)
        writer.write_float_value("totalCallCharge", self.total_call_charge)
        writer.write_int_value("totalCallSeconds", self.total_call_seconds)
        writer.write_str_value("usageLocation", self.usage_location)
        writer.write_str_value("userDisplayName", self.user_display_name)
        writer.write_str_value("userId", self.user_id)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def total_call_charge(self,) -> Optional[float]:
        """
        Gets the totalCallCharge property value. Total costs of all the calls within the selected time range, including call charges and connection fees.
        Returns: Optional[float]
        """
        return self._total_call_charge
    
    @total_call_charge.setter
    def total_call_charge(self,value: Optional[float] = None) -> None:
        """
        Sets the totalCallCharge property value. Total costs of all the calls within the selected time range, including call charges and connection fees.
        Args:
            value: Value to set for the total_call_charge property.
        """
        self._total_call_charge = value
    
    @property
    def total_call_seconds(self,) -> Optional[int]:
        """
        Gets the totalCallSeconds property value. Total duration of all the calls within the selected time range, in seconds.
        Returns: Optional[int]
        """
        return self._total_call_seconds
    
    @total_call_seconds.setter
    def total_call_seconds(self,value: Optional[int] = None) -> None:
        """
        Sets the totalCallSeconds property value. Total duration of all the calls within the selected time range, in seconds.
        Args:
            value: Value to set for the total_call_seconds property.
        """
        self._total_call_seconds = value
    
    @property
    def total_calls(self,) -> Optional[int]:
        """
        Gets the totalCalls property value. Total number of dial-out calls within the selected time range.
        Returns: Optional[int]
        """
        return self._total_calls
    
    @total_calls.setter
    def total_calls(self,value: Optional[int] = None) -> None:
        """
        Sets the totalCalls property value. Total number of dial-out calls within the selected time range.
        Args:
            value: Value to set for the total_calls property.
        """
        self._total_calls = value
    
    @property
    def usage_location(self,) -> Optional[str]:
        """
        Gets the usageLocation property value. Country code of the user. For details, see ISO 3166-1 alpha-2.
        Returns: Optional[str]
        """
        return self._usage_location
    
    @usage_location.setter
    def usage_location(self,value: Optional[str] = None) -> None:
        """
        Sets the usageLocation property value. Country code of the user. For details, see ISO 3166-1 alpha-2.
        Args:
            value: Value to set for the usage_location property.
        """
        self._usage_location = value
    
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
    

