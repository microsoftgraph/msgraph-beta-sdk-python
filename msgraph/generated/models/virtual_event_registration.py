from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, virtual_event_registrant, virtual_event_registration_question

from . import entity

class VirtualEventRegistration(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new virtualEventRegistration and sets the default values.
        """
        super().__init__()
        # The capacity property
        self._capacity: Optional[int] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The questions property
        self._questions: Optional[List[virtual_event_registration_question.VirtualEventRegistrationQuestion]] = None
        # The registrants property
        self._registrants: Optional[List[virtual_event_registrant.VirtualEventRegistrant]] = None
        # The registrationWebUrl property
        self._registration_web_url: Optional[str] = None
    
    @property
    def capacity(self,) -> Optional[int]:
        """
        Gets the capacity property value. The capacity property
        Returns: Optional[int]
        """
        return self._capacity
    
    @capacity.setter
    def capacity(self,value: Optional[int] = None) -> None:
        """
        Sets the capacity property value. The capacity property
        Args:
            value: Value to set for the capacity property.
        """
        self._capacity = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> VirtualEventRegistration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: VirtualEventRegistration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return VirtualEventRegistration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, virtual_event_registrant, virtual_event_registration_question

        fields: Dict[str, Callable[[Any], None]] = {
            "capacity": lambda n : setattr(self, 'capacity', n.get_int_value()),
            "questions": lambda n : setattr(self, 'questions', n.get_collection_of_object_values(virtual_event_registration_question.VirtualEventRegistrationQuestion)),
            "registrants": lambda n : setattr(self, 'registrants', n.get_collection_of_object_values(virtual_event_registrant.VirtualEventRegistrant)),
            "registrationWebUrl": lambda n : setattr(self, 'registration_web_url', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def questions(self,) -> Optional[List[virtual_event_registration_question.VirtualEventRegistrationQuestion]]:
        """
        Gets the questions property value. The questions property
        Returns: Optional[List[virtual_event_registration_question.VirtualEventRegistrationQuestion]]
        """
        return self._questions
    
    @questions.setter
    def questions(self,value: Optional[List[virtual_event_registration_question.VirtualEventRegistrationQuestion]] = None) -> None:
        """
        Sets the questions property value. The questions property
        Args:
            value: Value to set for the questions property.
        """
        self._questions = value
    
    @property
    def registrants(self,) -> Optional[List[virtual_event_registrant.VirtualEventRegistrant]]:
        """
        Gets the registrants property value. The registrants property
        Returns: Optional[List[virtual_event_registrant.VirtualEventRegistrant]]
        """
        return self._registrants
    
    @registrants.setter
    def registrants(self,value: Optional[List[virtual_event_registrant.VirtualEventRegistrant]] = None) -> None:
        """
        Sets the registrants property value. The registrants property
        Args:
            value: Value to set for the registrants property.
        """
        self._registrants = value
    
    @property
    def registration_web_url(self,) -> Optional[str]:
        """
        Gets the registrationWebUrl property value. The registrationWebUrl property
        Returns: Optional[str]
        """
        return self._registration_web_url
    
    @registration_web_url.setter
    def registration_web_url(self,value: Optional[str] = None) -> None:
        """
        Sets the registrationWebUrl property value. The registrationWebUrl property
        Args:
            value: Value to set for the registration_web_url property.
        """
        self._registration_web_url = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_int_value("capacity", self.capacity)
        writer.write_collection_of_object_values("questions", self.questions)
        writer.write_collection_of_object_values("registrants", self.registrants)
        writer.write_str_value("registrationWebUrl", self.registration_web_url)
    

