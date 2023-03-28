from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, invalid_license_alert_configuration, no_mfa_on_role_activation_alert_configuration, redundant_assignment_alert_configuration, roles_assigned_outside_privileged_identity_management_alert_configuration, sequential_activation_renewals_alert_configuration, stale_sign_in_alert_configuration, too_many_global_admins_assigned_to_tenant_alert_configuration, unified_role_management_alert_definition

from . import entity

class UnifiedRoleManagementAlertConfiguration(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new unifiedRoleManagementAlertConfiguration and sets the default values.
        """
        super().__init__()
        # The alertDefinition property
        self._alert_definition: Optional[unified_role_management_alert_definition.UnifiedRoleManagementAlertDefinition] = None
        # The alertDefinitionId property
        self._alert_definition_id: Optional[str] = None
        # The isEnabled property
        self._is_enabled: Optional[bool] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The scopeId property
        self._scope_id: Optional[str] = None
        # The scopeType property
        self._scope_type: Optional[str] = None
    
    @property
    def alert_definition(self,) -> Optional[unified_role_management_alert_definition.UnifiedRoleManagementAlertDefinition]:
        """
        Gets the alertDefinition property value. The alertDefinition property
        Returns: Optional[unified_role_management_alert_definition.UnifiedRoleManagementAlertDefinition]
        """
        return self._alert_definition
    
    @alert_definition.setter
    def alert_definition(self,value: Optional[unified_role_management_alert_definition.UnifiedRoleManagementAlertDefinition] = None) -> None:
        """
        Sets the alertDefinition property value. The alertDefinition property
        Args:
            value: Value to set for the alert_definition property.
        """
        self._alert_definition = value
    
    @property
    def alert_definition_id(self,) -> Optional[str]:
        """
        Gets the alertDefinitionId property value. The alertDefinitionId property
        Returns: Optional[str]
        """
        return self._alert_definition_id
    
    @alert_definition_id.setter
    def alert_definition_id(self,value: Optional[str] = None) -> None:
        """
        Sets the alertDefinitionId property value. The alertDefinitionId property
        Args:
            value: Value to set for the alert_definition_id property.
        """
        self._alert_definition_id = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UnifiedRoleManagementAlertConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UnifiedRoleManagementAlertConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.invalidLicenseAlertConfiguration":
                from . import invalid_license_alert_configuration

                return invalid_license_alert_configuration.InvalidLicenseAlertConfiguration()
            if mapping_value == "#microsoft.graph.noMfaOnRoleActivationAlertConfiguration":
                from . import no_mfa_on_role_activation_alert_configuration

                return no_mfa_on_role_activation_alert_configuration.NoMfaOnRoleActivationAlertConfiguration()
            if mapping_value == "#microsoft.graph.redundantAssignmentAlertConfiguration":
                from . import redundant_assignment_alert_configuration

                return redundant_assignment_alert_configuration.RedundantAssignmentAlertConfiguration()
            if mapping_value == "#microsoft.graph.rolesAssignedOutsidePrivilegedIdentityManagementAlertConfiguration":
                from . import roles_assigned_outside_privileged_identity_management_alert_configuration

                return roles_assigned_outside_privileged_identity_management_alert_configuration.RolesAssignedOutsidePrivilegedIdentityManagementAlertConfiguration()
            if mapping_value == "#microsoft.graph.sequentialActivationRenewalsAlertConfiguration":
                from . import sequential_activation_renewals_alert_configuration

                return sequential_activation_renewals_alert_configuration.SequentialActivationRenewalsAlertConfiguration()
            if mapping_value == "#microsoft.graph.staleSignInAlertConfiguration":
                from . import stale_sign_in_alert_configuration

                return stale_sign_in_alert_configuration.StaleSignInAlertConfiguration()
            if mapping_value == "#microsoft.graph.tooManyGlobalAdminsAssignedToTenantAlertConfiguration":
                from . import too_many_global_admins_assigned_to_tenant_alert_configuration

                return too_many_global_admins_assigned_to_tenant_alert_configuration.TooManyGlobalAdminsAssignedToTenantAlertConfiguration()
        return UnifiedRoleManagementAlertConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
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
    
    @property
    def is_enabled(self,) -> Optional[bool]:
        """
        Gets the isEnabled property value. The isEnabled property
        Returns: Optional[bool]
        """
        return self._is_enabled
    
    @is_enabled.setter
    def is_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isEnabled property value. The isEnabled property
        Args:
            value: Value to set for the is_enabled property.
        """
        self._is_enabled = value
    
    @property
    def scope_id(self,) -> Optional[str]:
        """
        Gets the scopeId property value. The scopeId property
        Returns: Optional[str]
        """
        return self._scope_id
    
    @scope_id.setter
    def scope_id(self,value: Optional[str] = None) -> None:
        """
        Sets the scopeId property value. The scopeId property
        Args:
            value: Value to set for the scope_id property.
        """
        self._scope_id = value
    
    @property
    def scope_type(self,) -> Optional[str]:
        """
        Gets the scopeType property value. The scopeType property
        Returns: Optional[str]
        """
        return self._scope_type
    
    @scope_type.setter
    def scope_type(self,value: Optional[str] = None) -> None:
        """
        Sets the scopeType property value. The scopeType property
        Args:
            value: Value to set for the scope_type property.
        """
        self._scope_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("alertDefinition", self.alert_definition)
        writer.write_str_value("alertDefinitionId", self.alert_definition_id)
        writer.write_bool_value("isEnabled", self.is_enabled)
        writer.write_str_value("scopeId", self.scope_id)
        writer.write_str_value("scopeType", self.scope_type)
    

