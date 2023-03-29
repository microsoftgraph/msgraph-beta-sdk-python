from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import certificate_validity_period_scale, device_configuration, key_storage_provider_option, subject_alternative_name_type, subject_name_format, windows10_certificate_profile_base, windows10_imported_p_f_x_certificate_profile, windows10_pkcs_certificate_profile, windows81_certificate_profile_base, windows81_s_c_e_p_certificate_profile, windows_phone81_imported_p_f_x_certificate_profile

from . import device_configuration

class WindowsCertificateProfileBase(device_configuration.DeviceConfiguration):
    def __init__(self,) -> None:
        """
        Instantiates a new WindowsCertificateProfileBase and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windowsCertificateProfileBase"
        # Certificate Validity Period Options.
        self._certificate_validity_period_scale: Optional[certificate_validity_period_scale.CertificateValidityPeriodScale] = None
        # Value for the Certificate Validity Period
        self._certificate_validity_period_value: Optional[int] = None
        # Key Storage Provider (KSP) Import Options.
        self._key_storage_provider: Optional[key_storage_provider_option.KeyStorageProviderOption] = None
        # Certificate renewal threshold percentage. Valid values 1 to 99
        self._renewal_threshold_percentage: Optional[int] = None
        # Certificate Subject Alternative Name Type. Possible values are: none, emailAddress, userPrincipalName, customAzureADAttribute, domainNameService, universalResourceIdentifier.
        self._subject_alternative_name_type: Optional[subject_alternative_name_type.SubjectAlternativeNameType] = None
        # Subject Name Format Options.
        self._subject_name_format: Optional[subject_name_format.SubjectNameFormat] = None
    
    @property
    def certificate_validity_period_scale(self,) -> Optional[certificate_validity_period_scale.CertificateValidityPeriodScale]:
        """
        Gets the certificateValidityPeriodScale property value. Certificate Validity Period Options.
        Returns: Optional[certificate_validity_period_scale.CertificateValidityPeriodScale]
        """
        return self._certificate_validity_period_scale
    
    @certificate_validity_period_scale.setter
    def certificate_validity_period_scale(self,value: Optional[certificate_validity_period_scale.CertificateValidityPeriodScale] = None) -> None:
        """
        Sets the certificateValidityPeriodScale property value. Certificate Validity Period Options.
        Args:
            value: Value to set for the certificate_validity_period_scale property.
        """
        self._certificate_validity_period_scale = value
    
    @property
    def certificate_validity_period_value(self,) -> Optional[int]:
        """
        Gets the certificateValidityPeriodValue property value. Value for the Certificate Validity Period
        Returns: Optional[int]
        """
        return self._certificate_validity_period_value
    
    @certificate_validity_period_value.setter
    def certificate_validity_period_value(self,value: Optional[int] = None) -> None:
        """
        Sets the certificateValidityPeriodValue property value. Value for the Certificate Validity Period
        Args:
            value: Value to set for the certificate_validity_period_value property.
        """
        self._certificate_validity_period_value = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsCertificateProfileBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsCertificateProfileBase
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.windows10CertificateProfileBase":
                from . import windows10_certificate_profile_base

                return windows10_certificate_profile_base.Windows10CertificateProfileBase()
            if mapping_value == "#microsoft.graph.windows10ImportedPFXCertificateProfile":
                from . import windows10_imported_p_f_x_certificate_profile

                return windows10_imported_p_f_x_certificate_profile.Windows10ImportedPFXCertificateProfile()
            if mapping_value == "#microsoft.graph.windows10PkcsCertificateProfile":
                from . import windows10_pkcs_certificate_profile

                return windows10_pkcs_certificate_profile.Windows10PkcsCertificateProfile()
            if mapping_value == "#microsoft.graph.windows81CertificateProfileBase":
                from . import windows81_certificate_profile_base

                return windows81_certificate_profile_base.Windows81CertificateProfileBase()
            if mapping_value == "#microsoft.graph.windows81SCEPCertificateProfile":
                from . import windows81_s_c_e_p_certificate_profile

                return windows81_s_c_e_p_certificate_profile.Windows81SCEPCertificateProfile()
            if mapping_value == "#microsoft.graph.windowsPhone81ImportedPFXCertificateProfile":
                from . import windows_phone81_imported_p_f_x_certificate_profile

                return windows_phone81_imported_p_f_x_certificate_profile.WindowsPhone81ImportedPFXCertificateProfile()
        return WindowsCertificateProfileBase()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import certificate_validity_period_scale, device_configuration, key_storage_provider_option, subject_alternative_name_type, subject_name_format, windows10_certificate_profile_base, windows10_imported_p_f_x_certificate_profile, windows10_pkcs_certificate_profile, windows81_certificate_profile_base, windows81_s_c_e_p_certificate_profile, windows_phone81_imported_p_f_x_certificate_profile

        fields: Dict[str, Callable[[Any], None]] = {
            "certificateValidityPeriodScale": lambda n : setattr(self, 'certificate_validity_period_scale', n.get_enum_value(certificate_validity_period_scale.CertificateValidityPeriodScale)),
            "certificateValidityPeriodValue": lambda n : setattr(self, 'certificate_validity_period_value', n.get_int_value()),
            "keyStorageProvider": lambda n : setattr(self, 'key_storage_provider', n.get_enum_value(key_storage_provider_option.KeyStorageProviderOption)),
            "renewalThresholdPercentage": lambda n : setattr(self, 'renewal_threshold_percentage', n.get_int_value()),
            "subjectAlternativeNameType": lambda n : setattr(self, 'subject_alternative_name_type', n.get_enum_value(subject_alternative_name_type.SubjectAlternativeNameType)),
            "subjectNameFormat": lambda n : setattr(self, 'subject_name_format', n.get_enum_value(subject_name_format.SubjectNameFormat)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def key_storage_provider(self,) -> Optional[key_storage_provider_option.KeyStorageProviderOption]:
        """
        Gets the keyStorageProvider property value. Key Storage Provider (KSP) Import Options.
        Returns: Optional[key_storage_provider_option.KeyStorageProviderOption]
        """
        return self._key_storage_provider
    
    @key_storage_provider.setter
    def key_storage_provider(self,value: Optional[key_storage_provider_option.KeyStorageProviderOption] = None) -> None:
        """
        Sets the keyStorageProvider property value. Key Storage Provider (KSP) Import Options.
        Args:
            value: Value to set for the key_storage_provider property.
        """
        self._key_storage_provider = value
    
    @property
    def renewal_threshold_percentage(self,) -> Optional[int]:
        """
        Gets the renewalThresholdPercentage property value. Certificate renewal threshold percentage. Valid values 1 to 99
        Returns: Optional[int]
        """
        return self._renewal_threshold_percentage
    
    @renewal_threshold_percentage.setter
    def renewal_threshold_percentage(self,value: Optional[int] = None) -> None:
        """
        Sets the renewalThresholdPercentage property value. Certificate renewal threshold percentage. Valid values 1 to 99
        Args:
            value: Value to set for the renewal_threshold_percentage property.
        """
        self._renewal_threshold_percentage = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("certificateValidityPeriodScale", self.certificate_validity_period_scale)
        writer.write_int_value("certificateValidityPeriodValue", self.certificate_validity_period_value)
        writer.write_enum_value("keyStorageProvider", self.key_storage_provider)
        writer.write_int_value("renewalThresholdPercentage", self.renewal_threshold_percentage)
        writer.write_enum_value("subjectAlternativeNameType", self.subject_alternative_name_type)
        writer.write_enum_value("subjectNameFormat", self.subject_name_format)
    
    @property
    def subject_alternative_name_type(self,) -> Optional[subject_alternative_name_type.SubjectAlternativeNameType]:
        """
        Gets the subjectAlternativeNameType property value. Certificate Subject Alternative Name Type. Possible values are: none, emailAddress, userPrincipalName, customAzureADAttribute, domainNameService, universalResourceIdentifier.
        Returns: Optional[subject_alternative_name_type.SubjectAlternativeNameType]
        """
        return self._subject_alternative_name_type
    
    @subject_alternative_name_type.setter
    def subject_alternative_name_type(self,value: Optional[subject_alternative_name_type.SubjectAlternativeNameType] = None) -> None:
        """
        Sets the subjectAlternativeNameType property value. Certificate Subject Alternative Name Type. Possible values are: none, emailAddress, userPrincipalName, customAzureADAttribute, domainNameService, universalResourceIdentifier.
        Args:
            value: Value to set for the subject_alternative_name_type property.
        """
        self._subject_alternative_name_type = value
    
    @property
    def subject_name_format(self,) -> Optional[subject_name_format.SubjectNameFormat]:
        """
        Gets the subjectNameFormat property value. Subject Name Format Options.
        Returns: Optional[subject_name_format.SubjectNameFormat]
        """
        return self._subject_name_format
    
    @subject_name_format.setter
    def subject_name_format(self,value: Optional[subject_name_format.SubjectNameFormat] = None) -> None:
        """
        Sets the subjectNameFormat property value. Subject Name Format Options.
        Args:
            value: Value to set for the subject_name_format property.
        """
        self._subject_name_format = value
    

