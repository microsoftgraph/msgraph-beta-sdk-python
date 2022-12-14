from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_management_compliance_scheduled_action_for_rule = lazy_import('msgraph.generated.models.device_management_compliance_scheduled_action_for_rule')

class SetScheduledActionsPostRequestBody(AdditionalDataHolder, Parsable):
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
        Instantiates a new setScheduledActionsPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The scheduledActions property
        self._scheduled_actions: Optional[List[device_management_compliance_scheduled_action_for_rule.DeviceManagementComplianceScheduledActionForRule]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SetScheduledActionsPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SetScheduledActionsPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SetScheduledActionsPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "scheduled_actions": lambda n : setattr(self, 'scheduled_actions', n.get_collection_of_object_values(device_management_compliance_scheduled_action_for_rule.DeviceManagementComplianceScheduledActionForRule)),
        }
        return fields
    
    @property
    def scheduled_actions(self,) -> Optional[List[device_management_compliance_scheduled_action_for_rule.DeviceManagementComplianceScheduledActionForRule]]:
        """
        Gets the scheduledActions property value. The scheduledActions property
        Returns: Optional[List[device_management_compliance_scheduled_action_for_rule.DeviceManagementComplianceScheduledActionForRule]]
        """
        return self._scheduled_actions
    
    @scheduled_actions.setter
    def scheduled_actions(self,value: Optional[List[device_management_compliance_scheduled_action_for_rule.DeviceManagementComplianceScheduledActionForRule]] = None) -> None:
        """
        Sets the scheduledActions property value. The scheduledActions property
        Args:
            value: Value to set for the scheduledActions property.
        """
        self._scheduled_actions = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_object_values("scheduledActions", self.scheduled_actions)
        writer.write_additional_data_value(self.additional_data)
    

