from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import education_identity_domain, education_identity_synchronization_configuration

from . import education_identity_synchronization_configuration

@dataclass
class EducationIdentityCreationConfiguration(education_identity_synchronization_configuration.EducationIdentitySynchronizationConfiguration):
    odata_type = "#microsoft.graph.educationIdentityCreationConfiguration"
    # The userDomains property
    user_domains: Optional[List[education_identity_domain.EducationIdentityDomain]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EducationIdentityCreationConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EducationIdentityCreationConfiguration
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return EducationIdentityCreationConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import education_identity_domain, education_identity_synchronization_configuration

        from . import education_identity_domain, education_identity_synchronization_configuration

        fields: Dict[str, Callable[[Any], None]] = {
            "userDomains": lambda n : setattr(self, 'user_domains', n.get_collection_of_object_values(education_identity_domain.EducationIdentityDomain)),
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
        writer.write_collection_of_object_values("userDomains", self.user_domains)
    

