from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
alert_severity = lazy_import('msgraph.generated.models.managed_tenants.alert_severity')
managed_tenant_alert = lazy_import('msgraph.generated.models.managed_tenants.managed_tenant_alert')
managed_tenant_alert_rule_definition = lazy_import('msgraph.generated.models.managed_tenants.managed_tenant_alert_rule_definition')
notification_destination = lazy_import('msgraph.generated.models.managed_tenants.notification_destination')
notification_target = lazy_import('msgraph.generated.models.managed_tenants.notification_target')
tenant_info = lazy_import('msgraph.generated.models.managed_tenants.tenant_info')

class ManagedTenantAlertRule(entity.Entity):
    @property
    def alert_display_name(self,) -> Optional[str]:
        """
        Gets the alertDisplayName property value. The alertDisplayName property
        Returns: Optional[str]
        """
        return self._alert_display_name
    
    @alert_display_name.setter
    def alert_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the alertDisplayName property value. The alertDisplayName property
        Args:
            value: Value to set for the alertDisplayName property.
        """
        self._alert_display_name = value
    
    @property
    def alerts(self,) -> Optional[List[managed_tenant_alert.ManagedTenantAlert]]:
        """
        Gets the alerts property value. The alerts property
        Returns: Optional[List[managed_tenant_alert.ManagedTenantAlert]]
        """
        return self._alerts
    
    @alerts.setter
    def alerts(self,value: Optional[List[managed_tenant_alert.ManagedTenantAlert]] = None) -> None:
        """
        Sets the alerts property value. The alerts property
        Args:
            value: Value to set for the alerts property.
        """
        self._alerts = value
    
    @property
    def alert_t_t_l(self,) -> Optional[int]:
        """
        Gets the alertTTL property value. The alertTTL property
        Returns: Optional[int]
        """
        return self._alert_t_t_l
    
    @alert_t_t_l.setter
    def alert_t_t_l(self,value: Optional[int] = None) -> None:
        """
        Sets the alertTTL property value. The alertTTL property
        Args:
            value: Value to set for the alertTTL property.
        """
        self._alert_t_t_l = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new managedTenantAlertRule and sets the default values.
        """
        super().__init__()
        # The alertDisplayName property
        self._alert_display_name: Optional[str] = None
        # The alerts property
        self._alerts: Optional[List[managed_tenant_alert.ManagedTenantAlert]] = None
        # The alertTTL property
        self._alert_t_t_l: Optional[int] = None
        # The createdByUserId property
        self._created_by_user_id: Optional[str] = None
        # The createdDateTime property
        self._created_date_time: Optional[datetime] = None
        # The description property
        self._description: Optional[str] = None
        # The displayName property
        self._display_name: Optional[str] = None
        # The lastActionByUserId property
        self._last_action_by_user_id: Optional[str] = None
        # The lastActionDateTime property
        self._last_action_date_time: Optional[datetime] = None
        # The lastRunDateTime property
        self._last_run_date_time: Optional[datetime] = None
        # The notificationFinalDestinations property
        self._notification_final_destinations: Optional[notification_destination.NotificationDestination] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The ruleDefinition property
        self._rule_definition: Optional[managed_tenant_alert_rule_definition.ManagedTenantAlertRuleDefinition] = None
        # The severity property
        self._severity: Optional[alert_severity.AlertSeverity] = None
        # The targets property
        self._targets: Optional[List[notification_target.NotificationTarget]] = None
        # The tenantIds property
        self._tenant_ids: Optional[List[tenant_info.TenantInfo]] = None
    
    @property
    def created_by_user_id(self,) -> Optional[str]:
        """
        Gets the createdByUserId property value. The createdByUserId property
        Returns: Optional[str]
        """
        return self._created_by_user_id
    
    @created_by_user_id.setter
    def created_by_user_id(self,value: Optional[str] = None) -> None:
        """
        Sets the createdByUserId property value. The createdByUserId property
        Args:
            value: Value to set for the createdByUserId property.
        """
        self._created_by_user_id = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The createdDateTime property
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The createdDateTime property
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
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
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. The description property
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. The description property
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The displayName property
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The displayName property
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
            "alert_display_name": lambda n : setattr(self, 'alert_display_name', n.get_str_value()),
            "alerts": lambda n : setattr(self, 'alerts', n.get_collection_of_object_values(managed_tenant_alert.ManagedTenantAlert)),
            "alert_t_t_l": lambda n : setattr(self, 'alert_t_t_l', n.get_int_value()),
            "created_by_user_id": lambda n : setattr(self, 'created_by_user_id', n.get_str_value()),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "last_action_by_user_id": lambda n : setattr(self, 'last_action_by_user_id', n.get_str_value()),
            "last_action_date_time": lambda n : setattr(self, 'last_action_date_time', n.get_datetime_value()),
            "last_run_date_time": lambda n : setattr(self, 'last_run_date_time', n.get_datetime_value()),
            "notification_final_destinations": lambda n : setattr(self, 'notification_final_destinations', n.get_enum_value(notification_destination.NotificationDestination)),
            "rule_definition": lambda n : setattr(self, 'rule_definition', n.get_object_value(managed_tenant_alert_rule_definition.ManagedTenantAlertRuleDefinition)),
            "severity": lambda n : setattr(self, 'severity', n.get_enum_value(alert_severity.AlertSeverity)),
            "targets": lambda n : setattr(self, 'targets', n.get_collection_of_object_values(notification_target.NotificationTarget)),
            "tenant_ids": lambda n : setattr(self, 'tenant_ids', n.get_collection_of_object_values(tenant_info.TenantInfo)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_action_by_user_id(self,) -> Optional[str]:
        """
        Gets the lastActionByUserId property value. The lastActionByUserId property
        Returns: Optional[str]
        """
        return self._last_action_by_user_id
    
    @last_action_by_user_id.setter
    def last_action_by_user_id(self,value: Optional[str] = None) -> None:
        """
        Sets the lastActionByUserId property value. The lastActionByUserId property
        Args:
            value: Value to set for the lastActionByUserId property.
        """
        self._last_action_by_user_id = value
    
    @property
    def last_action_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastActionDateTime property value. The lastActionDateTime property
        Returns: Optional[datetime]
        """
        return self._last_action_date_time
    
    @last_action_date_time.setter
    def last_action_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastActionDateTime property value. The lastActionDateTime property
        Args:
            value: Value to set for the lastActionDateTime property.
        """
        self._last_action_date_time = value
    
    @property
    def last_run_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastRunDateTime property value. The lastRunDateTime property
        Returns: Optional[datetime]
        """
        return self._last_run_date_time
    
    @last_run_date_time.setter
    def last_run_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastRunDateTime property value. The lastRunDateTime property
        Args:
            value: Value to set for the lastRunDateTime property.
        """
        self._last_run_date_time = value
    
    @property
    def notification_final_destinations(self,) -> Optional[notification_destination.NotificationDestination]:
        """
        Gets the notificationFinalDestinations property value. The notificationFinalDestinations property
        Returns: Optional[notification_destination.NotificationDestination]
        """
        return self._notification_final_destinations
    
    @notification_final_destinations.setter
    def notification_final_destinations(self,value: Optional[notification_destination.NotificationDestination] = None) -> None:
        """
        Sets the notificationFinalDestinations property value. The notificationFinalDestinations property
        Args:
            value: Value to set for the notificationFinalDestinations property.
        """
        self._notification_final_destinations = value
    
    @property
    def rule_definition(self,) -> Optional[managed_tenant_alert_rule_definition.ManagedTenantAlertRuleDefinition]:
        """
        Gets the ruleDefinition property value. The ruleDefinition property
        Returns: Optional[managed_tenant_alert_rule_definition.ManagedTenantAlertRuleDefinition]
        """
        return self._rule_definition
    
    @rule_definition.setter
    def rule_definition(self,value: Optional[managed_tenant_alert_rule_definition.ManagedTenantAlertRuleDefinition] = None) -> None:
        """
        Sets the ruleDefinition property value. The ruleDefinition property
        Args:
            value: Value to set for the ruleDefinition property.
        """
        self._rule_definition = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("alertDisplayName", self.alert_display_name)
        writer.write_collection_of_object_values("alerts", self.alerts)
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
    
    @property
    def severity(self,) -> Optional[alert_severity.AlertSeverity]:
        """
        Gets the severity property value. The severity property
        Returns: Optional[alert_severity.AlertSeverity]
        """
        return self._severity
    
    @severity.setter
    def severity(self,value: Optional[alert_severity.AlertSeverity] = None) -> None:
        """
        Sets the severity property value. The severity property
        Args:
            value: Value to set for the severity property.
        """
        self._severity = value
    
    @property
    def targets(self,) -> Optional[List[notification_target.NotificationTarget]]:
        """
        Gets the targets property value. The targets property
        Returns: Optional[List[notification_target.NotificationTarget]]
        """
        return self._targets
    
    @targets.setter
    def targets(self,value: Optional[List[notification_target.NotificationTarget]] = None) -> None:
        """
        Sets the targets property value. The targets property
        Args:
            value: Value to set for the targets property.
        """
        self._targets = value
    
    @property
    def tenant_ids(self,) -> Optional[List[tenant_info.TenantInfo]]:
        """
        Gets the tenantIds property value. The tenantIds property
        Returns: Optional[List[tenant_info.TenantInfo]]
        """
        return self._tenant_ids
    
    @tenant_ids.setter
    def tenant_ids(self,value: Optional[List[tenant_info.TenantInfo]] = None) -> None:
        """
        Sets the tenantIds property value. The tenantIds property
        Args:
            value: Value to set for the tenantIds property.
        """
        self._tenant_ids = value
    

