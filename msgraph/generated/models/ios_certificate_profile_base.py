from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import apple_subject_name_format, certificate_validity_period_scale, ios_certificate_profile, ios_pkcs_certificate_profile, ios_scep_certificate_profile, subject_alternative_name_type

from . import ios_certificate_profile

@dataclass
class IosCertificateProfileBase(ios_certificate_profile.IosCertificateProfile):
    odata_type = "#microsoft.graph.iosCertificateProfileBase"
    # Certificate Validity Period Options.
    certificate_validity_period_scale: Optional[certificate_validity_period_scale.CertificateValidityPeriodScale] = None
    # Value for the Certificate Validity Period.
    certificate_validity_period_value: Optional[int] = None
    # Certificate renewal threshold percentage. Valid values 1 to 99
    renewal_threshold_percentage: Optional[int] = None
    # Certificate Subject Alternative Name type. Possible values are: none, emailAddress, userPrincipalName, customAzureADAttribute, domainNameService, universalResourceIdentifier.
    subject_alternative_name_type: Optional[subject_alternative_name_type.SubjectAlternativeNameType] = None
    # Subject Name Format Options for Apple devices.
    subject_name_format: Optional[apple_subject_name_format.AppleSubjectNameFormat] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IosCertificateProfileBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IosCertificateProfileBase
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosPkcsCertificateProfile".casefold():
            from . import ios_pkcs_certificate_profile

            return ios_pkcs_certificate_profile.IosPkcsCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosScepCertificateProfile".casefold():
            from . import ios_scep_certificate_profile

            return ios_scep_certificate_profile.IosScepCertificateProfile()
        return IosCertificateProfileBase()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import apple_subject_name_format, certificate_validity_period_scale, ios_certificate_profile, ios_pkcs_certificate_profile, ios_scep_certificate_profile, subject_alternative_name_type

        from . import apple_subject_name_format, certificate_validity_period_scale, ios_certificate_profile, ios_pkcs_certificate_profile, ios_scep_certificate_profile, subject_alternative_name_type

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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_enum_value("certificateValidityPeriodScale", self.certificate_validity_period_scale)
        writer.write_int_value("certificateValidityPeriodValue", self.certificate_validity_period_value)
        writer.write_int_value("renewalThresholdPercentage", self.renewal_threshold_percentage)
        writer.write_enum_value("subjectAlternativeNameType", self.subject_alternative_name_type)
        writer.write_enum_value("subjectNameFormat", self.subject_name_format)
    

