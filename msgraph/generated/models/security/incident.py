from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import alert, alert_classification, alert_comment, alert_determination, alert_severity, incident_status, recommended_hunting_query
    from .. import entity

from .. import entity

@dataclass
class Incident(entity.Entity):
    # The list of related alerts. Supports $expand.
    alerts: Optional[List[alert.Alert]] = None
    # Owner of the incident, or null if no owner is assigned. Free editable text.
    assigned_to: Optional[str] = None
    # The specification for the incident. Possible values are: unknown, falsePositive, truePositive, informationalExpectedActivity, unknownFutureValue.
    classification: Optional[alert_classification.AlertClassification] = None
    # Array of comments created by the Security Operations (SecOps) team when the incident is managed.
    comments: Optional[List[alert_comment.AlertComment]] = None
    # Time when the incident was first created.
    created_date_time: Optional[datetime] = None
    # Array of custom tags associated with an incident.
    custom_tags: Optional[List[str]] = None
    # The description property
    description: Optional[str] = None
    # Specifies the determination of the incident. Possible values are: unknown, apt, malware, securityPersonnel, securityTesting, unwantedSoftware, other, multiStagedAttack, compromisedUser, phishing, maliciousUserActivity, clean, insufficientData, confirmedUserActivity, lineOfBusinessApplication, unknownFutureValue.
    determination: Optional[alert_determination.AlertDetermination] = None
    # The incident name.
    display_name: Optional[str] = None
    # The URL for the incident page in the Microsoft 365 Defender portal.
    incident_web_url: Optional[str] = None
    # Time when the incident was last updated.
    last_update_date_time: Optional[datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The recommendedActions property
    recommended_actions: Optional[str] = None
    # The recommendedHuntingQueries property
    recommended_hunting_queries: Optional[List[recommended_hunting_query.RecommendedHuntingQuery]] = None
    # Only populated in case an incident is grouped together with another incident, as part of the logic that processes incidents. In such a case, the status property is redirected.
    redirect_incident_id: Optional[str] = None
    # The severity property
    severity: Optional[alert_severity.AlertSeverity] = None
    # The status property
    status: Optional[incident_status.IncidentStatus] = None
    # The systemTags property
    system_tags: Optional[List[str]] = None
    # The Azure Active Directory tenant in which the alert was created.
    tenant_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Incident:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Incident
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Incident()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import alert, alert_classification, alert_comment, alert_determination, alert_severity, incident_status, recommended_hunting_query
        from .. import entity

        from . import alert, alert_classification, alert_comment, alert_determination, alert_severity, incident_status, recommended_hunting_query
        from .. import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "alerts": lambda n : setattr(self, 'alerts', n.get_collection_of_object_values(alert.Alert)),
            "assignedTo": lambda n : setattr(self, 'assigned_to', n.get_str_value()),
            "classification": lambda n : setattr(self, 'classification', n.get_enum_value(alert_classification.AlertClassification)),
            "comments": lambda n : setattr(self, 'comments', n.get_collection_of_object_values(alert_comment.AlertComment)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "customTags": lambda n : setattr(self, 'custom_tags', n.get_collection_of_primitive_values(str)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "determination": lambda n : setattr(self, 'determination', n.get_enum_value(alert_determination.AlertDetermination)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "incidentWebUrl": lambda n : setattr(self, 'incident_web_url', n.get_str_value()),
            "lastUpdateDateTime": lambda n : setattr(self, 'last_update_date_time', n.get_datetime_value()),
            "recommendedActions": lambda n : setattr(self, 'recommended_actions', n.get_str_value()),
            "recommendedHuntingQueries": lambda n : setattr(self, 'recommended_hunting_queries', n.get_collection_of_object_values(recommended_hunting_query.RecommendedHuntingQuery)),
            "redirectIncidentId": lambda n : setattr(self, 'redirect_incident_id', n.get_str_value()),
            "severity": lambda n : setattr(self, 'severity', n.get_enum_value(alert_severity.AlertSeverity)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(incident_status.IncidentStatus)),
            "systemTags": lambda n : setattr(self, 'system_tags', n.get_collection_of_primitive_values(str)),
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("alerts", self.alerts)
        writer.write_str_value("assignedTo", self.assigned_to)
        writer.write_enum_value("classification", self.classification)
        writer.write_collection_of_object_values("comments", self.comments)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_collection_of_primitive_values("customTags", self.custom_tags)
        writer.write_str_value("description", self.description)
        writer.write_enum_value("determination", self.determination)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("incidentWebUrl", self.incident_web_url)
        writer.write_datetime_value("lastUpdateDateTime", self.last_update_date_time)
        writer.write_str_value("recommendedActions", self.recommended_actions)
        writer.write_collection_of_object_values("recommendedHuntingQueries", self.recommended_hunting_queries)
        writer.write_str_value("redirectIncidentId", self.redirect_incident_id)
        writer.write_enum_value("severity", self.severity)
        writer.write_enum_value("status", self.status)
        writer.write_collection_of_primitive_values("systemTags", self.system_tags)
        writer.write_str_value("tenantId", self.tenant_id)
    

