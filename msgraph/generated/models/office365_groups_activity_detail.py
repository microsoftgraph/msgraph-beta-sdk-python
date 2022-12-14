from __future__ import annotations
from datetime import date
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class Office365GroupsActivityDetail(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new Office365GroupsActivityDetail and sets the default values.
        """
        super().__init__()
        # The storage used of the group mailbox.
        self._exchange_mailbox_storage_used_in_bytes: Optional[int] = None
        # The number of items in the group mailbox.
        self._exchange_mailbox_total_item_count: Optional[int] = None
        # The number of email that the group mailbox received.
        self._exchange_received_email_count: Optional[int] = None
        # The group external member count.
        self._external_member_count: Optional[int] = None
        # The display name of the group.
        self._group_display_name: Optional[str] = None
        # The group id.
        self._group_id: Optional[str] = None
        # The group type. Possible values are: Public or Private.
        self._group_type: Optional[str] = None
        # Whether this user has been deleted or soft deleted.
        self._is_deleted: Optional[bool] = None
        # The last activity date for the following scenarios:  group mailbox received email; user viewed, edited, shared, or synced files in SharePoint document library; user viewed SharePoint pages; user posted, read, or liked messages in Yammer groups.
        self._last_activity_date: Optional[Date] = None
        # The group member count.
        self._member_count: Optional[int] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The group owner principal name.
        self._owner_principal_name: Optional[str] = None
        # The number of days the report covers.
        self._report_period: Optional[str] = None
        # The latest date of the content.
        self._report_refresh_date: Optional[Date] = None
        # The number of active files in SharePoint Group site.
        self._share_point_active_file_count: Optional[int] = None
        # The storage used by SharePoint Group site.
        self._share_point_site_storage_used_in_bytes: Optional[int] = None
        # The total number of files in SharePoint Group site.
        self._share_point_total_file_count: Optional[int] = None
        # The teamsChannelMessagesCount property
        self._teams_channel_messages_count: Optional[int] = None
        # The teamsMeetingsOrganizedCount property
        self._teams_meetings_organized_count: Optional[int] = None
        # The number of messages liked in Yammer groups.
        self._yammer_liked_message_count: Optional[int] = None
        # The number of messages posted to Yammer groups.
        self._yammer_posted_message_count: Optional[int] = None
        # The number of messages read in Yammer groups.
        self._yammer_read_message_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Office365GroupsActivityDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Office365GroupsActivityDetail
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Office365GroupsActivityDetail()
    
    @property
    def exchange_mailbox_storage_used_in_bytes(self,) -> Optional[int]:
        """
        Gets the exchangeMailboxStorageUsedInBytes property value. The storage used of the group mailbox.
        Returns: Optional[int]
        """
        return self._exchange_mailbox_storage_used_in_bytes
    
    @exchange_mailbox_storage_used_in_bytes.setter
    def exchange_mailbox_storage_used_in_bytes(self,value: Optional[int] = None) -> None:
        """
        Sets the exchangeMailboxStorageUsedInBytes property value. The storage used of the group mailbox.
        Args:
            value: Value to set for the exchangeMailboxStorageUsedInBytes property.
        """
        self._exchange_mailbox_storage_used_in_bytes = value
    
    @property
    def exchange_mailbox_total_item_count(self,) -> Optional[int]:
        """
        Gets the exchangeMailboxTotalItemCount property value. The number of items in the group mailbox.
        Returns: Optional[int]
        """
        return self._exchange_mailbox_total_item_count
    
    @exchange_mailbox_total_item_count.setter
    def exchange_mailbox_total_item_count(self,value: Optional[int] = None) -> None:
        """
        Sets the exchangeMailboxTotalItemCount property value. The number of items in the group mailbox.
        Args:
            value: Value to set for the exchangeMailboxTotalItemCount property.
        """
        self._exchange_mailbox_total_item_count = value
    
    @property
    def exchange_received_email_count(self,) -> Optional[int]:
        """
        Gets the exchangeReceivedEmailCount property value. The number of email that the group mailbox received.
        Returns: Optional[int]
        """
        return self._exchange_received_email_count
    
    @exchange_received_email_count.setter
    def exchange_received_email_count(self,value: Optional[int] = None) -> None:
        """
        Sets the exchangeReceivedEmailCount property value. The number of email that the group mailbox received.
        Args:
            value: Value to set for the exchangeReceivedEmailCount property.
        """
        self._exchange_received_email_count = value
    
    @property
    def external_member_count(self,) -> Optional[int]:
        """
        Gets the externalMemberCount property value. The group external member count.
        Returns: Optional[int]
        """
        return self._external_member_count
    
    @external_member_count.setter
    def external_member_count(self,value: Optional[int] = None) -> None:
        """
        Sets the externalMemberCount property value. The group external member count.
        Args:
            value: Value to set for the externalMemberCount property.
        """
        self._external_member_count = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "exchange_mailbox_storage_used_in_bytes": lambda n : setattr(self, 'exchange_mailbox_storage_used_in_bytes', n.get_int_value()),
            "exchange_mailbox_total_item_count": lambda n : setattr(self, 'exchange_mailbox_total_item_count', n.get_int_value()),
            "exchange_received_email_count": lambda n : setattr(self, 'exchange_received_email_count', n.get_int_value()),
            "external_member_count": lambda n : setattr(self, 'external_member_count', n.get_int_value()),
            "group_display_name": lambda n : setattr(self, 'group_display_name', n.get_str_value()),
            "group_id": lambda n : setattr(self, 'group_id', n.get_str_value()),
            "group_type": lambda n : setattr(self, 'group_type', n.get_str_value()),
            "is_deleted": lambda n : setattr(self, 'is_deleted', n.get_bool_value()),
            "last_activity_date": lambda n : setattr(self, 'last_activity_date', n.get_object_value(Date)),
            "member_count": lambda n : setattr(self, 'member_count', n.get_int_value()),
            "owner_principal_name": lambda n : setattr(self, 'owner_principal_name', n.get_str_value()),
            "report_period": lambda n : setattr(self, 'report_period', n.get_str_value()),
            "report_refresh_date": lambda n : setattr(self, 'report_refresh_date', n.get_object_value(Date)),
            "share_point_active_file_count": lambda n : setattr(self, 'share_point_active_file_count', n.get_int_value()),
            "share_point_site_storage_used_in_bytes": lambda n : setattr(self, 'share_point_site_storage_used_in_bytes', n.get_int_value()),
            "share_point_total_file_count": lambda n : setattr(self, 'share_point_total_file_count', n.get_int_value()),
            "teams_channel_messages_count": lambda n : setattr(self, 'teams_channel_messages_count', n.get_int_value()),
            "teams_meetings_organized_count": lambda n : setattr(self, 'teams_meetings_organized_count', n.get_int_value()),
            "yammer_liked_message_count": lambda n : setattr(self, 'yammer_liked_message_count', n.get_int_value()),
            "yammer_posted_message_count": lambda n : setattr(self, 'yammer_posted_message_count', n.get_int_value()),
            "yammer_read_message_count": lambda n : setattr(self, 'yammer_read_message_count', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def group_display_name(self,) -> Optional[str]:
        """
        Gets the groupDisplayName property value. The display name of the group.
        Returns: Optional[str]
        """
        return self._group_display_name
    
    @group_display_name.setter
    def group_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the groupDisplayName property value. The display name of the group.
        Args:
            value: Value to set for the groupDisplayName property.
        """
        self._group_display_name = value
    
    @property
    def group_id(self,) -> Optional[str]:
        """
        Gets the groupId property value. The group id.
        Returns: Optional[str]
        """
        return self._group_id
    
    @group_id.setter
    def group_id(self,value: Optional[str] = None) -> None:
        """
        Sets the groupId property value. The group id.
        Args:
            value: Value to set for the groupId property.
        """
        self._group_id = value
    
    @property
    def group_type(self,) -> Optional[str]:
        """
        Gets the groupType property value. The group type. Possible values are: Public or Private.
        Returns: Optional[str]
        """
        return self._group_type
    
    @group_type.setter
    def group_type(self,value: Optional[str] = None) -> None:
        """
        Sets the groupType property value. The group type. Possible values are: Public or Private.
        Args:
            value: Value to set for the groupType property.
        """
        self._group_type = value
    
    @property
    def is_deleted(self,) -> Optional[bool]:
        """
        Gets the isDeleted property value. Whether this user has been deleted or soft deleted.
        Returns: Optional[bool]
        """
        return self._is_deleted
    
    @is_deleted.setter
    def is_deleted(self,value: Optional[bool] = None) -> None:
        """
        Sets the isDeleted property value. Whether this user has been deleted or soft deleted.
        Args:
            value: Value to set for the isDeleted property.
        """
        self._is_deleted = value
    
    @property
    def last_activity_date(self,) -> Optional[Date]:
        """
        Gets the lastActivityDate property value. The last activity date for the following scenarios:  group mailbox received email; user viewed, edited, shared, or synced files in SharePoint document library; user viewed SharePoint pages; user posted, read, or liked messages in Yammer groups.
        Returns: Optional[Date]
        """
        return self._last_activity_date
    
    @last_activity_date.setter
    def last_activity_date(self,value: Optional[Date] = None) -> None:
        """
        Sets the lastActivityDate property value. The last activity date for the following scenarios:  group mailbox received email; user viewed, edited, shared, or synced files in SharePoint document library; user viewed SharePoint pages; user posted, read, or liked messages in Yammer groups.
        Args:
            value: Value to set for the lastActivityDate property.
        """
        self._last_activity_date = value
    
    @property
    def member_count(self,) -> Optional[int]:
        """
        Gets the memberCount property value. The group member count.
        Returns: Optional[int]
        """
        return self._member_count
    
    @member_count.setter
    def member_count(self,value: Optional[int] = None) -> None:
        """
        Sets the memberCount property value. The group member count.
        Args:
            value: Value to set for the memberCount property.
        """
        self._member_count = value
    
    @property
    def owner_principal_name(self,) -> Optional[str]:
        """
        Gets the ownerPrincipalName property value. The group owner principal name.
        Returns: Optional[str]
        """
        return self._owner_principal_name
    
    @owner_principal_name.setter
    def owner_principal_name(self,value: Optional[str] = None) -> None:
        """
        Sets the ownerPrincipalName property value. The group owner principal name.
        Args:
            value: Value to set for the ownerPrincipalName property.
        """
        self._owner_principal_name = value
    
    @property
    def report_period(self,) -> Optional[str]:
        """
        Gets the reportPeriod property value. The number of days the report covers.
        Returns: Optional[str]
        """
        return self._report_period
    
    @report_period.setter
    def report_period(self,value: Optional[str] = None) -> None:
        """
        Sets the reportPeriod property value. The number of days the report covers.
        Args:
            value: Value to set for the reportPeriod property.
        """
        self._report_period = value
    
    @property
    def report_refresh_date(self,) -> Optional[Date]:
        """
        Gets the reportRefreshDate property value. The latest date of the content.
        Returns: Optional[Date]
        """
        return self._report_refresh_date
    
    @report_refresh_date.setter
    def report_refresh_date(self,value: Optional[Date] = None) -> None:
        """
        Sets the reportRefreshDate property value. The latest date of the content.
        Args:
            value: Value to set for the reportRefreshDate property.
        """
        self._report_refresh_date = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_int_value("exchangeMailboxStorageUsedInBytes", self.exchange_mailbox_storage_used_in_bytes)
        writer.write_int_value("exchangeMailboxTotalItemCount", self.exchange_mailbox_total_item_count)
        writer.write_int_value("exchangeReceivedEmailCount", self.exchange_received_email_count)
        writer.write_int_value("externalMemberCount", self.external_member_count)
        writer.write_str_value("groupDisplayName", self.group_display_name)
        writer.write_str_value("groupId", self.group_id)
        writer.write_str_value("groupType", self.group_type)
        writer.write_bool_value("isDeleted", self.is_deleted)
        writer.write_object_value("lastActivityDate", self.last_activity_date)
        writer.write_int_value("memberCount", self.member_count)
        writer.write_str_value("ownerPrincipalName", self.owner_principal_name)
        writer.write_str_value("reportPeriod", self.report_period)
        writer.write_object_value("reportRefreshDate", self.report_refresh_date)
        writer.write_int_value("sharePointActiveFileCount", self.share_point_active_file_count)
        writer.write_int_value("sharePointSiteStorageUsedInBytes", self.share_point_site_storage_used_in_bytes)
        writer.write_int_value("sharePointTotalFileCount", self.share_point_total_file_count)
        writer.write_int_value("teamsChannelMessagesCount", self.teams_channel_messages_count)
        writer.write_int_value("teamsMeetingsOrganizedCount", self.teams_meetings_organized_count)
        writer.write_int_value("yammerLikedMessageCount", self.yammer_liked_message_count)
        writer.write_int_value("yammerPostedMessageCount", self.yammer_posted_message_count)
        writer.write_int_value("yammerReadMessageCount", self.yammer_read_message_count)
    
    @property
    def share_point_active_file_count(self,) -> Optional[int]:
        """
        Gets the sharePointActiveFileCount property value. The number of active files in SharePoint Group site.
        Returns: Optional[int]
        """
        return self._share_point_active_file_count
    
    @share_point_active_file_count.setter
    def share_point_active_file_count(self,value: Optional[int] = None) -> None:
        """
        Sets the sharePointActiveFileCount property value. The number of active files in SharePoint Group site.
        Args:
            value: Value to set for the sharePointActiveFileCount property.
        """
        self._share_point_active_file_count = value
    
    @property
    def share_point_site_storage_used_in_bytes(self,) -> Optional[int]:
        """
        Gets the sharePointSiteStorageUsedInBytes property value. The storage used by SharePoint Group site.
        Returns: Optional[int]
        """
        return self._share_point_site_storage_used_in_bytes
    
    @share_point_site_storage_used_in_bytes.setter
    def share_point_site_storage_used_in_bytes(self,value: Optional[int] = None) -> None:
        """
        Sets the sharePointSiteStorageUsedInBytes property value. The storage used by SharePoint Group site.
        Args:
            value: Value to set for the sharePointSiteStorageUsedInBytes property.
        """
        self._share_point_site_storage_used_in_bytes = value
    
    @property
    def share_point_total_file_count(self,) -> Optional[int]:
        """
        Gets the sharePointTotalFileCount property value. The total number of files in SharePoint Group site.
        Returns: Optional[int]
        """
        return self._share_point_total_file_count
    
    @share_point_total_file_count.setter
    def share_point_total_file_count(self,value: Optional[int] = None) -> None:
        """
        Sets the sharePointTotalFileCount property value. The total number of files in SharePoint Group site.
        Args:
            value: Value to set for the sharePointTotalFileCount property.
        """
        self._share_point_total_file_count = value
    
    @property
    def teams_channel_messages_count(self,) -> Optional[int]:
        """
        Gets the teamsChannelMessagesCount property value. The teamsChannelMessagesCount property
        Returns: Optional[int]
        """
        return self._teams_channel_messages_count
    
    @teams_channel_messages_count.setter
    def teams_channel_messages_count(self,value: Optional[int] = None) -> None:
        """
        Sets the teamsChannelMessagesCount property value. The teamsChannelMessagesCount property
        Args:
            value: Value to set for the teamsChannelMessagesCount property.
        """
        self._teams_channel_messages_count = value
    
    @property
    def teams_meetings_organized_count(self,) -> Optional[int]:
        """
        Gets the teamsMeetingsOrganizedCount property value. The teamsMeetingsOrganizedCount property
        Returns: Optional[int]
        """
        return self._teams_meetings_organized_count
    
    @teams_meetings_organized_count.setter
    def teams_meetings_organized_count(self,value: Optional[int] = None) -> None:
        """
        Sets the teamsMeetingsOrganizedCount property value. The teamsMeetingsOrganizedCount property
        Args:
            value: Value to set for the teamsMeetingsOrganizedCount property.
        """
        self._teams_meetings_organized_count = value
    
    @property
    def yammer_liked_message_count(self,) -> Optional[int]:
        """
        Gets the yammerLikedMessageCount property value. The number of messages liked in Yammer groups.
        Returns: Optional[int]
        """
        return self._yammer_liked_message_count
    
    @yammer_liked_message_count.setter
    def yammer_liked_message_count(self,value: Optional[int] = None) -> None:
        """
        Sets the yammerLikedMessageCount property value. The number of messages liked in Yammer groups.
        Args:
            value: Value to set for the yammerLikedMessageCount property.
        """
        self._yammer_liked_message_count = value
    
    @property
    def yammer_posted_message_count(self,) -> Optional[int]:
        """
        Gets the yammerPostedMessageCount property value. The number of messages posted to Yammer groups.
        Returns: Optional[int]
        """
        return self._yammer_posted_message_count
    
    @yammer_posted_message_count.setter
    def yammer_posted_message_count(self,value: Optional[int] = None) -> None:
        """
        Sets the yammerPostedMessageCount property value. The number of messages posted to Yammer groups.
        Args:
            value: Value to set for the yammerPostedMessageCount property.
        """
        self._yammer_posted_message_count = value
    
    @property
    def yammer_read_message_count(self,) -> Optional[int]:
        """
        Gets the yammerReadMessageCount property value. The number of messages read in Yammer groups.
        Returns: Optional[int]
        """
        return self._yammer_read_message_count
    
    @yammer_read_message_count.setter
    def yammer_read_message_count(self,value: Optional[int] = None) -> None:
        """
        Sets the yammerReadMessageCount property value. The number of messages read in Yammer groups.
        Args:
            value: Value to set for the yammerReadMessageCount property.
        """
        self._yammer_read_message_count = value
    

