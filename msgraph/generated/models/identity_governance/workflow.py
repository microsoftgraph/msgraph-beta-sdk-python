from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

user = lazy_import('msgraph.generated.models.user')
run = lazy_import('msgraph.generated.models.identity_governance.run')
task_report = lazy_import('msgraph.generated.models.identity_governance.task_report')
user_processing_result = lazy_import('msgraph.generated.models.identity_governance.user_processing_result')
workflow_base = lazy_import('msgraph.generated.models.identity_governance.workflow_base')
workflow_version = lazy_import('msgraph.generated.models.identity_governance.workflow_version')

class Workflow(workflow_base.WorkflowBase):
    def __init__(self,) -> None:
        """
        Instantiates a new Workflow and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.identityGovernance.workflow"
        # When the workflow was deleted.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
        self._deleted_date_time: Optional[datetime] = None
        # The unique identifier of the Azure AD identity that last modified the workflow object.
        self._execution_scope: Optional[List[user.User]] = None
        # Identifier used for individually addressing a specific workflow.Supports $filter(eq, ne) and $orderby.
        self._id: Optional[str] = None
        # The date time when the workflow is expected to run next based on the schedule interval, if there are any users matching the execution conditions. Supports $filter(lt,gt) and $orderBy.
        self._next_schedule_run_date_time: Optional[datetime] = None
        # The runs property
        self._runs: Optional[List[run.Run]] = None
        # Represents the aggregation of task execution data for tasks within a workflow object.
        self._task_reports: Optional[List[task_report.TaskReport]] = None
        # The userProcessingResults property
        self._user_processing_results: Optional[List[user_processing_result.UserProcessingResult]] = None
        # The current version number of the workflow. Value is 1 when the workflow is first created.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
        self._version: Optional[int] = None
        # The workflow versions that are available.
        self._versions: Optional[List[workflow_version.WorkflowVersion]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Workflow:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Workflow
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Workflow()
    
    @property
    def deleted_date_time(self,) -> Optional[datetime]:
        """
        Gets the deletedDateTime property value. When the workflow was deleted.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
        Returns: Optional[datetime]
        """
        return self._deleted_date_time
    
    @deleted_date_time.setter
    def deleted_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the deletedDateTime property value. When the workflow was deleted.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
        Args:
            value: Value to set for the deletedDateTime property.
        """
        self._deleted_date_time = value
    
    @property
    def execution_scope(self,) -> Optional[List[user.User]]:
        """
        Gets the executionScope property value. The unique identifier of the Azure AD identity that last modified the workflow object.
        Returns: Optional[List[user.User]]
        """
        return self._execution_scope
    
    @execution_scope.setter
    def execution_scope(self,value: Optional[List[user.User]] = None) -> None:
        """
        Sets the executionScope property value. The unique identifier of the Azure AD identity that last modified the workflow object.
        Args:
            value: Value to set for the executionScope property.
        """
        self._execution_scope = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "deleted_date_time": lambda n : setattr(self, 'deleted_date_time', n.get_datetime_value()),
            "execution_scope": lambda n : setattr(self, 'execution_scope', n.get_collection_of_object_values(user.User)),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "next_schedule_run_date_time": lambda n : setattr(self, 'next_schedule_run_date_time', n.get_datetime_value()),
            "runs": lambda n : setattr(self, 'runs', n.get_collection_of_object_values(run.Run)),
            "task_reports": lambda n : setattr(self, 'task_reports', n.get_collection_of_object_values(task_report.TaskReport)),
            "user_processing_results": lambda n : setattr(self, 'user_processing_results', n.get_collection_of_object_values(user_processing_result.UserProcessingResult)),
            "version": lambda n : setattr(self, 'version', n.get_int_value()),
            "versions": lambda n : setattr(self, 'versions', n.get_collection_of_object_values(workflow_version.WorkflowVersion)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def id(self,) -> Optional[str]:
        """
        Gets the id property value. Identifier used for individually addressing a specific workflow.Supports $filter(eq, ne) and $orderby.
        Returns: Optional[str]
        """
        return self._id
    
    @id.setter
    def id(self,value: Optional[str] = None) -> None:
        """
        Sets the id property value. Identifier used for individually addressing a specific workflow.Supports $filter(eq, ne) and $orderby.
        Args:
            value: Value to set for the id property.
        """
        self._id = value
    
    @property
    def next_schedule_run_date_time(self,) -> Optional[datetime]:
        """
        Gets the nextScheduleRunDateTime property value. The date time when the workflow is expected to run next based on the schedule interval, if there are any users matching the execution conditions. Supports $filter(lt,gt) and $orderBy.
        Returns: Optional[datetime]
        """
        return self._next_schedule_run_date_time
    
    @next_schedule_run_date_time.setter
    def next_schedule_run_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the nextScheduleRunDateTime property value. The date time when the workflow is expected to run next based on the schedule interval, if there are any users matching the execution conditions. Supports $filter(lt,gt) and $orderBy.
        Args:
            value: Value to set for the nextScheduleRunDateTime property.
        """
        self._next_schedule_run_date_time = value
    
    @property
    def runs(self,) -> Optional[List[run.Run]]:
        """
        Gets the runs property value. The runs property
        Returns: Optional[List[run.Run]]
        """
        return self._runs
    
    @runs.setter
    def runs(self,value: Optional[List[run.Run]] = None) -> None:
        """
        Sets the runs property value. The runs property
        Args:
            value: Value to set for the runs property.
        """
        self._runs = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_datetime_value("deletedDateTime", self.deleted_date_time)
        writer.write_collection_of_object_values("executionScope", self.execution_scope)
        writer.write_str_value("id", self.id)
        writer.write_datetime_value("nextScheduleRunDateTime", self.next_schedule_run_date_time)
        writer.write_collection_of_object_values("runs", self.runs)
        writer.write_collection_of_object_values("taskReports", self.task_reports)
        writer.write_collection_of_object_values("userProcessingResults", self.user_processing_results)
        writer.write_int_value("version", self.version)
        writer.write_collection_of_object_values("versions", self.versions)
    
    @property
    def task_reports(self,) -> Optional[List[task_report.TaskReport]]:
        """
        Gets the taskReports property value. Represents the aggregation of task execution data for tasks within a workflow object.
        Returns: Optional[List[task_report.TaskReport]]
        """
        return self._task_reports
    
    @task_reports.setter
    def task_reports(self,value: Optional[List[task_report.TaskReport]] = None) -> None:
        """
        Sets the taskReports property value. Represents the aggregation of task execution data for tasks within a workflow object.
        Args:
            value: Value to set for the taskReports property.
        """
        self._task_reports = value
    
    @property
    def user_processing_results(self,) -> Optional[List[user_processing_result.UserProcessingResult]]:
        """
        Gets the userProcessingResults property value. The userProcessingResults property
        Returns: Optional[List[user_processing_result.UserProcessingResult]]
        """
        return self._user_processing_results
    
    @user_processing_results.setter
    def user_processing_results(self,value: Optional[List[user_processing_result.UserProcessingResult]] = None) -> None:
        """
        Sets the userProcessingResults property value. The userProcessingResults property
        Args:
            value: Value to set for the userProcessingResults property.
        """
        self._user_processing_results = value
    
    @property
    def version(self,) -> Optional[int]:
        """
        Gets the version property value. The current version number of the workflow. Value is 1 when the workflow is first created.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
        Returns: Optional[int]
        """
        return self._version
    
    @version.setter
    def version(self,value: Optional[int] = None) -> None:
        """
        Sets the version property value. The current version number of the workflow. Value is 1 when the workflow is first created.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
        Args:
            value: Value to set for the version property.
        """
        self._version = value
    
    @property
    def versions(self,) -> Optional[List[workflow_version.WorkflowVersion]]:
        """
        Gets the versions property value. The workflow versions that are available.
        Returns: Optional[List[workflow_version.WorkflowVersion]]
        """
        return self._versions
    
    @versions.setter
    def versions(self,value: Optional[List[workflow_version.WorkflowVersion]] = None) -> None:
        """
        Sets the versions property value. The workflow versions that are available.
        Args:
            value: Value to set for the versions property.
        """
        self._versions = value
    

