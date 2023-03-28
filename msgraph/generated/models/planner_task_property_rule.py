from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import planner_field_rules, planner_property_rule

from . import planner_property_rule

class PlannerTaskPropertyRule(planner_property_rule.PlannerPropertyRule):
    def __init__(self,) -> None:
        """
        Instantiates a new PlannerTaskPropertyRule and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.plannerTaskPropertyRule"
        # Rules and restrictions for applied categories. This value does not currently support overrides. Accepted values for the default rule and individual overrides are allow, block.
        self._applied_categories: Optional[planner_field_rules.PlannerFieldRules] = None
        # Rules and restrictions for assignments. Allowed overrides are userCreated and applicationCreated. Accepted values for the default rule and individual overrides are allow, add, addSelf, addOther, remove, removeSelf, removeOther, block.
        self._assignments: Optional[planner_field_rules.PlannerFieldRules] = None
        # Rules and restrictions for checklist. Allowed overrides are userCreated and applicationCreated. Accepted values for the default rule and individual overrides are allow, add, remove, update, check, reorder, block.
        self._check_lists: Optional[planner_field_rules.PlannerFieldRules] = None
        # Rules and restrictions for deleting the task. Accepted values are allow and block.
        self._delete: Optional[List[str]] = None
        # Rules and restrictions for changing the due date of the task. Accepted values are allow and block.
        self._due_date: Optional[List[str]] = None
        # Rules and restrictions for moving the task between buckets or plans. Accepted values are allow, moveBetweenPlans, moveBetweenBuckets, and block.
        self._move: Optional[List[str]] = None
        # Rules and restrictions for changing the notes of the task. Accepted values are allow and block.
        self._notes: Optional[List[str]] = None
        # Rules and restrictions for changing the order of the task. Accepted values are allow and block.
        self._order: Optional[List[str]] = None
        # Rules and restrictions for changing the completion percentage of the task. Accepted values are allow, setToComplete, setToNotStarted, setToInProgress, and block.
        self._percent_complete: Optional[List[str]] = None
        # Rules and restrictions for changing the preview type of the task. Accepted values are allow and block.
        self._preview_type: Optional[List[str]] = None
        # Rules and restrictions for changing the priority of the task. Accepted values are allow and block.
        self._priority: Optional[List[str]] = None
        # Rules and restrictions for references. Allowed overrides are userCreated and applicationCreated. Accepted values for the default rule and individual overrides are allow, add, remove, block.
        self._references: Optional[planner_field_rules.PlannerFieldRules] = None
        # Rules and restrictions for changing the start date of the task. Accepted values are allow and block.
        self._start_date: Optional[List[str]] = None
        # Rules and restrictions for changing the title of the task. Accepted values are allow and block.
        self._title: Optional[List[str]] = None
    
    @property
    def applied_categories(self,) -> Optional[planner_field_rules.PlannerFieldRules]:
        """
        Gets the appliedCategories property value. Rules and restrictions for applied categories. This value does not currently support overrides. Accepted values for the default rule and individual overrides are allow, block.
        Returns: Optional[planner_field_rules.PlannerFieldRules]
        """
        return self._applied_categories
    
    @applied_categories.setter
    def applied_categories(self,value: Optional[planner_field_rules.PlannerFieldRules] = None) -> None:
        """
        Sets the appliedCategories property value. Rules and restrictions for applied categories. This value does not currently support overrides. Accepted values for the default rule and individual overrides are allow, block.
        Args:
            value: Value to set for the applied_categories property.
        """
        self._applied_categories = value
    
    @property
    def assignments(self,) -> Optional[planner_field_rules.PlannerFieldRules]:
        """
        Gets the assignments property value. Rules and restrictions for assignments. Allowed overrides are userCreated and applicationCreated. Accepted values for the default rule and individual overrides are allow, add, addSelf, addOther, remove, removeSelf, removeOther, block.
        Returns: Optional[planner_field_rules.PlannerFieldRules]
        """
        return self._assignments
    
    @assignments.setter
    def assignments(self,value: Optional[planner_field_rules.PlannerFieldRules] = None) -> None:
        """
        Sets the assignments property value. Rules and restrictions for assignments. Allowed overrides are userCreated and applicationCreated. Accepted values for the default rule and individual overrides are allow, add, addSelf, addOther, remove, removeSelf, removeOther, block.
        Args:
            value: Value to set for the assignments property.
        """
        self._assignments = value
    
    @property
    def check_lists(self,) -> Optional[planner_field_rules.PlannerFieldRules]:
        """
        Gets the checkLists property value. Rules and restrictions for checklist. Allowed overrides are userCreated and applicationCreated. Accepted values for the default rule and individual overrides are allow, add, remove, update, check, reorder, block.
        Returns: Optional[planner_field_rules.PlannerFieldRules]
        """
        return self._check_lists
    
    @check_lists.setter
    def check_lists(self,value: Optional[planner_field_rules.PlannerFieldRules] = None) -> None:
        """
        Sets the checkLists property value. Rules and restrictions for checklist. Allowed overrides are userCreated and applicationCreated. Accepted values for the default rule and individual overrides are allow, add, remove, update, check, reorder, block.
        Args:
            value: Value to set for the check_lists property.
        """
        self._check_lists = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PlannerTaskPropertyRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PlannerTaskPropertyRule
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PlannerTaskPropertyRule()
    
    @property
    def delete(self,) -> Optional[List[str]]:
        """
        Gets the delete property value. Rules and restrictions for deleting the task. Accepted values are allow and block.
        Returns: Optional[List[str]]
        """
        return self._delete
    
    @delete.setter
    def delete(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the delete property value. Rules and restrictions for deleting the task. Accepted values are allow and block.
        Args:
            value: Value to set for the delete property.
        """
        self._delete = value
    
    @property
    def due_date(self,) -> Optional[List[str]]:
        """
        Gets the dueDate property value. Rules and restrictions for changing the due date of the task. Accepted values are allow and block.
        Returns: Optional[List[str]]
        """
        return self._due_date
    
    @due_date.setter
    def due_date(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the dueDate property value. Rules and restrictions for changing the due date of the task. Accepted values are allow and block.
        Args:
            value: Value to set for the due_date property.
        """
        self._due_date = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import planner_field_rules, planner_property_rule

        fields: Dict[str, Callable[[Any], None]] = {
            "appliedCategories": lambda n : setattr(self, 'applied_categories', n.get_object_value(planner_field_rules.PlannerFieldRules)),
            "assignments": lambda n : setattr(self, 'assignments', n.get_object_value(planner_field_rules.PlannerFieldRules)),
            "checkLists": lambda n : setattr(self, 'check_lists', n.get_object_value(planner_field_rules.PlannerFieldRules)),
            "delete": lambda n : setattr(self, 'delete', n.get_collection_of_primitive_values(str)),
            "dueDate": lambda n : setattr(self, 'due_date', n.get_collection_of_primitive_values(str)),
            "move": lambda n : setattr(self, 'move', n.get_collection_of_primitive_values(str)),
            "notes": lambda n : setattr(self, 'notes', n.get_collection_of_primitive_values(str)),
            "order": lambda n : setattr(self, 'order', n.get_collection_of_primitive_values(str)),
            "percentComplete": lambda n : setattr(self, 'percent_complete', n.get_collection_of_primitive_values(str)),
            "previewType": lambda n : setattr(self, 'preview_type', n.get_collection_of_primitive_values(str)),
            "priority": lambda n : setattr(self, 'priority', n.get_collection_of_primitive_values(str)),
            "references": lambda n : setattr(self, 'references', n.get_object_value(planner_field_rules.PlannerFieldRules)),
            "startDate": lambda n : setattr(self, 'start_date', n.get_collection_of_primitive_values(str)),
            "title": lambda n : setattr(self, 'title', n.get_collection_of_primitive_values(str)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def move(self,) -> Optional[List[str]]:
        """
        Gets the move property value. Rules and restrictions for moving the task between buckets or plans. Accepted values are allow, moveBetweenPlans, moveBetweenBuckets, and block.
        Returns: Optional[List[str]]
        """
        return self._move
    
    @move.setter
    def move(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the move property value. Rules and restrictions for moving the task between buckets or plans. Accepted values are allow, moveBetweenPlans, moveBetweenBuckets, and block.
        Args:
            value: Value to set for the move property.
        """
        self._move = value
    
    @property
    def notes(self,) -> Optional[List[str]]:
        """
        Gets the notes property value. Rules and restrictions for changing the notes of the task. Accepted values are allow and block.
        Returns: Optional[List[str]]
        """
        return self._notes
    
    @notes.setter
    def notes(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the notes property value. Rules and restrictions for changing the notes of the task. Accepted values are allow and block.
        Args:
            value: Value to set for the notes property.
        """
        self._notes = value
    
    @property
    def order(self,) -> Optional[List[str]]:
        """
        Gets the order property value. Rules and restrictions for changing the order of the task. Accepted values are allow and block.
        Returns: Optional[List[str]]
        """
        return self._order
    
    @order.setter
    def order(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the order property value. Rules and restrictions for changing the order of the task. Accepted values are allow and block.
        Args:
            value: Value to set for the order property.
        """
        self._order = value
    
    @property
    def percent_complete(self,) -> Optional[List[str]]:
        """
        Gets the percentComplete property value. Rules and restrictions for changing the completion percentage of the task. Accepted values are allow, setToComplete, setToNotStarted, setToInProgress, and block.
        Returns: Optional[List[str]]
        """
        return self._percent_complete
    
    @percent_complete.setter
    def percent_complete(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the percentComplete property value. Rules and restrictions for changing the completion percentage of the task. Accepted values are allow, setToComplete, setToNotStarted, setToInProgress, and block.
        Args:
            value: Value to set for the percent_complete property.
        """
        self._percent_complete = value
    
    @property
    def preview_type(self,) -> Optional[List[str]]:
        """
        Gets the previewType property value. Rules and restrictions for changing the preview type of the task. Accepted values are allow and block.
        Returns: Optional[List[str]]
        """
        return self._preview_type
    
    @preview_type.setter
    def preview_type(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the previewType property value. Rules and restrictions for changing the preview type of the task. Accepted values are allow and block.
        Args:
            value: Value to set for the preview_type property.
        """
        self._preview_type = value
    
    @property
    def priority(self,) -> Optional[List[str]]:
        """
        Gets the priority property value. Rules and restrictions for changing the priority of the task. Accepted values are allow and block.
        Returns: Optional[List[str]]
        """
        return self._priority
    
    @priority.setter
    def priority(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the priority property value. Rules and restrictions for changing the priority of the task. Accepted values are allow and block.
        Args:
            value: Value to set for the priority property.
        """
        self._priority = value
    
    @property
    def references(self,) -> Optional[planner_field_rules.PlannerFieldRules]:
        """
        Gets the references property value. Rules and restrictions for references. Allowed overrides are userCreated and applicationCreated. Accepted values for the default rule and individual overrides are allow, add, remove, block.
        Returns: Optional[planner_field_rules.PlannerFieldRules]
        """
        return self._references
    
    @references.setter
    def references(self,value: Optional[planner_field_rules.PlannerFieldRules] = None) -> None:
        """
        Sets the references property value. Rules and restrictions for references. Allowed overrides are userCreated and applicationCreated. Accepted values for the default rule and individual overrides are allow, add, remove, block.
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
        writer.write_object_value("appliedCategories", self.applied_categories)
        writer.write_object_value("assignments", self.assignments)
        writer.write_object_value("checkLists", self.check_lists)
        writer.write_collection_of_primitive_values("delete", self.delete)
        writer.write_collection_of_primitive_values("dueDate", self.due_date)
        writer.write_collection_of_primitive_values("move", self.move)
        writer.write_collection_of_primitive_values("notes", self.notes)
        writer.write_collection_of_primitive_values("order", self.order)
        writer.write_collection_of_primitive_values("percentComplete", self.percent_complete)
        writer.write_collection_of_primitive_values("previewType", self.preview_type)
        writer.write_collection_of_primitive_values("priority", self.priority)
        writer.write_object_value("references", self.references)
        writer.write_collection_of_primitive_values("startDate", self.start_date)
        writer.write_collection_of_primitive_values("title", self.title)
    
    @property
    def start_date(self,) -> Optional[List[str]]:
        """
        Gets the startDate property value. Rules and restrictions for changing the start date of the task. Accepted values are allow and block.
        Returns: Optional[List[str]]
        """
        return self._start_date
    
    @start_date.setter
    def start_date(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the startDate property value. Rules and restrictions for changing the start date of the task. Accepted values are allow and block.
        Args:
            value: Value to set for the start_date property.
        """
        self._start_date = value
    
    @property
    def title(self,) -> Optional[List[str]]:
        """
        Gets the title property value. Rules and restrictions for changing the title of the task. Accepted values are allow and block.
        Returns: Optional[List[str]]
        """
        return self._title
    
    @title.setter
    def title(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the title property value. Rules and restrictions for changing the title of the task. Accepted values are allow and block.
        Args:
            value: Value to set for the title property.
        """
        self._title = value
    

