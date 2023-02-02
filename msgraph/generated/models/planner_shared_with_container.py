from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

planner_plan_access_level = lazy_import('msgraph.generated.models.planner_plan_access_level')
planner_plan_container = lazy_import('msgraph.generated.models.planner_plan_container')

class PlannerSharedWithContainer(planner_plan_container.PlannerPlanContainer):
    @property
    def access_level(self,) -> Optional[planner_plan_access_level.PlannerPlanAccessLevel]:
        """
        Gets the accessLevel property value. The accessLevel property
        Returns: Optional[planner_plan_access_level.PlannerPlanAccessLevel]
        """
        return self._access_level
    
    @access_level.setter
    def access_level(self,value: Optional[planner_plan_access_level.PlannerPlanAccessLevel] = None) -> None:
        """
        Sets the accessLevel property value. The accessLevel property
        Args:
            value: Value to set for the access_level property.
        """
        self._access_level = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new PlannerSharedWithContainer and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.plannerSharedWithContainer"
        # The accessLevel property
        self._access_level: Optional[planner_plan_access_level.PlannerPlanAccessLevel] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PlannerSharedWithContainer:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PlannerSharedWithContainer
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PlannerSharedWithContainer()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "accessLevel": lambda n : setattr(self, 'access_level', n.get_enum_value(planner_plan_access_level.PlannerPlanAccessLevel)),
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
        writer.write_enum_value("accessLevel", self.access_level)
    

