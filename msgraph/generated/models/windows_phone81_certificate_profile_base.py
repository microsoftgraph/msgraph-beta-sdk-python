from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .certificate_validity_period_scale import CertificateValidityPeriodScale
    from .device_configuration import DeviceConfiguration
    from .extended_key_usage import ExtendedKeyUsage
    from .key_storage_provider_option import KeyStorageProviderOption
    from .subject_alternative_name_type import SubjectAlternativeNameType
    from .subject_name_format import SubjectNameFormat
    from .windows_phone81_s_c_e_p_certificate_profile import WindowsPhone81SCEPCertificateProfile

from .device_configuration import DeviceConfiguration

@dataclass
class WindowsPhone81CertificateProfileBase(DeviceConfiguration):
    """
    Base Windows Phone 8.1+ certificate profile.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.windowsPhone81CertificateProfileBase"
    # Certificate Validity Period Options.
    certificate_validity_period_scale: Optional[CertificateValidityPeriodScale] = None
    # Value for the Certificate Validtiy Period.
    certificate_validity_period_value: Optional[int] = None
    # Extended Key Usage (EKU) settings. This collection can contain a maximum of 500 elements.
    extended_key_usages: Optional[List[ExtendedKeyUsage]] = None
    # Key Storage Provider (KSP) Import Options.
    key_storage_provider: Optional[KeyStorageProviderOption] = None
    # Certificate renewal threshold percentage.
    renewal_threshold_percentage: Optional[int] = None
    # Subject Alternative Name Options.
    subject_alternative_name_type: Optional[SubjectAlternativeNameType] = None
    # Subject Name Format Options.
    subject_name_format: Optional[SubjectNameFormat] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsPhone81CertificateProfileBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsPhone81CertificateProfileBase
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsPhone81SCEPCertificateProfile".casefold():
            from .windows_phone81_s_c_e_p_certificate_profile import WindowsPhone81SCEPCertificateProfile

            return WindowsPhone81SCEPCertificateProfile()
        return WindowsPhone81CertificateProfileBase()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .certificate_validity_period_scale import CertificateValidityPeriodScale
        from .device_configuration import DeviceConfiguration
        from .extended_key_usage import ExtendedKeyUsage
        from .key_storage_provider_option import KeyStorageProviderOption
        from .subject_alternative_name_type import SubjectAlternativeNameType
        from .subject_name_format import SubjectNameFormat
        from .windows_phone81_s_c_e_p_certificate_profile import WindowsPhone81SCEPCertificateProfile

        from .certificate_validity_period_scale import CertificateValidityPeriodScale
        from .device_configuration import DeviceConfiguration
        from .extended_key_usage import ExtendedKeyUsage
        from .key_storage_provider_option import KeyStorageProviderOption
        from .subject_alternative_name_type import SubjectAlternativeNameType
        from .subject_name_format import SubjectNameFormat
        from .windows_phone81_s_c_e_p_certificate_profile import WindowsPhone81SCEPCertificateProfile

        fields: Dict[str, Callable[[Any], None]] = {
            "certificateValidityPeriodScale": lambda n : setattr(self, 'certificate_validity_period_scale', n.get_enum_value(CertificateValidityPeriodScale)),
            "certificateValidityPeriodValue": lambda n : setattr(self, 'certificate_validity_period_value', n.get_int_value()),
            "extendedKeyUsages": lambda n : setattr(self, 'extended_key_usages', n.get_collection_of_object_values(ExtendedKeyUsage)),
            "keyStorageProvider": lambda n : setattr(self, 'key_storage_provider', n.get_enum_value(KeyStorageProviderOption)),
            "renewalThresholdPercentage": lambda n : setattr(self, 'renewal_threshold_percentage', n.get_int_value()),
            "subjectAlternativeNameType": lambda n : setattr(self, 'subject_alternative_name_type', n.get_collection_of_enum_values(SubjectAlternativeNameType)),
            "subjectNameFormat": lambda n : setattr(self, 'subject_name_format', n.get_enum_value(SubjectNameFormat)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_enum_value("certificateValidityPeriodScale", self.certificate_validity_period_scale)
        writer.write_int_value("certificateValidityPeriodValue", self.certificate_validity_period_value)
        writer.write_collection_of_object_values("extendedKeyUsages", self.extended_key_usages)
        writer.write_enum_value("keyStorageProvider", self.key_storage_provider)
        writer.write_int_value("renewalThresholdPercentage", self.renewal_threshold_percentage)
        writer.write_enum_value("subjectAlternativeNameType", self.subject_alternative_name_type)
        writer.write_enum_value("subjectNameFormat", self.subject_name_format)
    

