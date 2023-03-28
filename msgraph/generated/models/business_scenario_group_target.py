from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import business_scenario_task_target_base

from . import business_scenario_task_target_base

class BusinessScenarioGroupTarget(business_scenario_task_target_base.BusinessScenarioTaskTargetBase):
    def __init__(self,) -> None:
        """
        Instantiates a new BusinessScenarioGroupTarget and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.businessScenarioGroupTarget"
        # The unique identifier for the group.
        self._group_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> BusinessScenarioGroupTarget:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: BusinessScenarioGroupTarget
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return BusinessScenarioGroupTarget()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import business_scenario_task_target_base

        fields: Dict[str, Callable[[Any], None]] = {
            "groupId": lambda n : setattr(self, 'group_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def group_id(self,) -> Optional[str]:
        """
        Gets the groupId property value. The unique identifier for the group.
        Returns: Optional[str]
        """
        return self._group_id
    
    @group_id.setter
    def group_id(self,value: Optional[str] = None) -> None:
        """
        Sets the groupId property value. The unique identifier for the group.
        Args:
            value: Value to set for the group_id property.
        """
        self._group_id = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("groupId", self.group_id)
    

