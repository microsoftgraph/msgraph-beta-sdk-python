from __future__ import annotations
from datetime import date
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class Office365ServicesUserCounts(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new Office365ServicesUserCounts and sets the default values.
        """
        super().__init__()
        # The number of active users on Exchange. Any user who can read and send email is considered an active user.
        self._exchange_active: Optional[int] = None
        # The number of inactive users on Exchange.
        self._exchange_inactive: Optional[int] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The number of active users on Microsoft 365.
        self._office365_active: Optional[int] = None
        # The number of inactive users on Microsoft 365.
        self._office365_inactive: Optional[int] = None
        # The number of active users on OneDrive. Any user who viewed or edited files, shared files internally or externally, or synced files is considered an active user.
        self._one_drive_active: Optional[int] = None
        # The number of inactive users on OneDrive.
        self._one_drive_inactive: Optional[int] = None
        # The number of days the report covers.
        self._report_period: Optional[str] = None
        # The latest date of the content.
        self._report_refresh_date: Optional[Date] = None
        # The number of active users on SharePoint. Any user who viewed or edited files, shared files internally or externally, synced files, or viewed SharePoint pages is considered an active user.
        self._share_point_active: Optional[int] = None
        # The number of inactive users on SharePoint.
        self._share_point_inactive: Optional[int] = None
        # The number of active users on Skype For Business. Any user who organized or participated in conferences, or joined peer-to-peer sessions is considered an active user.
        self._skype_for_business_active: Optional[int] = None
        # The number of inactive users on Skype For Business.
        self._skype_for_business_inactive: Optional[int] = None
        # The number of active users on Microsoft Teams. Any user who posted messages in team channels, sent messages in private chat sessions, or participated in meetings or calls is considered an active user.
        self._teams_active: Optional[int] = None
        # The number of inactive users on Microsoft Teams.
        self._teams_inactive: Optional[int] = None
        # The number of active users on Yammer. Any user who can post, read, or like messages is considered an active user.
        self._yammer_active: Optional[int] = None
        # The number of inactive users on Yammer.
        self._yammer_inactive: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Office365ServicesUserCounts:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Office365ServicesUserCounts
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Office365ServicesUserCounts()
    
    @property
    def exchange_active(self,) -> Optional[int]:
        """
        Gets the exchangeActive property value. The number of active users on Exchange. Any user who can read and send email is considered an active user.
        Returns: Optional[int]
        """
        return self._exchange_active
    
    @exchange_active.setter
    def exchange_active(self,value: Optional[int] = None) -> None:
        """
        Sets the exchangeActive property value. The number of active users on Exchange. Any user who can read and send email is considered an active user.
        Args:
            value: Value to set for the exchangeActive property.
        """
        self._exchange_active = value
    
    @property
    def exchange_inactive(self,) -> Optional[int]:
        """
        Gets the exchangeInactive property value. The number of inactive users on Exchange.
        Returns: Optional[int]
        """
        return self._exchange_inactive
    
    @exchange_inactive.setter
    def exchange_inactive(self,value: Optional[int] = None) -> None:
        """
        Sets the exchangeInactive property value. The number of inactive users on Exchange.
        Args:
            value: Value to set for the exchangeInactive property.
        """
        self._exchange_inactive = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "exchange_active": lambda n : setattr(self, 'exchange_active', n.get_int_value()),
            "exchange_inactive": lambda n : setattr(self, 'exchange_inactive', n.get_int_value()),
            "office365_active": lambda n : setattr(self, 'office365_active', n.get_int_value()),
            "office365_inactive": lambda n : setattr(self, 'office365_inactive', n.get_int_value()),
            "one_drive_active": lambda n : setattr(self, 'one_drive_active', n.get_int_value()),
            "one_drive_inactive": lambda n : setattr(self, 'one_drive_inactive', n.get_int_value()),
            "report_period": lambda n : setattr(self, 'report_period', n.get_str_value()),
            "report_refresh_date": lambda n : setattr(self, 'report_refresh_date', n.get_object_value(Date)),
            "share_point_active": lambda n : setattr(self, 'share_point_active', n.get_int_value()),
            "share_point_inactive": lambda n : setattr(self, 'share_point_inactive', n.get_int_value()),
            "skype_for_business_active": lambda n : setattr(self, 'skype_for_business_active', n.get_int_value()),
            "skype_for_business_inactive": lambda n : setattr(self, 'skype_for_business_inactive', n.get_int_value()),
            "teams_active": lambda n : setattr(self, 'teams_active', n.get_int_value()),
            "teams_inactive": lambda n : setattr(self, 'teams_inactive', n.get_int_value()),
            "yammer_active": lambda n : setattr(self, 'yammer_active', n.get_int_value()),
            "yammer_inactive": lambda n : setattr(self, 'yammer_inactive', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def office365_active(self,) -> Optional[int]:
        """
        Gets the office365Active property value. The number of active users on Microsoft 365.
        Returns: Optional[int]
        """
        return self._office365_active
    
    @office365_active.setter
    def office365_active(self,value: Optional[int] = None) -> None:
        """
        Sets the office365Active property value. The number of active users on Microsoft 365.
        Args:
            value: Value to set for the office365Active property.
        """
        self._office365_active = value
    
    @property
    def office365_inactive(self,) -> Optional[int]:
        """
        Gets the office365Inactive property value. The number of inactive users on Microsoft 365.
        Returns: Optional[int]
        """
        return self._office365_inactive
    
    @office365_inactive.setter
    def office365_inactive(self,value: Optional[int] = None) -> None:
        """
        Sets the office365Inactive property value. The number of inactive users on Microsoft 365.
        Args:
            value: Value to set for the office365Inactive property.
        """
        self._office365_inactive = value
    
    @property
    def one_drive_active(self,) -> Optional[int]:
        """
        Gets the oneDriveActive property value. The number of active users on OneDrive. Any user who viewed or edited files, shared files internally or externally, or synced files is considered an active user.
        Returns: Optional[int]
        """
        return self._one_drive_active
    
    @one_drive_active.setter
    def one_drive_active(self,value: Optional[int] = None) -> None:
        """
        Sets the oneDriveActive property value. The number of active users on OneDrive. Any user who viewed or edited files, shared files internally or externally, or synced files is considered an active user.
        Args:
            value: Value to set for the oneDriveActive property.
        """
        self._one_drive_active = value
    
    @property
    def one_drive_inactive(self,) -> Optional[int]:
        """
        Gets the oneDriveInactive property value. The number of inactive users on OneDrive.
        Returns: Optional[int]
        """
        return self._one_drive_inactive
    
    @one_drive_inactive.setter
    def one_drive_inactive(self,value: Optional[int] = None) -> None:
        """
        Sets the oneDriveInactive property value. The number of inactive users on OneDrive.
        Args:
            value: Value to set for the oneDriveInactive property.
        """
        self._one_drive_inactive = value
    
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
        writer.write_int_value("exchangeActive", self.exchange_active)
        writer.write_int_value("exchangeInactive", self.exchange_inactive)
        writer.write_int_value("office365Active", self.office365_active)
        writer.write_int_value("office365Inactive", self.office365_inactive)
        writer.write_int_value("oneDriveActive", self.one_drive_active)
        writer.write_int_value("oneDriveInactive", self.one_drive_inactive)
        writer.write_str_value("reportPeriod", self.report_period)
        writer.write_object_value("reportRefreshDate", self.report_refresh_date)
        writer.write_int_value("sharePointActive", self.share_point_active)
        writer.write_int_value("sharePointInactive", self.share_point_inactive)
        writer.write_int_value("skypeForBusinessActive", self.skype_for_business_active)
        writer.write_int_value("skypeForBusinessInactive", self.skype_for_business_inactive)
        writer.write_int_value("teamsActive", self.teams_active)
        writer.write_int_value("teamsInactive", self.teams_inactive)
        writer.write_int_value("yammerActive", self.yammer_active)
        writer.write_int_value("yammerInactive", self.yammer_inactive)
    
    @property
    def share_point_active(self,) -> Optional[int]:
        """
        Gets the sharePointActive property value. The number of active users on SharePoint. Any user who viewed or edited files, shared files internally or externally, synced files, or viewed SharePoint pages is considered an active user.
        Returns: Optional[int]
        """
        return self._share_point_active
    
    @share_point_active.setter
    def share_point_active(self,value: Optional[int] = None) -> None:
        """
        Sets the sharePointActive property value. The number of active users on SharePoint. Any user who viewed or edited files, shared files internally or externally, synced files, or viewed SharePoint pages is considered an active user.
        Args:
            value: Value to set for the sharePointActive property.
        """
        self._share_point_active = value
    
    @property
    def share_point_inactive(self,) -> Optional[int]:
        """
        Gets the sharePointInactive property value. The number of inactive users on SharePoint.
        Returns: Optional[int]
        """
        return self._share_point_inactive
    
    @share_point_inactive.setter
    def share_point_inactive(self,value: Optional[int] = None) -> None:
        """
        Sets the sharePointInactive property value. The number of inactive users on SharePoint.
        Args:
            value: Value to set for the sharePointInactive property.
        """
        self._share_point_inactive = value
    
    @property
    def skype_for_business_active(self,) -> Optional[int]:
        """
        Gets the skypeForBusinessActive property value. The number of active users on Skype For Business. Any user who organized or participated in conferences, or joined peer-to-peer sessions is considered an active user.
        Returns: Optional[int]
        """
        return self._skype_for_business_active
    
    @skype_for_business_active.setter
    def skype_for_business_active(self,value: Optional[int] = None) -> None:
        """
        Sets the skypeForBusinessActive property value. The number of active users on Skype For Business. Any user who organized or participated in conferences, or joined peer-to-peer sessions is considered an active user.
        Args:
            value: Value to set for the skypeForBusinessActive property.
        """
        self._skype_for_business_active = value
    
    @property
    def skype_for_business_inactive(self,) -> Optional[int]:
        """
        Gets the skypeForBusinessInactive property value. The number of inactive users on Skype For Business.
        Returns: Optional[int]
        """
        return self._skype_for_business_inactive
    
    @skype_for_business_inactive.setter
    def skype_for_business_inactive(self,value: Optional[int] = None) -> None:
        """
        Sets the skypeForBusinessInactive property value. The number of inactive users on Skype For Business.
        Args:
            value: Value to set for the skypeForBusinessInactive property.
        """
        self._skype_for_business_inactive = value
    
    @property
    def teams_active(self,) -> Optional[int]:
        """
        Gets the teamsActive property value. The number of active users on Microsoft Teams. Any user who posted messages in team channels, sent messages in private chat sessions, or participated in meetings or calls is considered an active user.
        Returns: Optional[int]
        """
        return self._teams_active
    
    @teams_active.setter
    def teams_active(self,value: Optional[int] = None) -> None:
        """
        Sets the teamsActive property value. The number of active users on Microsoft Teams. Any user who posted messages in team channels, sent messages in private chat sessions, or participated in meetings or calls is considered an active user.
        Args:
            value: Value to set for the teamsActive property.
        """
        self._teams_active = value
    
    @property
    def teams_inactive(self,) -> Optional[int]:
        """
        Gets the teamsInactive property value. The number of inactive users on Microsoft Teams.
        Returns: Optional[int]
        """
        return self._teams_inactive
    
    @teams_inactive.setter
    def teams_inactive(self,value: Optional[int] = None) -> None:
        """
        Sets the teamsInactive property value. The number of inactive users on Microsoft Teams.
        Args:
            value: Value to set for the teamsInactive property.
        """
        self._teams_inactive = value
    
    @property
    def yammer_active(self,) -> Optional[int]:
        """
        Gets the yammerActive property value. The number of active users on Yammer. Any user who can post, read, or like messages is considered an active user.
        Returns: Optional[int]
        """
        return self._yammer_active
    
    @yammer_active.setter
    def yammer_active(self,value: Optional[int] = None) -> None:
        """
        Sets the yammerActive property value. The number of active users on Yammer. Any user who can post, read, or like messages is considered an active user.
        Args:
            value: Value to set for the yammerActive property.
        """
        self._yammer_active = value
    
    @property
    def yammer_inactive(self,) -> Optional[int]:
        """
        Gets the yammerInactive property value. The number of inactive users on Yammer.
        Returns: Optional[int]
        """
        return self._yammer_inactive
    
    @yammer_inactive.setter
    def yammer_inactive(self,value: Optional[int] = None) -> None:
        """
        Sets the yammerInactive property value. The number of inactive users on Yammer.
        Args:
            value: Value to set for the yammerInactive property.
        """
        self._yammer_inactive = value
    

