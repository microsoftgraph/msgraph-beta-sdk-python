from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import run, task_report, user_processing_result, workflow_base, workflow_version

from . import workflow_base

@dataclass
class Workflow(workflow_base.WorkflowBase):
    odata_type = "#microsoft.graph.identityGovernance.workflow"
    # When the workflow was deleted.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
    deleted_date_time: Optional[datetime] = None
    # The unique identifier of the Azure AD identity that last modified the workflow object.
    execution_scope: Optional[List[user_processing_result.UserProcessingResult]] = None
    # Identifier used for individually addressing a specific workflow.Supports $filter(eq, ne) and $orderby.
    id: Optional[str] = None
    # The date time when the workflow is expected to run next based on the schedule interval, if there are any users matching the execution conditions. Supports $filter(lt,gt) and $orderBy.
    next_schedule_run_date_time: Optional[datetime] = None
    # Workflow runs.
    runs: Optional[List[run.Run]] = None
    # Represents the aggregation of task execution data for tasks within a workflow object.
    task_reports: Optional[List[task_report.TaskReport]] = None
    # Per-user workflow execution results.
    user_processing_results: Optional[List[user_processing_result.UserProcessingResult]] = None
    # The current version number of the workflow. Value is 1 when the workflow is first created.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
    version: Optional[int] = None
    # The workflow versions that are available.
    versions: Optional[List[workflow_version.WorkflowVersion]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Workflow:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Workflow
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Workflow()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import run, task_report, user_processing_result, workflow_base, workflow_version

        from . import run, task_report, user_processing_result, workflow_base, workflow_version

        fields: Dict[str, Callable[[Any], None]] = {
            "deletedDateTime": lambda n : setattr(self, 'deleted_date_time', n.get_datetime_value()),
            "executionScope": lambda n : setattr(self, 'execution_scope', n.get_collection_of_object_values(user_processing_result.UserProcessingResult)),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "nextScheduleRunDateTime": lambda n : setattr(self, 'next_schedule_run_date_time', n.get_datetime_value()),
            "runs": lambda n : setattr(self, 'runs', n.get_collection_of_object_values(run.Run)),
            "taskReports": lambda n : setattr(self, 'task_reports', n.get_collection_of_object_values(task_report.TaskReport)),
            "userProcessingResults": lambda n : setattr(self, 'user_processing_results', n.get_collection_of_object_values(user_processing_result.UserProcessingResult)),
            "version": lambda n : setattr(self, 'version', n.get_int_value()),
            "versions": lambda n : setattr(self, 'versions', n.get_collection_of_object_values(workflow_version.WorkflowVersion)),
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
        writer.write_datetime_value("deletedDateTime", self.deleted_date_time)
        writer.write_collection_of_object_values("executionScope", self.execution_scope)
        writer.write_str_value("id", self.id)
        writer.write_datetime_value("nextScheduleRunDateTime", self.next_schedule_run_date_time)
        writer.write_collection_of_object_values("runs", self.runs)
        writer.write_collection_of_object_values("taskReports", self.task_reports)
        writer.write_collection_of_object_values("userProcessingResults", self.user_processing_results)
        writer.write_int_value("version", self.version)
        writer.write_collection_of_object_values("versions", self.versions)
    

