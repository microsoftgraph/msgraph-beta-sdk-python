from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import alert_rule_template, notification_channel, rule_severity_type, rule_threshold
    from .. import entity

from .. import entity

class AlertRule(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new alertRule and sets the default values.
        """
        super().__init__()
        # The rule template of the alert event. The possible values are: cloudPcProvisionScenario, cloudPcImageUploadScenario, cloudPcOnPremiseNetworkConnectionCheckScenario, unknownFutureValue.
        self._alert_rule_template: Optional[alert_rule_template.AlertRuleTemplate] = None
        # The rule description.
        self._description: Optional[str] = None
        # The display name of the rule.
        self._display_name: Optional[str] = None
        # The status of the rule that indicates whether the rule is enabled or disabled. If true, the rule is enabled; otherwise, the rule is disabled.
        self._enabled: Optional[bool] = None
        # Indicates whether the rule is a system rule. If true, the rule is a system rule; otherwise, the rule is a custom defined rule and can be edited. System rules are built-in and only a few properties can be edited.
        self._is_system_rule: Optional[bool] = None
        # The notification channels of the rule selected by the user.
        self._notification_channels: Optional[List[notification_channel.NotificationChannel]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The severity of the rule. The possible values are: unknown, informational, warning, critical, unknownFutureValue.
        self._severity: Optional[rule_severity_type.RuleSeverityType] = None
        # The conditions to send alerts. For example, send alert when provisioning has failed for greater than or equal to 6 Cloud PCs.
        self._threshold: Optional[rule_threshold.RuleThreshold] = None
    
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
            value: Value to set for the alert_rule_template property.
        """
        self._alert_rule_template = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AlertRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AlertRule
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AlertRule()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. The rule description.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. The rule description.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The display name of the rule.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display name of the rule.
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    @property
    def enabled(self,) -> Optional[bool]:
        """
        Gets the enabled property value. The status of the rule that indicates whether the rule is enabled or disabled. If true, the rule is enabled; otherwise, the rule is disabled.
        Returns: Optional[bool]
        """
        return self._enabled
    
    @enabled.setter
    def enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the enabled property value. The status of the rule that indicates whether the rule is enabled or disabled. If true, the rule is enabled; otherwise, the rule is disabled.
        Args:
            value: Value to set for the enabled property.
        """
        self._enabled = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import alert_rule_template, notification_channel, rule_severity_type, rule_threshold
        from .. import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "alertRuleTemplate": lambda n : setattr(self, 'alert_rule_template', n.get_enum_value(alert_rule_template.AlertRuleTemplate)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "enabled": lambda n : setattr(self, 'enabled', n.get_bool_value()),
            "isSystemRule": lambda n : setattr(self, 'is_system_rule', n.get_bool_value()),
            "notificationChannels": lambda n : setattr(self, 'notification_channels', n.get_collection_of_object_values(notification_channel.NotificationChannel)),
            "severity": lambda n : setattr(self, 'severity', n.get_enum_value(rule_severity_type.RuleSeverityType)),
            "threshold": lambda n : setattr(self, 'threshold', n.get_object_value(rule_threshold.RuleThreshold)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_system_rule(self,) -> Optional[bool]:
        """
        Gets the isSystemRule property value. Indicates whether the rule is a system rule. If true, the rule is a system rule; otherwise, the rule is a custom defined rule and can be edited. System rules are built-in and only a few properties can be edited.
        Returns: Optional[bool]
        """
        return self._is_system_rule
    
    @is_system_rule.setter
    def is_system_rule(self,value: Optional[bool] = None) -> None:
        """
        Sets the isSystemRule property value. Indicates whether the rule is a system rule. If true, the rule is a system rule; otherwise, the rule is a custom defined rule and can be edited. System rules are built-in and only a few properties can be edited.
        Args:
            value: Value to set for the is_system_rule property.
        """
        self._is_system_rule = value
    
    @property
    def notification_channels(self,) -> Optional[List[notification_channel.NotificationChannel]]:
        """
        Gets the notificationChannels property value. The notification channels of the rule selected by the user.
        Returns: Optional[List[notification_channel.NotificationChannel]]
        """
        return self._notification_channels
    
    @notification_channels.setter
    def notification_channels(self,value: Optional[List[notification_channel.NotificationChannel]] = None) -> None:
        """
        Sets the notificationChannels property value. The notification channels of the rule selected by the user.
        Args:
            value: Value to set for the notification_channels property.
        """
        self._notification_channels = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("alertRuleTemplate", self.alert_rule_template)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_bool_value("enabled", self.enabled)
        writer.write_bool_value("isSystemRule", self.is_system_rule)
        writer.write_collection_of_object_values("notificationChannels", self.notification_channels)
        writer.write_enum_value("severity", self.severity)
        writer.write_object_value("threshold", self.threshold)
    
    @property
    def severity(self,) -> Optional[rule_severity_type.RuleSeverityType]:
        """
        Gets the severity property value. The severity of the rule. The possible values are: unknown, informational, warning, critical, unknownFutureValue.
        Returns: Optional[rule_severity_type.RuleSeverityType]
        """
        return self._severity
    
    @severity.setter
    def severity(self,value: Optional[rule_severity_type.RuleSeverityType] = None) -> None:
        """
        Sets the severity property value. The severity of the rule. The possible values are: unknown, informational, warning, critical, unknownFutureValue.
        Args:
            value: Value to set for the severity property.
        """
        self._severity = value
    
    @property
    def threshold(self,) -> Optional[rule_threshold.RuleThreshold]:
        """
        Gets the threshold property value. The conditions to send alerts. For example, send alert when provisioning has failed for greater than or equal to 6 Cloud PCs.
        Returns: Optional[rule_threshold.RuleThreshold]
        """
        return self._threshold
    
    @threshold.setter
    def threshold(self,value: Optional[rule_threshold.RuleThreshold] = None) -> None:
        """
        Sets the threshold property value. The conditions to send alerts. For example, send alert when provisioning has failed for greater than or equal to 6 Cloud PCs.
        Args:
            value: Value to set for the threshold property.
        """
        self._threshold = value
    

