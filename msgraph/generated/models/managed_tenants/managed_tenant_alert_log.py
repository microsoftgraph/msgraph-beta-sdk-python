from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
alert_log_content = lazy_import('msgraph.generated.models.managed_tenants.alert_log_content')
managed_tenant_alert = lazy_import('msgraph.generated.models.managed_tenants.managed_tenant_alert')

class ManagedTenantAlertLog(entity.Entity):
    """
    Provides operations to manage the collection of accessReviewDecision entities.
    """
    @property
    def alert(self,) -> Optional[managed_tenant_alert.ManagedTenantAlert]:
        """
        Gets the alert property value. The alert property
        Returns: Optional[managed_tenant_alert.ManagedTenantAlert]
        """
        return self._alert
    
    @alert.setter
    def alert(self,value: Optional[managed_tenant_alert.ManagedTenantAlert] = None) -> None:
        """
        Sets the alert property value. The alert property
        Args:
            value: Value to set for the alert property.
        """
        self._alert = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new managedTenantAlertLog and sets the default values.
        """
        super().__init__()
        # The alert property
        self._alert: Optional[managed_tenant_alert.ManagedTenantAlert] = None
        # The content property
        self._content: Optional[alert_log_content.AlertLogContent] = None
        # The createdByUserId property
        self._created_by_user_id: Optional[str] = None
        # The createdDateTime property
        self._created_date_time: Optional[datetime] = None
        # The lastActionByUserId property
        self._last_action_by_user_id: Optional[str] = None
        # The lastActionDateTime property
        self._last_action_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @property
    def content(self,) -> Optional[alert_log_content.AlertLogContent]:
        """
        Gets the content property value. The content property
        Returns: Optional[alert_log_content.AlertLogContent]
        """
        return self._content
    
    @content.setter
    def content(self,value: Optional[alert_log_content.AlertLogContent] = None) -> None:
        """
        Sets the content property value. The content property
        Args:
            value: Value to set for the content property.
        """
        self._content = value
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ManagedTenantAlertLog:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ManagedTenantAlertLog
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ManagedTenantAlertLog()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "alert": lambda n : setattr(self, 'alert', n.get_object_value(managed_tenant_alert.ManagedTenantAlert)),
            "content": lambda n : setattr(self, 'content', n.get_object_value(alert_log_content.AlertLogContent)),
            "created_by_user_id": lambda n : setattr(self, 'created_by_user_id', n.get_str_value()),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "last_action_by_user_id": lambda n : setattr(self, 'last_action_by_user_id', n.get_str_value()),
            "last_action_date_time": lambda n : setattr(self, 'last_action_date_time', n.get_datetime_value()),
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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("alert", self.alert)
        writer.write_object_value("content", self.content)
        writer.write_str_value("createdByUserId", self.created_by_user_id)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("lastActionByUserId", self.last_action_by_user_id)
        writer.write_datetime_value("lastActionDateTime", self.last_action_date_time)
    

