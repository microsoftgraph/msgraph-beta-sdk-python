from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
virtual_appointment_settings = lazy_import('msgraph.generated.models.virtual_appointment_settings')
virtual_appointment_user = lazy_import('msgraph.generated.models.virtual_appointment_user')

class VirtualAppointment(entity.Entity):
    @property
    def appointment_client_join_web_url(self,) -> Optional[str]:
        """
        Gets the appointmentClientJoinWebUrl property value. The join web URL of the virtual appointment for clients with waiting room and browser join. Optional.
        Returns: Optional[str]
        """
        return self._appointment_client_join_web_url
    
    @appointment_client_join_web_url.setter
    def appointment_client_join_web_url(self,value: Optional[str] = None) -> None:
        """
        Sets the appointmentClientJoinWebUrl property value. The join web URL of the virtual appointment for clients with waiting room and browser join. Optional.
        Args:
            value: Value to set for the appointmentClientJoinWebUrl property.
        """
        self._appointment_client_join_web_url = value
    
    @property
    def appointment_clients(self,) -> Optional[List[virtual_appointment_user.VirtualAppointmentUser]]:
        """
        Gets the appointmentClients property value. The client information for the virtual appointment, including name, email, and SMS phone number. Optional.
        Returns: Optional[List[virtual_appointment_user.VirtualAppointmentUser]]
        """
        return self._appointment_clients
    
    @appointment_clients.setter
    def appointment_clients(self,value: Optional[List[virtual_appointment_user.VirtualAppointmentUser]] = None) -> None:
        """
        Sets the appointmentClients property value. The client information for the virtual appointment, including name, email, and SMS phone number. Optional.
        Args:
            value: Value to set for the appointmentClients property.
        """
        self._appointment_clients = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new virtualAppointment and sets the default values.
        """
        super().__init__()
        # The join web URL of the virtual appointment for clients with waiting room and browser join. Optional.
        self._appointment_client_join_web_url: Optional[str] = None
        # The client information for the virtual appointment, including name, email, and SMS phone number. Optional.
        self._appointment_clients: Optional[List[virtual_appointment_user.VirtualAppointmentUser]] = None
        # The identifier of the appointment from the scheduling system, associated with the current virtual appointment. Optional.
        self._external_appointment_id: Optional[str] = None
        # The URL of the appointment resource from the scheduling system, associated with the current virtual appointment. Optional.
        self._external_appointment_url: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The settings associated with the virtual appointment resource. Optional.
        self._settings: Optional[virtual_appointment_settings.VirtualAppointmentSettings] = None
    
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
    
    @property
    def external_appointment_id(self,) -> Optional[str]:
        """
        Gets the externalAppointmentId property value. The identifier of the appointment from the scheduling system, associated with the current virtual appointment. Optional.
        Returns: Optional[str]
        """
        return self._external_appointment_id
    
    @external_appointment_id.setter
    def external_appointment_id(self,value: Optional[str] = None) -> None:
        """
        Sets the externalAppointmentId property value. The identifier of the appointment from the scheduling system, associated with the current virtual appointment. Optional.
        Args:
            value: Value to set for the externalAppointmentId property.
        """
        self._external_appointment_id = value
    
    @property
    def external_appointment_url(self,) -> Optional[str]:
        """
        Gets the externalAppointmentUrl property value. The URL of the appointment resource from the scheduling system, associated with the current virtual appointment. Optional.
        Returns: Optional[str]
        """
        return self._external_appointment_url
    
    @external_appointment_url.setter
    def external_appointment_url(self,value: Optional[str] = None) -> None:
        """
        Sets the externalAppointmentUrl property value. The URL of the appointment resource from the scheduling system, associated with the current virtual appointment. Optional.
        Args:
            value: Value to set for the externalAppointmentUrl property.
        """
        self._external_appointment_url = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "appointment_client_join_web_url": lambda n : setattr(self, 'appointment_client_join_web_url', n.get_str_value()),
            "appointment_clients": lambda n : setattr(self, 'appointment_clients', n.get_collection_of_object_values(virtual_appointment_user.VirtualAppointmentUser)),
            "external_appointment_id": lambda n : setattr(self, 'external_appointment_id', n.get_str_value()),
            "external_appointment_url": lambda n : setattr(self, 'external_appointment_url', n.get_str_value()),
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
        writer.write_str_value("appointmentClientJoinWebUrl", self.appointment_client_join_web_url)
        writer.write_collection_of_object_values("appointmentClients", self.appointment_clients)
        writer.write_str_value("externalAppointmentId", self.external_appointment_id)
        writer.write_str_value("externalAppointmentUrl", self.external_appointment_url)
        writer.write_object_value("settings", self.settings)
    
    @property
    def settings(self,) -> Optional[virtual_appointment_settings.VirtualAppointmentSettings]:
        """
        Gets the settings property value. The settings associated with the virtual appointment resource. Optional.
        Returns: Optional[virtual_appointment_settings.VirtualAppointmentSettings]
        """
        return self._settings
    
    @settings.setter
    def settings(self,value: Optional[virtual_appointment_settings.VirtualAppointmentSettings] = None) -> None:
        """
        Sets the settings property value. The settings associated with the virtual appointment resource. Optional.
        Args:
            value: Value to set for the settings property.
        """
        self._settings = value
    

