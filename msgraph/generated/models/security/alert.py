from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import alert_classification, alert_comment, alert_determination, alert_evidence, alert_severity, alert_status, detection_source, service_source
    from .. import entity

from .. import entity

@dataclass
class Alert(entity.Entity):
    # The adversary or activity group that is associated with this alert.
    actor_display_name: Optional[str] = None
    # URL for the alert page in the Microsoft 365 Defender portal.
    alert_web_url: Optional[str] = None
    # Owner of the alert, or null if no owner is assigned.
    assigned_to: Optional[str] = None
    # The attack kill-chain category that the alert belongs to. Aligned with the MITRE ATT&CK framework.
    category: Optional[str] = None
    # Specifies whether the alert represents a true threat. Possible values are: unknown, falsePositive, truePositive, benignPositive, unknownFutureValue.
    classification: Optional[alert_classification.AlertClassification] = None
    # Array of comments created by the Security Operations (SecOps) team during the alert management process.
    comments: Optional[List[alert_comment.AlertComment]] = None
    # Time when Microsoft 365 Defender created the alert.
    created_date_time: Optional[datetime] = None
    # String value describing each alert.
    description: Optional[str] = None
    # Detection technology or sensor that identified the notable component or activity. Possible values are: unknown, microsoftDefenderForEndpoint, antivirus, smartScreen, customTi, microsoftDefenderForOffice365, automatedInvestigation, microsoftThreatExperts, customDetection, microsoftDefenderForIdentity, cloudAppSecurity, microsoft365Defender, azureAdIdentityProtection, manual, microsoftDataLossPrevention, appGovernancePolicy, appGovernanceDetection, unknownFutureValue, microsoftDefenderForCloud. Note that you must use the Prefer: include-unknown-enum-members request header to get the following value(s) in this evolvable enum: microsoftDefenderForCloud.
    detection_source: Optional[detection_source.DetectionSource] = None
    # The ID of the detector that triggered the alert.
    detector_id: Optional[str] = None
    # Specifies the result of the investigation, whether the alert represents a true attack and if so, the nature of the attack. Possible values are: unknown, apt, malware, securityPersonnel, securityTesting, unwantedSoftware, other, multiStagedAttack, compromisedUser, phishing, maliciousUserActivity, clean, insufficientData, confirmedUserActivity, lineOfBusinessApplication, unknownFutureValue.
    determination: Optional[alert_determination.AlertDetermination] = None
    # Collection of evidence related to the alert.
    evidence: Optional[List[alert_evidence.AlertEvidence]] = None
    # The earliest activity associated with the alert.
    first_activity_date_time: Optional[datetime] = None
    # Unique identifier to represent the incident this alert resource is associated with.
    incident_id: Optional[str] = None
    # URL for the incident page in the Microsoft 365 Defender portal.
    incident_web_url: Optional[str] = None
    # The oldest activity associated with the alert.
    last_activity_date_time: Optional[datetime] = None
    # Time when the alert was last updated at Microsoft 365 Defender.
    last_update_date_time: Optional[datetime] = None
    # The attack techniques, as aligned with the MITRE ATT&CK framework.
    mitre_techniques: Optional[List[str]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The ID of the alert as it appears in the security provider product that generated the alert.
    provider_alert_id: Optional[str] = None
    # Recommended response and remediation actions to take in the event this alert was generated.
    recommended_actions: Optional[str] = None
    # Time when the alert was resolved.
    resolved_date_time: Optional[datetime] = None
    # The serviceSource property
    service_source: Optional[service_source.ServiceSource] = None
    # The severity property
    severity: Optional[alert_severity.AlertSeverity] = None
    # The status property
    status: Optional[alert_status.AlertStatus] = None
    # The systemTags property
    system_tags: Optional[List[str]] = None
    # The Azure Active Directory tenant the alert was created in.
    tenant_id: Optional[str] = None
    # The threat associated with this alert.
    threat_display_name: Optional[str] = None
    # Threat family associated with this alert.
    threat_family_name: Optional[str] = None
    # Brief identifying string value describing the alert.
    title: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Alert:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Alert
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Alert()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import alert_classification, alert_comment, alert_determination, alert_evidence, alert_severity, alert_status, detection_source, service_source
        from .. import entity

        from . import alert_classification, alert_comment, alert_determination, alert_evidence, alert_severity, alert_status, detection_source, service_source
        from .. import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "actorDisplayName": lambda n : setattr(self, 'actor_display_name', n.get_str_value()),
            "alertWebUrl": lambda n : setattr(self, 'alert_web_url', n.get_str_value()),
            "assignedTo": lambda n : setattr(self, 'assigned_to', n.get_str_value()),
            "category": lambda n : setattr(self, 'category', n.get_str_value()),
            "classification": lambda n : setattr(self, 'classification', n.get_enum_value(alert_classification.AlertClassification)),
            "comments": lambda n : setattr(self, 'comments', n.get_collection_of_object_values(alert_comment.AlertComment)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "detectionSource": lambda n : setattr(self, 'detection_source', n.get_enum_value(detection_source.DetectionSource)),
            "detectorId": lambda n : setattr(self, 'detector_id', n.get_str_value()),
            "determination": lambda n : setattr(self, 'determination', n.get_enum_value(alert_determination.AlertDetermination)),
            "evidence": lambda n : setattr(self, 'evidence', n.get_collection_of_object_values(alert_evidence.AlertEvidence)),
            "firstActivityDateTime": lambda n : setattr(self, 'first_activity_date_time', n.get_datetime_value()),
            "incidentId": lambda n : setattr(self, 'incident_id', n.get_str_value()),
            "incidentWebUrl": lambda n : setattr(self, 'incident_web_url', n.get_str_value()),
            "lastActivityDateTime": lambda n : setattr(self, 'last_activity_date_time', n.get_datetime_value()),
            "lastUpdateDateTime": lambda n : setattr(self, 'last_update_date_time', n.get_datetime_value()),
            "mitreTechniques": lambda n : setattr(self, 'mitre_techniques', n.get_collection_of_primitive_values(str)),
            "providerAlertId": lambda n : setattr(self, 'provider_alert_id', n.get_str_value()),
            "recommendedActions": lambda n : setattr(self, 'recommended_actions', n.get_str_value()),
            "resolvedDateTime": lambda n : setattr(self, 'resolved_date_time', n.get_datetime_value()),
            "serviceSource": lambda n : setattr(self, 'service_source', n.get_enum_value(service_source.ServiceSource)),
            "severity": lambda n : setattr(self, 'severity', n.get_enum_value(alert_severity.AlertSeverity)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(alert_status.AlertStatus)),
            "systemTags": lambda n : setattr(self, 'system_tags', n.get_collection_of_primitive_values(str)),
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
            "threatDisplayName": lambda n : setattr(self, 'threat_display_name', n.get_str_value()),
            "threatFamilyName": lambda n : setattr(self, 'threat_family_name', n.get_str_value()),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
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
        writer.write_str_value("actorDisplayName", self.actor_display_name)
        writer.write_str_value("alertWebUrl", self.alert_web_url)
        writer.write_str_value("assignedTo", self.assigned_to)
        writer.write_str_value("category", self.category)
        writer.write_enum_value("classification", self.classification)
        writer.write_collection_of_object_values("comments", self.comments)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_enum_value("detectionSource", self.detection_source)
        writer.write_str_value("detectorId", self.detector_id)
        writer.write_enum_value("determination", self.determination)
        writer.write_collection_of_object_values("evidence", self.evidence)
        writer.write_datetime_value("firstActivityDateTime", self.first_activity_date_time)
        writer.write_str_value("incidentId", self.incident_id)
        writer.write_str_value("incidentWebUrl", self.incident_web_url)
        writer.write_datetime_value("lastActivityDateTime", self.last_activity_date_time)
        writer.write_datetime_value("lastUpdateDateTime", self.last_update_date_time)
        writer.write_collection_of_primitive_values("mitreTechniques", self.mitre_techniques)
        writer.write_str_value("providerAlertId", self.provider_alert_id)
        writer.write_str_value("recommendedActions", self.recommended_actions)
        writer.write_datetime_value("resolvedDateTime", self.resolved_date_time)
        writer.write_enum_value("serviceSource", self.service_source)
        writer.write_enum_value("severity", self.severity)
        writer.write_enum_value("status", self.status)
        writer.write_collection_of_primitive_values("systemTags", self.system_tags)
        writer.write_str_value("tenantId", self.tenant_id)
        writer.write_str_value("threatDisplayName", self.threat_display_name)
        writer.write_str_value("threatFamilyName", self.threat_family_name)
        writer.write_str_value("title", self.title)
    

