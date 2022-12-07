from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

android_work_profile_certificate_profile_base = lazy_import('msgraph.generated.models.android_work_profile_certificate_profile_base')
certificate_store = lazy_import('msgraph.generated.models.certificate_store')
custom_subject_alternative_name = lazy_import('msgraph.generated.models.custom_subject_alternative_name')
hash_algorithms = lazy_import('msgraph.generated.models.hash_algorithms')
key_size = lazy_import('msgraph.generated.models.key_size')
key_usages = lazy_import('msgraph.generated.models.key_usages')
managed_device_certificate_state = lazy_import('msgraph.generated.models.managed_device_certificate_state')

class AndroidWorkProfileScepCertificateProfile(android_work_profile_certificate_profile_base.AndroidWorkProfileCertificateProfileBase):
    @property
    def certificate_store(self,) -> Optional[certificate_store.CertificateStore]:
        """
        Gets the certificateStore property value. Target store certificate. Possible values are: user, machine.
        Returns: Optional[certificate_store.CertificateStore]
        """
        return self._certificate_store
    
    @certificate_store.setter
    def certificate_store(self,value: Optional[certificate_store.CertificateStore] = None) -> None:
        """
        Sets the certificateStore property value. Target store certificate. Possible values are: user, machine.
        Args:
            value: Value to set for the certificateStore property.
        """
        self._certificate_store = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new AndroidWorkProfileScepCertificateProfile and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.androidWorkProfileScepCertificateProfile"
        # Target store certificate. Possible values are: user, machine.
        self._certificate_store: Optional[certificate_store.CertificateStore] = None
        # Custom Subject Alternative Name Settings. This collection can contain a maximum of 500 elements.
        self._custom_subject_alternative_names: Optional[List[custom_subject_alternative_name.CustomSubjectAlternativeName]] = None
        # Hash Algorithm Options.
        self._hash_algorithm: Optional[hash_algorithms.HashAlgorithms] = None
        # Key Size Options.
        self._key_size: Optional[key_size.KeySize] = None
        # Key Usage Options.
        self._key_usage: Optional[key_usages.KeyUsages] = None
        # Certificate state for devices. This collection can contain a maximum of 2147483647 elements.
        self._managed_device_certificate_states: Optional[List[managed_device_certificate_state.ManagedDeviceCertificateState]] = None
        # SCEP Server Url(s)
        self._scep_server_urls: Optional[List[str]] = None
        # Custom String that defines the AAD Attribute.
        self._subject_alternative_name_format_string: Optional[str] = None
        # Custom format to use with SubjectNameFormat = Custom. Example: CN={{EmailAddress}},E={{EmailAddress}},OU=Enterprise Users,O=Contoso Corporation,L=Redmond,ST=WA,C=US
        self._subject_name_format_string: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AndroidWorkProfileScepCertificateProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AndroidWorkProfileScepCertificateProfile
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AndroidWorkProfileScepCertificateProfile()
    
    @property
    def custom_subject_alternative_names(self,) -> Optional[List[custom_subject_alternative_name.CustomSubjectAlternativeName]]:
        """
        Gets the customSubjectAlternativeNames property value. Custom Subject Alternative Name Settings. This collection can contain a maximum of 500 elements.
        Returns: Optional[List[custom_subject_alternative_name.CustomSubjectAlternativeName]]
        """
        return self._custom_subject_alternative_names
    
    @custom_subject_alternative_names.setter
    def custom_subject_alternative_names(self,value: Optional[List[custom_subject_alternative_name.CustomSubjectAlternativeName]] = None) -> None:
        """
        Sets the customSubjectAlternativeNames property value. Custom Subject Alternative Name Settings. This collection can contain a maximum of 500 elements.
        Args:
            value: Value to set for the customSubjectAlternativeNames property.
        """
        self._custom_subject_alternative_names = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "certificate_store": lambda n : setattr(self, 'certificate_store', n.get_enum_value(certificate_store.CertificateStore)),
            "custom_subject_alternative_names": lambda n : setattr(self, 'custom_subject_alternative_names', n.get_collection_of_object_values(custom_subject_alternative_name.CustomSubjectAlternativeName)),
            "hash_algorithm": lambda n : setattr(self, 'hash_algorithm', n.get_enum_value(hash_algorithms.HashAlgorithms)),
            "key_size": lambda n : setattr(self, 'key_size', n.get_enum_value(key_size.KeySize)),
            "key_usage": lambda n : setattr(self, 'key_usage', n.get_enum_value(key_usages.KeyUsages)),
            "managed_device_certificate_states": lambda n : setattr(self, 'managed_device_certificate_states', n.get_collection_of_object_values(managed_device_certificate_state.ManagedDeviceCertificateState)),
            "scep_server_urls": lambda n : setattr(self, 'scep_server_urls', n.get_collection_of_primitive_values(str)),
            "subject_alternative_name_format_string": lambda n : setattr(self, 'subject_alternative_name_format_string', n.get_str_value()),
            "subject_name_format_string": lambda n : setattr(self, 'subject_name_format_string', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def hash_algorithm(self,) -> Optional[hash_algorithms.HashAlgorithms]:
        """
        Gets the hashAlgorithm property value. Hash Algorithm Options.
        Returns: Optional[hash_algorithms.HashAlgorithms]
        """
        return self._hash_algorithm
    
    @hash_algorithm.setter
    def hash_algorithm(self,value: Optional[hash_algorithms.HashAlgorithms] = None) -> None:
        """
        Sets the hashAlgorithm property value. Hash Algorithm Options.
        Args:
            value: Value to set for the hashAlgorithm property.
        """
        self._hash_algorithm = value
    
    @property
    def key_size(self,) -> Optional[key_size.KeySize]:
        """
        Gets the keySize property value. Key Size Options.
        Returns: Optional[key_size.KeySize]
        """
        return self._key_size
    
    @key_size.setter
    def key_size(self,value: Optional[key_size.KeySize] = None) -> None:
        """
        Sets the keySize property value. Key Size Options.
        Args:
            value: Value to set for the keySize property.
        """
        self._key_size = value
    
    @property
    def key_usage(self,) -> Optional[key_usages.KeyUsages]:
        """
        Gets the keyUsage property value. Key Usage Options.
        Returns: Optional[key_usages.KeyUsages]
        """
        return self._key_usage
    
    @key_usage.setter
    def key_usage(self,value: Optional[key_usages.KeyUsages] = None) -> None:
        """
        Sets the keyUsage property value. Key Usage Options.
        Args:
            value: Value to set for the keyUsage property.
        """
        self._key_usage = value
    
    @property
    def managed_device_certificate_states(self,) -> Optional[List[managed_device_certificate_state.ManagedDeviceCertificateState]]:
        """
        Gets the managedDeviceCertificateStates property value. Certificate state for devices. This collection can contain a maximum of 2147483647 elements.
        Returns: Optional[List[managed_device_certificate_state.ManagedDeviceCertificateState]]
        """
        return self._managed_device_certificate_states
    
    @managed_device_certificate_states.setter
    def managed_device_certificate_states(self,value: Optional[List[managed_device_certificate_state.ManagedDeviceCertificateState]] = None) -> None:
        """
        Sets the managedDeviceCertificateStates property value. Certificate state for devices. This collection can contain a maximum of 2147483647 elements.
        Args:
            value: Value to set for the managedDeviceCertificateStates property.
        """
        self._managed_device_certificate_states = value
    
    @property
    def scep_server_urls(self,) -> Optional[List[str]]:
        """
        Gets the scepServerUrls property value. SCEP Server Url(s)
        Returns: Optional[List[str]]
        """
        return self._scep_server_urls
    
    @scep_server_urls.setter
    def scep_server_urls(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the scepServerUrls property value. SCEP Server Url(s)
        Args:
            value: Value to set for the scepServerUrls property.
        """
        self._scep_server_urls = value
    
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
        writer.write_collection_of_object_values("customSubjectAlternativeNames", self.custom_subject_alternative_names)
        writer.write_enum_value("hashAlgorithm", self.hash_algorithm)
        writer.write_enum_value("keySize", self.key_size)
        writer.write_enum_value("keyUsage", self.key_usage)
        writer.write_collection_of_object_values("managedDeviceCertificateStates", self.managed_device_certificate_states)
        writer.write_collection_of_primitive_values("scepServerUrls", self.scep_server_urls)
        writer.write_str_value("subjectAlternativeNameFormatString", self.subject_alternative_name_format_string)
        writer.write_str_value("subjectNameFormatString", self.subject_name_format_string)
    
    @property
    def subject_alternative_name_format_string(self,) -> Optional[str]:
        """
        Gets the subjectAlternativeNameFormatString property value. Custom String that defines the AAD Attribute.
        Returns: Optional[str]
        """
        return self._subject_alternative_name_format_string
    
    @subject_alternative_name_format_string.setter
    def subject_alternative_name_format_string(self,value: Optional[str] = None) -> None:
        """
        Sets the subjectAlternativeNameFormatString property value. Custom String that defines the AAD Attribute.
        Args:
            value: Value to set for the subjectAlternativeNameFormatString property.
        """
        self._subject_alternative_name_format_string = value
    
    @property
    def subject_name_format_string(self,) -> Optional[str]:
        """
        Gets the subjectNameFormatString property value. Custom format to use with SubjectNameFormat = Custom. Example: CN={{EmailAddress}},E={{EmailAddress}},OU=Enterprise Users,O=Contoso Corporation,L=Redmond,ST=WA,C=US
        Returns: Optional[str]
        """
        return self._subject_name_format_string
    
    @subject_name_format_string.setter
    def subject_name_format_string(self,value: Optional[str] = None) -> None:
        """
        Sets the subjectNameFormatString property value. Custom format to use with SubjectNameFormat = Custom. Example: CN={{EmailAddress}},E={{EmailAddress}},OU=Enterprise Users,O=Contoso Corporation,L=Redmond,ST=WA,C=US
        Args:
            value: Value to set for the subjectNameFormatString property.
        """
        self._subject_name_format_string = value
    

