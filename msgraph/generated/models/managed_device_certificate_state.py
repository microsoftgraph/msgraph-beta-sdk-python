from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import certificate_issuance_states, certificate_revocation_status, certificate_validity_period_scale, device_platform_type, entity, key_storage_provider_option, key_usages, subject_alternative_name_type, subject_name_format

from . import entity

class ManagedDeviceCertificateState(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new managedDeviceCertificateState and sets the default values.
        """
        super().__init__()
        # Extended key usage
        self._certificate_enhanced_key_usage: Optional[str] = None
        # Error code
        self._certificate_error_code: Optional[int] = None
        # Certificate expiry date
        self._certificate_expiration_date_time: Optional[datetime] = None
        # Issuance date
        self._certificate_issuance_date_time: Optional[datetime] = None
        # Certificate Issuance State Options.
        self._certificate_issuance_state: Optional[certificate_issuance_states.CertificateIssuanceStates] = None
        # Issuer
        self._certificate_issuer: Optional[str] = None
        # Key length
        self._certificate_key_length: Optional[int] = None
        # Key Storage Provider (KSP) Import Options.
        self._certificate_key_storage_provider: Optional[key_storage_provider_option.KeyStorageProviderOption] = None
        # Key Usage Options.
        self._certificate_key_usage: Optional[key_usages.KeyUsages] = None
        # Last certificate issuance state change
        self._certificate_last_issuance_state_changed_date_time: Optional[datetime] = None
        # Certificate profile display name
        self._certificate_profile_display_name: Optional[str] = None
        # Certificate Revocation Status.
        self._certificate_revoke_status: Optional[certificate_revocation_status.CertificateRevocationStatus] = None
        # Serial number
        self._certificate_serial_number: Optional[str] = None
        # Subject Alternative Name Options.
        self._certificate_subject_alternative_name_format: Optional[subject_alternative_name_type.SubjectAlternativeNameType] = None
        # Subject alternative name format string for custom formats
        self._certificate_subject_alternative_name_format_string: Optional[str] = None
        # Subject Name Format Options.
        self._certificate_subject_name_format: Optional[subject_name_format.SubjectNameFormat] = None
        # Subject name format string for custom subject name formats
        self._certificate_subject_name_format_string: Optional[str] = None
        # Thumbprint
        self._certificate_thumbprint: Optional[str] = None
        # Validity period
        self._certificate_validity_period: Optional[int] = None
        # Certificate Validity Period Options.
        self._certificate_validity_period_units: Optional[certificate_validity_period_scale.CertificateValidityPeriodScale] = None
        # Device display name
        self._device_display_name: Optional[str] = None
        # Supported platform types.
        self._device_platform: Optional[device_platform_type.DevicePlatformType] = None
        # Last certificate issuance state change
        self._last_certificate_state_change_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # User display name
        self._user_display_name: Optional[str] = None
    
    @property
    def certificate_enhanced_key_usage(self,) -> Optional[str]:
        """
        Gets the certificateEnhancedKeyUsage property value. Extended key usage
        Returns: Optional[str]
        """
        return self._certificate_enhanced_key_usage
    
    @certificate_enhanced_key_usage.setter
    def certificate_enhanced_key_usage(self,value: Optional[str] = None) -> None:
        """
        Sets the certificateEnhancedKeyUsage property value. Extended key usage
        Args:
            value: Value to set for the certificate_enhanced_key_usage property.
        """
        self._certificate_enhanced_key_usage = value
    
    @property
    def certificate_error_code(self,) -> Optional[int]:
        """
        Gets the certificateErrorCode property value. Error code
        Returns: Optional[int]
        """
        return self._certificate_error_code
    
    @certificate_error_code.setter
    def certificate_error_code(self,value: Optional[int] = None) -> None:
        """
        Sets the certificateErrorCode property value. Error code
        Args:
            value: Value to set for the certificate_error_code property.
        """
        self._certificate_error_code = value
    
    @property
    def certificate_expiration_date_time(self,) -> Optional[datetime]:
        """
        Gets the certificateExpirationDateTime property value. Certificate expiry date
        Returns: Optional[datetime]
        """
        return self._certificate_expiration_date_time
    
    @certificate_expiration_date_time.setter
    def certificate_expiration_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the certificateExpirationDateTime property value. Certificate expiry date
        Args:
            value: Value to set for the certificate_expiration_date_time property.
        """
        self._certificate_expiration_date_time = value
    
    @property
    def certificate_issuance_date_time(self,) -> Optional[datetime]:
        """
        Gets the certificateIssuanceDateTime property value. Issuance date
        Returns: Optional[datetime]
        """
        return self._certificate_issuance_date_time
    
    @certificate_issuance_date_time.setter
    def certificate_issuance_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the certificateIssuanceDateTime property value. Issuance date
        Args:
            value: Value to set for the certificate_issuance_date_time property.
        """
        self._certificate_issuance_date_time = value
    
    @property
    def certificate_issuance_state(self,) -> Optional[certificate_issuance_states.CertificateIssuanceStates]:
        """
        Gets the certificateIssuanceState property value. Certificate Issuance State Options.
        Returns: Optional[certificate_issuance_states.CertificateIssuanceStates]
        """
        return self._certificate_issuance_state
    
    @certificate_issuance_state.setter
    def certificate_issuance_state(self,value: Optional[certificate_issuance_states.CertificateIssuanceStates] = None) -> None:
        """
        Sets the certificateIssuanceState property value. Certificate Issuance State Options.
        Args:
            value: Value to set for the certificate_issuance_state property.
        """
        self._certificate_issuance_state = value
    
    @property
    def certificate_issuer(self,) -> Optional[str]:
        """
        Gets the certificateIssuer property value. Issuer
        Returns: Optional[str]
        """
        return self._certificate_issuer
    
    @certificate_issuer.setter
    def certificate_issuer(self,value: Optional[str] = None) -> None:
        """
        Sets the certificateIssuer property value. Issuer
        Args:
            value: Value to set for the certificate_issuer property.
        """
        self._certificate_issuer = value
    
    @property
    def certificate_key_length(self,) -> Optional[int]:
        """
        Gets the certificateKeyLength property value. Key length
        Returns: Optional[int]
        """
        return self._certificate_key_length
    
    @certificate_key_length.setter
    def certificate_key_length(self,value: Optional[int] = None) -> None:
        """
        Sets the certificateKeyLength property value. Key length
        Args:
            value: Value to set for the certificate_key_length property.
        """
        self._certificate_key_length = value
    
    @property
    def certificate_key_storage_provider(self,) -> Optional[key_storage_provider_option.KeyStorageProviderOption]:
        """
        Gets the certificateKeyStorageProvider property value. Key Storage Provider (KSP) Import Options.
        Returns: Optional[key_storage_provider_option.KeyStorageProviderOption]
        """
        return self._certificate_key_storage_provider
    
    @certificate_key_storage_provider.setter
    def certificate_key_storage_provider(self,value: Optional[key_storage_provider_option.KeyStorageProviderOption] = None) -> None:
        """
        Sets the certificateKeyStorageProvider property value. Key Storage Provider (KSP) Import Options.
        Args:
            value: Value to set for the certificate_key_storage_provider property.
        """
        self._certificate_key_storage_provider = value
    
    @property
    def certificate_key_usage(self,) -> Optional[key_usages.KeyUsages]:
        """
        Gets the certificateKeyUsage property value. Key Usage Options.
        Returns: Optional[key_usages.KeyUsages]
        """
        return self._certificate_key_usage
    
    @certificate_key_usage.setter
    def certificate_key_usage(self,value: Optional[key_usages.KeyUsages] = None) -> None:
        """
        Sets the certificateKeyUsage property value. Key Usage Options.
        Args:
            value: Value to set for the certificate_key_usage property.
        """
        self._certificate_key_usage = value
    
    @property
    def certificate_last_issuance_state_changed_date_time(self,) -> Optional[datetime]:
        """
        Gets the certificateLastIssuanceStateChangedDateTime property value. Last certificate issuance state change
        Returns: Optional[datetime]
        """
        return self._certificate_last_issuance_state_changed_date_time
    
    @certificate_last_issuance_state_changed_date_time.setter
    def certificate_last_issuance_state_changed_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the certificateLastIssuanceStateChangedDateTime property value. Last certificate issuance state change
        Args:
            value: Value to set for the certificate_last_issuance_state_changed_date_time property.
        """
        self._certificate_last_issuance_state_changed_date_time = value
    
    @property
    def certificate_profile_display_name(self,) -> Optional[str]:
        """
        Gets the certificateProfileDisplayName property value. Certificate profile display name
        Returns: Optional[str]
        """
        return self._certificate_profile_display_name
    
    @certificate_profile_display_name.setter
    def certificate_profile_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the certificateProfileDisplayName property value. Certificate profile display name
        Args:
            value: Value to set for the certificate_profile_display_name property.
        """
        self._certificate_profile_display_name = value
    
    @property
    def certificate_revoke_status(self,) -> Optional[certificate_revocation_status.CertificateRevocationStatus]:
        """
        Gets the certificateRevokeStatus property value. Certificate Revocation Status.
        Returns: Optional[certificate_revocation_status.CertificateRevocationStatus]
        """
        return self._certificate_revoke_status
    
    @certificate_revoke_status.setter
    def certificate_revoke_status(self,value: Optional[certificate_revocation_status.CertificateRevocationStatus] = None) -> None:
        """
        Sets the certificateRevokeStatus property value. Certificate Revocation Status.
        Args:
            value: Value to set for the certificate_revoke_status property.
        """
        self._certificate_revoke_status = value
    
    @property
    def certificate_serial_number(self,) -> Optional[str]:
        """
        Gets the certificateSerialNumber property value. Serial number
        Returns: Optional[str]
        """
        return self._certificate_serial_number
    
    @certificate_serial_number.setter
    def certificate_serial_number(self,value: Optional[str] = None) -> None:
        """
        Sets the certificateSerialNumber property value. Serial number
        Args:
            value: Value to set for the certificate_serial_number property.
        """
        self._certificate_serial_number = value
    
    @property
    def certificate_subject_alternative_name_format(self,) -> Optional[subject_alternative_name_type.SubjectAlternativeNameType]:
        """
        Gets the certificateSubjectAlternativeNameFormat property value. Subject Alternative Name Options.
        Returns: Optional[subject_alternative_name_type.SubjectAlternativeNameType]
        """
        return self._certificate_subject_alternative_name_format
    
    @certificate_subject_alternative_name_format.setter
    def certificate_subject_alternative_name_format(self,value: Optional[subject_alternative_name_type.SubjectAlternativeNameType] = None) -> None:
        """
        Sets the certificateSubjectAlternativeNameFormat property value. Subject Alternative Name Options.
        Args:
            value: Value to set for the certificate_subject_alternative_name_format property.
        """
        self._certificate_subject_alternative_name_format = value
    
    @property
    def certificate_subject_alternative_name_format_string(self,) -> Optional[str]:
        """
        Gets the certificateSubjectAlternativeNameFormatString property value. Subject alternative name format string for custom formats
        Returns: Optional[str]
        """
        return self._certificate_subject_alternative_name_format_string
    
    @certificate_subject_alternative_name_format_string.setter
    def certificate_subject_alternative_name_format_string(self,value: Optional[str] = None) -> None:
        """
        Sets the certificateSubjectAlternativeNameFormatString property value. Subject alternative name format string for custom formats
        Args:
            value: Value to set for the certificate_subject_alternative_name_format_string property.
        """
        self._certificate_subject_alternative_name_format_string = value
    
    @property
    def certificate_subject_name_format(self,) -> Optional[subject_name_format.SubjectNameFormat]:
        """
        Gets the certificateSubjectNameFormat property value. Subject Name Format Options.
        Returns: Optional[subject_name_format.SubjectNameFormat]
        """
        return self._certificate_subject_name_format
    
    @certificate_subject_name_format.setter
    def certificate_subject_name_format(self,value: Optional[subject_name_format.SubjectNameFormat] = None) -> None:
        """
        Sets the certificateSubjectNameFormat property value. Subject Name Format Options.
        Args:
            value: Value to set for the certificate_subject_name_format property.
        """
        self._certificate_subject_name_format = value
    
    @property
    def certificate_subject_name_format_string(self,) -> Optional[str]:
        """
        Gets the certificateSubjectNameFormatString property value. Subject name format string for custom subject name formats
        Returns: Optional[str]
        """
        return self._certificate_subject_name_format_string
    
    @certificate_subject_name_format_string.setter
    def certificate_subject_name_format_string(self,value: Optional[str] = None) -> None:
        """
        Sets the certificateSubjectNameFormatString property value. Subject name format string for custom subject name formats
        Args:
            value: Value to set for the certificate_subject_name_format_string property.
        """
        self._certificate_subject_name_format_string = value
    
    @property
    def certificate_thumbprint(self,) -> Optional[str]:
        """
        Gets the certificateThumbprint property value. Thumbprint
        Returns: Optional[str]
        """
        return self._certificate_thumbprint
    
    @certificate_thumbprint.setter
    def certificate_thumbprint(self,value: Optional[str] = None) -> None:
        """
        Sets the certificateThumbprint property value. Thumbprint
        Args:
            value: Value to set for the certificate_thumbprint property.
        """
        self._certificate_thumbprint = value
    
    @property
    def certificate_validity_period(self,) -> Optional[int]:
        """
        Gets the certificateValidityPeriod property value. Validity period
        Returns: Optional[int]
        """
        return self._certificate_validity_period
    
    @certificate_validity_period.setter
    def certificate_validity_period(self,value: Optional[int] = None) -> None:
        """
        Sets the certificateValidityPeriod property value. Validity period
        Args:
            value: Value to set for the certificate_validity_period property.
        """
        self._certificate_validity_period = value
    
    @property
    def certificate_validity_period_units(self,) -> Optional[certificate_validity_period_scale.CertificateValidityPeriodScale]:
        """
        Gets the certificateValidityPeriodUnits property value. Certificate Validity Period Options.
        Returns: Optional[certificate_validity_period_scale.CertificateValidityPeriodScale]
        """
        return self._certificate_validity_period_units
    
    @certificate_validity_period_units.setter
    def certificate_validity_period_units(self,value: Optional[certificate_validity_period_scale.CertificateValidityPeriodScale] = None) -> None:
        """
        Sets the certificateValidityPeriodUnits property value. Certificate Validity Period Options.
        Args:
            value: Value to set for the certificate_validity_period_units property.
        """
        self._certificate_validity_period_units = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ManagedDeviceCertificateState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ManagedDeviceCertificateState
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ManagedDeviceCertificateState()
    
    @property
    def device_display_name(self,) -> Optional[str]:
        """
        Gets the deviceDisplayName property value. Device display name
        Returns: Optional[str]
        """
        return self._device_display_name
    
    @device_display_name.setter
    def device_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceDisplayName property value. Device display name
        Args:
            value: Value to set for the device_display_name property.
        """
        self._device_display_name = value
    
    @property
    def device_platform(self,) -> Optional[device_platform_type.DevicePlatformType]:
        """
        Gets the devicePlatform property value. Supported platform types.
        Returns: Optional[device_platform_type.DevicePlatformType]
        """
        return self._device_platform
    
    @device_platform.setter
    def device_platform(self,value: Optional[device_platform_type.DevicePlatformType] = None) -> None:
        """
        Sets the devicePlatform property value. Supported platform types.
        Args:
            value: Value to set for the device_platform property.
        """
        self._device_platform = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import certificate_issuance_states, certificate_revocation_status, certificate_validity_period_scale, device_platform_type, entity, key_storage_provider_option, key_usages, subject_alternative_name_type, subject_name_format

        fields: Dict[str, Callable[[Any], None]] = {
            "certificateEnhancedKeyUsage": lambda n : setattr(self, 'certificate_enhanced_key_usage', n.get_str_value()),
            "certificateErrorCode": lambda n : setattr(self, 'certificate_error_code', n.get_int_value()),
            "certificateExpirationDateTime": lambda n : setattr(self, 'certificate_expiration_date_time', n.get_datetime_value()),
            "certificateIssuanceDateTime": lambda n : setattr(self, 'certificate_issuance_date_time', n.get_datetime_value()),
            "certificateIssuanceState": lambda n : setattr(self, 'certificate_issuance_state', n.get_enum_value(certificate_issuance_states.CertificateIssuanceStates)),
            "certificateIssuer": lambda n : setattr(self, 'certificate_issuer', n.get_str_value()),
            "certificateKeyLength": lambda n : setattr(self, 'certificate_key_length', n.get_int_value()),
            "certificateKeyStorageProvider": lambda n : setattr(self, 'certificate_key_storage_provider', n.get_enum_value(key_storage_provider_option.KeyStorageProviderOption)),
            "certificateKeyUsage": lambda n : setattr(self, 'certificate_key_usage', n.get_enum_value(key_usages.KeyUsages)),
            "certificateLastIssuanceStateChangedDateTime": lambda n : setattr(self, 'certificate_last_issuance_state_changed_date_time', n.get_datetime_value()),
            "certificateProfileDisplayName": lambda n : setattr(self, 'certificate_profile_display_name', n.get_str_value()),
            "certificateRevokeStatus": lambda n : setattr(self, 'certificate_revoke_status', n.get_enum_value(certificate_revocation_status.CertificateRevocationStatus)),
            "certificateSerialNumber": lambda n : setattr(self, 'certificate_serial_number', n.get_str_value()),
            "certificateSubjectAlternativeNameFormat": lambda n : setattr(self, 'certificate_subject_alternative_name_format', n.get_enum_value(subject_alternative_name_type.SubjectAlternativeNameType)),
            "certificateSubjectAlternativeNameFormatString": lambda n : setattr(self, 'certificate_subject_alternative_name_format_string', n.get_str_value()),
            "certificateSubjectNameFormat": lambda n : setattr(self, 'certificate_subject_name_format', n.get_enum_value(subject_name_format.SubjectNameFormat)),
            "certificateSubjectNameFormatString": lambda n : setattr(self, 'certificate_subject_name_format_string', n.get_str_value()),
            "certificateThumbprint": lambda n : setattr(self, 'certificate_thumbprint', n.get_str_value()),
            "certificateValidityPeriod": lambda n : setattr(self, 'certificate_validity_period', n.get_int_value()),
            "certificateValidityPeriodUnits": lambda n : setattr(self, 'certificate_validity_period_units', n.get_enum_value(certificate_validity_period_scale.CertificateValidityPeriodScale)),
            "deviceDisplayName": lambda n : setattr(self, 'device_display_name', n.get_str_value()),
            "devicePlatform": lambda n : setattr(self, 'device_platform', n.get_enum_value(device_platform_type.DevicePlatformType)),
            "lastCertificateStateChangeDateTime": lambda n : setattr(self, 'last_certificate_state_change_date_time', n.get_datetime_value()),
            "userDisplayName": lambda n : setattr(self, 'user_display_name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_certificate_state_change_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastCertificateStateChangeDateTime property value. Last certificate issuance state change
        Returns: Optional[datetime]
        """
        return self._last_certificate_state_change_date_time
    
    @last_certificate_state_change_date_time.setter
    def last_certificate_state_change_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastCertificateStateChangeDateTime property value. Last certificate issuance state change
        Args:
            value: Value to set for the last_certificate_state_change_date_time property.
        """
        self._last_certificate_state_change_date_time = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("certificateEnhancedKeyUsage", self.certificate_enhanced_key_usage)
        writer.write_int_value("certificateErrorCode", self.certificate_error_code)
        writer.write_datetime_value("certificateExpirationDateTime", self.certificate_expiration_date_time)
        writer.write_datetime_value("certificateIssuanceDateTime", self.certificate_issuance_date_time)
        writer.write_enum_value("certificateIssuanceState", self.certificate_issuance_state)
        writer.write_str_value("certificateIssuer", self.certificate_issuer)
        writer.write_int_value("certificateKeyLength", self.certificate_key_length)
        writer.write_enum_value("certificateKeyStorageProvider", self.certificate_key_storage_provider)
        writer.write_enum_value("certificateKeyUsage", self.certificate_key_usage)
        writer.write_datetime_value("certificateLastIssuanceStateChangedDateTime", self.certificate_last_issuance_state_changed_date_time)
        writer.write_str_value("certificateProfileDisplayName", self.certificate_profile_display_name)
        writer.write_enum_value("certificateRevokeStatus", self.certificate_revoke_status)
        writer.write_str_value("certificateSerialNumber", self.certificate_serial_number)
        writer.write_enum_value("certificateSubjectAlternativeNameFormat", self.certificate_subject_alternative_name_format)
        writer.write_str_value("certificateSubjectAlternativeNameFormatString", self.certificate_subject_alternative_name_format_string)
        writer.write_enum_value("certificateSubjectNameFormat", self.certificate_subject_name_format)
        writer.write_str_value("certificateSubjectNameFormatString", self.certificate_subject_name_format_string)
        writer.write_str_value("certificateThumbprint", self.certificate_thumbprint)
        writer.write_int_value("certificateValidityPeriod", self.certificate_validity_period)
        writer.write_enum_value("certificateValidityPeriodUnits", self.certificate_validity_period_units)
        writer.write_str_value("deviceDisplayName", self.device_display_name)
        writer.write_enum_value("devicePlatform", self.device_platform)
        writer.write_datetime_value("lastCertificateStateChangeDateTime", self.last_certificate_state_change_date_time)
        writer.write_str_value("userDisplayName", self.user_display_name)
    
    @property
    def user_display_name(self,) -> Optional[str]:
        """
        Gets the userDisplayName property value. User display name
        Returns: Optional[str]
        """
        return self._user_display_name
    
    @user_display_name.setter
    def user_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userDisplayName property value. User display name
        Args:
            value: Value to set for the user_display_name property.
        """
        self._user_display_name = value
    

