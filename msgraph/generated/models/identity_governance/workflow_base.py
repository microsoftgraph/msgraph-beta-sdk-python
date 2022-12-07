from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

user = lazy_import('msgraph.generated.models.user')
lifecycle_workflow_category = lazy_import('msgraph.generated.models.identity_governance.lifecycle_workflow_category')
task = lazy_import('msgraph.generated.models.identity_governance.task')
workflow_execution_conditions = lazy_import('msgraph.generated.models.identity_governance.workflow_execution_conditions')

class WorkflowBase(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
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
        Instantiates a new workflowBase and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The category property
        self._category: Optional[lifecycle_workflow_category.LifecycleWorkflowCategory] = None
        # The user who created the workflow.
        self._created_by: Optional[user.User] = None
        # When a workflow was created.
        self._created_date_time: Optional[datetime] = None
        # A string that describes the purpose of the workflow.
        self._description: Optional[str] = None
        # A string to identify the workflow.
        self._display_name: Optional[str] = None
        # Defines when and for who the workflow will run.
        self._execution_conditions: Optional[workflow_execution_conditions.WorkflowExecutionConditions] = None
        # Whether the workflow is enabled or disabled. If this setting is true, the workflow can be run on demand or on schedule when isSchedulingEnabled is true.
        self._is_enabled: Optional[bool] = None
        # If true, the Lifecycle Workflow engine executes the workflow based on the schedule defined by tenant settings. Cannot be true for a disabled workflow (where isEnabled is false).
        self._is_scheduling_enabled: Optional[bool] = None
        # The user who last modified the workflow.
        self._last_modified_by: Optional[user.User] = None
        # When the workflow was last modified.
        self._last_modified_date_time: Optional[datetime] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The tasks in the workflow.
        self._tasks: Optional[List[task.Task]] = None
    
    @property
    def created_by(self,) -> Optional[user.User]:
        """
        Gets the createdBy property value. The user who created the workflow.
        Returns: Optional[user.User]
        """
        return self._created_by
    
    @created_by.setter
    def created_by(self,value: Optional[user.User] = None) -> None:
        """
        Sets the createdBy property value. The user who created the workflow.
        Args:
            value: Value to set for the createdBy property.
        """
        self._created_by = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. When a workflow was created.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. When a workflow was created.
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WorkflowBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WorkflowBase
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WorkflowBase()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. A string that describes the purpose of the workflow.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. A string that describes the purpose of the workflow.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. A string to identify the workflow.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. A string to identify the workflow.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def execution_conditions(self,) -> Optional[workflow_execution_conditions.WorkflowExecutionConditions]:
        """
        Gets the executionConditions property value. Defines when and for who the workflow will run.
        Returns: Optional[workflow_execution_conditions.WorkflowExecutionConditions]
        """
        return self._execution_conditions
    
    @execution_conditions.setter
    def execution_conditions(self,value: Optional[workflow_execution_conditions.WorkflowExecutionConditions] = None) -> None:
        """
        Sets the executionConditions property value. Defines when and for who the workflow will run.
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
            "created_by": lambda n : setattr(self, 'created_by', n.get_object_value(user.User)),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "execution_conditions": lambda n : setattr(self, 'execution_conditions', n.get_object_value(workflow_execution_conditions.WorkflowExecutionConditions)),
            "is_enabled": lambda n : setattr(self, 'is_enabled', n.get_bool_value()),
            "is_scheduling_enabled": lambda n : setattr(self, 'is_scheduling_enabled', n.get_bool_value()),
            "last_modified_by": lambda n : setattr(self, 'last_modified_by', n.get_object_value(user.User)),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "tasks": lambda n : setattr(self, 'tasks', n.get_collection_of_object_values(task.Task)),
        }
        return fields
    
    @property
    def is_enabled(self,) -> Optional[bool]:
        """
        Gets the isEnabled property value. Whether the workflow is enabled or disabled. If this setting is true, the workflow can be run on demand or on schedule when isSchedulingEnabled is true.
        Returns: Optional[bool]
        """
        return self._is_enabled
    
    @is_enabled.setter
    def is_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isEnabled property value. Whether the workflow is enabled or disabled. If this setting is true, the workflow can be run on demand or on schedule when isSchedulingEnabled is true.
        Args:
            value: Value to set for the isEnabled property.
        """
        self._is_enabled = value
    
    @property
    def is_scheduling_enabled(self,) -> Optional[bool]:
        """
        Gets the isSchedulingEnabled property value. If true, the Lifecycle Workflow engine executes the workflow based on the schedule defined by tenant settings. Cannot be true for a disabled workflow (where isEnabled is false).
        Returns: Optional[bool]
        """
        return self._is_scheduling_enabled
    
    @is_scheduling_enabled.setter
    def is_scheduling_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isSchedulingEnabled property value. If true, the Lifecycle Workflow engine executes the workflow based on the schedule defined by tenant settings. Cannot be true for a disabled workflow (where isEnabled is false).
        Args:
            value: Value to set for the isSchedulingEnabled property.
        """
        self._is_scheduling_enabled = value
    
    @property
    def last_modified_by(self,) -> Optional[user.User]:
        """
        Gets the lastModifiedBy property value. The user who last modified the workflow.
        Returns: Optional[user.User]
        """
        return self._last_modified_by
    
    @last_modified_by.setter
    def last_modified_by(self,value: Optional[user.User] = None) -> None:
        """
        Sets the lastModifiedBy property value. The user who last modified the workflow.
        Args:
            value: Value to set for the lastModifiedBy property.
        """
        self._last_modified_by = value
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. When the workflow was last modified.
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. When the workflow was last modified.
        Args:
            value: Value to set for the lastModifiedDateTime property.
        """
        self._last_modified_date_time = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_enum_value("category", self.category)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("executionConditions", self.execution_conditions)
        writer.write_bool_value("isEnabled", self.is_enabled)
        writer.write_bool_value("isSchedulingEnabled", self.is_scheduling_enabled)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("tasks", self.tasks)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def tasks(self,) -> Optional[List[task.Task]]:
        """
        Gets the tasks property value. The tasks in the workflow.
        Returns: Optional[List[task.Task]]
        """
        return self._tasks
    
    @tasks.setter
    def tasks(self,value: Optional[List[task.Task]] = None) -> None:
        """
        Sets the tasks property value. The tasks in the workflow.
        Args:
            value: Value to set for the tasks property.
        """
        self._tasks = value
    

