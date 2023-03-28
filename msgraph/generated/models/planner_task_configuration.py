from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, planner_task_policy

from . import entity

class PlannerTaskConfiguration(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new plannerTaskConfiguration and sets the default values.
        """
        super().__init__()
        # Policy configuration for tasks created for the businessScenario when they are being changed outside of the scenario.
        self._edit_policy: Optional[planner_task_policy.PlannerTaskPolicy] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PlannerTaskConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PlannerTaskConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PlannerTaskConfiguration()
    
    @property
    def edit_policy(self,) -> Optional[planner_task_policy.PlannerTaskPolicy]:
        """
        Gets the editPolicy property value. Policy configuration for tasks created for the businessScenario when they are being changed outside of the scenario.
        Returns: Optional[planner_task_policy.PlannerTaskPolicy]
        """
        return self._edit_policy
    
    @edit_policy.setter
    def edit_policy(self,value: Optional[planner_task_policy.PlannerTaskPolicy] = None) -> None:
        """
        Sets the editPolicy property value. Policy configuration for tasks created for the businessScenario when they are being changed outside of the scenario.
        Args:
            value: Value to set for the edit_policy property.
        """
        self._edit_policy = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, planner_task_policy

        fields: Dict[str, Callable[[Any], None]] = {
            "editPolicy": lambda n : setattr(self, 'edit_policy', n.get_object_value(planner_task_policy.PlannerTaskPolicy)),
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
        writer.write_object_value("editPolicy", self.edit_policy)
    

