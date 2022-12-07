from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
user = lazy_import('msgraph.generated.models.user')
lifecycle_workflow_processing_status = lazy_import('msgraph.generated.models.identity_governance.lifecycle_workflow_processing_status')
task = lazy_import('msgraph.generated.models.identity_governance.task')

class TaskProcessingResult(entity.Entity):
    """
    Provides operations to manage the collection of accessReview entities.
    """
    @property
    def completed_date_time(self,) -> Optional[datetime]:
        """
        Gets the completedDateTime property value. The date time when taskProcessingResult execution ended. Value is null if task execution is still in progress.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
        Returns: Optional[datetime]
        """
        return self._completed_date_time
    
    @completed_date_time.setter
    def completed_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the completedDateTime property value. The date time when taskProcessingResult execution ended. Value is null if task execution is still in progress.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
        Args:
            value: Value to set for the completedDateTime property.
        """
        self._completed_date_time = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new taskProcessingResult and sets the default values.
        """
        super().__init__()
        # The date time when taskProcessingResult execution ended. Value is null if task execution is still in progress.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
        self._completed_date_time: Optional[datetime] = None
        # The date time when the taskProcessingResult was created.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
        self._created_date_time: Optional[datetime] = None
        # Describes why the taskProcessingResult has failed.
        self._failure_reason: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The processingStatus property
        self._processing_status: Optional[lifecycle_workflow_processing_status.LifecycleWorkflowProcessingStatus] = None
        # The date time when taskProcessingResult execution started. Value is null if task execution has not yet started.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
        self._started_date_time: Optional[datetime] = None
        # The subject property
        self._subject: Optional[user.User] = None
        # The task property
        self._task: Optional[task.Task] = None
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The date time when the taskProcessingResult was created.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The date time when the taskProcessingResult was created.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TaskProcessingResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TaskProcessingResult
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TaskProcessingResult()
    
    @property
    def failure_reason(self,) -> Optional[str]:
        """
        Gets the failureReason property value. Describes why the taskProcessingResult has failed.
        Returns: Optional[str]
        """
        return self._failure_reason
    
    @failure_reason.setter
    def failure_reason(self,value: Optional[str] = None) -> None:
        """
        Sets the failureReason property value. Describes why the taskProcessingResult has failed.
        Args:
            value: Value to set for the failureReason property.
        """
        self._failure_reason = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "completed_date_time": lambda n : setattr(self, 'completed_date_time', n.get_datetime_value()),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "failure_reason": lambda n : setattr(self, 'failure_reason', n.get_str_value()),
            "processing_status": lambda n : setattr(self, 'processing_status', n.get_enum_value(lifecycle_workflow_processing_status.LifecycleWorkflowProcessingStatus)),
            "started_date_time": lambda n : setattr(self, 'started_date_time', n.get_datetime_value()),
            "subject": lambda n : setattr(self, 'subject', n.get_object_value(user.User)),
            "task": lambda n : setattr(self, 'task', n.get_object_value(task.Task)),
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
            value: Value to set for the processingStatus property.
        """
        self._processing_status = value
    
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
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("failureReason", self.failure_reason)
        writer.write_enum_value("processingStatus", self.processing_status)
        writer.write_datetime_value("startedDateTime", self.started_date_time)
        writer.write_object_value("subject", self.subject)
        writer.write_object_value("task", self.task)
    
    @property
    def started_date_time(self,) -> Optional[datetime]:
        """
        Gets the startedDateTime property value. The date time when taskProcessingResult execution started. Value is null if task execution has not yet started.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
        Returns: Optional[datetime]
        """
        return self._started_date_time
    
    @started_date_time.setter
    def started_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the startedDateTime property value. The date time when taskProcessingResult execution started. Value is null if task execution has not yet started.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
        Args:
            value: Value to set for the startedDateTime property.
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
    

