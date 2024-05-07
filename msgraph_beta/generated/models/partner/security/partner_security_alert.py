from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ...entity import Entity
    from .activity_log import ActivityLog
    from .additional_data_dictionary import AdditionalDataDictionary
    from .affected_resource import AffectedResource
    from .security_alert_confidence import SecurityAlertConfidence
    from .security_alert_resolved_reason import SecurityAlertResolvedReason
    from .security_alert_severity import SecurityAlertSeverity
    from .security_alert_status import SecurityAlertStatus

from ...entity import Entity

@dataclass
class PartnerSecurityAlert(Entity):
    # The activityLogs property
    activity_logs: Optional[List[ActivityLog]] = None
    # The additionalDetails property
    additional_details: Optional[AdditionalDataDictionary] = None
    # The affectedResources property
    affected_resources: Optional[List[AffectedResource]] = None
    # The alertType property
    alert_type: Optional[str] = None
    # The catalogOfferId property
    catalog_offer_id: Optional[str] = None
    # The confidenceLevel property
    confidence_level: Optional[SecurityAlertConfidence] = None
    # The customerTenantId property
    customer_tenant_id: Optional[str] = None
    # The description property
    description: Optional[str] = None
    # The detectedDateTime property
    detected_date_time: Optional[datetime.datetime] = None
    # The displayName property
    display_name: Optional[str] = None
    # The firstObservedDateTime property
    first_observed_date_time: Optional[datetime.datetime] = None
    # The isTest property
    is_test: Optional[bool] = None
    # The lastObservedDateTime property
    last_observed_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The resolvedBy property
    resolved_by: Optional[str] = None
    # The resolvedOnDateTime property
    resolved_on_date_time: Optional[datetime.datetime] = None
    # The resolvedReason property
    resolved_reason: Optional[SecurityAlertResolvedReason] = None
    # The severity property
    severity: Optional[SecurityAlertSeverity] = None
    # The status property
    status: Optional[SecurityAlertStatus] = None
    # The subscriptionId property
    subscription_id: Optional[str] = None
    # The valueAddedResellerTenantId property
    value_added_reseller_tenant_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PartnerSecurityAlert:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PartnerSecurityAlert
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return PartnerSecurityAlert()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ...entity import Entity
        from .activity_log import ActivityLog
        from .additional_data_dictionary import AdditionalDataDictionary
        from .affected_resource import AffectedResource
        from .security_alert_confidence import SecurityAlertConfidence
        from .security_alert_resolved_reason import SecurityAlertResolvedReason
        from .security_alert_severity import SecurityAlertSeverity
        from .security_alert_status import SecurityAlertStatus

        from ...entity import Entity
        from .activity_log import ActivityLog
        from .additional_data_dictionary import AdditionalDataDictionary
        from .affected_resource import AffectedResource
        from .security_alert_confidence import SecurityAlertConfidence
        from .security_alert_resolved_reason import SecurityAlertResolvedReason
        from .security_alert_severity import SecurityAlertSeverity
        from .security_alert_status import SecurityAlertStatus

        fields: Dict[str, Callable[[Any], None]] = {
            "activityLogs": lambda n : setattr(self, 'activity_logs', n.get_collection_of_object_values(ActivityLog)),
            "additionalDetails": lambda n : setattr(self, 'additional_details', n.get_object_value(AdditionalDataDictionary)),
            "affectedResources": lambda n : setattr(self, 'affected_resources', n.get_collection_of_object_values(AffectedResource)),
            "alertType": lambda n : setattr(self, 'alert_type', n.get_str_value()),
            "catalogOfferId": lambda n : setattr(self, 'catalog_offer_id', n.get_str_value()),
            "confidenceLevel": lambda n : setattr(self, 'confidence_level', n.get_enum_value(SecurityAlertConfidence)),
            "customerTenantId": lambda n : setattr(self, 'customer_tenant_id', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "detectedDateTime": lambda n : setattr(self, 'detected_date_time', n.get_datetime_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "firstObservedDateTime": lambda n : setattr(self, 'first_observed_date_time', n.get_datetime_value()),
            "isTest": lambda n : setattr(self, 'is_test', n.get_bool_value()),
            "lastObservedDateTime": lambda n : setattr(self, 'last_observed_date_time', n.get_datetime_value()),
            "resolvedBy": lambda n : setattr(self, 'resolved_by', n.get_str_value()),
            "resolvedOnDateTime": lambda n : setattr(self, 'resolved_on_date_time', n.get_datetime_value()),
            "resolvedReason": lambda n : setattr(self, 'resolved_reason', n.get_enum_value(SecurityAlertResolvedReason)),
            "severity": lambda n : setattr(self, 'severity', n.get_enum_value(SecurityAlertSeverity)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(SecurityAlertStatus)),
            "subscriptionId": lambda n : setattr(self, 'subscription_id', n.get_str_value()),
            "valueAddedResellerTenantId": lambda n : setattr(self, 'value_added_reseller_tenant_id', n.get_str_value()),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("activityLogs", self.activity_logs)
        writer.write_object_value("additionalDetails", self.additional_details)
        writer.write_collection_of_object_values("affectedResources", self.affected_resources)
        writer.write_str_value("alertType", self.alert_type)
        writer.write_str_value("catalogOfferId", self.catalog_offer_id)
        writer.write_enum_value("confidenceLevel", self.confidence_level)
        writer.write_str_value("customerTenantId", self.customer_tenant_id)
        writer.write_str_value("description", self.description)
        writer.write_datetime_value("detectedDateTime", self.detected_date_time)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("firstObservedDateTime", self.first_observed_date_time)
        writer.write_bool_value("isTest", self.is_test)
        writer.write_datetime_value("lastObservedDateTime", self.last_observed_date_time)
        writer.write_str_value("resolvedBy", self.resolved_by)
        writer.write_datetime_value("resolvedOnDateTime", self.resolved_on_date_time)
        writer.write_enum_value("resolvedReason", self.resolved_reason)
        writer.write_enum_value("severity", self.severity)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("subscriptionId", self.subscription_id)
        writer.write_str_value("valueAddedResellerTenantId", self.value_added_reseller_tenant_id)
    

