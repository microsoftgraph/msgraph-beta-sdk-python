from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .compliance_change_rule import ComplianceChangeRule
    from .content_filter import ContentFilter

from .compliance_change_rule import ComplianceChangeRule

@dataclass
class ContentApprovalRule(ComplianceChangeRule):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.windowsUpdates.contentApprovalRule"
    # A filter to determine which content matches the rule on an ongoing basis.
    content_filter: Optional[ContentFilter] = None
    # The time before the deployment starts represented in ISO 8601 format for durations.
    duration_before_deployment_start: Optional[datetime.timedelta] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ContentApprovalRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ContentApprovalRule
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ContentApprovalRule()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .compliance_change_rule import ComplianceChangeRule
        from .content_filter import ContentFilter

        from .compliance_change_rule import ComplianceChangeRule
        from .content_filter import ContentFilter

        fields: Dict[str, Callable[[Any], None]] = {
            "contentFilter": lambda n : setattr(self, 'content_filter', n.get_object_value(ContentFilter)),
            "durationBeforeDeploymentStart": lambda n : setattr(self, 'duration_before_deployment_start', n.get_timedelta_value()),
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
        writer.write_object_value("contentFilter", self.content_filter)
        writer.write_timedelta_value("durationBeforeDeploymentStart", self.duration_before_deployment_start)
    

