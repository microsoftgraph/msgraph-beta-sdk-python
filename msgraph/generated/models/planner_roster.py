from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, planner_plan, planner_roster_member

from . import entity

class PlannerRoster(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new PlannerRoster and sets the default values.
        """
        super().__init__()
        # Retrieves the members of the plannerRoster.
        self._members: Optional[List[planner_roster_member.PlannerRosterMember]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Retrieves the plans contained by the plannerRoster.
        self._plans: Optional[List[planner_plan.PlannerPlan]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PlannerRoster:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PlannerRoster
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PlannerRoster()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, planner_plan, planner_roster_member

        fields: Dict[str, Callable[[Any], None]] = {
            "members": lambda n : setattr(self, 'members', n.get_collection_of_object_values(planner_roster_member.PlannerRosterMember)),
            "plans": lambda n : setattr(self, 'plans', n.get_collection_of_object_values(planner_plan.PlannerPlan)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def members(self,) -> Optional[List[planner_roster_member.PlannerRosterMember]]:
        """
        Gets the members property value. Retrieves the members of the plannerRoster.
        Returns: Optional[List[planner_roster_member.PlannerRosterMember]]
        """
        return self._members
    
    @members.setter
    def members(self,value: Optional[List[planner_roster_member.PlannerRosterMember]] = None) -> None:
        """
        Sets the members property value. Retrieves the members of the plannerRoster.
        Args:
            value: Value to set for the members property.
        """
        self._members = value
    
    @property
    def plans(self,) -> Optional[List[planner_plan.PlannerPlan]]:
        """
        Gets the plans property value. Retrieves the plans contained by the plannerRoster.
        Returns: Optional[List[planner_plan.PlannerPlan]]
        """
        return self._plans
    
    @plans.setter
    def plans(self,value: Optional[List[planner_plan.PlannerPlan]] = None) -> None:
        """
        Sets the plans property value. Retrieves the plans contained by the plannerRoster.
        Args:
            value: Value to set for the plans property.
        """
        self._plans = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("members", self.members)
        writer.write_collection_of_object_values("plans", self.plans)
    

