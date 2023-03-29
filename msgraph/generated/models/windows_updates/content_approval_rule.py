from __future__ import annotations
from datetime import timedelta
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import compliance_change_rule, content_filter

from . import compliance_change_rule

class ContentApprovalRule(compliance_change_rule.ComplianceChangeRule):
    def __init__(self,) -> None:
        """
        Instantiates a new ContentApprovalRule and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windowsUpdates.contentApprovalRule"
        # A filter to determine which content matches the rule on an ongoing basis.
        self._content_filter: Optional[content_filter.ContentFilter] = None
        # The time before the deployment starts represented in ISO 8601 format for durations.
        self._duration_before_deployment_start: Optional[timedelta] = None
    
    @property
    def content_filter(self,) -> Optional[content_filter.ContentFilter]:
        """
        Gets the contentFilter property value. A filter to determine which content matches the rule on an ongoing basis.
        Returns: Optional[content_filter.ContentFilter]
        """
        return self._content_filter
    
    @content_filter.setter
    def content_filter(self,value: Optional[content_filter.ContentFilter] = None) -> None:
        """
        Sets the contentFilter property value. A filter to determine which content matches the rule on an ongoing basis.
        Args:
            value: Value to set for the content_filter property.
        """
        self._content_filter = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ContentApprovalRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ContentApprovalRule
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ContentApprovalRule()
    
    @property
    def duration_before_deployment_start(self,) -> Optional[timedelta]:
        """
        Gets the durationBeforeDeploymentStart property value. The time before the deployment starts represented in ISO 8601 format for durations.
        Returns: Optional[timedelta]
        """
        return self._duration_before_deployment_start
    
    @duration_before_deployment_start.setter
    def duration_before_deployment_start(self,value: Optional[timedelta] = None) -> None:
        """
        Sets the durationBeforeDeploymentStart property value. The time before the deployment starts represented in ISO 8601 format for durations.
        Args:
            value: Value to set for the duration_before_deployment_start property.
        """
        self._duration_before_deployment_start = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import compliance_change_rule, content_filter

        fields: Dict[str, Callable[[Any], None]] = {
            "contentFilter": lambda n : setattr(self, 'content_filter', n.get_object_value(content_filter.ContentFilter)),
            "durationBeforeDeploymentStart": lambda n : setattr(self, 'duration_before_deployment_start', n.get_timedelta_value()),
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
        writer.write_object_value("contentFilter", self.content_filter)
        writer.write_timedelta_value("durationBeforeDeploymentStart", self.duration_before_deployment_start)
    

