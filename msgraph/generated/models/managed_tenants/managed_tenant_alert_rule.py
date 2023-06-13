from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import alert_severity, managed_tenant_alert, managed_tenant_alert_rule_definition, notification_destination, notification_target, tenant_info
    from .. import entity

from .. import entity

@dataclass
class ManagedTenantAlertRule(entity.Entity):
    # The alertDisplayName property
    alert_display_name: Optional[str] = None
    # The alertTTL property
    alert_t_t_l: Optional[int] = None
    # The alerts property
    alerts: Optional[List[managed_tenant_alert.ManagedTenantAlert]] = None
    # The createdByUserId property
    created_by_user_id: Optional[str] = None
    # The createdDateTime property
    created_date_time: Optional[datetime] = None
    # The description property
    description: Optional[str] = None
    # The displayName property
    display_name: Optional[str] = None
    # The lastActionByUserId property
    last_action_by_user_id: Optional[str] = None
    # The lastActionDateTime property
    last_action_date_time: Optional[datetime] = None
    # The lastRunDateTime property
    last_run_date_time: Optional[datetime] = None
    # The notificationFinalDestinations property
    notification_final_destinations: Optional[notification_destination.NotificationDestination] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The ruleDefinition property
    rule_definition: Optional[managed_tenant_alert_rule_definition.ManagedTenantAlertRuleDefinition] = None
    # The severity property
    severity: Optional[alert_severity.AlertSeverity] = None
    # The targets property
    targets: Optional[List[notification_target.NotificationTarget]] = None
    # The tenantIds property
    tenant_ids: Optional[List[tenant_info.TenantInfo]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ManagedTenantAlertRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ManagedTenantAlertRule
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ManagedTenantAlertRule()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import alert_severity, managed_tenant_alert, managed_tenant_alert_rule_definition, notification_destination, notification_target, tenant_info
        from .. import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "alerts": lambda n : setattr(self, 'alerts', n.get_collection_of_object_values(managed_tenant_alert.ManagedTenantAlert)),
            "alertDisplayName": lambda n : setattr(self, 'alert_display_name', n.get_str_value()),
            "alertTTL": lambda n : setattr(self, 'alert_t_t_l', n.get_int_value()),
            "createdByUserId": lambda n : setattr(self, 'created_by_user_id', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lastActionByUserId": lambda n : setattr(self, 'last_action_by_user_id', n.get_str_value()),
            "lastActionDateTime": lambda n : setattr(self, 'last_action_date_time', n.get_datetime_value()),
            "lastRunDateTime": lambda n : setattr(self, 'last_run_date_time', n.get_datetime_value()),
            "notificationFinalDestinations": lambda n : setattr(self, 'notification_final_destinations', n.get_enum_value(notification_destination.NotificationDestination)),
            "ruleDefinition": lambda n : setattr(self, 'rule_definition', n.get_object_value(managed_tenant_alert_rule_definition.ManagedTenantAlertRuleDefinition)),
            "severity": lambda n : setattr(self, 'severity', n.get_enum_value(alert_severity.AlertSeverity)),
            "targets": lambda n : setattr(self, 'targets', n.get_collection_of_object_values(notification_target.NotificationTarget)),
            "tenantIds": lambda n : setattr(self, 'tenant_ids', n.get_collection_of_object_values(tenant_info.TenantInfo)),
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
        writer.write_collection_of_object_values("alerts", self.alerts)
        writer.write_str_value("alertDisplayName", self.alert_display_name)
        writer.write_int_value("alertTTL", self.alert_t_t_l)
        writer.write_str_value("createdByUserId", self.created_by_user_id)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("lastActionByUserId", self.last_action_by_user_id)
        writer.write_datetime_value("lastActionDateTime", self.last_action_date_time)
        writer.write_datetime_value("lastRunDateTime", self.last_run_date_time)
        writer.write_enum_value("notificationFinalDestinations", self.notification_final_destinations)
        writer.write_object_value("ruleDefinition", self.rule_definition)
        writer.write_enum_value("severity", self.severity)
        writer.write_collection_of_object_values("targets", self.targets)
        writer.write_collection_of_object_values("tenantIds", self.tenant_ids)
    

