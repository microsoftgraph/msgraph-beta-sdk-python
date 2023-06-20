from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import education_identity_matching_options, education_identity_synchronization_configuration

from . import education_identity_synchronization_configuration

@dataclass
class EducationIdentityMatchingConfiguration(education_identity_synchronization_configuration.EducationIdentitySynchronizationConfiguration):
    odata_type = "#microsoft.graph.educationIdentityMatchingConfiguration"
    # Mapping between the user account and the options to use to uniquely identify the user to update.
    matching_options: Optional[List[education_identity_matching_options.EducationIdentityMatchingOptions]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EducationIdentityMatchingConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EducationIdentityMatchingConfiguration
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return EducationIdentityMatchingConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import education_identity_matching_options, education_identity_synchronization_configuration

        from . import education_identity_matching_options, education_identity_synchronization_configuration

        fields: Dict[str, Callable[[Any], None]] = {
            "matchingOptions": lambda n : setattr(self, 'matching_options', n.get_collection_of_object_values(education_identity_matching_options.EducationIdentityMatchingOptions)),
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
        writer.write_collection_of_object_values("matchingOptions", self.matching_options)
    

