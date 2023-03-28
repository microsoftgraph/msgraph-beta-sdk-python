from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import item_body, planner_checklist_items, planner_delta, planner_external_references, planner_preview_type

from . import planner_delta

class PlannerTaskDetails(planner_delta.PlannerDelta):
    def __init__(self,) -> None:
        """
        Instantiates a new plannerTaskDetails and sets the default values.
        """
        super().__init__()
        # The collection of checklist items on the task.
        self._checklist: Optional[planner_checklist_items.PlannerChecklistItems] = None
        # Description of the task.
        self._description: Optional[str] = None
        # Rich text description of the task. To be used by HTML-aware clients. For backwards compatibility, a plain-text version of the HTML description will be synced to the 'description' field. If this field has not previously been set but 'description' has been, the existing description will be synchronized to 'notes' with minimal whitespace-preserving HTML markup. Setting both 'description' and 'notes' is an error and will result in an exception.
        self._notes: Optional[item_body.ItemBody] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # This sets the type of preview that shows up on the task. Possible values are: automatic, noPreview, checklist, description, reference. When set to automatic the displayed preview is chosen by the app viewing the task.
        self._preview_type: Optional[planner_preview_type.PlannerPreviewType] = None
        # The collection of references on the task.
        self._references: Optional[planner_external_references.PlannerExternalReferences] = None
    
    @property
    def checklist(self,) -> Optional[planner_checklist_items.PlannerChecklistItems]:
        """
        Gets the checklist property value. The collection of checklist items on the task.
        Returns: Optional[planner_checklist_items.PlannerChecklistItems]
        """
        return self._checklist
    
    @checklist.setter
    def checklist(self,value: Optional[planner_checklist_items.PlannerChecklistItems] = None) -> None:
        """
        Sets the checklist property value. The collection of checklist items on the task.
        Args:
            value: Value to set for the checklist property.
        """
        self._checklist = value
    
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
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. Description of the task.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. Description of the task.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import item_body, planner_checklist_items, planner_delta, planner_external_references, planner_preview_type

        fields: Dict[str, Callable[[Any], None]] = {
            "checklist": lambda n : setattr(self, 'checklist', n.get_object_value(planner_checklist_items.PlannerChecklistItems)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "notes": lambda n : setattr(self, 'notes', n.get_object_value(item_body.ItemBody)),
            "previewType": lambda n : setattr(self, 'preview_type', n.get_enum_value(planner_preview_type.PlannerPreviewType)),
            "references": lambda n : setattr(self, 'references', n.get_object_value(planner_external_references.PlannerExternalReferences)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def notes(self,) -> Optional[item_body.ItemBody]:
        """
        Gets the notes property value. Rich text description of the task. To be used by HTML-aware clients. For backwards compatibility, a plain-text version of the HTML description will be synced to the 'description' field. If this field has not previously been set but 'description' has been, the existing description will be synchronized to 'notes' with minimal whitespace-preserving HTML markup. Setting both 'description' and 'notes' is an error and will result in an exception.
        Returns: Optional[item_body.ItemBody]
        """
        return self._notes
    
    @notes.setter
    def notes(self,value: Optional[item_body.ItemBody] = None) -> None:
        """
        Sets the notes property value. Rich text description of the task. To be used by HTML-aware clients. For backwards compatibility, a plain-text version of the HTML description will be synced to the 'description' field. If this field has not previously been set but 'description' has been, the existing description will be synchronized to 'notes' with minimal whitespace-preserving HTML markup. Setting both 'description' and 'notes' is an error and will result in an exception.
        Args:
            value: Value to set for the notes property.
        """
        self._notes = value
    
    @property
    def preview_type(self,) -> Optional[planner_preview_type.PlannerPreviewType]:
        """
        Gets the previewType property value. This sets the type of preview that shows up on the task. Possible values are: automatic, noPreview, checklist, description, reference. When set to automatic the displayed preview is chosen by the app viewing the task.
        Returns: Optional[planner_preview_type.PlannerPreviewType]
        """
        return self._preview_type
    
    @preview_type.setter
    def preview_type(self,value: Optional[planner_preview_type.PlannerPreviewType] = None) -> None:
        """
        Sets the previewType property value. This sets the type of preview that shows up on the task. Possible values are: automatic, noPreview, checklist, description, reference. When set to automatic the displayed preview is chosen by the app viewing the task.
        Args:
            value: Value to set for the preview_type property.
        """
        self._preview_type = value
    
    @property
    def references(self,) -> Optional[planner_external_references.PlannerExternalReferences]:
        """
        Gets the references property value. The collection of references on the task.
        Returns: Optional[planner_external_references.PlannerExternalReferences]
        """
        return self._references
    
    @references.setter
    def references(self,value: Optional[planner_external_references.PlannerExternalReferences] = None) -> None:
        """
        Sets the references property value. The collection of references on the task.
        Args:
            value: Value to set for the references property.
        """
        self._references = value
    
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
        writer.write_str_value("description", self.description)
        writer.write_object_value("notes", self.notes)
        writer.write_enum_value("previewType", self.preview_type)
        writer.write_object_value("references", self.references)
    

