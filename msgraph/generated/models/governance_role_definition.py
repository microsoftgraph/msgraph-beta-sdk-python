from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .governance_resource import GovernanceResource
    from .governance_role_setting import GovernanceRoleSetting

from .entity import Entity

@dataclass
class GovernanceRoleDefinition(Entity):
    # The display name of the role definition.
    display_name: Optional[str] = None
    # The external id of the role definition.
    external_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Read-only. The associated resource for the role definition.
    resource: Optional[GovernanceResource] = None
    # Required. The id of the resource associated with the role definition.
    resource_id: Optional[str] = None
    # The associated role setting for the role definition.
    role_setting: Optional[GovernanceRoleSetting] = None
    # The templateId property
    template_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> GovernanceRoleDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: GovernanceRoleDefinition
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return GovernanceRoleDefinition()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .governance_resource import GovernanceResource
        from .governance_role_setting import GovernanceRoleSetting

        from .entity import Entity
        from .governance_resource import GovernanceResource
        from .governance_role_setting import GovernanceRoleSetting

        fields: Dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "externalId": lambda n : setattr(self, 'external_id', n.get_str_value()),
            "resource": lambda n : setattr(self, 'resource', n.get_object_value(GovernanceResource)),
            "resourceId": lambda n : setattr(self, 'resource_id', n.get_str_value()),
            "roleSetting": lambda n : setattr(self, 'role_setting', n.get_object_value(GovernanceRoleSetting)),
            "templateId": lambda n : setattr(self, 'template_id', n.get_str_value()),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("externalId", self.external_id)
        writer.write_object_value("resource", self.resource)
        writer.write_str_value("resourceId", self.resource_id)
        writer.write_object_value("roleSetting", self.role_setting)
        writer.write_str_value("templateId", self.template_id)
    

