from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, virtual_appointment_settings, virtual_appointment_user

from . import entity

@dataclass
class VirtualAppointment(entity.Entity):
    # The join web URL of the virtual appointment for clients with waiting room and browser join. Optional.
    appointment_client_join_web_url: Optional[str] = None
    # The client information for the virtual appointment, including name, email, and SMS phone number. Optional.
    appointment_clients: Optional[List[virtual_appointment_user.VirtualAppointmentUser]] = None
    # The identifier of the appointment from the scheduling system, associated with the current virtual appointment. Optional.
    external_appointment_id: Optional[str] = None
    # The URL of the appointment resource from the scheduling system, associated with the current virtual appointment. Optional.
    external_appointment_url: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The settings associated with the virtual appointment resource. Optional.
    settings: Optional[virtual_appointment_settings.VirtualAppointmentSettings] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> VirtualAppointment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: VirtualAppointment
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return VirtualAppointment()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, virtual_appointment_settings, virtual_appointment_user

        fields: Dict[str, Callable[[Any], None]] = {
            "appointmentClients": lambda n : setattr(self, 'appointment_clients', n.get_collection_of_object_values(virtual_appointment_user.VirtualAppointmentUser)),
            "appointmentClientJoinWebUrl": lambda n : setattr(self, 'appointment_client_join_web_url', n.get_str_value()),
            "externalAppointmentId": lambda n : setattr(self, 'external_appointment_id', n.get_str_value()),
            "externalAppointmentUrl": lambda n : setattr(self, 'external_appointment_url', n.get_str_value()),
            "settings": lambda n : setattr(self, 'settings', n.get_object_value(virtual_appointment_settings.VirtualAppointmentSettings)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("appointmentClients", self.appointment_clients)
        writer.write_str_value("appointmentClientJoinWebUrl", self.appointment_client_join_web_url)
        writer.write_str_value("externalAppointmentId", self.external_appointment_id)
        writer.write_str_value("externalAppointmentUrl", self.external_appointment_url)
        writer.write_object_value("settings", self.settings)
    

