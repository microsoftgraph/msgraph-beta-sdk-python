from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
alert_data = lazy_import('msgraph.generated.models.managed_tenants.alert_data')
alert_data_reference_string = lazy_import('msgraph.generated.models.managed_tenants.alert_data_reference_string')
alert_severity = lazy_import('msgraph.generated.models.managed_tenants.alert_severity')
alert_status = lazy_import('msgraph.generated.models.managed_tenants.alert_status')
managed_tenant_alert_log = lazy_import('msgraph.generated.models.managed_tenants.managed_tenant_alert_log')
managed_tenant_alert_rule = lazy_import('msgraph.generated.models.managed_tenants.managed_tenant_alert_rule')
managed_tenant_api_notification = lazy_import('msgraph.generated.models.managed_tenants.managed_tenant_api_notification')
managed_tenant_email_notification = lazy_import('msgraph.generated.models.managed_tenants.managed_tenant_email_notification')

class ManagedTenantAlert(entity.Entity):
    @property
    def alert_data(self,) -> Optional[alert_data.AlertData]:
        """
        Gets the alertData property value. The alertData property
        Returns: Optional[alert_data.AlertData]
        """
        return self._alert_data
    
    @alert_data.setter
    def alert_data(self,value: Optional[alert_data.AlertData] = None) -> None:
        """
        Sets the alertData property value. The alertData property
        Args:
            value: Value to set for the alertData property.
        """
        self._alert_data = value
    
    @property
    def alert_data_reference_strings(self,) -> Optional[List[alert_data_reference_string.AlertDataReferenceString]]:
        """
        Gets the alertDataReferenceStrings property value. The alertDataReferenceStrings property
        Returns: Optional[List[alert_data_reference_string.AlertDataReferenceString]]
        """
        return self._alert_data_reference_strings
    
    @alert_data_reference_strings.setter
    def alert_data_reference_strings(self,value: Optional[List[alert_data_reference_string.AlertDataReferenceString]] = None) -> None:
        """
        Sets the alertDataReferenceStrings property value. The alertDataReferenceStrings property
        Args:
            value: Value to set for the alertDataReferenceStrings property.
        """
        self._alert_data_reference_strings = value
    
    @property
    def alert_logs(self,) -> Optional[List[managed_tenant_alert_log.ManagedTenantAlertLog]]:
        """
        Gets the alertLogs property value. The alertLogs property
        Returns: Optional[List[managed_tenant_alert_log.ManagedTenantAlertLog]]
        """
        return self._alert_logs
    
    @alert_logs.setter
    def alert_logs(self,value: Optional[List[managed_tenant_alert_log.ManagedTenantAlertLog]] = None) -> None:
        """
        Sets the alertLogs property value. The alertLogs property
        Args:
            value: Value to set for the alertLogs property.
        """
        self._alert_logs = value
    
    @property
    def alert_rule(self,) -> Optional[managed_tenant_alert_rule.ManagedTenantAlertRule]:
        """
        Gets the alertRule property value. The alertRule property
        Returns: Optional[managed_tenant_alert_rule.ManagedTenantAlertRule]
        """
        return self._alert_rule
    
    @alert_rule.setter
    def alert_rule(self,value: Optional[managed_tenant_alert_rule.ManagedTenantAlertRule] = None) -> None:
        """
        Sets the alertRule property value. The alertRule property
        Args:
            value: Value to set for the alertRule property.
        """
        self._alert_rule = value
    
    @property
    def alert_rule_display_name(self,) -> Optional[str]:
        """
        Gets the alertRuleDisplayName property value. The alertRuleDisplayName property
        Returns: Optional[str]
        """
        return self._alert_rule_display_name
    
    @alert_rule_display_name.setter
    def alert_rule_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the alertRuleDisplayName property value. The alertRuleDisplayName property
        Args:
            value: Value to set for the alertRuleDisplayName property.
        """
        self._alert_rule_display_name = value
    
    @property
    def api_notifications(self,) -> Optional[List[managed_tenant_api_notification.ManagedTenantApiNotification]]:
        """
        Gets the apiNotifications property value. The apiNotifications property
        Returns: Optional[List[managed_tenant_api_notification.ManagedTenantApiNotification]]
        """
        return self._api_notifications
    
    @api_notifications.setter
    def api_notifications(self,value: Optional[List[managed_tenant_api_notification.ManagedTenantApiNotification]] = None) -> None:
        """
        Sets the apiNotifications property value. The apiNotifications property
        Args:
            value: Value to set for the apiNotifications property.
        """
        self._api_notifications = value
    
    @property
    def assigned_to_user_id(self,) -> Optional[str]:
        """
        Gets the assignedToUserId property value. The assignedToUserId property
        Returns: Optional[str]
        """
        return self._assigned_to_user_id
    
    @assigned_to_user_id.setter
    def assigned_to_user_id(self,value: Optional[str] = None) -> None:
        """
        Sets the assignedToUserId property value. The assignedToUserId property
        Args:
            value: Value to set for the assignedToUserId property.
        """
        self._assigned_to_user_id = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new managedTenantAlert and sets the default values.
        """
        super().__init__()
        # The alertData property
        self._alert_data: Optional[alert_data.AlertData] = None
        # The alertDataReferenceStrings property
        self._alert_data_reference_strings: Optional[List[alert_data_reference_string.AlertDataReferenceString]] = None
        # The alertLogs property
        self._alert_logs: Optional[List[managed_tenant_alert_log.ManagedTenantAlertLog]] = None
        # The alertRule property
        self._alert_rule: Optional[managed_tenant_alert_rule.ManagedTenantAlertRule] = None
        # The alertRuleDisplayName property
        self._alert_rule_display_name: Optional[str] = None
        # The apiNotifications property
        self._api_notifications: Optional[List[managed_tenant_api_notification.ManagedTenantApiNotification]] = None
        # The assignedToUserId property
        self._assigned_to_user_id: Optional[str] = None
        # The correlationCount property
        self._correlation_count: Optional[int] = None
        # The correlationId property
        self._correlation_id: Optional[str] = None
        # The createdByUserId property
        self._created_by_user_id: Optional[str] = None
        # The createdDateTime property
        self._created_date_time: Optional[datetime] = None
        # The emailNotifications property
        self._email_notifications: Optional[List[managed_tenant_email_notification.ManagedTenantEmailNotification]] = None
        # The lastActionByUserId property
        self._last_action_by_user_id: Optional[str] = None
        # The lastActionDateTime property
        self._last_action_date_time: Optional[datetime] = None
        # The message property
        self._message: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The severity property
        self._severity: Optional[alert_severity.AlertSeverity] = None
        # The status property
        self._status: Optional[alert_status.AlertStatus] = None
        # The tenantId property
        self._tenant_id: Optional[str] = None
        # The title property
        self._title: Optional[str] = None
    
    @property
    def correlation_count(self,) -> Optional[int]:
        """
        Gets the correlationCount property value. The correlationCount property
        Returns: Optional[int]
        """
        return self._correlation_count
    
    @correlation_count.setter
    def correlation_count(self,value: Optional[int] = None) -> None:
        """
        Sets the correlationCount property value. The correlationCount property
        Args:
            value: Value to set for the correlationCount property.
        """
        self._correlation_count = value
    
    @property
    def correlation_id(self,) -> Optional[str]:
        """
        Gets the correlationId property value. The correlationId property
        Returns: Optional[str]
        """
        return self._correlation_id
    
    @correlation_id.setter
    def correlation_id(self,value: Optional[str] = None) -> None:
        """
        Sets the correlationId property value. The correlationId property
        Args:
            value: Value to set for the correlationId property.
        """
        self._correlation_id = value
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ManagedTenantAlert:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ManagedTenantAlert
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ManagedTenantAlert()
    
    @property
    def email_notifications(self,) -> Optional[List[managed_tenant_email_notification.ManagedTenantEmailNotification]]:
        """
        Gets the emailNotifications property value. The emailNotifications property
        Returns: Optional[List[managed_tenant_email_notification.ManagedTenantEmailNotification]]
        """
        return self._email_notifications
    
    @email_notifications.setter
    def email_notifications(self,value: Optional[List[managed_tenant_email_notification.ManagedTenantEmailNotification]] = None) -> None:
        """
        Sets the emailNotifications property value. The emailNotifications property
        Args:
            value: Value to set for the emailNotifications property.
        """
        self._email_notifications = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "alert_data": lambda n : setattr(self, 'alert_data', n.get_object_value(alert_data.AlertData)),
            "alert_data_reference_strings": lambda n : setattr(self, 'alert_data_reference_strings', n.get_collection_of_object_values(alert_data_reference_string.AlertDataReferenceString)),
            "alert_logs": lambda n : setattr(self, 'alert_logs', n.get_collection_of_object_values(managed_tenant_alert_log.ManagedTenantAlertLog)),
            "alert_rule": lambda n : setattr(self, 'alert_rule', n.get_object_value(managed_tenant_alert_rule.ManagedTenantAlertRule)),
            "alert_rule_display_name": lambda n : setattr(self, 'alert_rule_display_name', n.get_str_value()),
            "api_notifications": lambda n : setattr(self, 'api_notifications', n.get_collection_of_object_values(managed_tenant_api_notification.ManagedTenantApiNotification)),
            "assigned_to_user_id": lambda n : setattr(self, 'assigned_to_user_id', n.get_str_value()),
            "correlation_count": lambda n : setattr(self, 'correlation_count', n.get_int_value()),
            "correlation_id": lambda n : setattr(self, 'correlation_id', n.get_str_value()),
            "created_by_user_id": lambda n : setattr(self, 'created_by_user_id', n.get_str_value()),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "email_notifications": lambda n : setattr(self, 'email_notifications', n.get_collection_of_object_values(managed_tenant_email_notification.ManagedTenantEmailNotification)),
            "last_action_by_user_id": lambda n : setattr(self, 'last_action_by_user_id', n.get_str_value()),
            "last_action_date_time": lambda n : setattr(self, 'last_action_date_time', n.get_datetime_value()),
            "message": lambda n : setattr(self, 'message', n.get_str_value()),
            "severity": lambda n : setattr(self, 'severity', n.get_enum_value(alert_severity.AlertSeverity)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(alert_status.AlertStatus)),
            "tenant_id": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
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
    def message(self,) -> Optional[str]:
        """
        Gets the message property value. The message property
        Returns: Optional[str]
        """
        return self._message
    
    @message.setter
    def message(self,value: Optional[str] = None) -> None:
        """
        Sets the message property value. The message property
        Args:
            value: Value to set for the message property.
        """
        self._message = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("alertData", self.alert_data)
        writer.write_collection_of_object_values("alertDataReferenceStrings", self.alert_data_reference_strings)
        writer.write_collection_of_object_values("alertLogs", self.alert_logs)
        writer.write_object_value("alertRule", self.alert_rule)
        writer.write_str_value("alertRuleDisplayName", self.alert_rule_display_name)
        writer.write_collection_of_object_values("apiNotifications", self.api_notifications)
        writer.write_str_value("assignedToUserId", self.assigned_to_user_id)
        writer.write_int_value("correlationCount", self.correlation_count)
        writer.write_str_value("correlationId", self.correlation_id)
        writer.write_str_value("createdByUserId", self.created_by_user_id)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_collection_of_object_values("emailNotifications", self.email_notifications)
        writer.write_str_value("lastActionByUserId", self.last_action_by_user_id)
        writer.write_datetime_value("lastActionDateTime", self.last_action_date_time)
        writer.write_str_value("message", self.message)
        writer.write_enum_value("severity", self.severity)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("tenantId", self.tenant_id)
        writer.write_str_value("title", self.title)
    
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
    def status(self,) -> Optional[alert_status.AlertStatus]:
        """
        Gets the status property value. The status property
        Returns: Optional[alert_status.AlertStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[alert_status.AlertStatus] = None) -> None:
        """
        Sets the status property value. The status property
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    
    @property
    def tenant_id(self,) -> Optional[str]:
        """
        Gets the tenantId property value. The tenantId property
        Returns: Optional[str]
        """
        return self._tenant_id
    
    @tenant_id.setter
    def tenant_id(self,value: Optional[str] = None) -> None:
        """
        Sets the tenantId property value. The tenantId property
        Args:
            value: Value to set for the tenantId property.
        """
        self._tenant_id = value
    
    @property
    def title(self,) -> Optional[str]:
        """
        Gets the title property value. The title property
        Returns: Optional[str]
        """
        return self._title
    
    @title.setter
    def title(self,value: Optional[str] = None) -> None:
        """
        Sets the title property value. The title property
        Args:
            value: Value to set for the title property.
        """
        self._title = value
    

