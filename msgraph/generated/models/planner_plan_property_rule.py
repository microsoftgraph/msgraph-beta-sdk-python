from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import planner_field_rules, planner_property_rule

from . import planner_property_rule

class PlannerPlanPropertyRule(planner_property_rule.PlannerPropertyRule):
    def __init__(self,) -> None:
        """
        Instantiates a new PlannerPlanPropertyRule and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.plannerPlanPropertyRule"
        # The buckets property
        self._buckets: Optional[List[str]] = None
        # The categoryDescriptions property
        self._category_descriptions: Optional[planner_field_rules.PlannerFieldRules] = None
        # The tasks property
        self._tasks: Optional[List[str]] = None
        # The title property
        self._title: Optional[planner_field_rules.PlannerFieldRules] = None
    
    @property
    def buckets(self,) -> Optional[List[str]]:
        """
        Gets the buckets property value. The buckets property
        Returns: Optional[List[str]]
        """
        return self._buckets
    
    @buckets.setter
    def buckets(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the buckets property value. The buckets property
        Args:
            value: Value to set for the buckets property.
        """
        self._buckets = value
    
    @property
    def category_descriptions(self,) -> Optional[planner_field_rules.PlannerFieldRules]:
        """
        Gets the categoryDescriptions property value. The categoryDescriptions property
        Returns: Optional[planner_field_rules.PlannerFieldRules]
        """
        return self._category_descriptions
    
    @category_descriptions.setter
    def category_descriptions(self,value: Optional[planner_field_rules.PlannerFieldRules] = None) -> None:
        """
        Sets the categoryDescriptions property value. The categoryDescriptions property
        Args:
            value: Value to set for the category_descriptions property.
        """
        self._category_descriptions = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PlannerPlanPropertyRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PlannerPlanPropertyRule
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PlannerPlanPropertyRule()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import planner_field_rules, planner_property_rule

        fields: Dict[str, Callable[[Any], None]] = {
            "buckets": lambda n : setattr(self, 'buckets', n.get_collection_of_primitive_values(str)),
            "categoryDescriptions": lambda n : setattr(self, 'category_descriptions', n.get_object_value(planner_field_rules.PlannerFieldRules)),
            "tasks": lambda n : setattr(self, 'tasks', n.get_collection_of_primitive_values(str)),
            "title": lambda n : setattr(self, 'title', n.get_object_value(planner_field_rules.PlannerFieldRules)),
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
        writer.write_collection_of_primitive_values("buckets", self.buckets)
        writer.write_object_value("categoryDescriptions", self.category_descriptions)
        writer.write_collection_of_primitive_values("tasks", self.tasks)
        writer.write_object_value("title", self.title)
    
    @property
    def tasks(self,) -> Optional[List[str]]:
        """
        Gets the tasks property value. The tasks property
        Returns: Optional[List[str]]
        """
        return self._tasks
    
    @tasks.setter
    def tasks(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the tasks property value. The tasks property
        Args:
            value: Value to set for the tasks property.
        """
        self._tasks = value
    
    @property
    def title(self,) -> Optional[planner_field_rules.PlannerFieldRules]:
        """
        Gets the title property value. The title property
        Returns: Optional[planner_field_rules.PlannerFieldRules]
        """
        return self._title
    
    @title.setter
    def title(self,value: Optional[planner_field_rules.PlannerFieldRules] = None) -> None:
        """
        Sets the title property value. The title property
        Args:
            value: Value to set for the title property.
        """
        self._title = value
    

