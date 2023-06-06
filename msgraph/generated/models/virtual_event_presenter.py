from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import communications_user_identity, entity, virtual_event_presenter_details

from . import entity

@dataclass
class VirtualEventPresenter(entity.Entity):
    # Email address of the presenter.
    email: Optional[str] = None
    # Identity information of the presenter.
    identity: Optional[communications_user_identity.CommunicationsUserIdentity] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Other detail information of the presenter.
    presenter_details: Optional[virtual_event_presenter_details.VirtualEventPresenterDetails] = None
    
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
    

