from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import lifecycle_workflow_processing_status, task_processing_result, user_processing_result, workflow_execution_type
    from .. import entity

from .. import entity

class Run(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new Run and sets the default values.
        """
        super().__init__()
        # The date time that the run completed. Value is null if the workflow hasn't completed.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
        self._completed_date_time: Optional[datetime] = None
        # The number of tasks that failed in the run execution.
        self._failed_tasks_count: Optional[int] = None
        # The number of users that failed in the run execution.
        self._failed_users_count: Optional[int] = None
        # The datetime that the run was last updated.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
        self._last_updated_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The processingStatus property
        self._processing_status: Optional[lifecycle_workflow_processing_status.LifecycleWorkflowProcessingStatus] = None
        # The date time that the run is scheduled to be executed for a workflow.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
        self._scheduled_date_time: Optional[datetime] = None
        # The date time that the run execution started.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
        self._started_date_time: Optional[datetime] = None
        # The number of successfully completed users in the run.
        self._successful_users_count: Optional[int] = None
        # The related taskProcessingResults.
        self._task_processing_results: Optional[List[task_processing_result.TaskProcessingResult]] = None
        # The totalTasksCount property
        self._total_tasks_count: Optional[int] = None
        # The total number of unprocessed tasks in the run execution.
        self._total_unprocessed_tasks_count: Optional[int] = None
        # The total number of users in the workflow execution.
        self._total_users_count: Optional[int] = None
        # The associated individual user execution.
        self._user_processing_results: Optional[List[user_processing_result.UserProcessingResult]] = None
        # The workflowExecutionType property
        self._workflow_execution_type: Optional[workflow_execution_type.WorkflowExecutionType] = None
    
    @property
    def completed_date_time(self,) -> Optional[datetime]:
        """
        Gets the completedDateTime property value. The date time that the run completed. Value is null if the workflow hasn't completed.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
        Returns: Optional[datetime]
        """
        return self._completed_date_time
    
    @completed_date_time.setter
    def completed_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the completedDateTime property value. The date time that the run completed. Value is null if the workflow hasn't completed.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
        Args:
            value: Value to set for the completed_date_time property.
        """
        self._completed_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Run:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Run
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Run()
    
    @property
    def failed_tasks_count(self,) -> Optional[int]:
        """
        Gets the failedTasksCount property value. The number of tasks that failed in the run execution.
        Returns: Optional[int]
        """
        return self._failed_tasks_count
    
    @failed_tasks_count.setter
    def failed_tasks_count(self,value: Optional[int] = None) -> None:
        """
        Sets the failedTasksCount property value. The number of tasks that failed in the run execution.
        Args:
            value: Value to set for the failed_tasks_count property.
        """
        self._failed_tasks_count = value
    
    @property
    def failed_users_count(self,) -> Optional[int]:
        """
        Gets the failedUsersCount property value. The number of users that failed in the run execution.
        Returns: Optional[int]
        """
        return self._failed_users_count
    
    @failed_users_count.setter
    def failed_users_count(self,value: Optional[int] = None) -> None:
        """
        Sets the failedUsersCount property value. The number of users that failed in the run execution.
        Args:
            value: Value to set for the failed_users_count property.
        """
        self._failed_users_count = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import lifecycle_workflow_processing_status, task_processing_result, user_processing_result, workflow_execution_type
        from .. import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "completedDateTime": lambda n : setattr(self, 'completed_date_time', n.get_datetime_value()),
            "failedTasksCount": lambda n : setattr(self, 'failed_tasks_count', n.get_int_value()),
            "failedUsersCount": lambda n : setattr(self, 'failed_users_count', n.get_int_value()),
            "lastUpdatedDateTime": lambda n : setattr(self, 'last_updated_date_time', n.get_datetime_value()),
            "processingStatus": lambda n : setattr(self, 'processing_status', n.get_enum_value(lifecycle_workflow_processing_status.LifecycleWorkflowProcessingStatus)),
            "scheduledDateTime": lambda n : setattr(self, 'scheduled_date_time', n.get_datetime_value()),
            "startedDateTime": lambda n : setattr(self, 'started_date_time', n.get_datetime_value()),
            "successfulUsersCount": lambda n : setattr(self, 'successful_users_count', n.get_int_value()),
            "taskProcessingResults": lambda n : setattr(self, 'task_processing_results', n.get_collection_of_object_values(task_processing_result.TaskProcessingResult)),
            "totalTasksCount": lambda n : setattr(self, 'total_tasks_count', n.get_int_value()),
            "totalUnprocessedTasksCount": lambda n : setattr(self, 'total_unprocessed_tasks_count', n.get_int_value()),
            "totalUsersCount": lambda n : setattr(self, 'total_users_count', n.get_int_value()),
            "userProcessingResults": lambda n : setattr(self, 'user_processing_results', n.get_collection_of_object_values(user_processing_result.UserProcessingResult)),
            "workflowExecutionType": lambda n : setattr(self, 'workflow_execution_type', n.get_enum_value(workflow_execution_type.WorkflowExecutionType)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_updated_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastUpdatedDateTime property value. The datetime that the run was last updated.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
        Returns: Optional[datetime]
        """
        return self._last_updated_date_time
    
    @last_updated_date_time.setter
    def last_updated_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastUpdatedDateTime property value. The datetime that the run was last updated.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
        Args:
            value: Value to set for the last_updated_date_time property.
        """
        self._last_updated_date_time = value
    
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
        Gets the scheduledDateTime property value. The date time that the run is scheduled to be executed for a workflow.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
        Returns: Optional[datetime]
        """
        return self._scheduled_date_time
    
    @scheduled_date_time.setter
    def scheduled_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the scheduledDateTime property value. The date time that the run is scheduled to be executed for a workflow.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
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
        writer.write_int_value("failedUsersCount", self.failed_users_count)
        writer.write_datetime_value("lastUpdatedDateTime", self.last_updated_date_time)
        writer.write_enum_value("processingStatus", self.processing_status)
        writer.write_datetime_value("scheduledDateTime", self.scheduled_date_time)
        writer.write_datetime_value("startedDateTime", self.started_date_time)
        writer.write_int_value("successfulUsersCount", self.successful_users_count)
        writer.write_collection_of_object_values("taskProcessingResults", self.task_processing_results)
        writer.write_int_value("totalTasksCount", self.total_tasks_count)
        writer.write_int_value("totalUnprocessedTasksCount", self.total_unprocessed_tasks_count)
        writer.write_int_value("totalUsersCount", self.total_users_count)
        writer.write_collection_of_object_values("userProcessingResults", self.user_processing_results)
        writer.write_enum_value("workflowExecutionType", self.workflow_execution_type)
    
    @property
    def started_date_time(self,) -> Optional[datetime]:
        """
        Gets the startedDateTime property value. The date time that the run execution started.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
        Returns: Optional[datetime]
        """
        return self._started_date_time
    
    @started_date_time.setter
    def started_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the startedDateTime property value. The date time that the run execution started.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
        Args:
            value: Value to set for the started_date_time property.
        """
        self._started_date_time = value
    
    @property
    def successful_users_count(self,) -> Optional[int]:
        """
        Gets the successfulUsersCount property value. The number of successfully completed users in the run.
        Returns: Optional[int]
        """
        return self._successful_users_count
    
    @successful_users_count.setter
    def successful_users_count(self,value: Optional[int] = None) -> None:
        """
        Sets the successfulUsersCount property value. The number of successfully completed users in the run.
        Args:
            value: Value to set for the successful_users_count property.
        """
        self._successful_users_count = value
    
    @property
    def task_processing_results(self,) -> Optional[List[task_processing_result.TaskProcessingResult]]:
        """
        Gets the taskProcessingResults property value. The related taskProcessingResults.
        Returns: Optional[List[task_processing_result.TaskProcessingResult]]
        """
        return self._task_processing_results
    
    @task_processing_results.setter
    def task_processing_results(self,value: Optional[List[task_processing_result.TaskProcessingResult]] = None) -> None:
        """
        Sets the taskProcessingResults property value. The related taskProcessingResults.
        Args:
            value: Value to set for the task_processing_results property.
        """
        self._task_processing_results = value
    
    @property
    def total_tasks_count(self,) -> Optional[int]:
        """
        Gets the totalTasksCount property value. The totalTasksCount property
        Returns: Optional[int]
        """
        return self._total_tasks_count
    
    @total_tasks_count.setter
    def total_tasks_count(self,value: Optional[int] = None) -> None:
        """
        Sets the totalTasksCount property value. The totalTasksCount property
        Args:
            value: Value to set for the total_tasks_count property.
        """
        self._total_tasks_count = value
    
    @property
    def total_unprocessed_tasks_count(self,) -> Optional[int]:
        """
        Gets the totalUnprocessedTasksCount property value. The total number of unprocessed tasks in the run execution.
        Returns: Optional[int]
        """
        return self._total_unprocessed_tasks_count
    
    @total_unprocessed_tasks_count.setter
    def total_unprocessed_tasks_count(self,value: Optional[int] = None) -> None:
        """
        Sets the totalUnprocessedTasksCount property value. The total number of unprocessed tasks in the run execution.
        Args:
            value: Value to set for the total_unprocessed_tasks_count property.
        """
        self._total_unprocessed_tasks_count = value
    
    @property
    def total_users_count(self,) -> Optional[int]:
        """
        Gets the totalUsersCount property value. The total number of users in the workflow execution.
        Returns: Optional[int]
        """
        return self._total_users_count
    
    @total_users_count.setter
    def total_users_count(self,value: Optional[int] = None) -> None:
        """
        Sets the totalUsersCount property value. The total number of users in the workflow execution.
        Args:
            value: Value to set for the total_users_count property.
        """
        self._total_users_count = value
    
    @property
    def user_processing_results(self,) -> Optional[List[user_processing_result.UserProcessingResult]]:
        """
        Gets the userProcessingResults property value. The associated individual user execution.
        Returns: Optional[List[user_processing_result.UserProcessingResult]]
        """
        return self._user_processing_results
    
    @user_processing_results.setter
    def user_processing_results(self,value: Optional[List[user_processing_result.UserProcessingResult]] = None) -> None:
        """
        Sets the userProcessingResults property value. The associated individual user execution.
        Args:
            value: Value to set for the user_processing_results property.
        """
        self._user_processing_results = value
    
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
    

