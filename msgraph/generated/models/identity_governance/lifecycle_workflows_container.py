from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

deleted_item_container = lazy_import('msgraph.generated.models.deleted_item_container')
entity = lazy_import('msgraph.generated.models.entity')
custom_task_extension = lazy_import('msgraph.generated.models.identity_governance.custom_task_extension')
lifecycle_management_settings = lazy_import('msgraph.generated.models.identity_governance.lifecycle_management_settings')
task_definition = lazy_import('msgraph.generated.models.identity_governance.task_definition')
workflow = lazy_import('msgraph.generated.models.identity_governance.workflow')
workflow_template = lazy_import('msgraph.generated.models.identity_governance.workflow_template')

class LifecycleWorkflowsContainer(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new LifecycleWorkflowsContainer and sets the default values.
        """
        super().__init__()
        # The customTaskExtension instance.
        self._custom_task_extensions: Optional[List[custom_task_extension.CustomTaskExtension]] = None
        # Deleted workflows in your lifecycle workflows instance.
        self._deleted_items: Optional[deleted_item_container.DeletedItemContainer] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The settings property
        self._settings: Optional[lifecycle_management_settings.LifecycleManagementSettings] = None
        # The definition of tasks within the lifecycle workflows instance.
        self._task_definitions: Optional[List[task_definition.TaskDefinition]] = None
        # The workflows in the lifecycle workflows instance.
        self._workflows: Optional[List[workflow.Workflow]] = None
        # The workflow templates in the lifecycle workflow instance.
        self._workflow_templates: Optional[List[workflow_template.WorkflowTemplate]] = None
    
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
    
    @property
    def custom_task_extensions(self,) -> Optional[List[custom_task_extension.CustomTaskExtension]]:
        """
        Gets the customTaskExtensions property value. The customTaskExtension instance.
        Returns: Optional[List[custom_task_extension.CustomTaskExtension]]
        """
        return self._custom_task_extensions
    
    @custom_task_extensions.setter
    def custom_task_extensions(self,value: Optional[List[custom_task_extension.CustomTaskExtension]] = None) -> None:
        """
        Sets the customTaskExtensions property value. The customTaskExtension instance.
        Args:
            value: Value to set for the customTaskExtensions property.
        """
        self._custom_task_extensions = value
    
    @property
    def deleted_items(self,) -> Optional[deleted_item_container.DeletedItemContainer]:
        """
        Gets the deletedItems property value. Deleted workflows in your lifecycle workflows instance.
        Returns: Optional[deleted_item_container.DeletedItemContainer]
        """
        return self._deleted_items
    
    @deleted_items.setter
    def deleted_items(self,value: Optional[deleted_item_container.DeletedItemContainer] = None) -> None:
        """
        Sets the deletedItems property value. Deleted workflows in your lifecycle workflows instance.
        Args:
            value: Value to set for the deletedItems property.
        """
        self._deleted_items = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "custom_task_extensions": lambda n : setattr(self, 'custom_task_extensions', n.get_collection_of_object_values(custom_task_extension.CustomTaskExtension)),
            "deleted_items": lambda n : setattr(self, 'deleted_items', n.get_object_value(deleted_item_container.DeletedItemContainer)),
            "settings": lambda n : setattr(self, 'settings', n.get_object_value(lifecycle_management_settings.LifecycleManagementSettings)),
            "task_definitions": lambda n : setattr(self, 'task_definitions', n.get_collection_of_object_values(task_definition.TaskDefinition)),
            "workflows": lambda n : setattr(self, 'workflows', n.get_collection_of_object_values(workflow.Workflow)),
            "workflow_templates": lambda n : setattr(self, 'workflow_templates', n.get_collection_of_object_values(workflow_template.WorkflowTemplate)),
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
    
    @property
    def settings(self,) -> Optional[lifecycle_management_settings.LifecycleManagementSettings]:
        """
        Gets the settings property value. The settings property
        Returns: Optional[lifecycle_management_settings.LifecycleManagementSettings]
        """
        return self._settings
    
    @settings.setter
    def settings(self,value: Optional[lifecycle_management_settings.LifecycleManagementSettings] = None) -> None:
        """
        Sets the settings property value. The settings property
        Args:
            value: Value to set for the settings property.
        """
        self._settings = value
    
    @property
    def task_definitions(self,) -> Optional[List[task_definition.TaskDefinition]]:
        """
        Gets the taskDefinitions property value. The definition of tasks within the lifecycle workflows instance.
        Returns: Optional[List[task_definition.TaskDefinition]]
        """
        return self._task_definitions
    
    @task_definitions.setter
    def task_definitions(self,value: Optional[List[task_definition.TaskDefinition]] = None) -> None:
        """
        Sets the taskDefinitions property value. The definition of tasks within the lifecycle workflows instance.
        Args:
            value: Value to set for the taskDefinitions property.
        """
        self._task_definitions = value
    
    @property
    def workflows(self,) -> Optional[List[workflow.Workflow]]:
        """
        Gets the workflows property value. The workflows in the lifecycle workflows instance.
        Returns: Optional[List[workflow.Workflow]]
        """
        return self._workflows
    
    @workflows.setter
    def workflows(self,value: Optional[List[workflow.Workflow]] = None) -> None:
        """
        Sets the workflows property value. The workflows in the lifecycle workflows instance.
        Args:
            value: Value to set for the workflows property.
        """
        self._workflows = value
    
    @property
    def workflow_templates(self,) -> Optional[List[workflow_template.WorkflowTemplate]]:
        """
        Gets the workflowTemplates property value. The workflow templates in the lifecycle workflow instance.
        Returns: Optional[List[workflow_template.WorkflowTemplate]]
        """
        return self._workflow_templates
    
    @workflow_templates.setter
    def workflow_templates(self,value: Optional[List[workflow_template.WorkflowTemplate]] = None) -> None:
        """
        Sets the workflowTemplates property value. The workflow templates in the lifecycle workflow instance.
        Args:
            value: Value to set for the workflowTemplates property.
        """
        self._workflow_templates = value
    

