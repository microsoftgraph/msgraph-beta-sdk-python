from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
key_value_pair = lazy_import('msgraph.generated.models.key_value_pair')
lifecycle_task_category = lazy_import('msgraph.generated.models.identity_governance.lifecycle_task_category')
task_processing_result = lazy_import('msgraph.generated.models.identity_governance.task_processing_result')

class Task(entity.Entity):
    """
    Provides operations to manage the collection of accessReview entities.
    """
    @property
    def arguments(self,) -> Optional[List[key_value_pair.KeyValuePair]]:
        """
        Gets the arguments property value. Arguments included within the task.  For guidance to configure this property, see Configure the arguments for built-in Lifecycle Workflow tasks. Required.
        Returns: Optional[List[key_value_pair.KeyValuePair]]
        """
        return self._arguments
    
    @arguments.setter
    def arguments(self,value: Optional[List[key_value_pair.KeyValuePair]] = None) -> None:
        """
        Sets the arguments property value. Arguments included within the task.  For guidance to configure this property, see Configure the arguments for built-in Lifecycle Workflow tasks. Required.
        Args:
            value: Value to set for the arguments property.
        """
        self._arguments = value
    
    @property
    def category(self,) -> Optional[lifecycle_task_category.LifecycleTaskCategory]:
        """
        Gets the category property value. The category property
        Returns: Optional[lifecycle_task_category.LifecycleTaskCategory]
        """
        return self._category
    
    @category.setter
    def category(self,value: Optional[lifecycle_task_category.LifecycleTaskCategory] = None) -> None:
        """
        Sets the category property value. The category property
        Args:
            value: Value to set for the category property.
        """
        self._category = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new task and sets the default values.
        """
        super().__init__()
        # Arguments included within the task.  For guidance to configure this property, see Configure the arguments for built-in Lifecycle Workflow tasks. Required.
        self._arguments: Optional[List[key_value_pair.KeyValuePair]] = None
        # The category property
        self._category: Optional[lifecycle_task_category.LifecycleTaskCategory] = None
        # A boolean value that specifies whether, if this task fails, the workflow will stop, and subsequent tasks will not run. Optional.
        self._continue_on_error: Optional[bool] = None
        # A string that describes the purpose of the task for administrative use. Optional.
        self._description: Optional[str] = None
        # A unique string that identifies the task. Required.Supports $filter(eq, ne) and orderBy.
        self._display_name: Optional[str] = None
        # An integer that states in what order the task will run in a workflow.Supports $orderby.
        self._execution_sequence: Optional[int] = None
        # A boolean value that denotes whether the task is set to run or not. Optional.Supports $filter(eq, ne) and orderBy.
        self._is_enabled: Optional[bool] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # A unique template identifier for the task. For more information about the tasks that Lifecycle Workflows currently supports and their unique identifiers, see supported tasks. Required.Supports $filter(eq, ne).
        self._task_definition_id: Optional[str] = None
        # The result of processing the task.
        self._task_processing_results: Optional[List[task_processing_result.TaskProcessingResult]] = None
    
    @property
    def continue_on_error(self,) -> Optional[bool]:
        """
        Gets the continueOnError property value. A boolean value that specifies whether, if this task fails, the workflow will stop, and subsequent tasks will not run. Optional.
        Returns: Optional[bool]
        """
        return self._continue_on_error
    
    @continue_on_error.setter
    def continue_on_error(self,value: Optional[bool] = None) -> None:
        """
        Sets the continueOnError property value. A boolean value that specifies whether, if this task fails, the workflow will stop, and subsequent tasks will not run. Optional.
        Args:
            value: Value to set for the continueOnError property.
        """
        self._continue_on_error = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Task:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Task
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Task()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. A string that describes the purpose of the task for administrative use. Optional.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. A string that describes the purpose of the task for administrative use. Optional.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. A unique string that identifies the task. Required.Supports $filter(eq, ne) and orderBy.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. A unique string that identifies the task. Required.Supports $filter(eq, ne) and orderBy.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def execution_sequence(self,) -> Optional[int]:
        """
        Gets the executionSequence property value. An integer that states in what order the task will run in a workflow.Supports $orderby.
        Returns: Optional[int]
        """
        return self._execution_sequence
    
    @execution_sequence.setter
    def execution_sequence(self,value: Optional[int] = None) -> None:
        """
        Sets the executionSequence property value. An integer that states in what order the task will run in a workflow.Supports $orderby.
        Args:
            value: Value to set for the executionSequence property.
        """
        self._execution_sequence = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "arguments": lambda n : setattr(self, 'arguments', n.get_collection_of_object_values(key_value_pair.KeyValuePair)),
            "category": lambda n : setattr(self, 'category', n.get_enum_value(lifecycle_task_category.LifecycleTaskCategory)),
            "continue_on_error": lambda n : setattr(self, 'continue_on_error', n.get_bool_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "execution_sequence": lambda n : setattr(self, 'execution_sequence', n.get_int_value()),
            "is_enabled": lambda n : setattr(self, 'is_enabled', n.get_bool_value()),
            "task_definition_id": lambda n : setattr(self, 'task_definition_id', n.get_str_value()),
            "task_processing_results": lambda n : setattr(self, 'task_processing_results', n.get_collection_of_object_values(task_processing_result.TaskProcessingResult)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_enabled(self,) -> Optional[bool]:
        """
        Gets the isEnabled property value. A boolean value that denotes whether the task is set to run or not. Optional.Supports $filter(eq, ne) and orderBy.
        Returns: Optional[bool]
        """
        return self._is_enabled
    
    @is_enabled.setter
    def is_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isEnabled property value. A boolean value that denotes whether the task is set to run or not. Optional.Supports $filter(eq, ne) and orderBy.
        Args:
            value: Value to set for the isEnabled property.
        """
        self._is_enabled = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("arguments", self.arguments)
        writer.write_enum_value("category", self.category)
        writer.write_bool_value("continueOnError", self.continue_on_error)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_int_value("executionSequence", self.execution_sequence)
        writer.write_bool_value("isEnabled", self.is_enabled)
        writer.write_str_value("taskDefinitionId", self.task_definition_id)
        writer.write_collection_of_object_values("taskProcessingResults", self.task_processing_results)
    
    @property
    def task_definition_id(self,) -> Optional[str]:
        """
        Gets the taskDefinitionId property value. A unique template identifier for the task. For more information about the tasks that Lifecycle Workflows currently supports and their unique identifiers, see supported tasks. Required.Supports $filter(eq, ne).
        Returns: Optional[str]
        """
        return self._task_definition_id
    
    @task_definition_id.setter
    def task_definition_id(self,value: Optional[str] = None) -> None:
        """
        Sets the taskDefinitionId property value. A unique template identifier for the task. For more information about the tasks that Lifecycle Workflows currently supports and their unique identifiers, see supported tasks. Required.Supports $filter(eq, ne).
        Args:
            value: Value to set for the taskDefinitionId property.
        """
        self._task_definition_id = value
    
    @property
    def task_processing_results(self,) -> Optional[List[task_processing_result.TaskProcessingResult]]:
        """
        Gets the taskProcessingResults property value. The result of processing the task.
        Returns: Optional[List[task_processing_result.TaskProcessingResult]]
        """
        return self._task_processing_results
    
    @task_processing_results.setter
    def task_processing_results(self,value: Optional[List[task_processing_result.TaskProcessingResult]] = None) -> None:
        """
        Sets the taskProcessingResults property value. The result of processing the task.
        Args:
            value: Value to set for the taskProcessingResults property.
        """
        self._task_processing_results = value
    

