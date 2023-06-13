from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from . import certificate_store, certificate_validity_period_scale, extended_key_usage, hash_algorithms, key_size, key_storage_provider_option, key_usages, windows10_x_certificate_profile, windows10_x_custom_subject_alternative_name

from . import windows10_x_certificate_profile

@dataclass
class Windows10XSCEPCertificateProfile(windows10_x_certificate_profile.Windows10XCertificateProfile):
    odata_type = "#microsoft.graph.windows10XSCEPCertificateProfile"
    # CertificateStore types
    certificate_store: Optional[certificate_store.CertificateStore] = None
    # Certificate Validity Period Options.
    certificate_validity_period_scale: Optional[certificate_validity_period_scale.CertificateValidityPeriodScale] = None
    # Value for the Certificate Validity Period
    certificate_validity_period_value: Optional[int] = None
    # Extended Key Usage (EKU) settings.
    extended_key_usages: Optional[List[extended_key_usage.ExtendedKeyUsage]] = None
    # SCEP Hash Algorithm.
    hash_algorithm: Optional[List[hash_algorithms.HashAlgorithms]] = None
    # Key Size Options.
    key_size: Optional[key_size.KeySize] = None
    # Key Storage Provider (KSP) Import Options.
    key_storage_provider: Optional[key_storage_provider_option.KeyStorageProviderOption] = None
    # Key Usage Options.
    key_usage: Optional[key_usages.KeyUsages] = None
    # Certificate renewal threshold percentage
    renewal_threshold_percentage: Optional[int] = None
    # Trusted Root Certificate ID
    root_certificate_id: Optional[UUID] = None
    # SCEP Server Url(s).
    scep_server_urls: Optional[List[str]] = None
    # Custom AAD Attributes.
    subject_alternative_name_formats: Optional[List[windows10_x_custom_subject_alternative_name.Windows10XCustomSubjectAlternativeName]] = None
    # Custom format to use with SubjectNameFormat = Custom. Example: CN={{EmailAddress}},E={{EmailAddress}},OU=Enterprise Users,O=Contoso Corporation,L=Redmond,ST=WA,C=US
    subject_name_format_string: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Windows10XSCEPCertificateProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Windows10XSCEPCertificateProfile
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Windows10XSCEPCertificateProfile()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import certificate_store, certificate_validity_period_scale, extended_key_usage, hash_algorithms, key_size, key_storage_provider_option, key_usages, windows10_x_certificate_profile, windows10_x_custom_subject_alternative_name

        fields: Dict[str, Callable[[Any], None]] = {
            "certificateStore": lambda n : setattr(self, 'certificate_store', n.get_enum_value(certificate_store.CertificateStore)),
            "certificateValidityPeriodScale": lambda n : setattr(self, 'certificate_validity_period_scale', n.get_enum_value(certificate_validity_period_scale.CertificateValidityPeriodScale)),
            "certificateValidityPeriodValue": lambda n : setattr(self, 'certificate_validity_period_value', n.get_int_value()),
            "extendedKeyUsages": lambda n : setattr(self, 'extended_key_usages', n.get_collection_of_object_values(extended_key_usage.ExtendedKeyUsage)),
            "hashAlgorithm": lambda n : setattr(self, 'hash_algorithm', n.get_collection_of_enum_values(hash_algorithms.HashAlgorithms)),
            "keySize": lambda n : setattr(self, 'key_size', n.get_enum_value(key_size.KeySize)),
            "keyStorageProvider": lambda n : setattr(self, 'key_storage_provider', n.get_enum_value(key_storage_provider_option.KeyStorageProviderOption)),
            "keyUsage": lambda n : setattr(self, 'key_usage', n.get_enum_value(key_usages.KeyUsages)),
            "renewalThresholdPercentage": lambda n : setattr(self, 'renewal_threshold_percentage', n.get_int_value()),
            "rootCertificateId": lambda n : setattr(self, 'root_certificate_id', n.get_uuid_value()),
            "scepServerUrls": lambda n : setattr(self, 'scep_server_urls', n.get_collection_of_primitive_values(str)),
            "subjectAlternativeNameFormats": lambda n : setattr(self, 'subject_alternative_name_formats', n.get_collection_of_object_values(windows10_x_custom_subject_alternative_name.Windows10XCustomSubjectAlternativeName)),
            "subjectNameFormatString": lambda n : setattr(self, 'subject_name_format_string', n.get_str_value()),
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
        writer.write_enum_value("certificateStore", self.certificate_store)
        writer.write_enum_value("certificateValidityPeriodScale", self.certificate_validity_period_scale)
        writer.write_int_value("certificateValidityPeriodValue", self.certificate_validity_period_value)
        writer.write_collection_of_object_values("extendedKeyUsages", self.extended_key_usages)
        writer.write_enum_value("hashAlgorithm", self.hash_algorithm)
        writer.write_enum_value("keySize", self.key_size)
        writer.write_enum_value("keyStorageProvider", self.key_storage_provider)
        writer.write_enum_value("keyUsage", self.key_usage)
        writer.write_int_value("renewalThresholdPercentage", self.renewal_threshold_percentage)
        writer.write_uuid_value("rootCertificateId", self.root_certificate_id)
        writer.write_collection_of_primitive_values("scepServerUrls", self.scep_server_urls)
        writer.write_collection_of_object_values("subjectAlternativeNameFormats", self.subject_alternative_name_formats)
        writer.write_str_value("subjectNameFormatString", self.subject_name_format_string)
    

