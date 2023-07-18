from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....models.device_compliance_scheduled_action_for_rule import DeviceComplianceScheduledActionForRule

@dataclass
class ScheduleActionsForRulesPostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The deviceComplianceScheduledActionForRules property
    device_compliance_scheduled_action_for_rules: Optional[List[DeviceComplianceScheduledActionForRule]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ScheduleActionsForRulesPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ScheduleActionsForRulesPostRequestBody
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ScheduleActionsForRulesPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .....models.device_compliance_scheduled_action_for_rule import DeviceComplianceScheduledActionForRule

        from .....models.device_compliance_scheduled_action_for_rule import DeviceComplianceScheduledActionForRule

        fields: Dict[str, Callable[[Any], None]] = {
            "deviceComplianceScheduledActionForRules": lambda n : setattr(self, 'device_compliance_scheduled_action_for_rules', n.get_collection_of_object_values(DeviceComplianceScheduledActionForRule)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_collection_of_object_values("deviceComplianceScheduledActionForRules", self.device_compliance_scheduled_action_for_rules)
        writer.write_additional_data_value(self.additional_data)
    

