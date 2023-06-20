from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, invalid_license_alert_configuration, no_mfa_on_role_activation_alert_configuration, redundant_assignment_alert_configuration, roles_assigned_outside_privileged_identity_management_alert_configuration, sequential_activation_renewals_alert_configuration, stale_sign_in_alert_configuration, too_many_global_admins_assigned_to_tenant_alert_configuration, unified_role_management_alert_definition

from . import entity

@dataclass
class UnifiedRoleManagementAlertConfiguration(entity.Entity):
    # The alertDefinition property
    alert_definition: Optional[unified_role_management_alert_definition.UnifiedRoleManagementAlertDefinition] = None
    # The alertDefinitionId property
    alert_definition_id: Optional[str] = None
    # The isEnabled property
    is_enabled: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The scopeId property
    scope_id: Optional[str] = None
    # The scopeType property
    scope_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UnifiedRoleManagementAlertConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UnifiedRoleManagementAlertConfiguration
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.invalidLicenseAlertConfiguration".casefold():
            from . import invalid_license_alert_configuration

            return invalid_license_alert_configuration.InvalidLicenseAlertConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.noMfaOnRoleActivationAlertConfiguration".casefold():
            from . import no_mfa_on_role_activation_alert_configuration

            return no_mfa_on_role_activation_alert_configuration.NoMfaOnRoleActivationAlertConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.redundantAssignmentAlertConfiguration".casefold():
            from . import redundant_assignment_alert_configuration

            return redundant_assignment_alert_configuration.RedundantAssignmentAlertConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.rolesAssignedOutsidePrivilegedIdentityManagementAlertConfiguration".casefold():
            from . import roles_assigned_outside_privileged_identity_management_alert_configuration

            return roles_assigned_outside_privileged_identity_management_alert_configuration.RolesAssignedOutsidePrivilegedIdentityManagementAlertConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.sequentialActivationRenewalsAlertConfiguration".casefold():
            from . import sequential_activation_renewals_alert_configuration

            return sequential_activation_renewals_alert_configuration.SequentialActivationRenewalsAlertConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.staleSignInAlertConfiguration".casefold():
            from . import stale_sign_in_alert_configuration

            return stale_sign_in_alert_configuration.StaleSignInAlertConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.tooManyGlobalAdminsAssignedToTenantAlertConfiguration".casefold():
            from . import too_many_global_admins_assigned_to_tenant_alert_configuration

            return too_many_global_admins_assigned_to_tenant_alert_configuration.TooManyGlobalAdminsAssignedToTenantAlertConfiguration()
        return UnifiedRoleManagementAlertConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, invalid_license_alert_configuration, no_mfa_on_role_activation_alert_configuration, redundant_assignment_alert_configuration, roles_assigned_outside_privileged_identity_management_alert_configuration, sequential_activation_renewals_alert_configuration, stale_sign_in_alert_configuration, too_many_global_admins_assigned_to_tenant_alert_configuration, unified_role_management_alert_definition

        from . import entity, invalid_license_alert_configuration, no_mfa_on_role_activation_alert_configuration, redundant_assignment_alert_configuration, roles_assigned_outside_privileged_identity_management_alert_configuration, sequential_activation_renewals_alert_configuration, stale_sign_in_alert_configuration, too_many_global_admins_assigned_to_tenant_alert_configuration, unified_role_management_alert_definition

        fields: Dict[str, Callable[[Any], None]] = {
            "alertDefinition": lambda n : setattr(self, 'alert_definition', n.get_object_value(unified_role_management_alert_definition.UnifiedRoleManagementAlertDefinition)),
            "alertDefinitionId": lambda n : setattr(self, 'alert_definition_id', n.get_str_value()),
            "isEnabled": lambda n : setattr(self, 'is_enabled', n.get_bool_value()),
            "scopeId": lambda n : setattr(self, 'scope_id', n.get_str_value()),
            "scopeType": lambda n : setattr(self, 'scope_type', n.get_str_value()),
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
        writer.write_object_value("alertDefinition", self.alert_definition)
        writer.write_str_value("alertDefinitionId", self.alert_definition_id)
        writer.write_bool_value("isEnabled", self.is_enabled)
        writer.write_str_value("scopeId", self.scope_id)
        writer.write_str_value("scopeType", self.scope_type)
    

