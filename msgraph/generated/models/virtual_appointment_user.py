from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class VirtualAppointmentUser(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The display name of the user who participates in a virtual appointment. Optional.
    display_name: Optional[str] = None
    # The email address of the user who participates in a virtual appointment. Optional.
    email_address: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The phone number for sending SMS texts for the user who participates in a virtual appointment. Optional.
    sms_capable_phone_number: Optional[str] = None
    
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
    

