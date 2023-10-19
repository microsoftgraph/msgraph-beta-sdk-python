from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authorization_system_identity import AuthorizationSystemIdentity
    from .finding import Finding
    from .identity_details import IdentityDetails
    from .permissions_creep_index import PermissionsCreepIndex
    from .privilege_escalation import PrivilegeEscalation
    from .privilege_escalation_aws_resource_finding import PrivilegeEscalationAwsResourceFinding
    from .privilege_escalation_aws_role_finding import PrivilegeEscalationAwsRoleFinding
    from .privilege_escalation_gcp_service_account_finding import PrivilegeEscalationGcpServiceAccountFinding
    from .privilege_escalation_user_finding import PrivilegeEscalationUserFinding

from .finding import Finding

@dataclass
class PrivilegeEscalationFinding(Finding):
    # The identity property
    identity: Optional[AuthorizationSystemIdentity] = None
    # The identityDetails property
    identity_details: Optional[IdentityDetails] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The permissionsCreepIndex property
    permissions_creep_index: Optional[PermissionsCreepIndex] = None
    # The privilegeEscalationDetails property
    privilege_escalation_details: Optional[List[PrivilegeEscalation]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PrivilegeEscalationFinding:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PrivilegeEscalationFinding
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.privilegeEscalationAwsResourceFinding".casefold():
            from .privilege_escalation_aws_resource_finding import PrivilegeEscalationAwsResourceFinding

            return PrivilegeEscalationAwsResourceFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.privilegeEscalationAwsRoleFinding".casefold():
            from .privilege_escalation_aws_role_finding import PrivilegeEscalationAwsRoleFinding

            return PrivilegeEscalationAwsRoleFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.privilegeEscalationGcpServiceAccountFinding".casefold():
            from .privilege_escalation_gcp_service_account_finding import PrivilegeEscalationGcpServiceAccountFinding

            return PrivilegeEscalationGcpServiceAccountFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.privilegeEscalationUserFinding".casefold():
            from .privilege_escalation_user_finding import PrivilegeEscalationUserFinding

            return PrivilegeEscalationUserFinding()
        return PrivilegeEscalationFinding()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .authorization_system_identity import AuthorizationSystemIdentity
        from .finding import Finding
        from .identity_details import IdentityDetails
        from .permissions_creep_index import PermissionsCreepIndex
        from .privilege_escalation import PrivilegeEscalation
        from .privilege_escalation_aws_resource_finding import PrivilegeEscalationAwsResourceFinding
        from .privilege_escalation_aws_role_finding import PrivilegeEscalationAwsRoleFinding
        from .privilege_escalation_gcp_service_account_finding import PrivilegeEscalationGcpServiceAccountFinding
        from .privilege_escalation_user_finding import PrivilegeEscalationUserFinding

        from .authorization_system_identity import AuthorizationSystemIdentity
        from .finding import Finding
        from .identity_details import IdentityDetails
        from .permissions_creep_index import PermissionsCreepIndex
        from .privilege_escalation import PrivilegeEscalation
        from .privilege_escalation_aws_resource_finding import PrivilegeEscalationAwsResourceFinding
        from .privilege_escalation_aws_role_finding import PrivilegeEscalationAwsRoleFinding
        from .privilege_escalation_gcp_service_account_finding import PrivilegeEscalationGcpServiceAccountFinding
        from .privilege_escalation_user_finding import PrivilegeEscalationUserFinding

        fields: Dict[str, Callable[[Any], None]] = {
            "identity": lambda n : setattr(self, 'identity', n.get_object_value(AuthorizationSystemIdentity)),
            "identityDetails": lambda n : setattr(self, 'identity_details', n.get_object_value(IdentityDetails)),
            "permissionsCreepIndex": lambda n : setattr(self, 'permissions_creep_index', n.get_object_value(PermissionsCreepIndex)),
            "privilegeEscalationDetails": lambda n : setattr(self, 'privilege_escalation_details', n.get_collection_of_object_values(PrivilegeEscalation)),
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
        writer.write_object_value("identity", self.identity)
        writer.write_object_value("identityDetails", self.identity_details)
        writer.write_object_value("permissionsCreepIndex", self.permissions_creep_index)
        writer.write_collection_of_object_values("privilegeEscalationDetails", self.privilege_escalation_details)
    

