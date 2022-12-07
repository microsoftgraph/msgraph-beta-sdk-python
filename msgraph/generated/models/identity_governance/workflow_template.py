from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
lifecycle_workflow_category = lazy_import('msgraph.generated.models.identity_governance.lifecycle_workflow_category')
task = lazy_import('msgraph.generated.models.identity_governance.task')
workflow_execution_conditions = lazy_import('msgraph.generated.models.identity_governance.workflow_execution_conditions')

class WorkflowTemplate(entity.Entity):
    """
    Provides operations to manage the collection of accessReviewDecision entities.
    """
    @property
    def category(self,) -> Optional[lifecycle_workflow_category.LifecycleWorkflowCategory]:
        """
        Gets the category property value. The category property
        Returns: Optional[lifecycle_workflow_category.LifecycleWorkflowCategory]
        """
        return self._category
    
    @category.setter
    def category(self,value: Optional[lifecycle_workflow_category.LifecycleWorkflowCategory] = None) -> None:
        """
        Sets the category property value. The category property
        Args:
            value: Value to set for the category property.
        """
        self._category = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new workflowTemplate and sets the default values.
        """
        super().__init__()
        # The category property
        self._category: Optional[lifecycle_workflow_category.LifecycleWorkflowCategory] = None
        # The description of the workflowTemplate.
        self._description: Optional[str] = None
        # The display name of the workflowTemplate.Supports $filter(eq, ne) and $orderby.
        self._display_name: Optional[str] = None
        # Conditions describing when to execute the workflow and the criteria to identify in-scope subject set.
        self._execution_conditions: Optional[workflow_execution_conditions.WorkflowExecutionConditions] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Represents the configured tasks to execute and their execution sequence within a workflow. This relationship is expanded by default.
        self._tasks: Optional[List[task.Task]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WorkflowTemplate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WorkflowTemplate
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WorkflowTemplate()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. The description of the workflowTemplate.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. The description of the workflowTemplate.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The display name of the workflowTemplate.Supports $filter(eq, ne) and $orderby.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display name of the workflowTemplate.Supports $filter(eq, ne) and $orderby.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def execution_conditions(self,) -> Optional[workflow_execution_conditions.WorkflowExecutionConditions]:
        """
        Gets the executionConditions property value. Conditions describing when to execute the workflow and the criteria to identify in-scope subject set.
        Returns: Optional[workflow_execution_conditions.WorkflowExecutionConditions]
        """
        return self._execution_conditions
    
    @execution_conditions.setter
    def execution_conditions(self,value: Optional[workflow_execution_conditions.WorkflowExecutionConditions] = None) -> None:
        """
        Sets the executionConditions property value. Conditions describing when to execute the workflow and the criteria to identify in-scope subject set.
        Args:
            value: Value to set for the executionConditions property.
        """
        self._execution_conditions = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "category": lambda n : setattr(self, 'category', n.get_enum_value(lifecycle_workflow_category.LifecycleWorkflowCategory)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "execution_conditions": lambda n : setattr(self, 'execution_conditions', n.get_object_value(workflow_execution_conditions.WorkflowExecutionConditions)),
            "tasks": lambda n : setattr(self, 'tasks', n.get_collection_of_object_values(task.Task)),
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
        writer.write_enum_value("category", self.category)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("executionConditions", self.execution_conditions)
        writer.write_collection_of_object_values("tasks", self.tasks)
    
    @property
    def tasks(self,) -> Optional[List[task.Task]]:
        """
        Gets the tasks property value. Represents the configured tasks to execute and their execution sequence within a workflow. This relationship is expanded by default.
        Returns: Optional[List[task.Task]]
        """
        return self._tasks
    
    @tasks.setter
    def tasks(self,value: Optional[List[task.Task]] = None) -> None:
        """
        Sets the tasks property value. Represents the configured tasks to execute and their execution sequence within a workflow. This relationship is expanded by default.
        Args:
            value: Value to set for the tasks property.
        """
        self._tasks = value
    

