from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import channel, conversation_member, entity, group, profile_photo, resource_specific_permission_grant, schedule, teams_app_installation, teams_async_operation, teams_template, teamwork_tag, team_discovery_settings, team_fun_settings, team_guest_settings, team_member_settings, team_messaging_settings, team_specialization, team_summary, team_template_definition, team_visibility_type, user

from . import entity

class Team(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new team and sets the default values.
        """
        super().__init__()
        # List of channels either hosted in or shared with the team (incoming channels).
        self._all_channels: Optional[List[channel.Channel]] = None
        # The collection of channels and messages associated with the team.
        self._channels: Optional[List[channel.Channel]] = None
        # An optional label. Typically describes the data or business sensitivity of the team. Must match one of a pre-configured set in the tenant's directory.
        self._classification: Optional[str] = None
        # Timestamp at which the team was created.
        self._created_date_time: Optional[datetime] = None
        # An optional description for the team. Maximum length: 1024 characters.
        self._description: Optional[str] = None
        # Settings to configure team discoverability by others.
        self._discovery_settings: Optional[team_discovery_settings.TeamDiscoverySettings] = None
        # The name of the team.
        self._display_name: Optional[str] = None
        # Settings to configure use of Giphy, memes, and stickers in the team.
        self._fun_settings: Optional[team_fun_settings.TeamFunSettings] = None
        # The group property
        self._group: Optional[group.Group] = None
        # Settings to configure whether guests can create, update, or delete channels in the team.
        self._guest_settings: Optional[team_guest_settings.TeamGuestSettings] = None
        # List of channels shared with the team.
        self._incoming_channels: Optional[List[channel.Channel]] = None
        # The apps installed in this team.
        self._installed_apps: Optional[List[teams_app_installation.TeamsAppInstallation]] = None
        # A unique ID for the team that has been used in a few places such as the audit log/Office 365 Management Activity API.
        self._internal_id: Optional[str] = None
        # Whether this team is in read-only mode.
        self._is_archived: Optional[bool] = None
        # If set to true, the team is currently in the owner-only team membership state and not accessible by other team members, such as students.
        self._is_membership_limited_to_owners: Optional[bool] = None
        # Settings to configure whether members can perform certain actions, for example, create channels and add bots, in the team.
        self._member_settings: Optional[team_member_settings.TeamMemberSettings] = None
        # Members and owners of the team.
        self._members: Optional[List[conversation_member.ConversationMember]] = None
        # Settings to configure messaging and mentions in the team.
        self._messaging_settings: Optional[team_messaging_settings.TeamMessagingSettings] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The async operations that ran or are running on this team.
        self._operations: Optional[List[teams_async_operation.TeamsAsyncOperation]] = None
        # The list of this team's owners. Currently, when creating a team using application permissions, exactly one owner must be specified. When using user delegated permissions, no owner can be specified (the current user is the owner). Owner must be specified as an object ID (GUID), not a UPN.
        self._owners: Optional[List[user.User]] = None
        # A collection of permissions granted to apps to access the team.
        self._permission_grants: Optional[List[resource_specific_permission_grant.ResourceSpecificPermissionGrant]] = None
        # The team photo.
        self._photo: Optional[profile_photo.ProfilePhoto] = None
        # The general channel for the team.
        self._primary_channel: Optional[channel.Channel] = None
        # The schedule of shifts for this team.
        self._schedule: Optional[schedule.Schedule] = None
        # Optional. Indicates whether the team is intended for a particular use case.  Each team specialization has access to unique behaviors and experiences targeted to its use case.
        self._specialization: Optional[team_specialization.TeamSpecialization] = None
        # Contains summary information about the team, including number of owners, members, and guests.
        self._summary: Optional[team_summary.TeamSummary] = None
        # The tags associated with the team.
        self._tags: Optional[List[teamwork_tag.TeamworkTag]] = None
        # The template this team was created from. See available templates.
        self._template: Optional[teams_template.TeamsTemplate] = None
        # Generic representation of a team template definition for a team with a specific structure and configuration.
        self._template_definition: Optional[team_template_definition.TeamTemplateDefinition] = None
        # The ID of the Azure Active Directory tenant.
        self._tenant_id: Optional[str] = None
        # The visibility of the group and team. Defaults to Public.
        self._visibility: Optional[team_visibility_type.TeamVisibilityType] = None
        # A hyperlink that will go to the team in the Microsoft Teams client. This is the URL that you get when you right-click a team in the Microsoft Teams client and select Get link to team. This URL should be treated as an opaque blob, and not parsed.
        self._web_url: Optional[str] = None
    
    @property
    def all_channels(self,) -> Optional[List[channel.Channel]]:
        """
        Gets the allChannels property value. List of channels either hosted in or shared with the team (incoming channels).
        Returns: Optional[List[channel.Channel]]
        """
        return self._all_channels
    
    @all_channels.setter
    def all_channels(self,value: Optional[List[channel.Channel]] = None) -> None:
        """
        Sets the allChannels property value. List of channels either hosted in or shared with the team (incoming channels).
        Args:
            value: Value to set for the all_channels property.
        """
        self._all_channels = value
    
    @property
    def channels(self,) -> Optional[List[channel.Channel]]:
        """
        Gets the channels property value. The collection of channels and messages associated with the team.
        Returns: Optional[List[channel.Channel]]
        """
        return self._channels
    
    @channels.setter
    def channels(self,value: Optional[List[channel.Channel]] = None) -> None:
        """
        Sets the channels property value. The collection of channels and messages associated with the team.
        Args:
            value: Value to set for the channels property.
        """
        self._channels = value
    
    @property
    def classification(self,) -> Optional[str]:
        """
        Gets the classification property value. An optional label. Typically describes the data or business sensitivity of the team. Must match one of a pre-configured set in the tenant's directory.
        Returns: Optional[str]
        """
        return self._classification
    
    @classification.setter
    def classification(self,value: Optional[str] = None) -> None:
        """
        Sets the classification property value. An optional label. Typically describes the data or business sensitivity of the team. Must match one of a pre-configured set in the tenant's directory.
        Args:
            value: Value to set for the classification property.
        """
        self._classification = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. Timestamp at which the team was created.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. Timestamp at which the team was created.
        Args:
            value: Value to set for the created_date_time property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Team:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Team
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Team()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. An optional description for the team. Maximum length: 1024 characters.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. An optional description for the team. Maximum length: 1024 characters.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def discovery_settings(self,) -> Optional[team_discovery_settings.TeamDiscoverySettings]:
        """
        Gets the discoverySettings property value. Settings to configure team discoverability by others.
        Returns: Optional[team_discovery_settings.TeamDiscoverySettings]
        """
        return self._discovery_settings
    
    @discovery_settings.setter
    def discovery_settings(self,value: Optional[team_discovery_settings.TeamDiscoverySettings] = None) -> None:
        """
        Sets the discoverySettings property value. Settings to configure team discoverability by others.
        Args:
            value: Value to set for the discovery_settings property.
        """
        self._discovery_settings = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The name of the team.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The name of the team.
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    @property
    def fun_settings(self,) -> Optional[team_fun_settings.TeamFunSettings]:
        """
        Gets the funSettings property value. Settings to configure use of Giphy, memes, and stickers in the team.
        Returns: Optional[team_fun_settings.TeamFunSettings]
        """
        return self._fun_settings
    
    @fun_settings.setter
    def fun_settings(self,value: Optional[team_fun_settings.TeamFunSettings] = None) -> None:
        """
        Sets the funSettings property value. Settings to configure use of Giphy, memes, and stickers in the team.
        Args:
            value: Value to set for the fun_settings property.
        """
        self._fun_settings = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import channel, conversation_member, entity, group, profile_photo, resource_specific_permission_grant, schedule, teams_app_installation, teams_async_operation, teams_template, teamwork_tag, team_discovery_settings, team_fun_settings, team_guest_settings, team_member_settings, team_messaging_settings, team_specialization, team_summary, team_template_definition, team_visibility_type, user

        fields: Dict[str, Callable[[Any], None]] = {
            "allChannels": lambda n : setattr(self, 'all_channels', n.get_collection_of_object_values(channel.Channel)),
            "channels": lambda n : setattr(self, 'channels', n.get_collection_of_object_values(channel.Channel)),
            "classification": lambda n : setattr(self, 'classification', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "discoverySettings": lambda n : setattr(self, 'discovery_settings', n.get_object_value(team_discovery_settings.TeamDiscoverySettings)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "funSettings": lambda n : setattr(self, 'fun_settings', n.get_object_value(team_fun_settings.TeamFunSettings)),
            "group": lambda n : setattr(self, 'group', n.get_object_value(group.Group)),
            "guestSettings": lambda n : setattr(self, 'guest_settings', n.get_object_value(team_guest_settings.TeamGuestSettings)),
            "incomingChannels": lambda n : setattr(self, 'incoming_channels', n.get_collection_of_object_values(channel.Channel)),
            "installedApps": lambda n : setattr(self, 'installed_apps', n.get_collection_of_object_values(teams_app_installation.TeamsAppInstallation)),
            "internalId": lambda n : setattr(self, 'internal_id', n.get_str_value()),
            "isArchived": lambda n : setattr(self, 'is_archived', n.get_bool_value()),
            "isMembershipLimitedToOwners": lambda n : setattr(self, 'is_membership_limited_to_owners', n.get_bool_value()),
            "members": lambda n : setattr(self, 'members', n.get_collection_of_object_values(conversation_member.ConversationMember)),
            "memberSettings": lambda n : setattr(self, 'member_settings', n.get_object_value(team_member_settings.TeamMemberSettings)),
            "messagingSettings": lambda n : setattr(self, 'messaging_settings', n.get_object_value(team_messaging_settings.TeamMessagingSettings)),
            "operations": lambda n : setattr(self, 'operations', n.get_collection_of_object_values(teams_async_operation.TeamsAsyncOperation)),
            "owners": lambda n : setattr(self, 'owners', n.get_collection_of_object_values(user.User)),
            "permissionGrants": lambda n : setattr(self, 'permission_grants', n.get_collection_of_object_values(resource_specific_permission_grant.ResourceSpecificPermissionGrant)),
            "photo": lambda n : setattr(self, 'photo', n.get_object_value(profile_photo.ProfilePhoto)),
            "primaryChannel": lambda n : setattr(self, 'primary_channel', n.get_object_value(channel.Channel)),
            "schedule": lambda n : setattr(self, 'schedule', n.get_object_value(schedule.Schedule)),
            "specialization": lambda n : setattr(self, 'specialization', n.get_enum_value(team_specialization.TeamSpecialization)),
            "summary": lambda n : setattr(self, 'summary', n.get_object_value(team_summary.TeamSummary)),
            "tags": lambda n : setattr(self, 'tags', n.get_collection_of_object_values(teamwork_tag.TeamworkTag)),
            "template": lambda n : setattr(self, 'template', n.get_object_value(teams_template.TeamsTemplate)),
            "templateDefinition": lambda n : setattr(self, 'template_definition', n.get_object_value(team_template_definition.TeamTemplateDefinition)),
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
            "visibility": lambda n : setattr(self, 'visibility', n.get_enum_value(team_visibility_type.TeamVisibilityType)),
            "webUrl": lambda n : setattr(self, 'web_url', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def group(self,) -> Optional[group.Group]:
        """
        Gets the group property value. The group property
        Returns: Optional[group.Group]
        """
        return self._group
    
    @group.setter
    def group(self,value: Optional[group.Group] = None) -> None:
        """
        Sets the group property value. The group property
        Args:
            value: Value to set for the group property.
        """
        self._group = value
    
    @property
    def guest_settings(self,) -> Optional[team_guest_settings.TeamGuestSettings]:
        """
        Gets the guestSettings property value. Settings to configure whether guests can create, update, or delete channels in the team.
        Returns: Optional[team_guest_settings.TeamGuestSettings]
        """
        return self._guest_settings
    
    @guest_settings.setter
    def guest_settings(self,value: Optional[team_guest_settings.TeamGuestSettings] = None) -> None:
        """
        Sets the guestSettings property value. Settings to configure whether guests can create, update, or delete channels in the team.
        Args:
            value: Value to set for the guest_settings property.
        """
        self._guest_settings = value
    
    @property
    def incoming_channels(self,) -> Optional[List[channel.Channel]]:
        """
        Gets the incomingChannels property value. List of channels shared with the team.
        Returns: Optional[List[channel.Channel]]
        """
        return self._incoming_channels
    
    @incoming_channels.setter
    def incoming_channels(self,value: Optional[List[channel.Channel]] = None) -> None:
        """
        Sets the incomingChannels property value. List of channels shared with the team.
        Args:
            value: Value to set for the incoming_channels property.
        """
        self._incoming_channels = value
    
    @property
    def installed_apps(self,) -> Optional[List[teams_app_installation.TeamsAppInstallation]]:
        """
        Gets the installedApps property value. The apps installed in this team.
        Returns: Optional[List[teams_app_installation.TeamsAppInstallation]]
        """
        return self._installed_apps
    
    @installed_apps.setter
    def installed_apps(self,value: Optional[List[teams_app_installation.TeamsAppInstallation]] = None) -> None:
        """
        Sets the installedApps property value. The apps installed in this team.
        Args:
            value: Value to set for the installed_apps property.
        """
        self._installed_apps = value
    
    @property
    def internal_id(self,) -> Optional[str]:
        """
        Gets the internalId property value. A unique ID for the team that has been used in a few places such as the audit log/Office 365 Management Activity API.
        Returns: Optional[str]
        """
        return self._internal_id
    
    @internal_id.setter
    def internal_id(self,value: Optional[str] = None) -> None:
        """
        Sets the internalId property value. A unique ID for the team that has been used in a few places such as the audit log/Office 365 Management Activity API.
        Args:
            value: Value to set for the internal_id property.
        """
        self._internal_id = value
    
    @property
    def is_archived(self,) -> Optional[bool]:
        """
        Gets the isArchived property value. Whether this team is in read-only mode.
        Returns: Optional[bool]
        """
        return self._is_archived
    
    @is_archived.setter
    def is_archived(self,value: Optional[bool] = None) -> None:
        """
        Sets the isArchived property value. Whether this team is in read-only mode.
        Args:
            value: Value to set for the is_archived property.
        """
        self._is_archived = value
    
    @property
    def is_membership_limited_to_owners(self,) -> Optional[bool]:
        """
        Gets the isMembershipLimitedToOwners property value. If set to true, the team is currently in the owner-only team membership state and not accessible by other team members, such as students.
        Returns: Optional[bool]
        """
        return self._is_membership_limited_to_owners
    
    @is_membership_limited_to_owners.setter
    def is_membership_limited_to_owners(self,value: Optional[bool] = None) -> None:
        """
        Sets the isMembershipLimitedToOwners property value. If set to true, the team is currently in the owner-only team membership state and not accessible by other team members, such as students.
        Args:
            value: Value to set for the is_membership_limited_to_owners property.
        """
        self._is_membership_limited_to_owners = value
    
    @property
    def member_settings(self,) -> Optional[team_member_settings.TeamMemberSettings]:
        """
        Gets the memberSettings property value. Settings to configure whether members can perform certain actions, for example, create channels and add bots, in the team.
        Returns: Optional[team_member_settings.TeamMemberSettings]
        """
        return self._member_settings
    
    @member_settings.setter
    def member_settings(self,value: Optional[team_member_settings.TeamMemberSettings] = None) -> None:
        """
        Sets the memberSettings property value. Settings to configure whether members can perform certain actions, for example, create channels and add bots, in the team.
        Args:
            value: Value to set for the member_settings property.
        """
        self._member_settings = value
    
    @property
    def members(self,) -> Optional[List[conversation_member.ConversationMember]]:
        """
        Gets the members property value. Members and owners of the team.
        Returns: Optional[List[conversation_member.ConversationMember]]
        """
        return self._members
    
    @members.setter
    def members(self,value: Optional[List[conversation_member.ConversationMember]] = None) -> None:
        """
        Sets the members property value. Members and owners of the team.
        Args:
            value: Value to set for the members property.
        """
        self._members = value
    
    @property
    def messaging_settings(self,) -> Optional[team_messaging_settings.TeamMessagingSettings]:
        """
        Gets the messagingSettings property value. Settings to configure messaging and mentions in the team.
        Returns: Optional[team_messaging_settings.TeamMessagingSettings]
        """
        return self._messaging_settings
    
    @messaging_settings.setter
    def messaging_settings(self,value: Optional[team_messaging_settings.TeamMessagingSettings] = None) -> None:
        """
        Sets the messagingSettings property value. Settings to configure messaging and mentions in the team.
        Args:
            value: Value to set for the messaging_settings property.
        """
        self._messaging_settings = value
    
    @property
    def operations(self,) -> Optional[List[teams_async_operation.TeamsAsyncOperation]]:
        """
        Gets the operations property value. The async operations that ran or are running on this team.
        Returns: Optional[List[teams_async_operation.TeamsAsyncOperation]]
        """
        return self._operations
    
    @operations.setter
    def operations(self,value: Optional[List[teams_async_operation.TeamsAsyncOperation]] = None) -> None:
        """
        Sets the operations property value. The async operations that ran or are running on this team.
        Args:
            value: Value to set for the operations property.
        """
        self._operations = value
    
    @property
    def owners(self,) -> Optional[List[user.User]]:
        """
        Gets the owners property value. The list of this team's owners. Currently, when creating a team using application permissions, exactly one owner must be specified. When using user delegated permissions, no owner can be specified (the current user is the owner). Owner must be specified as an object ID (GUID), not a UPN.
        Returns: Optional[List[user.User]]
        """
        return self._owners
    
    @owners.setter
    def owners(self,value: Optional[List[user.User]] = None) -> None:
        """
        Sets the owners property value. The list of this team's owners. Currently, when creating a team using application permissions, exactly one owner must be specified. When using user delegated permissions, no owner can be specified (the current user is the owner). Owner must be specified as an object ID (GUID), not a UPN.
        Args:
            value: Value to set for the owners property.
        """
        self._owners = value
    
    @property
    def permission_grants(self,) -> Optional[List[resource_specific_permission_grant.ResourceSpecificPermissionGrant]]:
        """
        Gets the permissionGrants property value. A collection of permissions granted to apps to access the team.
        Returns: Optional[List[resource_specific_permission_grant.ResourceSpecificPermissionGrant]]
        """
        return self._permission_grants
    
    @permission_grants.setter
    def permission_grants(self,value: Optional[List[resource_specific_permission_grant.ResourceSpecificPermissionGrant]] = None) -> None:
        """
        Sets the permissionGrants property value. A collection of permissions granted to apps to access the team.
        Args:
            value: Value to set for the permission_grants property.
        """
        self._permission_grants = value
    
    @property
    def photo(self,) -> Optional[profile_photo.ProfilePhoto]:
        """
        Gets the photo property value. The team photo.
        Returns: Optional[profile_photo.ProfilePhoto]
        """
        return self._photo
    
    @photo.setter
    def photo(self,value: Optional[profile_photo.ProfilePhoto] = None) -> None:
        """
        Sets the photo property value. The team photo.
        Args:
            value: Value to set for the photo property.
        """
        self._photo = value
    
    @property
    def primary_channel(self,) -> Optional[channel.Channel]:
        """
        Gets the primaryChannel property value. The general channel for the team.
        Returns: Optional[channel.Channel]
        """
        return self._primary_channel
    
    @primary_channel.setter
    def primary_channel(self,value: Optional[channel.Channel] = None) -> None:
        """
        Sets the primaryChannel property value. The general channel for the team.
        Args:
            value: Value to set for the primary_channel property.
        """
        self._primary_channel = value
    
    @property
    def schedule(self,) -> Optional[schedule.Schedule]:
        """
        Gets the schedule property value. The schedule of shifts for this team.
        Returns: Optional[schedule.Schedule]
        """
        return self._schedule
    
    @schedule.setter
    def schedule(self,value: Optional[schedule.Schedule] = None) -> None:
        """
        Sets the schedule property value. The schedule of shifts for this team.
        Args:
            value: Value to set for the schedule property.
        """
        self._schedule = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("allChannels", self.all_channels)
        writer.write_collection_of_object_values("channels", self.channels)
        writer.write_str_value("classification", self.classification)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_object_value("discoverySettings", self.discovery_settings)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("funSettings", self.fun_settings)
        writer.write_object_value("group", self.group)
        writer.write_object_value("guestSettings", self.guest_settings)
        writer.write_collection_of_object_values("incomingChannels", self.incoming_channels)
        writer.write_collection_of_object_values("installedApps", self.installed_apps)
        writer.write_str_value("internalId", self.internal_id)
        writer.write_bool_value("isArchived", self.is_archived)
        writer.write_bool_value("isMembershipLimitedToOwners", self.is_membership_limited_to_owners)
        writer.write_collection_of_object_values("members", self.members)
        writer.write_object_value("memberSettings", self.member_settings)
        writer.write_object_value("messagingSettings", self.messaging_settings)
        writer.write_collection_of_object_values("operations", self.operations)
        writer.write_collection_of_object_values("owners", self.owners)
        writer.write_collection_of_object_values("permissionGrants", self.permission_grants)
        writer.write_object_value("photo", self.photo)
        writer.write_object_value("primaryChannel", self.primary_channel)
        writer.write_object_value("schedule", self.schedule)
        writer.write_enum_value("specialization", self.specialization)
        writer.write_object_value("summary", self.summary)
        writer.write_collection_of_object_values("tags", self.tags)
        writer.write_object_value("template", self.template)
        writer.write_object_value("templateDefinition", self.template_definition)
        writer.write_str_value("tenantId", self.tenant_id)
        writer.write_enum_value("visibility", self.visibility)
        writer.write_str_value("webUrl", self.web_url)
    
    @property
    def specialization(self,) -> Optional[team_specialization.TeamSpecialization]:
        """
        Gets the specialization property value. Optional. Indicates whether the team is intended for a particular use case.  Each team specialization has access to unique behaviors and experiences targeted to its use case.
        Returns: Optional[team_specialization.TeamSpecialization]
        """
        return self._specialization
    
    @specialization.setter
    def specialization(self,value: Optional[team_specialization.TeamSpecialization] = None) -> None:
        """
        Sets the specialization property value. Optional. Indicates whether the team is intended for a particular use case.  Each team specialization has access to unique behaviors and experiences targeted to its use case.
        Args:
            value: Value to set for the specialization property.
        """
        self._specialization = value
    
    @property
    def summary(self,) -> Optional[team_summary.TeamSummary]:
        """
        Gets the summary property value. Contains summary information about the team, including number of owners, members, and guests.
        Returns: Optional[team_summary.TeamSummary]
        """
        return self._summary
    
    @summary.setter
    def summary(self,value: Optional[team_summary.TeamSummary] = None) -> None:
        """
        Sets the summary property value. Contains summary information about the team, including number of owners, members, and guests.
        Args:
            value: Value to set for the summary property.
        """
        self._summary = value
    
    @property
    def tags(self,) -> Optional[List[teamwork_tag.TeamworkTag]]:
        """
        Gets the tags property value. The tags associated with the team.
        Returns: Optional[List[teamwork_tag.TeamworkTag]]
        """
        return self._tags
    
    @tags.setter
    def tags(self,value: Optional[List[teamwork_tag.TeamworkTag]] = None) -> None:
        """
        Sets the tags property value. The tags associated with the team.
        Args:
            value: Value to set for the tags property.
        """
        self._tags = value
    
    @property
    def template(self,) -> Optional[teams_template.TeamsTemplate]:
        """
        Gets the template property value. The template this team was created from. See available templates.
        Returns: Optional[teams_template.TeamsTemplate]
        """
        return self._template
    
    @template.setter
    def template(self,value: Optional[teams_template.TeamsTemplate] = None) -> None:
        """
        Sets the template property value. The template this team was created from. See available templates.
        Args:
            value: Value to set for the template property.
        """
        self._template = value
    
    @property
    def template_definition(self,) -> Optional[team_template_definition.TeamTemplateDefinition]:
        """
        Gets the templateDefinition property value. Generic representation of a team template definition for a team with a specific structure and configuration.
        Returns: Optional[team_template_definition.TeamTemplateDefinition]
        """
        return self._template_definition
    
    @template_definition.setter
    def template_definition(self,value: Optional[team_template_definition.TeamTemplateDefinition] = None) -> None:
        """
        Sets the templateDefinition property value. Generic representation of a team template definition for a team with a specific structure and configuration.
        Args:
            value: Value to set for the template_definition property.
        """
        self._template_definition = value
    
    @property
    def tenant_id(self,) -> Optional[str]:
        """
        Gets the tenantId property value. The ID of the Azure Active Directory tenant.
        Returns: Optional[str]
        """
        return self._tenant_id
    
    @tenant_id.setter
    def tenant_id(self,value: Optional[str] = None) -> None:
        """
        Sets the tenantId property value. The ID of the Azure Active Directory tenant.
        Args:
            value: Value to set for the tenant_id property.
        """
        self._tenant_id = value
    
    @property
    def visibility(self,) -> Optional[team_visibility_type.TeamVisibilityType]:
        """
        Gets the visibility property value. The visibility of the group and team. Defaults to Public.
        Returns: Optional[team_visibility_type.TeamVisibilityType]
        """
        return self._visibility
    
    @visibility.setter
    def visibility(self,value: Optional[team_visibility_type.TeamVisibilityType] = None) -> None:
        """
        Sets the visibility property value. The visibility of the group and team. Defaults to Public.
        Args:
            value: Value to set for the visibility property.
        """
        self._visibility = value
    
    @property
    def web_url(self,) -> Optional[str]:
        """
        Gets the webUrl property value. A hyperlink that will go to the team in the Microsoft Teams client. This is the URL that you get when you right-click a team in the Microsoft Teams client and select Get link to team. This URL should be treated as an opaque blob, and not parsed.
        Returns: Optional[str]
        """
        return self._web_url
    
    @web_url.setter
    def web_url(self,value: Optional[str] = None) -> None:
        """
        Sets the webUrl property value. A hyperlink that will go to the team in the Microsoft Teams client. This is the URL that you get when you right-click a team in the Microsoft Teams client and select Get link to team. This URL should be treated as an opaque blob, and not parsed.
        Args:
            value: Value to set for the web_url property.
        """
        self._web_url = value
    

