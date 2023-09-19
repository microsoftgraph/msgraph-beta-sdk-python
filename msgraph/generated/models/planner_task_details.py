from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item_body import ItemBody
    from .planner_checklist_items import PlannerChecklistItems
    from .planner_delta import PlannerDelta
    from .planner_external_references import PlannerExternalReferences
    from .planner_preview_type import PlannerPreviewType
    from .planner_task_completion_requirement_details import PlannerTaskCompletionRequirementDetails

from .planner_delta import PlannerDelta

@dataclass
class PlannerTaskDetails(PlannerDelta):
    # The collection of checklist items on the task.
    checklist: Optional[PlannerChecklistItems] = None
    # Contains detailed information about requirements on the task.
    completion_requirements: Optional[PlannerTaskCompletionRequirementDetails] = None
    # Description of the task.
    description: Optional[str] = None
    # Rich text description of the task. To be used by HTML-aware clients. For backwards compatibility, a plain-text version of the HTML description will be synced to the 'description' field. If this field hasn't previously been set but 'description' has been, the existing description is synchronized to 'notes' with minimal whitespace-preserving HTML markup. Setting both 'description' and 'notes' is an error and will result in an exception.
    notes: Optional[ItemBody] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # This sets the type of preview that shows up on the task. Possible values are: automatic, noPreview, checklist, description, reference. When set to automatic the displayed preview is chosen by the app viewing the task.
    preview_type: Optional[PlannerPreviewType] = None
    # The collection of references on the task.
    references: Optional[PlannerExternalReferences] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PlannerTaskDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PlannerTaskDetails
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return PlannerTaskDetails()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .item_body import ItemBody
        from .planner_checklist_items import PlannerChecklistItems
        from .planner_delta import PlannerDelta
        from .planner_external_references import PlannerExternalReferences
        from .planner_preview_type import PlannerPreviewType
        from .planner_task_completion_requirement_details import PlannerTaskCompletionRequirementDetails

        from .item_body import ItemBody
        from .planner_checklist_items import PlannerChecklistItems
        from .planner_delta import PlannerDelta
        from .planner_external_references import PlannerExternalReferences
        from .planner_preview_type import PlannerPreviewType
        from .planner_task_completion_requirement_details import PlannerTaskCompletionRequirementDetails

        fields: Dict[str, Callable[[Any], None]] = {
            "checklist": lambda n : setattr(self, 'checklist', n.get_object_value(PlannerChecklistItems)),
            "completionRequirements": lambda n : setattr(self, 'completion_requirements', n.get_object_value(PlannerTaskCompletionRequirementDetails)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "notes": lambda n : setattr(self, 'notes', n.get_object_value(ItemBody)),
            "previewType": lambda n : setattr(self, 'preview_type', n.get_enum_value(PlannerPreviewType)),
            "references": lambda n : setattr(self, 'references', n.get_object_value(PlannerExternalReferences)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_object_value("checklist", self.checklist)
        writer.write_object_value("completionRequirements", self.completion_requirements)
        writer.write_str_value("description", self.description)
        writer.write_object_value("notes", self.notes)
        writer.write_enum_value("previewType", self.preview_type)
        writer.write_object_value("references", self.references)
    

