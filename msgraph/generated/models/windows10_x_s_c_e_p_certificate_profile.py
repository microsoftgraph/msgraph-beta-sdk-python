from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

certificate_store = lazy_import('msgraph.generated.models.certificate_store')
certificate_validity_period_scale = lazy_import('msgraph.generated.models.certificate_validity_period_scale')
extended_key_usage = lazy_import('msgraph.generated.models.extended_key_usage')
hash_algorithms = lazy_import('msgraph.generated.models.hash_algorithms')
key_size = lazy_import('msgraph.generated.models.key_size')
key_storage_provider_option = lazy_import('msgraph.generated.models.key_storage_provider_option')
key_usages = lazy_import('msgraph.generated.models.key_usages')
windows10_x_certificate_profile = lazy_import('msgraph.generated.models.windows10_x_certificate_profile')
windows10_x_custom_subject_alternative_name = lazy_import('msgraph.generated.models.windows10_x_custom_subject_alternative_name')

class Windows10XSCEPCertificateProfile(windows10_x_certificate_profile.Windows10XCertificateProfile):
    @property
    def certificate_store(self,) -> Optional[certificate_store.CertificateStore]:
        """
        Gets the certificateStore property value. CertificateStore types
        Returns: Optional[certificate_store.CertificateStore]
        """
        return self._certificate_store
    
    @certificate_store.setter
    def certificate_store(self,value: Optional[certificate_store.CertificateStore] = None) -> None:
        """
        Sets the certificateStore property value. CertificateStore types
        Args:
            value: Value to set for the certificateStore property.
        """
        self._certificate_store = value
    
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
            value: Value to set for the certificateValidityPeriodScale property.
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
            value: Value to set for the certificateValidityPeriodValue property.
        """
        self._certificate_validity_period_value = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new Windows10XSCEPCertificateProfile and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windows10XSCEPCertificateProfile"
        # CertificateStore types
        self._certificate_store: Optional[certificate_store.CertificateStore] = None
        # Certificate Validity Period Options.
        self._certificate_validity_period_scale: Optional[certificate_validity_period_scale.CertificateValidityPeriodScale] = None
        # Value for the Certificate Validity Period
        self._certificate_validity_period_value: Optional[int] = None
        # Extended Key Usage (EKU) settings.
        self._extended_key_usages: Optional[List[extended_key_usage.ExtendedKeyUsage]] = None
        # SCEP Hash Algorithm.
        self._hash_algorithm: Optional[List[hash_algorithms.HashAlgorithms]] = None
        # Key Size Options.
        self._key_size: Optional[key_size.KeySize] = None
        # Key Storage Provider (KSP) Import Options.
        self._key_storage_provider: Optional[key_storage_provider_option.KeyStorageProviderOption] = None
        # Key Usage Options.
        self._key_usage: Optional[key_usages.KeyUsages] = None
        # Certificate renewal threshold percentage
        self._renewal_threshold_percentage: Optional[int] = None
        # Trusted Root Certificate ID
        self._root_certificate_id: Optional[Guid] = None
        # SCEP Server Url(s).
        self._scep_server_urls: Optional[List[str]] = None
        # Custom AAD Attributes.
        self._subject_alternative_name_formats: Optional[List[windows10_x_custom_subject_alternative_name.Windows10XCustomSubjectAlternativeName]] = None
        # Custom format to use with SubjectNameFormat = Custom. Example: CN={{EmailAddress}},E={{EmailAddress}},OU=Enterprise Users,O=Contoso Corporation,L=Redmond,ST=WA,C=US
        self._subject_name_format_string: Optional[str] = None
    
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
    
    @property
    def extended_key_usages(self,) -> Optional[List[extended_key_usage.ExtendedKeyUsage]]:
        """
        Gets the extendedKeyUsages property value. Extended Key Usage (EKU) settings.
        Returns: Optional[List[extended_key_usage.ExtendedKeyUsage]]
        """
        return self._extended_key_usages
    
    @extended_key_usages.setter
    def extended_key_usages(self,value: Optional[List[extended_key_usage.ExtendedKeyUsage]] = None) -> None:
        """
        Sets the extendedKeyUsages property value. Extended Key Usage (EKU) settings.
        Args:
            value: Value to set for the extendedKeyUsages property.
        """
        self._extended_key_usages = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "certificate_store": lambda n : setattr(self, 'certificate_store', n.get_enum_value(certificate_store.CertificateStore)),
            "certificate_validity_period_scale": lambda n : setattr(self, 'certificate_validity_period_scale', n.get_enum_value(certificate_validity_period_scale.CertificateValidityPeriodScale)),
            "certificate_validity_period_value": lambda n : setattr(self, 'certificate_validity_period_value', n.get_int_value()),
            "extended_key_usages": lambda n : setattr(self, 'extended_key_usages', n.get_collection_of_object_values(extended_key_usage.ExtendedKeyUsage)),
            "hash_algorithm": lambda n : setattr(self, 'hash_algorithm', n.get_collection_of_enum_values(hash_algorithms.HashAlgorithms)),
            "key_size": lambda n : setattr(self, 'key_size', n.get_enum_value(key_size.KeySize)),
            "key_storage_provider": lambda n : setattr(self, 'key_storage_provider', n.get_enum_value(key_storage_provider_option.KeyStorageProviderOption)),
            "key_usage": lambda n : setattr(self, 'key_usage', n.get_enum_value(key_usages.KeyUsages)),
            "renewal_threshold_percentage": lambda n : setattr(self, 'renewal_threshold_percentage', n.get_int_value()),
            "root_certificate_id": lambda n : setattr(self, 'root_certificate_id', n.get_object_value(Guid)),
            "scep_server_urls": lambda n : setattr(self, 'scep_server_urls', n.get_collection_of_primitive_values(str)),
            "subject_alternative_name_formats": lambda n : setattr(self, 'subject_alternative_name_formats', n.get_collection_of_object_values(windows10_x_custom_subject_alternative_name.Windows10XCustomSubjectAlternativeName)),
            "subject_name_format_string": lambda n : setattr(self, 'subject_name_format_string', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def hash_algorithm(self,) -> Optional[List[hash_algorithms.HashAlgorithms]]:
        """
        Gets the hashAlgorithm property value. SCEP Hash Algorithm.
        Returns: Optional[List[hash_algorithms.HashAlgorithms]]
        """
        return self._hash_algorithm
    
    @hash_algorithm.setter
    def hash_algorithm(self,value: Optional[List[hash_algorithms.HashAlgorithms]] = None) -> None:
        """
        Sets the hashAlgorithm property value. SCEP Hash Algorithm.
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
            value: Value to set for the keyStorageProvider property.
        """
        self._key_storage_provider = value
    
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
    def renewal_threshold_percentage(self,) -> Optional[int]:
        """
        Gets the renewalThresholdPercentage property value. Certificate renewal threshold percentage
        Returns: Optional[int]
        """
        return self._renewal_threshold_percentage
    
    @renewal_threshold_percentage.setter
    def renewal_threshold_percentage(self,value: Optional[int] = None) -> None:
        """
        Sets the renewalThresholdPercentage property value. Certificate renewal threshold percentage
        Args:
            value: Value to set for the renewalThresholdPercentage property.
        """
        self._renewal_threshold_percentage = value
    
    @property
    def root_certificate_id(self,) -> Optional[Guid]:
        """
        Gets the rootCertificateId property value. Trusted Root Certificate ID
        Returns: Optional[Guid]
        """
        return self._root_certificate_id
    
    @root_certificate_id.setter
    def root_certificate_id(self,value: Optional[Guid] = None) -> None:
        """
        Sets the rootCertificateId property value. Trusted Root Certificate ID
        Args:
            value: Value to set for the rootCertificateId property.
        """
        self._root_certificate_id = value
    
    @property
    def scep_server_urls(self,) -> Optional[List[str]]:
        """
        Gets the scepServerUrls property value. SCEP Server Url(s).
        Returns: Optional[List[str]]
        """
        return self._scep_server_urls
    
    @scep_server_urls.setter
    def scep_server_urls(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the scepServerUrls property value. SCEP Server Url(s).
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
        writer.write_enum_value("certificateValidityPeriodScale", self.certificate_validity_period_scale)
        writer.write_int_value("certificateValidityPeriodValue", self.certificate_validity_period_value)
        writer.write_collection_of_object_values("extendedKeyUsages", self.extended_key_usages)
        writer.write_enum_value("hashAlgorithm", self.hash_algorithm)
        writer.write_enum_value("keySize", self.key_size)
        writer.write_enum_value("keyStorageProvider", self.key_storage_provider)
        writer.write_enum_value("keyUsage", self.key_usage)
        writer.write_int_value("renewalThresholdPercentage", self.renewal_threshold_percentage)
        writer.write_object_value("rootCertificateId", self.root_certificate_id)
        writer.write_collection_of_primitive_values("scepServerUrls", self.scep_server_urls)
        writer.write_collection_of_object_values("subjectAlternativeNameFormats", self.subject_alternative_name_formats)
        writer.write_str_value("subjectNameFormatString", self.subject_name_format_string)
    
    @property
    def subject_alternative_name_formats(self,) -> Optional[List[windows10_x_custom_subject_alternative_name.Windows10XCustomSubjectAlternativeName]]:
        """
        Gets the subjectAlternativeNameFormats property value. Custom AAD Attributes.
        Returns: Optional[List[windows10_x_custom_subject_alternative_name.Windows10XCustomSubjectAlternativeName]]
        """
        return self._subject_alternative_name_formats
    
    @subject_alternative_name_formats.setter
    def subject_alternative_name_formats(self,value: Optional[List[windows10_x_custom_subject_alternative_name.Windows10XCustomSubjectAlternativeName]] = None) -> None:
        """
        Sets the subjectAlternativeNameFormats property value. Custom AAD Attributes.
        Args:
            value: Value to set for the subjectAlternativeNameFormats property.
        """
        self._subject_alternative_name_formats = value
    
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
    

