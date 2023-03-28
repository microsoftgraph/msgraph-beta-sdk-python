from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

class VirtualAppointmentUser(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new virtualAppointmentUser and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The display name of the user who participates in a virtual appointment. Optional.
        self._display_name: Optional[str] = None
        # The email address of the user who participates in a virtual appointment. Optional.
        self._email_address: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The phone number for sending SMS texts for the user who participates in a virtual appointment. Optional.
        self._sms_capable_phone_number: Optional[str] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> VirtualAppointmentUser:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: VirtualAppointmentUser
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return VirtualAppointmentUser()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The display name of the user who participates in a virtual appointment. Optional.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display name of the user who participates in a virtual appointment. Optional.
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    @property
    def email_address(self,) -> Optional[str]:
        """
        Gets the emailAddress property value. The email address of the user who participates in a virtual appointment. Optional.
        Returns: Optional[str]
        """
        return self._email_address
    
    @email_address.setter
    def email_address(self,value: Optional[str] = None) -> None:
        """
        Sets the emailAddress property value. The email address of the user who participates in a virtual appointment. Optional.
        Args:
            value: Value to set for the email_address property.
        """
        self._email_address = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "emailAddress": lambda n : setattr(self, 'email_address', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "smsCapablePhoneNumber": lambda n : setattr(self, 'sms_capable_phone_number', n.get_str_value()),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("emailAddress", self.email_address)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("smsCapablePhoneNumber", self.sms_capable_phone_number)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def sms_capable_phone_number(self,) -> Optional[str]:
        """
        Gets the smsCapablePhoneNumber property value. The phone number for sending SMS texts for the user who participates in a virtual appointment. Optional.
        Returns: Optional[str]
        """
        return self._sms_capable_phone_number
    
    @sms_capable_phone_number.setter
    def sms_capable_phone_number(self,value: Optional[str] = None) -> None:
        """
        Sets the smsCapablePhoneNumber property value. The phone number for sending SMS texts for the user who participates in a virtual appointment. Optional.
        Args:
            value: Value to set for the sms_capable_phone_number property.
        """
        self._sms_capable_phone_number = value
    

