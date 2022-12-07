from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

education_synchronization_connection_settings = lazy_import('msgraph.generated.models.education_synchronization_connection_settings')
education_synchronization_customizations = lazy_import('msgraph.generated.models.education_synchronization_customizations')
education_synchronization_data_provider = lazy_import('msgraph.generated.models.education_synchronization_data_provider')

class EducationOneRosterApiDataProvider(education_synchronization_data_provider.EducationSynchronizationDataProvider):
    @property
    def connection_settings(self,) -> Optional[education_synchronization_connection_settings.EducationSynchronizationConnectionSettings]:
        """
        Gets the connectionSettings property value. The connectionSettings property
        Returns: Optional[education_synchronization_connection_settings.EducationSynchronizationConnectionSettings]
        """
        return self._connection_settings
    
    @connection_settings.setter
    def connection_settings(self,value: Optional[education_synchronization_connection_settings.EducationSynchronizationConnectionSettings] = None) -> None:
        """
        Sets the connectionSettings property value. The connectionSettings property
        Args:
            value: Value to set for the connectionSettings property.
        """
        self._connection_settings = value
    
    @property
    def connection_url(self,) -> Optional[str]:
        """
        Gets the connectionUrl property value. The connectionUrl property
        Returns: Optional[str]
        """
        return self._connection_url
    
    @connection_url.setter
    def connection_url(self,value: Optional[str] = None) -> None:
        """
        Sets the connectionUrl property value. The connectionUrl property
        Args:
            value: Value to set for the connectionUrl property.
        """
        self._connection_url = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new EducationOneRosterApiDataProvider and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.educationOneRosterApiDataProvider"
        # The connectionSettings property
        self._connection_settings: Optional[education_synchronization_connection_settings.EducationSynchronizationConnectionSettings] = None
        # The connectionUrl property
        self._connection_url: Optional[str] = None
        # The customizations property
        self._customizations: Optional[education_synchronization_customizations.EducationSynchronizationCustomizations] = None
        # The providerName property
        self._provider_name: Optional[str] = None
        # The schoolsIds property
        self._schools_ids: Optional[List[str]] = None
        # The termIds property
        self._term_ids: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EducationOneRosterApiDataProvider:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EducationOneRosterApiDataProvider
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EducationOneRosterApiDataProvider()
    
    @property
    def customizations(self,) -> Optional[education_synchronization_customizations.EducationSynchronizationCustomizations]:
        """
        Gets the customizations property value. The customizations property
        Returns: Optional[education_synchronization_customizations.EducationSynchronizationCustomizations]
        """
        return self._customizations
    
    @customizations.setter
    def customizations(self,value: Optional[education_synchronization_customizations.EducationSynchronizationCustomizations] = None) -> None:
        """
        Sets the customizations property value. The customizations property
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
            "connection_settings": lambda n : setattr(self, 'connection_settings', n.get_object_value(education_synchronization_connection_settings.EducationSynchronizationConnectionSettings)),
            "connection_url": lambda n : setattr(self, 'connection_url', n.get_str_value()),
            "customizations": lambda n : setattr(self, 'customizations', n.get_object_value(education_synchronization_customizations.EducationSynchronizationCustomizations)),
            "provider_name": lambda n : setattr(self, 'provider_name', n.get_str_value()),
            "schools_ids": lambda n : setattr(self, 'schools_ids', n.get_collection_of_primitive_values(str)),
            "term_ids": lambda n : setattr(self, 'term_ids', n.get_collection_of_primitive_values(str)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def provider_name(self,) -> Optional[str]:
        """
        Gets the providerName property value. The providerName property
        Returns: Optional[str]
        """
        return self._provider_name
    
    @provider_name.setter
    def provider_name(self,value: Optional[str] = None) -> None:
        """
        Sets the providerName property value. The providerName property
        Args:
            value: Value to set for the providerName property.
        """
        self._provider_name = value
    
    @property
    def schools_ids(self,) -> Optional[List[str]]:
        """
        Gets the schoolsIds property value. The schoolsIds property
        Returns: Optional[List[str]]
        """
        return self._schools_ids
    
    @schools_ids.setter
    def schools_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the schoolsIds property value. The schoolsIds property
        Args:
            value: Value to set for the schoolsIds property.
        """
        self._schools_ids = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("connectionSettings", self.connection_settings)
        writer.write_str_value("connectionUrl", self.connection_url)
        writer.write_object_value("customizations", self.customizations)
        writer.write_str_value("providerName", self.provider_name)
        writer.write_collection_of_primitive_values("schoolsIds", self.schools_ids)
        writer.write_collection_of_primitive_values("termIds", self.term_ids)
    
    @property
    def term_ids(self,) -> Optional[List[str]]:
        """
        Gets the termIds property value. The termIds property
        Returns: Optional[List[str]]
        """
        return self._term_ids
    
    @term_ids.setter
    def term_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the termIds property value. The termIds property
        Args:
            value: Value to set for the termIds property.
        """
        self._term_ids = value
    

