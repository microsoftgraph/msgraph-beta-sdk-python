from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

business_scenario_task_target_base = lazy_import('msgraph.generated.models.business_scenario_task_target_base')

class GetPlanPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the getPlan method.
    """
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
    
    def __init__(self,) -> None:
        """
        Instantiates a new getPlanPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The target property
        self._target: Optional[business_scenario_task_target_base.BusinessScenarioTaskTargetBase] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> GetPlanPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: GetPlanPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return GetPlanPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "target": lambda n : setattr(self, 'target', n.get_object_value(business_scenario_task_target_base.BusinessScenarioTaskTargetBase)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("target", self.target)
        writer.write_additional_data_value(self.additional_data)
    
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
    

