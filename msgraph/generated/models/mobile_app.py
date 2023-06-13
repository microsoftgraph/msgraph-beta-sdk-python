from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import android_for_work_app, android_lob_app, android_managed_store_app, android_managed_store_web_app, android_store_app, entity, iosi_pad_o_s_web_clip, ios_lob_app, ios_store_app, ios_vpp_app, mac_os_vpp_app, mac_o_s_dmg_app, mac_o_s_lob_app, mac_o_s_mdatp_app, mac_o_s_microsoft_defender_app, mac_o_s_microsoft_edge_app, mac_o_s_office_suite_app, mac_o_s_pkg_app, managed_android_lob_app, managed_android_store_app, managed_app, managed_i_o_s_lob_app, managed_i_o_s_store_app, managed_mobile_lob_app, microsoft_store_for_business_app, mime_content, mobile_app_assignment, mobile_app_category, mobile_app_publishing_state, mobile_app_relationship, mobile_lob_app, office_suite_app, web_app, win32_lob_app, windows_app_x, windows_microsoft_edge_app, windows_mobile_m_s_i, windows_phone81_app_x, windows_phone81_app_x_bundle, windows_phone81_store_app, windows_phone_x_a_p, windows_store_app, windows_universal_app_x, windows_web_app, win_get_app

from . import entity

@dataclass
class MobileApp(entity.Entity):
    """
    An abstract class containing the base properties for Intune mobile apps. Note: Listing mobile apps with `$expand=assignments` has been deprecated. Instead get the list of apps without the `$expand` query on `assignments`. Then, perform the expansion on individual applications.
    """
    # The list of group assignments for this mobile app.
    assignments: Optional[List[mobile_app_assignment.MobileAppAssignment]] = None
    # The list of categories for this app.
    categories: Optional[List[mobile_app_category.MobileAppCategory]] = None
    # The date and time the app was created.
    created_date_time: Optional[datetime] = None
    # The total number of dependencies the child app has.
    dependent_app_count: Optional[int] = None
    # The description of the app.
    description: Optional[str] = None
    # The developer of the app.
    developer: Optional[str] = None
    # The admin provided or imported title of the app.
    display_name: Optional[str] = None
    # The more information Url.
    information_url: Optional[str] = None
    # The value indicating whether the app is assigned to at least one group.
    is_assigned: Optional[bool] = None
    # The value indicating whether the app is marked as featured by the admin.
    is_featured: Optional[bool] = None
    # The large icon, to be displayed in the app details and used for upload of the icon.
    large_icon: Optional[mime_content.MimeContent] = None
    # The date and time the app was last modified.
    last_modified_date_time: Optional[datetime] = None
    # Notes for the app.
    notes: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The owner of the app.
    owner: Optional[str] = None
    # The privacy statement Url.
    privacy_information_url: Optional[str] = None
    # The publisher of the app.
    publisher: Optional[str] = None
    # Indicates the publishing state of an app.
    publishing_state: Optional[mobile_app_publishing_state.MobileAppPublishingState] = None
    # List of relationships for this mobile app.
    relationships: Optional[List[mobile_app_relationship.MobileAppRelationship]] = None
    # List of scope tag ids for this mobile app.
    role_scope_tag_ids: Optional[List[str]] = None
    # The total number of apps this app is directly or indirectly superseded by.
    superseded_app_count: Optional[int] = None
    # The total number of apps this app directly or indirectly supersedes.
    superseding_app_count: Optional[int] = None
    # The upload state.
    upload_state: Optional[int] = None
    
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
            if mapping_value == "#microsoft.graph.macOSPkgApp":
                from . import mac_o_s_pkg_app

                return mac_o_s_pkg_app.MacOSPkgApp()
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
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import android_for_work_app, android_lob_app, android_managed_store_app, android_managed_store_web_app, android_store_app, entity, iosi_pad_o_s_web_clip, ios_lob_app, ios_store_app, ios_vpp_app, mac_os_vpp_app, mac_o_s_dmg_app, mac_o_s_lob_app, mac_o_s_mdatp_app, mac_o_s_microsoft_defender_app, mac_o_s_microsoft_edge_app, mac_o_s_office_suite_app, mac_o_s_pkg_app, managed_android_lob_app, managed_android_store_app, managed_app, managed_i_o_s_lob_app, managed_i_o_s_store_app, managed_mobile_lob_app, microsoft_store_for_business_app, mime_content, mobile_app_assignment, mobile_app_category, mobile_app_publishing_state, mobile_app_relationship, mobile_lob_app, office_suite_app, web_app, win32_lob_app, windows_app_x, windows_microsoft_edge_app, windows_mobile_m_s_i, windows_phone81_app_x, windows_phone81_app_x_bundle, windows_phone81_store_app, windows_phone_x_a_p, windows_store_app, windows_universal_app_x, windows_web_app, win_get_app

        fields: Dict[str, Callable[[Any], None]] = {
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(mobile_app_assignment.MobileAppAssignment)),
            "categories": lambda n : setattr(self, 'categories', n.get_collection_of_object_values(mobile_app_category.MobileAppCategory)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "dependentAppCount": lambda n : setattr(self, 'dependent_app_count', n.get_int_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "developer": lambda n : setattr(self, 'developer', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "informationUrl": lambda n : setattr(self, 'information_url', n.get_str_value()),
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
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("informationUrl", self.information_url)
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
    

