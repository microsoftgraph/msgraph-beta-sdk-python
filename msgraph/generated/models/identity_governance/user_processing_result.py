from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import lifecycle_workflow_processing_status, task_processing_result, workflow_execution_type
    from .. import entity, user

from .. import entity

@dataclass
class UserProcessingResult(entity.Entity):
    # The date time that the workflow execution for a user completed. Value is null if the workflow hasn't completed.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
    completed_date_time: Optional[datetime] = None
    # The number of tasks that failed in the workflow execution.
    failed_tasks_count: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The processingStatus property
    processing_status: Optional[lifecycle_workflow_processing_status.LifecycleWorkflowProcessingStatus] = None
    # The date time that the workflow is scheduled to be executed for a user.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
    scheduled_date_time: Optional[datetime] = None
    # The date time that the workflow execution started. Value is null if the workflow execution has not started.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
    started_date_time: Optional[datetime] = None
    # The subject property
    subject: Optional[user.User] = None
    # The associated individual task execution.
    task_processing_results: Optional[List[task_processing_result.TaskProcessingResult]] = None
    # The total number of tasks that in the workflow execution.
    total_tasks_count: Optional[int] = None
    # The total number of unprocessed tasks for the workflow.
    total_unprocessed_tasks_count: Optional[int] = None
    # The workflowExecutionType property
    workflow_execution_type: Optional[workflow_execution_type.WorkflowExecutionType] = None
    # The version of the workflow that was executed.
    workflow_version: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserProcessingResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserProcessingResult
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UserProcessingResult()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import lifecycle_workflow_processing_status, task_processing_result, workflow_execution_type
        from .. import entity, user

        fields: Dict[str, Callable[[Any], None]] = {
            "completedDateTime": lambda n : setattr(self, 'completed_date_time', n.get_datetime_value()),
            "failedTasksCount": lambda n : setattr(self, 'failed_tasks_count', n.get_int_value()),
            "processingStatus": lambda n : setattr(self, 'processing_status', n.get_enum_value(lifecycle_workflow_processing_status.LifecycleWorkflowProcessingStatus)),
            "scheduledDateTime": lambda n : setattr(self, 'scheduled_date_time', n.get_datetime_value()),
            "startedDateTime": lambda n : setattr(self, 'started_date_time', n.get_datetime_value()),
            "subject": lambda n : setattr(self, 'subject', n.get_object_value(user.User)),
            "taskProcessingResults": lambda n : setattr(self, 'task_processing_results', n.get_collection_of_object_values(task_processing_result.TaskProcessingResult)),
            "totalTasksCount": lambda n : setattr(self, 'total_tasks_count', n.get_int_value()),
            "totalUnprocessedTasksCount": lambda n : setattr(self, 'total_unprocessed_tasks_count', n.get_int_value()),
            "workflowExecutionType": lambda n : setattr(self, 'workflow_execution_type', n.get_enum_value(workflow_execution_type.WorkflowExecutionType)),
            "workflowVersion": lambda n : setattr(self, 'workflow_version', n.get_int_value()),
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
        writer.write_datetime_value("completedDateTime", self.completed_date_time)
        writer.write_int_value("failedTasksCount", self.failed_tasks_count)
        writer.write_enum_value("processingStatus", self.processing_status)
        writer.write_datetime_value("scheduledDateTime", self.scheduled_date_time)
        writer.write_datetime_value("startedDateTime", self.started_date_time)
        writer.write_object_value("subject", self.subject)
        writer.write_collection_of_object_values("taskProcessingResults", self.task_processing_results)
        writer.write_int_value("totalTasksCount", self.total_tasks_count)
        writer.write_int_value("totalUnprocessedTasksCount", self.total_unprocessed_tasks_count)
        writer.write_enum_value("workflowExecutionType", self.workflow_execution_type)
        writer.write_int_value("workflowVersion", self.workflow_version)
    

