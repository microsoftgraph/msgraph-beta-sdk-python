from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
synchronization_job = lazy_import('msgraph.generated.models.synchronization_job')
synchronization_secret_key_string_value_pair = lazy_import('msgraph.generated.models.synchronization_secret_key_string_value_pair')
synchronization_template = lazy_import('msgraph.generated.models.synchronization_template')

class Synchronization(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new synchronization and sets the default values.
        """
        super().__init__()
        # Performs synchronization by periodically running in the background, polling for changes in one directory, and pushing them to another directory.
        self._jobs: Optional[List[synchronization_job.SynchronizationJob]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Represents a collection of credentials to access provisioned cloud applications.
        self._secrets: Optional[List[synchronization_secret_key_string_value_pair.SynchronizationSecretKeyStringValuePair]] = None
        # Pre-configured synchronization settings for a particular application.
        self._templates: Optional[List[synchronization_template.SynchronizationTemplate]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Synchronization:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Synchronization
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Synchronization()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "jobs": lambda n : setattr(self, 'jobs', n.get_collection_of_object_values(synchronization_job.SynchronizationJob)),
            "secrets": lambda n : setattr(self, 'secrets', n.get_collection_of_object_values(synchronization_secret_key_string_value_pair.SynchronizationSecretKeyStringValuePair)),
            "templates": lambda n : setattr(self, 'templates', n.get_collection_of_object_values(synchronization_template.SynchronizationTemplate)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def jobs(self,) -> Optional[List[synchronization_job.SynchronizationJob]]:
        """
        Gets the jobs property value. Performs synchronization by periodically running in the background, polling for changes in one directory, and pushing them to another directory.
        Returns: Optional[List[synchronization_job.SynchronizationJob]]
        """
        return self._jobs
    
    @jobs.setter
    def jobs(self,value: Optional[List[synchronization_job.SynchronizationJob]] = None) -> None:
        """
        Sets the jobs property value. Performs synchronization by periodically running in the background, polling for changes in one directory, and pushing them to another directory.
        Args:
            value: Value to set for the jobs property.
        """
        self._jobs = value
    
    @property
    def secrets(self,) -> Optional[List[synchronization_secret_key_string_value_pair.SynchronizationSecretKeyStringValuePair]]:
        """
        Gets the secrets property value. Represents a collection of credentials to access provisioned cloud applications.
        Returns: Optional[List[synchronization_secret_key_string_value_pair.SynchronizationSecretKeyStringValuePair]]
        """
        return self._secrets
    
    @secrets.setter
    def secrets(self,value: Optional[List[synchronization_secret_key_string_value_pair.SynchronizationSecretKeyStringValuePair]] = None) -> None:
        """
        Sets the secrets property value. Represents a collection of credentials to access provisioned cloud applications.
        Args:
            value: Value to set for the secrets property.
        """
        self._secrets = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("jobs", self.jobs)
        writer.write_collection_of_object_values("secrets", self.secrets)
        writer.write_collection_of_object_values("templates", self.templates)
    
    @property
    def templates(self,) -> Optional[List[synchronization_template.SynchronizationTemplate]]:
        """
        Gets the templates property value. Pre-configured synchronization settings for a particular application.
        Returns: Optional[List[synchronization_template.SynchronizationTemplate]]
        """
        return self._templates
    
    @templates.setter
    def templates(self,value: Optional[List[synchronization_template.SynchronizationTemplate]] = None) -> None:
        """
        Sets the templates property value. Pre-configured synchronization settings for a particular application.
        Args:
            value: Value to set for the templates property.
        """
        self._templates = value
    

