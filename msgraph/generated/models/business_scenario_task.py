from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

business_scenario_properties = lazy_import('msgraph.generated.models.business_scenario_properties')
business_scenario_task_target_base = lazy_import('msgraph.generated.models.business_scenario_task_target_base')
planner_task = lazy_import('msgraph.generated.models.planner_task')

class BusinessScenarioTask(planner_task.PlannerTask):
    @property
    def business_scenario_properties(self,) -> Optional[business_scenario_properties.BusinessScenarioProperties]:
        """
        Gets the businessScenarioProperties property value. The businessScenarioProperties property
        Returns: Optional[business_scenario_properties.BusinessScenarioProperties]
        """
        return self._business_scenario_properties
    
    @business_scenario_properties.setter
    def business_scenario_properties(self,value: Optional[business_scenario_properties.BusinessScenarioProperties] = None) -> None:
        """
        Sets the businessScenarioProperties property value. The businessScenarioProperties property
        Args:
            value: Value to set for the businessScenarioProperties property.
        """
        self._business_scenario_properties = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new BusinessScenarioTask and sets the default values.
        """
        super().__init__()
        # The businessScenarioProperties property
        self._business_scenario_properties: Optional[business_scenario_properties.BusinessScenarioProperties] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The target property
        self._target: Optional[business_scenario_task_target_base.BusinessScenarioTaskTargetBase] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> BusinessScenarioTask:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: BusinessScenarioTask
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return BusinessScenarioTask()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "business_scenario_properties": lambda n : setattr(self, 'business_scenario_properties', n.get_object_value(business_scenario_properties.BusinessScenarioProperties)),
            "target": lambda n : setattr(self, 'target', n.get_object_value(business_scenario_task_target_base.BusinessScenarioTaskTargetBase)),
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
        writer.write_object_value("businessScenarioProperties", self.business_scenario_properties)
        writer.write_object_value("target", self.target)
    
    @property
    def target(self,) -> Optional[business_scenario_task_target_base.BusinessScenarioTaskTargetBase]:
        """
        Gets the target property value. The target property
        Returns: Optional[business_scenario_task_target_base.BusinessScenarioTaskTargetBase]
        """
        return self._target
    
    @target.setter
    def target(self,value: Optional[business_scenario_task_target_base.BusinessScenarioTaskTargetBase] = None) -> None:
        """
        Sets the target property value. The target property
        Args:
            value: Value to set for the target property.
        """
        self._target = value
    

