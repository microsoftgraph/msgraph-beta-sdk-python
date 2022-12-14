from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

planner_plan_creation = lazy_import('msgraph.generated.models.planner_plan_creation')

class PlannerExternalPlanSource(planner_plan_creation.PlannerPlanCreation):
    def __init__(self,) -> None:
        """
        Instantiates a new PlannerExternalPlanSource and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.plannerExternalPlanSource"
        # Nullable. An identifier for the scenario associated with this external source. This should be in reverse DNS format. For example, Contoso company owned application for customer support would have a value like 'com.constoso.customerSupport'.
        self._context_scenario_id: Optional[str] = None
        # Nullable. The id of the external entity's containing entity or context.
        self._external_context_id: Optional[str] = None
        # Nullable. The id of the entity that an external service associates with a plan.
        self._external_object_id: Optional[str] = None
    
    @property
    def context_scenario_id(self,) -> Optional[str]:
        """
        Gets the contextScenarioId property value. Nullable. An identifier for the scenario associated with this external source. This should be in reverse DNS format. For example, Contoso company owned application for customer support would have a value like 'com.constoso.customerSupport'.
        Returns: Optional[str]
        """
        return self._context_scenario_id
    
    @context_scenario_id.setter
    def context_scenario_id(self,value: Optional[str] = None) -> None:
        """
        Sets the contextScenarioId property value. Nullable. An identifier for the scenario associated with this external source. This should be in reverse DNS format. For example, Contoso company owned application for customer support would have a value like 'com.constoso.customerSupport'.
        Args:
            value: Value to set for the contextScenarioId property.
        """
        self._context_scenario_id = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PlannerExternalPlanSource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PlannerExternalPlanSource
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PlannerExternalPlanSource()
    
    @property
    def external_context_id(self,) -> Optional[str]:
        """
        Gets the externalContextId property value. Nullable. The id of the external entity's containing entity or context.
        Returns: Optional[str]
        """
        return self._external_context_id
    
    @external_context_id.setter
    def external_context_id(self,value: Optional[str] = None) -> None:
        """
        Sets the externalContextId property value. Nullable. The id of the external entity's containing entity or context.
        Args:
            value: Value to set for the externalContextId property.
        """
        self._external_context_id = value
    
    @property
    def external_object_id(self,) -> Optional[str]:
        """
        Gets the externalObjectId property value. Nullable. The id of the entity that an external service associates with a plan.
        Returns: Optional[str]
        """
        return self._external_object_id
    
    @external_object_id.setter
    def external_object_id(self,value: Optional[str] = None) -> None:
        """
        Sets the externalObjectId property value. Nullable. The id of the entity that an external service associates with a plan.
        Args:
            value: Value to set for the externalObjectId property.
        """
        self._external_object_id = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "context_scenario_id": lambda n : setattr(self, 'context_scenario_id', n.get_str_value()),
            "external_context_id": lambda n : setattr(self, 'external_context_id', n.get_str_value()),
            "external_object_id": lambda n : setattr(self, 'external_object_id', n.get_str_value()),
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
        writer.write_str_value("contextScenarioId", self.context_scenario_id)
        writer.write_str_value("externalContextId", self.external_context_id)
        writer.write_str_value("externalObjectId", self.external_object_id)
    

