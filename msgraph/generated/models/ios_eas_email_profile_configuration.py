from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_management_derived_credential_settings, eas_authentication_method, eas_email_profile_configuration_base, eas_services, email_certificate_type, email_sync_duration, ios_certificate_profile, ios_certificate_profile_base, user_email_source

from . import eas_email_profile_configuration_base

@dataclass
class IosEasEmailProfileConfiguration(eas_email_profile_configuration_base.EasEmailProfileConfigurationBase):
    odata_type = "#microsoft.graph.iosEasEmailProfileConfiguration"
    # Account name.
    account_name: Optional[str] = None
    # Authentication method for this Email profile. Possible values are: usernameAndPassword, certificate, derivedCredential.
    authentication_method: Optional[eas_authentication_method.EasAuthenticationMethod] = None
    # Indicates whether or not to block moving messages to other email accounts.
    block_moving_messages_to_other_email_accounts: Optional[bool] = None
    # Indicates whether or not to block sending email from third party apps.
    block_sending_email_from_third_party_apps: Optional[bool] = None
    # Indicates whether or not to block syncing recently used email addresses, for instance - when composing new email.
    block_syncing_recently_used_email_addresses: Optional[bool] = None
    # Tenant level settings for the Derived Credentials to be used for authentication.
    derived_credential_settings: Optional[device_management_derived_credential_settings.DeviceManagementDerivedCredentialSettings] = None
    # Possible values for email sync duration.
    duration_of_email_to_sync: Optional[email_sync_duration.EmailSyncDuration] = None
    # Exchange data to sync. Possible values are: none, calendars, contacts, email, notes, reminders.
    eas_services: Optional[eas_services.EasServices] = None
    # Allow users to change sync settings.
    eas_services_user_override_enabled: Optional[bool] = None
    # Possible values for username source or email source.
    email_address_source: Optional[user_email_source.UserEmailSource] = None
    # Encryption Certificate type for this Email profile. Possible values are: none, certificate, derivedCredential.
    encryption_certificate_type: Optional[email_certificate_type.EmailCertificateType] = None
    # Exchange location that (URL) that the native mail app connects to.
    host_name: Optional[str] = None
    # Identity certificate.
    identity_certificate: Optional[ios_certificate_profile_base.IosCertificateProfileBase] = None
    # Profile ID of the Per-App VPN policy to be used to access emails from the native Mail client
    per_app_v_p_n_profile_id: Optional[str] = None
    # Indicates whether or not to use S/MIME certificate.
    require_smime: Optional[bool] = None
    # Indicates whether or not to use SSL.
    require_ssl: Optional[bool] = None
    # Signing Certificate type for this Email profile. Possible values are: none, certificate, derivedCredential.
    signing_certificate_type: Optional[email_certificate_type.EmailCertificateType] = None
    # Indicates whether or not to allow unencrypted emails.
    smime_enable_per_message_switch: Optional[bool] = None
    # If set to true S/MIME encryption is enabled by default.
    smime_encrypt_by_default_enabled: Optional[bool] = None
    # If set to true, the user can toggle the encryption by default setting.
    smime_encrypt_by_default_user_override_enabled: Optional[bool] = None
    # S/MIME encryption certificate.
    smime_encryption_certificate: Optional[ios_certificate_profile.IosCertificateProfile] = None
    # If set to true the user can select the S/MIME encryption identity.
    smime_encryption_certificate_user_override_enabled: Optional[bool] = None
    # S/MIME signing certificate.
    smime_signing_certificate: Optional[ios_certificate_profile.IosCertificateProfile] = None
    # If set to true, the user can select the signing identity.
    smime_signing_certificate_user_override_enabled: Optional[bool] = None
    # If set to true S/MIME signing is enabled for this account
    smime_signing_enabled: Optional[bool] = None
    # If set to true, the user can toggle S/MIME signing on or off.
    smime_signing_user_override_enabled: Optional[bool] = None
    # Specifies whether the connection should use OAuth for authentication.
    use_o_auth: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IosEasEmailProfileConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IosEasEmailProfileConfiguration
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return IosEasEmailProfileConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_management_derived_credential_settings, eas_authentication_method, eas_email_profile_configuration_base, eas_services, email_certificate_type, email_sync_duration, ios_certificate_profile, ios_certificate_profile_base, user_email_source

        from . import device_management_derived_credential_settings, eas_authentication_method, eas_email_profile_configuration_base, eas_services, email_certificate_type, email_sync_duration, ios_certificate_profile, ios_certificate_profile_base, user_email_source

        fields: Dict[str, Callable[[Any], None]] = {
            "accountName": lambda n : setattr(self, 'account_name', n.get_str_value()),
            "authenticationMethod": lambda n : setattr(self, 'authentication_method', n.get_enum_value(eas_authentication_method.EasAuthenticationMethod)),
            "blockMovingMessagesToOtherEmailAccounts": lambda n : setattr(self, 'block_moving_messages_to_other_email_accounts', n.get_bool_value()),
            "blockSendingEmailFromThirdPartyApps": lambda n : setattr(self, 'block_sending_email_from_third_party_apps', n.get_bool_value()),
            "blockSyncingRecentlyUsedEmailAddresses": lambda n : setattr(self, 'block_syncing_recently_used_email_addresses', n.get_bool_value()),
            "derivedCredentialSettings": lambda n : setattr(self, 'derived_credential_settings', n.get_object_value(device_management_derived_credential_settings.DeviceManagementDerivedCredentialSettings)),
            "durationOfEmailToSync": lambda n : setattr(self, 'duration_of_email_to_sync', n.get_enum_value(email_sync_duration.EmailSyncDuration)),
            "easServices": lambda n : setattr(self, 'eas_services', n.get_enum_value(eas_services.EasServices)),
            "easServicesUserOverrideEnabled": lambda n : setattr(self, 'eas_services_user_override_enabled', n.get_bool_value()),
            "emailAddressSource": lambda n : setattr(self, 'email_address_source', n.get_enum_value(user_email_source.UserEmailSource)),
            "encryptionCertificateType": lambda n : setattr(self, 'encryption_certificate_type', n.get_enum_value(email_certificate_type.EmailCertificateType)),
            "hostName": lambda n : setattr(self, 'host_name', n.get_str_value()),
            "identityCertificate": lambda n : setattr(self, 'identity_certificate', n.get_object_value(ios_certificate_profile_base.IosCertificateProfileBase)),
            "perAppVPNProfileId": lambda n : setattr(self, 'per_app_v_p_n_profile_id', n.get_str_value()),
            "requireSmime": lambda n : setattr(self, 'require_smime', n.get_bool_value()),
            "requireSsl": lambda n : setattr(self, 'require_ssl', n.get_bool_value()),
            "signingCertificateType": lambda n : setattr(self, 'signing_certificate_type', n.get_enum_value(email_certificate_type.EmailCertificateType)),
            "smimeEnablePerMessageSwitch": lambda n : setattr(self, 'smime_enable_per_message_switch', n.get_bool_value()),
            "smimeEncryptByDefaultEnabled": lambda n : setattr(self, 'smime_encrypt_by_default_enabled', n.get_bool_value()),
            "smimeEncryptByDefaultUserOverrideEnabled": lambda n : setattr(self, 'smime_encrypt_by_default_user_override_enabled', n.get_bool_value()),
            "smimeEncryptionCertificate": lambda n : setattr(self, 'smime_encryption_certificate', n.get_object_value(ios_certificate_profile.IosCertificateProfile)),
            "smimeEncryptionCertificateUserOverrideEnabled": lambda n : setattr(self, 'smime_encryption_certificate_user_override_enabled', n.get_bool_value()),
            "smimeSigningCertificate": lambda n : setattr(self, 'smime_signing_certificate', n.get_object_value(ios_certificate_profile.IosCertificateProfile)),
            "smimeSigningCertificateUserOverrideEnabled": lambda n : setattr(self, 'smime_signing_certificate_user_override_enabled', n.get_bool_value()),
            "smimeSigningEnabled": lambda n : setattr(self, 'smime_signing_enabled', n.get_bool_value()),
            "smimeSigningUserOverrideEnabled": lambda n : setattr(self, 'smime_signing_user_override_enabled', n.get_bool_value()),
            "useOAuth": lambda n : setattr(self, 'use_o_auth', n.get_bool_value()),
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
    

