from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class AuditEvent(entity.Entity):
    """
    Provides operations to manage the collection of accessReviewDecision entities.
    """
    @property
    def activity(self,) -> Optional[str]:
        """
        Gets the activity property value. A string which uniquely represents the operation that occurred. Required. Read-only.
        Returns: Optional[str]
        """
        return self._activity
    
    @activity.setter
    def activity(self,value: Optional[str] = None) -> None:
        """
        Sets the activity property value. A string which uniquely represents the operation that occurred. Required. Read-only.
        Args:
            value: Value to set for the activity property.
        """
        self._activity = value
    
    @property
    def activity_date_time(self,) -> Optional[datetime]:
        """
        Gets the activityDateTime property value. The time when the activity ocurred. Required. Read-only.
        Returns: Optional[datetime]
        """
        return self._activity_date_time
    
    @activity_date_time.setter
    def activity_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the activityDateTime property value. The time when the activity ocurred. Required. Read-only.
        Args:
            value: Value to set for the activityDateTime property.
        """
        self._activity_date_time = value
    
    @property
    def activity_id(self,) -> Optional[str]:
        """
        Gets the activityId property value. The identifier of the activity request that made the audit event. Required. Read-only.
        Returns: Optional[str]
        """
        return self._activity_id
    
    @activity_id.setter
    def activity_id(self,value: Optional[str] = None) -> None:
        """
        Sets the activityId property value. The identifier of the activity request that made the audit event. Required. Read-only.
        Args:
            value: Value to set for the activityId property.
        """
        self._activity_id = value
    
    @property
    def category(self,) -> Optional[str]:
        """
        Gets the category property value. A category which represents a logical grouping of activities. Required. Read-only.
        Returns: Optional[str]
        """
        return self._category
    
    @category.setter
    def category(self,value: Optional[str] = None) -> None:
        """
        Sets the category property value. A category which represents a logical grouping of activities. Required. Read-only.
        Args:
            value: Value to set for the category property.
        """
        self._category = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new auditEvent and sets the default values.
        """
        super().__init__()
        # A string which uniquely represents the operation that occurred. Required. Read-only.
        self._activity: Optional[str] = None
        # The time when the activity ocurred. Required. Read-only.
        self._activity_date_time: Optional[datetime] = None
        # The identifier of the activity request that made the audit event. Required. Read-only.
        self._activity_id: Optional[str] = None
        # A category which represents a logical grouping of activities. Required. Read-only.
        self._category: Optional[str] = None
        # The HTTP verb that was used when making the API request. Required. Read-only.
        self._http_verb: Optional[str] = None
        # The identifier of the app that was used to make the request. Required. Read-only.
        self._initiated_by_app_id: Optional[str] = None
        # The UPN of the user who initiated the activity. Required. Read-only.
        self._initiated_by_upn: Optional[str] = None
        # The identifier of the user who initiated the activity. Required. Read-only.
        self._initiated_by_user_id: Optional[str] = None
        # The IP address of where the activity was initiated. This may be an IPv4 or IPv6 address. Required. Read-only.
        self._ip_address: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The raw HTTP request body. Some sensitive information may be removed.
        self._request_body: Optional[str] = None
        # The raw HTTP request URL. Required. Read-only.
        self._request_url: Optional[str] = None
        # The collection of Azure Active Directory tenant identifiers for the managed tenants that were impacted by this change. This is formatted as a list of comma-separated values. Required. Read-only.
        self._tenant_ids: Optional[str] = None
        # The collection of tenant names that were impacted by this change. This is formatted as a list of comma-separated values. Required. Read-only.
        self._tenant_names: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AuditEvent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AuditEvent
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AuditEvent()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "activity": lambda n : setattr(self, 'activity', n.get_str_value()),
            "activity_date_time": lambda n : setattr(self, 'activity_date_time', n.get_datetime_value()),
            "activity_id": lambda n : setattr(self, 'activity_id', n.get_str_value()),
            "category": lambda n : setattr(self, 'category', n.get_str_value()),
            "http_verb": lambda n : setattr(self, 'http_verb', n.get_str_value()),
            "initiated_by_app_id": lambda n : setattr(self, 'initiated_by_app_id', n.get_str_value()),
            "initiated_by_upn": lambda n : setattr(self, 'initiated_by_upn', n.get_str_value()),
            "initiated_by_user_id": lambda n : setattr(self, 'initiated_by_user_id', n.get_str_value()),
            "ip_address": lambda n : setattr(self, 'ip_address', n.get_str_value()),
            "request_body": lambda n : setattr(self, 'request_body', n.get_str_value()),
            "request_url": lambda n : setattr(self, 'request_url', n.get_str_value()),
            "tenant_ids": lambda n : setattr(self, 'tenant_ids', n.get_str_value()),
            "tenant_names": lambda n : setattr(self, 'tenant_names', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def http_verb(self,) -> Optional[str]:
        """
        Gets the httpVerb property value. The HTTP verb that was used when making the API request. Required. Read-only.
        Returns: Optional[str]
        """
        return self._http_verb
    
    @http_verb.setter
    def http_verb(self,value: Optional[str] = None) -> None:
        """
        Sets the httpVerb property value. The HTTP verb that was used when making the API request. Required. Read-only.
        Args:
            value: Value to set for the httpVerb property.
        """
        self._http_verb = value
    
    @property
    def initiated_by_app_id(self,) -> Optional[str]:
        """
        Gets the initiatedByAppId property value. The identifier of the app that was used to make the request. Required. Read-only.
        Returns: Optional[str]
        """
        return self._initiated_by_app_id
    
    @initiated_by_app_id.setter
    def initiated_by_app_id(self,value: Optional[str] = None) -> None:
        """
        Sets the initiatedByAppId property value. The identifier of the app that was used to make the request. Required. Read-only.
        Args:
            value: Value to set for the initiatedByAppId property.
        """
        self._initiated_by_app_id = value
    
    @property
    def initiated_by_upn(self,) -> Optional[str]:
        """
        Gets the initiatedByUpn property value. The UPN of the user who initiated the activity. Required. Read-only.
        Returns: Optional[str]
        """
        return self._initiated_by_upn
    
    @initiated_by_upn.setter
    def initiated_by_upn(self,value: Optional[str] = None) -> None:
        """
        Sets the initiatedByUpn property value. The UPN of the user who initiated the activity. Required. Read-only.
        Args:
            value: Value to set for the initiatedByUpn property.
        """
        self._initiated_by_upn = value
    
    @property
    def initiated_by_user_id(self,) -> Optional[str]:
        """
        Gets the initiatedByUserId property value. The identifier of the user who initiated the activity. Required. Read-only.
        Returns: Optional[str]
        """
        return self._initiated_by_user_id
    
    @initiated_by_user_id.setter
    def initiated_by_user_id(self,value: Optional[str] = None) -> None:
        """
        Sets the initiatedByUserId property value. The identifier of the user who initiated the activity. Required. Read-only.
        Args:
            value: Value to set for the initiatedByUserId property.
        """
        self._initiated_by_user_id = value
    
    @property
    def ip_address(self,) -> Optional[str]:
        """
        Gets the ipAddress property value. The IP address of where the activity was initiated. This may be an IPv4 or IPv6 address. Required. Read-only.
        Returns: Optional[str]
        """
        return self._ip_address
    
    @ip_address.setter
    def ip_address(self,value: Optional[str] = None) -> None:
        """
        Sets the ipAddress property value. The IP address of where the activity was initiated. This may be an IPv4 or IPv6 address. Required. Read-only.
        Args:
            value: Value to set for the ipAddress property.
        """
        self._ip_address = value
    
    @property
    def request_body(self,) -> Optional[str]:
        """
        Gets the requestBody property value. The raw HTTP request body. Some sensitive information may be removed.
        Returns: Optional[str]
        """
        return self._request_body
    
    @request_body.setter
    def request_body(self,value: Optional[str] = None) -> None:
        """
        Sets the requestBody property value. The raw HTTP request body. Some sensitive information may be removed.
        Args:
            value: Value to set for the requestBody property.
        """
        self._request_body = value
    
    @property
    def request_url(self,) -> Optional[str]:
        """
        Gets the requestUrl property value. The raw HTTP request URL. Required. Read-only.
        Returns: Optional[str]
        """
        return self._request_url
    
    @request_url.setter
    def request_url(self,value: Optional[str] = None) -> None:
        """
        Sets the requestUrl property value. The raw HTTP request URL. Required. Read-only.
        Args:
            value: Value to set for the requestUrl property.
        """
        self._request_url = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("activity", self.activity)
        writer.write_datetime_value("activityDateTime", self.activity_date_time)
        writer.write_str_value("activityId", self.activity_id)
        writer.write_str_value("category", self.category)
        writer.write_str_value("httpVerb", self.http_verb)
        writer.write_str_value("initiatedByAppId", self.initiated_by_app_id)
        writer.write_str_value("initiatedByUpn", self.initiated_by_upn)
        writer.write_str_value("initiatedByUserId", self.initiated_by_user_id)
        writer.write_str_value("ipAddress", self.ip_address)
        writer.write_str_value("requestBody", self.request_body)
        writer.write_str_value("requestUrl", self.request_url)
        writer.write_str_value("tenantIds", self.tenant_ids)
        writer.write_str_value("tenantNames", self.tenant_names)
    
    @property
    def tenant_ids(self,) -> Optional[str]:
        """
        Gets the tenantIds property value. The collection of Azure Active Directory tenant identifiers for the managed tenants that were impacted by this change. This is formatted as a list of comma-separated values. Required. Read-only.
        Returns: Optional[str]
        """
        return self._tenant_ids
    
    @tenant_ids.setter
    def tenant_ids(self,value: Optional[str] = None) -> None:
        """
        Sets the tenantIds property value. The collection of Azure Active Directory tenant identifiers for the managed tenants that were impacted by this change. This is formatted as a list of comma-separated values. Required. Read-only.
        Args:
            value: Value to set for the tenantIds property.
        """
        self._tenant_ids = value
    
    @property
    def tenant_names(self,) -> Optional[str]:
        """
        Gets the tenantNames property value. The collection of tenant names that were impacted by this change. This is formatted as a list of comma-separated values. Required. Read-only.
        Returns: Optional[str]
        """
        return self._tenant_names
    
    @tenant_names.setter
    def tenant_names(self,value: Optional[str] = None) -> None:
        """
        Sets the tenantNames property value. The collection of tenant names that were impacted by this change. This is formatted as a list of comma-separated values. Required. Read-only.
        Args:
            value: Value to set for the tenantNames property.
        """
        self._tenant_names = value
    

