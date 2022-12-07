from __future__ import annotations
from datetime import date
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class Office365ActiveUserDetail(entity.Entity):
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
            value: Value to set for the assignedProducts property.
        """
        self._assigned_products = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new Office365ActiveUserDetail and sets the default values.
        """
        super().__init__()
        # All the products assigned for the user.
        self._assigned_products: Optional[List[str]] = None
        # The date when the delete operation happened. Default value is 'null' when the user has not been deleted.
        self._deleted_date: Optional[Date] = None
        # The name displayed in the address book for the user. This is usually the combination of the user's first name, middle initial, and last name. This property is required when a user is created and it cannot be cleared during updates.
        self._display_name: Optional[str] = None
        # The date when user last read or sent email.
        self._exchange_last_activity_date: Optional[Date] = None
        # The last date when the user was assigned an Exchange license.
        self._exchange_license_assign_date: Optional[Date] = None
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
        self._one_drive_last_activity_date: Optional[Date] = None
        # The last date when the user was assigned a OneDrive license.
        self._one_drive_license_assign_date: Optional[Date] = None
        # The latest date of the content.
        self._report_refresh_date: Optional[Date] = None
        # The date when user last viewed or edited files, shared files internally or externally, synced files, or viewed SharePoint pages.
        self._share_point_last_activity_date: Optional[Date] = None
        # The last date when the user was assigned a SharePoint license.
        self._share_point_license_assign_date: Optional[Date] = None
        # The date when user last organized or participated in conferences, or joined peer-to-peer sessions.
        self._skype_for_business_last_activity_date: Optional[Date] = None
        # The last date when the user was assigned a Skype For Business license.
        self._skype_for_business_license_assign_date: Optional[Date] = None
        # The date when user last posted messages in team channels, sent messages in private chat sessions, or participated in meetings or calls.
        self._teams_last_activity_date: Optional[Date] = None
        # The last date when the user was assigned a Teams license.
        self._teams_license_assign_date: Optional[Date] = None
        # The user principal name (UPN) of the user. The UPN is an Internet-style login name for the user based on the Internet standard RFC 822. By convention, this should map to the user's email name. The general format is alias@domain, where domain must be present in the tenant’s collection of verified domains. This property is required when a user is created.
        self._user_principal_name: Optional[str] = None
        # The date when user last posted, read, or liked message.
        self._yammer_last_activity_date: Optional[Date] = None
        # The last date when the user was assigned a Yammer license.
        self._yammer_license_assign_date: Optional[Date] = None
    
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
    def deleted_date(self,) -> Optional[Date]:
        """
        Gets the deletedDate property value. The date when the delete operation happened. Default value is 'null' when the user has not been deleted.
        Returns: Optional[Date]
        """
        return self._deleted_date
    
    @deleted_date.setter
    def deleted_date(self,value: Optional[Date] = None) -> None:
        """
        Sets the deletedDate property value. The date when the delete operation happened. Default value is 'null' when the user has not been deleted.
        Args:
            value: Value to set for the deletedDate property.
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
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def exchange_last_activity_date(self,) -> Optional[Date]:
        """
        Gets the exchangeLastActivityDate property value. The date when user last read or sent email.
        Returns: Optional[Date]
        """
        return self._exchange_last_activity_date
    
    @exchange_last_activity_date.setter
    def exchange_last_activity_date(self,value: Optional[Date] = None) -> None:
        """
        Sets the exchangeLastActivityDate property value. The date when user last read or sent email.
        Args:
            value: Value to set for the exchangeLastActivityDate property.
        """
        self._exchange_last_activity_date = value
    
    @property
    def exchange_license_assign_date(self,) -> Optional[Date]:
        """
        Gets the exchangeLicenseAssignDate property value. The last date when the user was assigned an Exchange license.
        Returns: Optional[Date]
        """
        return self._exchange_license_assign_date
    
    @exchange_license_assign_date.setter
    def exchange_license_assign_date(self,value: Optional[Date] = None) -> None:
        """
        Sets the exchangeLicenseAssignDate property value. The last date when the user was assigned an Exchange license.
        Args:
            value: Value to set for the exchangeLicenseAssignDate property.
        """
        self._exchange_license_assign_date = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "assigned_products": lambda n : setattr(self, 'assigned_products', n.get_collection_of_primitive_values(str)),
            "deleted_date": lambda n : setattr(self, 'deleted_date', n.get_object_value(Date)),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "exchange_last_activity_date": lambda n : setattr(self, 'exchange_last_activity_date', n.get_object_value(Date)),
            "exchange_license_assign_date": lambda n : setattr(self, 'exchange_license_assign_date', n.get_object_value(Date)),
            "has_exchange_license": lambda n : setattr(self, 'has_exchange_license', n.get_bool_value()),
            "has_one_drive_license": lambda n : setattr(self, 'has_one_drive_license', n.get_bool_value()),
            "has_share_point_license": lambda n : setattr(self, 'has_share_point_license', n.get_bool_value()),
            "has_skype_for_business_license": lambda n : setattr(self, 'has_skype_for_business_license', n.get_bool_value()),
            "has_teams_license": lambda n : setattr(self, 'has_teams_license', n.get_bool_value()),
            "has_yammer_license": lambda n : setattr(self, 'has_yammer_license', n.get_bool_value()),
            "is_deleted": lambda n : setattr(self, 'is_deleted', n.get_bool_value()),
            "one_drive_last_activity_date": lambda n : setattr(self, 'one_drive_last_activity_date', n.get_object_value(Date)),
            "one_drive_license_assign_date": lambda n : setattr(self, 'one_drive_license_assign_date', n.get_object_value(Date)),
            "report_refresh_date": lambda n : setattr(self, 'report_refresh_date', n.get_object_value(Date)),
            "share_point_last_activity_date": lambda n : setattr(self, 'share_point_last_activity_date', n.get_object_value(Date)),
            "share_point_license_assign_date": lambda n : setattr(self, 'share_point_license_assign_date', n.get_object_value(Date)),
            "skype_for_business_last_activity_date": lambda n : setattr(self, 'skype_for_business_last_activity_date', n.get_object_value(Date)),
            "skype_for_business_license_assign_date": lambda n : setattr(self, 'skype_for_business_license_assign_date', n.get_object_value(Date)),
            "teams_last_activity_date": lambda n : setattr(self, 'teams_last_activity_date', n.get_object_value(Date)),
            "teams_license_assign_date": lambda n : setattr(self, 'teams_license_assign_date', n.get_object_value(Date)),
            "user_principal_name": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
            "yammer_last_activity_date": lambda n : setattr(self, 'yammer_last_activity_date', n.get_object_value(Date)),
            "yammer_license_assign_date": lambda n : setattr(self, 'yammer_license_assign_date', n.get_object_value(Date)),
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
            value: Value to set for the hasExchangeLicense property.
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
            value: Value to set for the hasOneDriveLicense property.
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
            value: Value to set for the hasSharePointLicense property.
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
            value: Value to set for the hasSkypeForBusinessLicense property.
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
            value: Value to set for the hasTeamsLicense property.
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
            value: Value to set for the hasYammerLicense property.
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
            value: Value to set for the isDeleted property.
        """
        self._is_deleted = value
    
    @property
    def one_drive_last_activity_date(self,) -> Optional[Date]:
        """
        Gets the oneDriveLastActivityDate property value. The date when user last viewed or edited files, shared files internally or externally, or synced files.
        Returns: Optional[Date]
        """
        return self._one_drive_last_activity_date
    
    @one_drive_last_activity_date.setter
    def one_drive_last_activity_date(self,value: Optional[Date] = None) -> None:
        """
        Sets the oneDriveLastActivityDate property value. The date when user last viewed or edited files, shared files internally or externally, or synced files.
        Args:
            value: Value to set for the oneDriveLastActivityDate property.
        """
        self._one_drive_last_activity_date = value
    
    @property
    def one_drive_license_assign_date(self,) -> Optional[Date]:
        """
        Gets the oneDriveLicenseAssignDate property value. The last date when the user was assigned a OneDrive license.
        Returns: Optional[Date]
        """
        return self._one_drive_license_assign_date
    
    @one_drive_license_assign_date.setter
    def one_drive_license_assign_date(self,value: Optional[Date] = None) -> None:
        """
        Sets the oneDriveLicenseAssignDate property value. The last date when the user was assigned a OneDrive license.
        Args:
            value: Value to set for the oneDriveLicenseAssignDate property.
        """
        self._one_drive_license_assign_date = value
    
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
        writer.write_collection_of_primitive_values("assignedProducts", self.assigned_products)
        writer.write_object_value("deletedDate", self.deleted_date)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("exchangeLastActivityDate", self.exchange_last_activity_date)
        writer.write_object_value("exchangeLicenseAssignDate", self.exchange_license_assign_date)
        writer.write_bool_value("hasExchangeLicense", self.has_exchange_license)
        writer.write_bool_value("hasOneDriveLicense", self.has_one_drive_license)
        writer.write_bool_value("hasSharePointLicense", self.has_share_point_license)
        writer.write_bool_value("hasSkypeForBusinessLicense", self.has_skype_for_business_license)
        writer.write_bool_value("hasTeamsLicense", self.has_teams_license)
        writer.write_bool_value("hasYammerLicense", self.has_yammer_license)
        writer.write_bool_value("isDeleted", self.is_deleted)
        writer.write_object_value("oneDriveLastActivityDate", self.one_drive_last_activity_date)
        writer.write_object_value("oneDriveLicenseAssignDate", self.one_drive_license_assign_date)
        writer.write_object_value("reportRefreshDate", self.report_refresh_date)
        writer.write_object_value("sharePointLastActivityDate", self.share_point_last_activity_date)
        writer.write_object_value("sharePointLicenseAssignDate", self.share_point_license_assign_date)
        writer.write_object_value("skypeForBusinessLastActivityDate", self.skype_for_business_last_activity_date)
        writer.write_object_value("skypeForBusinessLicenseAssignDate", self.skype_for_business_license_assign_date)
        writer.write_object_value("teamsLastActivityDate", self.teams_last_activity_date)
        writer.write_object_value("teamsLicenseAssignDate", self.teams_license_assign_date)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
        writer.write_object_value("yammerLastActivityDate", self.yammer_last_activity_date)
        writer.write_object_value("yammerLicenseAssignDate", self.yammer_license_assign_date)
    
    @property
    def share_point_last_activity_date(self,) -> Optional[Date]:
        """
        Gets the sharePointLastActivityDate property value. The date when user last viewed or edited files, shared files internally or externally, synced files, or viewed SharePoint pages.
        Returns: Optional[Date]
        """
        return self._share_point_last_activity_date
    
    @share_point_last_activity_date.setter
    def share_point_last_activity_date(self,value: Optional[Date] = None) -> None:
        """
        Sets the sharePointLastActivityDate property value. The date when user last viewed or edited files, shared files internally or externally, synced files, or viewed SharePoint pages.
        Args:
            value: Value to set for the sharePointLastActivityDate property.
        """
        self._share_point_last_activity_date = value
    
    @property
    def share_point_license_assign_date(self,) -> Optional[Date]:
        """
        Gets the sharePointLicenseAssignDate property value. The last date when the user was assigned a SharePoint license.
        Returns: Optional[Date]
        """
        return self._share_point_license_assign_date
    
    @share_point_license_assign_date.setter
    def share_point_license_assign_date(self,value: Optional[Date] = None) -> None:
        """
        Sets the sharePointLicenseAssignDate property value. The last date when the user was assigned a SharePoint license.
        Args:
            value: Value to set for the sharePointLicenseAssignDate property.
        """
        self._share_point_license_assign_date = value
    
    @property
    def skype_for_business_last_activity_date(self,) -> Optional[Date]:
        """
        Gets the skypeForBusinessLastActivityDate property value. The date when user last organized or participated in conferences, or joined peer-to-peer sessions.
        Returns: Optional[Date]
        """
        return self._skype_for_business_last_activity_date
    
    @skype_for_business_last_activity_date.setter
    def skype_for_business_last_activity_date(self,value: Optional[Date] = None) -> None:
        """
        Sets the skypeForBusinessLastActivityDate property value. The date when user last organized or participated in conferences, or joined peer-to-peer sessions.
        Args:
            value: Value to set for the skypeForBusinessLastActivityDate property.
        """
        self._skype_for_business_last_activity_date = value
    
    @property
    def skype_for_business_license_assign_date(self,) -> Optional[Date]:
        """
        Gets the skypeForBusinessLicenseAssignDate property value. The last date when the user was assigned a Skype For Business license.
        Returns: Optional[Date]
        """
        return self._skype_for_business_license_assign_date
    
    @skype_for_business_license_assign_date.setter
    def skype_for_business_license_assign_date(self,value: Optional[Date] = None) -> None:
        """
        Sets the skypeForBusinessLicenseAssignDate property value. The last date when the user was assigned a Skype For Business license.
        Args:
            value: Value to set for the skypeForBusinessLicenseAssignDate property.
        """
        self._skype_for_business_license_assign_date = value
    
    @property
    def teams_last_activity_date(self,) -> Optional[Date]:
        """
        Gets the teamsLastActivityDate property value. The date when user last posted messages in team channels, sent messages in private chat sessions, or participated in meetings or calls.
        Returns: Optional[Date]
        """
        return self._teams_last_activity_date
    
    @teams_last_activity_date.setter
    def teams_last_activity_date(self,value: Optional[Date] = None) -> None:
        """
        Sets the teamsLastActivityDate property value. The date when user last posted messages in team channels, sent messages in private chat sessions, or participated in meetings or calls.
        Args:
            value: Value to set for the teamsLastActivityDate property.
        """
        self._teams_last_activity_date = value
    
    @property
    def teams_license_assign_date(self,) -> Optional[Date]:
        """
        Gets the teamsLicenseAssignDate property value. The last date when the user was assigned a Teams license.
        Returns: Optional[Date]
        """
        return self._teams_license_assign_date
    
    @teams_license_assign_date.setter
    def teams_license_assign_date(self,value: Optional[Date] = None) -> None:
        """
        Sets the teamsLicenseAssignDate property value. The last date when the user was assigned a Teams license.
        Args:
            value: Value to set for the teamsLicenseAssignDate property.
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
            value: Value to set for the userPrincipalName property.
        """
        self._user_principal_name = value
    
    @property
    def yammer_last_activity_date(self,) -> Optional[Date]:
        """
        Gets the yammerLastActivityDate property value. The date when user last posted, read, or liked message.
        Returns: Optional[Date]
        """
        return self._yammer_last_activity_date
    
    @yammer_last_activity_date.setter
    def yammer_last_activity_date(self,value: Optional[Date] = None) -> None:
        """
        Sets the yammerLastActivityDate property value. The date when user last posted, read, or liked message.
        Args:
            value: Value to set for the yammerLastActivityDate property.
        """
        self._yammer_last_activity_date = value
    
    @property
    def yammer_license_assign_date(self,) -> Optional[Date]:
        """
        Gets the yammerLicenseAssignDate property value. The last date when the user was assigned a Yammer license.
        Returns: Optional[Date]
        """
        return self._yammer_license_assign_date
    
    @yammer_license_assign_date.setter
    def yammer_license_assign_date(self,value: Optional[Date] = None) -> None:
        """
        Sets the yammerLicenseAssignDate property value. The last date when the user was assigned a Yammer license.
        Args:
            value: Value to set for the yammerLicenseAssignDate property.
        """
        self._yammer_license_assign_date = value
    

