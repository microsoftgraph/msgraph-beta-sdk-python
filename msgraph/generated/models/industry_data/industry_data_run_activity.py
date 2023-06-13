from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import inbound_flow_activity, industry_data_activity, industry_data_activity_status, outbound_flow_activity
    from .. import entity, public_error

from .. import entity

@dataclass
class IndustryDataRunActivity(entity.Entity):
    # The flow that was run by this activity.
    activity: Optional[industry_data_activity.IndustryDataActivity] = None
    # An error object to diagnose critical failures in an activity.
    blocking_error: Optional[public_error.PublicError] = None
    # The name of the running flow.
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The status property
    status: Optional[industry_data_activity_status.IndustryDataActivityStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IndustryDataRunActivity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IndustryDataRunActivity
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.industryData.inboundFlowActivity":
                from . import inbound_flow_activity

                return inbound_flow_activity.InboundFlowActivity()
            if mapping_value == "#microsoft.graph.industryData.outboundFlowActivity":
                from . import outbound_flow_activity

                return outbound_flow_activity.OutboundFlowActivity()
        return IndustryDataRunActivity()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import inbound_flow_activity, industry_data_activity, industry_data_activity_status, outbound_flow_activity
        from .. import entity, public_error

        fields: Dict[str, Callable[[Any], None]] = {
            "activity": lambda n : setattr(self, 'activity', n.get_object_value(industry_data_activity.IndustryDataActivity)),
            "blockingError": lambda n : setattr(self, 'blocking_error', n.get_object_value(public_error.PublicError)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(industry_data_activity_status.IndustryDataActivityStatus)),
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
        writer.write_object_value("activity", self.activity)
        writer.write_enum_value("status", self.status)
    

