from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import android_for_work_imported_p_f_x_certificate_profile, android_imported_p_f_x_certificate_profile, android_pkcs_certificate_profile, android_scep_certificate_profile, android_trusted_root_certificate, certificate_validity_period_scale, device_configuration, extended_key_usage, subject_alternative_name_type, subject_name_format

from . import device_configuration

@dataclass
class AndroidCertificateProfileBase(device_configuration.DeviceConfiguration):
    odata_type = "#microsoft.graph.androidCertificateProfileBase"
    # Certificate Validity Period Options.
    certificate_validity_period_scale: Optional[certificate_validity_period_scale.CertificateValidityPeriodScale] = None
    # Value for the Certificate Validity Period.
    certificate_validity_period_value: Optional[int] = None
    # Extended Key Usage (EKU) settings. This collection can contain a maximum of 500 elements.
    extended_key_usages: Optional[List[extended_key_usage.ExtendedKeyUsage]] = None
    # Certificate renewal threshold percentage. Valid values 1 to 99
    renewal_threshold_percentage: Optional[int] = None
    # Trusted Root Certificate.
    root_certificate: Optional[android_trusted_root_certificate.AndroidTrustedRootCertificate] = None
    # Subject Alternative Name Options.
    subject_alternative_name_type: Optional[subject_alternative_name_type.SubjectAlternativeNameType] = None
    # Subject Name Format Options.
    subject_name_format: Optional[subject_name_format.SubjectNameFormat] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AndroidCertificateProfileBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AndroidCertificateProfileBase
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidForWorkImportedPFXCertificateProfile".casefold():
            from . import android_for_work_imported_p_f_x_certificate_profile

            return android_for_work_imported_p_f_x_certificate_profile.AndroidForWorkImportedPFXCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidImportedPFXCertificateProfile".casefold():
            from . import android_imported_p_f_x_certificate_profile

            return android_imported_p_f_x_certificate_profile.AndroidImportedPFXCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidPkcsCertificateProfile".casefold():
            from . import android_pkcs_certificate_profile

            return android_pkcs_certificate_profile.AndroidPkcsCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidScepCertificateProfile".casefold():
            from . import android_scep_certificate_profile

            return android_scep_certificate_profile.AndroidScepCertificateProfile()
        return AndroidCertificateProfileBase()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import android_for_work_imported_p_f_x_certificate_profile, android_imported_p_f_x_certificate_profile, android_pkcs_certificate_profile, android_scep_certificate_profile, android_trusted_root_certificate, certificate_validity_period_scale, device_configuration, extended_key_usage, subject_alternative_name_type, subject_name_format

        from . import android_for_work_imported_p_f_x_certificate_profile, android_imported_p_f_x_certificate_profile, android_pkcs_certificate_profile, android_scep_certificate_profile, android_trusted_root_certificate, certificate_validity_period_scale, device_configuration, extended_key_usage, subject_alternative_name_type, subject_name_format

        fields: Dict[str, Callable[[Any], None]] = {
            "certificateValidityPeriodScale": lambda n : setattr(self, 'certificate_validity_period_scale', n.get_enum_value(certificate_validity_period_scale.CertificateValidityPeriodScale)),
            "certificateValidityPeriodValue": lambda n : setattr(self, 'certificate_validity_period_value', n.get_int_value()),
            "extendedKeyUsages": lambda n : setattr(self, 'extended_key_usages', n.get_collection_of_object_values(extended_key_usage.ExtendedKeyUsage)),
            "renewalThresholdPercentage": lambda n : setattr(self, 'renewal_threshold_percentage', n.get_int_value()),
            "rootCertificate": lambda n : setattr(self, 'root_certificate', n.get_object_value(android_trusted_root_certificate.AndroidTrustedRootCertificate)),
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
        writer.write_collection_of_object_values("extendedKeyUsages", self.extended_key_usages)
        writer.write_int_value("renewalThresholdPercentage", self.renewal_threshold_percentage)
        writer.write_object_value("rootCertificate", self.root_certificate)
        writer.write_enum_value("subjectAlternativeNameType", self.subject_alternative_name_type)
        writer.write_enum_value("subjectNameFormat", self.subject_name_format)
    

