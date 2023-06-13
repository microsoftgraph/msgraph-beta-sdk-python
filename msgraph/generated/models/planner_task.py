from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import business_scenario_task, identity_set, planner_applied_categories, planner_assigned_to_task_board_task_format, planner_assignments, planner_bucket_task_board_task_format, planner_delta, planner_preview_type, planner_progress_task_board_task_format, planner_task_completion_requirements, planner_task_creation, planner_task_details, planner_task_recurrence

from . import planner_delta

@dataclass
class PlannerTask(planner_delta.PlannerDelta):
    # Number of checklist items with value set to false, representing incomplete items.
    active_checklist_item_count: Optional[int] = None
    # The categories to which the task has been applied. See applied Categories for possible values.
    applied_categories: Optional[planner_applied_categories.PlannerAppliedCategories] = None
    # Read-only. Nullable. Used to render the task correctly in the task board view when grouped by assignedTo.
    assigned_to_task_board_format: Optional[planner_assigned_to_task_board_task_format.PlannerAssignedToTaskBoardTaskFormat] = None
    # Hint used to order items of this type in a list view. The format is defined as outlined here.
    assignee_priority: Optional[str] = None
    # The set of assignees the task is assigned to.
    assignments: Optional[planner_assignments.PlannerAssignments] = None
    # Bucket ID to which the task belongs. The bucket needs to be in the plan that the task is in. It is 28 characters long and case-sensitive. Format validation is done on the service.
    bucket_id: Optional[str] = None
    # Read-only. Nullable. Used to render the task correctly in the task board view when grouped by bucket.
    bucket_task_board_format: Optional[planner_bucket_task_board_task_format.PlannerBucketTaskBoardTaskFormat] = None
    # Number of checklist items that are present on the task.
    checklist_item_count: Optional[int] = None
    # Identity of the user that completed the task.
    completed_by: Optional[identity_set.IdentitySet] = None
    # Read-only. Date and time at which the 'percentComplete' of the task is set to '100'. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    completed_date_time: Optional[datetime] = None
    # Thread ID of the conversation on the task. This is the ID of the conversation thread object created in the group.
    conversation_thread_id: Optional[str] = None
    # Identity of the user that created the task.
    created_by: Optional[identity_set.IdentitySet] = None
    # Read-only. Date and time at which the task is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    created_date_time: Optional[datetime] = None
    # Contains information about the origin of the task.
    creation_source: Optional[planner_task_creation.PlannerTaskCreation] = None
    # Read-only. Nullable. Additional details about the task.
    details: Optional[planner_task_details.PlannerTaskDetails] = None
    # Date and time at which the task is due. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    due_date_time: Optional[datetime] = None
    # Read-only. Value is true if the details object of the task has a non-empty description and false otherwise.
    has_description: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Hint used to order items of this type in a list view. The format is defined as outlined here.
    order_hint: Optional[str] = None
    # Percentage of task completion. When set to 100, the task is considered completed.
    percent_complete: Optional[int] = None
    # Plan ID to which the task belongs.
    plan_id: Optional[str] = None
    # This sets the type of preview that shows up on the task. Possible values are: automatic, noPreview, checklist, description, reference.
    preview_type: Optional[planner_preview_type.PlannerPreviewType] = None
    # Priority of the task. Valid range of values is between 0 and 10 (inclusive), with increasing value being lower priority (0 has the highest priority and 10 has the lowest priority).  Currently, Planner interprets values 0 and 1 as 'urgent', 2 and 3 and 4 as 'important', 5, 6, and 7 as 'medium', and 8, 9, and 10 as 'low'.  Currently, Planner sets the value 1 for 'urgent', 3 for 'important', 5 for 'medium', and 9 for 'low'.
    priority: Optional[int] = None
    # Read-only. Nullable. Used to render the task correctly in the task board view when grouped by progress.
    progress_task_board_format: Optional[planner_progress_task_board_task_format.PlannerProgressTaskBoardTaskFormat] = None
    # Defines active or inactive recurrence for the task. null when the recurrence has never been defined for the task.
    recurrence: Optional[planner_task_recurrence.PlannerTaskRecurrence] = None
    # Number of external references that exist on the task.
    reference_count: Optional[int] = None
    # Indicates all the requirements specified on the plannerTask. Possible values are: none, checklistCompletion, unknownFutureValue. Read-only. The plannerTaskCompletionRequirementDetails in plannerTaskDetails has details of the requirements specified, if any.
    specified_completion_requirements: Optional[planner_task_completion_requirements.PlannerTaskCompletionRequirements] = None
    # Date and time at which the task starts. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    start_date_time: Optional[datetime] = None
    # Title of the task.
    title: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PlannerTask:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PlannerTask
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.businessScenarioTask":
                from . import business_scenario_task

                return business_scenario_task.BusinessScenarioTask()
        return PlannerTask()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import business_scenario_task, identity_set, planner_applied_categories, planner_assigned_to_task_board_task_format, planner_assignments, planner_bucket_task_board_task_format, planner_delta, planner_preview_type, planner_progress_task_board_task_format, planner_task_completion_requirements, planner_task_creation, planner_task_details, planner_task_recurrence

        fields: Dict[str, Callable[[Any], None]] = {
            "activeChecklistItemCount": lambda n : setattr(self, 'active_checklist_item_count', n.get_int_value()),
            "appliedCategories": lambda n : setattr(self, 'applied_categories', n.get_object_value(planner_applied_categories.PlannerAppliedCategories)),
            "assignedToTaskBoardFormat": lambda n : setattr(self, 'assigned_to_task_board_format', n.get_object_value(planner_assigned_to_task_board_task_format.PlannerAssignedToTaskBoardTaskFormat)),
            "assigneePriority": lambda n : setattr(self, 'assignee_priority', n.get_str_value()),
            "assignments": lambda n : setattr(self, 'assignments', n.get_object_value(planner_assignments.PlannerAssignments)),
            "bucketId": lambda n : setattr(self, 'bucket_id', n.get_str_value()),
            "bucketTaskBoardFormat": lambda n : setattr(self, 'bucket_task_board_format', n.get_object_value(planner_bucket_task_board_task_format.PlannerBucketTaskBoardTaskFormat)),
            "checklistItemCount": lambda n : setattr(self, 'checklist_item_count', n.get_int_value()),
            "completedBy": lambda n : setattr(self, 'completed_by', n.get_object_value(identity_set.IdentitySet)),
            "completedDateTime": lambda n : setattr(self, 'completed_date_time', n.get_datetime_value()),
            "conversationThreadId": lambda n : setattr(self, 'conversation_thread_id', n.get_str_value()),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(identity_set.IdentitySet)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "creationSource": lambda n : setattr(self, 'creation_source', n.get_object_value(planner_task_creation.PlannerTaskCreation)),
            "details": lambda n : setattr(self, 'details', n.get_object_value(planner_task_details.PlannerTaskDetails)),
            "dueDateTime": lambda n : setattr(self, 'due_date_time', n.get_datetime_value()),
            "hasDescription": lambda n : setattr(self, 'has_description', n.get_bool_value()),
            "orderHint": lambda n : setattr(self, 'order_hint', n.get_str_value()),
            "percentComplete": lambda n : setattr(self, 'percent_complete', n.get_int_value()),
            "planId": lambda n : setattr(self, 'plan_id', n.get_str_value()),
            "previewType": lambda n : setattr(self, 'preview_type', n.get_enum_value(planner_preview_type.PlannerPreviewType)),
            "priority": lambda n : setattr(self, 'priority', n.get_int_value()),
            "progressTaskBoardFormat": lambda n : setattr(self, 'progress_task_board_format', n.get_object_value(planner_progress_task_board_task_format.PlannerProgressTaskBoardTaskFormat)),
            "recurrence": lambda n : setattr(self, 'recurrence', n.get_object_value(planner_task_recurrence.PlannerTaskRecurrence)),
            "referenceCount": lambda n : setattr(self, 'reference_count', n.get_int_value()),
            "specifiedCompletionRequirements": lambda n : setattr(self, 'specified_completion_requirements', n.get_enum_value(planner_task_completion_requirements.PlannerTaskCompletionRequirements)),
            "startDateTime": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
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
        writer.write_int_value("activeChecklistItemCount", self.active_checklist_item_count)
        writer.write_object_value("appliedCategories", self.applied_categories)
        writer.write_object_value("assignedToTaskBoardFormat", self.assigned_to_task_board_format)
        writer.write_str_value("assigneePriority", self.assignee_priority)
        writer.write_object_value("assignments", self.assignments)
        writer.write_str_value("bucketId", self.bucket_id)
        writer.write_object_value("bucketTaskBoardFormat", self.bucket_task_board_format)
        writer.write_int_value("checklistItemCount", self.checklist_item_count)
        writer.write_object_value("completedBy", self.completed_by)
        writer.write_datetime_value("completedDateTime", self.completed_date_time)
        writer.write_str_value("conversationThreadId", self.conversation_thread_id)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("creationSource", self.creation_source)
        writer.write_object_value("details", self.details)
        writer.write_datetime_value("dueDateTime", self.due_date_time)
        writer.write_bool_value("hasDescription", self.has_description)
        writer.write_str_value("orderHint", self.order_hint)
        writer.write_int_value("percentComplete", self.percent_complete)
        writer.write_str_value("planId", self.plan_id)
        writer.write_enum_value("previewType", self.preview_type)
        writer.write_int_value("priority", self.priority)
        writer.write_object_value("progressTaskBoardFormat", self.progress_task_board_format)
        writer.write_object_value("recurrence", self.recurrence)
        writer.write_int_value("referenceCount", self.reference_count)
        writer.write_enum_value("specifiedCompletionRequirements", self.specified_completion_requirements)
        writer.write_datetime_value("startDateTime", self.start_date_time)
        writer.write_str_value("title", self.title)
    

