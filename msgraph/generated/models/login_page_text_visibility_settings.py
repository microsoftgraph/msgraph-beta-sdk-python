from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class LoginPageTextVisibilitySettings(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new loginPageTextVisibilitySettings and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Option to hide the self-service password reset (SSPR) hyperlinks such as 'Can't access your account?', 'Forgot my password' and 'Reset it now' on the sign-in form.
        self._hide_account_reset_credentials: Optional[bool] = None
        # Option to hide the self-service password reset (SSPR) 'Can't access your account?' hyperlink on the sign-in form.
        self._hide_cannot_access_your_account: Optional[bool] = None
        # Option to hide the self-service password reset (SSPR) 'Forgot my password' hyperlink on the sign-in form.
        self._hide_forgot_my_password: Optional[bool] = None
        # Option to hide the 'Privacy & Cookies' hyperlink in the footer.
        self._hide_privacy_and_cookies: Optional[bool] = None
        # Option to hide the self-service password reset (SSPR) 'reset it now' hyperlink on the sign-in form.
        self._hide_reset_it_now: Optional[bool] = None
        # Option to hide the 'Terms of Use' hyperlink in the footer.
        self._hide_terms_of_use: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> LoginPageTextVisibilitySettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: LoginPageTextVisibilitySettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return LoginPageTextVisibilitySettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "hide_account_reset_credentials": lambda n : setattr(self, 'hide_account_reset_credentials', n.get_bool_value()),
            "hide_cannot_access_your_account": lambda n : setattr(self, 'hide_cannot_access_your_account', n.get_bool_value()),
            "hide_forgot_my_password": lambda n : setattr(self, 'hide_forgot_my_password', n.get_bool_value()),
            "hide_privacy_and_cookies": lambda n : setattr(self, 'hide_privacy_and_cookies', n.get_bool_value()),
            "hide_reset_it_now": lambda n : setattr(self, 'hide_reset_it_now', n.get_bool_value()),
            "hide_terms_of_use": lambda n : setattr(self, 'hide_terms_of_use', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def hide_account_reset_credentials(self,) -> Optional[bool]:
        """
        Gets the hideAccountResetCredentials property value. Option to hide the self-service password reset (SSPR) hyperlinks such as 'Can't access your account?', 'Forgot my password' and 'Reset it now' on the sign-in form.
        Returns: Optional[bool]
        """
        return self._hide_account_reset_credentials
    
    @hide_account_reset_credentials.setter
    def hide_account_reset_credentials(self,value: Optional[bool] = None) -> None:
        """
        Sets the hideAccountResetCredentials property value. Option to hide the self-service password reset (SSPR) hyperlinks such as 'Can't access your account?', 'Forgot my password' and 'Reset it now' on the sign-in form.
        Args:
            value: Value to set for the hideAccountResetCredentials property.
        """
        self._hide_account_reset_credentials = value
    
    @property
    def hide_cannot_access_your_account(self,) -> Optional[bool]:
        """
        Gets the hideCannotAccessYourAccount property value. Option to hide the self-service password reset (SSPR) 'Can't access your account?' hyperlink on the sign-in form.
        Returns: Optional[bool]
        """
        return self._hide_cannot_access_your_account
    
    @hide_cannot_access_your_account.setter
    def hide_cannot_access_your_account(self,value: Optional[bool] = None) -> None:
        """
        Sets the hideCannotAccessYourAccount property value. Option to hide the self-service password reset (SSPR) 'Can't access your account?' hyperlink on the sign-in form.
        Args:
            value: Value to set for the hideCannotAccessYourAccount property.
        """
        self._hide_cannot_access_your_account = value
    
    @property
    def hide_forgot_my_password(self,) -> Optional[bool]:
        """
        Gets the hideForgotMyPassword property value. Option to hide the self-service password reset (SSPR) 'Forgot my password' hyperlink on the sign-in form.
        Returns: Optional[bool]
        """
        return self._hide_forgot_my_password
    
    @hide_forgot_my_password.setter
    def hide_forgot_my_password(self,value: Optional[bool] = None) -> None:
        """
        Sets the hideForgotMyPassword property value. Option to hide the self-service password reset (SSPR) 'Forgot my password' hyperlink on the sign-in form.
        Args:
            value: Value to set for the hideForgotMyPassword property.
        """
        self._hide_forgot_my_password = value
    
    @property
    def hide_privacy_and_cookies(self,) -> Optional[bool]:
        """
        Gets the hidePrivacyAndCookies property value. Option to hide the 'Privacy & Cookies' hyperlink in the footer.
        Returns: Optional[bool]
        """
        return self._hide_privacy_and_cookies
    
    @hide_privacy_and_cookies.setter
    def hide_privacy_and_cookies(self,value: Optional[bool] = None) -> None:
        """
        Sets the hidePrivacyAndCookies property value. Option to hide the 'Privacy & Cookies' hyperlink in the footer.
        Args:
            value: Value to set for the hidePrivacyAndCookies property.
        """
        self._hide_privacy_and_cookies = value
    
    @property
    def hide_reset_it_now(self,) -> Optional[bool]:
        """
        Gets the hideResetItNow property value. Option to hide the self-service password reset (SSPR) 'reset it now' hyperlink on the sign-in form.
        Returns: Optional[bool]
        """
        return self._hide_reset_it_now
    
    @hide_reset_it_now.setter
    def hide_reset_it_now(self,value: Optional[bool] = None) -> None:
        """
        Sets the hideResetItNow property value. Option to hide the self-service password reset (SSPR) 'reset it now' hyperlink on the sign-in form.
        Args:
            value: Value to set for the hideResetItNow property.
        """
        self._hide_reset_it_now = value
    
    @property
    def hide_terms_of_use(self,) -> Optional[bool]:
        """
        Gets the hideTermsOfUse property value. Option to hide the 'Terms of Use' hyperlink in the footer.
        Returns: Optional[bool]
        """
        return self._hide_terms_of_use
    
    @hide_terms_of_use.setter
    def hide_terms_of_use(self,value: Optional[bool] = None) -> None:
        """
        Sets the hideTermsOfUse property value. Option to hide the 'Terms of Use' hyperlink in the footer.
        Args:
            value: Value to set for the hideTermsOfUse property.
        """
        self._hide_terms_of_use = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_bool_value("hideAccountResetCredentials", self.hide_account_reset_credentials)
        writer.write_bool_value("hideCannotAccessYourAccount", self.hide_cannot_access_your_account)
        writer.write_bool_value("hideForgotMyPassword", self.hide_forgot_my_password)
        writer.write_bool_value("hidePrivacyAndCookies", self.hide_privacy_and_cookies)
        writer.write_bool_value("hideResetItNow", self.hide_reset_it_now)
        writer.write_bool_value("hideTermsOfUse", self.hide_terms_of_use)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

