from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, planner_plan, planner_roster_member

from . import entity

@dataclass
class PlannerRoster(entity.Entity):
    # Retrieves the members of the plannerRoster.
    members: Optional[List[planner_roster_member.PlannerRosterMember]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Retrieves the plans contained by the plannerRoster.
    plans: Optional[List[planner_plan.PlannerPlan]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PlannerRoster:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
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
        from . import entity, planner_plan, planner_roster_member

        from . import entity, planner_plan, planner_roster_member

        fields: Dict[str, Callable[[Any], None]] = {
            "members": lambda n : setattr(self, 'members', n.get_collection_of_object_values(planner_roster_member.PlannerRosterMember)),
            "plans": lambda n : setattr(self, 'plans', n.get_collection_of_object_values(planner_plan.PlannerPlan)),
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
        writer.write_collection_of_object_values("members", self.members)
        writer.write_collection_of_object_values("plans", self.plans)
    

