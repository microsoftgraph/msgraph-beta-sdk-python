from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from . import allow_invites_from, default_user_role_override, default_user_role_permissions, policy_base

from . import policy_base

class AuthorizationPolicy(policy_base.PolicyBase):
    def __init__(self,) -> None:
        """
        Instantiates a new AuthorizationPolicy and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.authorizationPolicy"
        # Indicates whether a user can join the tenant by email validation.
        self._allow_email_verified_users_to_join_organization: Optional[bool] = None
        # Indicates who can invite external users to the organization. Possible values are: none, adminsAndGuestInviters, adminsGuestInvitersAndAllMembers, everyone. everyone is the default setting for all cloud environments except US Government. See more in the table below.
        self._allow_invites_from: Optional[allow_invites_from.AllowInvitesFrom] = None
        # Indicates whether user consent for risky apps is allowed. We recommend to keep this as false.
        self._allow_user_consent_for_risky_apps: Optional[bool] = None
        # Indicates whether users can sign up for email based subscriptions.
        self._allowed_to_sign_up_email_based_subscriptions: Optional[bool] = None
        # Indicates whether the Self-Serve Password Reset feature can be used by users on the tenant.
        self._allowed_to_use_s_s_p_r: Optional[bool] = None
        # To disable the use of the MSOnline PowerShell module set this property to true. This will also disable user-based access to the legacy service endpoint used by the MSOnline PowerShell module. This does not affect Azure AD Connect or Microsoft Graph.
        self._block_msol_power_shell: Optional[bool] = None
        # The defaultUserRoleOverrides property
        self._default_user_role_overrides: Optional[List[default_user_role_override.DefaultUserRoleOverride]] = None
        # The defaultUserRolePermissions property
        self._default_user_role_permissions: Optional[default_user_role_permissions.DefaultUserRolePermissions] = None
        # List of features enabled for private preview on the tenant.
        self._enabled_preview_features: Optional[List[str]] = None
        # Represents role templateId for the role that should be granted to guest user. Refer to List unifiedRoleDefinitions to find the list of available role templates. Currently following roles are supported:  User (a0b1b346-4d3e-4e8b-98f8-753987be4970), Guest User (10dae51f-b6af-4016-8d66-8c2a99b929b3), and Restricted Guest User (2af84b1e-32c8-42b7-82bc-daa82404023b).
        self._guest_user_role_id: Optional[UUID] = None
        # Indicates if user consent to apps is allowed, and if it is, which app consent policy (permissionGrantPolicy) governs the permission for users to grant consent. Values should be in the format managePermissionGrantsForSelf.{id}, where {id} is the id of a built-in or custom app consent policy. An empty list indicates user consent to apps is disabled.
        self._permission_grant_policy_ids_assigned_to_default_user_role: Optional[List[str]] = None
    
    @property
    def allow_email_verified_users_to_join_organization(self,) -> Optional[bool]:
        """
        Gets the allowEmailVerifiedUsersToJoinOrganization property value. Indicates whether a user can join the tenant by email validation.
        Returns: Optional[bool]
        """
        return self._allow_email_verified_users_to_join_organization
    
    @allow_email_verified_users_to_join_organization.setter
    def allow_email_verified_users_to_join_organization(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowEmailVerifiedUsersToJoinOrganization property value. Indicates whether a user can join the tenant by email validation.
        Args:
            value: Value to set for the allow_email_verified_users_to_join_organization property.
        """
        self._allow_email_verified_users_to_join_organization = value
    
    @property
    def allow_invites_from(self,) -> Optional[allow_invites_from.AllowInvitesFrom]:
        """
        Gets the allowInvitesFrom property value. Indicates who can invite external users to the organization. Possible values are: none, adminsAndGuestInviters, adminsGuestInvitersAndAllMembers, everyone. everyone is the default setting for all cloud environments except US Government. See more in the table below.
        Returns: Optional[allow_invites_from.AllowInvitesFrom]
        """
        return self._allow_invites_from
    
    @allow_invites_from.setter
    def allow_invites_from(self,value: Optional[allow_invites_from.AllowInvitesFrom] = None) -> None:
        """
        Sets the allowInvitesFrom property value. Indicates who can invite external users to the organization. Possible values are: none, adminsAndGuestInviters, adminsGuestInvitersAndAllMembers, everyone. everyone is the default setting for all cloud environments except US Government. See more in the table below.
        Args:
            value: Value to set for the allow_invites_from property.
        """
        self._allow_invites_from = value
    
    @property
    def allow_user_consent_for_risky_apps(self,) -> Optional[bool]:
        """
        Gets the allowUserConsentForRiskyApps property value. Indicates whether user consent for risky apps is allowed. We recommend to keep this as false.
        Returns: Optional[bool]
        """
        return self._allow_user_consent_for_risky_apps
    
    @allow_user_consent_for_risky_apps.setter
    def allow_user_consent_for_risky_apps(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowUserConsentForRiskyApps property value. Indicates whether user consent for risky apps is allowed. We recommend to keep this as false.
        Args:
            value: Value to set for the allow_user_consent_for_risky_apps property.
        """
        self._allow_user_consent_for_risky_apps = value
    
    @property
    def allowed_to_sign_up_email_based_subscriptions(self,) -> Optional[bool]:
        """
        Gets the allowedToSignUpEmailBasedSubscriptions property value. Indicates whether users can sign up for email based subscriptions.
        Returns: Optional[bool]
        """
        return self._allowed_to_sign_up_email_based_subscriptions
    
    @allowed_to_sign_up_email_based_subscriptions.setter
    def allowed_to_sign_up_email_based_subscriptions(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowedToSignUpEmailBasedSubscriptions property value. Indicates whether users can sign up for email based subscriptions.
        Args:
            value: Value to set for the allowed_to_sign_up_email_based_subscriptions property.
        """
        self._allowed_to_sign_up_email_based_subscriptions = value
    
    @property
    def allowed_to_use_s_s_p_r(self,) -> Optional[bool]:
        """
        Gets the allowedToUseSSPR property value. Indicates whether the Self-Serve Password Reset feature can be used by users on the tenant.
        Returns: Optional[bool]
        """
        return self._allowed_to_use_s_s_p_r
    
    @allowed_to_use_s_s_p_r.setter
    def allowed_to_use_s_s_p_r(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowedToUseSSPR property value. Indicates whether the Self-Serve Password Reset feature can be used by users on the tenant.
        Args:
            value: Value to set for the allowed_to_use_s_s_p_r property.
        """
        self._allowed_to_use_s_s_p_r = value
    
    @property
    def block_msol_power_shell(self,) -> Optional[bool]:
        """
        Gets the blockMsolPowerShell property value. To disable the use of the MSOnline PowerShell module set this property to true. This will also disable user-based access to the legacy service endpoint used by the MSOnline PowerShell module. This does not affect Azure AD Connect or Microsoft Graph.
        Returns: Optional[bool]
        """
        return self._block_msol_power_shell
    
    @block_msol_power_shell.setter
    def block_msol_power_shell(self,value: Optional[bool] = None) -> None:
        """
        Sets the blockMsolPowerShell property value. To disable the use of the MSOnline PowerShell module set this property to true. This will also disable user-based access to the legacy service endpoint used by the MSOnline PowerShell module. This does not affect Azure AD Connect or Microsoft Graph.
        Args:
            value: Value to set for the block_msol_power_shell property.
        """
        self._block_msol_power_shell = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AuthorizationPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AuthorizationPolicy
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AuthorizationPolicy()
    
    @property
    def default_user_role_overrides(self,) -> Optional[List[default_user_role_override.DefaultUserRoleOverride]]:
        """
        Gets the defaultUserRoleOverrides property value. The defaultUserRoleOverrides property
        Returns: Optional[List[default_user_role_override.DefaultUserRoleOverride]]
        """
        return self._default_user_role_overrides
    
    @default_user_role_overrides.setter
    def default_user_role_overrides(self,value: Optional[List[default_user_role_override.DefaultUserRoleOverride]] = None) -> None:
        """
        Sets the defaultUserRoleOverrides property value. The defaultUserRoleOverrides property
        Args:
            value: Value to set for the default_user_role_overrides property.
        """
        self._default_user_role_overrides = value
    
    @property
    def default_user_role_permissions(self,) -> Optional[default_user_role_permissions.DefaultUserRolePermissions]:
        """
        Gets the defaultUserRolePermissions property value. The defaultUserRolePermissions property
        Returns: Optional[default_user_role_permissions.DefaultUserRolePermissions]
        """
        return self._default_user_role_permissions
    
    @default_user_role_permissions.setter
    def default_user_role_permissions(self,value: Optional[default_user_role_permissions.DefaultUserRolePermissions] = None) -> None:
        """
        Sets the defaultUserRolePermissions property value. The defaultUserRolePermissions property
        Args:
            value: Value to set for the default_user_role_permissions property.
        """
        self._default_user_role_permissions = value
    
    @property
    def enabled_preview_features(self,) -> Optional[List[str]]:
        """
        Gets the enabledPreviewFeatures property value. List of features enabled for private preview on the tenant.
        Returns: Optional[List[str]]
        """
        return self._enabled_preview_features
    
    @enabled_preview_features.setter
    def enabled_preview_features(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the enabledPreviewFeatures property value. List of features enabled for private preview on the tenant.
        Args:
            value: Value to set for the enabled_preview_features property.
        """
        self._enabled_preview_features = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import allow_invites_from, default_user_role_override, default_user_role_permissions, policy_base

        fields: Dict[str, Callable[[Any], None]] = {
            "allowedToSignUpEmailBasedSubscriptions": lambda n : setattr(self, 'allowed_to_sign_up_email_based_subscriptions', n.get_bool_value()),
            "allowedToUseSSPR": lambda n : setattr(self, 'allowed_to_use_s_s_p_r', n.get_bool_value()),
            "allowEmailVerifiedUsersToJoinOrganization": lambda n : setattr(self, 'allow_email_verified_users_to_join_organization', n.get_bool_value()),
            "allowInvitesFrom": lambda n : setattr(self, 'allow_invites_from', n.get_enum_value(allow_invites_from.AllowInvitesFrom)),
            "allowUserConsentForRiskyApps": lambda n : setattr(self, 'allow_user_consent_for_risky_apps', n.get_bool_value()),
            "blockMsolPowerShell": lambda n : setattr(self, 'block_msol_power_shell', n.get_bool_value()),
            "defaultUserRoleOverrides": lambda n : setattr(self, 'default_user_role_overrides', n.get_collection_of_object_values(default_user_role_override.DefaultUserRoleOverride)),
            "defaultUserRolePermissions": lambda n : setattr(self, 'default_user_role_permissions', n.get_object_value(default_user_role_permissions.DefaultUserRolePermissions)),
            "enabledPreviewFeatures": lambda n : setattr(self, 'enabled_preview_features', n.get_collection_of_primitive_values(str)),
            "guestUserRoleId": lambda n : setattr(self, 'guest_user_role_id', n.get_uuid_value()),
            "permissionGrantPolicyIdsAssignedToDefaultUserRole": lambda n : setattr(self, 'permission_grant_policy_ids_assigned_to_default_user_role', n.get_collection_of_primitive_values(str)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def guest_user_role_id(self,) -> Optional[UUID]:
        """
        Gets the guestUserRoleId property value. Represents role templateId for the role that should be granted to guest user. Refer to List unifiedRoleDefinitions to find the list of available role templates. Currently following roles are supported:  User (a0b1b346-4d3e-4e8b-98f8-753987be4970), Guest User (10dae51f-b6af-4016-8d66-8c2a99b929b3), and Restricted Guest User (2af84b1e-32c8-42b7-82bc-daa82404023b).
        Returns: Optional[UUID]
        """
        return self._guest_user_role_id
    
    @guest_user_role_id.setter
    def guest_user_role_id(self,value: Optional[UUID] = None) -> None:
        """
        Sets the guestUserRoleId property value. Represents role templateId for the role that should be granted to guest user. Refer to List unifiedRoleDefinitions to find the list of available role templates. Currently following roles are supported:  User (a0b1b346-4d3e-4e8b-98f8-753987be4970), Guest User (10dae51f-b6af-4016-8d66-8c2a99b929b3), and Restricted Guest User (2af84b1e-32c8-42b7-82bc-daa82404023b).
        Args:
            value: Value to set for the guest_user_role_id property.
        """
        self._guest_user_role_id = value
    
    @property
    def permission_grant_policy_ids_assigned_to_default_user_role(self,) -> Optional[List[str]]:
        """
        Gets the permissionGrantPolicyIdsAssignedToDefaultUserRole property value. Indicates if user consent to apps is allowed, and if it is, which app consent policy (permissionGrantPolicy) governs the permission for users to grant consent. Values should be in the format managePermissionGrantsForSelf.{id}, where {id} is the id of a built-in or custom app consent policy. An empty list indicates user consent to apps is disabled.
        Returns: Optional[List[str]]
        """
        return self._permission_grant_policy_ids_assigned_to_default_user_role
    
    @permission_grant_policy_ids_assigned_to_default_user_role.setter
    def permission_grant_policy_ids_assigned_to_default_user_role(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the permissionGrantPolicyIdsAssignedToDefaultUserRole property value. Indicates if user consent to apps is allowed, and if it is, which app consent policy (permissionGrantPolicy) governs the permission for users to grant consent. Values should be in the format managePermissionGrantsForSelf.{id}, where {id} is the id of a built-in or custom app consent policy. An empty list indicates user consent to apps is disabled.
        Args:
            value: Value to set for the permission_grant_policy_ids_assigned_to_default_user_role property.
        """
        self._permission_grant_policy_ids_assigned_to_default_user_role = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_bool_value("allowedToSignUpEmailBasedSubscriptions", self.allowed_to_sign_up_email_based_subscriptions)
        writer.write_bool_value("allowedToUseSSPR", self.allowed_to_use_s_s_p_r)
        writer.write_bool_value("allowEmailVerifiedUsersToJoinOrganization", self.allow_email_verified_users_to_join_organization)
        writer.write_enum_value("allowInvitesFrom", self.allow_invites_from)
        writer.write_bool_value("allowUserConsentForRiskyApps", self.allow_user_consent_for_risky_apps)
        writer.write_bool_value("blockMsolPowerShell", self.block_msol_power_shell)
        writer.write_collection_of_object_values("defaultUserRoleOverrides", self.default_user_role_overrides)
        writer.write_object_value("defaultUserRolePermissions", self.default_user_role_permissions)
        writer.write_collection_of_primitive_values("enabledPreviewFeatures", self.enabled_preview_features)
        writer.write_uuid_value("guestUserRoleId", self.guest_user_role_id)
        writer.write_collection_of_primitive_values("permissionGrantPolicyIdsAssignedToDefaultUserRole", self.permission_grant_policy_ids_assigned_to_default_user_role)
    

