from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

android_for_work_certificate_profile_base = lazy_import('msgraph.generated.models.android_for_work_certificate_profile_base')
managed_device_certificate_state = lazy_import('msgraph.generated.models.managed_device_certificate_state')

class AndroidForWorkPkcsCertificateProfile(android_for_work_certificate_profile_base.AndroidForWorkCertificateProfileBase):
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
            value: Value to set for the certificateTemplateName property.
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
            value: Value to set for the certificationAuthority property.
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
            value: Value to set for the certificationAuthorityName property.
        """
        self._certification_authority_name = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new AndroidForWorkPkcsCertificateProfile and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.androidForWorkPkcsCertificateProfile"
        # PKCS Certificate Template Name
        self._certificate_template_name: Optional[str] = None
        # PKCS Certification Authority
        self._certification_authority: Optional[str] = None
        # PKCS Certification Authority Name
        self._certification_authority_name: Optional[str] = None
        # Certificate state for devices. This collection can contain a maximum of 2147483647 elements.
        self._managed_device_certificate_states: Optional[List[managed_device_certificate_state.ManagedDeviceCertificateState]] = None
        # Custom String that defines the AAD Attribute.
        self._subject_alternative_name_format_string: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AndroidForWorkPkcsCertificateProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AndroidForWorkPkcsCertificateProfile
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AndroidForWorkPkcsCertificateProfile()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "certificate_template_name": lambda n : setattr(self, 'certificate_template_name', n.get_str_value()),
            "certification_authority": lambda n : setattr(self, 'certification_authority', n.get_str_value()),
            "certification_authority_name": lambda n : setattr(self, 'certification_authority_name', n.get_str_value()),
            "managed_device_certificate_states": lambda n : setattr(self, 'managed_device_certificate_states', n.get_collection_of_object_values(managed_device_certificate_state.ManagedDeviceCertificateState)),
            "subject_alternative_name_format_string": lambda n : setattr(self, 'subject_alternative_name_format_string', n.get_str_value()),
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
            value: Value to set for the managedDeviceCertificateStates property.
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
        writer.write_str_value("certificateTemplateName", self.certificate_template_name)
        writer.write_str_value("certificationAuthority", self.certification_authority)
        writer.write_str_value("certificationAuthorityName", self.certification_authority_name)
        writer.write_collection_of_object_values("managedDeviceCertificateStates", self.managed_device_certificate_states)
        writer.write_str_value("subjectAlternativeNameFormatString", self.subject_alternative_name_format_string)
    
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
    

