from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import app_role_assignment, assigned_label, assigned_license, calendar, conversation, conversation_thread, directory_object, directory_setting, drive, endpoint, event, extension, group_access_type, group_lifecycle_policy, group_writeback_configuration, license_processing_state, membership_rule_processing_status, onenote, on_premises_provisioning_error, planner_group, profile_photo, resource_specific_permission_grant, site, team

from . import directory_object

class Group(directory_object.DirectoryObject):
    def __init__(self,) -> None:
        """
        Instantiates a new group and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.group"
        # The list of users or groups that are allowed to create post's or calendar events in this group. If this list is non-empty then only users or groups listed here are allowed to post.
        self._accepted_senders: Optional[List[directory_object.DirectoryObject]] = None
        # The accessType property
        self._access_type: Optional[group_access_type.GroupAccessType] = None
        # Indicates if people external to the organization can send messages to the group. Default value is false. Returned only on $select. Supported only on the Get group API (GET /groups/{ID}).
        self._allow_external_senders: Optional[bool] = None
        # Represents the app roles a group has been granted for an application. Supports $expand.
        self._app_role_assignments: Optional[List[app_role_assignment.AppRoleAssignment]] = None
        # The list of sensitivity label pairs (label ID, label name) associated with a Microsoft 365 group. Returned only on $select.
        self._assigned_labels: Optional[List[assigned_label.AssignedLabel]] = None
        # The licenses that are assigned to the group. Returned only on $select. Supports $filter (eq). Read-only.
        self._assigned_licenses: Optional[List[assigned_license.AssignedLicense]] = None
        # Indicates if new members added to the group will be auto-subscribed to receive email notifications. You can set this property in a PATCH request for the group; do not set it in the initial POST request that creates the group. Default value is false. Returned only on $select. Supported only on the Get group API (GET /groups/{ID}).
        self._auto_subscribe_new_members: Optional[bool] = None
        # The group's calendar. Read-only.
        self._calendar: Optional[calendar.Calendar] = None
        # The calendar view for the calendar. Read-only.
        self._calendar_view: Optional[List[event.Event]] = None
        # Describes a classification for the group (such as low, medium or high business impact). Valid values for this property are defined by creating a ClassificationList setting value, based on the template definition.Returned by default. Supports $filter (eq, ne, not, ge, le, startsWith).
        self._classification: Optional[str] = None
        # The group's conversations.
        self._conversations: Optional[List[conversation.Conversation]] = None
        # App ID of the app used to create the group. Can be null for some groups. Returned by default. Read-only. Supports $filter (eq, ne, not, in, startsWith).
        self._created_by_app_id: Optional[str] = None
        # Timestamp of when the group was created. The value cannot be modified and is automatically populated when the group is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Returned by default. Read-only.
        self._created_date_time: Optional[datetime] = None
        # The user (or application) that created the group. Note: This is not set if the user is an administrator. Read-only.
        self._created_on_behalf_of: Optional[directory_object.DirectoryObject] = None
        # An optional description for the group. Returned by default. Supports $filter (eq, ne, not, ge, le, startsWith) and $search.
        self._description: Optional[str] = None
        # The display name for the group. Required. Maximum length is 256 characters. Returned by default. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values), $search, and $orderBy.
        self._display_name: Optional[str] = None
        # The group's default drive. Read-only.
        self._drive: Optional[drive.Drive] = None
        # The group's drives. Read-only.
        self._drives: Optional[List[drive.Drive]] = None
        # Endpoints for the group. Read-only. Nullable.
        self._endpoints: Optional[List[endpoint.Endpoint]] = None
        # The group's events.
        self._events: Optional[List[event.Event]] = None
        # Timestamp of when the group is set to expire. The value cannot be modified and is automatically populated when the group is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Returned by default. Supports $filter (eq, ne, not, ge, le, in). Read-only.
        self._expiration_date_time: Optional[datetime] = None
        # The collection of open extensions defined for the group. Read-only. Nullable.
        self._extensions: Optional[List[extension.Extension]] = None
        # The collection of lifecycle policies for this group. Read-only. Nullable.
        self._group_lifecycle_policies: Optional[List[group_lifecycle_policy.GroupLifecyclePolicy]] = None
        # Specifies the group type and its membership. If the collection contains Unified, the group is a Microsoft 365 group; otherwise, it's either a security group or distribution group. For details, see groups overview.If the collection includes DynamicMembership, the group has dynamic membership; otherwise, membership is static. Returned by default. Supports $filter (eq, not).
        self._group_types: Optional[List[str]] = None
        # Indicates whether there are members in this group that have license errors from its group-based license assignment. This property is never returned on a GET operation. You can use it as a $filter argument to get groups that have members with license errors (that is, filter for this property being true).  Supports $filter (eq).
        self._has_members_with_license_errors: Optional[bool] = None
        # true if the group is not displayed in certain parts of the Outlook user interface: in the Address Book, in address lists for selecting message recipients, and in the Browse Groups dialog for searching groups; false otherwise. Default value is false. Returned only on $select. Supported only on the Get group API (GET /groups/{ID}).
        self._hide_from_address_lists: Optional[bool] = None
        # true if the group is not displayed in Outlook clients, such as Outlook for Windows and Outlook on the web, false otherwise. Default value is false. Returned only on $select. Supported only on the Get group API (GET /groups/{ID}).
        self._hide_from_outlook_clients: Optional[bool] = None
        # Identifies the info segments assigned to the group. Returned by default. Supports $filter (eq, not, ge, le, startsWith).
        self._info_catalogs: Optional[List[str]] = None
        # When a group is associated with a team, this property determines whether the team is in read-only mode. To read this property, use the /group/{groupId}/team endpoint or the Get team API. To update this property, use the archiveTeam and unarchiveTeam APIs.
        self._is_archived: Optional[bool] = None
        # Indicates whether this group can be assigned to an Azure Active Directory role. Optional. This property can only be set while creating the group and is immutable. If set to true, the securityEnabled property must also be set to true,  visibility must be Hidden, and the group cannot be a dynamic group (that is, groupTypes cannot contain DynamicMembership). Only callers in Global Administrator and Privileged Role Administrator roles can set this property. The caller must also be assigned the RoleManagement.ReadWrite.Directory permission to set this property or update the membership of such groups. For more, see Using a group to manage Azure AD role assignmentsUsing this feature requires a Azure AD Premium P1 license. Returned by default. Supports $filter (eq, ne, not).
        self._is_assignable_to_role: Optional[bool] = None
        # The isFavorite property
        self._is_favorite: Optional[bool] = None
        # The isManagementRestricted property
        self._is_management_restricted: Optional[bool] = None
        # Indicates whether the signed-in user is subscribed to receive email conversations. Default value is true. Returned only on $select. Supported only on the Get group API (GET /groups/{ID}).
        self._is_subscribed_by_mail: Optional[bool] = None
        # Indicates status of the group license assignment to all members of the group. Possible values: QueuedForProcessing, ProcessingInProgress, and ProcessingComplete. Returned only on $select. Read-only.
        self._license_processing_state: Optional[license_processing_state.LicenseProcessingState] = None
        # The SMTP address for the group, for example, 'serviceadmins@contoso.onmicrosoft.com'. Returned by default. Read-only. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).
        self._mail: Optional[str] = None
        # Specifies whether the group is mail-enabled. Required. Returned by default. Supports $filter (eq, ne, not, and eq on null values).
        self._mail_enabled: Optional[bool] = None
        # The mail alias for the group, unique for Microsoft 365 groups in the organization. Maximum length is 64 characters. This property can contain only characters in the ASCII character set 0 - 127 except the following: @ () / [] ' ; : <> , SPACE. Returned by default. Supports $filter (eq, ne, not, ge, le, in, startsWith).
        self._mail_nickname: Optional[str] = None
        # Groups and administrative units that this group is a member of. HTTP Methods: GET (supported for all groups). Read-only. Nullable. Supports $expand.
        self._member_of: Optional[List[directory_object.DirectoryObject]] = None
        # Direct members of this group, who can be users, devices, other groups, or service principals. Supports the List members, Add member, and Remove member operations. Nullable. Supports $expand including nested $select. For example, /groups?$filter=startsWith(displayName,'Role')&$select=id,displayName&$expand=members($select=id,userPrincipalName,displayName).
        self._members: Optional[List[directory_object.DirectoryObject]] = None
        # A list of group members with license errors from this group-based license assignment. Read-only.
        self._members_with_license_errors: Optional[List[directory_object.DirectoryObject]] = None
        # The rule that determines members for this group if the group is a dynamic group (groupTypes contains DynamicMembership). For more information about the syntax of the membership rule, see Membership Rules syntax. Returned by default. Supports $filter (eq, ne, not, ge, le, startsWith).
        self._membership_rule: Optional[str] = None
        # Indicates whether the dynamic membership processing is on or paused. Possible values are On or Paused. Returned by default. Supports $filter (eq, ne, not, in).
        self._membership_rule_processing_state: Optional[str] = None
        # Describes the processing status for rules-based dynamic groups. The property is null for non-rule based dynamic groups or if the dynamic group processing has been paused. Returned only on $select. Supported only on the Get group API (GET /groups/{ID}). Read-only.
        self._membership_rule_processing_status: Optional[membership_rule_processing_status.MembershipRuleProcessingStatus] = None
        # Contains the on-premises domain FQDN, also called dnsDomainName synchronized from the on-premises directory. The property is only populated for customers who are synchronizing their on-premises directory to Azure Active Directory via Azure AD Connect.Returned by default. Read-only.
        self._on_premises_domain_name: Optional[str] = None
        # Indicates the last time at which the group was synced with the on-premises directory.The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Returned by default. Read-only. Supports $filter (eq, ne, not, ge, le, in).
        self._on_premises_last_sync_date_time: Optional[datetime] = None
        # Contains the on-premises netBios name synchronized from the on-premises directory. The property is only populated for customers who are synchronizing their on-premises directory to Azure Active Directory via Azure AD Connect.Returned by default. Read-only.
        self._on_premises_net_bios_name: Optional[str] = None
        # Errors when using Microsoft synchronization product during provisioning. Returned by default. Supports $filter (eq, not).
        self._on_premises_provisioning_errors: Optional[List[on_premises_provisioning_error.OnPremisesProvisioningError]] = None
        # Contains the on-premises SAM account name synchronized from the on-premises directory. The property is only populated for customers who are synchronizing their on-premises directory to Azure Active Directory via Azure AD Connect.Returned by default. Supports $filter (eq, ne, not, ge, le, in, startsWith). Read-only.
        self._on_premises_sam_account_name: Optional[str] = None
        # Contains the on-premises security identifier (SID) for the group that was synchronized from on-premises to the cloud. Returned by default. Supports $filter (eq including on null values). Read-only.
        self._on_premises_security_identifier: Optional[str] = None
        # true if this group is synced from an on-premises directory; false if this group was originally synced from an on-premises directory but is no longer synced; null if this object has never been synced from an on-premises directory (default). Returned by default. Read-only. Supports $filter (eq, ne, not, in, and eq on null values).
        self._on_premises_sync_enabled: Optional[bool] = None
        # The onenote property
        self._onenote: Optional[onenote.Onenote] = None
        # The organizationId property
        self._organization_id: Optional[str] = None
        # The owners of the group who can be users or service principals. Nullable. If this property is not specified when creating a Microsoft 365 group, the calling user is automatically assigned as the group owner.  Supports $filter (/$count eq 0, /$count ne 0, /$count eq 1, /$count ne 1); Supports $expand including nested $select. For example, /groups?$filter=startsWith(displayName,'Role')&$select=id,displayName&$expand=owners($select=id,userPrincipalName,displayName).
        self._owners: Optional[List[directory_object.DirectoryObject]] = None
        # The permissions that have been granted for a group to a specific application. Supports $expand.
        self._permission_grants: Optional[List[resource_specific_permission_grant.ResourceSpecificPermissionGrant]] = None
        # The group's profile photo.
        self._photo: Optional[profile_photo.ProfilePhoto] = None
        # The profile photos owned by the group. Read-only. Nullable.
        self._photos: Optional[List[profile_photo.ProfilePhoto]] = None
        # Selective Planner services available to the group. Read-only. Nullable.
        self._planner: Optional[planner_group.PlannerGroup] = None
        # The preferred data location for the Microsoft 365 group. By default, the group inherits the group creator's preferred data location. To set this property, the calling user must be assigned one of the following Azure AD roles:  Global Administrator  User Account Administrator Directory Writer  Exchange Administrator  SharePoint Administrator  For more information about this property, see OneDrive Online Multi-Geo. Nullable. Returned by default.
        self._preferred_data_location: Optional[str] = None
        # The preferred language for a Microsoft 365 group. Should follow ISO 639-1 Code; for example en-US. Returned by default. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).
        self._preferred_language: Optional[str] = None
        # Email addresses for the group that direct to the same group mailbox. For example: ['SMTP: bob@contoso.com', 'smtp: bob@sales.contoso.com']. The any operator is required for filter expressions on multi-valued properties. Returned by default. Read-only. Not nullable. Supports $filter (eq, not, ge, le, startsWith, endsWith, /$count eq 0, /$count ne 0).
        self._proxy_addresses: Optional[List[str]] = None
        # The list of users or groups that are not allowed to create posts or calendar events in this group. Nullable
        self._rejected_senders: Optional[List[directory_object.DirectoryObject]] = None
        # Timestamp of when the group was last renewed. This cannot be modified directly and is only updated via the renew service action. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Returned by default. Supports $filter (eq, ne, not, ge, le, in). Read-only.
        self._renewed_date_time: Optional[datetime] = None
        # Specifies the group behaviors that can be set for a Microsoft 365 group during creation. This can be set only as part of creation (POST). Possible values are AllowOnlyMembersToPost, HideGroupInOutlook, SubscribeNewGroupMembers, WelcomeEmailDisabled. For more information, see Set Microsoft 365 group behaviors and provisioning options.
        self._resource_behavior_options: Optional[List[str]] = None
        # Specifies the group resources that are provisioned as part of Microsoft 365 group creation, that are not normally part of default group creation. Possible value is Team. For more information, see Set Microsoft 365 group behaviors and provisioning options. Returned by default. Supports $filter (eq, not, startsWith.
        self._resource_provisioning_options: Optional[List[str]] = None
        # Specifies whether the group is a security group. Required.Returned by default. Supports $filter (eq, ne, not, in).
        self._security_enabled: Optional[bool] = None
        # Security identifier of the group, used in Windows scenarios. Returned by default.
        self._security_identifier: Optional[str] = None
        # Settings that can govern this group's behavior, like whether members can invite guest users to the group. Nullable.
        self._settings: Optional[List[directory_setting.DirectorySetting]] = None
        # The list of SharePoint sites in this group. Access the default site with /sites/root.
        self._sites: Optional[List[site.Site]] = None
        # The team associated with this group.
        self._team: Optional[team.Team] = None
        # Specifies a Microsoft 365 group's color theme. Possible values are Teal, Purple, Green, Blue, Pink, Orange or Red. Returned by default.
        self._theme: Optional[str] = None
        # The group's conversation threads. Nullable.
        self._threads: Optional[List[conversation_thread.ConversationThread]] = None
        # The groups that a group is a member of, either directly and through nested membership. Nullable.
        self._transitive_member_of: Optional[List[directory_object.DirectoryObject]] = None
        # The direct and transitive members of a group. Nullable.
        self._transitive_members: Optional[List[directory_object.DirectoryObject]] = None
        # Count of conversations that have been delivered one or more new posts since the signed-in user's last visit to the group. This property is the same as unseenCount. Returned only on $select.
        self._unseen_conversations_count: Optional[int] = None
        # Count of conversations that have received new posts since the signed-in user last visited the group. This property is the same as unseenConversationsCount.Returned only on $select. Supported only on the Get group API (GET /groups/{ID}).
        self._unseen_count: Optional[int] = None
        # Count of new posts that have been delivered to the group's conversations since the signed-in user's last visit to the group. Returned only on $select.
        self._unseen_messages_count: Optional[int] = None
        # Specifies the group join policy and group content visibility for groups. Possible values are: Private, Public, or HiddenMembership. HiddenMembership can be set only for Microsoft 365 groups, when the groups are created. It can't be updated later. Other values of visibility can be updated after group creation. If visibility value is not specified during group creation on Microsoft Graph, a security group is created as Private by default and Microsoft 365 group is Public. Groups assignable to roles are always Private. See group visibility options to learn more. Returned by default. Nullable.
        self._visibility: Optional[str] = None
        # Specifies whether or not a group is configured to write back group object properties to on-premise Active Directory. These properties are used when group writeback is configured in the Azure AD Connect sync client.
        self._writeback_configuration: Optional[group_writeback_configuration.GroupWritebackConfiguration] = None
    
    @property
    def accepted_senders(self,) -> Optional[List[directory_object.DirectoryObject]]:
        """
        Gets the acceptedSenders property value. The list of users or groups that are allowed to create post's or calendar events in this group. If this list is non-empty then only users or groups listed here are allowed to post.
        Returns: Optional[List[directory_object.DirectoryObject]]
        """
        return self._accepted_senders
    
    @accepted_senders.setter
    def accepted_senders(self,value: Optional[List[directory_object.DirectoryObject]] = None) -> None:
        """
        Sets the acceptedSenders property value. The list of users or groups that are allowed to create post's or calendar events in this group. If this list is non-empty then only users or groups listed here are allowed to post.
        Args:
            value: Value to set for the accepted_senders property.
        """
        self._accepted_senders = value
    
    @property
    def access_type(self,) -> Optional[group_access_type.GroupAccessType]:
        """
        Gets the accessType property value. The accessType property
        Returns: Optional[group_access_type.GroupAccessType]
        """
        return self._access_type
    
    @access_type.setter
    def access_type(self,value: Optional[group_access_type.GroupAccessType] = None) -> None:
        """
        Sets the accessType property value. The accessType property
        Args:
            value: Value to set for the access_type property.
        """
        self._access_type = value
    
    @property
    def allow_external_senders(self,) -> Optional[bool]:
        """
        Gets the allowExternalSenders property value. Indicates if people external to the organization can send messages to the group. Default value is false. Returned only on $select. Supported only on the Get group API (GET /groups/{ID}).
        Returns: Optional[bool]
        """
        return self._allow_external_senders
    
    @allow_external_senders.setter
    def allow_external_senders(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowExternalSenders property value. Indicates if people external to the organization can send messages to the group. Default value is false. Returned only on $select. Supported only on the Get group API (GET /groups/{ID}).
        Args:
            value: Value to set for the allow_external_senders property.
        """
        self._allow_external_senders = value
    
    @property
    def app_role_assignments(self,) -> Optional[List[app_role_assignment.AppRoleAssignment]]:
        """
        Gets the appRoleAssignments property value. Represents the app roles a group has been granted for an application. Supports $expand.
        Returns: Optional[List[app_role_assignment.AppRoleAssignment]]
        """
        return self._app_role_assignments
    
    @app_role_assignments.setter
    def app_role_assignments(self,value: Optional[List[app_role_assignment.AppRoleAssignment]] = None) -> None:
        """
        Sets the appRoleAssignments property value. Represents the app roles a group has been granted for an application. Supports $expand.
        Args:
            value: Value to set for the app_role_assignments property.
        """
        self._app_role_assignments = value
    
    @property
    def assigned_labels(self,) -> Optional[List[assigned_label.AssignedLabel]]:
        """
        Gets the assignedLabels property value. The list of sensitivity label pairs (label ID, label name) associated with a Microsoft 365 group. Returned only on $select.
        Returns: Optional[List[assigned_label.AssignedLabel]]
        """
        return self._assigned_labels
    
    @assigned_labels.setter
    def assigned_labels(self,value: Optional[List[assigned_label.AssignedLabel]] = None) -> None:
        """
        Sets the assignedLabels property value. The list of sensitivity label pairs (label ID, label name) associated with a Microsoft 365 group. Returned only on $select.
        Args:
            value: Value to set for the assigned_labels property.
        """
        self._assigned_labels = value
    
    @property
    def assigned_licenses(self,) -> Optional[List[assigned_license.AssignedLicense]]:
        """
        Gets the assignedLicenses property value. The licenses that are assigned to the group. Returned only on $select. Supports $filter (eq). Read-only.
        Returns: Optional[List[assigned_license.AssignedLicense]]
        """
        return self._assigned_licenses
    
    @assigned_licenses.setter
    def assigned_licenses(self,value: Optional[List[assigned_license.AssignedLicense]] = None) -> None:
        """
        Sets the assignedLicenses property value. The licenses that are assigned to the group. Returned only on $select. Supports $filter (eq). Read-only.
        Args:
            value: Value to set for the assigned_licenses property.
        """
        self._assigned_licenses = value
    
    @property
    def auto_subscribe_new_members(self,) -> Optional[bool]:
        """
        Gets the autoSubscribeNewMembers property value. Indicates if new members added to the group will be auto-subscribed to receive email notifications. You can set this property in a PATCH request for the group; do not set it in the initial POST request that creates the group. Default value is false. Returned only on $select. Supported only on the Get group API (GET /groups/{ID}).
        Returns: Optional[bool]
        """
        return self._auto_subscribe_new_members
    
    @auto_subscribe_new_members.setter
    def auto_subscribe_new_members(self,value: Optional[bool] = None) -> None:
        """
        Sets the autoSubscribeNewMembers property value. Indicates if new members added to the group will be auto-subscribed to receive email notifications. You can set this property in a PATCH request for the group; do not set it in the initial POST request that creates the group. Default value is false. Returned only on $select. Supported only on the Get group API (GET /groups/{ID}).
        Args:
            value: Value to set for the auto_subscribe_new_members property.
        """
        self._auto_subscribe_new_members = value
    
    @property
    def calendar(self,) -> Optional[calendar.Calendar]:
        """
        Gets the calendar property value. The group's calendar. Read-only.
        Returns: Optional[calendar.Calendar]
        """
        return self._calendar
    
    @calendar.setter
    def calendar(self,value: Optional[calendar.Calendar] = None) -> None:
        """
        Sets the calendar property value. The group's calendar. Read-only.
        Args:
            value: Value to set for the calendar property.
        """
        self._calendar = value
    
    @property
    def calendar_view(self,) -> Optional[List[event.Event]]:
        """
        Gets the calendarView property value. The calendar view for the calendar. Read-only.
        Returns: Optional[List[event.Event]]
        """
        return self._calendar_view
    
    @calendar_view.setter
    def calendar_view(self,value: Optional[List[event.Event]] = None) -> None:
        """
        Sets the calendarView property value. The calendar view for the calendar. Read-only.
        Args:
            value: Value to set for the calendar_view property.
        """
        self._calendar_view = value
    
    @property
    def classification(self,) -> Optional[str]:
        """
        Gets the classification property value. Describes a classification for the group (such as low, medium or high business impact). Valid values for this property are defined by creating a ClassificationList setting value, based on the template definition.Returned by default. Supports $filter (eq, ne, not, ge, le, startsWith).
        Returns: Optional[str]
        """
        return self._classification
    
    @classification.setter
    def classification(self,value: Optional[str] = None) -> None:
        """
        Sets the classification property value. Describes a classification for the group (such as low, medium or high business impact). Valid values for this property are defined by creating a ClassificationList setting value, based on the template definition.Returned by default. Supports $filter (eq, ne, not, ge, le, startsWith).
        Args:
            value: Value to set for the classification property.
        """
        self._classification = value
    
    @property
    def conversations(self,) -> Optional[List[conversation.Conversation]]:
        """
        Gets the conversations property value. The group's conversations.
        Returns: Optional[List[conversation.Conversation]]
        """
        return self._conversations
    
    @conversations.setter
    def conversations(self,value: Optional[List[conversation.Conversation]] = None) -> None:
        """
        Sets the conversations property value. The group's conversations.
        Args:
            value: Value to set for the conversations property.
        """
        self._conversations = value
    
    @property
    def created_by_app_id(self,) -> Optional[str]:
        """
        Gets the createdByAppId property value. App ID of the app used to create the group. Can be null for some groups. Returned by default. Read-only. Supports $filter (eq, ne, not, in, startsWith).
        Returns: Optional[str]
        """
        return self._created_by_app_id
    
    @created_by_app_id.setter
    def created_by_app_id(self,value: Optional[str] = None) -> None:
        """
        Sets the createdByAppId property value. App ID of the app used to create the group. Can be null for some groups. Returned by default. Read-only. Supports $filter (eq, ne, not, in, startsWith).
        Args:
            value: Value to set for the created_by_app_id property.
        """
        self._created_by_app_id = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. Timestamp of when the group was created. The value cannot be modified and is automatically populated when the group is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Returned by default. Read-only.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. Timestamp of when the group was created. The value cannot be modified and is automatically populated when the group is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Returned by default. Read-only.
        Args:
            value: Value to set for the created_date_time property.
        """
        self._created_date_time = value
    
    @property
    def created_on_behalf_of(self,) -> Optional[directory_object.DirectoryObject]:
        """
        Gets the createdOnBehalfOf property value. The user (or application) that created the group. Note: This is not set if the user is an administrator. Read-only.
        Returns: Optional[directory_object.DirectoryObject]
        """
        return self._created_on_behalf_of
    
    @created_on_behalf_of.setter
    def created_on_behalf_of(self,value: Optional[directory_object.DirectoryObject] = None) -> None:
        """
        Sets the createdOnBehalfOf property value. The user (or application) that created the group. Note: This is not set if the user is an administrator. Read-only.
        Args:
            value: Value to set for the created_on_behalf_of property.
        """
        self._created_on_behalf_of = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Group:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Group
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Group()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. An optional description for the group. Returned by default. Supports $filter (eq, ne, not, ge, le, startsWith) and $search.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. An optional description for the group. Returned by default. Supports $filter (eq, ne, not, ge, le, startsWith) and $search.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The display name for the group. Required. Maximum length is 256 characters. Returned by default. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values), $search, and $orderBy.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display name for the group. Required. Maximum length is 256 characters. Returned by default. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values), $search, and $orderBy.
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    @property
    def drive(self,) -> Optional[drive.Drive]:
        """
        Gets the drive property value. The group's default drive. Read-only.
        Returns: Optional[drive.Drive]
        """
        return self._drive
    
    @drive.setter
    def drive(self,value: Optional[drive.Drive] = None) -> None:
        """
        Sets the drive property value. The group's default drive. Read-only.
        Args:
            value: Value to set for the drive property.
        """
        self._drive = value
    
    @property
    def drives(self,) -> Optional[List[drive.Drive]]:
        """
        Gets the drives property value. The group's drives. Read-only.
        Returns: Optional[List[drive.Drive]]
        """
        return self._drives
    
    @drives.setter
    def drives(self,value: Optional[List[drive.Drive]] = None) -> None:
        """
        Sets the drives property value. The group's drives. Read-only.
        Args:
            value: Value to set for the drives property.
        """
        self._drives = value
    
    @property
    def endpoints(self,) -> Optional[List[endpoint.Endpoint]]:
        """
        Gets the endpoints property value. Endpoints for the group. Read-only. Nullable.
        Returns: Optional[List[endpoint.Endpoint]]
        """
        return self._endpoints
    
    @endpoints.setter
    def endpoints(self,value: Optional[List[endpoint.Endpoint]] = None) -> None:
        """
        Sets the endpoints property value. Endpoints for the group. Read-only. Nullable.
        Args:
            value: Value to set for the endpoints property.
        """
        self._endpoints = value
    
    @property
    def events(self,) -> Optional[List[event.Event]]:
        """
        Gets the events property value. The group's events.
        Returns: Optional[List[event.Event]]
        """
        return self._events
    
    @events.setter
    def events(self,value: Optional[List[event.Event]] = None) -> None:
        """
        Sets the events property value. The group's events.
        Args:
            value: Value to set for the events property.
        """
        self._events = value
    
    @property
    def expiration_date_time(self,) -> Optional[datetime]:
        """
        Gets the expirationDateTime property value. Timestamp of when the group is set to expire. The value cannot be modified and is automatically populated when the group is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Returned by default. Supports $filter (eq, ne, not, ge, le, in). Read-only.
        Returns: Optional[datetime]
        """
        return self._expiration_date_time
    
    @expiration_date_time.setter
    def expiration_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the expirationDateTime property value. Timestamp of when the group is set to expire. The value cannot be modified and is automatically populated when the group is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Returned by default. Supports $filter (eq, ne, not, ge, le, in). Read-only.
        Args:
            value: Value to set for the expiration_date_time property.
        """
        self._expiration_date_time = value
    
    @property
    def extensions(self,) -> Optional[List[extension.Extension]]:
        """
        Gets the extensions property value. The collection of open extensions defined for the group. Read-only. Nullable.
        Returns: Optional[List[extension.Extension]]
        """
        return self._extensions
    
    @extensions.setter
    def extensions(self,value: Optional[List[extension.Extension]] = None) -> None:
        """
        Sets the extensions property value. The collection of open extensions defined for the group. Read-only. Nullable.
        Args:
            value: Value to set for the extensions property.
        """
        self._extensions = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import app_role_assignment, assigned_label, assigned_license, calendar, conversation, conversation_thread, directory_object, directory_setting, drive, endpoint, event, extension, group_access_type, group_lifecycle_policy, group_writeback_configuration, license_processing_state, membership_rule_processing_status, onenote, on_premises_provisioning_error, planner_group, profile_photo, resource_specific_permission_grant, site, team

        fields: Dict[str, Callable[[Any], None]] = {
            "acceptedSenders": lambda n : setattr(self, 'accepted_senders', n.get_collection_of_object_values(directory_object.DirectoryObject)),
            "accessType": lambda n : setattr(self, 'access_type', n.get_enum_value(group_access_type.GroupAccessType)),
            "allowExternalSenders": lambda n : setattr(self, 'allow_external_senders', n.get_bool_value()),
            "appRoleAssignments": lambda n : setattr(self, 'app_role_assignments', n.get_collection_of_object_values(app_role_assignment.AppRoleAssignment)),
            "assignedLabels": lambda n : setattr(self, 'assigned_labels', n.get_collection_of_object_values(assigned_label.AssignedLabel)),
            "assignedLicenses": lambda n : setattr(self, 'assigned_licenses', n.get_collection_of_object_values(assigned_license.AssignedLicense)),
            "autoSubscribeNewMembers": lambda n : setattr(self, 'auto_subscribe_new_members', n.get_bool_value()),
            "calendar": lambda n : setattr(self, 'calendar', n.get_object_value(calendar.Calendar)),
            "calendarView": lambda n : setattr(self, 'calendar_view', n.get_collection_of_object_values(event.Event)),
            "classification": lambda n : setattr(self, 'classification', n.get_str_value()),
            "conversations": lambda n : setattr(self, 'conversations', n.get_collection_of_object_values(conversation.Conversation)),
            "createdByAppId": lambda n : setattr(self, 'created_by_app_id', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "createdOnBehalfOf": lambda n : setattr(self, 'created_on_behalf_of', n.get_object_value(directory_object.DirectoryObject)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "drive": lambda n : setattr(self, 'drive', n.get_object_value(drive.Drive)),
            "drives": lambda n : setattr(self, 'drives', n.get_collection_of_object_values(drive.Drive)),
            "endpoints": lambda n : setattr(self, 'endpoints', n.get_collection_of_object_values(endpoint.Endpoint)),
            "events": lambda n : setattr(self, 'events', n.get_collection_of_object_values(event.Event)),
            "expirationDateTime": lambda n : setattr(self, 'expiration_date_time', n.get_datetime_value()),
            "extensions": lambda n : setattr(self, 'extensions', n.get_collection_of_object_values(extension.Extension)),
            "groupLifecyclePolicies": lambda n : setattr(self, 'group_lifecycle_policies', n.get_collection_of_object_values(group_lifecycle_policy.GroupLifecyclePolicy)),
            "groupTypes": lambda n : setattr(self, 'group_types', n.get_collection_of_primitive_values(str)),
            "hasMembersWithLicenseErrors": lambda n : setattr(self, 'has_members_with_license_errors', n.get_bool_value()),
            "hideFromAddressLists": lambda n : setattr(self, 'hide_from_address_lists', n.get_bool_value()),
            "hideFromOutlookClients": lambda n : setattr(self, 'hide_from_outlook_clients', n.get_bool_value()),
            "infoCatalogs": lambda n : setattr(self, 'info_catalogs', n.get_collection_of_primitive_values(str)),
            "isArchived": lambda n : setattr(self, 'is_archived', n.get_bool_value()),
            "isAssignableToRole": lambda n : setattr(self, 'is_assignable_to_role', n.get_bool_value()),
            "isFavorite": lambda n : setattr(self, 'is_favorite', n.get_bool_value()),
            "isManagementRestricted": lambda n : setattr(self, 'is_management_restricted', n.get_bool_value()),
            "isSubscribedByMail": lambda n : setattr(self, 'is_subscribed_by_mail', n.get_bool_value()),
            "licenseProcessingState": lambda n : setattr(self, 'license_processing_state', n.get_object_value(license_processing_state.LicenseProcessingState)),
            "mail": lambda n : setattr(self, 'mail', n.get_str_value()),
            "mailEnabled": lambda n : setattr(self, 'mail_enabled', n.get_bool_value()),
            "mailNickname": lambda n : setattr(self, 'mail_nickname', n.get_str_value()),
            "members": lambda n : setattr(self, 'members', n.get_collection_of_object_values(directory_object.DirectoryObject)),
            "membershipRule": lambda n : setattr(self, 'membership_rule', n.get_str_value()),
            "membershipRuleProcessingState": lambda n : setattr(self, 'membership_rule_processing_state', n.get_str_value()),
            "membershipRuleProcessingStatus": lambda n : setattr(self, 'membership_rule_processing_status', n.get_object_value(membership_rule_processing_status.MembershipRuleProcessingStatus)),
            "membersWithLicenseErrors": lambda n : setattr(self, 'members_with_license_errors', n.get_collection_of_object_values(directory_object.DirectoryObject)),
            "memberOf": lambda n : setattr(self, 'member_of', n.get_collection_of_object_values(directory_object.DirectoryObject)),
            "onenote": lambda n : setattr(self, 'onenote', n.get_object_value(onenote.Onenote)),
            "onPremisesDomainName": lambda n : setattr(self, 'on_premises_domain_name', n.get_str_value()),
            "onPremisesLastSyncDateTime": lambda n : setattr(self, 'on_premises_last_sync_date_time', n.get_datetime_value()),
            "onPremisesNetBiosName": lambda n : setattr(self, 'on_premises_net_bios_name', n.get_str_value()),
            "onPremisesProvisioningErrors": lambda n : setattr(self, 'on_premises_provisioning_errors', n.get_collection_of_object_values(on_premises_provisioning_error.OnPremisesProvisioningError)),
            "onPremisesSamAccountName": lambda n : setattr(self, 'on_premises_sam_account_name', n.get_str_value()),
            "onPremisesSecurityIdentifier": lambda n : setattr(self, 'on_premises_security_identifier', n.get_str_value()),
            "onPremisesSyncEnabled": lambda n : setattr(self, 'on_premises_sync_enabled', n.get_bool_value()),
            "organizationId": lambda n : setattr(self, 'organization_id', n.get_str_value()),
            "owners": lambda n : setattr(self, 'owners', n.get_collection_of_object_values(directory_object.DirectoryObject)),
            "permissionGrants": lambda n : setattr(self, 'permission_grants', n.get_collection_of_object_values(resource_specific_permission_grant.ResourceSpecificPermissionGrant)),
            "photo": lambda n : setattr(self, 'photo', n.get_object_value(profile_photo.ProfilePhoto)),
            "photos": lambda n : setattr(self, 'photos', n.get_collection_of_object_values(profile_photo.ProfilePhoto)),
            "planner": lambda n : setattr(self, 'planner', n.get_object_value(planner_group.PlannerGroup)),
            "preferredDataLocation": lambda n : setattr(self, 'preferred_data_location', n.get_str_value()),
            "preferredLanguage": lambda n : setattr(self, 'preferred_language', n.get_str_value()),
            "proxyAddresses": lambda n : setattr(self, 'proxy_addresses', n.get_collection_of_primitive_values(str)),
            "rejectedSenders": lambda n : setattr(self, 'rejected_senders', n.get_collection_of_object_values(directory_object.DirectoryObject)),
            "renewedDateTime": lambda n : setattr(self, 'renewed_date_time', n.get_datetime_value()),
            "resourceBehaviorOptions": lambda n : setattr(self, 'resource_behavior_options', n.get_collection_of_primitive_values(str)),
            "resourceProvisioningOptions": lambda n : setattr(self, 'resource_provisioning_options', n.get_collection_of_primitive_values(str)),
            "securityEnabled": lambda n : setattr(self, 'security_enabled', n.get_bool_value()),
            "securityIdentifier": lambda n : setattr(self, 'security_identifier', n.get_str_value()),
            "settings": lambda n : setattr(self, 'settings', n.get_collection_of_object_values(directory_setting.DirectorySetting)),
            "sites": lambda n : setattr(self, 'sites', n.get_collection_of_object_values(site.Site)),
            "team": lambda n : setattr(self, 'team', n.get_object_value(team.Team)),
            "theme": lambda n : setattr(self, 'theme', n.get_str_value()),
            "threads": lambda n : setattr(self, 'threads', n.get_collection_of_object_values(conversation_thread.ConversationThread)),
            "transitiveMembers": lambda n : setattr(self, 'transitive_members', n.get_collection_of_object_values(directory_object.DirectoryObject)),
            "transitiveMemberOf": lambda n : setattr(self, 'transitive_member_of', n.get_collection_of_object_values(directory_object.DirectoryObject)),
            "unseenConversationsCount": lambda n : setattr(self, 'unseen_conversations_count', n.get_int_value()),
            "unseenCount": lambda n : setattr(self, 'unseen_count', n.get_int_value()),
            "unseenMessagesCount": lambda n : setattr(self, 'unseen_messages_count', n.get_int_value()),
            "visibility": lambda n : setattr(self, 'visibility', n.get_str_value()),
            "writebackConfiguration": lambda n : setattr(self, 'writeback_configuration', n.get_object_value(group_writeback_configuration.GroupWritebackConfiguration)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def group_lifecycle_policies(self,) -> Optional[List[group_lifecycle_policy.GroupLifecyclePolicy]]:
        """
        Gets the groupLifecyclePolicies property value. The collection of lifecycle policies for this group. Read-only. Nullable.
        Returns: Optional[List[group_lifecycle_policy.GroupLifecyclePolicy]]
        """
        return self._group_lifecycle_policies
    
    @group_lifecycle_policies.setter
    def group_lifecycle_policies(self,value: Optional[List[group_lifecycle_policy.GroupLifecyclePolicy]] = None) -> None:
        """
        Sets the groupLifecyclePolicies property value. The collection of lifecycle policies for this group. Read-only. Nullable.
        Args:
            value: Value to set for the group_lifecycle_policies property.
        """
        self._group_lifecycle_policies = value
    
    @property
    def group_types(self,) -> Optional[List[str]]:
        """
        Gets the groupTypes property value. Specifies the group type and its membership. If the collection contains Unified, the group is a Microsoft 365 group; otherwise, it's either a security group or distribution group. For details, see groups overview.If the collection includes DynamicMembership, the group has dynamic membership; otherwise, membership is static. Returned by default. Supports $filter (eq, not).
        Returns: Optional[List[str]]
        """
        return self._group_types
    
    @group_types.setter
    def group_types(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the groupTypes property value. Specifies the group type and its membership. If the collection contains Unified, the group is a Microsoft 365 group; otherwise, it's either a security group or distribution group. For details, see groups overview.If the collection includes DynamicMembership, the group has dynamic membership; otherwise, membership is static. Returned by default. Supports $filter (eq, not).
        Args:
            value: Value to set for the group_types property.
        """
        self._group_types = value
    
    @property
    def has_members_with_license_errors(self,) -> Optional[bool]:
        """
        Gets the hasMembersWithLicenseErrors property value. Indicates whether there are members in this group that have license errors from its group-based license assignment. This property is never returned on a GET operation. You can use it as a $filter argument to get groups that have members with license errors (that is, filter for this property being true).  Supports $filter (eq).
        Returns: Optional[bool]
        """
        return self._has_members_with_license_errors
    
    @has_members_with_license_errors.setter
    def has_members_with_license_errors(self,value: Optional[bool] = None) -> None:
        """
        Sets the hasMembersWithLicenseErrors property value. Indicates whether there are members in this group that have license errors from its group-based license assignment. This property is never returned on a GET operation. You can use it as a $filter argument to get groups that have members with license errors (that is, filter for this property being true).  Supports $filter (eq).
        Args:
            value: Value to set for the has_members_with_license_errors property.
        """
        self._has_members_with_license_errors = value
    
    @property
    def hide_from_address_lists(self,) -> Optional[bool]:
        """
        Gets the hideFromAddressLists property value. true if the group is not displayed in certain parts of the Outlook user interface: in the Address Book, in address lists for selecting message recipients, and in the Browse Groups dialog for searching groups; false otherwise. Default value is false. Returned only on $select. Supported only on the Get group API (GET /groups/{ID}).
        Returns: Optional[bool]
        """
        return self._hide_from_address_lists
    
    @hide_from_address_lists.setter
    def hide_from_address_lists(self,value: Optional[bool] = None) -> None:
        """
        Sets the hideFromAddressLists property value. true if the group is not displayed in certain parts of the Outlook user interface: in the Address Book, in address lists for selecting message recipients, and in the Browse Groups dialog for searching groups; false otherwise. Default value is false. Returned only on $select. Supported only on the Get group API (GET /groups/{ID}).
        Args:
            value: Value to set for the hide_from_address_lists property.
        """
        self._hide_from_address_lists = value
    
    @property
    def hide_from_outlook_clients(self,) -> Optional[bool]:
        """
        Gets the hideFromOutlookClients property value. true if the group is not displayed in Outlook clients, such as Outlook for Windows and Outlook on the web, false otherwise. Default value is false. Returned only on $select. Supported only on the Get group API (GET /groups/{ID}).
        Returns: Optional[bool]
        """
        return self._hide_from_outlook_clients
    
    @hide_from_outlook_clients.setter
    def hide_from_outlook_clients(self,value: Optional[bool] = None) -> None:
        """
        Sets the hideFromOutlookClients property value. true if the group is not displayed in Outlook clients, such as Outlook for Windows and Outlook on the web, false otherwise. Default value is false. Returned only on $select. Supported only on the Get group API (GET /groups/{ID}).
        Args:
            value: Value to set for the hide_from_outlook_clients property.
        """
        self._hide_from_outlook_clients = value
    
    @property
    def info_catalogs(self,) -> Optional[List[str]]:
        """
        Gets the infoCatalogs property value. Identifies the info segments assigned to the group. Returned by default. Supports $filter (eq, not, ge, le, startsWith).
        Returns: Optional[List[str]]
        """
        return self._info_catalogs
    
    @info_catalogs.setter
    def info_catalogs(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the infoCatalogs property value. Identifies the info segments assigned to the group. Returned by default. Supports $filter (eq, not, ge, le, startsWith).
        Args:
            value: Value to set for the info_catalogs property.
        """
        self._info_catalogs = value
    
    @property
    def is_archived(self,) -> Optional[bool]:
        """
        Gets the isArchived property value. When a group is associated with a team, this property determines whether the team is in read-only mode. To read this property, use the /group/{groupId}/team endpoint or the Get team API. To update this property, use the archiveTeam and unarchiveTeam APIs.
        Returns: Optional[bool]
        """
        return self._is_archived
    
    @is_archived.setter
    def is_archived(self,value: Optional[bool] = None) -> None:
        """
        Sets the isArchived property value. When a group is associated with a team, this property determines whether the team is in read-only mode. To read this property, use the /group/{groupId}/team endpoint or the Get team API. To update this property, use the archiveTeam and unarchiveTeam APIs.
        Args:
            value: Value to set for the is_archived property.
        """
        self._is_archived = value
    
    @property
    def is_assignable_to_role(self,) -> Optional[bool]:
        """
        Gets the isAssignableToRole property value. Indicates whether this group can be assigned to an Azure Active Directory role. Optional. This property can only be set while creating the group and is immutable. If set to true, the securityEnabled property must also be set to true,  visibility must be Hidden, and the group cannot be a dynamic group (that is, groupTypes cannot contain DynamicMembership). Only callers in Global Administrator and Privileged Role Administrator roles can set this property. The caller must also be assigned the RoleManagement.ReadWrite.Directory permission to set this property or update the membership of such groups. For more, see Using a group to manage Azure AD role assignmentsUsing this feature requires a Azure AD Premium P1 license. Returned by default. Supports $filter (eq, ne, not).
        Returns: Optional[bool]
        """
        return self._is_assignable_to_role
    
    @is_assignable_to_role.setter
    def is_assignable_to_role(self,value: Optional[bool] = None) -> None:
        """
        Sets the isAssignableToRole property value. Indicates whether this group can be assigned to an Azure Active Directory role. Optional. This property can only be set while creating the group and is immutable. If set to true, the securityEnabled property must also be set to true,  visibility must be Hidden, and the group cannot be a dynamic group (that is, groupTypes cannot contain DynamicMembership). Only callers in Global Administrator and Privileged Role Administrator roles can set this property. The caller must also be assigned the RoleManagement.ReadWrite.Directory permission to set this property or update the membership of such groups. For more, see Using a group to manage Azure AD role assignmentsUsing this feature requires a Azure AD Premium P1 license. Returned by default. Supports $filter (eq, ne, not).
        Args:
            value: Value to set for the is_assignable_to_role property.
        """
        self._is_assignable_to_role = value
    
    @property
    def is_favorite(self,) -> Optional[bool]:
        """
        Gets the isFavorite property value. The isFavorite property
        Returns: Optional[bool]
        """
        return self._is_favorite
    
    @is_favorite.setter
    def is_favorite(self,value: Optional[bool] = None) -> None:
        """
        Sets the isFavorite property value. The isFavorite property
        Args:
            value: Value to set for the is_favorite property.
        """
        self._is_favorite = value
    
    @property
    def is_management_restricted(self,) -> Optional[bool]:
        """
        Gets the isManagementRestricted property value. The isManagementRestricted property
        Returns: Optional[bool]
        """
        return self._is_management_restricted
    
    @is_management_restricted.setter
    def is_management_restricted(self,value: Optional[bool] = None) -> None:
        """
        Sets the isManagementRestricted property value. The isManagementRestricted property
        Args:
            value: Value to set for the is_management_restricted property.
        """
        self._is_management_restricted = value
    
    @property
    def is_subscribed_by_mail(self,) -> Optional[bool]:
        """
        Gets the isSubscribedByMail property value. Indicates whether the signed-in user is subscribed to receive email conversations. Default value is true. Returned only on $select. Supported only on the Get group API (GET /groups/{ID}).
        Returns: Optional[bool]
        """
        return self._is_subscribed_by_mail
    
    @is_subscribed_by_mail.setter
    def is_subscribed_by_mail(self,value: Optional[bool] = None) -> None:
        """
        Sets the isSubscribedByMail property value. Indicates whether the signed-in user is subscribed to receive email conversations. Default value is true. Returned only on $select. Supported only on the Get group API (GET /groups/{ID}).
        Args:
            value: Value to set for the is_subscribed_by_mail property.
        """
        self._is_subscribed_by_mail = value
    
    @property
    def license_processing_state(self,) -> Optional[license_processing_state.LicenseProcessingState]:
        """
        Gets the licenseProcessingState property value. Indicates status of the group license assignment to all members of the group. Possible values: QueuedForProcessing, ProcessingInProgress, and ProcessingComplete. Returned only on $select. Read-only.
        Returns: Optional[license_processing_state.LicenseProcessingState]
        """
        return self._license_processing_state
    
    @license_processing_state.setter
    def license_processing_state(self,value: Optional[license_processing_state.LicenseProcessingState] = None) -> None:
        """
        Sets the licenseProcessingState property value. Indicates status of the group license assignment to all members of the group. Possible values: QueuedForProcessing, ProcessingInProgress, and ProcessingComplete. Returned only on $select. Read-only.
        Args:
            value: Value to set for the license_processing_state property.
        """
        self._license_processing_state = value
    
    @property
    def mail(self,) -> Optional[str]:
        """
        Gets the mail property value. The SMTP address for the group, for example, 'serviceadmins@contoso.onmicrosoft.com'. Returned by default. Read-only. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).
        Returns: Optional[str]
        """
        return self._mail
    
    @mail.setter
    def mail(self,value: Optional[str] = None) -> None:
        """
        Sets the mail property value. The SMTP address for the group, for example, 'serviceadmins@contoso.onmicrosoft.com'. Returned by default. Read-only. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).
        Args:
            value: Value to set for the mail property.
        """
        self._mail = value
    
    @property
    def mail_enabled(self,) -> Optional[bool]:
        """
        Gets the mailEnabled property value. Specifies whether the group is mail-enabled. Required. Returned by default. Supports $filter (eq, ne, not, and eq on null values).
        Returns: Optional[bool]
        """
        return self._mail_enabled
    
    @mail_enabled.setter
    def mail_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the mailEnabled property value. Specifies whether the group is mail-enabled. Required. Returned by default. Supports $filter (eq, ne, not, and eq on null values).
        Args:
            value: Value to set for the mail_enabled property.
        """
        self._mail_enabled = value
    
    @property
    def mail_nickname(self,) -> Optional[str]:
        """
        Gets the mailNickname property value. The mail alias for the group, unique for Microsoft 365 groups in the organization. Maximum length is 64 characters. This property can contain only characters in the ASCII character set 0 - 127 except the following: @ () / [] ' ; : <> , SPACE. Returned by default. Supports $filter (eq, ne, not, ge, le, in, startsWith).
        Returns: Optional[str]
        """
        return self._mail_nickname
    
    @mail_nickname.setter
    def mail_nickname(self,value: Optional[str] = None) -> None:
        """
        Sets the mailNickname property value. The mail alias for the group, unique for Microsoft 365 groups in the organization. Maximum length is 64 characters. This property can contain only characters in the ASCII character set 0 - 127 except the following: @ () / [] ' ; : <> , SPACE. Returned by default. Supports $filter (eq, ne, not, ge, le, in, startsWith).
        Args:
            value: Value to set for the mail_nickname property.
        """
        self._mail_nickname = value
    
    @property
    def member_of(self,) -> Optional[List[directory_object.DirectoryObject]]:
        """
        Gets the memberOf property value. Groups and administrative units that this group is a member of. HTTP Methods: GET (supported for all groups). Read-only. Nullable. Supports $expand.
        Returns: Optional[List[directory_object.DirectoryObject]]
        """
        return self._member_of
    
    @member_of.setter
    def member_of(self,value: Optional[List[directory_object.DirectoryObject]] = None) -> None:
        """
        Sets the memberOf property value. Groups and administrative units that this group is a member of. HTTP Methods: GET (supported for all groups). Read-only. Nullable. Supports $expand.
        Args:
            value: Value to set for the member_of property.
        """
        self._member_of = value
    
    @property
    def members(self,) -> Optional[List[directory_object.DirectoryObject]]:
        """
        Gets the members property value. Direct members of this group, who can be users, devices, other groups, or service principals. Supports the List members, Add member, and Remove member operations. Nullable. Supports $expand including nested $select. For example, /groups?$filter=startsWith(displayName,'Role')&$select=id,displayName&$expand=members($select=id,userPrincipalName,displayName).
        Returns: Optional[List[directory_object.DirectoryObject]]
        """
        return self._members
    
    @members.setter
    def members(self,value: Optional[List[directory_object.DirectoryObject]] = None) -> None:
        """
        Sets the members property value. Direct members of this group, who can be users, devices, other groups, or service principals. Supports the List members, Add member, and Remove member operations. Nullable. Supports $expand including nested $select. For example, /groups?$filter=startsWith(displayName,'Role')&$select=id,displayName&$expand=members($select=id,userPrincipalName,displayName).
        Args:
            value: Value to set for the members property.
        """
        self._members = value
    
    @property
    def members_with_license_errors(self,) -> Optional[List[directory_object.DirectoryObject]]:
        """
        Gets the membersWithLicenseErrors property value. A list of group members with license errors from this group-based license assignment. Read-only.
        Returns: Optional[List[directory_object.DirectoryObject]]
        """
        return self._members_with_license_errors
    
    @members_with_license_errors.setter
    def members_with_license_errors(self,value: Optional[List[directory_object.DirectoryObject]] = None) -> None:
        """
        Sets the membersWithLicenseErrors property value. A list of group members with license errors from this group-based license assignment. Read-only.
        Args:
            value: Value to set for the members_with_license_errors property.
        """
        self._members_with_license_errors = value
    
    @property
    def membership_rule(self,) -> Optional[str]:
        """
        Gets the membershipRule property value. The rule that determines members for this group if the group is a dynamic group (groupTypes contains DynamicMembership). For more information about the syntax of the membership rule, see Membership Rules syntax. Returned by default. Supports $filter (eq, ne, not, ge, le, startsWith).
        Returns: Optional[str]
        """
        return self._membership_rule
    
    @membership_rule.setter
    def membership_rule(self,value: Optional[str] = None) -> None:
        """
        Sets the membershipRule property value. The rule that determines members for this group if the group is a dynamic group (groupTypes contains DynamicMembership). For more information about the syntax of the membership rule, see Membership Rules syntax. Returned by default. Supports $filter (eq, ne, not, ge, le, startsWith).
        Args:
            value: Value to set for the membership_rule property.
        """
        self._membership_rule = value
    
    @property
    def membership_rule_processing_state(self,) -> Optional[str]:
        """
        Gets the membershipRuleProcessingState property value. Indicates whether the dynamic membership processing is on or paused. Possible values are On or Paused. Returned by default. Supports $filter (eq, ne, not, in).
        Returns: Optional[str]
        """
        return self._membership_rule_processing_state
    
    @membership_rule_processing_state.setter
    def membership_rule_processing_state(self,value: Optional[str] = None) -> None:
        """
        Sets the membershipRuleProcessingState property value. Indicates whether the dynamic membership processing is on or paused. Possible values are On or Paused. Returned by default. Supports $filter (eq, ne, not, in).
        Args:
            value: Value to set for the membership_rule_processing_state property.
        """
        self._membership_rule_processing_state = value
    
    @property
    def membership_rule_processing_status(self,) -> Optional[membership_rule_processing_status.MembershipRuleProcessingStatus]:
        """
        Gets the membershipRuleProcessingStatus property value. Describes the processing status for rules-based dynamic groups. The property is null for non-rule based dynamic groups or if the dynamic group processing has been paused. Returned only on $select. Supported only on the Get group API (GET /groups/{ID}). Read-only.
        Returns: Optional[membership_rule_processing_status.MembershipRuleProcessingStatus]
        """
        return self._membership_rule_processing_status
    
    @membership_rule_processing_status.setter
    def membership_rule_processing_status(self,value: Optional[membership_rule_processing_status.MembershipRuleProcessingStatus] = None) -> None:
        """
        Sets the membershipRuleProcessingStatus property value. Describes the processing status for rules-based dynamic groups. The property is null for non-rule based dynamic groups or if the dynamic group processing has been paused. Returned only on $select. Supported only on the Get group API (GET /groups/{ID}). Read-only.
        Args:
            value: Value to set for the membership_rule_processing_status property.
        """
        self._membership_rule_processing_status = value
    
    @property
    def on_premises_domain_name(self,) -> Optional[str]:
        """
        Gets the onPremisesDomainName property value. Contains the on-premises domain FQDN, also called dnsDomainName synchronized from the on-premises directory. The property is only populated for customers who are synchronizing their on-premises directory to Azure Active Directory via Azure AD Connect.Returned by default. Read-only.
        Returns: Optional[str]
        """
        return self._on_premises_domain_name
    
    @on_premises_domain_name.setter
    def on_premises_domain_name(self,value: Optional[str] = None) -> None:
        """
        Sets the onPremisesDomainName property value. Contains the on-premises domain FQDN, also called dnsDomainName synchronized from the on-premises directory. The property is only populated for customers who are synchronizing their on-premises directory to Azure Active Directory via Azure AD Connect.Returned by default. Read-only.
        Args:
            value: Value to set for the on_premises_domain_name property.
        """
        self._on_premises_domain_name = value
    
    @property
    def on_premises_last_sync_date_time(self,) -> Optional[datetime]:
        """
        Gets the onPremisesLastSyncDateTime property value. Indicates the last time at which the group was synced with the on-premises directory.The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Returned by default. Read-only. Supports $filter (eq, ne, not, ge, le, in).
        Returns: Optional[datetime]
        """
        return self._on_premises_last_sync_date_time
    
    @on_premises_last_sync_date_time.setter
    def on_premises_last_sync_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the onPremisesLastSyncDateTime property value. Indicates the last time at which the group was synced with the on-premises directory.The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Returned by default. Read-only. Supports $filter (eq, ne, not, ge, le, in).
        Args:
            value: Value to set for the on_premises_last_sync_date_time property.
        """
        self._on_premises_last_sync_date_time = value
    
    @property
    def on_premises_net_bios_name(self,) -> Optional[str]:
        """
        Gets the onPremisesNetBiosName property value. Contains the on-premises netBios name synchronized from the on-premises directory. The property is only populated for customers who are synchronizing their on-premises directory to Azure Active Directory via Azure AD Connect.Returned by default. Read-only.
        Returns: Optional[str]
        """
        return self._on_premises_net_bios_name
    
    @on_premises_net_bios_name.setter
    def on_premises_net_bios_name(self,value: Optional[str] = None) -> None:
        """
        Sets the onPremisesNetBiosName property value. Contains the on-premises netBios name synchronized from the on-premises directory. The property is only populated for customers who are synchronizing their on-premises directory to Azure Active Directory via Azure AD Connect.Returned by default. Read-only.
        Args:
            value: Value to set for the on_premises_net_bios_name property.
        """
        self._on_premises_net_bios_name = value
    
    @property
    def on_premises_provisioning_errors(self,) -> Optional[List[on_premises_provisioning_error.OnPremisesProvisioningError]]:
        """
        Gets the onPremisesProvisioningErrors property value. Errors when using Microsoft synchronization product during provisioning. Returned by default. Supports $filter (eq, not).
        Returns: Optional[List[on_premises_provisioning_error.OnPremisesProvisioningError]]
        """
        return self._on_premises_provisioning_errors
    
    @on_premises_provisioning_errors.setter
    def on_premises_provisioning_errors(self,value: Optional[List[on_premises_provisioning_error.OnPremisesProvisioningError]] = None) -> None:
        """
        Sets the onPremisesProvisioningErrors property value. Errors when using Microsoft synchronization product during provisioning. Returned by default. Supports $filter (eq, not).
        Args:
            value: Value to set for the on_premises_provisioning_errors property.
        """
        self._on_premises_provisioning_errors = value
    
    @property
    def on_premises_sam_account_name(self,) -> Optional[str]:
        """
        Gets the onPremisesSamAccountName property value. Contains the on-premises SAM account name synchronized from the on-premises directory. The property is only populated for customers who are synchronizing their on-premises directory to Azure Active Directory via Azure AD Connect.Returned by default. Supports $filter (eq, ne, not, ge, le, in, startsWith). Read-only.
        Returns: Optional[str]
        """
        return self._on_premises_sam_account_name
    
    @on_premises_sam_account_name.setter
    def on_premises_sam_account_name(self,value: Optional[str] = None) -> None:
        """
        Sets the onPremisesSamAccountName property value. Contains the on-premises SAM account name synchronized from the on-premises directory. The property is only populated for customers who are synchronizing their on-premises directory to Azure Active Directory via Azure AD Connect.Returned by default. Supports $filter (eq, ne, not, ge, le, in, startsWith). Read-only.
        Args:
            value: Value to set for the on_premises_sam_account_name property.
        """
        self._on_premises_sam_account_name = value
    
    @property
    def on_premises_security_identifier(self,) -> Optional[str]:
        """
        Gets the onPremisesSecurityIdentifier property value. Contains the on-premises security identifier (SID) for the group that was synchronized from on-premises to the cloud. Returned by default. Supports $filter (eq including on null values). Read-only.
        Returns: Optional[str]
        """
        return self._on_premises_security_identifier
    
    @on_premises_security_identifier.setter
    def on_premises_security_identifier(self,value: Optional[str] = None) -> None:
        """
        Sets the onPremisesSecurityIdentifier property value. Contains the on-premises security identifier (SID) for the group that was synchronized from on-premises to the cloud. Returned by default. Supports $filter (eq including on null values). Read-only.
        Args:
            value: Value to set for the on_premises_security_identifier property.
        """
        self._on_premises_security_identifier = value
    
    @property
    def on_premises_sync_enabled(self,) -> Optional[bool]:
        """
        Gets the onPremisesSyncEnabled property value. true if this group is synced from an on-premises directory; false if this group was originally synced from an on-premises directory but is no longer synced; null if this object has never been synced from an on-premises directory (default). Returned by default. Read-only. Supports $filter (eq, ne, not, in, and eq on null values).
        Returns: Optional[bool]
        """
        return self._on_premises_sync_enabled
    
    @on_premises_sync_enabled.setter
    def on_premises_sync_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the onPremisesSyncEnabled property value. true if this group is synced from an on-premises directory; false if this group was originally synced from an on-premises directory but is no longer synced; null if this object has never been synced from an on-premises directory (default). Returned by default. Read-only. Supports $filter (eq, ne, not, in, and eq on null values).
        Args:
            value: Value to set for the on_premises_sync_enabled property.
        """
        self._on_premises_sync_enabled = value
    
    @property
    def onenote(self,) -> Optional[onenote.Onenote]:
        """
        Gets the onenote property value. The onenote property
        Returns: Optional[onenote.Onenote]
        """
        return self._onenote
    
    @onenote.setter
    def onenote(self,value: Optional[onenote.Onenote] = None) -> None:
        """
        Sets the onenote property value. The onenote property
        Args:
            value: Value to set for the onenote property.
        """
        self._onenote = value
    
    @property
    def organization_id(self,) -> Optional[str]:
        """
        Gets the organizationId property value. The organizationId property
        Returns: Optional[str]
        """
        return self._organization_id
    
    @organization_id.setter
    def organization_id(self,value: Optional[str] = None) -> None:
        """
        Sets the organizationId property value. The organizationId property
        Args:
            value: Value to set for the organization_id property.
        """
        self._organization_id = value
    
    @property
    def owners(self,) -> Optional[List[directory_object.DirectoryObject]]:
        """
        Gets the owners property value. The owners of the group who can be users or service principals. Nullable. If this property is not specified when creating a Microsoft 365 group, the calling user is automatically assigned as the group owner.  Supports $filter (/$count eq 0, /$count ne 0, /$count eq 1, /$count ne 1); Supports $expand including nested $select. For example, /groups?$filter=startsWith(displayName,'Role')&$select=id,displayName&$expand=owners($select=id,userPrincipalName,displayName).
        Returns: Optional[List[directory_object.DirectoryObject]]
        """
        return self._owners
    
    @owners.setter
    def owners(self,value: Optional[List[directory_object.DirectoryObject]] = None) -> None:
        """
        Sets the owners property value. The owners of the group who can be users or service principals. Nullable. If this property is not specified when creating a Microsoft 365 group, the calling user is automatically assigned as the group owner.  Supports $filter (/$count eq 0, /$count ne 0, /$count eq 1, /$count ne 1); Supports $expand including nested $select. For example, /groups?$filter=startsWith(displayName,'Role')&$select=id,displayName&$expand=owners($select=id,userPrincipalName,displayName).
        Args:
            value: Value to set for the owners property.
        """
        self._owners = value
    
    @property
    def permission_grants(self,) -> Optional[List[resource_specific_permission_grant.ResourceSpecificPermissionGrant]]:
        """
        Gets the permissionGrants property value. The permissions that have been granted for a group to a specific application. Supports $expand.
        Returns: Optional[List[resource_specific_permission_grant.ResourceSpecificPermissionGrant]]
        """
        return self._permission_grants
    
    @permission_grants.setter
    def permission_grants(self,value: Optional[List[resource_specific_permission_grant.ResourceSpecificPermissionGrant]] = None) -> None:
        """
        Sets the permissionGrants property value. The permissions that have been granted for a group to a specific application. Supports $expand.
        Args:
            value: Value to set for the permission_grants property.
        """
        self._permission_grants = value
    
    @property
    def photo(self,) -> Optional[profile_photo.ProfilePhoto]:
        """
        Gets the photo property value. The group's profile photo.
        Returns: Optional[profile_photo.ProfilePhoto]
        """
        return self._photo
    
    @photo.setter
    def photo(self,value: Optional[profile_photo.ProfilePhoto] = None) -> None:
        """
        Sets the photo property value. The group's profile photo.
        Args:
            value: Value to set for the photo property.
        """
        self._photo = value
    
    @property
    def photos(self,) -> Optional[List[profile_photo.ProfilePhoto]]:
        """
        Gets the photos property value. The profile photos owned by the group. Read-only. Nullable.
        Returns: Optional[List[profile_photo.ProfilePhoto]]
        """
        return self._photos
    
    @photos.setter
    def photos(self,value: Optional[List[profile_photo.ProfilePhoto]] = None) -> None:
        """
        Sets the photos property value. The profile photos owned by the group. Read-only. Nullable.
        Args:
            value: Value to set for the photos property.
        """
        self._photos = value
    
    @property
    def planner(self,) -> Optional[planner_group.PlannerGroup]:
        """
        Gets the planner property value. Selective Planner services available to the group. Read-only. Nullable.
        Returns: Optional[planner_group.PlannerGroup]
        """
        return self._planner
    
    @planner.setter
    def planner(self,value: Optional[planner_group.PlannerGroup] = None) -> None:
        """
        Sets the planner property value. Selective Planner services available to the group. Read-only. Nullable.
        Args:
            value: Value to set for the planner property.
        """
        self._planner = value
    
    @property
    def preferred_data_location(self,) -> Optional[str]:
        """
        Gets the preferredDataLocation property value. The preferred data location for the Microsoft 365 group. By default, the group inherits the group creator's preferred data location. To set this property, the calling user must be assigned one of the following Azure AD roles:  Global Administrator  User Account Administrator Directory Writer  Exchange Administrator  SharePoint Administrator  For more information about this property, see OneDrive Online Multi-Geo. Nullable. Returned by default.
        Returns: Optional[str]
        """
        return self._preferred_data_location
    
    @preferred_data_location.setter
    def preferred_data_location(self,value: Optional[str] = None) -> None:
        """
        Sets the preferredDataLocation property value. The preferred data location for the Microsoft 365 group. By default, the group inherits the group creator's preferred data location. To set this property, the calling user must be assigned one of the following Azure AD roles:  Global Administrator  User Account Administrator Directory Writer  Exchange Administrator  SharePoint Administrator  For more information about this property, see OneDrive Online Multi-Geo. Nullable. Returned by default.
        Args:
            value: Value to set for the preferred_data_location property.
        """
        self._preferred_data_location = value
    
    @property
    def preferred_language(self,) -> Optional[str]:
        """
        Gets the preferredLanguage property value. The preferred language for a Microsoft 365 group. Should follow ISO 639-1 Code; for example en-US. Returned by default. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).
        Returns: Optional[str]
        """
        return self._preferred_language
    
    @preferred_language.setter
    def preferred_language(self,value: Optional[str] = None) -> None:
        """
        Sets the preferredLanguage property value. The preferred language for a Microsoft 365 group. Should follow ISO 639-1 Code; for example en-US. Returned by default. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).
        Args:
            value: Value to set for the preferred_language property.
        """
        self._preferred_language = value
    
    @property
    def proxy_addresses(self,) -> Optional[List[str]]:
        """
        Gets the proxyAddresses property value. Email addresses for the group that direct to the same group mailbox. For example: ['SMTP: bob@contoso.com', 'smtp: bob@sales.contoso.com']. The any operator is required for filter expressions on multi-valued properties. Returned by default. Read-only. Not nullable. Supports $filter (eq, not, ge, le, startsWith, endsWith, /$count eq 0, /$count ne 0).
        Returns: Optional[List[str]]
        """
        return self._proxy_addresses
    
    @proxy_addresses.setter
    def proxy_addresses(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the proxyAddresses property value. Email addresses for the group that direct to the same group mailbox. For example: ['SMTP: bob@contoso.com', 'smtp: bob@sales.contoso.com']. The any operator is required for filter expressions on multi-valued properties. Returned by default. Read-only. Not nullable. Supports $filter (eq, not, ge, le, startsWith, endsWith, /$count eq 0, /$count ne 0).
        Args:
            value: Value to set for the proxy_addresses property.
        """
        self._proxy_addresses = value
    
    @property
    def rejected_senders(self,) -> Optional[List[directory_object.DirectoryObject]]:
        """
        Gets the rejectedSenders property value. The list of users or groups that are not allowed to create posts or calendar events in this group. Nullable
        Returns: Optional[List[directory_object.DirectoryObject]]
        """
        return self._rejected_senders
    
    @rejected_senders.setter
    def rejected_senders(self,value: Optional[List[directory_object.DirectoryObject]] = None) -> None:
        """
        Sets the rejectedSenders property value. The list of users or groups that are not allowed to create posts or calendar events in this group. Nullable
        Args:
            value: Value to set for the rejected_senders property.
        """
        self._rejected_senders = value
    
    @property
    def renewed_date_time(self,) -> Optional[datetime]:
        """
        Gets the renewedDateTime property value. Timestamp of when the group was last renewed. This cannot be modified directly and is only updated via the renew service action. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Returned by default. Supports $filter (eq, ne, not, ge, le, in). Read-only.
        Returns: Optional[datetime]
        """
        return self._renewed_date_time
    
    @renewed_date_time.setter
    def renewed_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the renewedDateTime property value. Timestamp of when the group was last renewed. This cannot be modified directly and is only updated via the renew service action. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Returned by default. Supports $filter (eq, ne, not, ge, le, in). Read-only.
        Args:
            value: Value to set for the renewed_date_time property.
        """
        self._renewed_date_time = value
    
    @property
    def resource_behavior_options(self,) -> Optional[List[str]]:
        """
        Gets the resourceBehaviorOptions property value. Specifies the group behaviors that can be set for a Microsoft 365 group during creation. This can be set only as part of creation (POST). Possible values are AllowOnlyMembersToPost, HideGroupInOutlook, SubscribeNewGroupMembers, WelcomeEmailDisabled. For more information, see Set Microsoft 365 group behaviors and provisioning options.
        Returns: Optional[List[str]]
        """
        return self._resource_behavior_options
    
    @resource_behavior_options.setter
    def resource_behavior_options(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the resourceBehaviorOptions property value. Specifies the group behaviors that can be set for a Microsoft 365 group during creation. This can be set only as part of creation (POST). Possible values are AllowOnlyMembersToPost, HideGroupInOutlook, SubscribeNewGroupMembers, WelcomeEmailDisabled. For more information, see Set Microsoft 365 group behaviors and provisioning options.
        Args:
            value: Value to set for the resource_behavior_options property.
        """
        self._resource_behavior_options = value
    
    @property
    def resource_provisioning_options(self,) -> Optional[List[str]]:
        """
        Gets the resourceProvisioningOptions property value. Specifies the group resources that are provisioned as part of Microsoft 365 group creation, that are not normally part of default group creation. Possible value is Team. For more information, see Set Microsoft 365 group behaviors and provisioning options. Returned by default. Supports $filter (eq, not, startsWith.
        Returns: Optional[List[str]]
        """
        return self._resource_provisioning_options
    
    @resource_provisioning_options.setter
    def resource_provisioning_options(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the resourceProvisioningOptions property value. Specifies the group resources that are provisioned as part of Microsoft 365 group creation, that are not normally part of default group creation. Possible value is Team. For more information, see Set Microsoft 365 group behaviors and provisioning options. Returned by default. Supports $filter (eq, not, startsWith.
        Args:
            value: Value to set for the resource_provisioning_options property.
        """
        self._resource_provisioning_options = value
    
    @property
    def security_enabled(self,) -> Optional[bool]:
        """
        Gets the securityEnabled property value. Specifies whether the group is a security group. Required.Returned by default. Supports $filter (eq, ne, not, in).
        Returns: Optional[bool]
        """
        return self._security_enabled
    
    @security_enabled.setter
    def security_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the securityEnabled property value. Specifies whether the group is a security group. Required.Returned by default. Supports $filter (eq, ne, not, in).
        Args:
            value: Value to set for the security_enabled property.
        """
        self._security_enabled = value
    
    @property
    def security_identifier(self,) -> Optional[str]:
        """
        Gets the securityIdentifier property value. Security identifier of the group, used in Windows scenarios. Returned by default.
        Returns: Optional[str]
        """
        return self._security_identifier
    
    @security_identifier.setter
    def security_identifier(self,value: Optional[str] = None) -> None:
        """
        Sets the securityIdentifier property value. Security identifier of the group, used in Windows scenarios. Returned by default.
        Args:
            value: Value to set for the security_identifier property.
        """
        self._security_identifier = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("acceptedSenders", self.accepted_senders)
        writer.write_enum_value("accessType", self.access_type)
        writer.write_bool_value("allowExternalSenders", self.allow_external_senders)
        writer.write_collection_of_object_values("appRoleAssignments", self.app_role_assignments)
        writer.write_collection_of_object_values("assignedLabels", self.assigned_labels)
        writer.write_collection_of_object_values("assignedLicenses", self.assigned_licenses)
        writer.write_bool_value("autoSubscribeNewMembers", self.auto_subscribe_new_members)
        writer.write_object_value("calendar", self.calendar)
        writer.write_collection_of_object_values("calendarView", self.calendar_view)
        writer.write_str_value("classification", self.classification)
        writer.write_collection_of_object_values("conversations", self.conversations)
        writer.write_str_value("createdByAppId", self.created_by_app_id)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("createdOnBehalfOf", self.created_on_behalf_of)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("drive", self.drive)
        writer.write_collection_of_object_values("drives", self.drives)
        writer.write_collection_of_object_values("endpoints", self.endpoints)
        writer.write_collection_of_object_values("events", self.events)
        writer.write_datetime_value("expirationDateTime", self.expiration_date_time)
        writer.write_collection_of_object_values("extensions", self.extensions)
        writer.write_collection_of_object_values("groupLifecyclePolicies", self.group_lifecycle_policies)
        writer.write_collection_of_primitive_values("groupTypes", self.group_types)
        writer.write_bool_value("hasMembersWithLicenseErrors", self.has_members_with_license_errors)
        writer.write_bool_value("hideFromAddressLists", self.hide_from_address_lists)
        writer.write_bool_value("hideFromOutlookClients", self.hide_from_outlook_clients)
        writer.write_collection_of_primitive_values("infoCatalogs", self.info_catalogs)
        writer.write_bool_value("isArchived", self.is_archived)
        writer.write_bool_value("isAssignableToRole", self.is_assignable_to_role)
        writer.write_bool_value("isFavorite", self.is_favorite)
        writer.write_bool_value("isManagementRestricted", self.is_management_restricted)
        writer.write_bool_value("isSubscribedByMail", self.is_subscribed_by_mail)
        writer.write_object_value("licenseProcessingState", self.license_processing_state)
        writer.write_str_value("mail", self.mail)
        writer.write_bool_value("mailEnabled", self.mail_enabled)
        writer.write_str_value("mailNickname", self.mail_nickname)
        writer.write_collection_of_object_values("members", self.members)
        writer.write_str_value("membershipRule", self.membership_rule)
        writer.write_str_value("membershipRuleProcessingState", self.membership_rule_processing_state)
        writer.write_object_value("membershipRuleProcessingStatus", self.membership_rule_processing_status)
        writer.write_collection_of_object_values("membersWithLicenseErrors", self.members_with_license_errors)
        writer.write_collection_of_object_values("memberOf", self.member_of)
        writer.write_object_value("onenote", self.onenote)
        writer.write_str_value("onPremisesDomainName", self.on_premises_domain_name)
        writer.write_datetime_value("onPremisesLastSyncDateTime", self.on_premises_last_sync_date_time)
        writer.write_str_value("onPremisesNetBiosName", self.on_premises_net_bios_name)
        writer.write_collection_of_object_values("onPremisesProvisioningErrors", self.on_premises_provisioning_errors)
        writer.write_str_value("onPremisesSamAccountName", self.on_premises_sam_account_name)
        writer.write_str_value("onPremisesSecurityIdentifier", self.on_premises_security_identifier)
        writer.write_bool_value("onPremisesSyncEnabled", self.on_premises_sync_enabled)
        writer.write_str_value("organizationId", self.organization_id)
        writer.write_collection_of_object_values("owners", self.owners)
        writer.write_collection_of_object_values("permissionGrants", self.permission_grants)
        writer.write_object_value("photo", self.photo)
        writer.write_collection_of_object_values("photos", self.photos)
        writer.write_object_value("planner", self.planner)
        writer.write_str_value("preferredDataLocation", self.preferred_data_location)
        writer.write_str_value("preferredLanguage", self.preferred_language)
        writer.write_collection_of_primitive_values("proxyAddresses", self.proxy_addresses)
        writer.write_collection_of_object_values("rejectedSenders", self.rejected_senders)
        writer.write_datetime_value("renewedDateTime", self.renewed_date_time)
        writer.write_collection_of_primitive_values("resourceBehaviorOptions", self.resource_behavior_options)
        writer.write_collection_of_primitive_values("resourceProvisioningOptions", self.resource_provisioning_options)
        writer.write_bool_value("securityEnabled", self.security_enabled)
        writer.write_str_value("securityIdentifier", self.security_identifier)
        writer.write_collection_of_object_values("settings", self.settings)
        writer.write_collection_of_object_values("sites", self.sites)
        writer.write_object_value("team", self.team)
        writer.write_str_value("theme", self.theme)
        writer.write_collection_of_object_values("threads", self.threads)
        writer.write_collection_of_object_values("transitiveMembers", self.transitive_members)
        writer.write_collection_of_object_values("transitiveMemberOf", self.transitive_member_of)
        writer.write_int_value("unseenConversationsCount", self.unseen_conversations_count)
        writer.write_int_value("unseenCount", self.unseen_count)
        writer.write_int_value("unseenMessagesCount", self.unseen_messages_count)
        writer.write_str_value("visibility", self.visibility)
        writer.write_object_value("writebackConfiguration", self.writeback_configuration)
    
    @property
    def settings(self,) -> Optional[List[directory_setting.DirectorySetting]]:
        """
        Gets the settings property value. Settings that can govern this group's behavior, like whether members can invite guest users to the group. Nullable.
        Returns: Optional[List[directory_setting.DirectorySetting]]
        """
        return self._settings
    
    @settings.setter
    def settings(self,value: Optional[List[directory_setting.DirectorySetting]] = None) -> None:
        """
        Sets the settings property value. Settings that can govern this group's behavior, like whether members can invite guest users to the group. Nullable.
        Args:
            value: Value to set for the settings property.
        """
        self._settings = value
    
    @property
    def sites(self,) -> Optional[List[site.Site]]:
        """
        Gets the sites property value. The list of SharePoint sites in this group. Access the default site with /sites/root.
        Returns: Optional[List[site.Site]]
        """
        return self._sites
    
    @sites.setter
    def sites(self,value: Optional[List[site.Site]] = None) -> None:
        """
        Sets the sites property value. The list of SharePoint sites in this group. Access the default site with /sites/root.
        Args:
            value: Value to set for the sites property.
        """
        self._sites = value
    
    @property
    def team(self,) -> Optional[team.Team]:
        """
        Gets the team property value. The team associated with this group.
        Returns: Optional[team.Team]
        """
        return self._team
    
    @team.setter
    def team(self,value: Optional[team.Team] = None) -> None:
        """
        Sets the team property value. The team associated with this group.
        Args:
            value: Value to set for the team property.
        """
        self._team = value
    
    @property
    def theme(self,) -> Optional[str]:
        """
        Gets the theme property value. Specifies a Microsoft 365 group's color theme. Possible values are Teal, Purple, Green, Blue, Pink, Orange or Red. Returned by default.
        Returns: Optional[str]
        """
        return self._theme
    
    @theme.setter
    def theme(self,value: Optional[str] = None) -> None:
        """
        Sets the theme property value. Specifies a Microsoft 365 group's color theme. Possible values are Teal, Purple, Green, Blue, Pink, Orange or Red. Returned by default.
        Args:
            value: Value to set for the theme property.
        """
        self._theme = value
    
    @property
    def threads(self,) -> Optional[List[conversation_thread.ConversationThread]]:
        """
        Gets the threads property value. The group's conversation threads. Nullable.
        Returns: Optional[List[conversation_thread.ConversationThread]]
        """
        return self._threads
    
    @threads.setter
    def threads(self,value: Optional[List[conversation_thread.ConversationThread]] = None) -> None:
        """
        Sets the threads property value. The group's conversation threads. Nullable.
        Args:
            value: Value to set for the threads property.
        """
        self._threads = value
    
    @property
    def transitive_member_of(self,) -> Optional[List[directory_object.DirectoryObject]]:
        """
        Gets the transitiveMemberOf property value. The groups that a group is a member of, either directly and through nested membership. Nullable.
        Returns: Optional[List[directory_object.DirectoryObject]]
        """
        return self._transitive_member_of
    
    @transitive_member_of.setter
    def transitive_member_of(self,value: Optional[List[directory_object.DirectoryObject]] = None) -> None:
        """
        Sets the transitiveMemberOf property value. The groups that a group is a member of, either directly and through nested membership. Nullable.
        Args:
            value: Value to set for the transitive_member_of property.
        """
        self._transitive_member_of = value
    
    @property
    def transitive_members(self,) -> Optional[List[directory_object.DirectoryObject]]:
        """
        Gets the transitiveMembers property value. The direct and transitive members of a group. Nullable.
        Returns: Optional[List[directory_object.DirectoryObject]]
        """
        return self._transitive_members
    
    @transitive_members.setter
    def transitive_members(self,value: Optional[List[directory_object.DirectoryObject]] = None) -> None:
        """
        Sets the transitiveMembers property value. The direct and transitive members of a group. Nullable.
        Args:
            value: Value to set for the transitive_members property.
        """
        self._transitive_members = value
    
    @property
    def unseen_conversations_count(self,) -> Optional[int]:
        """
        Gets the unseenConversationsCount property value. Count of conversations that have been delivered one or more new posts since the signed-in user's last visit to the group. This property is the same as unseenCount. Returned only on $select.
        Returns: Optional[int]
        """
        return self._unseen_conversations_count
    
    @unseen_conversations_count.setter
    def unseen_conversations_count(self,value: Optional[int] = None) -> None:
        """
        Sets the unseenConversationsCount property value. Count of conversations that have been delivered one or more new posts since the signed-in user's last visit to the group. This property is the same as unseenCount. Returned only on $select.
        Args:
            value: Value to set for the unseen_conversations_count property.
        """
        self._unseen_conversations_count = value
    
    @property
    def unseen_count(self,) -> Optional[int]:
        """
        Gets the unseenCount property value. Count of conversations that have received new posts since the signed-in user last visited the group. This property is the same as unseenConversationsCount.Returned only on $select. Supported only on the Get group API (GET /groups/{ID}).
        Returns: Optional[int]
        """
        return self._unseen_count
    
    @unseen_count.setter
    def unseen_count(self,value: Optional[int] = None) -> None:
        """
        Sets the unseenCount property value. Count of conversations that have received new posts since the signed-in user last visited the group. This property is the same as unseenConversationsCount.Returned only on $select. Supported only on the Get group API (GET /groups/{ID}).
        Args:
            value: Value to set for the unseen_count property.
        """
        self._unseen_count = value
    
    @property
    def unseen_messages_count(self,) -> Optional[int]:
        """
        Gets the unseenMessagesCount property value. Count of new posts that have been delivered to the group's conversations since the signed-in user's last visit to the group. Returned only on $select.
        Returns: Optional[int]
        """
        return self._unseen_messages_count
    
    @unseen_messages_count.setter
    def unseen_messages_count(self,value: Optional[int] = None) -> None:
        """
        Sets the unseenMessagesCount property value. Count of new posts that have been delivered to the group's conversations since the signed-in user's last visit to the group. Returned only on $select.
        Args:
            value: Value to set for the unseen_messages_count property.
        """
        self._unseen_messages_count = value
    
    @property
    def visibility(self,) -> Optional[str]:
        """
        Gets the visibility property value. Specifies the group join policy and group content visibility for groups. Possible values are: Private, Public, or HiddenMembership. HiddenMembership can be set only for Microsoft 365 groups, when the groups are created. It can't be updated later. Other values of visibility can be updated after group creation. If visibility value is not specified during group creation on Microsoft Graph, a security group is created as Private by default and Microsoft 365 group is Public. Groups assignable to roles are always Private. See group visibility options to learn more. Returned by default. Nullable.
        Returns: Optional[str]
        """
        return self._visibility
    
    @visibility.setter
    def visibility(self,value: Optional[str] = None) -> None:
        """
        Sets the visibility property value. Specifies the group join policy and group content visibility for groups. Possible values are: Private, Public, or HiddenMembership. HiddenMembership can be set only for Microsoft 365 groups, when the groups are created. It can't be updated later. Other values of visibility can be updated after group creation. If visibility value is not specified during group creation on Microsoft Graph, a security group is created as Private by default and Microsoft 365 group is Public. Groups assignable to roles are always Private. See group visibility options to learn more. Returned by default. Nullable.
        Args:
            value: Value to set for the visibility property.
        """
        self._visibility = value
    
    @property
    def writeback_configuration(self,) -> Optional[group_writeback_configuration.GroupWritebackConfiguration]:
        """
        Gets the writebackConfiguration property value. Specifies whether or not a group is configured to write back group object properties to on-premise Active Directory. These properties are used when group writeback is configured in the Azure AD Connect sync client.
        Returns: Optional[group_writeback_configuration.GroupWritebackConfiguration]
        """
        return self._writeback_configuration
    
    @writeback_configuration.setter
    def writeback_configuration(self,value: Optional[group_writeback_configuration.GroupWritebackConfiguration] = None) -> None:
        """
        Sets the writebackConfiguration property value. Specifies whether or not a group is configured to write back group object properties to on-premise Active Directory. These properties are used when group writeback is configured in the Azure AD Connect sync client.
        Args:
            value: Value to set for the writeback_configuration property.
        """
        self._writeback_configuration = value
    

