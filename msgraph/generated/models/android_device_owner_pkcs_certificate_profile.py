from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

android_device_owner_certificate_access_type = lazy_import('msgraph.generated.models.android_device_owner_certificate_access_type')
android_device_owner_certificate_profile_base = lazy_import('msgraph.generated.models.android_device_owner_certificate_profile_base')
android_device_owner_silent_certificate_access = lazy_import('msgraph.generated.models.android_device_owner_silent_certificate_access')
certificate_store = lazy_import('msgraph.generated.models.certificate_store')
custom_subject_alternative_name = lazy_import('msgraph.generated.models.custom_subject_alternative_name')
device_management_certification_authority = lazy_import('msgraph.generated.models.device_management_certification_authority')
managed_device_certificate_state = lazy_import('msgraph.generated.models.managed_device_certificate_state')

class AndroidDeviceOwnerPkcsCertificateProfile(android_device_owner_certificate_profile_base.AndroidDeviceOwnerCertificateProfileBase):
    @property
    def certificate_access_type(self,) -> Optional[android_device_owner_certificate_access_type.AndroidDeviceOwnerCertificateAccessType]:
        """
        Gets the certificateAccessType property value. Certificate access type. Possible values are: userApproval, specificApps, unknownFutureValue.
        Returns: Optional[android_device_owner_certificate_access_type.AndroidDeviceOwnerCertificateAccessType]
        """
        return self._certificate_access_type
    
    @certificate_access_type.setter
    def certificate_access_type(self,value: Optional[android_device_owner_certificate_access_type.AndroidDeviceOwnerCertificateAccessType] = None) -> None:
        """
        Sets the certificateAccessType property value. Certificate access type. Possible values are: userApproval, specificApps, unknownFutureValue.
        Args:
            value: Value to set for the certificateAccessType property.
        """
        self._certificate_access_type = value
    
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
    
    @property
    def certification_authority_type(self,) -> Optional[device_management_certification_authority.DeviceManagementCertificationAuthority]:
        """
        Gets the certificationAuthorityType property value. Device Management Certification Authority Types.
        Returns: Optional[device_management_certification_authority.DeviceManagementCertificationAuthority]
        """
        return self._certification_authority_type
    
    @certification_authority_type.setter
    def certification_authority_type(self,value: Optional[device_management_certification_authority.DeviceManagementCertificationAuthority] = None) -> None:
        """
        Sets the certificationAuthorityType property value. Device Management Certification Authority Types.
        Args:
            value: Value to set for the certificationAuthorityType property.
        """
        self._certification_authority_type = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new AndroidDeviceOwnerPkcsCertificateProfile and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.androidDeviceOwnerPkcsCertificateProfile"
        # Certificate access type. Possible values are: userApproval, specificApps, unknownFutureValue.
        self._certificate_access_type: Optional[android_device_owner_certificate_access_type.AndroidDeviceOwnerCertificateAccessType] = None
        # CertificateStore types
        self._certificate_store: Optional[certificate_store.CertificateStore] = None
        # PKCS Certificate Template Name
        self._certificate_template_name: Optional[str] = None
        # PKCS Certification Authority
        self._certification_authority: Optional[str] = None
        # PKCS Certification Authority Name
        self._certification_authority_name: Optional[str] = None
        # Device Management Certification Authority Types.
        self._certification_authority_type: Optional[device_management_certification_authority.DeviceManagementCertificationAuthority] = None
        # Custom Subject Alternative Name Settings. This collection can contain a maximum of 500 elements.
        self._custom_subject_alternative_names: Optional[List[custom_subject_alternative_name.CustomSubjectAlternativeName]] = None
        # Certificate state for devices. This collection can contain a maximum of 2147483647 elements.
        self._managed_device_certificate_states: Optional[List[managed_device_certificate_state.ManagedDeviceCertificateState]] = None
        # Certificate access information. This collection can contain a maximum of 50 elements.
        self._silent_certificate_access_details: Optional[List[android_device_owner_silent_certificate_access.AndroidDeviceOwnerSilentCertificateAccess]] = None
        # Custom String that defines the AAD Attribute.
        self._subject_alternative_name_format_string: Optional[str] = None
        # Custom format to use with SubjectNameFormat = Custom. Example: CN={{EmailAddress}},E={{EmailAddress}},OU=Enterprise Users,O=Contoso Corporation,L=Redmond,ST=WA,C=US
        self._subject_name_format_string: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AndroidDeviceOwnerPkcsCertificateProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AndroidDeviceOwnerPkcsCertificateProfile
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AndroidDeviceOwnerPkcsCertificateProfile()
    
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
            "certificate_access_type": lambda n : setattr(self, 'certificate_access_type', n.get_enum_value(android_device_owner_certificate_access_type.AndroidDeviceOwnerCertificateAccessType)),
            "certificate_store": lambda n : setattr(self, 'certificate_store', n.get_enum_value(certificate_store.CertificateStore)),
            "certificate_template_name": lambda n : setattr(self, 'certificate_template_name', n.get_str_value()),
            "certification_authority": lambda n : setattr(self, 'certification_authority', n.get_str_value()),
            "certification_authority_name": lambda n : setattr(self, 'certification_authority_name', n.get_str_value()),
            "certification_authority_type": lambda n : setattr(self, 'certification_authority_type', n.get_enum_value(device_management_certification_authority.DeviceManagementCertificationAuthority)),
            "custom_subject_alternative_names": lambda n : setattr(self, 'custom_subject_alternative_names', n.get_collection_of_object_values(custom_subject_alternative_name.CustomSubjectAlternativeName)),
            "managed_device_certificate_states": lambda n : setattr(self, 'managed_device_certificate_states', n.get_collection_of_object_values(managed_device_certificate_state.ManagedDeviceCertificateState)),
            "silent_certificate_access_details": lambda n : setattr(self, 'silent_certificate_access_details', n.get_collection_of_object_values(android_device_owner_silent_certificate_access.AndroidDeviceOwnerSilentCertificateAccess)),
            "subject_alternative_name_format_string": lambda n : setattr(self, 'subject_alternative_name_format_string', n.get_str_value()),
            "subject_name_format_string": lambda n : setattr(self, 'subject_name_format_string', n.get_str_value()),
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
        writer.write_enum_value("certificateAccessType", self.certificate_access_type)
        writer.write_enum_value("certificateStore", self.certificate_store)
        writer.write_str_value("certificateTemplateName", self.certificate_template_name)
        writer.write_str_value("certificationAuthority", self.certification_authority)
        writer.write_str_value("certificationAuthorityName", self.certification_authority_name)
        writer.write_enum_value("certificationAuthorityType", self.certification_authority_type)
        writer.write_collection_of_object_values("customSubjectAlternativeNames", self.custom_subject_alternative_names)
        writer.write_collection_of_object_values("managedDeviceCertificateStates", self.managed_device_certificate_states)
        writer.write_collection_of_object_values("silentCertificateAccessDetails", self.silent_certificate_access_details)
        writer.write_str_value("subjectAlternativeNameFormatString", self.subject_alternative_name_format_string)
        writer.write_str_value("subjectNameFormatString", self.subject_name_format_string)
    
    @property
    def silent_certificate_access_details(self,) -> Optional[List[android_device_owner_silent_certificate_access.AndroidDeviceOwnerSilentCertificateAccess]]:
        """
        Gets the silentCertificateAccessDetails property value. Certificate access information. This collection can contain a maximum of 50 elements.
        Returns: Optional[List[android_device_owner_silent_certificate_access.AndroidDeviceOwnerSilentCertificateAccess]]
        """
        return self._silent_certificate_access_details
    
    @silent_certificate_access_details.setter
    def silent_certificate_access_details(self,value: Optional[List[android_device_owner_silent_certificate_access.AndroidDeviceOwnerSilentCertificateAccess]] = None) -> None:
        """
        Sets the silentCertificateAccessDetails property value. Certificate access information. This collection can contain a maximum of 50 elements.
        Args:
            value: Value to set for the silentCertificateAccessDetails property.
        """
        self._silent_certificate_access_details = value
    
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
    

