from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import management_action_deployment_status
    from .. import entity

from .. import entity

@dataclass
class ManagementActionTenantDeploymentStatus(entity.Entity):
    # The OdataType property
    odata_type: Optional[str] = None
    # The collection of deployment status for each instance of a management action. Optional.
    statuses: Optional[List[management_action_deployment_status.ManagementActionDeploymentStatus]] = None
    # The identifier for the tenant group that is associated with the management action. Required. Read-only.
    tenant_group_id: Optional[str] = None
    # The Azure Active Directory tenant identifier for the managed tenant. Required. Read-only.
    tenant_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ManagementActionTenantDeploymentStatus:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ManagementActionTenantDeploymentStatus
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ManagementActionTenantDeploymentStatus()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import management_action_deployment_status
        from .. import entity

        from . import management_action_deployment_status
        from .. import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "statuses": lambda n : setattr(self, 'statuses', n.get_collection_of_object_values(management_action_deployment_status.ManagementActionDeploymentStatus)),
            "tenantGroupId": lambda n : setattr(self, 'tenant_group_id', n.get_str_value()),
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("statuses", self.statuses)
        writer.write_str_value("tenantGroupId", self.tenant_group_id)
        writer.write_str_value("tenantId", self.tenant_id)
    

