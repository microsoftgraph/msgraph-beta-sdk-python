from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .planner_plan import PlannerPlan
    from .planner_roster_member import PlannerRosterMember
    from .sensitivity_label_assignment import SensitivityLabelAssignment

from .entity import Entity

@dataclass
class PlannerRoster(Entity):
    # The assignedSensitivityLabel property
    assigned_sensitivity_label: Optional[SensitivityLabelAssignment] = None
    # Retrieves the members of the plannerRoster.
    members: Optional[List[PlannerRosterMember]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Retrieves the plans contained by the plannerRoster.
    plans: Optional[List[PlannerPlan]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PlannerRoster:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PlannerRoster
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return PlannerRoster()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .planner_plan import PlannerPlan
        from .planner_roster_member import PlannerRosterMember
        from .sensitivity_label_assignment import SensitivityLabelAssignment

        from .entity import Entity
        from .planner_plan import PlannerPlan
        from .planner_roster_member import PlannerRosterMember
        from .sensitivity_label_assignment import SensitivityLabelAssignment

        fields: Dict[str, Callable[[Any], None]] = {
            "assignedSensitivityLabel": lambda n : setattr(self, 'assigned_sensitivity_label', n.get_object_value(SensitivityLabelAssignment)),
            "members": lambda n : setattr(self, 'members', n.get_collection_of_object_values(PlannerRosterMember)),
            "plans": lambda n : setattr(self, 'plans', n.get_collection_of_object_values(PlannerPlan)),
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
        writer.write_object_value("assignedSensitivityLabel", self.assigned_sensitivity_label)
        writer.write_collection_of_object_values("members", self.members)
        writer.write_collection_of_object_values("plans", self.plans)
    

