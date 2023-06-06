from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import endpoint_type, identity, identity_set

from . import identity_set

@dataclass
class CommunicationsIdentitySet(identity_set.IdentitySet):
    odata_type = "#microsoft.graph.communicationsIdentitySet"
    # The application instance associated with this action.
    application_instance: Optional[identity.Identity] = None
    # An identity the participant would like to present itself as to the other participants in the call.
    asserted_identity: Optional[identity.Identity] = None
    # The Azure Communication Services user associated with this action.
    azure_communication_services_user: Optional[identity.Identity] = None
    # The encrypted user associated with this action.
    encrypted: Optional[identity.Identity] = None
    # Type of endpoint the participant is using. Possible values are: default, voicemail, skypeForBusiness, skypeForBusinessVoipPhone and unknownFutureValue.
    endpoint_type: Optional[endpoint_type.EndpointType] = None
    # The guest user associated with this action.
    guest: Optional[identity.Identity] = None
    # The Skype for Business On-Premises user associated with this action.
    on_premises: Optional[identity.Identity] = None
    # Inherited from identitySet. The phone user associated with this action.
    phone: Optional[identity.Identity] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CommunicationsIdentitySet:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CommunicationsIdentitySet
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CommunicationsIdentitySet()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import endpoint_type, identity, identity_set

        fields: Dict[str, Callable[[Any], None]] = {
            "applicationInstance": lambda n : setattr(self, 'application_instance', n.get_object_value(identity.Identity)),
            "assertedIdentity": lambda n : setattr(self, 'asserted_identity', n.get_object_value(identity.Identity)),
            "azureCommunicationServicesUser": lambda n : setattr(self, 'azure_communication_services_user', n.get_object_value(identity.Identity)),
            "encrypted": lambda n : setattr(self, 'encrypted', n.get_object_value(identity.Identity)),
            "endpointType": lambda n : setattr(self, 'endpoint_type', n.get_enum_value(endpoint_type.EndpointType)),
            "guest": lambda n : setattr(self, 'guest', n.get_object_value(identity.Identity)),
            "onPremises": lambda n : setattr(self, 'on_premises', n.get_object_value(identity.Identity)),
            "phone": lambda n : setattr(self, 'phone', n.get_object_value(identity.Identity)),
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
        writer.write_object_value("applicationInstance", self.application_instance)
        writer.write_object_value("assertedIdentity", self.asserted_identity)
        writer.write_object_value("azureCommunicationServicesUser", self.azure_communication_services_user)
        writer.write_object_value("encrypted", self.encrypted)
        writer.write_enum_value("endpointType", self.endpoint_type)
        writer.write_object_value("guest", self.guest)
        writer.write_object_value("onPremises", self.on_premises)
        writer.write_object_value("phone", self.phone)
    

