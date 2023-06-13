from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import item_body, planner_checklist_items, planner_delta, planner_external_references, planner_preview_type, planner_task_completion_requirement_details

from . import planner_delta

@dataclass
class PlannerTaskDetails(planner_delta.PlannerDelta):
    # The collection of checklist items on the task.
    checklist: Optional[planner_checklist_items.PlannerChecklistItems] = None
    # Contains detailed information about requirements on the task.
    completion_requirements: Optional[planner_task_completion_requirement_details.PlannerTaskCompletionRequirementDetails] = None
    # Description of the task.
    description: Optional[str] = None
    # Rich text description of the task. To be used by HTML-aware clients. For backwards compatibility, a plain-text version of the HTML description will be synced to the 'description' field. If this field has not previously been set but 'description' has been, the existing description will be synchronized to 'notes' with minimal whitespace-preserving HTML markup. Setting both 'description' and 'notes' is an error and will result in an exception.
    notes: Optional[item_body.ItemBody] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # This sets the type of preview that shows up on the task. Possible values are: automatic, noPreview, checklist, description, reference. When set to automatic the displayed preview is chosen by the app viewing the task.
    preview_type: Optional[planner_preview_type.PlannerPreviewType] = None
    # The collection of references on the task.
    references: Optional[planner_external_references.PlannerExternalReferences] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PlannerTaskDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PlannerTaskDetails
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PlannerTaskDetails()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import item_body, planner_checklist_items, planner_delta, planner_external_references, planner_preview_type, planner_task_completion_requirement_details

        fields: Dict[str, Callable[[Any], None]] = {
            "checklist": lambda n : setattr(self, 'checklist', n.get_object_value(planner_checklist_items.PlannerChecklistItems)),
            "completionRequirements": lambda n : setattr(self, 'completion_requirements', n.get_object_value(planner_task_completion_requirement_details.PlannerTaskCompletionRequirementDetails)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "notes": lambda n : setattr(self, 'notes', n.get_object_value(item_body.ItemBody)),
            "previewType": lambda n : setattr(self, 'preview_type', n.get_enum_value(planner_preview_type.PlannerPreviewType)),
            "references": lambda n : setattr(self, 'references', n.get_object_value(planner_external_references.PlannerExternalReferences)),
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
        writer.write_object_value("checklist", self.checklist)
        writer.write_object_value("completionRequirements", self.completion_requirements)
        writer.write_str_value("description", self.description)
        writer.write_object_value("notes", self.notes)
        writer.write_enum_value("previewType", self.preview_type)
        writer.write_object_value("references", self.references)
    

