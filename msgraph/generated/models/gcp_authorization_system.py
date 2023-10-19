from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authorization_system import AuthorizationSystem
    from .authorization_system_type_service import AuthorizationSystemTypeService
    from .gcp_associated_identities import GcpAssociatedIdentities
    from .gcp_authorization_system_resource import GcpAuthorizationSystemResource
    from .gcp_authorization_system_type_action import GcpAuthorizationSystemTypeAction
    from .gcp_role import GcpRole

from .authorization_system import AuthorizationSystem

@dataclass
class GcpAuthorizationSystem(AuthorizationSystem):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.gcpAuthorizationSystem"
    # The actions property
    actions: Optional[List[GcpAuthorizationSystemTypeAction]] = None
    # The associatedIdentities property
    associated_identities: Optional[GcpAssociatedIdentities] = None
    # The resources property
    resources: Optional[List[GcpAuthorizationSystemResource]] = None
    # The roles property
    roles: Optional[List[GcpRole]] = None
    # The services property
    services: Optional[List[AuthorizationSystemTypeService]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> GcpAuthorizationSystem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: GcpAuthorizationSystem
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return GcpAuthorizationSystem()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .authorization_system import AuthorizationSystem
        from .authorization_system_type_service import AuthorizationSystemTypeService
        from .gcp_associated_identities import GcpAssociatedIdentities
        from .gcp_authorization_system_resource import GcpAuthorizationSystemResource
        from .gcp_authorization_system_type_action import GcpAuthorizationSystemTypeAction
        from .gcp_role import GcpRole

        from .authorization_system import AuthorizationSystem
        from .authorization_system_type_service import AuthorizationSystemTypeService
        from .gcp_associated_identities import GcpAssociatedIdentities
        from .gcp_authorization_system_resource import GcpAuthorizationSystemResource
        from .gcp_authorization_system_type_action import GcpAuthorizationSystemTypeAction
        from .gcp_role import GcpRole

        fields: Dict[str, Callable[[Any], None]] = {
            "actions": lambda n : setattr(self, 'actions', n.get_collection_of_object_values(GcpAuthorizationSystemTypeAction)),
            "associatedIdentities": lambda n : setattr(self, 'associated_identities', n.get_object_value(GcpAssociatedIdentities)),
            "resources": lambda n : setattr(self, 'resources', n.get_collection_of_object_values(GcpAuthorizationSystemResource)),
            "roles": lambda n : setattr(self, 'roles', n.get_collection_of_object_values(GcpRole)),
            "services": lambda n : setattr(self, 'services', n.get_collection_of_object_values(AuthorizationSystemTypeService)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("actions", self.actions)
        writer.write_object_value("associatedIdentities", self.associated_identities)
        writer.write_collection_of_object_values("resources", self.resources)
        writer.write_collection_of_object_values("roles", self.roles)
        writer.write_collection_of_object_values("services", self.services)
    

