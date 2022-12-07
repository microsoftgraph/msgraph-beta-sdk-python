from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_management_derived_credential_settings = lazy_import('msgraph.generated.models.device_management_derived_credential_settings')
eas_authentication_method = lazy_import('msgraph.generated.models.eas_authentication_method')
eas_email_profile_configuration_base = lazy_import('msgraph.generated.models.eas_email_profile_configuration_base')
eas_services = lazy_import('msgraph.generated.models.eas_services')
email_certificate_type = lazy_import('msgraph.generated.models.email_certificate_type')
email_sync_duration = lazy_import('msgraph.generated.models.email_sync_duration')
ios_certificate_profile = lazy_import('msgraph.generated.models.ios_certificate_profile')
ios_certificate_profile_base = lazy_import('msgraph.generated.models.ios_certificate_profile_base')
user_email_source = lazy_import('msgraph.generated.models.user_email_source')

class IosEasEmailProfileConfiguration(eas_email_profile_configuration_base.EasEmailProfileConfigurationBase):
    @property
    def account_name(self,) -> Optional[str]:
        """
        Gets the accountName property value. Account name.
        Returns: Optional[str]
        """
        return self._account_name
    
    @account_name.setter
    def account_name(self,value: Optional[str] = None) -> None:
        """
        Sets the accountName property value. Account name.
        Args:
            value: Value to set for the accountName property.
        """
        self._account_name = value
    
    @property
    def authentication_method(self,) -> Optional[eas_authentication_method.EasAuthenticationMethod]:
        """
        Gets the authenticationMethod property value. Authentication method for this Email profile. Possible values are: usernameAndPassword, certificate, derivedCredential.
        Returns: Optional[eas_authentication_method.EasAuthenticationMethod]
        """
        return self._authentication_method
    
    @authentication_method.setter
    def authentication_method(self,value: Optional[eas_authentication_method.EasAuthenticationMethod] = None) -> None:
        """
        Sets the authenticationMethod property value. Authentication method for this Email profile. Possible values are: usernameAndPassword, certificate, derivedCredential.
        Args:
            value: Value to set for the authenticationMethod property.
        """
        self._authentication_method = value
    
    @property
    def block_moving_messages_to_other_email_accounts(self,) -> Optional[bool]:
        """
        Gets the blockMovingMessagesToOtherEmailAccounts property value. Indicates whether or not to block moving messages to other email accounts.
        Returns: Optional[bool]
        """
        return self._block_moving_messages_to_other_email_accounts
    
    @block_moving_messages_to_other_email_accounts.setter
    def block_moving_messages_to_other_email_accounts(self,value: Optional[bool] = None) -> None:
        """
        Sets the blockMovingMessagesToOtherEmailAccounts property value. Indicates whether or not to block moving messages to other email accounts.
        Args:
            value: Value to set for the blockMovingMessagesToOtherEmailAccounts property.
        """
        self._block_moving_messages_to_other_email_accounts = value
    
    @property
    def block_sending_email_from_third_party_apps(self,) -> Optional[bool]:
        """
        Gets the blockSendingEmailFromThirdPartyApps property value. Indicates whether or not to block sending email from third party apps.
        Returns: Optional[bool]
        """
        return self._block_sending_email_from_third_party_apps
    
    @block_sending_email_from_third_party_apps.setter
    def block_sending_email_from_third_party_apps(self,value: Optional[bool] = None) -> None:
        """
        Sets the blockSendingEmailFromThirdPartyApps property value. Indicates whether or not to block sending email from third party apps.
        Args:
            value: Value to set for the blockSendingEmailFromThirdPartyApps property.
        """
        self._block_sending_email_from_third_party_apps = value
    
    @property
    def block_syncing_recently_used_email_addresses(self,) -> Optional[bool]:
        """
        Gets the blockSyncingRecentlyUsedEmailAddresses property value. Indicates whether or not to block syncing recently used email addresses, for instance - when composing new email.
        Returns: Optional[bool]
        """
        return self._block_syncing_recently_used_email_addresses
    
    @block_syncing_recently_used_email_addresses.setter
    def block_syncing_recently_used_email_addresses(self,value: Optional[bool] = None) -> None:
        """
        Sets the blockSyncingRecentlyUsedEmailAddresses property value. Indicates whether or not to block syncing recently used email addresses, for instance - when composing new email.
        Args:
            value: Value to set for the blockSyncingRecentlyUsedEmailAddresses property.
        """
        self._block_syncing_recently_used_email_addresses = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new IosEasEmailProfileConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.iosEasEmailProfileConfiguration"
        # Account name.
        self._account_name: Optional[str] = None
        # Authentication method for this Email profile. Possible values are: usernameAndPassword, certificate, derivedCredential.
        self._authentication_method: Optional[eas_authentication_method.EasAuthenticationMethod] = None
        # Indicates whether or not to block moving messages to other email accounts.
        self._block_moving_messages_to_other_email_accounts: Optional[bool] = None
        # Indicates whether or not to block sending email from third party apps.
        self._block_sending_email_from_third_party_apps: Optional[bool] = None
        # Indicates whether or not to block syncing recently used email addresses, for instance - when composing new email.
        self._block_syncing_recently_used_email_addresses: Optional[bool] = None
        # Tenant level settings for the Derived Credentials to be used for authentication.
        self._derived_credential_settings: Optional[device_management_derived_credential_settings.DeviceManagementDerivedCredentialSettings] = None
        # Possible values for email sync duration.
        self._duration_of_email_to_sync: Optional[email_sync_duration.EmailSyncDuration] = None
        # Exchange data to sync. Possible values are: none, calendars, contacts, email, notes, reminders.
        self._eas_services: Optional[eas_services.EasServices] = None
        # Allow users to change sync settings.
        self._eas_services_user_override_enabled: Optional[bool] = None
        # Possible values for username source or email source.
        self._email_address_source: Optional[user_email_source.UserEmailSource] = None
        # Encryption Certificate type for this Email profile. Possible values are: none, certificate, derivedCredential.
        self._encryption_certificate_type: Optional[email_certificate_type.EmailCertificateType] = None
        # Exchange location that (URL) that the native mail app connects to.
        self._host_name: Optional[str] = None
        # Identity certificate.
        self._identity_certificate: Optional[ios_certificate_profile_base.IosCertificateProfileBase] = None
        # Profile ID of the Per-App VPN policy to be used to access emails from the native Mail client
        self._per_app_v_p_n_profile_id: Optional[str] = None
        # Indicates whether or not to use S/MIME certificate.
        self._require_smime: Optional[bool] = None
        # Indicates whether or not to use SSL.
        self._require_ssl: Optional[bool] = None
        # Signing Certificate type for this Email profile. Possible values are: none, certificate, derivedCredential.
        self._signing_certificate_type: Optional[email_certificate_type.EmailCertificateType] = None
        # Indicates whether or not to allow unencrypted emails.
        self._smime_enable_per_message_switch: Optional[bool] = None
        # If set to true S/MIME encryption is enabled by default.
        self._smime_encrypt_by_default_enabled: Optional[bool] = None
        # If set to true, the user can toggle the encryption by default setting.
        self._smime_encrypt_by_default_user_override_enabled: Optional[bool] = None
        # S/MIME encryption certificate.
        self._smime_encryption_certificate: Optional[ios_certificate_profile.IosCertificateProfile] = None
        # If set to true the user can select the S/MIME encryption identity.
        self._smime_encryption_certificate_user_override_enabled: Optional[bool] = None
        # S/MIME signing certificate.
        self._smime_signing_certificate: Optional[ios_certificate_profile.IosCertificateProfile] = None
        # If set to true, the user can select the signing identity.
        self._smime_signing_certificate_user_override_enabled: Optional[bool] = None
        # If set to true S/MIME signing is enabled for this account
        self._smime_signing_enabled: Optional[bool] = None
        # If set to true, the user can toggle S/MIME signing on or off.
        self._smime_signing_user_override_enabled: Optional[bool] = None
        # Specifies whether the connection should use OAuth for authentication.
        self._use_o_auth: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IosEasEmailProfileConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IosEasEmailProfileConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return IosEasEmailProfileConfiguration()
    
    @property
    def derived_credential_settings(self,) -> Optional[device_management_derived_credential_settings.DeviceManagementDerivedCredentialSettings]:
        """
        Gets the derivedCredentialSettings property value. Tenant level settings for the Derived Credentials to be used for authentication.
        Returns: Optional[device_management_derived_credential_settings.DeviceManagementDerivedCredentialSettings]
        """
        return self._derived_credential_settings
    
    @derived_credential_settings.setter
    def derived_credential_settings(self,value: Optional[device_management_derived_credential_settings.DeviceManagementDerivedCredentialSettings] = None) -> None:
        """
        Sets the derivedCredentialSettings property value. Tenant level settings for the Derived Credentials to be used for authentication.
        Args:
            value: Value to set for the derivedCredentialSettings property.
        """
        self._derived_credential_settings = value
    
    @property
    def duration_of_email_to_sync(self,) -> Optional[email_sync_duration.EmailSyncDuration]:
        """
        Gets the durationOfEmailToSync property value. Possible values for email sync duration.
        Returns: Optional[email_sync_duration.EmailSyncDuration]
        """
        return self._duration_of_email_to_sync
    
    @duration_of_email_to_sync.setter
    def duration_of_email_to_sync(self,value: Optional[email_sync_duration.EmailSyncDuration] = None) -> None:
        """
        Sets the durationOfEmailToSync property value. Possible values for email sync duration.
        Args:
            value: Value to set for the durationOfEmailToSync property.
        """
        self._duration_of_email_to_sync = value
    
    @property
    def eas_services(self,) -> Optional[eas_services.EasServices]:
        """
        Gets the easServices property value. Exchange data to sync. Possible values are: none, calendars, contacts, email, notes, reminders.
        Returns: Optional[eas_services.EasServices]
        """
        return self._eas_services
    
    @eas_services.setter
    def eas_services(self,value: Optional[eas_services.EasServices] = None) -> None:
        """
        Sets the easServices property value. Exchange data to sync. Possible values are: none, calendars, contacts, email, notes, reminders.
        Args:
            value: Value to set for the easServices property.
        """
        self._eas_services = value
    
    @property
    def eas_services_user_override_enabled(self,) -> Optional[bool]:
        """
        Gets the easServicesUserOverrideEnabled property value. Allow users to change sync settings.
        Returns: Optional[bool]
        """
        return self._eas_services_user_override_enabled
    
    @eas_services_user_override_enabled.setter
    def eas_services_user_override_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the easServicesUserOverrideEnabled property value. Allow users to change sync settings.
        Args:
            value: Value to set for the easServicesUserOverrideEnabled property.
        """
        self._eas_services_user_override_enabled = value
    
    @property
    def email_address_source(self,) -> Optional[user_email_source.UserEmailSource]:
        """
        Gets the emailAddressSource property value. Possible values for username source or email source.
        Returns: Optional[user_email_source.UserEmailSource]
        """
        return self._email_address_source
    
    @email_address_source.setter
    def email_address_source(self,value: Optional[user_email_source.UserEmailSource] = None) -> None:
        """
        Sets the emailAddressSource property value. Possible values for username source or email source.
        Args:
            value: Value to set for the emailAddressSource property.
        """
        self._email_address_source = value
    
    @property
    def encryption_certificate_type(self,) -> Optional[email_certificate_type.EmailCertificateType]:
        """
        Gets the encryptionCertificateType property value. Encryption Certificate type for this Email profile. Possible values are: none, certificate, derivedCredential.
        Returns: Optional[email_certificate_type.EmailCertificateType]
        """
        return self._encryption_certificate_type
    
    @encryption_certificate_type.setter
    def encryption_certificate_type(self,value: Optional[email_certificate_type.EmailCertificateType] = None) -> None:
        """
        Sets the encryptionCertificateType property value. Encryption Certificate type for this Email profile. Possible values are: none, certificate, derivedCredential.
        Args:
            value: Value to set for the encryptionCertificateType property.
        """
        self._encryption_certificate_type = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "account_name": lambda n : setattr(self, 'account_name', n.get_str_value()),
            "authentication_method": lambda n : setattr(self, 'authentication_method', n.get_enum_value(eas_authentication_method.EasAuthenticationMethod)),
            "block_moving_messages_to_other_email_accounts": lambda n : setattr(self, 'block_moving_messages_to_other_email_accounts', n.get_bool_value()),
            "block_sending_email_from_third_party_apps": lambda n : setattr(self, 'block_sending_email_from_third_party_apps', n.get_bool_value()),
            "block_syncing_recently_used_email_addresses": lambda n : setattr(self, 'block_syncing_recently_used_email_addresses', n.get_bool_value()),
            "derived_credential_settings": lambda n : setattr(self, 'derived_credential_settings', n.get_object_value(device_management_derived_credential_settings.DeviceManagementDerivedCredentialSettings)),
            "duration_of_email_to_sync": lambda n : setattr(self, 'duration_of_email_to_sync', n.get_enum_value(email_sync_duration.EmailSyncDuration)),
            "eas_services": lambda n : setattr(self, 'eas_services', n.get_enum_value(eas_services.EasServices)),
            "eas_services_user_override_enabled": lambda n : setattr(self, 'eas_services_user_override_enabled', n.get_bool_value()),
            "email_address_source": lambda n : setattr(self, 'email_address_source', n.get_enum_value(user_email_source.UserEmailSource)),
            "encryption_certificate_type": lambda n : setattr(self, 'encryption_certificate_type', n.get_enum_value(email_certificate_type.EmailCertificateType)),
            "host_name": lambda n : setattr(self, 'host_name', n.get_str_value()),
            "identity_certificate": lambda n : setattr(self, 'identity_certificate', n.get_object_value(ios_certificate_profile_base.IosCertificateProfileBase)),
            "per_app_v_p_n_profile_id": lambda n : setattr(self, 'per_app_v_p_n_profile_id', n.get_str_value()),
            "require_smime": lambda n : setattr(self, 'require_smime', n.get_bool_value()),
            "require_ssl": lambda n : setattr(self, 'require_ssl', n.get_bool_value()),
            "signing_certificate_type": lambda n : setattr(self, 'signing_certificate_type', n.get_enum_value(email_certificate_type.EmailCertificateType)),
            "smime_enable_per_message_switch": lambda n : setattr(self, 'smime_enable_per_message_switch', n.get_bool_value()),
            "smime_encrypt_by_default_enabled": lambda n : setattr(self, 'smime_encrypt_by_default_enabled', n.get_bool_value()),
            "smime_encrypt_by_default_user_override_enabled": lambda n : setattr(self, 'smime_encrypt_by_default_user_override_enabled', n.get_bool_value()),
            "smime_encryption_certificate": lambda n : setattr(self, 'smime_encryption_certificate', n.get_object_value(ios_certificate_profile.IosCertificateProfile)),
            "smime_encryption_certificate_user_override_enabled": lambda n : setattr(self, 'smime_encryption_certificate_user_override_enabled', n.get_bool_value()),
            "smime_signing_certificate": lambda n : setattr(self, 'smime_signing_certificate', n.get_object_value(ios_certificate_profile.IosCertificateProfile)),
            "smime_signing_certificate_user_override_enabled": lambda n : setattr(self, 'smime_signing_certificate_user_override_enabled', n.get_bool_value()),
            "smime_signing_enabled": lambda n : setattr(self, 'smime_signing_enabled', n.get_bool_value()),
            "smime_signing_user_override_enabled": lambda n : setattr(self, 'smime_signing_user_override_enabled', n.get_bool_value()),
            "use_o_auth": lambda n : setattr(self, 'use_o_auth', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def host_name(self,) -> Optional[str]:
        """
        Gets the hostName property value. Exchange location that (URL) that the native mail app connects to.
        Returns: Optional[str]
        """
        return self._host_name
    
    @host_name.setter
    def host_name(self,value: Optional[str] = None) -> None:
        """
        Sets the hostName property value. Exchange location that (URL) that the native mail app connects to.
        Args:
            value: Value to set for the hostName property.
        """
        self._host_name = value
    
    @property
    def identity_certificate(self,) -> Optional[ios_certificate_profile_base.IosCertificateProfileBase]:
        """
        Gets the identityCertificate property value. Identity certificate.
        Returns: Optional[ios_certificate_profile_base.IosCertificateProfileBase]
        """
        return self._identity_certificate
    
    @identity_certificate.setter
    def identity_certificate(self,value: Optional[ios_certificate_profile_base.IosCertificateProfileBase] = None) -> None:
        """
        Sets the identityCertificate property value. Identity certificate.
        Args:
            value: Value to set for the identityCertificate property.
        """
        self._identity_certificate = value
    
    @property
    def per_app_v_p_n_profile_id(self,) -> Optional[str]:
        """
        Gets the perAppVPNProfileId property value. Profile ID of the Per-App VPN policy to be used to access emails from the native Mail client
        Returns: Optional[str]
        """
        return self._per_app_v_p_n_profile_id
    
    @per_app_v_p_n_profile_id.setter
    def per_app_v_p_n_profile_id(self,value: Optional[str] = None) -> None:
        """
        Sets the perAppVPNProfileId property value. Profile ID of the Per-App VPN policy to be used to access emails from the native Mail client
        Args:
            value: Value to set for the perAppVPNProfileId property.
        """
        self._per_app_v_p_n_profile_id = value
    
    @property
    def require_smime(self,) -> Optional[bool]:
        """
        Gets the requireSmime property value. Indicates whether or not to use S/MIME certificate.
        Returns: Optional[bool]
        """
        return self._require_smime
    
    @require_smime.setter
    def require_smime(self,value: Optional[bool] = None) -> None:
        """
        Sets the requireSmime property value. Indicates whether or not to use S/MIME certificate.
        Args:
            value: Value to set for the requireSmime property.
        """
        self._require_smime = value
    
    @property
    def require_ssl(self,) -> Optional[bool]:
        """
        Gets the requireSsl property value. Indicates whether or not to use SSL.
        Returns: Optional[bool]
        """
        return self._require_ssl
    
    @require_ssl.setter
    def require_ssl(self,value: Optional[bool] = None) -> None:
        """
        Sets the requireSsl property value. Indicates whether or not to use SSL.
        Args:
            value: Value to set for the requireSsl property.
        """
        self._require_ssl = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("accountName", self.account_name)
        writer.write_enum_value("authenticationMethod", self.authentication_method)
        writer.write_bool_value("blockMovingMessagesToOtherEmailAccounts", self.block_moving_messages_to_other_email_accounts)
        writer.write_bool_value("blockSendingEmailFromThirdPartyApps", self.block_sending_email_from_third_party_apps)
        writer.write_bool_value("blockSyncingRecentlyUsedEmailAddresses", self.block_syncing_recently_used_email_addresses)
        writer.write_object_value("derivedCredentialSettings", self.derived_credential_settings)
        writer.write_enum_value("durationOfEmailToSync", self.duration_of_email_to_sync)
        writer.write_enum_value("easServices", self.eas_services)
        writer.write_bool_value("easServicesUserOverrideEnabled", self.eas_services_user_override_enabled)
        writer.write_enum_value("emailAddressSource", self.email_address_source)
        writer.write_enum_value("encryptionCertificateType", self.encryption_certificate_type)
        writer.write_str_value("hostName", self.host_name)
        writer.write_object_value("identityCertificate", self.identity_certificate)
        writer.write_str_value("perAppVPNProfileId", self.per_app_v_p_n_profile_id)
        writer.write_bool_value("requireSmime", self.require_smime)
        writer.write_bool_value("requireSsl", self.require_ssl)
        writer.write_enum_value("signingCertificateType", self.signing_certificate_type)
        writer.write_bool_value("smimeEnablePerMessageSwitch", self.smime_enable_per_message_switch)
        writer.write_bool_value("smimeEncryptByDefaultEnabled", self.smime_encrypt_by_default_enabled)
        writer.write_bool_value("smimeEncryptByDefaultUserOverrideEnabled", self.smime_encrypt_by_default_user_override_enabled)
        writer.write_object_value("smimeEncryptionCertificate", self.smime_encryption_certificate)
        writer.write_bool_value("smimeEncryptionCertificateUserOverrideEnabled", self.smime_encryption_certificate_user_override_enabled)
        writer.write_object_value("smimeSigningCertificate", self.smime_signing_certificate)
        writer.write_bool_value("smimeSigningCertificateUserOverrideEnabled", self.smime_signing_certificate_user_override_enabled)
        writer.write_bool_value("smimeSigningEnabled", self.smime_signing_enabled)
        writer.write_bool_value("smimeSigningUserOverrideEnabled", self.smime_signing_user_override_enabled)
        writer.write_bool_value("useOAuth", self.use_o_auth)
    
    @property
    def signing_certificate_type(self,) -> Optional[email_certificate_type.EmailCertificateType]:
        """
        Gets the signingCertificateType property value. Signing Certificate type for this Email profile. Possible values are: none, certificate, derivedCredential.
        Returns: Optional[email_certificate_type.EmailCertificateType]
        """
        return self._signing_certificate_type
    
    @signing_certificate_type.setter
    def signing_certificate_type(self,value: Optional[email_certificate_type.EmailCertificateType] = None) -> None:
        """
        Sets the signingCertificateType property value. Signing Certificate type for this Email profile. Possible values are: none, certificate, derivedCredential.
        Args:
            value: Value to set for the signingCertificateType property.
        """
        self._signing_certificate_type = value
    
    @property
    def smime_enable_per_message_switch(self,) -> Optional[bool]:
        """
        Gets the smimeEnablePerMessageSwitch property value. Indicates whether or not to allow unencrypted emails.
        Returns: Optional[bool]
        """
        return self._smime_enable_per_message_switch
    
    @smime_enable_per_message_switch.setter
    def smime_enable_per_message_switch(self,value: Optional[bool] = None) -> None:
        """
        Sets the smimeEnablePerMessageSwitch property value. Indicates whether or not to allow unencrypted emails.
        Args:
            value: Value to set for the smimeEnablePerMessageSwitch property.
        """
        self._smime_enable_per_message_switch = value
    
    @property
    def smime_encrypt_by_default_enabled(self,) -> Optional[bool]:
        """
        Gets the smimeEncryptByDefaultEnabled property value. If set to true S/MIME encryption is enabled by default.
        Returns: Optional[bool]
        """
        return self._smime_encrypt_by_default_enabled
    
    @smime_encrypt_by_default_enabled.setter
    def smime_encrypt_by_default_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the smimeEncryptByDefaultEnabled property value. If set to true S/MIME encryption is enabled by default.
        Args:
            value: Value to set for the smimeEncryptByDefaultEnabled property.
        """
        self._smime_encrypt_by_default_enabled = value
    
    @property
    def smime_encrypt_by_default_user_override_enabled(self,) -> Optional[bool]:
        """
        Gets the smimeEncryptByDefaultUserOverrideEnabled property value. If set to true, the user can toggle the encryption by default setting.
        Returns: Optional[bool]
        """
        return self._smime_encrypt_by_default_user_override_enabled
    
    @smime_encrypt_by_default_user_override_enabled.setter
    def smime_encrypt_by_default_user_override_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the smimeEncryptByDefaultUserOverrideEnabled property value. If set to true, the user can toggle the encryption by default setting.
        Args:
            value: Value to set for the smimeEncryptByDefaultUserOverrideEnabled property.
        """
        self._smime_encrypt_by_default_user_override_enabled = value
    
    @property
    def smime_encryption_certificate(self,) -> Optional[ios_certificate_profile.IosCertificateProfile]:
        """
        Gets the smimeEncryptionCertificate property value. S/MIME encryption certificate.
        Returns: Optional[ios_certificate_profile.IosCertificateProfile]
        """
        return self._smime_encryption_certificate
    
    @smime_encryption_certificate.setter
    def smime_encryption_certificate(self,value: Optional[ios_certificate_profile.IosCertificateProfile] = None) -> None:
        """
        Sets the smimeEncryptionCertificate property value. S/MIME encryption certificate.
        Args:
            value: Value to set for the smimeEncryptionCertificate property.
        """
        self._smime_encryption_certificate = value
    
    @property
    def smime_encryption_certificate_user_override_enabled(self,) -> Optional[bool]:
        """
        Gets the smimeEncryptionCertificateUserOverrideEnabled property value. If set to true the user can select the S/MIME encryption identity.
        Returns: Optional[bool]
        """
        return self._smime_encryption_certificate_user_override_enabled
    
    @smime_encryption_certificate_user_override_enabled.setter
    def smime_encryption_certificate_user_override_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the smimeEncryptionCertificateUserOverrideEnabled property value. If set to true the user can select the S/MIME encryption identity.
        Args:
            value: Value to set for the smimeEncryptionCertificateUserOverrideEnabled property.
        """
        self._smime_encryption_certificate_user_override_enabled = value
    
    @property
    def smime_signing_certificate(self,) -> Optional[ios_certificate_profile.IosCertificateProfile]:
        """
        Gets the smimeSigningCertificate property value. S/MIME signing certificate.
        Returns: Optional[ios_certificate_profile.IosCertificateProfile]
        """
        return self._smime_signing_certificate
    
    @smime_signing_certificate.setter
    def smime_signing_certificate(self,value: Optional[ios_certificate_profile.IosCertificateProfile] = None) -> None:
        """
        Sets the smimeSigningCertificate property value. S/MIME signing certificate.
        Args:
            value: Value to set for the smimeSigningCertificate property.
        """
        self._smime_signing_certificate = value
    
    @property
    def smime_signing_certificate_user_override_enabled(self,) -> Optional[bool]:
        """
        Gets the smimeSigningCertificateUserOverrideEnabled property value. If set to true, the user can select the signing identity.
        Returns: Optional[bool]
        """
        return self._smime_signing_certificate_user_override_enabled
    
    @smime_signing_certificate_user_override_enabled.setter
    def smime_signing_certificate_user_override_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the smimeSigningCertificateUserOverrideEnabled property value. If set to true, the user can select the signing identity.
        Args:
            value: Value to set for the smimeSigningCertificateUserOverrideEnabled property.
        """
        self._smime_signing_certificate_user_override_enabled = value
    
    @property
    def smime_signing_enabled(self,) -> Optional[bool]:
        """
        Gets the smimeSigningEnabled property value. If set to true S/MIME signing is enabled for this account
        Returns: Optional[bool]
        """
        return self._smime_signing_enabled
    
    @smime_signing_enabled.setter
    def smime_signing_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the smimeSigningEnabled property value. If set to true S/MIME signing is enabled for this account
        Args:
            value: Value to set for the smimeSigningEnabled property.
        """
        self._smime_signing_enabled = value
    
    @property
    def smime_signing_user_override_enabled(self,) -> Optional[bool]:
        """
        Gets the smimeSigningUserOverrideEnabled property value. If set to true, the user can toggle S/MIME signing on or off.
        Returns: Optional[bool]
        """
        return self._smime_signing_user_override_enabled
    
    @smime_signing_user_override_enabled.setter
    def smime_signing_user_override_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the smimeSigningUserOverrideEnabled property value. If set to true, the user can toggle S/MIME signing on or off.
        Args:
            value: Value to set for the smimeSigningUserOverrideEnabled property.
        """
        self._smime_signing_user_override_enabled = value
    
    @property
    def use_o_auth(self,) -> Optional[bool]:
        """
        Gets the useOAuth property value. Specifies whether the connection should use OAuth for authentication.
        Returns: Optional[bool]
        """
        return self._use_o_auth
    
    @use_o_auth.setter
    def use_o_auth(self,value: Optional[bool] = None) -> None:
        """
        Sets the useOAuth property value. Specifies whether the connection should use OAuth for authentication.
        Args:
            value: Value to set for the useOAuth property.
        """
        self._use_o_auth = value
    

