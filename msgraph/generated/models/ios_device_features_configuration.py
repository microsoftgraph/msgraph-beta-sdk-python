from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import apple_device_features_configuration_base, ios_certificate_profile_base, ios_home_screen_item, ios_home_screen_page, ios_notification_settings, ios_single_sign_on_extension, ios_single_sign_on_settings, ios_wallpaper_display_location, ios_web_content_filter_base, mime_content, single_sign_on_extension

from . import apple_device_features_configuration_base

@dataclass
class IosDeviceFeaturesConfiguration(apple_device_features_configuration_base.AppleDeviceFeaturesConfigurationBase):
    odata_type = "#microsoft.graph.iosDeviceFeaturesConfiguration"
    # Asset tag information for the device, displayed on the login window and lock screen.
    asset_tag_template: Optional[str] = None
    # Gets or sets iOS Web Content Filter settings, supervised mode only
    content_filter_settings: Optional[ios_web_content_filter_base.IosWebContentFilterBase] = None
    # A list of app and folders to appear on the Home Screen Dock. This collection can contain a maximum of 500 elements.
    home_screen_dock_icons: Optional[List[ios_home_screen_item.IosHomeScreenItem]] = None
    # Gets or sets the number of rows to render when configuring iOS home screen layout settings. If this value is configured, homeScreenGridWidth must be configured as well.
    home_screen_grid_height: Optional[int] = None
    # Gets or sets the number of columns to render when configuring iOS home screen layout settings. If this value is configured, homeScreenGridHeight must be configured as well.
    home_screen_grid_width: Optional[int] = None
    # A list of pages on the Home Screen. This collection can contain a maximum of 500 elements.
    home_screen_pages: Optional[List[ios_home_screen_page.IosHomeScreenPage]] = None
    # Identity Certificate for the renewal of Kerberos ticket used in single sign-on settings.
    identity_certificate_for_client_authentication: Optional[ios_certificate_profile_base.IosCertificateProfileBase] = None
    # Gets or sets a single sign-on extension profile.
    ios_single_sign_on_extension: Optional[ios_single_sign_on_extension.IosSingleSignOnExtension] = None
    # A footnote displayed on the login window and lock screen. Available in iOS 9.3.1 and later.
    lock_screen_footnote: Optional[str] = None
    # Notification settings for each bundle id. Applicable to devices in supervised mode only (iOS 9.3 and later). This collection can contain a maximum of 500 elements.
    notification_settings: Optional[List[ios_notification_settings.IosNotificationSettings]] = None
    # Gets or sets a single sign-on extension profile. Deprecated: use IOSSingleSignOnExtension instead.
    single_sign_on_extension: Optional[single_sign_on_extension.SingleSignOnExtension] = None
    # PKINIT Certificate for the authentication with single sign-on extension settings.
    single_sign_on_extension_pkinit_certificate: Optional[ios_certificate_profile_base.IosCertificateProfileBase] = None
    # The Kerberos login settings that enable apps on receiving devices to authenticate smoothly.
    single_sign_on_settings: Optional[ios_single_sign_on_settings.IosSingleSignOnSettings] = None
    # An enum type for wallpaper display location specifier.
    wallpaper_display_location: Optional[ios_wallpaper_display_location.IosWallpaperDisplayLocation] = None
    # A wallpaper image must be in either PNG or JPEG format. It requires a supervised device with iOS 8 or later version.
    wallpaper_image: Optional[mime_content.MimeContent] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IosDeviceFeaturesConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IosDeviceFeaturesConfiguration
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return IosDeviceFeaturesConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import apple_device_features_configuration_base, ios_certificate_profile_base, ios_home_screen_item, ios_home_screen_page, ios_notification_settings, ios_single_sign_on_extension, ios_single_sign_on_settings, ios_wallpaper_display_location, ios_web_content_filter_base, mime_content, single_sign_on_extension

        from . import apple_device_features_configuration_base, ios_certificate_profile_base, ios_home_screen_item, ios_home_screen_page, ios_notification_settings, ios_single_sign_on_extension, ios_single_sign_on_settings, ios_wallpaper_display_location, ios_web_content_filter_base, mime_content, single_sign_on_extension

        fields: Dict[str, Callable[[Any], None]] = {
            "assetTagTemplate": lambda n : setattr(self, 'asset_tag_template', n.get_str_value()),
            "contentFilterSettings": lambda n : setattr(self, 'content_filter_settings', n.get_object_value(ios_web_content_filter_base.IosWebContentFilterBase)),
            "homeScreenDockIcons": lambda n : setattr(self, 'home_screen_dock_icons', n.get_collection_of_object_values(ios_home_screen_item.IosHomeScreenItem)),
            "homeScreenGridHeight": lambda n : setattr(self, 'home_screen_grid_height', n.get_int_value()),
            "homeScreenGridWidth": lambda n : setattr(self, 'home_screen_grid_width', n.get_int_value()),
            "homeScreenPages": lambda n : setattr(self, 'home_screen_pages', n.get_collection_of_object_values(ios_home_screen_page.IosHomeScreenPage)),
            "identityCertificateForClientAuthentication": lambda n : setattr(self, 'identity_certificate_for_client_authentication', n.get_object_value(ios_certificate_profile_base.IosCertificateProfileBase)),
            "iosSingleSignOnExtension": lambda n : setattr(self, 'ios_single_sign_on_extension', n.get_object_value(ios_single_sign_on_extension.IosSingleSignOnExtension)),
            "lockScreenFootnote": lambda n : setattr(self, 'lock_screen_footnote', n.get_str_value()),
            "notificationSettings": lambda n : setattr(self, 'notification_settings', n.get_collection_of_object_values(ios_notification_settings.IosNotificationSettings)),
            "singleSignOnExtension": lambda n : setattr(self, 'single_sign_on_extension', n.get_object_value(single_sign_on_extension.SingleSignOnExtension)),
            "singleSignOnExtensionPkinitCertificate": lambda n : setattr(self, 'single_sign_on_extension_pkinit_certificate', n.get_object_value(ios_certificate_profile_base.IosCertificateProfileBase)),
            "singleSignOnSettings": lambda n : setattr(self, 'single_sign_on_settings', n.get_object_value(ios_single_sign_on_settings.IosSingleSignOnSettings)),
            "wallpaperDisplayLocation": lambda n : setattr(self, 'wallpaper_display_location', n.get_enum_value(ios_wallpaper_display_location.IosWallpaperDisplayLocation)),
            "wallpaperImage": lambda n : setattr(self, 'wallpaper_image', n.get_object_value(mime_content.MimeContent)),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("assetTagTemplate", self.asset_tag_template)
        writer.write_object_value("contentFilterSettings", self.content_filter_settings)
        writer.write_collection_of_object_values("homeScreenDockIcons", self.home_screen_dock_icons)
        writer.write_int_value("homeScreenGridHeight", self.home_screen_grid_height)
        writer.write_int_value("homeScreenGridWidth", self.home_screen_grid_width)
        writer.write_collection_of_object_values("homeScreenPages", self.home_screen_pages)
        writer.write_object_value("identityCertificateForClientAuthentication", self.identity_certificate_for_client_authentication)
        writer.write_object_value("iosSingleSignOnExtension", self.ios_single_sign_on_extension)
        writer.write_str_value("lockScreenFootnote", self.lock_screen_footnote)
        writer.write_collection_of_object_values("notificationSettings", self.notification_settings)
        writer.write_object_value("singleSignOnExtension", self.single_sign_on_extension)
        writer.write_object_value("singleSignOnExtensionPkinitCertificate", self.single_sign_on_extension_pkinit_certificate)
        writer.write_object_value("singleSignOnSettings", self.single_sign_on_settings)
        writer.write_enum_value("wallpaperDisplayLocation", self.wallpaper_display_location)
        writer.write_object_value("wallpaperImage", self.wallpaper_image)
    

