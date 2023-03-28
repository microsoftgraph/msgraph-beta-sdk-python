from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import certificate_store, custom_subject_alternative_name, extended_key_usage, managed_device_certificate_state, windows10_certificate_profile_base

from . import windows10_certificate_profile_base

class Windows10PkcsCertificateProfile(windows10_certificate_profile_base.Windows10CertificateProfileBase):
    def __init__(self,) -> None:
        """
        Instantiates a new Windows10PkcsCertificateProfile and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windows10PkcsCertificateProfile"
        # Target store certificate. Possible values are: user, machine.
        self._certificate_store: Optional[certificate_store.CertificateStore] = None
        # PKCS Certificate Template Name
        self._certificate_template_name: Optional[str] = None
        # PKCS Certification Authority
        self._certification_authority: Optional[str] = None
        # PKCS Certification Authority Name
        self._certification_authority_name: Optional[str] = None
        # Custom Subject Alternative Name Settings. This collection can contain a maximum of 500 elements.
        self._custom_subject_alternative_names: Optional[List[custom_subject_alternative_name.CustomSubjectAlternativeName]] = None
        # Extended Key Usage (EKU) settings. This collection can contain a maximum of 500 elements.
        self._extended_key_usages: Optional[List[extended_key_usage.ExtendedKeyUsage]] = None
        # Certificate state for devices. This collection can contain a maximum of 2147483647 elements.
        self._managed_device_certificate_states: Optional[List[managed_device_certificate_state.ManagedDeviceCertificateState]] = None
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
    
    @property
    def certificate_template_name(self,) -> Optional[str]:
        """
        Gets the certificateTemplateName property value. PKCS Certificate Template Name
        Returns: Optional[str]
        """
        return self._certificate_template_name
    
    @certificate_template_name.setter
    def certificate_template_name(self,value: Optional[str] = None) -> None:
        """
        Sets the certificateTemplateName property value. PKCS Certificate Template Name
        Args:
            value: Value to set for the certificate_template_name property.
        """
        self._certificate_template_name = value
    
    @property
    def certification_authority(self,) -> Optional[str]:
        """
        Gets the certificationAuthority property value. PKCS Certification Authority
        Returns: Optional[str]
        """
        return self._certification_authority
    
    @certification_authority.setter
    def certification_authority(self,value: Optional[str] = None) -> None:
        """
        Sets the certificationAuthority property value. PKCS Certification Authority
        Args:
            value: Value to set for the certification_authority property.
        """
        self._certification_authority = value
    
    @property
    def certification_authority_name(self,) -> Optional[str]:
        """
        Gets the certificationAuthorityName property value. PKCS Certification Authority Name
        Returns: Optional[str]
        """
        return self._certification_authority_name
    
    @certification_authority_name.setter
    def certification_authority_name(self,value: Optional[str] = None) -> None:
        """
        Sets the certificationAuthorityName property value. PKCS Certification Authority Name
        Args:
            value: Value to set for the certification_authority_name property.
        """
        self._certification_authority_name = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Windows10PkcsCertificateProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Windows10PkcsCertificateProfile
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Windows10PkcsCertificateProfile()
    
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
        from . import certificate_store, custom_subject_alternative_name, extended_key_usage, managed_device_certificate_state, windows10_certificate_profile_base

        fields: Dict[str, Callable[[Any], None]] = {
            "certificateStore": lambda n : setattr(self, 'certificate_store', n.get_enum_value(certificate_store.CertificateStore)),
            "certificateTemplateName": lambda n : setattr(self, 'certificate_template_name', n.get_str_value()),
            "certificationAuthority": lambda n : setattr(self, 'certification_authority', n.get_str_value()),
            "certificationAuthorityName": lambda n : setattr(self, 'certification_authority_name', n.get_str_value()),
            "customSubjectAlternativeNames": lambda n : setattr(self, 'custom_subject_alternative_names', n.get_collection_of_object_values(custom_subject_alternative_name.CustomSubjectAlternativeName)),
            "extendedKeyUsages": lambda n : setattr(self, 'extended_key_usages', n.get_collection_of_object_values(extended_key_usage.ExtendedKeyUsage)),
            "managedDeviceCertificateStates": lambda n : setattr(self, 'managed_device_certificate_states', n.get_collection_of_object_values(managed_device_certificate_state.ManagedDeviceCertificateState)),
            "subjectAlternativeNameFormatString": lambda n : setattr(self, 'subject_alternative_name_format_string', n.get_str_value()),
            "subjectNameFormatString": lambda n : setattr(self, 'subject_name_format_string', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
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
        writer.write_str_value("certificateTemplateName", self.certificate_template_name)
        writer.write_str_value("certificationAuthority", self.certification_authority)
        writer.write_str_value("certificationAuthorityName", self.certification_authority_name)
        writer.write_collection_of_object_values("customSubjectAlternativeNames", self.custom_subject_alternative_names)
        writer.write_collection_of_object_values("extendedKeyUsages", self.extended_key_usages)
        writer.write_collection_of_object_values("managedDeviceCertificateStates", self.managed_device_certificate_states)
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
    

