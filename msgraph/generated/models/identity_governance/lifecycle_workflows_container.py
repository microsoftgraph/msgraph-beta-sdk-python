from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import custom_task_extension, lifecycle_management_settings, task_definition, workflow, workflow_template
    from .. import deleted_item_container, entity

from .. import entity

@dataclass
class LifecycleWorkflowsContainer(entity.Entity):
    # The customTaskExtension instance.
    custom_task_extensions: Optional[List[custom_task_extension.CustomTaskExtension]] = None
    # Deleted workflows in your lifecycle workflows instance.
    deleted_items: Optional[deleted_item_container.DeletedItemContainer] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The settings property
    settings: Optional[lifecycle_management_settings.LifecycleManagementSettings] = None
    # The definition of tasks within the lifecycle workflows instance.
    task_definitions: Optional[List[task_definition.TaskDefinition]] = None
    # The workflow templates in the lifecycle workflow instance.
    workflow_templates: Optional[List[workflow_template.WorkflowTemplate]] = None
    # The workflows in the lifecycle workflows instance.
    workflows: Optional[List[workflow.Workflow]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> LifecycleWorkflowsContainer:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: LifecycleWorkflowsContainer
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return LifecycleWorkflowsContainer()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import custom_task_extension, lifecycle_management_settings, task_definition, workflow, workflow_template
        from .. import deleted_item_container, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "customTaskExtensions": lambda n : setattr(self, 'custom_task_extensions', n.get_collection_of_object_values(custom_task_extension.CustomTaskExtension)),
            "deletedItems": lambda n : setattr(self, 'deleted_items', n.get_object_value(deleted_item_container.DeletedItemContainer)),
            "settings": lambda n : setattr(self, 'settings', n.get_object_value(lifecycle_management_settings.LifecycleManagementSettings)),
            "taskDefinitions": lambda n : setattr(self, 'task_definitions', n.get_collection_of_object_values(task_definition.TaskDefinition)),
            "workflows": lambda n : setattr(self, 'workflows', n.get_collection_of_object_values(workflow.Workflow)),
            "workflowTemplates": lambda n : setattr(self, 'workflow_templates', n.get_collection_of_object_values(workflow_template.WorkflowTemplate)),
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
        writer.write_collection_of_object_values("customTaskExtensions", self.custom_task_extensions)
        writer.write_object_value("deletedItems", self.deleted_items)
        writer.write_object_value("settings", self.settings)
        writer.write_collection_of_object_values("taskDefinitions", self.task_definitions)
        writer.write_collection_of_object_values("workflows", self.workflows)
        writer.write_collection_of_object_values("workflowTemplates", self.workflow_templates)
    

