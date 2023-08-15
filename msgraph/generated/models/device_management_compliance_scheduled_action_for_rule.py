from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_management_compliance_action_item import DeviceManagementComplianceActionItem
    from .entity import Entity

from .entity import Entity

@dataclass
class DeviceManagementComplianceScheduledActionForRule(Entity):
    """
    Scheduled Action for Rule
    """
    # The OdataType property
    odata_type: Optional[str] = None
    # Name of the rule which this scheduled action applies to.
    rule_name: Optional[str] = None
    # The list of scheduled action configurations for this compliance policy. This collection can contain a maximum of 100 elements.
    scheduled_action_configurations: Optional[List[DeviceManagementComplianceActionItem]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementComplianceScheduledActionForRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementComplianceScheduledActionForRule
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return DeviceManagementComplianceScheduledActionForRule()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .device_management_compliance_action_item import DeviceManagementComplianceActionItem
        from .entity import Entity

        from .device_management_compliance_action_item import DeviceManagementComplianceActionItem
        from .entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "ruleName": lambda n : setattr(self, 'rule_name', n.get_str_value()),
            "scheduledActionConfigurations": lambda n : setattr(self, 'scheduled_action_configurations', n.get_collection_of_object_values(DeviceManagementComplianceActionItem)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("ruleName", self.rule_name)
        writer.write_collection_of_object_values("scheduledActionConfigurations", self.scheduled_action_configurations)
    

