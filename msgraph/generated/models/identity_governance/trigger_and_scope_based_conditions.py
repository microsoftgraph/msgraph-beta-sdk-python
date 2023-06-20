from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import workflow_execution_conditions, workflow_execution_trigger
    from .. import subject_set

from . import workflow_execution_conditions

@dataclass
class TriggerAndScopeBasedConditions(workflow_execution_conditions.WorkflowExecutionConditions):
    odata_type = "#microsoft.graph.identityGovernance.triggerAndScopeBasedConditions"
    # Defines who the workflow runs for.
    scope: Optional[subject_set.SubjectSet] = None
    # What triggers a workflow to run.
    trigger: Optional[workflow_execution_trigger.WorkflowExecutionTrigger] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TriggerAndScopeBasedConditions:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TriggerAndScopeBasedConditions
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return TriggerAndScopeBasedConditions()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import workflow_execution_conditions, workflow_execution_trigger
        from .. import subject_set

        from . import workflow_execution_conditions, workflow_execution_trigger
        from .. import subject_set

        fields: Dict[str, Callable[[Any], None]] = {
            "scope": lambda n : setattr(self, 'scope', n.get_object_value(subject_set.SubjectSet)),
            "trigger": lambda n : setattr(self, 'trigger', n.get_object_value(workflow_execution_trigger.WorkflowExecutionTrigger)),
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
        writer.write_object_value("scope", self.scope)
        writer.write_object_value("trigger", self.trigger)
    

