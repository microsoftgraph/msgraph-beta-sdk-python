from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
alert_impact = lazy_import('msgraph.generated.models.device_management.alert_impact')
alert_rule_template = lazy_import('msgraph.generated.models.device_management.alert_rule_template')
alert_status_type = lazy_import('msgraph.generated.models.device_management.alert_status_type')
rule_severity_type = lazy_import('msgraph.generated.models.device_management.rule_severity_type')

class AlertRecord(entity.Entity):
    """
    Provides operations to manage the collection of accessReviewDecision entities.
    """
    @property
    def alert_impact(self,) -> Optional[alert_impact.AlertImpact]:
        """
        Gets the alertImpact property value. The impact of the alert event. Consists of a number followed by the aggregation type. For example, 6 Count and 12 AffectedCloudPcPercentage.
        Returns: Optional[alert_impact.AlertImpact]
        """
        return self._alert_impact
    
    @alert_impact.setter
    def alert_impact(self,value: Optional[alert_impact.AlertImpact] = None) -> None:
        """
        Sets the alertImpact property value. The impact of the alert event. Consists of a number followed by the aggregation type. For example, 6 Count and 12 AffectedCloudPcPercentage.
        Args:
            value: Value to set for the alertImpact property.
        """
        self._alert_impact = value
    
    @property
    def alert_rule_id(self,) -> Optional[str]:
        """
        Gets the alertRuleId property value. The corresponding ID of the alert rule.
        Returns: Optional[str]
        """
        return self._alert_rule_id
    
    @alert_rule_id.setter
    def alert_rule_id(self,value: Optional[str] = None) -> None:
        """
        Sets the alertRuleId property value. The corresponding ID of the alert rule.
        Args:
            value: Value to set for the alertRuleId property.
        """
        self._alert_rule_id = value
    
    @property
    def alert_rule_template(self,) -> Optional[alert_rule_template.AlertRuleTemplate]:
        """
        Gets the alertRuleTemplate property value. The rule template of the alert event. The possible values are: cloudPcProvisionScenario, cloudPcImageUploadScenario, cloudPcOnPremiseNetworkConnectionCheckScenario, unknownFutureValue.
        Returns: Optional[alert_rule_template.AlertRuleTemplate]
        """
        return self._alert_rule_template
    
    @alert_rule_template.setter
    def alert_rule_template(self,value: Optional[alert_rule_template.AlertRuleTemplate] = None) -> None:
        """
        Sets the alertRuleTemplate property value. The rule template of the alert event. The possible values are: cloudPcProvisionScenario, cloudPcImageUploadScenario, cloudPcOnPremiseNetworkConnectionCheckScenario, unknownFutureValue.
        Args:
            value: Value to set for the alertRuleTemplate property.
        """
        self._alert_rule_template = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new alertRecord and sets the default values.
        """
        super().__init__()
        # The impact of the alert event. Consists of a number followed by the aggregation type. For example, 6 Count and 12 AffectedCloudPcPercentage.
        self._alert_impact: Optional[alert_impact.AlertImpact] = None
        # The corresponding ID of the alert rule.
        self._alert_rule_id: Optional[str] = None
        # The rule template of the alert event. The possible values are: cloudPcProvisionScenario, cloudPcImageUploadScenario, cloudPcOnPremiseNetworkConnectionCheckScenario, unknownFutureValue.
        self._alert_rule_template: Optional[alert_rule_template.AlertRuleTemplate] = None
        # The date and time when the alert event was detected. The Timestamp type represents date and time information using ISO 8601 format. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        self._detected_date_time: Optional[datetime] = None
        # The display name of the alert record.
        self._display_name: Optional[str] = None
        # The date and time when the alert record was last updated. The Timestamp type represents date and time information using ISO 8601 format. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        self._last_updated_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The date and time when the alert event was resolved. The Timestamp type represents date and time information using ISO 8601 format. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        self._resolved_date_time: Optional[datetime] = None
        # The severity of the alert event. The possible values are: unknown, informational, warning, critical, unknownFutureValue.
        self._severity: Optional[rule_severity_type.RuleSeverityType] = None
        # The status of the alert record. The possible values are: active, resolved, unknownFutureValue.
        self._status: Optional[alert_status_type.AlertStatusType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AlertRecord:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AlertRecord
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AlertRecord()
    
    @property
    def detected_date_time(self,) -> Optional[datetime]:
        """
        Gets the detectedDateTime property value. The date and time when the alert event was detected. The Timestamp type represents date and time information using ISO 8601 format. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Returns: Optional[datetime]
        """
        return self._detected_date_time
    
    @detected_date_time.setter
    def detected_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the detectedDateTime property value. The date and time when the alert event was detected. The Timestamp type represents date and time information using ISO 8601 format. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Args:
            value: Value to set for the detectedDateTime property.
        """
        self._detected_date_time = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The display name of the alert record.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display name of the alert record.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "alert_impact": lambda n : setattr(self, 'alert_impact', n.get_object_value(alert_impact.AlertImpact)),
            "alert_rule_id": lambda n : setattr(self, 'alert_rule_id', n.get_str_value()),
            "alert_rule_template": lambda n : setattr(self, 'alert_rule_template', n.get_enum_value(alert_rule_template.AlertRuleTemplate)),
            "detected_date_time": lambda n : setattr(self, 'detected_date_time', n.get_datetime_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "last_updated_date_time": lambda n : setattr(self, 'last_updated_date_time', n.get_datetime_value()),
            "resolved_date_time": lambda n : setattr(self, 'resolved_date_time', n.get_datetime_value()),
            "severity": lambda n : setattr(self, 'severity', n.get_enum_value(rule_severity_type.RuleSeverityType)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(alert_status_type.AlertStatusType)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_updated_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastUpdatedDateTime property value. The date and time when the alert record was last updated. The Timestamp type represents date and time information using ISO 8601 format. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Returns: Optional[datetime]
        """
        return self._last_updated_date_time
    
    @last_updated_date_time.setter
    def last_updated_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastUpdatedDateTime property value. The date and time when the alert record was last updated. The Timestamp type represents date and time information using ISO 8601 format. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Args:
            value: Value to set for the lastUpdatedDateTime property.
        """
        self._last_updated_date_time = value
    
    @property
    def resolved_date_time(self,) -> Optional[datetime]:
        """
        Gets the resolvedDateTime property value. The date and time when the alert event was resolved. The Timestamp type represents date and time information using ISO 8601 format. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Returns: Optional[datetime]
        """
        return self._resolved_date_time
    
    @resolved_date_time.setter
    def resolved_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the resolvedDateTime property value. The date and time when the alert event was resolved. The Timestamp type represents date and time information using ISO 8601 format. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Args:
            value: Value to set for the resolvedDateTime property.
        """
        self._resolved_date_time = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("alertImpact", self.alert_impact)
        writer.write_str_value("alertRuleId", self.alert_rule_id)
        writer.write_enum_value("alertRuleTemplate", self.alert_rule_template)
        writer.write_datetime_value("detectedDateTime", self.detected_date_time)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("lastUpdatedDateTime", self.last_updated_date_time)
        writer.write_datetime_value("resolvedDateTime", self.resolved_date_time)
        writer.write_enum_value("severity", self.severity)
        writer.write_enum_value("status", self.status)
    
    @property
    def severity(self,) -> Optional[rule_severity_type.RuleSeverityType]:
        """
        Gets the severity property value. The severity of the alert event. The possible values are: unknown, informational, warning, critical, unknownFutureValue.
        Returns: Optional[rule_severity_type.RuleSeverityType]
        """
        return self._severity
    
    @severity.setter
    def severity(self,value: Optional[rule_severity_type.RuleSeverityType] = None) -> None:
        """
        Sets the severity property value. The severity of the alert event. The possible values are: unknown, informational, warning, critical, unknownFutureValue.
        Args:
            value: Value to set for the severity property.
        """
        self._severity = value
    
    @property
    def status(self,) -> Optional[alert_status_type.AlertStatusType]:
        """
        Gets the status property value. The status of the alert record. The possible values are: active, resolved, unknownFutureValue.
        Returns: Optional[alert_status_type.AlertStatusType]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[alert_status_type.AlertStatusType] = None) -> None:
        """
        Sets the status property value. The status of the alert record. The possible values are: active, resolved, unknownFutureValue.
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    

