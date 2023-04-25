from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import android_for_work_app, android_lob_app, android_managed_store_app, android_managed_store_web_app, android_store_app, entity, iosi_pad_o_s_web_clip, ios_lob_app, ios_store_app, ios_vpp_app, mac_os_vpp_app, mac_o_s_dmg_app, mac_o_s_lob_app, mac_o_s_mdatp_app, mac_o_s_microsoft_defender_app, mac_o_s_microsoft_edge_app, mac_o_s_office_suite_app, managed_android_lob_app, managed_android_store_app, managed_app, managed_i_o_s_lob_app, managed_i_o_s_store_app, managed_mobile_lob_app, microsoft_store_for_business_app, mime_content, mobile_app_assignment, mobile_app_category, mobile_app_install_status, mobile_app_install_summary, mobile_app_publishing_state, mobile_app_relationship, mobile_lob_app, office_suite_app, user_app_install_status, web_app, win32_lob_app, windows_app_x, windows_microsoft_edge_app, windows_mobile_m_s_i, windows_phone81_app_x, windows_phone81_app_x_bundle, windows_phone81_store_app, windows_phone_x_a_p, windows_store_app, windows_universal_app_x, windows_web_app, win_get_app

from . import entity

class MobileApp(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new MobileApp and sets the default values.
        """
        super().__init__()
        # The list of group assignments for this mobile app.
        self._assignments: Optional[List[mobile_app_assignment.MobileAppAssignment]] = None
        # The list of categories for this app.
        self._categories: Optional[List[mobile_app_category.MobileAppCategory]] = None
        # The date and time the app was created.
        self._created_date_time: Optional[datetime] = None
        # The total number of dependencies the child app has.
        self._dependent_app_count: Optional[int] = None
        # The description of the app.
        self._description: Optional[str] = None
        # The developer of the app.
        self._developer: Optional[str] = None
        # The list of installation states for this mobile app.
        self._device_statuses: Optional[List[mobile_app_install_status.MobileAppInstallStatus]] = None
        # The admin provided or imported title of the app.
        self._display_name: Optional[str] = None
        # The more information Url.
        self._information_url: Optional[str] = None
        # Mobile App Install Summary.
        self._install_summary: Optional[mobile_app_install_summary.MobileAppInstallSummary] = None
        # The value indicating whether the app is assigned to at least one group.
        self._is_assigned: Optional[bool] = None
        # The value indicating whether the app is marked as featured by the admin.
        self._is_featured: Optional[bool] = None
        # The large icon, to be displayed in the app details and used for upload of the icon.
        self._large_icon: Optional[mime_content.MimeContent] = None
        # The date and time the app was last modified.
        self._last_modified_date_time: Optional[datetime] = None
        # Notes for the app.
        self._notes: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The owner of the app.
        self._owner: Optional[str] = None
        # The privacy statement Url.
        self._privacy_information_url: Optional[str] = None
        # The publisher of the app.
        self._publisher: Optional[str] = None
        # Indicates the publishing state of an app.
        self._publishing_state: Optional[mobile_app_publishing_state.MobileAppPublishingState] = None
        # List of relationships for this mobile app.
        self._relationships: Optional[List[mobile_app_relationship.MobileAppRelationship]] = None
        # List of scope tag ids for this mobile app.
        self._role_scope_tag_ids: Optional[List[str]] = None
        # The total number of apps this app is directly or indirectly superseded by.
        self._superseded_app_count: Optional[int] = None
        # The total number of apps this app directly or indirectly supersedes.
        self._superseding_app_count: Optional[int] = None
        # The upload state.
        self._upload_state: Optional[int] = None
        # The list of installation states for this mobile app.
        self._user_statuses: Optional[List[user_app_install_status.UserAppInstallStatus]] = None
    
    @property
    def assignments(self,) -> Optional[List[mobile_app_assignment.MobileAppAssignment]]:
        """
        Gets the assignments property value. The list of group assignments for this mobile app.
        Returns: Optional[List[mobile_app_assignment.MobileAppAssignment]]
        """
        return self._assignments
    
    @assignments.setter
    def assignments(self,value: Optional[List[mobile_app_assignment.MobileAppAssignment]] = None) -> None:
        """
        Sets the assignments property value. The list of group assignments for this mobile app.
        Args:
            value: Value to set for the assignments property.
        """
        self._assignments = value
    
    @property
    def categories(self,) -> Optional[List[mobile_app_category.MobileAppCategory]]:
        """
        Gets the categories property value. The list of categories for this app.
        Returns: Optional[List[mobile_app_category.MobileAppCategory]]
        """
        return self._categories
    
    @categories.setter
    def categories(self,value: Optional[List[mobile_app_category.MobileAppCategory]] = None) -> None:
        """
        Sets the categories property value. The list of categories for this app.
        Args:
            value: Value to set for the categories property.
        """
        self._categories = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The date and time the app was created.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The date and time the app was created.
        Args:
            value: Value to set for the created_date_time property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MobileApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MobileApp
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.androidForWorkApp":
                from . import android_for_work_app

                return android_for_work_app.AndroidForWorkApp()
            if mapping_value == "#microsoft.graph.androidLobApp":
                from . import android_lob_app

                return android_lob_app.AndroidLobApp()
            if mapping_value == "#microsoft.graph.androidManagedStoreApp":
                from . import android_managed_store_app

                return android_managed_store_app.AndroidManagedStoreApp()
            if mapping_value == "#microsoft.graph.androidManagedStoreWebApp":
                from . import android_managed_store_web_app

                return android_managed_store_web_app.AndroidManagedStoreWebApp()
            if mapping_value == "#microsoft.graph.androidStoreApp":
                from . import android_store_app

                return android_store_app.AndroidStoreApp()
            if mapping_value == "#microsoft.graph.iosiPadOSWebClip":
                from . import iosi_pad_o_s_web_clip

                return iosi_pad_o_s_web_clip.IosiPadOSWebClip()
            if mapping_value == "#microsoft.graph.iosLobApp":
                from . import ios_lob_app

                return ios_lob_app.IosLobApp()
            if mapping_value == "#microsoft.graph.iosStoreApp":
                from . import ios_store_app

                return ios_store_app.IosStoreApp()
            if mapping_value == "#microsoft.graph.iosVppApp":
                from . import ios_vpp_app

                return ios_vpp_app.IosVppApp()
            if mapping_value == "#microsoft.graph.macOSDmgApp":
                from . import mac_o_s_dmg_app

                return mac_o_s_dmg_app.MacOSDmgApp()
            if mapping_value == "#microsoft.graph.macOSLobApp":
                from . import mac_o_s_lob_app

                return mac_o_s_lob_app.MacOSLobApp()
            if mapping_value == "#microsoft.graph.macOSMdatpApp":
                from . import mac_o_s_mdatp_app

                return mac_o_s_mdatp_app.MacOSMdatpApp()
            if mapping_value == "#microsoft.graph.macOSMicrosoftDefenderApp":
                from . import mac_o_s_microsoft_defender_app

                return mac_o_s_microsoft_defender_app.MacOSMicrosoftDefenderApp()
            if mapping_value == "#microsoft.graph.macOSMicrosoftEdgeApp":
                from . import mac_o_s_microsoft_edge_app

                return mac_o_s_microsoft_edge_app.MacOSMicrosoftEdgeApp()
            if mapping_value == "#microsoft.graph.macOSOfficeSuiteApp":
                from . import mac_o_s_office_suite_app

                return mac_o_s_office_suite_app.MacOSOfficeSuiteApp()
            if mapping_value == "#microsoft.graph.macOsVppApp":
                from . import mac_os_vpp_app

                return mac_os_vpp_app.MacOsVppApp()
            if mapping_value == "#microsoft.graph.managedAndroidLobApp":
                from . import managed_android_lob_app

                return managed_android_lob_app.ManagedAndroidLobApp()
            if mapping_value == "#microsoft.graph.managedAndroidStoreApp":
                from . import managed_android_store_app

                return managed_android_store_app.ManagedAndroidStoreApp()
            if mapping_value == "#microsoft.graph.managedApp":
                from . import managed_app

                return managed_app.ManagedApp()
            if mapping_value == "#microsoft.graph.managedIOSLobApp":
                from . import managed_i_o_s_lob_app

                return managed_i_o_s_lob_app.ManagedIOSLobApp()
            if mapping_value == "#microsoft.graph.managedIOSStoreApp":
                from . import managed_i_o_s_store_app

                return managed_i_o_s_store_app.ManagedIOSStoreApp()
            if mapping_value == "#microsoft.graph.managedMobileLobApp":
                from . import managed_mobile_lob_app

                return managed_mobile_lob_app.ManagedMobileLobApp()
            if mapping_value == "#microsoft.graph.microsoftStoreForBusinessApp":
                from . import microsoft_store_for_business_app

                return microsoft_store_for_business_app.MicrosoftStoreForBusinessApp()
            if mapping_value == "#microsoft.graph.mobileLobApp":
                from . import mobile_lob_app

                return mobile_lob_app.MobileLobApp()
            if mapping_value == "#microsoft.graph.officeSuiteApp":
                from . import office_suite_app

                return office_suite_app.OfficeSuiteApp()
            if mapping_value == "#microsoft.graph.webApp":
                from . import web_app

                return web_app.WebApp()
            if mapping_value == "#microsoft.graph.win32LobApp":
                from . import win32_lob_app

                return win32_lob_app.Win32LobApp()
            if mapping_value == "#microsoft.graph.windowsAppX":
                from . import windows_app_x

                return windows_app_x.WindowsAppX()
            if mapping_value == "#microsoft.graph.windowsMicrosoftEdgeApp":
                from . import windows_microsoft_edge_app

                return windows_microsoft_edge_app.WindowsMicrosoftEdgeApp()
            if mapping_value == "#microsoft.graph.windowsMobileMSI":
                from . import windows_mobile_m_s_i

                return windows_mobile_m_s_i.WindowsMobileMSI()
            if mapping_value == "#microsoft.graph.windowsPhone81AppX":
                from . import windows_phone81_app_x

                return windows_phone81_app_x.WindowsPhone81AppX()
            if mapping_value == "#microsoft.graph.windowsPhone81AppXBundle":
                from . import windows_phone81_app_x_bundle

                return windows_phone81_app_x_bundle.WindowsPhone81AppXBundle()
            if mapping_value == "#microsoft.graph.windowsPhone81StoreApp":
                from . import windows_phone81_store_app

                return windows_phone81_store_app.WindowsPhone81StoreApp()
            if mapping_value == "#microsoft.graph.windowsPhoneXAP":
                from . import windows_phone_x_a_p

                return windows_phone_x_a_p.WindowsPhoneXAP()
            if mapping_value == "#microsoft.graph.windowsStoreApp":
                from . import windows_store_app

                return windows_store_app.WindowsStoreApp()
            if mapping_value == "#microsoft.graph.windowsUniversalAppX":
                from . import windows_universal_app_x

                return windows_universal_app_x.WindowsUniversalAppX()
            if mapping_value == "#microsoft.graph.windowsWebApp":
                from . import windows_web_app

                return windows_web_app.WindowsWebApp()
            if mapping_value == "#microsoft.graph.winGetApp":
                from . import win_get_app

                return win_get_app.WinGetApp()
        return MobileApp()
    
    @property
    def dependent_app_count(self,) -> Optional[int]:
        """
        Gets the dependentAppCount property value. The total number of dependencies the child app has.
        Returns: Optional[int]
        """
        return self._dependent_app_count
    
    @dependent_app_count.setter
    def dependent_app_count(self,value: Optional[int] = None) -> None:
        """
        Sets the dependentAppCount property value. The total number of dependencies the child app has.
        Args:
            value: Value to set for the dependent_app_count property.
        """
        self._dependent_app_count = value
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. The description of the app.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. The description of the app.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def developer(self,) -> Optional[str]:
        """
        Gets the developer property value. The developer of the app.
        Returns: Optional[str]
        """
        return self._developer
    
    @developer.setter
    def developer(self,value: Optional[str] = None) -> None:
        """
        Sets the developer property value. The developer of the app.
        Args:
            value: Value to set for the developer property.
        """
        self._developer = value
    
    @property
    def device_statuses(self,) -> Optional[List[mobile_app_install_status.MobileAppInstallStatus]]:
        """
        Gets the deviceStatuses property value. The list of installation states for this mobile app.
        Returns: Optional[List[mobile_app_install_status.MobileAppInstallStatus]]
        """
        return self._device_statuses
    
    @device_statuses.setter
    def device_statuses(self,value: Optional[List[mobile_app_install_status.MobileAppInstallStatus]] = None) -> None:
        """
        Sets the deviceStatuses property value. The list of installation states for this mobile app.
        Args:
            value: Value to set for the device_statuses property.
        """
        self._device_statuses = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The admin provided or imported title of the app.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The admin provided or imported title of the app.
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import android_for_work_app, android_lob_app, android_managed_store_app, android_managed_store_web_app, android_store_app, entity, iosi_pad_o_s_web_clip, ios_lob_app, ios_store_app, ios_vpp_app, mac_os_vpp_app, mac_o_s_dmg_app, mac_o_s_lob_app, mac_o_s_mdatp_app, mac_o_s_microsoft_defender_app, mac_o_s_microsoft_edge_app, mac_o_s_office_suite_app, managed_android_lob_app, managed_android_store_app, managed_app, managed_i_o_s_lob_app, managed_i_o_s_store_app, managed_mobile_lob_app, microsoft_store_for_business_app, mime_content, mobile_app_assignment, mobile_app_category, mobile_app_install_status, mobile_app_install_summary, mobile_app_publishing_state, mobile_app_relationship, mobile_lob_app, office_suite_app, user_app_install_status, web_app, win32_lob_app, windows_app_x, windows_microsoft_edge_app, windows_mobile_m_s_i, windows_phone81_app_x, windows_phone81_app_x_bundle, windows_phone81_store_app, windows_phone_x_a_p, windows_store_app, windows_universal_app_x, windows_web_app, win_get_app

        fields: Dict[str, Callable[[Any], None]] = {
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(mobile_app_assignment.MobileAppAssignment)),
            "categories": lambda n : setattr(self, 'categories', n.get_collection_of_object_values(mobile_app_category.MobileAppCategory)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "dependentAppCount": lambda n : setattr(self, 'dependent_app_count', n.get_int_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "developer": lambda n : setattr(self, 'developer', n.get_str_value()),
            "deviceStatuses": lambda n : setattr(self, 'device_statuses', n.get_collection_of_object_values(mobile_app_install_status.MobileAppInstallStatus)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "informationUrl": lambda n : setattr(self, 'information_url', n.get_str_value()),
            "installSummary": lambda n : setattr(self, 'install_summary', n.get_object_value(mobile_app_install_summary.MobileAppInstallSummary)),
            "isAssigned": lambda n : setattr(self, 'is_assigned', n.get_bool_value()),
            "isFeatured": lambda n : setattr(self, 'is_featured', n.get_bool_value()),
            "largeIcon": lambda n : setattr(self, 'large_icon', n.get_object_value(mime_content.MimeContent)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "notes": lambda n : setattr(self, 'notes', n.get_str_value()),
            "owner": lambda n : setattr(self, 'owner', n.get_str_value()),
            "privacyInformationUrl": lambda n : setattr(self, 'privacy_information_url', n.get_str_value()),
            "publisher": lambda n : setattr(self, 'publisher', n.get_str_value()),
            "publishingState": lambda n : setattr(self, 'publishing_state', n.get_enum_value(mobile_app_publishing_state.MobileAppPublishingState)),
            "relationships": lambda n : setattr(self, 'relationships', n.get_collection_of_object_values(mobile_app_relationship.MobileAppRelationship)),
            "roleScopeTagIds": lambda n : setattr(self, 'role_scope_tag_ids', n.get_collection_of_primitive_values(str)),
            "supersededAppCount": lambda n : setattr(self, 'superseded_app_count', n.get_int_value()),
            "supersedingAppCount": lambda n : setattr(self, 'superseding_app_count', n.get_int_value()),
            "uploadState": lambda n : setattr(self, 'upload_state', n.get_int_value()),
            "userStatuses": lambda n : setattr(self, 'user_statuses', n.get_collection_of_object_values(user_app_install_status.UserAppInstallStatus)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def information_url(self,) -> Optional[str]:
        """
        Gets the informationUrl property value. The more information Url.
        Returns: Optional[str]
        """
        return self._information_url
    
    @information_url.setter
    def information_url(self,value: Optional[str] = None) -> None:
        """
        Sets the informationUrl property value. The more information Url.
        Args:
            value: Value to set for the information_url property.
        """
        self._information_url = value
    
    @property
    def install_summary(self,) -> Optional[mobile_app_install_summary.MobileAppInstallSummary]:
        """
        Gets the installSummary property value. Mobile App Install Summary.
        Returns: Optional[mobile_app_install_summary.MobileAppInstallSummary]
        """
        return self._install_summary
    
    @install_summary.setter
    def install_summary(self,value: Optional[mobile_app_install_summary.MobileAppInstallSummary] = None) -> None:
        """
        Sets the installSummary property value. Mobile App Install Summary.
        Args:
            value: Value to set for the install_summary property.
        """
        self._install_summary = value
    
    @property
    def is_assigned(self,) -> Optional[bool]:
        """
        Gets the isAssigned property value. The value indicating whether the app is assigned to at least one group.
        Returns: Optional[bool]
        """
        return self._is_assigned
    
    @is_assigned.setter
    def is_assigned(self,value: Optional[bool] = None) -> None:
        """
        Sets the isAssigned property value. The value indicating whether the app is assigned to at least one group.
        Args:
            value: Value to set for the is_assigned property.
        """
        self._is_assigned = value
    
    @property
    def is_featured(self,) -> Optional[bool]:
        """
        Gets the isFeatured property value. The value indicating whether the app is marked as featured by the admin.
        Returns: Optional[bool]
        """
        return self._is_featured
    
    @is_featured.setter
    def is_featured(self,value: Optional[bool] = None) -> None:
        """
        Sets the isFeatured property value. The value indicating whether the app is marked as featured by the admin.
        Args:
            value: Value to set for the is_featured property.
        """
        self._is_featured = value
    
    @property
    def large_icon(self,) -> Optional[mime_content.MimeContent]:
        """
        Gets the largeIcon property value. The large icon, to be displayed in the app details and used for upload of the icon.
        Returns: Optional[mime_content.MimeContent]
        """
        return self._large_icon
    
    @large_icon.setter
    def large_icon(self,value: Optional[mime_content.MimeContent] = None) -> None:
        """
        Sets the largeIcon property value. The large icon, to be displayed in the app details and used for upload of the icon.
        Args:
            value: Value to set for the large_icon property.
        """
        self._large_icon = value
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. The date and time the app was last modified.
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. The date and time the app was last modified.
        Args:
            value: Value to set for the last_modified_date_time property.
        """
        self._last_modified_date_time = value
    
    @property
    def notes(self,) -> Optional[str]:
        """
        Gets the notes property value. Notes for the app.
        Returns: Optional[str]
        """
        return self._notes
    
    @notes.setter
    def notes(self,value: Optional[str] = None) -> None:
        """
        Sets the notes property value. Notes for the app.
        Args:
            value: Value to set for the notes property.
        """
        self._notes = value
    
    @property
    def owner(self,) -> Optional[str]:
        """
        Gets the owner property value. The owner of the app.
        Returns: Optional[str]
        """
        return self._owner
    
    @owner.setter
    def owner(self,value: Optional[str] = None) -> None:
        """
        Sets the owner property value. The owner of the app.
        Args:
            value: Value to set for the owner property.
        """
        self._owner = value
    
    @property
    def privacy_information_url(self,) -> Optional[str]:
        """
        Gets the privacyInformationUrl property value. The privacy statement Url.
        Returns: Optional[str]
        """
        return self._privacy_information_url
    
    @privacy_information_url.setter
    def privacy_information_url(self,value: Optional[str] = None) -> None:
        """
        Sets the privacyInformationUrl property value. The privacy statement Url.
        Args:
            value: Value to set for the privacy_information_url property.
        """
        self._privacy_information_url = value
    
    @property
    def publisher(self,) -> Optional[str]:
        """
        Gets the publisher property value. The publisher of the app.
        Returns: Optional[str]
        """
        return self._publisher
    
    @publisher.setter
    def publisher(self,value: Optional[str] = None) -> None:
        """
        Sets the publisher property value. The publisher of the app.
        Args:
            value: Value to set for the publisher property.
        """
        self._publisher = value
    
    @property
    def publishing_state(self,) -> Optional[mobile_app_publishing_state.MobileAppPublishingState]:
        """
        Gets the publishingState property value. Indicates the publishing state of an app.
        Returns: Optional[mobile_app_publishing_state.MobileAppPublishingState]
        """
        return self._publishing_state
    
    @publishing_state.setter
    def publishing_state(self,value: Optional[mobile_app_publishing_state.MobileAppPublishingState] = None) -> None:
        """
        Sets the publishingState property value. Indicates the publishing state of an app.
        Args:
            value: Value to set for the publishing_state property.
        """
        self._publishing_state = value
    
    @property
    def relationships(self,) -> Optional[List[mobile_app_relationship.MobileAppRelationship]]:
        """
        Gets the relationships property value. List of relationships for this mobile app.
        Returns: Optional[List[mobile_app_relationship.MobileAppRelationship]]
        """
        return self._relationships
    
    @relationships.setter
    def relationships(self,value: Optional[List[mobile_app_relationship.MobileAppRelationship]] = None) -> None:
        """
        Sets the relationships property value. List of relationships for this mobile app.
        Args:
            value: Value to set for the relationships property.
        """
        self._relationships = value
    
    @property
    def role_scope_tag_ids(self,) -> Optional[List[str]]:
        """
        Gets the roleScopeTagIds property value. List of scope tag ids for this mobile app.
        Returns: Optional[List[str]]
        """
        return self._role_scope_tag_ids
    
    @role_scope_tag_ids.setter
    def role_scope_tag_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the roleScopeTagIds property value. List of scope tag ids for this mobile app.
        Args:
            value: Value to set for the role_scope_tag_ids property.
        """
        self._role_scope_tag_ids = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("assignments", self.assignments)
        writer.write_collection_of_object_values("categories", self.categories)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_int_value("dependentAppCount", self.dependent_app_count)
        writer.write_str_value("description", self.description)
        writer.write_str_value("developer", self.developer)
        writer.write_collection_of_object_values("deviceStatuses", self.device_statuses)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("informationUrl", self.information_url)
        writer.write_object_value("installSummary", self.install_summary)
        writer.write_bool_value("isAssigned", self.is_assigned)
        writer.write_bool_value("isFeatured", self.is_featured)
        writer.write_object_value("largeIcon", self.large_icon)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("notes", self.notes)
        writer.write_str_value("owner", self.owner)
        writer.write_str_value("privacyInformationUrl", self.privacy_information_url)
        writer.write_str_value("publisher", self.publisher)
        writer.write_enum_value("publishingState", self.publishing_state)
        writer.write_collection_of_object_values("relationships", self.relationships)
        writer.write_collection_of_primitive_values("roleScopeTagIds", self.role_scope_tag_ids)
        writer.write_int_value("supersededAppCount", self.superseded_app_count)
        writer.write_int_value("supersedingAppCount", self.superseding_app_count)
        writer.write_int_value("uploadState", self.upload_state)
        writer.write_collection_of_object_values("userStatuses", self.user_statuses)
    
    @property
    def superseded_app_count(self,) -> Optional[int]:
        """
        Gets the supersededAppCount property value. The total number of apps this app is directly or indirectly superseded by.
        Returns: Optional[int]
        """
        return self._superseded_app_count
    
    @superseded_app_count.setter
    def superseded_app_count(self,value: Optional[int] = None) -> None:
        """
        Sets the supersededAppCount property value. The total number of apps this app is directly or indirectly superseded by.
        Args:
            value: Value to set for the superseded_app_count property.
        """
        self._superseded_app_count = value
    
    @property
    def superseding_app_count(self,) -> Optional[int]:
        """
        Gets the supersedingAppCount property value. The total number of apps this app directly or indirectly supersedes.
        Returns: Optional[int]
        """
        return self._superseding_app_count
    
    @superseding_app_count.setter
    def superseding_app_count(self,value: Optional[int] = None) -> None:
        """
        Sets the supersedingAppCount property value. The total number of apps this app directly or indirectly supersedes.
        Args:
            value: Value to set for the superseding_app_count property.
        """
        self._superseding_app_count = value
    
    @property
    def upload_state(self,) -> Optional[int]:
        """
        Gets the uploadState property value. The upload state.
        Returns: Optional[int]
        """
        return self._upload_state
    
    @upload_state.setter
    def upload_state(self,value: Optional[int] = None) -> None:
        """
        Sets the uploadState property value. The upload state.
        Args:
            value: Value to set for the upload_state property.
        """
        self._upload_state = value
    
    @property
    def user_statuses(self,) -> Optional[List[user_app_install_status.UserAppInstallStatus]]:
        """
        Gets the userStatuses property value. The list of installation states for this mobile app.
        Returns: Optional[List[user_app_install_status.UserAppInstallStatus]]
        """
        return self._user_statuses
    
    @user_statuses.setter
    def user_statuses(self,value: Optional[List[user_app_install_status.UserAppInstallStatus]] = None) -> None:
        """
        Sets the userStatuses property value. The list of installation states for this mobile app.
        Args:
            value: Value to set for the user_statuses property.
        """
        self._user_statuses = value
    

