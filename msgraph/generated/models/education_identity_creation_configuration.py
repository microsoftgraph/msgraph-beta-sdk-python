from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

education_identity_domain = lazy_import('msgraph.generated.models.education_identity_domain')
education_identity_synchronization_configuration = lazy_import('msgraph.generated.models.education_identity_synchronization_configuration')

class EducationIdentityCreationConfiguration(education_identity_synchronization_configuration.EducationIdentitySynchronizationConfiguration):
    def __init__(self,) -> None:
        """
        Instantiates a new EducationIdentityCreationConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.educationIdentityCreationConfiguration"
        # The userDomains property
        self._user_domains: Optional[List[education_identity_domain.EducationIdentityDomain]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EducationIdentityCreationConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EducationIdentityCreationConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EducationIdentityCreationConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "user_domains": lambda n : setattr(self, 'user_domains', n.get_collection_of_object_values(education_identity_domain.EducationIdentityDomain)),
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
        writer.write_collection_of_object_values("userDomains", self.user_domains)
    
    @property
    def user_domains(self,) -> Optional[List[education_identity_domain.EducationIdentityDomain]]:
        """
        Gets the userDomains property value. The userDomains property
        Returns: Optional[List[education_identity_domain.EducationIdentityDomain]]
        """
        return self._user_domains
    
    @user_domains.setter
    def user_domains(self,value: Optional[List[education_identity_domain.EducationIdentityDomain]] = None) -> None:
        """
        Sets the userDomains property value. The userDomains property
        Args:
            value: Value to set for the userDomains property.
        """
        self._user_domains = value
    

