from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import alert_impact, alert_rule_template, rule_severity_type

@dataclass
class PortalNotification(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The associated alert impact.
    alert_impact: Optional[alert_impact.AlertImpact] = None
    # The associated alert record ID.
    alert_record_id: Optional[str] = None
    # The associated alert rule ID.
    alert_rule_id: Optional[str] = None
    # The associated alert rule name.
    alert_rule_name: Optional[str] = None
    # The associated alert rule template. The possible values are: cloudPcProvisionScenario, cloudPcImageUploadScenario, cloudPcOnPremiseNetworkConnectionCheckScenario, unknownFutureValue.
    alert_rule_template: Optional[alert_rule_template.AlertRuleTemplate] = None
    # The unique identifier for the portal notification.
    id: Optional[str] = None
    # true if the portal notification has already been sent to the user; false otherwise.
    is_portal_notification_sent: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The associated alert rule severity. The possible values are: unknown, informational, warning, critical, unknownFutureValue.
    severity: Optional[rule_severity_type.RuleSeverityType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PortalNotification:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PortalNotification
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PortalNotification()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import alert_impact, alert_rule_template, rule_severity_type

        fields: Dict[str, Callable[[Any], None]] = {
            "alertImpact": lambda n : setattr(self, 'alert_impact', n.get_object_value(alert_impact.AlertImpact)),
            "alertRecordId": lambda n : setattr(self, 'alert_record_id', n.get_str_value()),
            "alertRuleId": lambda n : setattr(self, 'alert_rule_id', n.get_str_value()),
            "alertRuleName": lambda n : setattr(self, 'alert_rule_name', n.get_str_value()),
            "alertRuleTemplate": lambda n : setattr(self, 'alert_rule_template', n.get_enum_value(alert_rule_template.AlertRuleTemplate)),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "isPortalNotificationSent": lambda n : setattr(self, 'is_portal_notification_sent', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "severity": lambda n : setattr(self, 'severity', n.get_enum_value(rule_severity_type.RuleSeverityType)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("alertImpact", self.alert_impact)
        writer.write_str_value("alertRecordId", self.alert_record_id)
        writer.write_str_value("alertRuleId", self.alert_rule_id)
        writer.write_str_value("alertRuleName", self.alert_rule_name)
        writer.write_enum_value("alertRuleTemplate", self.alert_rule_template)
        writer.write_str_value("id", self.id)
        writer.write_bool_value("isPortalNotificationSent", self.is_portal_notification_sent)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("severity", self.severity)
        writer.write_additional_data_value(self.additional_data)
    

