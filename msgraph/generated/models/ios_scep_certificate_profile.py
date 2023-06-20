from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import certificate_store, custom_subject_alternative_name, extended_key_usage, ios_certificate_profile_base, ios_trusted_root_certificate, key_size, key_usages, managed_device_certificate_state

from . import ios_certificate_profile_base

@dataclass
class IosScepCertificateProfile(ios_certificate_profile_base.IosCertificateProfileBase):
    odata_type = "#microsoft.graph.iosScepCertificateProfile"
    # Target store certificate. Possible values are: user, machine.
    certificate_store: Optional[certificate_store.CertificateStore] = None
    # Custom Subject Alternative Name Settings. The OnPremisesUserPrincipalName variable is support as well as others documented here: https://go.microsoft.com/fwlink/?LinkId=2027630. This collection can contain a maximum of 500 elements.
    custom_subject_alternative_names: Optional[List[custom_subject_alternative_name.CustomSubjectAlternativeName]] = None
    # Extended Key Usage (EKU) settings. This collection can contain a maximum of 500 elements.
    extended_key_usages: Optional[List[extended_key_usage.ExtendedKeyUsage]] = None
    # Key Size Options.
    key_size: Optional[key_size.KeySize] = None
    # Key Usage Options.
    key_usage: Optional[key_usages.KeyUsages] = None
    # Certificate state for devices. This collection can contain a maximum of 2147483647 elements.
    managed_device_certificate_states: Optional[List[managed_device_certificate_state.ManagedDeviceCertificateState]] = None
    # Trusted Root Certificate.
    root_certificate: Optional[ios_trusted_root_certificate.IosTrustedRootCertificate] = None
    # SCEP Server Url(s).
    scep_server_urls: Optional[List[str]] = None
    # Custom String that defines the AAD Attribute.
    subject_alternative_name_format_string: Optional[str] = None
    # Custom format to use with SubjectNameFormat = Custom. Example: CN={{EmailAddress}},E={{EmailAddress}},OU=Enterprise Users,O=Contoso Corporation,L=Redmond,ST=WA,C=US
    subject_name_format_string: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IosScepCertificateProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IosScepCertificateProfile
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return IosScepCertificateProfile()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import certificate_store, custom_subject_alternative_name, extended_key_usage, ios_certificate_profile_base, ios_trusted_root_certificate, key_size, key_usages, managed_device_certificate_state

        from . import certificate_store, custom_subject_alternative_name, extended_key_usage, ios_certificate_profile_base, ios_trusted_root_certificate, key_size, key_usages, managed_device_certificate_state

        fields: Dict[str, Callable[[Any], None]] = {
            "certificateStore": lambda n : setattr(self, 'certificate_store', n.get_enum_value(certificate_store.CertificateStore)),
            "customSubjectAlternativeNames": lambda n : setattr(self, 'custom_subject_alternative_names', n.get_collection_of_object_values(custom_subject_alternative_name.CustomSubjectAlternativeName)),
            "extendedKeyUsages": lambda n : setattr(self, 'extended_key_usages', n.get_collection_of_object_values(extended_key_usage.ExtendedKeyUsage)),
            "keySize": lambda n : setattr(self, 'key_size', n.get_enum_value(key_size.KeySize)),
            "keyUsage": lambda n : setattr(self, 'key_usage', n.get_enum_value(key_usages.KeyUsages)),
            "managedDeviceCertificateStates": lambda n : setattr(self, 'managed_device_certificate_states', n.get_collection_of_object_values(managed_device_certificate_state.ManagedDeviceCertificateState)),
            "rootCertificate": lambda n : setattr(self, 'root_certificate', n.get_object_value(ios_trusted_root_certificate.IosTrustedRootCertificate)),
            "scepServerUrls": lambda n : setattr(self, 'scep_server_urls', n.get_collection_of_primitive_values(str)),
            "subjectAlternativeNameFormatString": lambda n : setattr(self, 'subject_alternative_name_format_string', n.get_str_value()),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_enum_value("certificateStore", self.certificate_store)
        writer.write_collection_of_object_values("customSubjectAlternativeNames", self.custom_subject_alternative_names)
        writer.write_collection_of_object_values("extendedKeyUsages", self.extended_key_usages)
        writer.write_enum_value("keySize", self.key_size)
        writer.write_enum_value("keyUsage", self.key_usage)
        writer.write_collection_of_object_values("managedDeviceCertificateStates", self.managed_device_certificate_states)
        writer.write_object_value("rootCertificate", self.root_certificate)
        writer.write_collection_of_primitive_values("scepServerUrls", self.scep_server_urls)
        writer.write_str_value("subjectAlternativeNameFormatString", self.subject_alternative_name_format_string)
        writer.write_str_value("subjectNameFormatString", self.subject_name_format_string)
    

