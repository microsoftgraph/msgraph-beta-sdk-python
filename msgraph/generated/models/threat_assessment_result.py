from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, threat_assessment_result_type

from . import entity

@dataclass
class ThreatAssessmentResult(entity.Entity):
    # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    created_date_time: Optional[datetime] = None
    # The result message for each threat assessment.
    message: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The threat assessment result type. Possible values are: checkPolicy (only for mail assessment), rescan.
    result_type: Optional[threat_assessment_result_type.ThreatAssessmentResultType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ThreatAssessmentResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ThreatAssessmentResult
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ThreatAssessmentResult()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, threat_assessment_result_type

        fields: Dict[str, Callable[[Any], None]] = {
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "message": lambda n : setattr(self, 'message', n.get_str_value()),
            "resultType": lambda n : setattr(self, 'result_type', n.get_enum_value(threat_assessment_result_type.ThreatAssessmentResultType)),
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
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("message", self.message)
        writer.write_enum_value("resultType", self.result_type)
    

