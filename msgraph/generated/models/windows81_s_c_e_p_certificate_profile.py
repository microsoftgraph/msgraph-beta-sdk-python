from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .certificate_store import CertificateStore
    from .hash_algorithms import HashAlgorithms
    from .key_size import KeySize
    from .key_usages import KeyUsages
    from .managed_device_certificate_state import ManagedDeviceCertificateState
    from .windows81_certificate_profile_base import Windows81CertificateProfileBase
    from .windows81_trusted_root_certificate import Windows81TrustedRootCertificate

from .windows81_certificate_profile_base import Windows81CertificateProfileBase

@dataclass
class Windows81SCEPCertificateProfile(Windows81CertificateProfileBase):
    """
    Windows 8.1+ SCEP certificate profile
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.windows81SCEPCertificateProfile"
    # Target store certificate. Possible values are: user, machine.
    certificate_store: Optional[CertificateStore] = None
    # Hash Algorithm Options.
    hash_algorithm: Optional[HashAlgorithms] = None
    # Key Size Options.
    key_size: Optional[KeySize] = None
    # Key Usage Options.
    key_usage: Optional[KeyUsages] = None
    # Certificate state for devices. This collection can contain a maximum of 2147483647 elements.
    managed_device_certificate_states: Optional[List[ManagedDeviceCertificateState]] = None
    # Trusted Root Certificate
    root_certificate: Optional[Windows81TrustedRootCertificate] = None
    # SCEP Server Url(s).
    scep_server_urls: Optional[List[str]] = None
    # Custom String that defines the AAD Attribute.
    subject_alternative_name_format_string: Optional[str] = None
    # Custom format to use with SubjectNameFormat = Custom. Example: CN={{EmailAddress}},E={{EmailAddress}},OU=Enterprise Users,O=Contoso Corporation,L=Redmond,ST=WA,C=US
    subject_name_format_string: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Windows81SCEPCertificateProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Windows81SCEPCertificateProfile
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Windows81SCEPCertificateProfile()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .certificate_store import CertificateStore
        from .hash_algorithms import HashAlgorithms
        from .key_size import KeySize
        from .key_usages import KeyUsages
        from .managed_device_certificate_state import ManagedDeviceCertificateState
        from .windows81_certificate_profile_base import Windows81CertificateProfileBase
        from .windows81_trusted_root_certificate import Windows81TrustedRootCertificate

        from .certificate_store import CertificateStore
        from .hash_algorithms import HashAlgorithms
        from .key_size import KeySize
        from .key_usages import KeyUsages
        from .managed_device_certificate_state import ManagedDeviceCertificateState
        from .windows81_certificate_profile_base import Windows81CertificateProfileBase
        from .windows81_trusted_root_certificate import Windows81TrustedRootCertificate

        fields: Dict[str, Callable[[Any], None]] = {
            "certificateStore": lambda n : setattr(self, 'certificate_store', n.get_enum_value(CertificateStore)),
            "hashAlgorithm": lambda n : setattr(self, 'hash_algorithm', n.get_collection_of_enum_values(HashAlgorithms)),
            "keySize": lambda n : setattr(self, 'key_size', n.get_enum_value(KeySize)),
            "keyUsage": lambda n : setattr(self, 'key_usage', n.get_collection_of_enum_values(KeyUsages)),
            "managedDeviceCertificateStates": lambda n : setattr(self, 'managed_device_certificate_states', n.get_collection_of_object_values(ManagedDeviceCertificateState)),
            "rootCertificate": lambda n : setattr(self, 'root_certificate', n.get_object_value(Windows81TrustedRootCertificate)),
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
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_enum_value("certificateStore", self.certificate_store)
        writer.write_enum_value("hashAlgorithm", self.hash_algorithm)
        writer.write_enum_value("keySize", self.key_size)
        writer.write_enum_value("keyUsage", self.key_usage)
        writer.write_collection_of_object_values("managedDeviceCertificateStates", self.managed_device_certificate_states)
        writer.write_object_value("rootCertificate", self.root_certificate)
        writer.write_collection_of_primitive_values("scepServerUrls", self.scep_server_urls)
        writer.write_str_value("subjectAlternativeNameFormatString", self.subject_alternative_name_format_string)
        writer.write_str_value("subjectNameFormatString", self.subject_name_format_string)
    

