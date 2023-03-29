from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import lifecycle_workflow_processing_status, task_processing_result, workflow_execution_type
    from .. import entity, user

from .. import entity

class UserProcessingResult(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new userProcessingResult and sets the default values.
        """
        super().__init__()
        # The date time that the workflow execution for a user completed. Value is null if the workflow hasn't completed.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
        self._completed_date_time: Optional[datetime] = None
        # The number of tasks that failed in the workflow execution.
        self._failed_tasks_count: Optional[int] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The processingStatus property
        self._processing_status: Optional[lifecycle_workflow_processing_status.LifecycleWorkflowProcessingStatus] = None
        # The date time that the workflow is scheduled to be executed for a user.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
        self._scheduled_date_time: Optional[datetime] = None
        # The date time that the workflow execution started. Value is null if the workflow execution has not started.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
        self._started_date_time: Optional[datetime] = None
        # The subject property
        self._subject: Optional[user.User] = None
        # The associated individual task execution.
        self._task_processing_results: Optional[List[task_processing_result.TaskProcessingResult]] = None
        # The total number of tasks that in the workflow execution.
        self._total_tasks_count: Optional[int] = None
        # The total number of unprocessed tasks for the workflow.
        self._total_unprocessed_tasks_count: Optional[int] = None
        # The workflowExecutionType property
        self._workflow_execution_type: Optional[workflow_execution_type.WorkflowExecutionType] = None
        # The version of the workflow that was executed.
        self._workflow_version: Optional[int] = None
    
    @property
    def completed_date_time(self,) -> Optional[datetime]:
        """
        Gets the completedDateTime property value. The date time that the workflow execution for a user completed. Value is null if the workflow hasn't completed.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
        Returns: Optional[datetime]
        """
        return self._completed_date_time
    
    @completed_date_time.setter
    def completed_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the completedDateTime property value. The date time that the workflow execution for a user completed. Value is null if the workflow hasn't completed.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
        Args:
            value: Value to set for the completed_date_time property.
        """
        self._completed_date_time = value
    
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
    
    @property
    def failed_tasks_count(self,) -> Optional[int]:
        """
        Gets the failedTasksCount property value. The number of tasks that failed in the workflow execution.
        Returns: Optional[int]
        """
        return self._failed_tasks_count
    
    @failed_tasks_count.setter
    def failed_tasks_count(self,value: Optional[int] = None) -> None:
        """
        Sets the failedTasksCount property value. The number of tasks that failed in the workflow execution.
        Args:
            value: Value to set for the failed_tasks_count property.
        """
        self._failed_tasks_count = value
    
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
    
    @property
    def processing_status(self,) -> Optional[lifecycle_workflow_processing_status.LifecycleWorkflowProcessingStatus]:
        """
        Gets the processingStatus property value. The processingStatus property
        Returns: Optional[lifecycle_workflow_processing_status.LifecycleWorkflowProcessingStatus]
        """
        return self._processing_status
    
    @processing_status.setter
    def processing_status(self,value: Optional[lifecycle_workflow_processing_status.LifecycleWorkflowProcessingStatus] = None) -> None:
        """
        Sets the processingStatus property value. The processingStatus property
        Args:
            value: Value to set for the processing_status property.
        """
        self._processing_status = value
    
    @property
    def scheduled_date_time(self,) -> Optional[datetime]:
        """
        Gets the scheduledDateTime property value. The date time that the workflow is scheduled to be executed for a user.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
        Returns: Optional[datetime]
        """
        return self._scheduled_date_time
    
    @scheduled_date_time.setter
    def scheduled_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the scheduledDateTime property value. The date time that the workflow is scheduled to be executed for a user.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
        Args:
            value: Value to set for the scheduled_date_time property.
        """
        self._scheduled_date_time = value
    
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
    
    @property
    def started_date_time(self,) -> Optional[datetime]:
        """
        Gets the startedDateTime property value. The date time that the workflow execution started. Value is null if the workflow execution has not started.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
        Returns: Optional[datetime]
        """
        return self._started_date_time
    
    @started_date_time.setter
    def started_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the startedDateTime property value. The date time that the workflow execution started. Value is null if the workflow execution has not started.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
        Args:
            value: Value to set for the started_date_time property.
        """
        self._started_date_time = value
    
    @property
    def subject(self,) -> Optional[user.User]:
        """
        Gets the subject property value. The subject property
        Returns: Optional[user.User]
        """
        return self._subject
    
    @subject.setter
    def subject(self,value: Optional[user.User] = None) -> None:
        """
        Sets the subject property value. The subject property
        Args:
            value: Value to set for the subject property.
        """
        self._subject = value
    
    @property
    def task_processing_results(self,) -> Optional[List[task_processing_result.TaskProcessingResult]]:
        """
        Gets the taskProcessingResults property value. The associated individual task execution.
        Returns: Optional[List[task_processing_result.TaskProcessingResult]]
        """
        return self._task_processing_results
    
    @task_processing_results.setter
    def task_processing_results(self,value: Optional[List[task_processing_result.TaskProcessingResult]] = None) -> None:
        """
        Sets the taskProcessingResults property value. The associated individual task execution.
        Args:
            value: Value to set for the task_processing_results property.
        """
        self._task_processing_results = value
    
    @property
    def total_tasks_count(self,) -> Optional[int]:
        """
        Gets the totalTasksCount property value. The total number of tasks that in the workflow execution.
        Returns: Optional[int]
        """
        return self._total_tasks_count
    
    @total_tasks_count.setter
    def total_tasks_count(self,value: Optional[int] = None) -> None:
        """
        Sets the totalTasksCount property value. The total number of tasks that in the workflow execution.
        Args:
            value: Value to set for the total_tasks_count property.
        """
        self._total_tasks_count = value
    
    @property
    def total_unprocessed_tasks_count(self,) -> Optional[int]:
        """
        Gets the totalUnprocessedTasksCount property value. The total number of unprocessed tasks for the workflow.
        Returns: Optional[int]
        """
        return self._total_unprocessed_tasks_count
    
    @total_unprocessed_tasks_count.setter
    def total_unprocessed_tasks_count(self,value: Optional[int] = None) -> None:
        """
        Sets the totalUnprocessedTasksCount property value. The total number of unprocessed tasks for the workflow.
        Args:
            value: Value to set for the total_unprocessed_tasks_count property.
        """
        self._total_unprocessed_tasks_count = value
    
    @property
    def workflow_execution_type(self,) -> Optional[workflow_execution_type.WorkflowExecutionType]:
        """
        Gets the workflowExecutionType property value. The workflowExecutionType property
        Returns: Optional[workflow_execution_type.WorkflowExecutionType]
        """
        return self._workflow_execution_type
    
    @workflow_execution_type.setter
    def workflow_execution_type(self,value: Optional[workflow_execution_type.WorkflowExecutionType] = None) -> None:
        """
        Sets the workflowExecutionType property value. The workflowExecutionType property
        Args:
            value: Value to set for the workflow_execution_type property.
        """
        self._workflow_execution_type = value
    
    @property
    def workflow_version(self,) -> Optional[int]:
        """
        Gets the workflowVersion property value. The version of the workflow that was executed.
        Returns: Optional[int]
        """
        return self._workflow_version
    
    @workflow_version.setter
    def workflow_version(self,value: Optional[int] = None) -> None:
        """
        Sets the workflowVersion property value. The version of the workflow that was executed.
        Args:
            value: Value to set for the workflow_version property.
        """
        self._workflow_version = value
    

