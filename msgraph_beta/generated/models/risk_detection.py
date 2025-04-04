from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .activity_type import ActivityType
    from .entity import Entity
    from .risk_detail import RiskDetail
    from .risk_detection_timing_type import RiskDetectionTimingType
    from .risk_event_type import RiskEventType
    from .risk_level import RiskLevel
    from .risk_state import RiskState
    from .sign_in_location import SignInLocation
    from .token_issuer_type import TokenIssuerType

from .entity import Entity

@dataclass
class RiskDetection(Entity, Parsable):
    # Indicates the activity type the detected risk is linked to. The possible values are signin, user, unknownFutureValue.
    activity: Optional[ActivityType] = None
    # Date and time that the risky activity occurred. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    activity_date_time: Optional[datetime.datetime] = None
    # Additional information associated with the risk detection in JSON format.
    additional_info: Optional[str] = None
    # Correlation ID of the sign-in associated with the risk detection. This property is null if the risk detection is not associated with a sign-in.
    correlation_id: Optional[str] = None
    # Date and time that the risk was detected. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    detected_date_time: Optional[datetime.datetime] = None
    # Timing of the detected risk (real-time/offline). The possible values are notDefined, realtime, nearRealtime, offline, unknownFutureValue.
    detection_timing_type: Optional[RiskDetectionTimingType] = None
    # Provides the IP address of the client from where the risk occurred.
    ip_address: Optional[str] = None
    # Date and time that the risk detection was last updated.
    last_updated_date_time: Optional[datetime.datetime] = None
    # Location of the sign-in.
    location: Optional[SignInLocation] = None
    # The mitreTechniqueId property
    mitre_technique_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Request ID of the sign-in associated with the risk detection. This property is null if the risk detection is not associated with a sign-in.
    request_id: Optional[str] = None
    # Details of the detected risk. The possible values are: none, adminGeneratedTemporaryPassword, userPerformedSecuredPasswordChange, userPerformedSecuredPasswordReset, adminConfirmedSigninSafe, aiConfirmedSigninSafe, userPassedMFADrivenByRiskBasedPolicy, adminDismissedAllRiskForUser, adminConfirmedSigninCompromised, hidden, adminConfirmedUserCompromised, unknownFutureValue, adminConfirmedServicePrincipalCompromised, adminDismissedAllRiskForServicePrincipal, m365DAdminDismissedDetection. Use the Prefer: include - unknown -enum-members request header to get the following value(s) in this evolvable enum: adminConfirmedServicePrincipalCompromised , adminDismissedAllRiskForServicePrincipal , m365DAdminDismissedDetection. Note: Details for this property are only available for Microsoft Entra ID P2 customers. P1 customers will be returned hidden.
    risk_detail: Optional[RiskDetail] = None
    # The type of risk event detected. The possible values are adminConfirmedUserCompromised, anomalousUserActivity, anomalousToken, anonymizedIPAddress,attackerinTheMiddle,attemptedPRTAccess, generic, investigationsThreatIntelligence, investigationsThreatIntelligenceSigninLinked,leakedCredentials, maliciousIPAddress, maliciousIPAddressValidCredentialsBlockedIP, malwareInfectedIPAddress, mcasImpossibleTravel,mcasFinSuspiciousFileAccess, mcasSuspiciousInboxManipulationRules,nationStateIP, newCountry, passwordSpray, riskyIPAddress, suspiciousAPITraffic, suspiciousBrowser, suspiciousInboxForwarding, suspiciousIPAddress,suspiciousSendingPatterns, tokenIssuerAnomaly,  unfamiliarFeatures, unlikelyTravel, userReportedSuspiciousActivity.  For more information about each value, see Risk types and detection.
    risk_event_type: Optional[str] = None
    # Level of the detected risk. The possible values are low, medium, high, hidden, none, unknownFutureValue. Note: Details for this property are only available for Microsoft Entra ID P2 customers. P1 customers will be returned hidden.
    risk_level: Optional[RiskLevel] = None
    # The state of a detected risky user or sign-in. The possible values are none, confirmedSafe, remediated, dismissed, atRisk, confirmedCompromised, and unknownFutureValue.
    risk_state: Optional[RiskState] = None
    # List of risk event types.Note: This property is deprecated. Use riskEventType instead.
    risk_type: Optional[RiskEventType] = None
    # Source of the risk detection. For example, activeDirectory.
    source: Optional[str] = None
    # Indicates the type of token issuer for the detected sign-in risk. The possible values are AzureAD, ADFederationServices, and unknownFutureValue.
    token_issuer_type: Optional[TokenIssuerType] = None
    # Name of the user.
    user_display_name: Optional[str] = None
    # Unique ID of the user.  The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    user_id: Optional[str] = None
    # The user principal name (UPN) of the user.
    user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RiskDetection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RiskDetection
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RiskDetection()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .activity_type import ActivityType
        from .entity import Entity
        from .risk_detail import RiskDetail
        from .risk_detection_timing_type import RiskDetectionTimingType
        from .risk_event_type import RiskEventType
        from .risk_level import RiskLevel
        from .risk_state import RiskState
        from .sign_in_location import SignInLocation
        from .token_issuer_type import TokenIssuerType

        from .activity_type import ActivityType
        from .entity import Entity
        from .risk_detail import RiskDetail
        from .risk_detection_timing_type import RiskDetectionTimingType
        from .risk_event_type import RiskEventType
        from .risk_level import RiskLevel
        from .risk_state import RiskState
        from .sign_in_location import SignInLocation
        from .token_issuer_type import TokenIssuerType

        fields: dict[str, Callable[[Any], None]] = {
            "activity": lambda n : setattr(self, 'activity', n.get_enum_value(ActivityType)),
            "activityDateTime": lambda n : setattr(self, 'activity_date_time', n.get_datetime_value()),
            "additionalInfo": lambda n : setattr(self, 'additional_info', n.get_str_value()),
            "correlationId": lambda n : setattr(self, 'correlation_id', n.get_str_value()),
            "detectedDateTime": lambda n : setattr(self, 'detected_date_time', n.get_datetime_value()),
            "detectionTimingType": lambda n : setattr(self, 'detection_timing_type', n.get_enum_value(RiskDetectionTimingType)),
            "ipAddress": lambda n : setattr(self, 'ip_address', n.get_str_value()),
            "lastUpdatedDateTime": lambda n : setattr(self, 'last_updated_date_time', n.get_datetime_value()),
            "location": lambda n : setattr(self, 'location', n.get_object_value(SignInLocation)),
            "mitreTechniqueId": lambda n : setattr(self, 'mitre_technique_id', n.get_str_value()),
            "requestId": lambda n : setattr(self, 'request_id', n.get_str_value()),
            "riskDetail": lambda n : setattr(self, 'risk_detail', n.get_enum_value(RiskDetail)),
            "riskEventType": lambda n : setattr(self, 'risk_event_type', n.get_str_value()),
            "riskLevel": lambda n : setattr(self, 'risk_level', n.get_enum_value(RiskLevel)),
            "riskState": lambda n : setattr(self, 'risk_state', n.get_enum_value(RiskState)),
            "riskType": lambda n : setattr(self, 'risk_type', n.get_enum_value(RiskEventType)),
            "source": lambda n : setattr(self, 'source', n.get_str_value()),
            "tokenIssuerType": lambda n : setattr(self, 'token_issuer_type', n.get_enum_value(TokenIssuerType)),
            "userDisplayName": lambda n : setattr(self, 'user_display_name', n.get_str_value()),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
            "userPrincipalName": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
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
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_enum_value("activity", self.activity)
        writer.write_datetime_value("activityDateTime", self.activity_date_time)
        writer.write_str_value("additionalInfo", self.additional_info)
        writer.write_str_value("correlationId", self.correlation_id)
        writer.write_datetime_value("detectedDateTime", self.detected_date_time)
        writer.write_enum_value("detectionTimingType", self.detection_timing_type)
        writer.write_str_value("ipAddress", self.ip_address)
        writer.write_datetime_value("lastUpdatedDateTime", self.last_updated_date_time)
        writer.write_object_value("location", self.location)
        writer.write_str_value("mitreTechniqueId", self.mitre_technique_id)
        writer.write_str_value("requestId", self.request_id)
        writer.write_enum_value("riskDetail", self.risk_detail)
        writer.write_str_value("riskEventType", self.risk_event_type)
        writer.write_enum_value("riskLevel", self.risk_level)
        writer.write_enum_value("riskState", self.risk_state)
        writer.write_enum_value("riskType", self.risk_type)
        writer.write_str_value("source", self.source)
        writer.write_enum_value("tokenIssuerType", self.token_issuer_type)
        writer.write_str_value("userDisplayName", self.user_display_name)
        writer.write_str_value("userId", self.user_id)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
    

