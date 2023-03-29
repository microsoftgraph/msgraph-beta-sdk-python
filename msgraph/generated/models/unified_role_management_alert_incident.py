from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, invalid_license_alert_incident, no_mfa_on_role_activation_alert_incident, redundant_assignment_alert_incident, roles_assigned_outside_privileged_identity_management_alert_incident, sequential_activation_renewals_alert_incident, stale_sign_in_alert_incident, too_many_global_admins_assigned_to_tenant_alert_incident

from . import entity

class UnifiedRoleManagementAlertIncident(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new unifiedRoleManagementAlertIncident and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UnifiedRoleManagementAlertIncident:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UnifiedRoleManagementAlertIncident
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.invalidLicenseAlertIncident":
                from . import invalid_license_alert_incident

                return invalid_license_alert_incident.InvalidLicenseAlertIncident()
            if mapping_value == "#microsoft.graph.noMfaOnRoleActivationAlertIncident":
                from . import no_mfa_on_role_activation_alert_incident

                return no_mfa_on_role_activation_alert_incident.NoMfaOnRoleActivationAlertIncident()
            if mapping_value == "#microsoft.graph.redundantAssignmentAlertIncident":
                from . import redundant_assignment_alert_incident

                return redundant_assignment_alert_incident.RedundantAssignmentAlertIncident()
            if mapping_value == "#microsoft.graph.rolesAssignedOutsidePrivilegedIdentityManagementAlertIncident":
                from . import roles_assigned_outside_privileged_identity_management_alert_incident

                return roles_assigned_outside_privileged_identity_management_alert_incident.RolesAssignedOutsidePrivilegedIdentityManagementAlertIncident()
            if mapping_value == "#microsoft.graph.sequentialActivationRenewalsAlertIncident":
                from . import sequential_activation_renewals_alert_incident

                return sequential_activation_renewals_alert_incident.SequentialActivationRenewalsAlertIncident()
            if mapping_value == "#microsoft.graph.staleSignInAlertIncident":
                from . import stale_sign_in_alert_incident

                return stale_sign_in_alert_incident.StaleSignInAlertIncident()
            if mapping_value == "#microsoft.graph.tooManyGlobalAdminsAssignedToTenantAlertIncident":
                from . import too_many_global_admins_assigned_to_tenant_alert_incident

                return too_many_global_admins_assigned_to_tenant_alert_incident.TooManyGlobalAdminsAssignedToTenantAlertIncident()
        return UnifiedRoleManagementAlertIncident()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, invalid_license_alert_incident, no_mfa_on_role_activation_alert_incident, redundant_assignment_alert_incident, roles_assigned_outside_privileged_identity_management_alert_incident, sequential_activation_renewals_alert_incident, stale_sign_in_alert_incident, too_many_global_admins_assigned_to_tenant_alert_incident

        fields: Dict[str, Callable[[Any], None]] = {
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
    

