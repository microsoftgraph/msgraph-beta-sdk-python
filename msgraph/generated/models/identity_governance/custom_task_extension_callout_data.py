from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

custom_extension_data = lazy_import('msgraph.generated.models.custom_extension_data')
user = lazy_import('msgraph.generated.models.user')
task = lazy_import('msgraph.generated.models.identity_governance.task')
task_processing_result = lazy_import('msgraph.generated.models.identity_governance.task_processing_result')
workflow = lazy_import('msgraph.generated.models.identity_governance.workflow')

class CustomTaskExtensionCalloutData(custom_extension_data.CustomExtensionData):
    def __init__(self,) -> None:
        """
        Instantiates a new CustomTaskExtensionCalloutData and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.identityGovernance.customTaskExtensionCalloutData"
        # The subject property
        self._subject: Optional[user.User] = None
        # The task property
        self._task: Optional[task.Task] = None
        # The taskProcessingresult property
        self._task_processingresult: Optional[task_processing_result.TaskProcessingResult] = None
        # The workflow property
        self._workflow: Optional[workflow.Workflow] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CustomTaskExtensionCalloutData:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CustomTaskExtensionCalloutData
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CustomTaskExtensionCalloutData()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "subject": lambda n : setattr(self, 'subject', n.get_object_value(user.User)),
            "task": lambda n : setattr(self, 'task', n.get_object_value(task.Task)),
            "task_processingresult": lambda n : setattr(self, 'task_processingresult', n.get_object_value(task_processing_result.TaskProcessingResult)),
            "workflow": lambda n : setattr(self, 'workflow', n.get_object_value(workflow.Workflow)),
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
        writer.write_object_value("subject", self.subject)
        writer.write_object_value("task", self.task)
        writer.write_object_value("taskProcessingresult", self.task_processingresult)
        writer.write_object_value("workflow", self.workflow)
    
    @property
    def subject(self,) -> Optional[user.User]:
        """
        Gets the subject property value. The subject property
        Returns: Optional[user.User]
        """
        return self._subject
    
    @subject.setter
    def subject(self,value: Optional[user.User] = None) -> None:
        """
        Sets the subject property value. The subject property
        Args:
            value: Value to set for the subject property.
        """
        self._subject = value
    
    @property
    def task(self,) -> Optional[task.Task]:
        """
        Gets the task property value. The task property
        Returns: Optional[task.Task]
        """
        return self._task
    
    @task.setter
    def task(self,value: Optional[task.Task] = None) -> None:
        """
        Sets the task property value. The task property
        Args:
            value: Value to set for the task property.
        """
        self._task = value
    
    @property
    def task_processingresult(self,) -> Optional[task_processing_result.TaskProcessingResult]:
        """
        Gets the taskProcessingresult property value. The taskProcessingresult property
        Returns: Optional[task_processing_result.TaskProcessingResult]
        """
        return self._task_processingresult
    
    @task_processingresult.setter
    def task_processingresult(self,value: Optional[task_processing_result.TaskProcessingResult] = None) -> None:
        """
        Sets the taskProcessingresult property value. The taskProcessingresult property
        Args:
            value: Value to set for the taskProcessingresult property.
        """
        self._task_processingresult = value
    
    @property
    def workflow(self,) -> Optional[workflow.Workflow]:
        """
        Gets the workflow property value. The workflow property
        Returns: Optional[workflow.Workflow]
        """
        return self._workflow
    
    @workflow.setter
    def workflow(self,value: Optional[workflow.Workflow] = None) -> None:
        """
        Sets the workflow property value. The workflow property
        Args:
            value: Value to set for the workflow property.
        """
        self._workflow = value
    

