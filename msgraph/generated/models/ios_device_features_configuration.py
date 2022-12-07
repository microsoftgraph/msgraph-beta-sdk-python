from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

apple_device_features_configuration_base = lazy_import('msgraph.generated.models.apple_device_features_configuration_base')
ios_certificate_profile_base = lazy_import('msgraph.generated.models.ios_certificate_profile_base')
ios_home_screen_item = lazy_import('msgraph.generated.models.ios_home_screen_item')
ios_home_screen_page = lazy_import('msgraph.generated.models.ios_home_screen_page')
ios_notification_settings = lazy_import('msgraph.generated.models.ios_notification_settings')
ios_single_sign_on_extension = lazy_import('msgraph.generated.models.ios_single_sign_on_extension')
ios_single_sign_on_settings = lazy_import('msgraph.generated.models.ios_single_sign_on_settings')
ios_wallpaper_display_location = lazy_import('msgraph.generated.models.ios_wallpaper_display_location')
ios_web_content_filter_base = lazy_import('msgraph.generated.models.ios_web_content_filter_base')
mime_content = lazy_import('msgraph.generated.models.mime_content')
single_sign_on_extension = lazy_import('msgraph.generated.models.single_sign_on_extension')

class IosDeviceFeaturesConfiguration(apple_device_features_configuration_base.AppleDeviceFeaturesConfigurationBase):
    @property
    def asset_tag_template(self,) -> Optional[str]:
        """
        Gets the assetTagTemplate property value. Asset tag information for the device, displayed on the login window and lock screen.
        Returns: Optional[str]
        """
        return self._asset_tag_template
    
    @asset_tag_template.setter
    def asset_tag_template(self,value: Optional[str] = None) -> None:
        """
        Sets the assetTagTemplate property value. Asset tag information for the device, displayed on the login window and lock screen.
        Args:
            value: Value to set for the assetTagTemplate property.
        """
        self._asset_tag_template = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new IosDeviceFeaturesConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.iosDeviceFeaturesConfiguration"
        # Asset tag information for the device, displayed on the login window and lock screen.
        self._asset_tag_template: Optional[str] = None
        # Gets or sets iOS Web Content Filter settings, supervised mode only
        self._content_filter_settings: Optional[ios_web_content_filter_base.IosWebContentFilterBase] = None
        # A list of app and folders to appear on the Home Screen Dock. This collection can contain a maximum of 500 elements.
        self._home_screen_dock_icons: Optional[List[ios_home_screen_item.IosHomeScreenItem]] = None
        # Gets or sets the number of rows to render when configuring iOS home screen layout settings. If this value is configured, homeScreenGridWidth must be configured as well.
        self._home_screen_grid_height: Optional[int] = None
        # Gets or sets the number of columns to render when configuring iOS home screen layout settings. If this value is configured, homeScreenGridHeight must be configured as well.
        self._home_screen_grid_width: Optional[int] = None
        # A list of pages on the Home Screen. This collection can contain a maximum of 500 elements.
        self._home_screen_pages: Optional[List[ios_home_screen_page.IosHomeScreenPage]] = None
        # Identity Certificate for the renewal of Kerberos ticket used in single sign-on settings.
        self._identity_certificate_for_client_authentication: Optional[ios_certificate_profile_base.IosCertificateProfileBase] = None
        # Gets or sets a single sign-on extension profile.
        self._ios_single_sign_on_extension: Optional[ios_single_sign_on_extension.IosSingleSignOnExtension] = None
        # A footnote displayed on the login window and lock screen. Available in iOS 9.3.1 and later.
        self._lock_screen_footnote: Optional[str] = None
        # Notification settings for each bundle id. Applicable to devices in supervised mode only (iOS 9.3 and later). This collection can contain a maximum of 500 elements.
        self._notification_settings: Optional[List[ios_notification_settings.IosNotificationSettings]] = None
        # Gets or sets a single sign-on extension profile. Deprecated: use IOSSingleSignOnExtension instead.
        self._single_sign_on_extension: Optional[single_sign_on_extension.SingleSignOnExtension] = None
        # PKINIT Certificate for the authentication with single sign-on extension settings.
        self._single_sign_on_extension_pkinit_certificate: Optional[ios_certificate_profile_base.IosCertificateProfileBase] = None
        # The Kerberos login settings that enable apps on receiving devices to authenticate smoothly.
        self._single_sign_on_settings: Optional[ios_single_sign_on_settings.IosSingleSignOnSettings] = None
        # An enum type for wallpaper display location specifier.
        self._wallpaper_display_location: Optional[ios_wallpaper_display_location.IosWallpaperDisplayLocation] = None
        # A wallpaper image must be in either PNG or JPEG format. It requires a supervised device with iOS 8 or later version.
        self._wallpaper_image: Optional[mime_content.MimeContent] = None
    
    @property
    def content_filter_settings(self,) -> Optional[ios_web_content_filter_base.IosWebContentFilterBase]:
        """
        Gets the contentFilterSettings property value. Gets or sets iOS Web Content Filter settings, supervised mode only
        Returns: Optional[ios_web_content_filter_base.IosWebContentFilterBase]
        """
        return self._content_filter_settings
    
    @content_filter_settings.setter
    def content_filter_settings(self,value: Optional[ios_web_content_filter_base.IosWebContentFilterBase] = None) -> None:
        """
        Sets the contentFilterSettings property value. Gets or sets iOS Web Content Filter settings, supervised mode only
        Args:
            value: Value to set for the contentFilterSettings property.
        """
        self._content_filter_settings = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IosDeviceFeaturesConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IosDeviceFeaturesConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return IosDeviceFeaturesConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "asset_tag_template": lambda n : setattr(self, 'asset_tag_template', n.get_str_value()),
            "content_filter_settings": lambda n : setattr(self, 'content_filter_settings', n.get_object_value(ios_web_content_filter_base.IosWebContentFilterBase)),
            "home_screen_dock_icons": lambda n : setattr(self, 'home_screen_dock_icons', n.get_collection_of_object_values(ios_home_screen_item.IosHomeScreenItem)),
            "home_screen_grid_height": lambda n : setattr(self, 'home_screen_grid_height', n.get_int_value()),
            "home_screen_grid_width": lambda n : setattr(self, 'home_screen_grid_width', n.get_int_value()),
            "home_screen_pages": lambda n : setattr(self, 'home_screen_pages', n.get_collection_of_object_values(ios_home_screen_page.IosHomeScreenPage)),
            "identity_certificate_for_client_authentication": lambda n : setattr(self, 'identity_certificate_for_client_authentication', n.get_object_value(ios_certificate_profile_base.IosCertificateProfileBase)),
            "ios_single_sign_on_extension": lambda n : setattr(self, 'ios_single_sign_on_extension', n.get_object_value(ios_single_sign_on_extension.IosSingleSignOnExtension)),
            "lock_screen_footnote": lambda n : setattr(self, 'lock_screen_footnote', n.get_str_value()),
            "notification_settings": lambda n : setattr(self, 'notification_settings', n.get_collection_of_object_values(ios_notification_settings.IosNotificationSettings)),
            "single_sign_on_extension": lambda n : setattr(self, 'single_sign_on_extension', n.get_object_value(single_sign_on_extension.SingleSignOnExtension)),
            "single_sign_on_extension_pkinit_certificate": lambda n : setattr(self, 'single_sign_on_extension_pkinit_certificate', n.get_object_value(ios_certificate_profile_base.IosCertificateProfileBase)),
            "single_sign_on_settings": lambda n : setattr(self, 'single_sign_on_settings', n.get_object_value(ios_single_sign_on_settings.IosSingleSignOnSettings)),
            "wallpaper_display_location": lambda n : setattr(self, 'wallpaper_display_location', n.get_enum_value(ios_wallpaper_display_location.IosWallpaperDisplayLocation)),
            "wallpaper_image": lambda n : setattr(self, 'wallpaper_image', n.get_object_value(mime_content.MimeContent)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def home_screen_dock_icons(self,) -> Optional[List[ios_home_screen_item.IosHomeScreenItem]]:
        """
        Gets the homeScreenDockIcons property value. A list of app and folders to appear on the Home Screen Dock. This collection can contain a maximum of 500 elements.
        Returns: Optional[List[ios_home_screen_item.IosHomeScreenItem]]
        """
        return self._home_screen_dock_icons
    
    @home_screen_dock_icons.setter
    def home_screen_dock_icons(self,value: Optional[List[ios_home_screen_item.IosHomeScreenItem]] = None) -> None:
        """
        Sets the homeScreenDockIcons property value. A list of app and folders to appear on the Home Screen Dock. This collection can contain a maximum of 500 elements.
        Args:
            value: Value to set for the homeScreenDockIcons property.
        """
        self._home_screen_dock_icons = value
    
    @property
    def home_screen_grid_height(self,) -> Optional[int]:
        """
        Gets the homeScreenGridHeight property value. Gets or sets the number of rows to render when configuring iOS home screen layout settings. If this value is configured, homeScreenGridWidth must be configured as well.
        Returns: Optional[int]
        """
        return self._home_screen_grid_height
    
    @home_screen_grid_height.setter
    def home_screen_grid_height(self,value: Optional[int] = None) -> None:
        """
        Sets the homeScreenGridHeight property value. Gets or sets the number of rows to render when configuring iOS home screen layout settings. If this value is configured, homeScreenGridWidth must be configured as well.
        Args:
            value: Value to set for the homeScreenGridHeight property.
        """
        self._home_screen_grid_height = value
    
    @property
    def home_screen_grid_width(self,) -> Optional[int]:
        """
        Gets the homeScreenGridWidth property value. Gets or sets the number of columns to render when configuring iOS home screen layout settings. If this value is configured, homeScreenGridHeight must be configured as well.
        Returns: Optional[int]
        """
        return self._home_screen_grid_width
    
    @home_screen_grid_width.setter
    def home_screen_grid_width(self,value: Optional[int] = None) -> None:
        """
        Sets the homeScreenGridWidth property value. Gets or sets the number of columns to render when configuring iOS home screen layout settings. If this value is configured, homeScreenGridHeight must be configured as well.
        Args:
            value: Value to set for the homeScreenGridWidth property.
        """
        self._home_screen_grid_width = value
    
    @property
    def home_screen_pages(self,) -> Optional[List[ios_home_screen_page.IosHomeScreenPage]]:
        """
        Gets the homeScreenPages property value. A list of pages on the Home Screen. This collection can contain a maximum of 500 elements.
        Returns: Optional[List[ios_home_screen_page.IosHomeScreenPage]]
        """
        return self._home_screen_pages
    
    @home_screen_pages.setter
    def home_screen_pages(self,value: Optional[List[ios_home_screen_page.IosHomeScreenPage]] = None) -> None:
        """
        Sets the homeScreenPages property value. A list of pages on the Home Screen. This collection can contain a maximum of 500 elements.
        Args:
            value: Value to set for the homeScreenPages property.
        """
        self._home_screen_pages = value
    
    @property
    def identity_certificate_for_client_authentication(self,) -> Optional[ios_certificate_profile_base.IosCertificateProfileBase]:
        """
        Gets the identityCertificateForClientAuthentication property value. Identity Certificate for the renewal of Kerberos ticket used in single sign-on settings.
        Returns: Optional[ios_certificate_profile_base.IosCertificateProfileBase]
        """
        return self._identity_certificate_for_client_authentication
    
    @identity_certificate_for_client_authentication.setter
    def identity_certificate_for_client_authentication(self,value: Optional[ios_certificate_profile_base.IosCertificateProfileBase] = None) -> None:
        """
        Sets the identityCertificateForClientAuthentication property value. Identity Certificate for the renewal of Kerberos ticket used in single sign-on settings.
        Args:
            value: Value to set for the identityCertificateForClientAuthentication property.
        """
        self._identity_certificate_for_client_authentication = value
    
    @property
    def ios_single_sign_on_extension(self,) -> Optional[ios_single_sign_on_extension.IosSingleSignOnExtension]:
        """
        Gets the iosSingleSignOnExtension property value. Gets or sets a single sign-on extension profile.
        Returns: Optional[ios_single_sign_on_extension.IosSingleSignOnExtension]
        """
        return self._ios_single_sign_on_extension
    
    @ios_single_sign_on_extension.setter
    def ios_single_sign_on_extension(self,value: Optional[ios_single_sign_on_extension.IosSingleSignOnExtension] = None) -> None:
        """
        Sets the iosSingleSignOnExtension property value. Gets or sets a single sign-on extension profile.
        Args:
            value: Value to set for the iosSingleSignOnExtension property.
        """
        self._ios_single_sign_on_extension = value
    
    @property
    def lock_screen_footnote(self,) -> Optional[str]:
        """
        Gets the lockScreenFootnote property value. A footnote displayed on the login window and lock screen. Available in iOS 9.3.1 and later.
        Returns: Optional[str]
        """
        return self._lock_screen_footnote
    
    @lock_screen_footnote.setter
    def lock_screen_footnote(self,value: Optional[str] = None) -> None:
        """
        Sets the lockScreenFootnote property value. A footnote displayed on the login window and lock screen. Available in iOS 9.3.1 and later.
        Args:
            value: Value to set for the lockScreenFootnote property.
        """
        self._lock_screen_footnote = value
    
    @property
    def notification_settings(self,) -> Optional[List[ios_notification_settings.IosNotificationSettings]]:
        """
        Gets the notificationSettings property value. Notification settings for each bundle id. Applicable to devices in supervised mode only (iOS 9.3 and later). This collection can contain a maximum of 500 elements.
        Returns: Optional[List[ios_notification_settings.IosNotificationSettings]]
        """
        return self._notification_settings
    
    @notification_settings.setter
    def notification_settings(self,value: Optional[List[ios_notification_settings.IosNotificationSettings]] = None) -> None:
        """
        Sets the notificationSettings property value. Notification settings for each bundle id. Applicable to devices in supervised mode only (iOS 9.3 and later). This collection can contain a maximum of 500 elements.
        Args:
            value: Value to set for the notificationSettings property.
        """
        self._notification_settings = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
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
    
    @property
    def single_sign_on_extension(self,) -> Optional[single_sign_on_extension.SingleSignOnExtension]:
        """
        Gets the singleSignOnExtension property value. Gets or sets a single sign-on extension profile. Deprecated: use IOSSingleSignOnExtension instead.
        Returns: Optional[single_sign_on_extension.SingleSignOnExtension]
        """
        return self._single_sign_on_extension
    
    @single_sign_on_extension.setter
    def single_sign_on_extension(self,value: Optional[single_sign_on_extension.SingleSignOnExtension] = None) -> None:
        """
        Sets the singleSignOnExtension property value. Gets or sets a single sign-on extension profile. Deprecated: use IOSSingleSignOnExtension instead.
        Args:
            value: Value to set for the singleSignOnExtension property.
        """
        self._single_sign_on_extension = value
    
    @property
    def single_sign_on_extension_pkinit_certificate(self,) -> Optional[ios_certificate_profile_base.IosCertificateProfileBase]:
        """
        Gets the singleSignOnExtensionPkinitCertificate property value. PKINIT Certificate for the authentication with single sign-on extension settings.
        Returns: Optional[ios_certificate_profile_base.IosCertificateProfileBase]
        """
        return self._single_sign_on_extension_pkinit_certificate
    
    @single_sign_on_extension_pkinit_certificate.setter
    def single_sign_on_extension_pkinit_certificate(self,value: Optional[ios_certificate_profile_base.IosCertificateProfileBase] = None) -> None:
        """
        Sets the singleSignOnExtensionPkinitCertificate property value. PKINIT Certificate for the authentication with single sign-on extension settings.
        Args:
            value: Value to set for the singleSignOnExtensionPkinitCertificate property.
        """
        self._single_sign_on_extension_pkinit_certificate = value
    
    @property
    def single_sign_on_settings(self,) -> Optional[ios_single_sign_on_settings.IosSingleSignOnSettings]:
        """
        Gets the singleSignOnSettings property value. The Kerberos login settings that enable apps on receiving devices to authenticate smoothly.
        Returns: Optional[ios_single_sign_on_settings.IosSingleSignOnSettings]
        """
        return self._single_sign_on_settings
    
    @single_sign_on_settings.setter
    def single_sign_on_settings(self,value: Optional[ios_single_sign_on_settings.IosSingleSignOnSettings] = None) -> None:
        """
        Sets the singleSignOnSettings property value. The Kerberos login settings that enable apps on receiving devices to authenticate smoothly.
        Args:
            value: Value to set for the singleSignOnSettings property.
        """
        self._single_sign_on_settings = value
    
    @property
    def wallpaper_display_location(self,) -> Optional[ios_wallpaper_display_location.IosWallpaperDisplayLocation]:
        """
        Gets the wallpaperDisplayLocation property value. An enum type for wallpaper display location specifier.
        Returns: Optional[ios_wallpaper_display_location.IosWallpaperDisplayLocation]
        """
        return self._wallpaper_display_location
    
    @wallpaper_display_location.setter
    def wallpaper_display_location(self,value: Optional[ios_wallpaper_display_location.IosWallpaperDisplayLocation] = None) -> None:
        """
        Sets the wallpaperDisplayLocation property value. An enum type for wallpaper display location specifier.
        Args:
            value: Value to set for the wallpaperDisplayLocation property.
        """
        self._wallpaper_display_location = value
    
    @property
    def wallpaper_image(self,) -> Optional[mime_content.MimeContent]:
        """
        Gets the wallpaperImage property value. A wallpaper image must be in either PNG or JPEG format. It requires a supervised device with iOS 8 or later version.
        Returns: Optional[mime_content.MimeContent]
        """
        return self._wallpaper_image
    
    @wallpaper_image.setter
    def wallpaper_image(self,value: Optional[mime_content.MimeContent] = None) -> None:
        """
        Sets the wallpaperImage property value. A wallpaper image must be in either PNG or JPEG format. It requires a supervised device with iOS 8 or later version.
        Args:
            value: Value to set for the wallpaperImage property.
        """
        self._wallpaper_image = value
    

