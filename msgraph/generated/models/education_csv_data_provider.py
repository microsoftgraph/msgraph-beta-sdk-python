from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

education_synchronization_customizations = lazy_import('msgraph.generated.models.education_synchronization_customizations')
education_synchronization_data_provider = lazy_import('msgraph.generated.models.education_synchronization_data_provider')

class EducationCsvDataProvider(education_synchronization_data_provider.EducationSynchronizationDataProvider):
    def __init__(self,) -> None:
        """
        Instantiates a new EducationCsvDataProvider and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.educationCsvDataProvider"
        # Optional customizations to be applied to the synchronization profile.
        self._customizations: Optional[education_synchronization_customizations.EducationSynchronizationCustomizations] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EducationCsvDataProvider:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EducationCsvDataProvider
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EducationCsvDataProvider()
    
    @property
    def customizations(self,) -> Optional[education_synchronization_customizations.EducationSynchronizationCustomizations]:
        """
        Gets the customizations property value. Optional customizations to be applied to the synchronization profile.
        Returns: Optional[education_synchronization_customizations.EducationSynchronizationCustomizations]
        """
        return self._customizations
    
    @customizations.setter
    def customizations(self,value: Optional[education_synchronization_customizations.EducationSynchronizationCustomizations] = None) -> None:
        """
        Sets the customizations property value. Optional customizations to be applied to the synchronization profile.
        Args:
            value: Value to set for the customizations property.
        """
        self._customizations = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "customizations": lambda n : setattr(self, 'customizations', n.get_object_value(education_synchronization_customizations.EducationSynchronizationCustomizations)),
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
        writer.write_object_value("customizations", self.customizations)
    

