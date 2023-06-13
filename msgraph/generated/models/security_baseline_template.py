from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_management_template, security_baseline_category_state_summary, security_baseline_device_state, security_baseline_state_summary

from . import device_management_template

@dataclass
class SecurityBaselineTemplate(device_management_template.DeviceManagementTemplate):
    odata_type = "#microsoft.graph.securityBaselineTemplate"
    # The security baseline per category device state summary
    category_device_state_summaries: Optional[List[security_baseline_category_state_summary.SecurityBaselineCategoryStateSummary]] = None
    # The security baseline device state summary
    device_state_summary: Optional[security_baseline_state_summary.SecurityBaselineStateSummary] = None
    # The security baseline device states
    device_states: Optional[List[security_baseline_device_state.SecurityBaselineDeviceState]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SecurityBaselineTemplate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SecurityBaselineTemplate
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SecurityBaselineTemplate()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_management_template, security_baseline_category_state_summary, security_baseline_device_state, security_baseline_state_summary

        fields: Dict[str, Callable[[Any], None]] = {
            "categoryDeviceStateSummaries": lambda n : setattr(self, 'category_device_state_summaries', n.get_collection_of_object_values(security_baseline_category_state_summary.SecurityBaselineCategoryStateSummary)),
            "deviceStates": lambda n : setattr(self, 'device_states', n.get_collection_of_object_values(security_baseline_device_state.SecurityBaselineDeviceState)),
            "deviceStateSummary": lambda n : setattr(self, 'device_state_summary', n.get_object_value(security_baseline_state_summary.SecurityBaselineStateSummary)),
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
        writer.write_collection_of_object_values("categoryDeviceStateSummaries", self.category_device_state_summaries)
        writer.write_collection_of_object_values("deviceStates", self.device_states)
        writer.write_object_value("deviceStateSummary", self.device_state_summary)
    

