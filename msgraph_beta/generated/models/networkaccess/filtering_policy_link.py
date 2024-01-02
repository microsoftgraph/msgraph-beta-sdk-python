from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .policy_link import PolicyLink
    from .status import Status

from .policy_link import PolicyLink

@dataclass
class FilteringPolicyLink(PolicyLink):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.networkaccess.filteringPolicyLink"
    # The date and time when the filtering Policy link was created.
    created_date_time: Optional[datetime.datetime] = None
    # The date and time when the policy was most recently modified.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The loggingState property
    logging_state: Optional[Status] = None
    # The priority property
    priority: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> FilteringPolicyLink:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FilteringPolicyLink
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return FilteringPolicyLink()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .policy_link import PolicyLink
        from .status import Status

        from .policy_link import PolicyLink
        from .status import Status

        fields: Dict[str, Callable[[Any], None]] = {
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "loggingState": lambda n : setattr(self, 'logging_state', n.get_enum_value(Status)),
            "priority": lambda n : setattr(self, 'priority', n.get_int_value()),
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
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_enum_value("loggingState", self.logging_state)
        writer.write_int_value("priority", self.priority)
    

