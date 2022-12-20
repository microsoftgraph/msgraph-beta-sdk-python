from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
lifecycle_workflow_processing_status = lazy_import('msgraph.generated.models.identity_governance.lifecycle_workflow_processing_status')
task = lazy_import('msgraph.generated.models.identity_governance.task')
task_definition = lazy_import('msgraph.generated.models.identity_governance.task_definition')
task_processing_result = lazy_import('msgraph.generated.models.identity_governance.task_processing_result')

class TaskReport(entity.Entity):
    """
    Provides operations to manage the collection of accessReviewDecision entities.
    """
    @property
    def completed_date_time(self,) -> Optional[datetime]:
        """
        Gets the completedDateTime property value. The date time that the associated run completed. Value is null if the run has not completed.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
        Returns: Optional[datetime]
        """
        return self._completed_date_time
    
    @completed_date_time.setter
    def completed_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the completedDateTime property value. The date time that the associated run completed. Value is null if the run has not completed.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
        Args:
            value: Value to set for the completedDateTime property.
        """
        self._completed_date_time = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new taskReport and sets the default values.
        """
        super().__init__()
        # The date time that the associated run completed. Value is null if the run has not completed.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
        self._completed_date_time: Optional[datetime] = None
        # The number of users in the run execution for which the associated task failed.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
        self._failed_users_count: Optional[int] = None
        # The date and time that the task report was last updated.
        self._last_updated_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The processingStatus property
        self._processing_status: Optional[lifecycle_workflow_processing_status.LifecycleWorkflowProcessingStatus] = None
        # The unique identifier of the associated run.
        self._run_id: Optional[str] = None
        # The date time that the associated run started. Value is null if the run has not started.
        self._started_date_time: Optional[datetime] = None
        # The number of users in the run execution for which the associated task succeeded.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
        self._successful_users_count: Optional[int] = None
        # The task property
        self._task: Optional[task.Task] = None
        # The taskDefinition property
        self._task_definition: Optional[task_definition.TaskDefinition] = None
        # The related lifecycle workflow taskProcessingResults.
        self._task_processing_results: Optional[List[task_processing_result.TaskProcessingResult]] = None
        # The total number of users in the run execution for which the associated task was scheduled to execute.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
        self._total_users_count: Optional[int] = None
        # The number of users in the run execution for which the associated task is queued, in progress, or canceled.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
        self._unprocessed_users_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TaskReport:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TaskReport
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TaskReport()
    
    @property
    def failed_users_count(self,) -> Optional[int]:
        """
        Gets the failedUsersCount property value. The number of users in the run execution for which the associated task failed.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
        Returns: Optional[int]
        """
        return self._failed_users_count
    
    @failed_users_count.setter
    def failed_users_count(self,value: Optional[int] = None) -> None:
        """
        Sets the failedUsersCount property value. The number of users in the run execution for which the associated task failed.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
        Args:
            value: Value to set for the failedUsersCount property.
        """
        self._failed_users_count = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "completed_date_time": lambda n : setattr(self, 'completed_date_time', n.get_datetime_value()),
            "failed_users_count": lambda n : setattr(self, 'failed_users_count', n.get_int_value()),
            "last_updated_date_time": lambda n : setattr(self, 'last_updated_date_time', n.get_datetime_value()),
            "processing_status": lambda n : setattr(self, 'processing_status', n.get_enum_value(lifecycle_workflow_processing_status.LifecycleWorkflowProcessingStatus)),
            "run_id": lambda n : setattr(self, 'run_id', n.get_str_value()),
            "started_date_time": lambda n : setattr(self, 'started_date_time', n.get_datetime_value()),
            "successful_users_count": lambda n : setattr(self, 'successful_users_count', n.get_int_value()),
            "task": lambda n : setattr(self, 'task', n.get_object_value(task.Task)),
            "task_definition": lambda n : setattr(self, 'task_definition', n.get_object_value(task_definition.TaskDefinition)),
            "task_processing_results": lambda n : setattr(self, 'task_processing_results', n.get_collection_of_object_values(task_processing_result.TaskProcessingResult)),
            "total_users_count": lambda n : setattr(self, 'total_users_count', n.get_int_value()),
            "unprocessed_users_count": lambda n : setattr(self, 'unprocessed_users_count', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_updated_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastUpdatedDateTime property value. The date and time that the task report was last updated.
        Returns: Optional[datetime]
        """
        return self._last_updated_date_time
    
    @last_updated_date_time.setter
    def last_updated_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastUpdatedDateTime property value. The date and time that the task report was last updated.
        Args:
            value: Value to set for the lastUpdatedDateTime property.
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
            value: Value to set for the processingStatus property.
        """
        self._processing_status = value
    
    @property
    def run_id(self,) -> Optional[str]:
        """
        Gets the runId property value. The unique identifier of the associated run.
        Returns: Optional[str]
        """
        return self._run_id
    
    @run_id.setter
    def run_id(self,value: Optional[str] = None) -> None:
        """
        Sets the runId property value. The unique identifier of the associated run.
        Args:
            value: Value to set for the runId property.
        """
        self._run_id = value
    
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
        writer.write_int_value("failedUsersCount", self.failed_users_count)
        writer.write_datetime_value("lastUpdatedDateTime", self.last_updated_date_time)
        writer.write_enum_value("processingStatus", self.processing_status)
        writer.write_str_value("runId", self.run_id)
        writer.write_datetime_value("startedDateTime", self.started_date_time)
        writer.write_int_value("successfulUsersCount", self.successful_users_count)
        writer.write_object_value("task", self.task)
        writer.write_object_value("taskDefinition", self.task_definition)
        writer.write_collection_of_object_values("taskProcessingResults", self.task_processing_results)
        writer.write_int_value("totalUsersCount", self.total_users_count)
        writer.write_int_value("unprocessedUsersCount", self.unprocessed_users_count)
    
    @property
    def started_date_time(self,) -> Optional[datetime]:
        """
        Gets the startedDateTime property value. The date time that the associated run started. Value is null if the run has not started.
        Returns: Optional[datetime]
        """
        return self._started_date_time
    
    @started_date_time.setter
    def started_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the startedDateTime property value. The date time that the associated run started. Value is null if the run has not started.
        Args:
            value: Value to set for the startedDateTime property.
        """
        self._started_date_time = value
    
    @property
    def successful_users_count(self,) -> Optional[int]:
        """
        Gets the successfulUsersCount property value. The number of users in the run execution for which the associated task succeeded.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
        Returns: Optional[int]
        """
        return self._successful_users_count
    
    @successful_users_count.setter
    def successful_users_count(self,value: Optional[int] = None) -> None:
        """
        Sets the successfulUsersCount property value. The number of users in the run execution for which the associated task succeeded.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
        Args:
            value: Value to set for the successfulUsersCount property.
        """
        self._successful_users_count = value
    
    @property
    def task(self,) -> Optional[task.Task]:
        """
        Gets the task property value. The task property
        Returns: Optional[task.Task]
        """
        return self._task
    
    @task.setter
    def task(self,value: Optional[task.Task] = None) -> None:
        """
        Sets the task property value. The task property
        Args:
            value: Value to set for the task property.
        """
        self._task = value
    
    @property
    def task_definition(self,) -> Optional[task_definition.TaskDefinition]:
        """
        Gets the taskDefinition property value. The taskDefinition property
        Returns: Optional[task_definition.TaskDefinition]
        """
        return self._task_definition
    
    @task_definition.setter
    def task_definition(self,value: Optional[task_definition.TaskDefinition] = None) -> None:
        """
        Sets the taskDefinition property value. The taskDefinition property
        Args:
            value: Value to set for the taskDefinition property.
        """
        self._task_definition = value
    
    @property
    def task_processing_results(self,) -> Optional[List[task_processing_result.TaskProcessingResult]]:
        """
        Gets the taskProcessingResults property value. The related lifecycle workflow taskProcessingResults.
        Returns: Optional[List[task_processing_result.TaskProcessingResult]]
        """
        return self._task_processing_results
    
    @task_processing_results.setter
    def task_processing_results(self,value: Optional[List[task_processing_result.TaskProcessingResult]] = None) -> None:
        """
        Sets the taskProcessingResults property value. The related lifecycle workflow taskProcessingResults.
        Args:
            value: Value to set for the taskProcessingResults property.
        """
        self._task_processing_results = value
    
    @property
    def total_users_count(self,) -> Optional[int]:
        """
        Gets the totalUsersCount property value. The total number of users in the run execution for which the associated task was scheduled to execute.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
        Returns: Optional[int]
        """
        return self._total_users_count
    
    @total_users_count.setter
    def total_users_count(self,value: Optional[int] = None) -> None:
        """
        Sets the totalUsersCount property value. The total number of users in the run execution for which the associated task was scheduled to execute.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
        Args:
            value: Value to set for the totalUsersCount property.
        """
        self._total_users_count = value
    
    @property
    def unprocessed_users_count(self,) -> Optional[int]:
        """
        Gets the unprocessedUsersCount property value. The number of users in the run execution for which the associated task is queued, in progress, or canceled.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
        Returns: Optional[int]
        """
        return self._unprocessed_users_count
    
    @unprocessed_users_count.setter
    def unprocessed_users_count(self,value: Optional[int] = None) -> None:
        """
        Sets the unprocessedUsersCount property value. The number of users in the run execution for which the associated task is queued, in progress, or canceled.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
        Args:
            value: Value to set for the unprocessedUsersCount property.
        """
        self._unprocessed_users_count = value
    

