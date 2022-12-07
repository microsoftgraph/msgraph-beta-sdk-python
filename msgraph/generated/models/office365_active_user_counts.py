from __future__ import annotations
from datetime import date
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class Office365ActiveUserCounts(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new Office365ActiveUserCounts and sets the default values.
        """
        super().__init__()
        # The number of active users in Exchange. Any user who can read and send email is considered an active user.
        self._exchange: Optional[int] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The number of active users in Microsoft 365. This number includes all the active users in Exchange, OneDrive, SharePoint, Skype For Business, Yammer, and Microsoft Teams. You can find the definition of active user for each product in the respective property description.
        self._office365: Optional[int] = None
        # The number of active users in OneDrive. Any user who viewed or edited files, shared files internally or externally, or synced files is considered an active user.
        self._one_drive: Optional[int] = None
        # The date on which a number of users were active.
        self._report_date: Optional[Date] = None
        # The number of days the report covers.
        self._report_period: Optional[str] = None
        # The latest date of the content.
        self._report_refresh_date: Optional[Date] = None
        # The number of active users in SharePoint. Any user who viewed or edited files, shared files internally or externally, synced files, or viewed SharePoint pages is considered an active user.
        self._share_point: Optional[int] = None
        # The number of active users in Skype For Business. Any user who organized or participated in conferences, or joined peer-to-peer sessions is considered an active user.
        self._skype_for_business: Optional[int] = None
        # The number of active users in Microsoft Teams. Any user who posted messages in team channels, sent messages in private chat sessions, or participated in meetings or calls is considered an active user.
        self._teams: Optional[int] = None
        # The number of active users in Yammer. Any user who can post, read, or like messages is considered an active user.
        self._yammer: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Office365ActiveUserCounts:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Office365ActiveUserCounts
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Office365ActiveUserCounts()
    
    @property
    def exchange(self,) -> Optional[int]:
        """
        Gets the exchange property value. The number of active users in Exchange. Any user who can read and send email is considered an active user.
        Returns: Optional[int]
        """
        return self._exchange
    
    @exchange.setter
    def exchange(self,value: Optional[int] = None) -> None:
        """
        Sets the exchange property value. The number of active users in Exchange. Any user who can read and send email is considered an active user.
        Args:
            value: Value to set for the exchange property.
        """
        self._exchange = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "exchange": lambda n : setattr(self, 'exchange', n.get_int_value()),
            "office365": lambda n : setattr(self, 'office365', n.get_int_value()),
            "one_drive": lambda n : setattr(self, 'one_drive', n.get_int_value()),
            "report_date": lambda n : setattr(self, 'report_date', n.get_object_value(Date)),
            "report_period": lambda n : setattr(self, 'report_period', n.get_str_value()),
            "report_refresh_date": lambda n : setattr(self, 'report_refresh_date', n.get_object_value(Date)),
            "share_point": lambda n : setattr(self, 'share_point', n.get_int_value()),
            "skype_for_business": lambda n : setattr(self, 'skype_for_business', n.get_int_value()),
            "teams": lambda n : setattr(self, 'teams', n.get_int_value()),
            "yammer": lambda n : setattr(self, 'yammer', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def office365(self,) -> Optional[int]:
        """
        Gets the office365 property value. The number of active users in Microsoft 365. This number includes all the active users in Exchange, OneDrive, SharePoint, Skype For Business, Yammer, and Microsoft Teams. You can find the definition of active user for each product in the respective property description.
        Returns: Optional[int]
        """
        return self._office365
    
    @office365.setter
    def office365(self,value: Optional[int] = None) -> None:
        """
        Sets the office365 property value. The number of active users in Microsoft 365. This number includes all the active users in Exchange, OneDrive, SharePoint, Skype For Business, Yammer, and Microsoft Teams. You can find the definition of active user for each product in the respective property description.
        Args:
            value: Value to set for the office365 property.
        """
        self._office365 = value
    
    @property
    def one_drive(self,) -> Optional[int]:
        """
        Gets the oneDrive property value. The number of active users in OneDrive. Any user who viewed or edited files, shared files internally or externally, or synced files is considered an active user.
        Returns: Optional[int]
        """
        return self._one_drive
    
    @one_drive.setter
    def one_drive(self,value: Optional[int] = None) -> None:
        """
        Sets the oneDrive property value. The number of active users in OneDrive. Any user who viewed or edited files, shared files internally or externally, or synced files is considered an active user.
        Args:
            value: Value to set for the oneDrive property.
        """
        self._one_drive = value
    
    @property
    def report_date(self,) -> Optional[Date]:
        """
        Gets the reportDate property value. The date on which a number of users were active.
        Returns: Optional[Date]
        """
        return self._report_date
    
    @report_date.setter
    def report_date(self,value: Optional[Date] = None) -> None:
        """
        Sets the reportDate property value. The date on which a number of users were active.
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
        writer.write_int_value("exchange", self.exchange)
        writer.write_int_value("office365", self.office365)
        writer.write_int_value("oneDrive", self.one_drive)
        writer.write_object_value("reportDate", self.report_date)
        writer.write_str_value("reportPeriod", self.report_period)
        writer.write_object_value("reportRefreshDate", self.report_refresh_date)
        writer.write_int_value("sharePoint", self.share_point)
        writer.write_int_value("skypeForBusiness", self.skype_for_business)
        writer.write_int_value("teams", self.teams)
        writer.write_int_value("yammer", self.yammer)
    
    @property
    def share_point(self,) -> Optional[int]:
        """
        Gets the sharePoint property value. The number of active users in SharePoint. Any user who viewed or edited files, shared files internally or externally, synced files, or viewed SharePoint pages is considered an active user.
        Returns: Optional[int]
        """
        return self._share_point
    
    @share_point.setter
    def share_point(self,value: Optional[int] = None) -> None:
        """
        Sets the sharePoint property value. The number of active users in SharePoint. Any user who viewed or edited files, shared files internally or externally, synced files, or viewed SharePoint pages is considered an active user.
        Args:
            value: Value to set for the sharePoint property.
        """
        self._share_point = value
    
    @property
    def skype_for_business(self,) -> Optional[int]:
        """
        Gets the skypeForBusiness property value. The number of active users in Skype For Business. Any user who organized or participated in conferences, or joined peer-to-peer sessions is considered an active user.
        Returns: Optional[int]
        """
        return self._skype_for_business
    
    @skype_for_business.setter
    def skype_for_business(self,value: Optional[int] = None) -> None:
        """
        Sets the skypeForBusiness property value. The number of active users in Skype For Business. Any user who organized or participated in conferences, or joined peer-to-peer sessions is considered an active user.
        Args:
            value: Value to set for the skypeForBusiness property.
        """
        self._skype_for_business = value
    
    @property
    def teams(self,) -> Optional[int]:
        """
        Gets the teams property value. The number of active users in Microsoft Teams. Any user who posted messages in team channels, sent messages in private chat sessions, or participated in meetings or calls is considered an active user.
        Returns: Optional[int]
        """
        return self._teams
    
    @teams.setter
    def teams(self,value: Optional[int] = None) -> None:
        """
        Sets the teams property value. The number of active users in Microsoft Teams. Any user who posted messages in team channels, sent messages in private chat sessions, or participated in meetings or calls is considered an active user.
        Args:
            value: Value to set for the teams property.
        """
        self._teams = value
    
    @property
    def yammer(self,) -> Optional[int]:
        """
        Gets the yammer property value. The number of active users in Yammer. Any user who can post, read, or like messages is considered an active user.
        Returns: Optional[int]
        """
        return self._yammer
    
    @yammer.setter
    def yammer(self,value: Optional[int] = None) -> None:
        """
        Sets the yammer property value. The number of active users in Yammer. Any user who can post, read, or like messages is considered an active user.
        Args:
            value: Value to set for the yammer property.
        """
        self._yammer = value
    

