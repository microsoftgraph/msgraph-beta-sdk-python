from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .apple_device_features_configuration_base import AppleDeviceFeaturesConfigurationBase
    from .ios_certificate_profile_base import IosCertificateProfileBase
    from .ios_home_screen_item import IosHomeScreenItem
    from .ios_home_screen_page import IosHomeScreenPage
    from .ios_notification_settings import IosNotificationSettings
    from .ios_single_sign_on_extension import IosSingleSignOnExtension
    from .ios_single_sign_on_settings import IosSingleSignOnSettings
    from .ios_wallpaper_display_location import IosWallpaperDisplayLocation
    from .ios_web_content_filter_base import IosWebContentFilterBase
    from .mime_content import MimeContent
    from .single_sign_on_extension import SingleSignOnExtension

from .apple_device_features_configuration_base import AppleDeviceFeaturesConfigurationBase

@dataclass
class IosDeviceFeaturesConfiguration(AppleDeviceFeaturesConfigurationBase):
    """
    iOS Device Features Configuration Profile.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.iosDeviceFeaturesConfiguration"
    # Asset tag information for the device, displayed on the login window and lock screen.
    asset_tag_template: Optional[str] = None
    # Gets or sets iOS Web Content Filter settings, supervised mode only
    content_filter_settings: Optional[IosWebContentFilterBase] = None
    # A list of app and folders to appear on the Home Screen Dock. This collection can contain a maximum of 500 elements.
    home_screen_dock_icons: Optional[List[IosHomeScreenItem]] = None
    # Gets or sets the number of rows to render when configuring iOS home screen layout settings. If this value is configured, homeScreenGridWidth must be configured as well.
    home_screen_grid_height: Optional[int] = None
    # Gets or sets the number of columns to render when configuring iOS home screen layout settings. If this value is configured, homeScreenGridHeight must be configured as well.
    home_screen_grid_width: Optional[int] = None
    # A list of pages on the Home Screen. This collection can contain a maximum of 500 elements.
    home_screen_pages: Optional[List[IosHomeScreenPage]] = None
    # Identity Certificate for the renewal of Kerberos ticket used in single sign-on settings.
    identity_certificate_for_client_authentication: Optional[IosCertificateProfileBase] = None
    # Gets or sets a single sign-on extension profile.
    ios_single_sign_on_extension: Optional[IosSingleSignOnExtension] = None
    # A footnote displayed on the login window and lock screen. Available in iOS 9.3.1 and later.
    lock_screen_footnote: Optional[str] = None
    # Notification settings for each bundle id. Applicable to devices in supervised mode only (iOS 9.3 and later). This collection can contain a maximum of 500 elements.
    notification_settings: Optional[List[IosNotificationSettings]] = None
    # Gets or sets a single sign-on extension profile. Deprecated: use IOSSingleSignOnExtension instead.
    single_sign_on_extension: Optional[SingleSignOnExtension] = None
    # PKINIT Certificate for the authentication with single sign-on extension settings.
    single_sign_on_extension_pkinit_certificate: Optional[IosCertificateProfileBase] = None
    # The Kerberos login settings that enable apps on receiving devices to authenticate smoothly.
    single_sign_on_settings: Optional[IosSingleSignOnSettings] = None
    # An enum type for wallpaper display location specifier.
    wallpaper_display_location: Optional[IosWallpaperDisplayLocation] = None
    # A wallpaper image must be in either PNG or JPEG format. It requires a supervised device with iOS 8 or later version.
    wallpaper_image: Optional[MimeContent] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IosDeviceFeaturesConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
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
        from .apple_device_features_configuration_base import AppleDeviceFeaturesConfigurationBase
        from .ios_certificate_profile_base import IosCertificateProfileBase
        from .ios_home_screen_item import IosHomeScreenItem
        from .ios_home_screen_page import IosHomeScreenPage
        from .ios_notification_settings import IosNotificationSettings
        from .ios_single_sign_on_extension import IosSingleSignOnExtension
        from .ios_single_sign_on_settings import IosSingleSignOnSettings
        from .ios_wallpaper_display_location import IosWallpaperDisplayLocation
        from .ios_web_content_filter_base import IosWebContentFilterBase
        from .mime_content import MimeContent
        from .single_sign_on_extension import SingleSignOnExtension

        from .apple_device_features_configuration_base import AppleDeviceFeaturesConfigurationBase
        from .ios_certificate_profile_base import IosCertificateProfileBase
        from .ios_home_screen_item import IosHomeScreenItem
        from .ios_home_screen_page import IosHomeScreenPage
        from .ios_notification_settings import IosNotificationSettings
        from .ios_single_sign_on_extension import IosSingleSignOnExtension
        from .ios_single_sign_on_settings import IosSingleSignOnSettings
        from .ios_wallpaper_display_location import IosWallpaperDisplayLocation
        from .ios_web_content_filter_base import IosWebContentFilterBase
        from .mime_content import MimeContent
        from .single_sign_on_extension import SingleSignOnExtension

        fields: Dict[str, Callable[[Any], None]] = {
            "assetTagTemplate": lambda n : setattr(self, 'asset_tag_template', n.get_str_value()),
            "contentFilterSettings": lambda n : setattr(self, 'content_filter_settings', n.get_object_value(IosWebContentFilterBase)),
            "homeScreenDockIcons": lambda n : setattr(self, 'home_screen_dock_icons', n.get_collection_of_object_values(IosHomeScreenItem)),
            "homeScreenGridHeight": lambda n : setattr(self, 'home_screen_grid_height', n.get_int_value()),
            "homeScreenGridWidth": lambda n : setattr(self, 'home_screen_grid_width', n.get_int_value()),
            "homeScreenPages": lambda n : setattr(self, 'home_screen_pages', n.get_collection_of_object_values(IosHomeScreenPage)),
            "identityCertificateForClientAuthentication": lambda n : setattr(self, 'identity_certificate_for_client_authentication', n.get_object_value(IosCertificateProfileBase)),
            "iosSingleSignOnExtension": lambda n : setattr(self, 'ios_single_sign_on_extension', n.get_object_value(IosSingleSignOnExtension)),
            "lockScreenFootnote": lambda n : setattr(self, 'lock_screen_footnote', n.get_str_value()),
            "notificationSettings": lambda n : setattr(self, 'notification_settings', n.get_collection_of_object_values(IosNotificationSettings)),
            "singleSignOnExtension": lambda n : setattr(self, 'single_sign_on_extension', n.get_object_value(SingleSignOnExtension)),
            "singleSignOnExtensionPkinitCertificate": lambda n : setattr(self, 'single_sign_on_extension_pkinit_certificate', n.get_object_value(IosCertificateProfileBase)),
            "singleSignOnSettings": lambda n : setattr(self, 'single_sign_on_settings', n.get_object_value(IosSingleSignOnSettings)),
            "wallpaperDisplayLocation": lambda n : setattr(self, 'wallpaper_display_location', n.get_enum_value(IosWallpaperDisplayLocation)),
            "wallpaperImage": lambda n : setattr(self, 'wallpaper_image', n.get_object_value(MimeContent)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
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
    

