from __future__ import annotations
from datetime import date
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity

from . import entity

class Office365ActiveUserDetail(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new Office365ActiveUserDetail and sets the default values.
        """
        super().__init__()
        # All the products assigned for the user.
        self._assigned_products: Optional[List[str]] = None
        # The date when the delete operation happened. Default value is 'null' when the user has not been deleted.
        self._deleted_date: Optional[date] = None
        # The name displayed in the address book for the user. This is usually the combination of the user's first name, middle initial, and last name. This property is required when a user is created and it cannot be cleared during updates.
        self._display_name: Optional[str] = None
        # The date when user last read or sent email.
        self._exchange_last_activity_date: Optional[date] = None
        # The last date when the user was assigned an Exchange license.
        self._exchange_license_assign_date: Optional[date] = None
        # Whether the user has been assigned an Exchange license.
        self._has_exchange_license: Optional[bool] = None
        # Whether the user has been assigned a OneDrive license.
        self._has_one_drive_license: Optional[bool] = None
        # Whether the user has been assigned a SharePoint license.
        self._has_share_point_license: Optional[bool] = None
        # Whether the user has been assigned a Skype For Business license.
        self._has_skype_for_business_license: Optional[bool] = None
        # Whether the user has been assigned a Teams license.
        self._has_teams_license: Optional[bool] = None
        # Whether the user has been assigned a Yammer license.
        self._has_yammer_license: Optional[bool] = None
        # Whether this user has been deleted or soft deleted.
        self._is_deleted: Optional[bool] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The date when user last viewed or edited files, shared files internally or externally, or synced files.
        self._one_drive_last_activity_date: Optional[date] = None
        # The last date when the user was assigned a OneDrive license.
        self._one_drive_license_assign_date: Optional[date] = None
        # The latest date of the content.
        self._report_refresh_date: Optional[date] = None
        # The date when user last viewed or edited files, shared files internally or externally, synced files, or viewed SharePoint pages.
        self._share_point_last_activity_date: Optional[date] = None
        # The last date when the user was assigned a SharePoint license.
        self._share_point_license_assign_date: Optional[date] = None
        # The date when user last organized or participated in conferences, or joined peer-to-peer sessions.
        self._skype_for_business_last_activity_date: Optional[date] = None
        # The last date when the user was assigned a Skype For Business license.
        self._skype_for_business_license_assign_date: Optional[date] = None
        # The date when user last posted messages in team channels, sent messages in private chat sessions, or participated in meetings or calls.
        self._teams_last_activity_date: Optional[date] = None
        # The last date when the user was assigned a Teams license.
        self._teams_license_assign_date: Optional[date] = None
        # The user principal name (UPN) of the user. The UPN is an Internet-style login name for the user based on the Internet standard RFC 822. By convention, this should map to the user's email name. The general format is alias@domain, where domain must be present in the tenant’s collection of verified domains. This property is required when a user is created.
        self._user_principal_name: Optional[str] = None
        # The date when user last posted, read, or liked message.
        self._yammer_last_activity_date: Optional[date] = None
        # The last date when the user was assigned a Yammer license.
        self._yammer_license_assign_date: Optional[date] = None
    
    @property
    def assigned_products(self,) -> Optional[List[str]]:
        """
        Gets the assignedProducts property value. All the products assigned for the user.
        Returns: Optional[List[str]]
        """
        return self._assigned_products
    
    @assigned_products.setter
    def assigned_products(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the assignedProducts property value. All the products assigned for the user.
        Args:
            value: Value to set for the assigned_products property.
        """
        self._assigned_products = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Office365ActiveUserDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Office365ActiveUserDetail
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Office365ActiveUserDetail()
    
    @property
    def deleted_date(self,) -> Optional[date]:
        """
        Gets the deletedDate property value. The date when the delete operation happened. Default value is 'null' when the user has not been deleted.
        Returns: Optional[date]
        """
        return self._deleted_date
    
    @deleted_date.setter
    def deleted_date(self,value: Optional[date] = None) -> None:
        """
        Sets the deletedDate property value. The date when the delete operation happened. Default value is 'null' when the user has not been deleted.
        Args:
            value: Value to set for the deleted_date property.
        """
        self._deleted_date = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The name displayed in the address book for the user. This is usually the combination of the user's first name, middle initial, and last name. This property is required when a user is created and it cannot be cleared during updates.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The name displayed in the address book for the user. This is usually the combination of the user's first name, middle initial, and last name. This property is required when a user is created and it cannot be cleared during updates.
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    @property
    def exchange_last_activity_date(self,) -> Optional[date]:
        """
        Gets the exchangeLastActivityDate property value. The date when user last read or sent email.
        Returns: Optional[date]
        """
        return self._exchange_last_activity_date
    
    @exchange_last_activity_date.setter
    def exchange_last_activity_date(self,value: Optional[date] = None) -> None:
        """
        Sets the exchangeLastActivityDate property value. The date when user last read or sent email.
        Args:
            value: Value to set for the exchange_last_activity_date property.
        """
        self._exchange_last_activity_date = value
    
    @property
    def exchange_license_assign_date(self,) -> Optional[date]:
        """
        Gets the exchangeLicenseAssignDate property value. The last date when the user was assigned an Exchange license.
        Returns: Optional[date]
        """
        return self._exchange_license_assign_date
    
    @exchange_license_assign_date.setter
    def exchange_license_assign_date(self,value: Optional[date] = None) -> None:
        """
        Sets the exchangeLicenseAssignDate property value. The last date when the user was assigned an Exchange license.
        Args:
            value: Value to set for the exchange_license_assign_date property.
        """
        self._exchange_license_assign_date = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "assignedProducts": lambda n : setattr(self, 'assigned_products', n.get_collection_of_primitive_values(str)),
            "deletedDate": lambda n : setattr(self, 'deleted_date', n.get_date_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "exchangeLastActivityDate": lambda n : setattr(self, 'exchange_last_activity_date', n.get_date_value()),
            "exchangeLicenseAssignDate": lambda n : setattr(self, 'exchange_license_assign_date', n.get_date_value()),
            "hasExchangeLicense": lambda n : setattr(self, 'has_exchange_license', n.get_bool_value()),
            "hasOneDriveLicense": lambda n : setattr(self, 'has_one_drive_license', n.get_bool_value()),
            "hasSharePointLicense": lambda n : setattr(self, 'has_share_point_license', n.get_bool_value()),
            "hasSkypeForBusinessLicense": lambda n : setattr(self, 'has_skype_for_business_license', n.get_bool_value()),
            "hasTeamsLicense": lambda n : setattr(self, 'has_teams_license', n.get_bool_value()),
            "hasYammerLicense": lambda n : setattr(self, 'has_yammer_license', n.get_bool_value()),
            "isDeleted": lambda n : setattr(self, 'is_deleted', n.get_bool_value()),
            "oneDriveLastActivityDate": lambda n : setattr(self, 'one_drive_last_activity_date', n.get_date_value()),
            "oneDriveLicenseAssignDate": lambda n : setattr(self, 'one_drive_license_assign_date', n.get_date_value()),
            "reportRefreshDate": lambda n : setattr(self, 'report_refresh_date', n.get_date_value()),
            "sharePointLastActivityDate": lambda n : setattr(self, 'share_point_last_activity_date', n.get_date_value()),
            "sharePointLicenseAssignDate": lambda n : setattr(self, 'share_point_license_assign_date', n.get_date_value()),
            "skypeForBusinessLastActivityDate": lambda n : setattr(self, 'skype_for_business_last_activity_date', n.get_date_value()),
            "skypeForBusinessLicenseAssignDate": lambda n : setattr(self, 'skype_for_business_license_assign_date', n.get_date_value()),
            "teamsLastActivityDate": lambda n : setattr(self, 'teams_last_activity_date', n.get_date_value()),
            "teamsLicenseAssignDate": lambda n : setattr(self, 'teams_license_assign_date', n.get_date_value()),
            "userPrincipalName": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
            "yammerLastActivityDate": lambda n : setattr(self, 'yammer_last_activity_date', n.get_date_value()),
            "yammerLicenseAssignDate": lambda n : setattr(self, 'yammer_license_assign_date', n.get_date_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def has_exchange_license(self,) -> Optional[bool]:
        """
        Gets the hasExchangeLicense property value. Whether the user has been assigned an Exchange license.
        Returns: Optional[bool]
        """
        return self._has_exchange_license
    
    @has_exchange_license.setter
    def has_exchange_license(self,value: Optional[bool] = None) -> None:
        """
        Sets the hasExchangeLicense property value. Whether the user has been assigned an Exchange license.
        Args:
            value: Value to set for the has_exchange_license property.
        """
        self._has_exchange_license = value
    
    @property
    def has_one_drive_license(self,) -> Optional[bool]:
        """
        Gets the hasOneDriveLicense property value. Whether the user has been assigned a OneDrive license.
        Returns: Optional[bool]
        """
        return self._has_one_drive_license
    
    @has_one_drive_license.setter
    def has_one_drive_license(self,value: Optional[bool] = None) -> None:
        """
        Sets the hasOneDriveLicense property value. Whether the user has been assigned a OneDrive license.
        Args:
            value: Value to set for the has_one_drive_license property.
        """
        self._has_one_drive_license = value
    
    @property
    def has_share_point_license(self,) -> Optional[bool]:
        """
        Gets the hasSharePointLicense property value. Whether the user has been assigned a SharePoint license.
        Returns: Optional[bool]
        """
        return self._has_share_point_license
    
    @has_share_point_license.setter
    def has_share_point_license(self,value: Optional[bool] = None) -> None:
        """
        Sets the hasSharePointLicense property value. Whether the user has been assigned a SharePoint license.
        Args:
            value: Value to set for the has_share_point_license property.
        """
        self._has_share_point_license = value
    
    @property
    def has_skype_for_business_license(self,) -> Optional[bool]:
        """
        Gets the hasSkypeForBusinessLicense property value. Whether the user has been assigned a Skype For Business license.
        Returns: Optional[bool]
        """
        return self._has_skype_for_business_license
    
    @has_skype_for_business_license.setter
    def has_skype_for_business_license(self,value: Optional[bool] = None) -> None:
        """
        Sets the hasSkypeForBusinessLicense property value. Whether the user has been assigned a Skype For Business license.
        Args:
            value: Value to set for the has_skype_for_business_license property.
        """
        self._has_skype_for_business_license = value
    
    @property
    def has_teams_license(self,) -> Optional[bool]:
        """
        Gets the hasTeamsLicense property value. Whether the user has been assigned a Teams license.
        Returns: Optional[bool]
        """
        return self._has_teams_license
    
    @has_teams_license.setter
    def has_teams_license(self,value: Optional[bool] = None) -> None:
        """
        Sets the hasTeamsLicense property value. Whether the user has been assigned a Teams license.
        Args:
            value: Value to set for the has_teams_license property.
        """
        self._has_teams_license = value
    
    @property
    def has_yammer_license(self,) -> Optional[bool]:
        """
        Gets the hasYammerLicense property value. Whether the user has been assigned a Yammer license.
        Returns: Optional[bool]
        """
        return self._has_yammer_license
    
    @has_yammer_license.setter
    def has_yammer_license(self,value: Optional[bool] = None) -> None:
        """
        Sets the hasYammerLicense property value. Whether the user has been assigned a Yammer license.
        Args:
            value: Value to set for the has_yammer_license property.
        """
        self._has_yammer_license = value
    
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
            value: Value to set for the is_deleted property.
        """
        self._is_deleted = value
    
    @property
    def one_drive_last_activity_date(self,) -> Optional[date]:
        """
        Gets the oneDriveLastActivityDate property value. The date when user last viewed or edited files, shared files internally or externally, or synced files.
        Returns: Optional[date]
        """
        return self._one_drive_last_activity_date
    
    @one_drive_last_activity_date.setter
    def one_drive_last_activity_date(self,value: Optional[date] = None) -> None:
        """
        Sets the oneDriveLastActivityDate property value. The date when user last viewed or edited files, shared files internally or externally, or synced files.
        Args:
            value: Value to set for the one_drive_last_activity_date property.
        """
        self._one_drive_last_activity_date = value
    
    @property
    def one_drive_license_assign_date(self,) -> Optional[date]:
        """
        Gets the oneDriveLicenseAssignDate property value. The last date when the user was assigned a OneDrive license.
        Returns: Optional[date]
        """
        return self._one_drive_license_assign_date
    
    @one_drive_license_assign_date.setter
    def one_drive_license_assign_date(self,value: Optional[date] = None) -> None:
        """
        Sets the oneDriveLicenseAssignDate property value. The last date when the user was assigned a OneDrive license.
        Args:
            value: Value to set for the one_drive_license_assign_date property.
        """
        self._one_drive_license_assign_date = value
    
    @property
    def report_refresh_date(self,) -> Optional[date]:
        """
        Gets the reportRefreshDate property value. The latest date of the content.
        Returns: Optional[date]
        """
        return self._report_refresh_date
    
    @report_refresh_date.setter
    def report_refresh_date(self,value: Optional[date] = None) -> None:
        """
        Sets the reportRefreshDate property value. The latest date of the content.
        Args:
            value: Value to set for the report_refresh_date property.
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
        writer.write_collection_of_primitive_values("assignedProducts", self.assigned_products)
        writer.write_date_value("deletedDate", self.deleted_date)
        writer.write_str_value("displayName", self.display_name)
        writer.write_date_value("exchangeLastActivityDate", self.exchange_last_activity_date)
        writer.write_date_value("exchangeLicenseAssignDate", self.exchange_license_assign_date)
        writer.write_bool_value("hasExchangeLicense", self.has_exchange_license)
        writer.write_bool_value("hasOneDriveLicense", self.has_one_drive_license)
        writer.write_bool_value("hasSharePointLicense", self.has_share_point_license)
        writer.write_bool_value("hasSkypeForBusinessLicense", self.has_skype_for_business_license)
        writer.write_bool_value("hasTeamsLicense", self.has_teams_license)
        writer.write_bool_value("hasYammerLicense", self.has_yammer_license)
        writer.write_bool_value("isDeleted", self.is_deleted)
        writer.write_date_value("oneDriveLastActivityDate", self.one_drive_last_activity_date)
        writer.write_date_value("oneDriveLicenseAssignDate", self.one_drive_license_assign_date)
        writer.write_date_value("reportRefreshDate", self.report_refresh_date)
        writer.write_date_value("sharePointLastActivityDate", self.share_point_last_activity_date)
        writer.write_date_value("sharePointLicenseAssignDate", self.share_point_license_assign_date)
        writer.write_date_value("skypeForBusinessLastActivityDate", self.skype_for_business_last_activity_date)
        writer.write_date_value("skypeForBusinessLicenseAssignDate", self.skype_for_business_license_assign_date)
        writer.write_date_value("teamsLastActivityDate", self.teams_last_activity_date)
        writer.write_date_value("teamsLicenseAssignDate", self.teams_license_assign_date)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
        writer.write_date_value("yammerLastActivityDate", self.yammer_last_activity_date)
        writer.write_date_value("yammerLicenseAssignDate", self.yammer_license_assign_date)
    
    @property
    def share_point_last_activity_date(self,) -> Optional[date]:
        """
        Gets the sharePointLastActivityDate property value. The date when user last viewed or edited files, shared files internally or externally, synced files, or viewed SharePoint pages.
        Returns: Optional[date]
        """
        return self._share_point_last_activity_date
    
    @share_point_last_activity_date.setter
    def share_point_last_activity_date(self,value: Optional[date] = None) -> None:
        """
        Sets the sharePointLastActivityDate property value. The date when user last viewed or edited files, shared files internally or externally, synced files, or viewed SharePoint pages.
        Args:
            value: Value to set for the share_point_last_activity_date property.
        """
        self._share_point_last_activity_date = value
    
    @property
    def share_point_license_assign_date(self,) -> Optional[date]:
        """
        Gets the sharePointLicenseAssignDate property value. The last date when the user was assigned a SharePoint license.
        Returns: Optional[date]
        """
        return self._share_point_license_assign_date
    
    @share_point_license_assign_date.setter
    def share_point_license_assign_date(self,value: Optional[date] = None) -> None:
        """
        Sets the sharePointLicenseAssignDate property value. The last date when the user was assigned a SharePoint license.
        Args:
            value: Value to set for the share_point_license_assign_date property.
        """
        self._share_point_license_assign_date = value
    
    @property
    def skype_for_business_last_activity_date(self,) -> Optional[date]:
        """
        Gets the skypeForBusinessLastActivityDate property value. The date when user last organized or participated in conferences, or joined peer-to-peer sessions.
        Returns: Optional[date]
        """
        return self._skype_for_business_last_activity_date
    
    @skype_for_business_last_activity_date.setter
    def skype_for_business_last_activity_date(self,value: Optional[date] = None) -> None:
        """
        Sets the skypeForBusinessLastActivityDate property value. The date when user last organized or participated in conferences, or joined peer-to-peer sessions.
        Args:
            value: Value to set for the skype_for_business_last_activity_date property.
        """
        self._skype_for_business_last_activity_date = value
    
    @property
    def skype_for_business_license_assign_date(self,) -> Optional[date]:
        """
        Gets the skypeForBusinessLicenseAssignDate property value. The last date when the user was assigned a Skype For Business license.
        Returns: Optional[date]
        """
        return self._skype_for_business_license_assign_date
    
    @skype_for_business_license_assign_date.setter
    def skype_for_business_license_assign_date(self,value: Optional[date] = None) -> None:
        """
        Sets the skypeForBusinessLicenseAssignDate property value. The last date when the user was assigned a Skype For Business license.
        Args:
            value: Value to set for the skype_for_business_license_assign_date property.
        """
        self._skype_for_business_license_assign_date = value
    
    @property
    def teams_last_activity_date(self,) -> Optional[date]:
        """
        Gets the teamsLastActivityDate property value. The date when user last posted messages in team channels, sent messages in private chat sessions, or participated in meetings or calls.
        Returns: Optional[date]
        """
        return self._teams_last_activity_date
    
    @teams_last_activity_date.setter
    def teams_last_activity_date(self,value: Optional[date] = None) -> None:
        """
        Sets the teamsLastActivityDate property value. The date when user last posted messages in team channels, sent messages in private chat sessions, or participated in meetings or calls.
        Args:
            value: Value to set for the teams_last_activity_date property.
        """
        self._teams_last_activity_date = value
    
    @property
    def teams_license_assign_date(self,) -> Optional[date]:
        """
        Gets the teamsLicenseAssignDate property value. The last date when the user was assigned a Teams license.
        Returns: Optional[date]
        """
        return self._teams_license_assign_date
    
    @teams_license_assign_date.setter
    def teams_license_assign_date(self,value: Optional[date] = None) -> None:
        """
        Sets the teamsLicenseAssignDate property value. The last date when the user was assigned a Teams license.
        Args:
            value: Value to set for the teams_license_assign_date property.
        """
        self._teams_license_assign_date = value
    
    @property
    def user_principal_name(self,) -> Optional[str]:
        """
        Gets the userPrincipalName property value. The user principal name (UPN) of the user. The UPN is an Internet-style login name for the user based on the Internet standard RFC 822. By convention, this should map to the user's email name. The general format is alias@domain, where domain must be present in the tenant’s collection of verified domains. This property is required when a user is created.
        Returns: Optional[str]
        """
        return self._user_principal_name
    
    @user_principal_name.setter
    def user_principal_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userPrincipalName property value. The user principal name (UPN) of the user. The UPN is an Internet-style login name for the user based on the Internet standard RFC 822. By convention, this should map to the user's email name. The general format is alias@domain, where domain must be present in the tenant’s collection of verified domains. This property is required when a user is created.
        Args:
            value: Value to set for the user_principal_name property.
        """
        self._user_principal_name = value
    
    @property
    def yammer_last_activity_date(self,) -> Optional[date]:
        """
        Gets the yammerLastActivityDate property value. The date when user last posted, read, or liked message.
        Returns: Optional[date]
        """
        return self._yammer_last_activity_date
    
    @yammer_last_activity_date.setter
    def yammer_last_activity_date(self,value: Optional[date] = None) -> None:
        """
        Sets the yammerLastActivityDate property value. The date when user last posted, read, or liked message.
        Args:
            value: Value to set for the yammer_last_activity_date property.
        """
        self._yammer_last_activity_date = value
    
    @property
    def yammer_license_assign_date(self,) -> Optional[date]:
        """
        Gets the yammerLicenseAssignDate property value. The last date when the user was assigned a Yammer license.
        Returns: Optional[date]
        """
        return self._yammer_license_assign_date
    
    @yammer_license_assign_date.setter
    def yammer_license_assign_date(self,value: Optional[date] = None) -> None:
        """
        Sets the yammerLicenseAssignDate property value. The last date when the user was assigned a Yammer license.
        Args:
            value: Value to set for the yammer_license_assign_date property.
        """
        self._yammer_license_assign_date = value
    

