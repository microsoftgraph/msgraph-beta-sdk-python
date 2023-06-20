from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, print_document, print_job_configuration, print_job_status, print_task, user_identity

from . import entity

@dataclass
class PrintJob(entity.Entity):
    # The acknowledgedDateTime property
    acknowledged_date_time: Optional[datetime] = None
    # The completedDateTime property
    completed_date_time: Optional[datetime] = None
    # A group of settings that a printer should use to print a job.
    configuration: Optional[print_job_configuration.PrintJobConfiguration] = None
    # The createdBy property
    created_by: Optional[user_identity.UserIdentity] = None
    # The DateTimeOffset when the job was created. Read-only.
    created_date_time: Optional[datetime] = None
    # The name of the print job.
    display_name: Optional[str] = None
    # The documents property
    documents: Optional[List[print_document.PrintDocument]] = None
    # The errorCode property
    error_code: Optional[int] = None
    # If true, document can be fetched by printer.
    is_fetchable: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Contains the source job URL, if the job has been redirected from another printer.
    redirected_from: Optional[str] = None
    # Contains the destination job URL, if the job has been redirected to another printer.
    redirected_to: Optional[str] = None
    # The status of the print job. Read-only.
    status: Optional[print_job_status.PrintJobStatus] = None
    # A list of printTasks that were triggered by this print job.
    tasks: Optional[List[print_task.PrintTask]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PrintJob:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PrintJob
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return PrintJob()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, print_document, print_job_configuration, print_job_status, print_task, user_identity

        from . import entity, print_document, print_job_configuration, print_job_status, print_task, user_identity

        fields: Dict[str, Callable[[Any], None]] = {
            "acknowledgedDateTime": lambda n : setattr(self, 'acknowledged_date_time', n.get_datetime_value()),
            "completedDateTime": lambda n : setattr(self, 'completed_date_time', n.get_datetime_value()),
            "configuration": lambda n : setattr(self, 'configuration', n.get_object_value(print_job_configuration.PrintJobConfiguration)),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(user_identity.UserIdentity)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "documents": lambda n : setattr(self, 'documents', n.get_collection_of_object_values(print_document.PrintDocument)),
            "errorCode": lambda n : setattr(self, 'error_code', n.get_int_value()),
            "isFetchable": lambda n : setattr(self, 'is_fetchable', n.get_bool_value()),
            "redirectedFrom": lambda n : setattr(self, 'redirected_from', n.get_str_value()),
            "redirectedTo": lambda n : setattr(self, 'redirected_to', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_object_value(print_job_status.PrintJobStatus)),
            "tasks": lambda n : setattr(self, 'tasks', n.get_collection_of_object_values(print_task.PrintTask)),
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
        writer.write_datetime_value("acknowledgedDateTime", self.acknowledged_date_time)
        writer.write_datetime_value("completedDateTime", self.completed_date_time)
        writer.write_object_value("configuration", self.configuration)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("documents", self.documents)
        writer.write_int_value("errorCode", self.error_code)
        writer.write_bool_value("isFetchable", self.is_fetchable)
        writer.write_str_value("redirectedFrom", self.redirected_from)
        writer.write_str_value("redirectedTo", self.redirected_to)
        writer.write_object_value("status", self.status)
        writer.write_collection_of_object_values("tasks", self.tasks)
    

