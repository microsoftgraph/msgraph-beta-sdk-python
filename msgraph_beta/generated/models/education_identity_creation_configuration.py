from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .education_identity_domain import EducationIdentityDomain
    from .education_identity_synchronization_configuration import EducationIdentitySynchronizationConfiguration

from .education_identity_synchronization_configuration import EducationIdentitySynchronizationConfiguration

@dataclass
class EducationIdentityCreationConfiguration(EducationIdentitySynchronizationConfiguration):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.educationIdentityCreationConfiguration"
    # The userDomains property
    user_domains: Optional[List[EducationIdentityDomain]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EducationIdentityCreationConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EducationIdentityCreationConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EducationIdentityCreationConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .education_identity_domain import EducationIdentityDomain
        from .education_identity_synchronization_configuration import EducationIdentitySynchronizationConfiguration

        from .education_identity_domain import EducationIdentityDomain
        from .education_identity_synchronization_configuration import EducationIdentitySynchronizationConfiguration

        fields: Dict[str, Callable[[Any], None]] = {
            "userDomains": lambda n : setattr(self, 'user_domains', n.get_collection_of_object_values(EducationIdentityDomain)),
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
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("userDomains", self.user_domains)
    

