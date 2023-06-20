from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import certificate_validity_period_scale, device_configuration, key_storage_provider_option, subject_alternative_name_type, subject_name_format, windows10_certificate_profile_base, windows10_imported_p_f_x_certificate_profile, windows10_pkcs_certificate_profile, windows81_certificate_profile_base, windows81_s_c_e_p_certificate_profile, windows_phone81_imported_p_f_x_certificate_profile

from . import device_configuration

@dataclass
class WindowsCertificateProfileBase(device_configuration.DeviceConfiguration):
    odata_type = "#microsoft.graph.windowsCertificateProfileBase"
    # Certificate Validity Period Options.
    certificate_validity_period_scale: Optional[certificate_validity_period_scale.CertificateValidityPeriodScale] = None
    # Value for the Certificate Validity Period
    certificate_validity_period_value: Optional[int] = None
    # Key Storage Provider (KSP) Import Options.
    key_storage_provider: Optional[key_storage_provider_option.KeyStorageProviderOption] = None
    # Certificate renewal threshold percentage. Valid values 1 to 99
    renewal_threshold_percentage: Optional[int] = None
    # Certificate Subject Alternative Name Type. Possible values are: none, emailAddress, userPrincipalName, customAzureADAttribute, domainNameService, universalResourceIdentifier.
    subject_alternative_name_type: Optional[subject_alternative_name_type.SubjectAlternativeNameType] = None
    # Subject Name Format Options.
    subject_name_format: Optional[subject_name_format.SubjectNameFormat] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsCertificateProfileBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsCertificateProfileBase
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10CertificateProfileBase".casefold():
            from . import windows10_certificate_profile_base

            return windows10_certificate_profile_base.Windows10CertificateProfileBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10ImportedPFXCertificateProfile".casefold():
            from . import windows10_imported_p_f_x_certificate_profile

            return windows10_imported_p_f_x_certificate_profile.Windows10ImportedPFXCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10PkcsCertificateProfile".casefold():
            from . import windows10_pkcs_certificate_profile

            return windows10_pkcs_certificate_profile.Windows10PkcsCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows81CertificateProfileBase".casefold():
            from . import windows81_certificate_profile_base

            return windows81_certificate_profile_base.Windows81CertificateProfileBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows81SCEPCertificateProfile".casefold():
            from . import windows81_s_c_e_p_certificate_profile

            return windows81_s_c_e_p_certificate_profile.Windows81SCEPCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsPhone81ImportedPFXCertificateProfile".casefold():
            from . import windows_phone81_imported_p_f_x_certificate_profile

            return windows_phone81_imported_p_f_x_certificate_profile.WindowsPhone81ImportedPFXCertificateProfile()
        return WindowsCertificateProfileBase()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import certificate_validity_period_scale, device_configuration, key_storage_provider_option, subject_alternative_name_type, subject_name_format, windows10_certificate_profile_base, windows10_imported_p_f_x_certificate_profile, windows10_pkcs_certificate_profile, windows81_certificate_profile_base, windows81_s_c_e_p_certificate_profile, windows_phone81_imported_p_f_x_certificate_profile

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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_enum_value("certificateValidityPeriodScale", self.certificate_validity_period_scale)
        writer.write_int_value("certificateValidityPeriodValue", self.certificate_validity_period_value)
        writer.write_enum_value("keyStorageProvider", self.key_storage_provider)
        writer.write_int_value("renewalThresholdPercentage", self.renewal_threshold_percentage)
        writer.write_enum_value("subjectAlternativeNameType", self.subject_alternative_name_type)
        writer.write_enum_value("subjectNameFormat", self.subject_name_format)
    

