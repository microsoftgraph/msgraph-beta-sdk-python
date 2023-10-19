from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .allow_invites_from import AllowInvitesFrom
    from .default_user_role_override import DefaultUserRoleOverride
    from .default_user_role_permissions import DefaultUserRolePermissions
    from .policy_base import PolicyBase

from .policy_base import PolicyBase

@dataclass
class AuthorizationPolicy(PolicyBase):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.authorizationPolicy"
    # Indicates whether a user can join the tenant by email validation.
    allow_email_verified_users_to_join_organization: Optional[bool] = None
    # Indicates who can invite guests to the organization. Possible values are: none, adminsAndGuestInviters, adminsGuestInvitersAndAllMembers, everyone. everyone is the default setting for all cloud environments except US Government. See more in the table below.
    allow_invites_from: Optional[AllowInvitesFrom] = None
    # Indicates whether user consent for risky apps is allowed. Default value is false. We recommend that you keep the value set to false.
    allow_user_consent_for_risky_apps: Optional[bool] = None
    # Indicates whether users can sign up for email based subscriptions.
    allowed_to_sign_up_email_based_subscriptions: Optional[bool] = None
    # Indicates whether the Admin Self-Serve Password Reset feature is enabled on the tenant.
    allowed_to_use_s_s_p_r: Optional[bool] = None
    # To disable the use of the MSOnline PowerShell module set this property to true. This will also disable user-based access to the legacy service endpoint used by the MSOnline PowerShell module. This doesn't affect Microsoft Entra Connect or Microsoft Graph.
    block_msol_power_shell: Optional[bool] = None
    # The defaultUserRoleOverrides property
    default_user_role_overrides: Optional[List[DefaultUserRoleOverride]] = None
    # The defaultUserRolePermissions property
    default_user_role_permissions: Optional[DefaultUserRolePermissions] = None
    # List of features enabled for private preview on the tenant.
    enabled_preview_features: Optional[List[str]] = None
    # Represents role templateId for the role that should be granted to guests. Refer to List unifiedRoleDefinitions to find the list of available role templates. Currently following roles are supported:  User (a0b1b346-4d3e-4e8b-98f8-753987be4970), Guest User (10dae51f-b6af-4016-8d66-8c2a99b929b3), and Restricted Guest User (2af84b1e-32c8-42b7-82bc-daa82404023b).
    guest_user_role_id: Optional[UUID] = None
    # Indicates if user consent to apps is allowed, and if it is, which app consent policy (permissionGrantPolicy) governs the permission for users to grant consent. Values should be in the format managePermissionGrantsForSelf.{id}, where {id} is the id of a built-in or custom app consent policy. An empty list indicates user consent to apps is disabled.
    permission_grant_policy_ids_assigned_to_default_user_role: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AuthorizationPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AuthorizationPolicy
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AuthorizationPolicy()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .allow_invites_from import AllowInvitesFrom
        from .default_user_role_override import DefaultUserRoleOverride
        from .default_user_role_permissions import DefaultUserRolePermissions
        from .policy_base import PolicyBase

        from .allow_invites_from import AllowInvitesFrom
        from .default_user_role_override import DefaultUserRoleOverride
        from .default_user_role_permissions import DefaultUserRolePermissions
        from .policy_base import PolicyBase

        fields: Dict[str, Callable[[Any], None]] = {
            "allowEmailVerifiedUsersToJoinOrganization": lambda n : setattr(self, 'allow_email_verified_users_to_join_organization', n.get_bool_value()),
            "allowInvitesFrom": lambda n : setattr(self, 'allow_invites_from', n.get_enum_value(AllowInvitesFrom)),
            "allowUserConsentForRiskyApps": lambda n : setattr(self, 'allow_user_consent_for_risky_apps', n.get_bool_value()),
            "allowedToSignUpEmailBasedSubscriptions": lambda n : setattr(self, 'allowed_to_sign_up_email_based_subscriptions', n.get_bool_value()),
            "allowedToUseSSPR": lambda n : setattr(self, 'allowed_to_use_s_s_p_r', n.get_bool_value()),
            "blockMsolPowerShell": lambda n : setattr(self, 'block_msol_power_shell', n.get_bool_value()),
            "defaultUserRoleOverrides": lambda n : setattr(self, 'default_user_role_overrides', n.get_collection_of_object_values(DefaultUserRoleOverride)),
            "defaultUserRolePermissions": lambda n : setattr(self, 'default_user_role_permissions', n.get_object_value(DefaultUserRolePermissions)),
            "enabledPreviewFeatures": lambda n : setattr(self, 'enabled_preview_features', n.get_collection_of_primitive_values(str)),
            "guestUserRoleId": lambda n : setattr(self, 'guest_user_role_id', n.get_uuid_value()),
            "permissionGrantPolicyIdsAssignedToDefaultUserRole": lambda n : setattr(self, 'permission_grant_policy_ids_assigned_to_default_user_role', n.get_collection_of_primitive_values(str)),
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
        writer.write_bool_value("allowEmailVerifiedUsersToJoinOrganization", self.allow_email_verified_users_to_join_organization)
        writer.write_enum_value("allowInvitesFrom", self.allow_invites_from)
        writer.write_bool_value("allowUserConsentForRiskyApps", self.allow_user_consent_for_risky_apps)
        writer.write_bool_value("allowedToSignUpEmailBasedSubscriptions", self.allowed_to_sign_up_email_based_subscriptions)
        writer.write_bool_value("allowedToUseSSPR", self.allowed_to_use_s_s_p_r)
        writer.write_bool_value("blockMsolPowerShell", self.block_msol_power_shell)
        writer.write_collection_of_object_values("defaultUserRoleOverrides", self.default_user_role_overrides)
        writer.write_object_value("defaultUserRolePermissions", self.default_user_role_permissions)
        writer.write_collection_of_primitive_values("enabledPreviewFeatures", self.enabled_preview_features)
        writer.write_uuid_value("guestUserRoleId", self.guest_user_role_id)
        writer.write_collection_of_primitive_values("permissionGrantPolicyIdsAssignedToDefaultUserRole", self.permission_grant_policy_ids_assigned_to_default_user_role)
    

