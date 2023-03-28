from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import planner_property_rule

from . import planner_property_rule

class PlannerBucketPropertyRule(planner_property_rule.PlannerPropertyRule):
    def __init__(self,) -> None:
        """
        Instantiates a new PlannerBucketPropertyRule and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.plannerBucketPropertyRule"
        # The order property
        self._order: Optional[List[str]] = None
        # The title property
        self._title: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PlannerBucketPropertyRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PlannerBucketPropertyRule
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PlannerBucketPropertyRule()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import planner_property_rule

        fields: Dict[str, Callable[[Any], None]] = {
            "order": lambda n : setattr(self, 'order', n.get_collection_of_primitive_values(str)),
            "title": lambda n : setattr(self, 'title', n.get_collection_of_primitive_values(str)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def order(self,) -> Optional[List[str]]:
        """
        Gets the order property value. The order property
        Returns: Optional[List[str]]
        """
        return self._order
    
    @order.setter
    def order(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the order property value. The order property
        Args:
            value: Value to set for the order property.
        """
        self._order = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_primitive_values("order", self.order)
        writer.write_collection_of_primitive_values("title", self.title)
    
    @property
    def title(self,) -> Optional[List[str]]:
        """
        Gets the title property value. The title property
        Returns: Optional[List[str]]
        """
        return self._title
    
    @title.setter
    def title(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the title property value. The title property
        Args:
            value: Value to set for the title property.
        """
        self._title = value
    

