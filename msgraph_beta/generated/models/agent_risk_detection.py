from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .risk_detail import RiskDetail
    from .risk_detection_timing_type import RiskDetectionTimingType
    from .risk_level import RiskLevel
    from .risk_state import RiskState

from .entity import Entity

@dataclass
class AgentRiskDetection(Entity, Parsable):
    # Date and time that the risky activity occurred. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.  Supports $filter (eq, le, and ge).
    activity_date_time: Optional[datetime.datetime] = None
    # Additional information associated with the risk detection.
    additional_info: Optional[str] = None
    # Name of the agent.  Supports $filter (eq, startsWith).
    agent_display_name: Optional[str] = None
    # The unique identifier for the agent. This is equivalent to 'id' to the specific agent type. See riskyAgentIdentity, riskyAgentIdentityBlueprintPrincipal, and riskyAgentUser.  Supports $filter (eq, startsWith).
    agent_id: Optional[str] = None
    # Date and time that the risk was detected. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.  Supports $filter (eq, le, and ge).
    detected_date_time: Optional[datetime.datetime] = None
    # The detectionTimingType property
    detection_timing_type: Optional[RiskDetectionTimingType] = None
    # Date and time that the risk detection was last updated.  Supports $filter (eq, le, and ge).
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The riskDetail property
    risk_detail: Optional[RiskDetail] = None
    # The type of risk event detected.  Supports $filter (eq).
    risk_event_type: Optional[str] = None
    # Evidence on the risky activity occurred.  Supports $filter (eq).
    risk_evidence: Optional[str] = None
    # The riskLevel property
    risk_level: Optional[RiskLevel] = None
    # The riskState property
    risk_state: Optional[RiskState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AgentRiskDetection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AgentRiskDetection
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AgentRiskDetection()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .risk_detail import RiskDetail
        from .risk_detection_timing_type import RiskDetectionTimingType
        from .risk_level import RiskLevel
        from .risk_state import RiskState

        from .entity import Entity
        from .risk_detail import RiskDetail
        from .risk_detection_timing_type import RiskDetectionTimingType
        from .risk_level import RiskLevel
        from .risk_state import RiskState

        fields: dict[str, Callable[[Any], None]] = {
            "activityDateTime": lambda n : setattr(self, 'activity_date_time', n.get_datetime_value()),
            "additionalInfo": lambda n : setattr(self, 'additional_info', n.get_str_value()),
            "agentDisplayName": lambda n : setattr(self, 'agent_display_name', n.get_str_value()),
            "agentId": lambda n : setattr(self, 'agent_id', n.get_str_value()),
            "detectedDateTime": lambda n : setattr(self, 'detected_date_time', n.get_datetime_value()),
            "detectionTimingType": lambda n : setattr(self, 'detection_timing_type', n.get_enum_value(RiskDetectionTimingType)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "riskDetail": lambda n : setattr(self, 'risk_detail', n.get_enum_value(RiskDetail)),
            "riskEventType": lambda n : setattr(self, 'risk_event_type', n.get_str_value()),
            "riskEvidence": lambda n : setattr(self, 'risk_evidence', n.get_str_value()),
            "riskLevel": lambda n : setattr(self, 'risk_level', n.get_enum_value(RiskLevel)),
            "riskState": lambda n : setattr(self, 'risk_state', n.get_enum_value(RiskState)),
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
        writer.write_datetime_value("activityDateTime", self.activity_date_time)
        writer.write_str_value("additionalInfo", self.additional_info)
        writer.write_str_value("agentDisplayName", self.agent_display_name)
        writer.write_str_value("agentId", self.agent_id)
        writer.write_datetime_value("detectedDateTime", self.detected_date_time)
        writer.write_enum_value("detectionTimingType", self.detection_timing_type)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_enum_value("riskDetail", self.risk_detail)
        writer.write_str_value("riskEventType", self.risk_event_type)
        writer.write_str_value("riskEvidence", self.risk_evidence)
        writer.write_enum_value("riskLevel", self.risk_level)
        writer.write_enum_value("riskState", self.risk_state)
    

