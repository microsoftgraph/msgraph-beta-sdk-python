from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
login_page_layout_configuration = lazy_import('msgraph.generated.models.login_page_layout_configuration')
login_page_text_visibility_settings = lazy_import('msgraph.generated.models.login_page_text_visibility_settings')

class OrganizationalBrandingProperties(entity.Entity):
    @property
    def background_color(self,) -> Optional[str]:
        """
        Gets the backgroundColor property value. Color that appears in place of the background image in low-bandwidth connections. We recommend that you use the primary color of your banner logo or your organization color. Specify this in hexadecimal format, for example, white is #FFFFFF.
        Returns: Optional[str]
        """
        return self._background_color
    
    @background_color.setter
    def background_color(self,value: Optional[str] = None) -> None:
        """
        Sets the backgroundColor property value. Color that appears in place of the background image in low-bandwidth connections. We recommend that you use the primary color of your banner logo or your organization color. Specify this in hexadecimal format, for example, white is #FFFFFF.
        Args:
            value: Value to set for the backgroundColor property.
        """
        self._background_color = value
    
    @property
    def background_image(self,) -> Optional[bytes]:
        """
        Gets the backgroundImage property value. Image that appears as the background of the sign-in page. The allowed types are PNG or JPEG not smaller than 300 KB and not larger than 1920 × 1080 pixels. A smaller image will reduce bandwidth requirements and make the page load faster.
        Returns: Optional[bytes]
        """
        return self._background_image
    
    @background_image.setter
    def background_image(self,value: Optional[bytes] = None) -> None:
        """
        Sets the backgroundImage property value. Image that appears as the background of the sign-in page. The allowed types are PNG or JPEG not smaller than 300 KB and not larger than 1920 × 1080 pixels. A smaller image will reduce bandwidth requirements and make the page load faster.
        Args:
            value: Value to set for the backgroundImage property.
        """
        self._background_image = value
    
    @property
    def background_image_relative_url(self,) -> Optional[str]:
        """
        Gets the backgroundImageRelativeUrl property value. A relative URL for the backgroundImage property that is combined with a CDN base URL from the cdnList to provide the version served by a CDN. Read-only.
        Returns: Optional[str]
        """
        return self._background_image_relative_url
    
    @background_image_relative_url.setter
    def background_image_relative_url(self,value: Optional[str] = None) -> None:
        """
        Sets the backgroundImageRelativeUrl property value. A relative URL for the backgroundImage property that is combined with a CDN base URL from the cdnList to provide the version served by a CDN. Read-only.
        Args:
            value: Value to set for the backgroundImageRelativeUrl property.
        """
        self._background_image_relative_url = value
    
    @property
    def banner_logo(self,) -> Optional[bytes]:
        """
        Gets the bannerLogo property value. A banner version of your company logo that appears on the sign-in page. The allowed types are PNG or JPEG not larger than 36 × 245 pixels. We recommend using a transparent image with no padding around the logo.
        Returns: Optional[bytes]
        """
        return self._banner_logo
    
    @banner_logo.setter
    def banner_logo(self,value: Optional[bytes] = None) -> None:
        """
        Sets the bannerLogo property value. A banner version of your company logo that appears on the sign-in page. The allowed types are PNG or JPEG not larger than 36 × 245 pixels. We recommend using a transparent image with no padding around the logo.
        Args:
            value: Value to set for the bannerLogo property.
        """
        self._banner_logo = value
    
    @property
    def banner_logo_relative_url(self,) -> Optional[str]:
        """
        Gets the bannerLogoRelativeUrl property value. A relative URL for the bannerLogo property that is combined with a CDN base URL from the cdnList to provide the read-only version served by a CDN. Read-only.
        Returns: Optional[str]
        """
        return self._banner_logo_relative_url
    
    @banner_logo_relative_url.setter
    def banner_logo_relative_url(self,value: Optional[str] = None) -> None:
        """
        Sets the bannerLogoRelativeUrl property value. A relative URL for the bannerLogo property that is combined with a CDN base URL from the cdnList to provide the read-only version served by a CDN. Read-only.
        Args:
            value: Value to set for the bannerLogoRelativeUrl property.
        """
        self._banner_logo_relative_url = value
    
    @property
    def cdn_list(self,) -> Optional[List[str]]:
        """
        Gets the cdnList property value. A list of base URLs for all available CDN providers that are serving the assets of the current resource. Several CDN providers are used at the same time for high availability of read requests. Read-only.
        Returns: Optional[List[str]]
        """
        return self._cdn_list
    
    @cdn_list.setter
    def cdn_list(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the cdnList property value. A list of base URLs for all available CDN providers that are serving the assets of the current resource. Several CDN providers are used at the same time for high availability of read requests. Read-only.
        Args:
            value: Value to set for the cdnList property.
        """
        self._cdn_list = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new organizationalBrandingProperties and sets the default values.
        """
        super().__init__()
        # Color that appears in place of the background image in low-bandwidth connections. We recommend that you use the primary color of your banner logo or your organization color. Specify this in hexadecimal format, for example, white is #FFFFFF.
        self._background_color: Optional[str] = None
        # Image that appears as the background of the sign-in page. The allowed types are PNG or JPEG not smaller than 300 KB and not larger than 1920 × 1080 pixels. A smaller image will reduce bandwidth requirements and make the page load faster.
        self._background_image: Optional[bytes] = None
        # A relative URL for the backgroundImage property that is combined with a CDN base URL from the cdnList to provide the version served by a CDN. Read-only.
        self._background_image_relative_url: Optional[str] = None
        # A banner version of your company logo that appears on the sign-in page. The allowed types are PNG or JPEG not larger than 36 × 245 pixels. We recommend using a transparent image with no padding around the logo.
        self._banner_logo: Optional[bytes] = None
        # A relative URL for the bannerLogo property that is combined with a CDN base URL from the cdnList to provide the read-only version served by a CDN. Read-only.
        self._banner_logo_relative_url: Optional[str] = None
        # A list of base URLs for all available CDN providers that are serving the assets of the current resource. Several CDN providers are used at the same time for high availability of read requests. Read-only.
        self._cdn_list: Optional[List[str]] = None
        # A custom URL for resetting account credentials. This URL must be in ASCII format or non-ASCII characters must be URL encoded, and not exceed 128 characters.
        self._custom_account_reset_credentials_url: Optional[str] = None
        # A string to replace the default 'Can't access your account?' self-service password reset (SSPR) hyperlink text on the sign-in page. This text must be in Unicode format and not exceed 256 characters.
        self._custom_cannot_access_your_account_text: Optional[str] = None
        # A custom URL to replace the default URL of the self-service password reset (SSPR) 'Can't access your account?' hyperlink on the sign-in page. This URL must be in ASCII format or non-ASCII characters must be URL encoded, and not exceed 128 characters. DO NOT USE. Use customAccountResetCredentialsUrl instead.
        self._custom_cannot_access_your_account_url: Optional[str] = None
        # CSS styling that appears on the sign-in page. The allowed format is .css format only and not larger than 25 KB.
        self._custom_c_s_s: Optional[bytes] = None
        # A relative URL for the customCSS property that is combined with a CDN base URL from the cdnList to provide the version served by a CDN. Read-only.
        self._custom_c_s_s_relative_url: Optional[str] = None
        # A string to replace the default 'Forgot my password' hyperlink text on the sign-in form. This text must be in Unicode format and not exceed 256 characters.
        self._custom_forgot_my_password_text: Optional[str] = None
        # A string to replace the default 'Privacy and Cookies' hyperlink text in the footer. This text must be in Unicode format and not exceed 256 characters.
        self._custom_privacy_and_cookies_text: Optional[str] = None
        # A custom URL to replace the default URL of the 'Privacy and Cookies' hyperlink in the footer. This URL must be in ASCII format or non-ASCII characters must be URL encoded, and not exceed 128 characters.
        self._custom_privacy_and_cookies_url: Optional[str] = None
        # A string to replace the default 'reset it now' hyperlink text on the sign-in form. This text must be in Unicode format and not exceed 256 characters. DO NOT USE: Customization of the 'reset it now' hyperlink text is currently not supported.
        self._custom_reset_it_now_text: Optional[str] = None
        # A string to replace the the default 'Terms of Use' hyperlink text in the footer. This text must be in Unicode format and not exceed 256 characters.
        self._custom_terms_of_use_text: Optional[str] = None
        # A custom URL to replace the default URL of the 'Terms of Use' hyperlink in the footer. This URL must be in ASCII format or non-ASCII characters must be URL encoded, and not exceed 128characters.
        self._custom_terms_of_use_url: Optional[str] = None
        # A custom icon (favicon) to replace a default Microsoft product favicon on an Azure AD tenant.
        self._favicon: Optional[bytes] = None
        # A relative url for the favicon above that is combined with a CDN base URL from the cdnList to provide the version served by a CDN. Read-only.
        self._favicon_relative_url: Optional[str] = None
        # The RGB color to apply to customize the color of the header.
        self._header_background_color: Optional[str] = None
        # A company logo that appears in the header of the sign-in page. The allowed types are PNG or JPEG not larger than 36 × 245 pixels. We recommend using a transparent image with no padding around the logo.
        self._header_logo: Optional[bytes] = None
        # A relative URL for the headerLogo property that is combined with a CDN base URL from the cdnList to provide the read-only version served by a CDN. Read-only.
        self._header_logo_relative_url: Optional[str] = None
        # Represents the layout configuration to be displayed on the login page for a tenant.
        self._login_page_layout_configuration: Optional[login_page_layout_configuration.LoginPageLayoutConfiguration] = None
        # Represents the various texts that can be hidden on the login page for a tenant.
        self._login_page_text_visibility_settings: Optional[login_page_text_visibility_settings.LoginPageTextVisibilitySettings] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Text that appears at the bottom of the sign-in box. Use this to communicate additional information, such as the phone number to your help desk or a legal statement. This text must be in Unicode format and not exceed 1024 characters.
        self._sign_in_page_text: Optional[str] = None
        # A square version of your company logo that appears in Windows 10 out-of-box experiences (OOBE) and when Windows Autopilot is enabled for deployment. Allowed types are PNG or JPEG not larger than 240 x 240 pixels and not more than 10 KB in size. We recommend using a transparent image with no padding around the logo.
        self._square_logo: Optional[bytes] = None
        # A square dark version of your company logo that appears in Windows 10 out-of-box experiences (OOBE) and when Windows Autopilot is enabled for deployment. Allowed types are PNG or JPEG not larger than 240 x 240 pixels and not more than 10 KB in size. We recommend using a transparent image with no padding around the logo.
        self._square_logo_dark: Optional[bytes] = None
        # A relative URL for the squareLogoDark property that is combined with a CDN base URL from the cdnList to provide the version served by a CDN. Read-only.
        self._square_logo_dark_relative_url: Optional[str] = None
        # A relative URL for the squareLogo property that is combined with a CDN base URL from the cdnList to provide the version served by a CDN. Read-only.
        self._square_logo_relative_url: Optional[str] = None
        # A string that shows as the hint in the username textbox on the sign-in screen. This text must be a Unicode, without links or code, and can't exceed 64 characters.
        self._username_hint_text: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OrganizationalBrandingProperties:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OrganizationalBrandingProperties
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return OrganizationalBrandingProperties()
    
    @property
    def custom_account_reset_credentials_url(self,) -> Optional[str]:
        """
        Gets the customAccountResetCredentialsUrl property value. A custom URL for resetting account credentials. This URL must be in ASCII format or non-ASCII characters must be URL encoded, and not exceed 128 characters.
        Returns: Optional[str]
        """
        return self._custom_account_reset_credentials_url
    
    @custom_account_reset_credentials_url.setter
    def custom_account_reset_credentials_url(self,value: Optional[str] = None) -> None:
        """
        Sets the customAccountResetCredentialsUrl property value. A custom URL for resetting account credentials. This URL must be in ASCII format or non-ASCII characters must be URL encoded, and not exceed 128 characters.
        Args:
            value: Value to set for the customAccountResetCredentialsUrl property.
        """
        self._custom_account_reset_credentials_url = value
    
    @property
    def custom_cannot_access_your_account_text(self,) -> Optional[str]:
        """
        Gets the customCannotAccessYourAccountText property value. A string to replace the default 'Can't access your account?' self-service password reset (SSPR) hyperlink text on the sign-in page. This text must be in Unicode format and not exceed 256 characters.
        Returns: Optional[str]
        """
        return self._custom_cannot_access_your_account_text
    
    @custom_cannot_access_your_account_text.setter
    def custom_cannot_access_your_account_text(self,value: Optional[str] = None) -> None:
        """
        Sets the customCannotAccessYourAccountText property value. A string to replace the default 'Can't access your account?' self-service password reset (SSPR) hyperlink text on the sign-in page. This text must be in Unicode format and not exceed 256 characters.
        Args:
            value: Value to set for the customCannotAccessYourAccountText property.
        """
        self._custom_cannot_access_your_account_text = value
    
    @property
    def custom_cannot_access_your_account_url(self,) -> Optional[str]:
        """
        Gets the customCannotAccessYourAccountUrl property value. A custom URL to replace the default URL of the self-service password reset (SSPR) 'Can't access your account?' hyperlink on the sign-in page. This URL must be in ASCII format or non-ASCII characters must be URL encoded, and not exceed 128 characters. DO NOT USE. Use customAccountResetCredentialsUrl instead.
        Returns: Optional[str]
        """
        return self._custom_cannot_access_your_account_url
    
    @custom_cannot_access_your_account_url.setter
    def custom_cannot_access_your_account_url(self,value: Optional[str] = None) -> None:
        """
        Sets the customCannotAccessYourAccountUrl property value. A custom URL to replace the default URL of the self-service password reset (SSPR) 'Can't access your account?' hyperlink on the sign-in page. This URL must be in ASCII format or non-ASCII characters must be URL encoded, and not exceed 128 characters. DO NOT USE. Use customAccountResetCredentialsUrl instead.
        Args:
            value: Value to set for the customCannotAccessYourAccountUrl property.
        """
        self._custom_cannot_access_your_account_url = value
    
    @property
    def custom_c_s_s(self,) -> Optional[bytes]:
        """
        Gets the customCSS property value. CSS styling that appears on the sign-in page. The allowed format is .css format only and not larger than 25 KB.
        Returns: Optional[bytes]
        """
        return self._custom_c_s_s
    
    @custom_c_s_s.setter
    def custom_c_s_s(self,value: Optional[bytes] = None) -> None:
        """
        Sets the customCSS property value. CSS styling that appears on the sign-in page. The allowed format is .css format only and not larger than 25 KB.
        Args:
            value: Value to set for the customCSS property.
        """
        self._custom_c_s_s = value
    
    @property
    def custom_c_s_s_relative_url(self,) -> Optional[str]:
        """
        Gets the customCSSRelativeUrl property value. A relative URL for the customCSS property that is combined with a CDN base URL from the cdnList to provide the version served by a CDN. Read-only.
        Returns: Optional[str]
        """
        return self._custom_c_s_s_relative_url
    
    @custom_c_s_s_relative_url.setter
    def custom_c_s_s_relative_url(self,value: Optional[str] = None) -> None:
        """
        Sets the customCSSRelativeUrl property value. A relative URL for the customCSS property that is combined with a CDN base URL from the cdnList to provide the version served by a CDN. Read-only.
        Args:
            value: Value to set for the customCSSRelativeUrl property.
        """
        self._custom_c_s_s_relative_url = value
    
    @property
    def custom_forgot_my_password_text(self,) -> Optional[str]:
        """
        Gets the customForgotMyPasswordText property value. A string to replace the default 'Forgot my password' hyperlink text on the sign-in form. This text must be in Unicode format and not exceed 256 characters.
        Returns: Optional[str]
        """
        return self._custom_forgot_my_password_text
    
    @custom_forgot_my_password_text.setter
    def custom_forgot_my_password_text(self,value: Optional[str] = None) -> None:
        """
        Sets the customForgotMyPasswordText property value. A string to replace the default 'Forgot my password' hyperlink text on the sign-in form. This text must be in Unicode format and not exceed 256 characters.
        Args:
            value: Value to set for the customForgotMyPasswordText property.
        """
        self._custom_forgot_my_password_text = value
    
    @property
    def custom_privacy_and_cookies_text(self,) -> Optional[str]:
        """
        Gets the customPrivacyAndCookiesText property value. A string to replace the default 'Privacy and Cookies' hyperlink text in the footer. This text must be in Unicode format and not exceed 256 characters.
        Returns: Optional[str]
        """
        return self._custom_privacy_and_cookies_text
    
    @custom_privacy_and_cookies_text.setter
    def custom_privacy_and_cookies_text(self,value: Optional[str] = None) -> None:
        """
        Sets the customPrivacyAndCookiesText property value. A string to replace the default 'Privacy and Cookies' hyperlink text in the footer. This text must be in Unicode format and not exceed 256 characters.
        Args:
            value: Value to set for the customPrivacyAndCookiesText property.
        """
        self._custom_privacy_and_cookies_text = value
    
    @property
    def custom_privacy_and_cookies_url(self,) -> Optional[str]:
        """
        Gets the customPrivacyAndCookiesUrl property value. A custom URL to replace the default URL of the 'Privacy and Cookies' hyperlink in the footer. This URL must be in ASCII format or non-ASCII characters must be URL encoded, and not exceed 128 characters.
        Returns: Optional[str]
        """
        return self._custom_privacy_and_cookies_url
    
    @custom_privacy_and_cookies_url.setter
    def custom_privacy_and_cookies_url(self,value: Optional[str] = None) -> None:
        """
        Sets the customPrivacyAndCookiesUrl property value. A custom URL to replace the default URL of the 'Privacy and Cookies' hyperlink in the footer. This URL must be in ASCII format or non-ASCII characters must be URL encoded, and not exceed 128 characters.
        Args:
            value: Value to set for the customPrivacyAndCookiesUrl property.
        """
        self._custom_privacy_and_cookies_url = value
    
    @property
    def custom_reset_it_now_text(self,) -> Optional[str]:
        """
        Gets the customResetItNowText property value. A string to replace the default 'reset it now' hyperlink text on the sign-in form. This text must be in Unicode format and not exceed 256 characters. DO NOT USE: Customization of the 'reset it now' hyperlink text is currently not supported.
        Returns: Optional[str]
        """
        return self._custom_reset_it_now_text
    
    @custom_reset_it_now_text.setter
    def custom_reset_it_now_text(self,value: Optional[str] = None) -> None:
        """
        Sets the customResetItNowText property value. A string to replace the default 'reset it now' hyperlink text on the sign-in form. This text must be in Unicode format and not exceed 256 characters. DO NOT USE: Customization of the 'reset it now' hyperlink text is currently not supported.
        Args:
            value: Value to set for the customResetItNowText property.
        """
        self._custom_reset_it_now_text = value
    
    @property
    def custom_terms_of_use_text(self,) -> Optional[str]:
        """
        Gets the customTermsOfUseText property value. A string to replace the the default 'Terms of Use' hyperlink text in the footer. This text must be in Unicode format and not exceed 256 characters.
        Returns: Optional[str]
        """
        return self._custom_terms_of_use_text
    
    @custom_terms_of_use_text.setter
    def custom_terms_of_use_text(self,value: Optional[str] = None) -> None:
        """
        Sets the customTermsOfUseText property value. A string to replace the the default 'Terms of Use' hyperlink text in the footer. This text must be in Unicode format and not exceed 256 characters.
        Args:
            value: Value to set for the customTermsOfUseText property.
        """
        self._custom_terms_of_use_text = value
    
    @property
    def custom_terms_of_use_url(self,) -> Optional[str]:
        """
        Gets the customTermsOfUseUrl property value. A custom URL to replace the default URL of the 'Terms of Use' hyperlink in the footer. This URL must be in ASCII format or non-ASCII characters must be URL encoded, and not exceed 128characters.
        Returns: Optional[str]
        """
        return self._custom_terms_of_use_url
    
    @custom_terms_of_use_url.setter
    def custom_terms_of_use_url(self,value: Optional[str] = None) -> None:
        """
        Sets the customTermsOfUseUrl property value. A custom URL to replace the default URL of the 'Terms of Use' hyperlink in the footer. This URL must be in ASCII format or non-ASCII characters must be URL encoded, and not exceed 128characters.
        Args:
            value: Value to set for the customTermsOfUseUrl property.
        """
        self._custom_terms_of_use_url = value
    
    @property
    def favicon(self,) -> Optional[bytes]:
        """
        Gets the favicon property value. A custom icon (favicon) to replace a default Microsoft product favicon on an Azure AD tenant.
        Returns: Optional[bytes]
        """
        return self._favicon
    
    @favicon.setter
    def favicon(self,value: Optional[bytes] = None) -> None:
        """
        Sets the favicon property value. A custom icon (favicon) to replace a default Microsoft product favicon on an Azure AD tenant.
        Args:
            value: Value to set for the favicon property.
        """
        self._favicon = value
    
    @property
    def favicon_relative_url(self,) -> Optional[str]:
        """
        Gets the faviconRelativeUrl property value. A relative url for the favicon above that is combined with a CDN base URL from the cdnList to provide the version served by a CDN. Read-only.
        Returns: Optional[str]
        """
        return self._favicon_relative_url
    
    @favicon_relative_url.setter
    def favicon_relative_url(self,value: Optional[str] = None) -> None:
        """
        Sets the faviconRelativeUrl property value. A relative url for the favicon above that is combined with a CDN base URL from the cdnList to provide the version served by a CDN. Read-only.
        Args:
            value: Value to set for the faviconRelativeUrl property.
        """
        self._favicon_relative_url = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "background_color": lambda n : setattr(self, 'background_color', n.get_str_value()),
            "background_image": lambda n : setattr(self, 'background_image', n.get_bytes_value()),
            "background_image_relative_url": lambda n : setattr(self, 'background_image_relative_url', n.get_str_value()),
            "banner_logo": lambda n : setattr(self, 'banner_logo', n.get_bytes_value()),
            "banner_logo_relative_url": lambda n : setattr(self, 'banner_logo_relative_url', n.get_str_value()),
            "cdn_list": lambda n : setattr(self, 'cdn_list', n.get_collection_of_primitive_values(str)),
            "custom_account_reset_credentials_url": lambda n : setattr(self, 'custom_account_reset_credentials_url', n.get_str_value()),
            "custom_cannot_access_your_account_text": lambda n : setattr(self, 'custom_cannot_access_your_account_text', n.get_str_value()),
            "custom_cannot_access_your_account_url": lambda n : setattr(self, 'custom_cannot_access_your_account_url', n.get_str_value()),
            "custom_c_s_s": lambda n : setattr(self, 'custom_c_s_s', n.get_bytes_value()),
            "custom_c_s_s_relative_url": lambda n : setattr(self, 'custom_c_s_s_relative_url', n.get_str_value()),
            "custom_forgot_my_password_text": lambda n : setattr(self, 'custom_forgot_my_password_text', n.get_str_value()),
            "custom_privacy_and_cookies_text": lambda n : setattr(self, 'custom_privacy_and_cookies_text', n.get_str_value()),
            "custom_privacy_and_cookies_url": lambda n : setattr(self, 'custom_privacy_and_cookies_url', n.get_str_value()),
            "custom_reset_it_now_text": lambda n : setattr(self, 'custom_reset_it_now_text', n.get_str_value()),
            "custom_terms_of_use_text": lambda n : setattr(self, 'custom_terms_of_use_text', n.get_str_value()),
            "custom_terms_of_use_url": lambda n : setattr(self, 'custom_terms_of_use_url', n.get_str_value()),
            "favicon": lambda n : setattr(self, 'favicon', n.get_bytes_value()),
            "favicon_relative_url": lambda n : setattr(self, 'favicon_relative_url', n.get_str_value()),
            "header_background_color": lambda n : setattr(self, 'header_background_color', n.get_str_value()),
            "header_logo": lambda n : setattr(self, 'header_logo', n.get_bytes_value()),
            "header_logo_relative_url": lambda n : setattr(self, 'header_logo_relative_url', n.get_str_value()),
            "login_page_layout_configuration": lambda n : setattr(self, 'login_page_layout_configuration', n.get_object_value(login_page_layout_configuration.LoginPageLayoutConfiguration)),
            "login_page_text_visibility_settings": lambda n : setattr(self, 'login_page_text_visibility_settings', n.get_object_value(login_page_text_visibility_settings.LoginPageTextVisibilitySettings)),
            "sign_in_page_text": lambda n : setattr(self, 'sign_in_page_text', n.get_str_value()),
            "square_logo": lambda n : setattr(self, 'square_logo', n.get_bytes_value()),
            "square_logo_dark": lambda n : setattr(self, 'square_logo_dark', n.get_bytes_value()),
            "square_logo_dark_relative_url": lambda n : setattr(self, 'square_logo_dark_relative_url', n.get_str_value()),
            "square_logo_relative_url": lambda n : setattr(self, 'square_logo_relative_url', n.get_str_value()),
            "username_hint_text": lambda n : setattr(self, 'username_hint_text', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def header_background_color(self,) -> Optional[str]:
        """
        Gets the headerBackgroundColor property value. The RGB color to apply to customize the color of the header.
        Returns: Optional[str]
        """
        return self._header_background_color
    
    @header_background_color.setter
    def header_background_color(self,value: Optional[str] = None) -> None:
        """
        Sets the headerBackgroundColor property value. The RGB color to apply to customize the color of the header.
        Args:
            value: Value to set for the headerBackgroundColor property.
        """
        self._header_background_color = value
    
    @property
    def header_logo(self,) -> Optional[bytes]:
        """
        Gets the headerLogo property value. A company logo that appears in the header of the sign-in page. The allowed types are PNG or JPEG not larger than 36 × 245 pixels. We recommend using a transparent image with no padding around the logo.
        Returns: Optional[bytes]
        """
        return self._header_logo
    
    @header_logo.setter
    def header_logo(self,value: Optional[bytes] = None) -> None:
        """
        Sets the headerLogo property value. A company logo that appears in the header of the sign-in page. The allowed types are PNG or JPEG not larger than 36 × 245 pixels. We recommend using a transparent image with no padding around the logo.
        Args:
            value: Value to set for the headerLogo property.
        """
        self._header_logo = value
    
    @property
    def header_logo_relative_url(self,) -> Optional[str]:
        """
        Gets the headerLogoRelativeUrl property value. A relative URL for the headerLogo property that is combined with a CDN base URL from the cdnList to provide the read-only version served by a CDN. Read-only.
        Returns: Optional[str]
        """
        return self._header_logo_relative_url
    
    @header_logo_relative_url.setter
    def header_logo_relative_url(self,value: Optional[str] = None) -> None:
        """
        Sets the headerLogoRelativeUrl property value. A relative URL for the headerLogo property that is combined with a CDN base URL from the cdnList to provide the read-only version served by a CDN. Read-only.
        Args:
            value: Value to set for the headerLogoRelativeUrl property.
        """
        self._header_logo_relative_url = value
    
    @property
    def login_page_layout_configuration(self,) -> Optional[login_page_layout_configuration.LoginPageLayoutConfiguration]:
        """
        Gets the loginPageLayoutConfiguration property value. Represents the layout configuration to be displayed on the login page for a tenant.
        Returns: Optional[login_page_layout_configuration.LoginPageLayoutConfiguration]
        """
        return self._login_page_layout_configuration
    
    @login_page_layout_configuration.setter
    def login_page_layout_configuration(self,value: Optional[login_page_layout_configuration.LoginPageLayoutConfiguration] = None) -> None:
        """
        Sets the loginPageLayoutConfiguration property value. Represents the layout configuration to be displayed on the login page for a tenant.
        Args:
            value: Value to set for the loginPageLayoutConfiguration property.
        """
        self._login_page_layout_configuration = value
    
    @property
    def login_page_text_visibility_settings(self,) -> Optional[login_page_text_visibility_settings.LoginPageTextVisibilitySettings]:
        """
        Gets the loginPageTextVisibilitySettings property value. Represents the various texts that can be hidden on the login page for a tenant.
        Returns: Optional[login_page_text_visibility_settings.LoginPageTextVisibilitySettings]
        """
        return self._login_page_text_visibility_settings
    
    @login_page_text_visibility_settings.setter
    def login_page_text_visibility_settings(self,value: Optional[login_page_text_visibility_settings.LoginPageTextVisibilitySettings] = None) -> None:
        """
        Sets the loginPageTextVisibilitySettings property value. Represents the various texts that can be hidden on the login page for a tenant.
        Args:
            value: Value to set for the loginPageTextVisibilitySettings property.
        """
        self._login_page_text_visibility_settings = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("backgroundColor", self.background_color)
        writer.write_object_value("backgroundImage", self.background_image)
        writer.write_str_value("backgroundImageRelativeUrl", self.background_image_relative_url)
        writer.write_object_value("bannerLogo", self.banner_logo)
        writer.write_str_value("bannerLogoRelativeUrl", self.banner_logo_relative_url)
        writer.write_collection_of_primitive_values("cdnList", self.cdn_list)
        writer.write_str_value("customAccountResetCredentialsUrl", self.custom_account_reset_credentials_url)
        writer.write_str_value("customCannotAccessYourAccountText", self.custom_cannot_access_your_account_text)
        writer.write_str_value("customCannotAccessYourAccountUrl", self.custom_cannot_access_your_account_url)
        writer.write_object_value("customCSS", self.custom_c_s_s)
        writer.write_str_value("customCSSRelativeUrl", self.custom_c_s_s_relative_url)
        writer.write_str_value("customForgotMyPasswordText", self.custom_forgot_my_password_text)
        writer.write_str_value("customPrivacyAndCookiesText", self.custom_privacy_and_cookies_text)
        writer.write_str_value("customPrivacyAndCookiesUrl", self.custom_privacy_and_cookies_url)
        writer.write_str_value("customResetItNowText", self.custom_reset_it_now_text)
        writer.write_str_value("customTermsOfUseText", self.custom_terms_of_use_text)
        writer.write_str_value("customTermsOfUseUrl", self.custom_terms_of_use_url)
        writer.write_object_value("favicon", self.favicon)
        writer.write_str_value("faviconRelativeUrl", self.favicon_relative_url)
        writer.write_str_value("headerBackgroundColor", self.header_background_color)
        writer.write_object_value("headerLogo", self.header_logo)
        writer.write_str_value("headerLogoRelativeUrl", self.header_logo_relative_url)
        writer.write_object_value("loginPageLayoutConfiguration", self.login_page_layout_configuration)
        writer.write_object_value("loginPageTextVisibilitySettings", self.login_page_text_visibility_settings)
        writer.write_str_value("signInPageText", self.sign_in_page_text)
        writer.write_object_value("squareLogo", self.square_logo)
        writer.write_object_value("squareLogoDark", self.square_logo_dark)
        writer.write_str_value("squareLogoDarkRelativeUrl", self.square_logo_dark_relative_url)
        writer.write_str_value("squareLogoRelativeUrl", self.square_logo_relative_url)
        writer.write_str_value("usernameHintText", self.username_hint_text)
    
    @property
    def sign_in_page_text(self,) -> Optional[str]:
        """
        Gets the signInPageText property value. Text that appears at the bottom of the sign-in box. Use this to communicate additional information, such as the phone number to your help desk or a legal statement. This text must be in Unicode format and not exceed 1024 characters.
        Returns: Optional[str]
        """
        return self._sign_in_page_text
    
    @sign_in_page_text.setter
    def sign_in_page_text(self,value: Optional[str] = None) -> None:
        """
        Sets the signInPageText property value. Text that appears at the bottom of the sign-in box. Use this to communicate additional information, such as the phone number to your help desk or a legal statement. This text must be in Unicode format and not exceed 1024 characters.
        Args:
            value: Value to set for the signInPageText property.
        """
        self._sign_in_page_text = value
    
    @property
    def square_logo(self,) -> Optional[bytes]:
        """
        Gets the squareLogo property value. A square version of your company logo that appears in Windows 10 out-of-box experiences (OOBE) and when Windows Autopilot is enabled for deployment. Allowed types are PNG or JPEG not larger than 240 x 240 pixels and not more than 10 KB in size. We recommend using a transparent image with no padding around the logo.
        Returns: Optional[bytes]
        """
        return self._square_logo
    
    @square_logo.setter
    def square_logo(self,value: Optional[bytes] = None) -> None:
        """
        Sets the squareLogo property value. A square version of your company logo that appears in Windows 10 out-of-box experiences (OOBE) and when Windows Autopilot is enabled for deployment. Allowed types are PNG or JPEG not larger than 240 x 240 pixels and not more than 10 KB in size. We recommend using a transparent image with no padding around the logo.
        Args:
            value: Value to set for the squareLogo property.
        """
        self._square_logo = value
    
    @property
    def square_logo_dark(self,) -> Optional[bytes]:
        """
        Gets the squareLogoDark property value. A square dark version of your company logo that appears in Windows 10 out-of-box experiences (OOBE) and when Windows Autopilot is enabled for deployment. Allowed types are PNG or JPEG not larger than 240 x 240 pixels and not more than 10 KB in size. We recommend using a transparent image with no padding around the logo.
        Returns: Optional[bytes]
        """
        return self._square_logo_dark
    
    @square_logo_dark.setter
    def square_logo_dark(self,value: Optional[bytes] = None) -> None:
        """
        Sets the squareLogoDark property value. A square dark version of your company logo that appears in Windows 10 out-of-box experiences (OOBE) and when Windows Autopilot is enabled for deployment. Allowed types are PNG or JPEG not larger than 240 x 240 pixels and not more than 10 KB in size. We recommend using a transparent image with no padding around the logo.
        Args:
            value: Value to set for the squareLogoDark property.
        """
        self._square_logo_dark = value
    
    @property
    def square_logo_dark_relative_url(self,) -> Optional[str]:
        """
        Gets the squareLogoDarkRelativeUrl property value. A relative URL for the squareLogoDark property that is combined with a CDN base URL from the cdnList to provide the version served by a CDN. Read-only.
        Returns: Optional[str]
        """
        return self._square_logo_dark_relative_url
    
    @square_logo_dark_relative_url.setter
    def square_logo_dark_relative_url(self,value: Optional[str] = None) -> None:
        """
        Sets the squareLogoDarkRelativeUrl property value. A relative URL for the squareLogoDark property that is combined with a CDN base URL from the cdnList to provide the version served by a CDN. Read-only.
        Args:
            value: Value to set for the squareLogoDarkRelativeUrl property.
        """
        self._square_logo_dark_relative_url = value
    
    @property
    def square_logo_relative_url(self,) -> Optional[str]:
        """
        Gets the squareLogoRelativeUrl property value. A relative URL for the squareLogo property that is combined with a CDN base URL from the cdnList to provide the version served by a CDN. Read-only.
        Returns: Optional[str]
        """
        return self._square_logo_relative_url
    
    @square_logo_relative_url.setter
    def square_logo_relative_url(self,value: Optional[str] = None) -> None:
        """
        Sets the squareLogoRelativeUrl property value. A relative URL for the squareLogo property that is combined with a CDN base URL from the cdnList to provide the version served by a CDN. Read-only.
        Args:
            value: Value to set for the squareLogoRelativeUrl property.
        """
        self._square_logo_relative_url = value
    
    @property
    def username_hint_text(self,) -> Optional[str]:
        """
        Gets the usernameHintText property value. A string that shows as the hint in the username textbox on the sign-in screen. This text must be a Unicode, without links or code, and can't exceed 64 characters.
        Returns: Optional[str]
        """
        return self._username_hint_text
    
    @username_hint_text.setter
    def username_hint_text(self,value: Optional[str] = None) -> None:
        """
        Sets the usernameHintText property value. A string that shows as the hint in the username textbox on the sign-in screen. This text must be a Unicode, without links or code, and can't exceed 64 characters.
        Args:
            value: Value to set for the usernameHintText property.
        """
        self._username_hint_text = value
    

