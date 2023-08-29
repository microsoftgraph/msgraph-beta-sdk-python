from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .custom_subject_alternative_name import CustomSubjectAlternativeName
    from .extended_key_usage import ExtendedKeyUsage
    from .windows81_s_c_e_p_certificate_profile import Windows81SCEPCertificateProfile
    from .windows_certificate_profile_base import WindowsCertificateProfileBase

from .windows_certificate_profile_base import WindowsCertificateProfileBase

@dataclass
class Windows81CertificateProfileBase(WindowsCertificateProfileBase):
    """
    Device Configuration.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.windows81CertificateProfileBase"
    # Custom Subject Alternative Name Settings. This collection can contain a maximum of 500 elements.
    custom_subject_alternative_names: Optional[List[CustomSubjectAlternativeName]] = None
    # Extended Key Usage (EKU) settings. This collection can contain a maximum of 500 elements.
    extended_key_usages: Optional[List[ExtendedKeyUsage]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Windows81CertificateProfileBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Windows81CertificateProfileBase
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows81SCEPCertificateProfile".casefold():
            from .windows81_s_c_e_p_certificate_profile import Windows81SCEPCertificateProfile

            return Windows81SCEPCertificateProfile()
        return Windows81CertificateProfileBase()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .custom_subject_alternative_name import CustomSubjectAlternativeName
        from .extended_key_usage import ExtendedKeyUsage
        from .windows81_s_c_e_p_certificate_profile import Windows81SCEPCertificateProfile
        from .windows_certificate_profile_base import WindowsCertificateProfileBase

        from .custom_subject_alternative_name import CustomSubjectAlternativeName
        from .extended_key_usage import ExtendedKeyUsage
        from .windows81_s_c_e_p_certificate_profile import Windows81SCEPCertificateProfile
        from .windows_certificate_profile_base import WindowsCertificateProfileBase

        fields: Dict[str, Callable[[Any], None]] = {
            "customSubjectAlternativeNames": lambda n : setattr(self, 'custom_subject_alternative_names', n.get_collection_of_object_values(CustomSubjectAlternativeName)),
            "extendedKeyUsages": lambda n : setattr(self, 'extended_key_usages', n.get_collection_of_object_values(ExtendedKeyUsage)),
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
        writer.write_collection_of_object_values("customSubjectAlternativeNames", self.custom_subject_alternative_names)
        writer.write_collection_of_object_values("extendedKeyUsages", self.extended_key_usages)
    

