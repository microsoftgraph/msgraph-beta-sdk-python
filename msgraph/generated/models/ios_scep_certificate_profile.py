from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import certificate_store, custom_subject_alternative_name, extended_key_usage, ios_certificate_profile_base, ios_trusted_root_certificate, key_size, key_usages, managed_device_certificate_state

from . import ios_certificate_profile_base

class IosScepCertificateProfile(ios_certificate_profile_base.IosCertificateProfileBase):
    def __init__(self,) -> None:
        """
        Instantiates a new IosScepCertificateProfile and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.iosScepCertificateProfile"
        # Target store certificate. Possible values are: user, machine.
        self._certificate_store: Optional[certificate_store.CertificateStore] = None
        # Custom Subject Alternative Name Settings. The OnPremisesUserPrincipalName variable is support as well as others documented here: https://go.microsoft.com/fwlink/?LinkId=2027630. This collection can contain a maximum of 500 elements.
        self._custom_subject_alternative_names: Optional[List[custom_subject_alternative_name.CustomSubjectAlternativeName]] = None
        # Extended Key Usage (EKU) settings. This collection can contain a maximum of 500 elements.
        self._extended_key_usages: Optional[List[extended_key_usage.ExtendedKeyUsage]] = None
        # Key Size Options.
        self._key_size: Optional[key_size.KeySize] = None
        # Key Usage Options.
        self._key_usage: Optional[key_usages.KeyUsages] = None
        # Certificate state for devices. This collection can contain a maximum of 2147483647 elements.
        self._managed_device_certificate_states: Optional[List[managed_device_certificate_state.ManagedDeviceCertificateState]] = None
        # Trusted Root Certificate.
        self._root_certificate: Optional[ios_trusted_root_certificate.IosTrustedRootCertificate] = None
        # SCEP Server Url(s).
        self._scep_server_urls: Optional[List[str]] = None
        # Custom String that defines the AAD Attribute.
        self._subject_alternative_name_format_string: Optional[str] = None
        # Custom format to use with SubjectNameFormat = Custom. Example: CN={{EmailAddress}},E={{EmailAddress}},OU=Enterprise Users,O=Contoso Corporation,L=Redmond,ST=WA,C=US
        self._subject_name_format_string: Optional[str] = None
    
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
            value: Value to set for the certificate_store property.
        """
        self._certificate_store = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IosScepCertificateProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IosScepCertificateProfile
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return IosScepCertificateProfile()
    
    @property
    def custom_subject_alternative_names(self,) -> Optional[List[custom_subject_alternative_name.CustomSubjectAlternativeName]]:
        """
        Gets the customSubjectAlternativeNames property value. Custom Subject Alternative Name Settings. The OnPremisesUserPrincipalName variable is support as well as others documented here: https://go.microsoft.com/fwlink/?LinkId=2027630. This collection can contain a maximum of 500 elements.
        Returns: Optional[List[custom_subject_alternative_name.CustomSubjectAlternativeName]]
        """
        return self._custom_subject_alternative_names
    
    @custom_subject_alternative_names.setter
    def custom_subject_alternative_names(self,value: Optional[List[custom_subject_alternative_name.CustomSubjectAlternativeName]] = None) -> None:
        """
        Sets the customSubjectAlternativeNames property value. Custom Subject Alternative Name Settings. The OnPremisesUserPrincipalName variable is support as well as others documented here: https://go.microsoft.com/fwlink/?LinkId=2027630. This collection can contain a maximum of 500 elements.
        Args:
            value: Value to set for the custom_subject_alternative_names property.
        """
        self._custom_subject_alternative_names = value
    
    @property
    def extended_key_usages(self,) -> Optional[List[extended_key_usage.ExtendedKeyUsage]]:
        """
        Gets the extendedKeyUsages property value. Extended Key Usage (EKU) settings. This collection can contain a maximum of 500 elements.
        Returns: Optional[List[extended_key_usage.ExtendedKeyUsage]]
        """
        return self._extended_key_usages
    
    @extended_key_usages.setter
    def extended_key_usages(self,value: Optional[List[extended_key_usage.ExtendedKeyUsage]] = None) -> None:
        """
        Sets the extendedKeyUsages property value. Extended Key Usage (EKU) settings. This collection can contain a maximum of 500 elements.
        Args:
            value: Value to set for the extended_key_usages property.
        """
        self._extended_key_usages = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
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
            value: Value to set for the key_size property.
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
            value: Value to set for the key_usage property.
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
            value: Value to set for the managed_device_certificate_states property.
        """
        self._managed_device_certificate_states = value
    
    @property
    def root_certificate(self,) -> Optional[ios_trusted_root_certificate.IosTrustedRootCertificate]:
        """
        Gets the rootCertificate property value. Trusted Root Certificate.
        Returns: Optional[ios_trusted_root_certificate.IosTrustedRootCertificate]
        """
        return self._root_certificate
    
    @root_certificate.setter
    def root_certificate(self,value: Optional[ios_trusted_root_certificate.IosTrustedRootCertificate] = None) -> None:
        """
        Sets the rootCertificate property value. Trusted Root Certificate.
        Args:
            value: Value to set for the root_certificate property.
        """
        self._root_certificate = value
    
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
            value: Value to set for the scep_server_urls property.
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
        writer.write_collection_of_object_values("extendedKeyUsages", self.extended_key_usages)
        writer.write_enum_value("keySize", self.key_size)
        writer.write_enum_value("keyUsage", self.key_usage)
        writer.write_collection_of_object_values("managedDeviceCertificateStates", self.managed_device_certificate_states)
        writer.write_object_value("rootCertificate", self.root_certificate)
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
            value: Value to set for the subject_alternative_name_format_string property.
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
            value: Value to set for the subject_name_format_string property.
        """
        self._subject_name_format_string = value
    

