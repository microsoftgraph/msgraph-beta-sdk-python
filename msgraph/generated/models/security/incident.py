from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import alert, alert_classification, alert_comment, alert_determination, alert_severity, incident_status, recommended_hunting_query
    from .. import entity

from .. import entity

class Incident(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new incident and sets the default values.
        """
        super().__init__()
        # The list of related alerts. Supports $expand.
        self._alerts: Optional[List[alert.Alert]] = None
        # Owner of the incident, or null if no owner is assigned. Free editable text.
        self._assigned_to: Optional[str] = None
        # The specification for the incident. Possible values are: unknown, falsePositive, truePositive, informationalExpectedActivity, unknownFutureValue.
        self._classification: Optional[alert_classification.AlertClassification] = None
        # Array of comments created by the Security Operations (SecOps) team when the incident is managed.
        self._comments: Optional[List[alert_comment.AlertComment]] = None
        # Time when the incident was first created.
        self._created_date_time: Optional[datetime] = None
        # Array of custom tags associated with an incident.
        self._custom_tags: Optional[List[str]] = None
        # The description property
        self._description: Optional[str] = None
        # Specifies the determination of the incident. Possible values are: unknown, apt, malware, securityPersonnel, securityTesting, unwantedSoftware, other, multiStagedAttack, compromisedUser, phishing, maliciousUserActivity, clean, insufficientData, confirmedUserActivity, lineOfBusinessApplication, unknownFutureValue.
        self._determination: Optional[alert_determination.AlertDetermination] = None
        # The incident name.
        self._display_name: Optional[str] = None
        # The URL for the incident page in the Microsoft 365 Defender portal.
        self._incident_web_url: Optional[str] = None
        # Time when the incident was last updated.
        self._last_update_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The recommendedActions property
        self._recommended_actions: Optional[str] = None
        # The recommendedHuntingQueries property
        self._recommended_hunting_queries: Optional[List[recommended_hunting_query.RecommendedHuntingQuery]] = None
        # Only populated in case an incident is grouped together with another incident, as part of the logic that processes incidents. In such a case, the status property is redirected.
        self._redirect_incident_id: Optional[str] = None
        # The severity property
        self._severity: Optional[alert_severity.AlertSeverity] = None
        # The status property
        self._status: Optional[incident_status.IncidentStatus] = None
        # The systemTags property
        self._system_tags: Optional[List[str]] = None
        # The Azure Active Directory tenant in which the alert was created.
        self._tenant_id: Optional[str] = None
    
    @property
    def alerts(self,) -> Optional[List[alert.Alert]]:
        """
        Gets the alerts property value. The list of related alerts. Supports $expand.
        Returns: Optional[List[alert.Alert]]
        """
        return self._alerts
    
    @alerts.setter
    def alerts(self,value: Optional[List[alert.Alert]] = None) -> None:
        """
        Sets the alerts property value. The list of related alerts. Supports $expand.
        Args:
            value: Value to set for the alerts property.
        """
        self._alerts = value
    
    @property
    def assigned_to(self,) -> Optional[str]:
        """
        Gets the assignedTo property value. Owner of the incident, or null if no owner is assigned. Free editable text.
        Returns: Optional[str]
        """
        return self._assigned_to
    
    @assigned_to.setter
    def assigned_to(self,value: Optional[str] = None) -> None:
        """
        Sets the assignedTo property value. Owner of the incident, or null if no owner is assigned. Free editable text.
        Args:
            value: Value to set for the assigned_to property.
        """
        self._assigned_to = value
    
    @property
    def classification(self,) -> Optional[alert_classification.AlertClassification]:
        """
        Gets the classification property value. The specification for the incident. Possible values are: unknown, falsePositive, truePositive, informationalExpectedActivity, unknownFutureValue.
        Returns: Optional[alert_classification.AlertClassification]
        """
        return self._classification
    
    @classification.setter
    def classification(self,value: Optional[alert_classification.AlertClassification] = None) -> None:
        """
        Sets the classification property value. The specification for the incident. Possible values are: unknown, falsePositive, truePositive, informationalExpectedActivity, unknownFutureValue.
        Args:
            value: Value to set for the classification property.
        """
        self._classification = value
    
    @property
    def comments(self,) -> Optional[List[alert_comment.AlertComment]]:
        """
        Gets the comments property value. Array of comments created by the Security Operations (SecOps) team when the incident is managed.
        Returns: Optional[List[alert_comment.AlertComment]]
        """
        return self._comments
    
    @comments.setter
    def comments(self,value: Optional[List[alert_comment.AlertComment]] = None) -> None:
        """
        Sets the comments property value. Array of comments created by the Security Operations (SecOps) team when the incident is managed.
        Args:
            value: Value to set for the comments property.
        """
        self._comments = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. Time when the incident was first created.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. Time when the incident was first created.
        Args:
            value: Value to set for the created_date_time property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Incident:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Incident
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Incident()
    
    @property
    def custom_tags(self,) -> Optional[List[str]]:
        """
        Gets the customTags property value. Array of custom tags associated with an incident.
        Returns: Optional[List[str]]
        """
        return self._custom_tags
    
    @custom_tags.setter
    def custom_tags(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the customTags property value. Array of custom tags associated with an incident.
        Args:
            value: Value to set for the custom_tags property.
        """
        self._custom_tags = value
    
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
    def determination(self,) -> Optional[alert_determination.AlertDetermination]:
        """
        Gets the determination property value. Specifies the determination of the incident. Possible values are: unknown, apt, malware, securityPersonnel, securityTesting, unwantedSoftware, other, multiStagedAttack, compromisedUser, phishing, maliciousUserActivity, clean, insufficientData, confirmedUserActivity, lineOfBusinessApplication, unknownFutureValue.
        Returns: Optional[alert_determination.AlertDetermination]
        """
        return self._determination
    
    @determination.setter
    def determination(self,value: Optional[alert_determination.AlertDetermination] = None) -> None:
        """
        Sets the determination property value. Specifies the determination of the incident. Possible values are: unknown, apt, malware, securityPersonnel, securityTesting, unwantedSoftware, other, multiStagedAttack, compromisedUser, phishing, maliciousUserActivity, clean, insufficientData, confirmedUserActivity, lineOfBusinessApplication, unknownFutureValue.
        Args:
            value: Value to set for the determination property.
        """
        self._determination = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The incident name.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The incident name.
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
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
    
    @property
    def incident_web_url(self,) -> Optional[str]:
        """
        Gets the incidentWebUrl property value. The URL for the incident page in the Microsoft 365 Defender portal.
        Returns: Optional[str]
        """
        return self._incident_web_url
    
    @incident_web_url.setter
    def incident_web_url(self,value: Optional[str] = None) -> None:
        """
        Sets the incidentWebUrl property value. The URL for the incident page in the Microsoft 365 Defender portal.
        Args:
            value: Value to set for the incident_web_url property.
        """
        self._incident_web_url = value
    
    @property
    def last_update_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastUpdateDateTime property value. Time when the incident was last updated.
        Returns: Optional[datetime]
        """
        return self._last_update_date_time
    
    @last_update_date_time.setter
    def last_update_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastUpdateDateTime property value. Time when the incident was last updated.
        Args:
            value: Value to set for the last_update_date_time property.
        """
        self._last_update_date_time = value
    
    @property
    def recommended_actions(self,) -> Optional[str]:
        """
        Gets the recommendedActions property value. The recommendedActions property
        Returns: Optional[str]
        """
        return self._recommended_actions
    
    @recommended_actions.setter
    def recommended_actions(self,value: Optional[str] = None) -> None:
        """
        Sets the recommendedActions property value. The recommendedActions property
        Args:
            value: Value to set for the recommended_actions property.
        """
        self._recommended_actions = value
    
    @property
    def recommended_hunting_queries(self,) -> Optional[List[recommended_hunting_query.RecommendedHuntingQuery]]:
        """
        Gets the recommendedHuntingQueries property value. The recommendedHuntingQueries property
        Returns: Optional[List[recommended_hunting_query.RecommendedHuntingQuery]]
        """
        return self._recommended_hunting_queries
    
    @recommended_hunting_queries.setter
    def recommended_hunting_queries(self,value: Optional[List[recommended_hunting_query.RecommendedHuntingQuery]] = None) -> None:
        """
        Sets the recommendedHuntingQueries property value. The recommendedHuntingQueries property
        Args:
            value: Value to set for the recommended_hunting_queries property.
        """
        self._recommended_hunting_queries = value
    
    @property
    def redirect_incident_id(self,) -> Optional[str]:
        """
        Gets the redirectIncidentId property value. Only populated in case an incident is grouped together with another incident, as part of the logic that processes incidents. In such a case, the status property is redirected.
        Returns: Optional[str]
        """
        return self._redirect_incident_id
    
    @redirect_incident_id.setter
    def redirect_incident_id(self,value: Optional[str] = None) -> None:
        """
        Sets the redirectIncidentId property value. Only populated in case an incident is grouped together with another incident, as part of the logic that processes incidents. In such a case, the status property is redirected.
        Args:
            value: Value to set for the redirect_incident_id property.
        """
        self._redirect_incident_id = value
    
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
    def status(self,) -> Optional[incident_status.IncidentStatus]:
        """
        Gets the status property value. The status property
        Returns: Optional[incident_status.IncidentStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[incident_status.IncidentStatus] = None) -> None:
        """
        Sets the status property value. The status property
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    
    @property
    def system_tags(self,) -> Optional[List[str]]:
        """
        Gets the systemTags property value. The systemTags property
        Returns: Optional[List[str]]
        """
        return self._system_tags
    
    @system_tags.setter
    def system_tags(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the systemTags property value. The systemTags property
        Args:
            value: Value to set for the system_tags property.
        """
        self._system_tags = value
    
    @property
    def tenant_id(self,) -> Optional[str]:
        """
        Gets the tenantId property value. The Azure Active Directory tenant in which the alert was created.
        Returns: Optional[str]
        """
        return self._tenant_id
    
    @tenant_id.setter
    def tenant_id(self,value: Optional[str] = None) -> None:
        """
        Sets the tenantId property value. The Azure Active Directory tenant in which the alert was created.
        Args:
            value: Value to set for the tenant_id property.
        """
        self._tenant_id = value
    

