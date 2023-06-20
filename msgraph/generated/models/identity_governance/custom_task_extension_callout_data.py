from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import task, task_processing_result, workflow
    from .. import custom_extension_data, user

from .. import custom_extension_data

@dataclass
class CustomTaskExtensionCalloutData(custom_extension_data.CustomExtensionData):
    odata_type = "#microsoft.graph.identityGovernance.customTaskExtensionCalloutData"
    # The subject property
    subject: Optional[user.User] = None
    # The task property
    task: Optional[task.Task] = None
    # The taskProcessingresult property
    task_processingresult: Optional[task_processing_result.TaskProcessingResult] = None
    # The workflow property
    workflow: Optional[workflow.Workflow] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CustomTaskExtensionCalloutData:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CustomTaskExtensionCalloutData
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return CustomTaskExtensionCalloutData()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import task, task_processing_result, workflow
        from .. import custom_extension_data, user

        from . import task, task_processing_result, workflow
        from .. import custom_extension_data, user

        fields: Dict[str, Callable[[Any], None]] = {
            "subject": lambda n : setattr(self, 'subject', n.get_object_value(user.User)),
            "task": lambda n : setattr(self, 'task', n.get_object_value(task.Task)),
            "taskProcessingresult": lambda n : setattr(self, 'task_processingresult', n.get_object_value(task_processing_result.TaskProcessingResult)),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_object_value("subject", self.subject)
        writer.write_object_value("task", self.task)
        writer.write_object_value("taskProcessingresult", self.task_processingresult)
        writer.write_object_value("workflow", self.workflow)
    

