from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import apple_subject_name_format, certificate_validity_period_scale, device_configuration, mac_o_s_imported_p_f_x_certificate_profile, mac_o_s_pkcs_certificate_profile, mac_o_s_scep_certificate_profile, subject_alternative_name_type

from . import device_configuration

@dataclass
class MacOSCertificateProfileBase(device_configuration.DeviceConfiguration):
    """
    Mac OS certificate profile.
    """
    odata_type = "#microsoft.graph.macOSCertificateProfileBase"
    # Certificate Validity Period Options.
    certificate_validity_period_scale: Optional[certificate_validity_period_scale.CertificateValidityPeriodScale] = None
    # Value for the Certificate Validity Period.
    certificate_validity_period_value: Optional[int] = None
    # Certificate renewal threshold percentage.
    renewal_threshold_percentage: Optional[int] = None
    # Certificate Subject Alternative Name Type. Possible values are: none, emailAddress, userPrincipalName, customAzureADAttribute, domainNameService, universalResourceIdentifier.
    subject_alternative_name_type: Optional[subject_alternative_name_type.SubjectAlternativeNameType] = None
    # Subject Name Format Options for Apple devices.
    subject_name_format: Optional[apple_subject_name_format.AppleSubjectNameFormat] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MacOSCertificateProfileBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MacOSCertificateProfileBase
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.macOSImportedPFXCertificateProfile":
                from . import mac_o_s_imported_p_f_x_certificate_profile

                return mac_o_s_imported_p_f_x_certificate_profile.MacOSImportedPFXCertificateProfile()
            if mapping_value == "#microsoft.graph.macOSPkcsCertificateProfile":
                from . import mac_o_s_pkcs_certificate_profile

                return mac_o_s_pkcs_certificate_profile.MacOSPkcsCertificateProfile()
            if mapping_value == "#microsoft.graph.macOSScepCertificateProfile":
                from . import mac_o_s_scep_certificate_profile

                return mac_o_s_scep_certificate_profile.MacOSScepCertificateProfile()
        return MacOSCertificateProfileBase()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import apple_subject_name_format, certificate_validity_period_scale, device_configuration, mac_o_s_imported_p_f_x_certificate_profile, mac_o_s_pkcs_certificate_profile, mac_o_s_scep_certificate_profile, subject_alternative_name_type

        fields: Dict[str, Callable[[Any], None]] = {
            "certificateValidityPeriodScale": lambda n : setattr(self, 'certificate_validity_period_scale', n.get_enum_value(certificate_validity_period_scale.CertificateValidityPeriodScale)),
            "certificateValidityPeriodValue": lambda n : setattr(self, 'certificate_validity_period_value', n.get_int_value()),
            "renewalThresholdPercentage": lambda n : setattr(self, 'renewal_threshold_percentage', n.get_int_value()),
            "subjectAlternativeNameType": lambda n : setattr(self, 'subject_alternative_name_type', n.get_enum_value(subject_alternative_name_type.SubjectAlternativeNameType)),
            "subjectNameFormat": lambda n : setattr(self, 'subject_name_format', n.get_enum_value(apple_subject_name_format.AppleSubjectNameFormat)),
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
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("certificateValidityPeriodScale", self.certificate_validity_period_scale)
        writer.write_int_value("certificateValidityPeriodValue", self.certificate_validity_period_value)
        writer.write_int_value("renewalThresholdPercentage", self.renewal_threshold_percentage)
        writer.write_enum_value("subjectAlternativeNameType", self.subject_alternative_name_type)
        writer.write_enum_value("subjectNameFormat", self.subject_name_format)
    

