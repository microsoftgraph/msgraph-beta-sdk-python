from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
key_value_pair = lazy_import('msgraph.generated.models.key_value_pair')
synchronization_schedule = lazy_import('msgraph.generated.models.synchronization_schedule')
synchronization_schema = lazy_import('msgraph.generated.models.synchronization_schema')
synchronization_status = lazy_import('msgraph.generated.models.synchronization_status')

class SynchronizationJob(entity.Entity):
    """
    Casts the previous resource to application.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new synchronizationJob and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Schedule used to run the job. Read-only.
        self._schedule: Optional[synchronization_schedule.SynchronizationSchedule] = None
        # The synchronization schema configured for the job.
        self._schema: Optional[synchronization_schema.SynchronizationSchema] = None
        # Status of the job, which includes when the job was last run, current job state, and errors.
        self._status: Optional[synchronization_status.SynchronizationStatus] = None
        # Settings associated with the job. Some settings are inherited from the template.
        self._synchronization_job_settings: Optional[List[key_value_pair.KeyValuePair]] = None
        # Identifier of the synchronization template this job is based on.
        self._template_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SynchronizationJob:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SynchronizationJob
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SynchronizationJob()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "schedule": lambda n : setattr(self, 'schedule', n.get_object_value(synchronization_schedule.SynchronizationSchedule)),
            "schema": lambda n : setattr(self, 'schema', n.get_object_value(synchronization_schema.SynchronizationSchema)),
            "status": lambda n : setattr(self, 'status', n.get_object_value(synchronization_status.SynchronizationStatus)),
            "synchronization_job_settings": lambda n : setattr(self, 'synchronization_job_settings', n.get_collection_of_object_values(key_value_pair.KeyValuePair)),
            "template_id": lambda n : setattr(self, 'template_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def schedule(self,) -> Optional[synchronization_schedule.SynchronizationSchedule]:
        """
        Gets the schedule property value. Schedule used to run the job. Read-only.
        Returns: Optional[synchronization_schedule.SynchronizationSchedule]
        """
        return self._schedule
    
    @schedule.setter
    def schedule(self,value: Optional[synchronization_schedule.SynchronizationSchedule] = None) -> None:
        """
        Sets the schedule property value. Schedule used to run the job. Read-only.
        Args:
            value: Value to set for the schedule property.
        """
        self._schedule = value
    
    @property
    def schema(self,) -> Optional[synchronization_schema.SynchronizationSchema]:
        """
        Gets the schema property value. The synchronization schema configured for the job.
        Returns: Optional[synchronization_schema.SynchronizationSchema]
        """
        return self._schema
    
    @schema.setter
    def schema(self,value: Optional[synchronization_schema.SynchronizationSchema] = None) -> None:
        """
        Sets the schema property value. The synchronization schema configured for the job.
        Args:
            value: Value to set for the schema property.
        """
        self._schema = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("schedule", self.schedule)
        writer.write_object_value("schema", self.schema)
        writer.write_object_value("status", self.status)
        writer.write_collection_of_object_values("synchronizationJobSettings", self.synchronization_job_settings)
        writer.write_str_value("templateId", self.template_id)
    
    @property
    def status(self,) -> Optional[synchronization_status.SynchronizationStatus]:
        """
        Gets the status property value. Status of the job, which includes when the job was last run, current job state, and errors.
        Returns: Optional[synchronization_status.SynchronizationStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[synchronization_status.SynchronizationStatus] = None) -> None:
        """
        Sets the status property value. Status of the job, which includes when the job was last run, current job state, and errors.
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    
    @property
    def synchronization_job_settings(self,) -> Optional[List[key_value_pair.KeyValuePair]]:
        """
        Gets the synchronizationJobSettings property value. Settings associated with the job. Some settings are inherited from the template.
        Returns: Optional[List[key_value_pair.KeyValuePair]]
        """
        return self._synchronization_job_settings
    
    @synchronization_job_settings.setter
    def synchronization_job_settings(self,value: Optional[List[key_value_pair.KeyValuePair]] = None) -> None:
        """
        Sets the synchronizationJobSettings property value. Settings associated with the job. Some settings are inherited from the template.
        Args:
            value: Value to set for the synchronizationJobSettings property.
        """
        self._synchronization_job_settings = value
    
    @property
    def template_id(self,) -> Optional[str]:
        """
        Gets the templateId property value. Identifier of the synchronization template this job is based on.
        Returns: Optional[str]
        """
        return self._template_id
    
    @template_id.setter
    def template_id(self,value: Optional[str] = None) -> None:
        """
        Sets the templateId property value. Identifier of the synchronization template this job is based on.
        Args:
            value: Value to set for the templateId property.
        """
        self._template_id = value
    

