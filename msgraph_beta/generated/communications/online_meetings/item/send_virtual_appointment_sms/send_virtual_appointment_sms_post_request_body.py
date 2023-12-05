from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....models.virtual_appointment_sms_type import VirtualAppointmentSmsType

@dataclass
class SendVirtualAppointmentSmsPostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The phoneNumbers property
    phone_numbers: Optional[List[str]] = None
    # The smsType property
    sms_type: Optional[VirtualAppointmentSmsType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SendVirtualAppointmentSmsPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SendVirtualAppointmentSmsPostRequestBody
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return SendVirtualAppointmentSmsPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .....models.virtual_appointment_sms_type import VirtualAppointmentSmsType

        from .....models.virtual_appointment_sms_type import VirtualAppointmentSmsType

        fields: Dict[str, Callable[[Any], None]] = {
            "phoneNumbers": lambda n : setattr(self, 'phone_numbers', n.get_collection_of_primitive_values(str)),
            "smsType": lambda n : setattr(self, 'sms_type', n.get_enum_value(VirtualAppointmentSmsType)),
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
        writer.write_collection_of_primitive_values("phoneNumbers", self.phone_numbers)
        writer.write_enum_value("smsType", self.sms_type)
        writer.write_additional_data_value(self.additional_data)
    

