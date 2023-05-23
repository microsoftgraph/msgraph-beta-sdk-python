from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import communications_user_identity, entity, virtual_event_presenter_details

from . import entity

class VirtualEventPresenter(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new virtualEventPresenter and sets the default values.
        """
        super().__init__()
        # The email property
        self._email: Optional[str] = None
        # The identity property
        self._identity: Optional[communications_user_identity.CommunicationsUserIdentity] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The presenterDetails property
        self._presenter_details: Optional[virtual_event_presenter_details.VirtualEventPresenterDetails] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> VirtualEventPresenter:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: VirtualEventPresenter
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return VirtualEventPresenter()
    
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
        from . import communications_user_identity, entity, virtual_event_presenter_details

        fields: Dict[str, Callable[[Any], None]] = {
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "identity": lambda n : setattr(self, 'identity', n.get_object_value(communications_user_identity.CommunicationsUserIdentity)),
            "presenterDetails": lambda n : setattr(self, 'presenter_details', n.get_object_value(virtual_event_presenter_details.VirtualEventPresenterDetails)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def identity(self,) -> Optional[communications_user_identity.CommunicationsUserIdentity]:
        """
        Gets the identity property value. The identity property
        Returns: Optional[communications_user_identity.CommunicationsUserIdentity]
        """
        return self._identity
    
    @identity.setter
    def identity(self,value: Optional[communications_user_identity.CommunicationsUserIdentity] = None) -> None:
        """
        Sets the identity property value. The identity property
        Args:
            value: Value to set for the identity property.
        """
        self._identity = value
    
    @property
    def presenter_details(self,) -> Optional[virtual_event_presenter_details.VirtualEventPresenterDetails]:
        """
        Gets the presenterDetails property value. The presenterDetails property
        Returns: Optional[virtual_event_presenter_details.VirtualEventPresenterDetails]
        """
        return self._presenter_details
    
    @presenter_details.setter
    def presenter_details(self,value: Optional[virtual_event_presenter_details.VirtualEventPresenterDetails] = None) -> None:
        """
        Sets the presenterDetails property value. The presenterDetails property
        Args:
            value: Value to set for the presenter_details property.
        """
        self._presenter_details = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("email", self.email)
        writer.write_object_value("identity", self.identity)
        writer.write_object_value("presenterDetails", self.presenter_details)
    

