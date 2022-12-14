from __future__ import annotations
from datetime import date
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class Office365GroupsActivityCounts(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new Office365GroupsActivityCounts and sets the default values.
        """
        super().__init__()
        # The number of emails received by Group mailboxes.
        self._exchange_emails_received: Optional[int] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The date on which a number of emails were sent to a group mailbox or a number of messages were posted, read, or liked in a Yammer group
        self._report_date: Optional[Date] = None
        # The number of days the report covers.
        self._report_period: Optional[str] = None
        # The latest date of the content.
        self._report_refresh_date: Optional[Date] = None
        # The teamsChannelMessages property
        self._teams_channel_messages: Optional[int] = None
        # The teamsMeetingsOrganized property
        self._teams_meetings_organized: Optional[int] = None
        # The number of messages liked in Yammer groups.
        self._yammer_messages_liked: Optional[int] = None
        # The number of messages posted to Yammer groups.
        self._yammer_messages_posted: Optional[int] = None
        # The number of messages read in Yammer groups.
        self._yammer_messages_read: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Office365GroupsActivityCounts:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Office365GroupsActivityCounts
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Office365GroupsActivityCounts()
    
    @property
    def exchange_emails_received(self,) -> Optional[int]:
        """
        Gets the exchangeEmailsReceived property value. The number of emails received by Group mailboxes.
        Returns: Optional[int]
        """
        return self._exchange_emails_received
    
    @exchange_emails_received.setter
    def exchange_emails_received(self,value: Optional[int] = None) -> None:
        """
        Sets the exchangeEmailsReceived property value. The number of emails received by Group mailboxes.
        Args:
            value: Value to set for the exchangeEmailsReceived property.
        """
        self._exchange_emails_received = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "exchange_emails_received": lambda n : setattr(self, 'exchange_emails_received', n.get_int_value()),
            "report_date": lambda n : setattr(self, 'report_date', n.get_object_value(Date)),
            "report_period": lambda n : setattr(self, 'report_period', n.get_str_value()),
            "report_refresh_date": lambda n : setattr(self, 'report_refresh_date', n.get_object_value(Date)),
            "teams_channel_messages": lambda n : setattr(self, 'teams_channel_messages', n.get_int_value()),
            "teams_meetings_organized": lambda n : setattr(self, 'teams_meetings_organized', n.get_int_value()),
            "yammer_messages_liked": lambda n : setattr(self, 'yammer_messages_liked', n.get_int_value()),
            "yammer_messages_posted": lambda n : setattr(self, 'yammer_messages_posted', n.get_int_value()),
            "yammer_messages_read": lambda n : setattr(self, 'yammer_messages_read', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def report_date(self,) -> Optional[Date]:
        """
        Gets the reportDate property value. The date on which a number of emails were sent to a group mailbox or a number of messages were posted, read, or liked in a Yammer group
        Returns: Optional[Date]
        """
        return self._report_date
    
    @report_date.setter
    def report_date(self,value: Optional[Date] = None) -> None:
        """
        Sets the reportDate property value. The date on which a number of emails were sent to a group mailbox or a number of messages were posted, read, or liked in a Yammer group
        Args:
            value: Value to set for the reportDate property.
        """
        self._report_date = value
    
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
        writer.write_int_value("exchangeEmailsReceived", self.exchange_emails_received)
        writer.write_object_value("reportDate", self.report_date)
        writer.write_str_value("reportPeriod", self.report_period)
        writer.write_object_value("reportRefreshDate", self.report_refresh_date)
        writer.write_int_value("teamsChannelMessages", self.teams_channel_messages)
        writer.write_int_value("teamsMeetingsOrganized", self.teams_meetings_organized)
        writer.write_int_value("yammerMessagesLiked", self.yammer_messages_liked)
        writer.write_int_value("yammerMessagesPosted", self.yammer_messages_posted)
        writer.write_int_value("yammerMessagesRead", self.yammer_messages_read)
    
    @property
    def teams_channel_messages(self,) -> Optional[int]:
        """
        Gets the teamsChannelMessages property value. The teamsChannelMessages property
        Returns: Optional[int]
        """
        return self._teams_channel_messages
    
    @teams_channel_messages.setter
    def teams_channel_messages(self,value: Optional[int] = None) -> None:
        """
        Sets the teamsChannelMessages property value. The teamsChannelMessages property
        Args:
            value: Value to set for the teamsChannelMessages property.
        """
        self._teams_channel_messages = value
    
    @property
    def teams_meetings_organized(self,) -> Optional[int]:
        """
        Gets the teamsMeetingsOrganized property value. The teamsMeetingsOrganized property
        Returns: Optional[int]
        """
        return self._teams_meetings_organized
    
    @teams_meetings_organized.setter
    def teams_meetings_organized(self,value: Optional[int] = None) -> None:
        """
        Sets the teamsMeetingsOrganized property value. The teamsMeetingsOrganized property
        Args:
            value: Value to set for the teamsMeetingsOrganized property.
        """
        self._teams_meetings_organized = value
    
    @property
    def yammer_messages_liked(self,) -> Optional[int]:
        """
        Gets the yammerMessagesLiked property value. The number of messages liked in Yammer groups.
        Returns: Optional[int]
        """
        return self._yammer_messages_liked
    
    @yammer_messages_liked.setter
    def yammer_messages_liked(self,value: Optional[int] = None) -> None:
        """
        Sets the yammerMessagesLiked property value. The number of messages liked in Yammer groups.
        Args:
            value: Value to set for the yammerMessagesLiked property.
        """
        self._yammer_messages_liked = value
    
    @property
    def yammer_messages_posted(self,) -> Optional[int]:
        """
        Gets the yammerMessagesPosted property value. The number of messages posted to Yammer groups.
        Returns: Optional[int]
        """
        return self._yammer_messages_posted
    
    @yammer_messages_posted.setter
    def yammer_messages_posted(self,value: Optional[int] = None) -> None:
        """
        Sets the yammerMessagesPosted property value. The number of messages posted to Yammer groups.
        Args:
            value: Value to set for the yammerMessagesPosted property.
        """
        self._yammer_messages_posted = value
    
    @property
    def yammer_messages_read(self,) -> Optional[int]:
        """
        Gets the yammerMessagesRead property value. The number of messages read in Yammer groups.
        Returns: Optional[int]
        """
        return self._yammer_messages_read
    
    @yammer_messages_read.setter
    def yammer_messages_read(self,value: Optional[int] = None) -> None:
        """
        Sets the yammerMessagesRead property value. The number of messages read in Yammer groups.
        Args:
            value: Value to set for the yammerMessagesRead property.
        """
        self._yammer_messages_read = value
    

