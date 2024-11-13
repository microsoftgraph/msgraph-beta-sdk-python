from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .security_requirement import SecurityRequirement

from .security_requirement import SecurityRequirement

@dataclass
class ResponseTimeSecurityRequirement(SecurityRequirement, Parsable):
    # The average response time for alerts from the past 30 days.
    average_response_time_in_hours: Optional[float] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ResponseTimeSecurityRequirement:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ResponseTimeSecurityRequirement
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ResponseTimeSecurityRequirement()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .security_requirement import SecurityRequirement

        from .security_requirement import SecurityRequirement

        fields: Dict[str, Callable[[Any], None]] = {
            "averageResponseTimeInHours": lambda n : setattr(self, 'average_response_time_in_hours', n.get_float_value()),
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
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        from .security_requirement import SecurityRequirement

        writer.write_float_value("averageResponseTimeInHours", self.average_response_time_in_hours)
    

