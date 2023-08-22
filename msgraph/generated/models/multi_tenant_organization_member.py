from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .directory_object import DirectoryObject
    from .multi_tenant_organization_member_role import MultiTenantOrganizationMemberRole
    from .multi_tenant_organization_member_state import MultiTenantOrganizationMemberState
    from .multi_tenant_organization_member_transition_details import MultiTenantOrganizationMemberTransitionDetails

from .directory_object import DirectoryObject

@dataclass
class MultiTenantOrganizationMember(DirectoryObject):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.multiTenantOrganizationMember"
    # The addedByTenantId property
    added_by_tenant_id: Optional[UUID] = None
    # The addedDateTime property
    added_date_time: Optional[datetime.datetime] = None
    # The displayName property
    display_name: Optional[str] = None
    # The joinedDateTime property
    joined_date_time: Optional[datetime.datetime] = None
    # The role property
    role: Optional[MultiTenantOrganizationMemberRole] = None
    # The state property
    state: Optional[MultiTenantOrganizationMemberState] = None
    # The tenantId property
    tenant_id: Optional[str] = None
    # The transitionDetails property
    transition_details: Optional[MultiTenantOrganizationMemberTransitionDetails] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MultiTenantOrganizationMember:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MultiTenantOrganizationMember
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return MultiTenantOrganizationMember()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .directory_object import DirectoryObject
        from .multi_tenant_organization_member_role import MultiTenantOrganizationMemberRole
        from .multi_tenant_organization_member_state import MultiTenantOrganizationMemberState
        from .multi_tenant_organization_member_transition_details import MultiTenantOrganizationMemberTransitionDetails

        from .directory_object import DirectoryObject
        from .multi_tenant_organization_member_role import MultiTenantOrganizationMemberRole
        from .multi_tenant_organization_member_state import MultiTenantOrganizationMemberState
        from .multi_tenant_organization_member_transition_details import MultiTenantOrganizationMemberTransitionDetails

        fields: Dict[str, Callable[[Any], None]] = {
            "addedByTenantId": lambda n : setattr(self, 'added_by_tenant_id', n.get_uuid_value()),
            "addedDateTime": lambda n : setattr(self, 'added_date_time', n.get_datetime_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "joinedDateTime": lambda n : setattr(self, 'joined_date_time', n.get_datetime_value()),
            "role": lambda n : setattr(self, 'role', n.get_enum_value(MultiTenantOrganizationMemberRole)),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(MultiTenantOrganizationMemberState)),
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
            "transitionDetails": lambda n : setattr(self, 'transition_details', n.get_object_value(MultiTenantOrganizationMemberTransitionDetails)),
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
        writer.write_uuid_value("addedByTenantId", self.added_by_tenant_id)
        writer.write_datetime_value("addedDateTime", self.added_date_time)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("joinedDateTime", self.joined_date_time)
        writer.write_enum_value("role", self.role)
        writer.write_enum_value("state", self.state)
        writer.write_str_value("tenantId", self.tenant_id)
        writer.write_object_value("transitionDetails", self.transition_details)
    

