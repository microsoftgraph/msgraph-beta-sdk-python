from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

custom_subject_alternative_name = lazy_import('msgraph.generated.models.custom_subject_alternative_name')
extended_key_usage = lazy_import('msgraph.generated.models.extended_key_usage')
windows_certificate_profile_base = lazy_import('msgraph.generated.models.windows_certificate_profile_base')

class Windows81CertificateProfileBase(windows_certificate_profile_base.WindowsCertificateProfileBase):
    def __init__(self,) -> None:
        """
        Instantiates a new Windows81CertificateProfileBase and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windows81CertificateProfileBase"
        # Custom Subject Alternative Name Settings. This collection can contain a maximum of 500 elements.
        self._custom_subject_alternative_names: Optional[List[custom_subject_alternative_name.CustomSubjectAlternativeName]] = None
        # Extended Key Usage (EKU) settings. This collection can contain a maximum of 500 elements.
        self._extended_key_usages: Optional[List[extended_key_usage.ExtendedKeyUsage]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Windows81CertificateProfileBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Windows81CertificateProfileBase
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Windows81CertificateProfileBase()
    
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
            value: Value to set for the extendedKeyUsages property.
        """
        self._extended_key_usages = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "custom_subject_alternative_names": lambda n : setattr(self, 'custom_subject_alternative_names', n.get_collection_of_object_values(custom_subject_alternative_name.CustomSubjectAlternativeName)),
            "extended_key_usages": lambda n : setattr(self, 'extended_key_usages', n.get_collection_of_object_values(extended_key_usage.ExtendedKeyUsage)),
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
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("customSubjectAlternativeNames", self.custom_subject_alternative_names)
        writer.write_collection_of_object_values("extendedKeyUsages", self.extended_key_usages)
    

