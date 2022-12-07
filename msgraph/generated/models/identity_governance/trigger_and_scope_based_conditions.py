from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

subject_set = lazy_import('msgraph.generated.models.subject_set')
workflow_execution_conditions = lazy_import('msgraph.generated.models.identity_governance.workflow_execution_conditions')
workflow_execution_trigger = lazy_import('msgraph.generated.models.identity_governance.workflow_execution_trigger')

class TriggerAndScopeBasedConditions(workflow_execution_conditions.WorkflowExecutionConditions):
    def __init__(self,) -> None:
        """
        Instantiates a new TriggerAndScopeBasedConditions and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.identityGovernance.triggerAndScopeBasedConditions"
        # Defines who the workflow runs for.
        self._scope: Optional[subject_set.SubjectSet] = None
        # What triggers a workflow to run.
        self._trigger: Optional[workflow_execution_trigger.WorkflowExecutionTrigger] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TriggerAndScopeBasedConditions:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TriggerAndScopeBasedConditions
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TriggerAndScopeBasedConditions()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "scope": lambda n : setattr(self, 'scope', n.get_object_value(subject_set.SubjectSet)),
            "trigger": lambda n : setattr(self, 'trigger', n.get_object_value(workflow_execution_trigger.WorkflowExecutionTrigger)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def scope(self,) -> Optional[subject_set.SubjectSet]:
        """
        Gets the scope property value. Defines who the workflow runs for.
        Returns: Optional[subject_set.SubjectSet]
        """
        return self._scope
    
    @scope.setter
    def scope(self,value: Optional[subject_set.SubjectSet] = None) -> None:
        """
        Sets the scope property value. Defines who the workflow runs for.
        Args:
            value: Value to set for the scope property.
        """
        self._scope = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("scope", self.scope)
        writer.write_object_value("trigger", self.trigger)
    
    @property
    def trigger(self,) -> Optional[workflow_execution_trigger.WorkflowExecutionTrigger]:
        """
        Gets the trigger property value. What triggers a workflow to run.
        Returns: Optional[workflow_execution_trigger.WorkflowExecutionTrigger]
        """
        return self._trigger
    
    @trigger.setter
    def trigger(self,value: Optional[workflow_execution_trigger.WorkflowExecutionTrigger] = None) -> None:
        """
        Sets the trigger property value. What triggers a workflow to run.
        Args:
            value: Value to set for the trigger property.
        """
        self._trigger = value
    

