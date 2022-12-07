from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

alert_impact = lazy_import('msgraph.generated.models.device_management.alert_impact')
alert_rule_template = lazy_import('msgraph.generated.models.device_management.alert_rule_template')
rule_severity_type = lazy_import('msgraph.generated.models.device_management.rule_severity_type')

class PortalNotification(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def alert_impact(self,) -> Optional[alert_impact.AlertImpact]:
        """
        Gets the alertImpact property value. The associated alert impact.
        Returns: Optional[alert_impact.AlertImpact]
        """
        return self._alert_impact
    
    @alert_impact.setter
    def alert_impact(self,value: Optional[alert_impact.AlertImpact] = None) -> None:
        """
        Sets the alertImpact property value. The associated alert impact.
        Args:
            value: Value to set for the alertImpact property.
        """
        self._alert_impact = value
    
    @property
    def alert_record_id(self,) -> Optional[str]:
        """
        Gets the alertRecordId property value. The associated alert record ID.
        Returns: Optional[str]
        """
        return self._alert_record_id
    
    @alert_record_id.setter
    def alert_record_id(self,value: Optional[str] = None) -> None:
        """
        Sets the alertRecordId property value. The associated alert record ID.
        Args:
            value: Value to set for the alertRecordId property.
        """
        self._alert_record_id = value
    
    @property
    def alert_rule_id(self,) -> Optional[str]:
        """
        Gets the alertRuleId property value. The associated alert rule ID.
        Returns: Optional[str]
        """
        return self._alert_rule_id
    
    @alert_rule_id.setter
    def alert_rule_id(self,value: Optional[str] = None) -> None:
        """
        Sets the alertRuleId property value. The associated alert rule ID.
        Args:
            value: Value to set for the alertRuleId property.
        """
        self._alert_rule_id = value
    
    @property
    def alert_rule_name(self,) -> Optional[str]:
        """
        Gets the alertRuleName property value. The associated alert rule name.
        Returns: Optional[str]
        """
        return self._alert_rule_name
    
    @alert_rule_name.setter
    def alert_rule_name(self,value: Optional[str] = None) -> None:
        """
        Sets the alertRuleName property value. The associated alert rule name.
        Args:
            value: Value to set for the alertRuleName property.
        """
        self._alert_rule_name = value
    
    @property
    def alert_rule_template(self,) -> Optional[alert_rule_template.AlertRuleTemplate]:
        """
        Gets the alertRuleTemplate property value. The associated alert rule template. The possible values are: cloudPcProvisionScenario, cloudPcImageUploadScenario, cloudPcOnPremiseNetworkConnectionCheckScenario, unknownFutureValue.
        Returns: Optional[alert_rule_template.AlertRuleTemplate]
        """
        return self._alert_rule_template
    
    @alert_rule_template.setter
    def alert_rule_template(self,value: Optional[alert_rule_template.AlertRuleTemplate] = None) -> None:
        """
        Sets the alertRuleTemplate property value. The associated alert rule template. The possible values are: cloudPcProvisionScenario, cloudPcImageUploadScenario, cloudPcOnPremiseNetworkConnectionCheckScenario, unknownFutureValue.
        Args:
            value: Value to set for the alertRuleTemplate property.
        """
        self._alert_rule_template = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new portalNotification and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The associated alert impact.
        self._alert_impact: Optional[alert_impact.AlertImpact] = None
        # The associated alert record ID.
        self._alert_record_id: Optional[str] = None
        # The associated alert rule ID.
        self._alert_rule_id: Optional[str] = None
        # The associated alert rule name.
        self._alert_rule_name: Optional[str] = None
        # The associated alert rule template. The possible values are: cloudPcProvisionScenario, cloudPcImageUploadScenario, cloudPcOnPremiseNetworkConnectionCheckScenario, unknownFutureValue.
        self._alert_rule_template: Optional[alert_rule_template.AlertRuleTemplate] = None
        # The unique identifier for the portal notification.
        self._id: Optional[str] = None
        # If true, the portal notification has already been sent for the user; otherwise, the portal notification hasn't been sent yet.
        self._is_portal_notification_sent: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The associated alert rule severity. The possible values are: unknown, informational, warning, critical, unknownFutureValue.
        self._severity: Optional[rule_severity_type.RuleSeverityType] = None
    
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
        fields = {
            "alert_impact": lambda n : setattr(self, 'alert_impact', n.get_object_value(alert_impact.AlertImpact)),
            "alert_record_id": lambda n : setattr(self, 'alert_record_id', n.get_str_value()),
            "alert_rule_id": lambda n : setattr(self, 'alert_rule_id', n.get_str_value()),
            "alert_rule_name": lambda n : setattr(self, 'alert_rule_name', n.get_str_value()),
            "alert_rule_template": lambda n : setattr(self, 'alert_rule_template', n.get_enum_value(alert_rule_template.AlertRuleTemplate)),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "is_portal_notification_sent": lambda n : setattr(self, 'is_portal_notification_sent', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "severity": lambda n : setattr(self, 'severity', n.get_enum_value(rule_severity_type.RuleSeverityType)),
        }
        return fields
    
    @property
    def id(self,) -> Optional[str]:
        """
        Gets the id property value. The unique identifier for the portal notification.
        Returns: Optional[str]
        """
        return self._id
    
    @id.setter
    def id(self,value: Optional[str] = None) -> None:
        """
        Sets the id property value. The unique identifier for the portal notification.
        Args:
            value: Value to set for the id property.
        """
        self._id = value
    
    @property
    def is_portal_notification_sent(self,) -> Optional[bool]:
        """
        Gets the isPortalNotificationSent property value. If true, the portal notification has already been sent for the user; otherwise, the portal notification hasn't been sent yet.
        Returns: Optional[bool]
        """
        return self._is_portal_notification_sent
    
    @is_portal_notification_sent.setter
    def is_portal_notification_sent(self,value: Optional[bool] = None) -> None:
        """
        Sets the isPortalNotificationSent property value. If true, the portal notification has already been sent for the user; otherwise, the portal notification hasn't been sent yet.
        Args:
            value: Value to set for the isPortalNotificationSent property.
        """
        self._is_portal_notification_sent = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
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
    
    @property
    def severity(self,) -> Optional[rule_severity_type.RuleSeverityType]:
        """
        Gets the severity property value. The associated alert rule severity. The possible values are: unknown, informational, warning, critical, unknownFutureValue.
        Returns: Optional[rule_severity_type.RuleSeverityType]
        """
        return self._severity
    
    @severity.setter
    def severity(self,value: Optional[rule_severity_type.RuleSeverityType] = None) -> None:
        """
        Sets the severity property value. The associated alert rule severity. The possible values are: unknown, informational, warning, critical, unknownFutureValue.
        Args:
            value: Value to set for the severity property.
        """
        self._severity = value
    

