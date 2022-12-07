from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

education_identity_matching_options = lazy_import('msgraph.generated.models.education_identity_matching_options')
education_identity_synchronization_configuration = lazy_import('msgraph.generated.models.education_identity_synchronization_configuration')

class EducationIdentityMatchingConfiguration(education_identity_synchronization_configuration.EducationIdentitySynchronizationConfiguration):
    def __init__(self,) -> None:
        """
        Instantiates a new EducationIdentityMatchingConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.educationIdentityMatchingConfiguration"
        # Mapping between the user account and the options to use to uniquely identify the user to update.
        self._matching_options: Optional[List[education_identity_matching_options.EducationIdentityMatchingOptions]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EducationIdentityMatchingConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EducationIdentityMatchingConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EducationIdentityMatchingConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "matching_options": lambda n : setattr(self, 'matching_options', n.get_collection_of_object_values(education_identity_matching_options.EducationIdentityMatchingOptions)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def matching_options(self,) -> Optional[List[education_identity_matching_options.EducationIdentityMatchingOptions]]:
        """
        Gets the matchingOptions property value. Mapping between the user account and the options to use to uniquely identify the user to update.
        Returns: Optional[List[education_identity_matching_options.EducationIdentityMatchingOptions]]
        """
        return self._matching_options
    
    @matching_options.setter
    def matching_options(self,value: Optional[List[education_identity_matching_options.EducationIdentityMatchingOptions]] = None) -> None:
        """
        Sets the matchingOptions property value. Mapping between the user account and the options to use to uniquely identify the user to update.
        Args:
            value: Value to set for the matchingOptions property.
        """
        self._matching_options = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("matchingOptions", self.matching_options)
    

