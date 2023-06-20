from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import certificate_store, custom_subject_alternative_name, mac_o_s_certificate_profile_base, managed_device_certificate_state

from . import mac_o_s_certificate_profile_base

@dataclass
class MacOSPkcsCertificateProfile(mac_o_s_certificate_profile_base.MacOSCertificateProfileBase):
    odata_type = "#microsoft.graph.macOSPkcsCertificateProfile"
    # AllowAllAppsAccess setting
    allow_all_apps_access: Optional[bool] = None
    # Target store certificate. Possible values are: user, machine.
    certificate_store: Optional[certificate_store.CertificateStore] = None
    # PKCS certificate template name.
    certificate_template_name: Optional[str] = None
    # PKCS certification authority FQDN.
    certification_authority: Optional[str] = None
    # PKCS certification authority Name.
    certification_authority_name: Optional[str] = None
    # Custom Subject Alternative Name Settings. This collection can contain a maximum of 500 elements.
    custom_subject_alternative_names: Optional[List[custom_subject_alternative_name.CustomSubjectAlternativeName]] = None
    # Certificate state for devices. This collection can contain a maximum of 2147483647 elements.
    managed_device_certificate_states: Optional[List[managed_device_certificate_state.ManagedDeviceCertificateState]] = None
    # Format string that defines the subject alternative name.
    subject_alternative_name_format_string: Optional[str] = None
    # Format string that defines the subject name. Example: CN={{EmailAddress}},E={{EmailAddress}},OU=Enterprise Users,O=Contoso Corporation,L=Redmond,ST=WA,C=US
    subject_name_format_string: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MacOSPkcsCertificateProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MacOSPkcsCertificateProfile
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return MacOSPkcsCertificateProfile()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import certificate_store, custom_subject_alternative_name, mac_o_s_certificate_profile_base, managed_device_certificate_state

        from . import certificate_store, custom_subject_alternative_name, mac_o_s_certificate_profile_base, managed_device_certificate_state

        fields: Dict[str, Callable[[Any], None]] = {
            "allowAllAppsAccess": lambda n : setattr(self, 'allow_all_apps_access', n.get_bool_value()),
            "certificateStore": lambda n : setattr(self, 'certificate_store', n.get_enum_value(certificate_store.CertificateStore)),
            "certificateTemplateName": lambda n : setattr(self, 'certificate_template_name', n.get_str_value()),
            "certificationAuthority": lambda n : setattr(self, 'certification_authority', n.get_str_value()),
            "certificationAuthorityName": lambda n : setattr(self, 'certification_authority_name', n.get_str_value()),
            "customSubjectAlternativeNames": lambda n : setattr(self, 'custom_subject_alternative_names', n.get_collection_of_object_values(custom_subject_alternative_name.CustomSubjectAlternativeName)),
            "managedDeviceCertificateStates": lambda n : setattr(self, 'managed_device_certificate_states', n.get_collection_of_object_values(managed_device_certificate_state.ManagedDeviceCertificateState)),
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
        writer.write_bool_value("allowAllAppsAccess", self.allow_all_apps_access)
        writer.write_enum_value("certificateStore", self.certificate_store)
        writer.write_str_value("certificateTemplateName", self.certificate_template_name)
        writer.write_str_value("certificationAuthority", self.certification_authority)
        writer.write_str_value("certificationAuthorityName", self.certification_authority_name)
        writer.write_collection_of_object_values("customSubjectAlternativeNames", self.custom_subject_alternative_names)
        writer.write_collection_of_object_values("managedDeviceCertificateStates", self.managed_device_certificate_states)
        writer.write_str_value("subjectAlternativeNameFormatString", self.subject_alternative_name_format_string)
        writer.write_str_value("subjectNameFormatString", self.subject_name_format_string)
    

