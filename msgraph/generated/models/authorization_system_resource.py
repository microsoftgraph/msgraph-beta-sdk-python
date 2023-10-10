from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authorization_system import AuthorizationSystem
    from .aws_authorization_system_resource import AwsAuthorizationSystemResource
    from .azure_authorization_system_resource import AzureAuthorizationSystemResource
    from .entity import Entity
    from .gcp_authorization_system_resource import GcpAuthorizationSystemResource

from .entity import Entity

@dataclass
class AuthorizationSystemResource(Entity):
    # The authorizationSystem property
    authorization_system: Optional[AuthorizationSystem] = None
    # The displayName property
    display_name: Optional[str] = None
    # The externalId property
    external_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The resourceType property
    resource_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AuthorizationSystemResource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AuthorizationSystemResource
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.awsAuthorizationSystemResource".casefold():
            from .aws_authorization_system_resource import AwsAuthorizationSystemResource

            return AwsAuthorizationSystemResource()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.azureAuthorizationSystemResource".casefold():
            from .azure_authorization_system_resource import AzureAuthorizationSystemResource

            return AzureAuthorizationSystemResource()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.gcpAuthorizationSystemResource".casefold():
            from .gcp_authorization_system_resource import GcpAuthorizationSystemResource

            return GcpAuthorizationSystemResource()
        return AuthorizationSystemResource()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .authorization_system import AuthorizationSystem
        from .aws_authorization_system_resource import AwsAuthorizationSystemResource
        from .azure_authorization_system_resource import AzureAuthorizationSystemResource
        from .entity import Entity
        from .gcp_authorization_system_resource import GcpAuthorizationSystemResource

        from .authorization_system import AuthorizationSystem
        from .aws_authorization_system_resource import AwsAuthorizationSystemResource
        from .azure_authorization_system_resource import AzureAuthorizationSystemResource
        from .entity import Entity
        from .gcp_authorization_system_resource import GcpAuthorizationSystemResource

        fields: Dict[str, Callable[[Any], None]] = {
            "authorizationSystem": lambda n : setattr(self, 'authorization_system', n.get_object_value(AuthorizationSystem)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "externalId": lambda n : setattr(self, 'external_id', n.get_str_value()),
            "resourceType": lambda n : setattr(self, 'resource_type', n.get_str_value()),
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
        writer.write_object_value("authorizationSystem", self.authorization_system)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("externalId", self.external_id)
        writer.write_str_value("resourceType", self.resource_type)
    

