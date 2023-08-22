from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .multi_tenant_organization_join_request_transition_details import MultiTenantOrganizationJoinRequestTransitionDetails
    from .multi_tenant_organization_member_role import MultiTenantOrganizationMemberRole
    from .multi_tenant_organization_member_state import MultiTenantOrganizationMemberState

from .entity import Entity

@dataclass
class MultiTenantOrganizationJoinRequestRecord(Entity):
    # The addedByTenantId property
    added_by_tenant_id: Optional[str] = None
    # The memberState property
    member_state: Optional[MultiTenantOrganizationMemberState] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The role property
    role: Optional[MultiTenantOrganizationMemberRole] = None
    # The transitionDetails property
    transition_details: Optional[MultiTenantOrganizationJoinRequestTransitionDetails] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MultiTenantOrganizationJoinRequestRecord:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MultiTenantOrganizationJoinRequestRecord
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return MultiTenantOrganizationJoinRequestRecord()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .multi_tenant_organization_join_request_transition_details import MultiTenantOrganizationJoinRequestTransitionDetails
        from .multi_tenant_organization_member_role import MultiTenantOrganizationMemberRole
        from .multi_tenant_organization_member_state import MultiTenantOrganizationMemberState

        from .entity import Entity
        from .multi_tenant_organization_join_request_transition_details import MultiTenantOrganizationJoinRequestTransitionDetails
        from .multi_tenant_organization_member_role import MultiTenantOrganizationMemberRole
        from .multi_tenant_organization_member_state import MultiTenantOrganizationMemberState

        fields: Dict[str, Callable[[Any], None]] = {
            "addedByTenantId": lambda n : setattr(self, 'added_by_tenant_id', n.get_str_value()),
            "memberState": lambda n : setattr(self, 'member_state', n.get_enum_value(MultiTenantOrganizationMemberState)),
            "role": lambda n : setattr(self, 'role', n.get_enum_value(MultiTenantOrganizationMemberRole)),
            "transitionDetails": lambda n : setattr(self, 'transition_details', n.get_object_value(MultiTenantOrganizationJoinRequestTransitionDetails)),
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
        writer.write_str_value("addedByTenantId", self.added_by_tenant_id)
        writer.write_enum_value("memberState", self.member_state)
        writer.write_enum_value("role", self.role)
        writer.write_object_value("transitionDetails", self.transition_details)
    

