from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .detection_action import DetectionAction
    from .protection_rule import ProtectionRule
    from .query_condition import QueryCondition
    from .rule_schedule import RuleSchedule
    from .run_details import RunDetails

from .protection_rule import ProtectionRule

@dataclass
class DetectionRule(ProtectionRule):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.detectionRule"
    # Complex type representing the actions taken when a detection is made by this rule.
    detection_action: Optional[DetectionAction] = None
    # The ID of the detector that triggered the alert. Also see the 'detectorId' field in microsoft.graph.security.alert.
    detector_id: Optional[str] = None
    # Complex type holding details about the last run of this rule.
    last_run_details: Optional[RunDetails] = None
    # Complex type holding data about the advanced hunting query of this rule.
    query_condition: Optional[QueryCondition] = None
    # Complex type holding data about the triggering schedule of this rule.
    schedule: Optional[RuleSchedule] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DetectionRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DetectionRule
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DetectionRule()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .detection_action import DetectionAction
        from .protection_rule import ProtectionRule
        from .query_condition import QueryCondition
        from .rule_schedule import RuleSchedule
        from .run_details import RunDetails

        from .detection_action import DetectionAction
        from .protection_rule import ProtectionRule
        from .query_condition import QueryCondition
        from .rule_schedule import RuleSchedule
        from .run_details import RunDetails

        fields: Dict[str, Callable[[Any], None]] = {
            "detectionAction": lambda n : setattr(self, 'detection_action', n.get_object_value(DetectionAction)),
            "detectorId": lambda n : setattr(self, 'detector_id', n.get_str_value()),
            "lastRunDetails": lambda n : setattr(self, 'last_run_details', n.get_object_value(RunDetails)),
            "queryCondition": lambda n : setattr(self, 'query_condition', n.get_object_value(QueryCondition)),
            "schedule": lambda n : setattr(self, 'schedule', n.get_object_value(RuleSchedule)),
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
        writer.write_object_value("detectionAction", self.detection_action)
        writer.write_str_value("detectorId", self.detector_id)
        writer.write_object_value("lastRunDetails", self.last_run_details)
        writer.write_object_value("queryCondition", self.query_condition)
        writer.write_object_value("schedule", self.schedule)
    

