from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .action_step import ActionStep
    from .entity import Entity
    from .impacted_resource import ImpactedResource
    from .recommendation import Recommendation
    from .recommendation_category import RecommendationCategory
    from .recommendation_feature_areas import RecommendationFeatureAreas
    from .recommendation_priority import RecommendationPriority
    from .recommendation_status import RecommendationStatus
    from .recommendation_type import RecommendationType
    from .required_licenses import RequiredLicenses

from .entity import Entity

@dataclass
class RecommendationBase(Entity):
    # List of actions to take to complete a recommendation.
    action_steps: Optional[List[ActionStep]] = None
    # An explanation of why completing the recommendation will benefit you. Corresponds to the Value section of a recommendation shown in the Microsoft Entra admin center.
    benefits: Optional[str] = None
    # The category property
    category: Optional[RecommendationCategory] = None
    # The date and time when the recommendation was detected as applicable to your directory.
    created_date_time: Optional[datetime.datetime] = None
    # The number of points the tenant has attained. Only applies to recommendations with category set to identitySecureScore.
    current_score: Optional[float] = None
    # The title of the recommendation.
    display_name: Optional[str] = None
    # The directory feature that the recommendation is related to.
    feature_areas: Optional[List[RecommendationFeatureAreas]] = None
    # The future date and time when a recommendation should be completed.
    impact_start_date_time: Optional[datetime.datetime] = None
    # Indicates the scope of impact of a recommendation. Tenant level indicates that the recommendation impacts the whole tenant. Other possible values include users, applications.
    impact_type: Optional[str] = None
    # The list of directory objects associated with the recommendation.
    impacted_resources: Optional[List[ImpactedResource]] = None
    # Describes why a recommendation uniquely applies to your directory. Corresponds to the Description section of a recommendation shown in the Microsoft Entra admin center.
    insights: Optional[str] = None
    # The most recent date and time a recommendation was deemed applicable to your directory.
    last_checked_date_time: Optional[datetime.datetime] = None
    # Name of the user who last updated the status of the recommendation.
    last_modified_by: Optional[str] = None
    # The date and time the status of a recommendation was last updated.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The maximum number of points attainable. Only applies to recommendations with category set to identitySecureScore.
    max_score: Optional[float] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The future date and time when the status of a postponed recommendation will be active again.
    postpone_until_date_time: Optional[datetime.datetime] = None
    # The priority property
    priority: Optional[RecommendationPriority] = None
    # Friendly shortname to identify the recommendation. The possible values are: adfsAppsMigration, enableDesktopSSO, enablePHS, enableProvisioning, switchFromPerUserMFA, tenantMFA, thirdPartyApps, turnOffPerUserMFA, useAuthenticatorApp, useMyApps, staleApps, staleAppCreds, applicationCredentialExpiry, servicePrincipalKeyExpiry, adminMFAV2, blockLegacyAuthentication, integratedApps, mfaRegistrationV2, pwagePolicyNew, passwordHashSync, oneAdmin, roleOverlap, selfServicePasswordReset, signinRiskPolicy, userRiskPolicy, verifyAppPublisher, privateLinkForAAD, appRoleAssignmentsGroups, appRoleAssignmentsUsers, managedIdentity, overprivilegedApps, unknownFutureValue, longLivedCredentials, aadConnectDeprecated, adalToMsalMigration, ownerlessApps, inactiveGuests, aadGraphDeprecationApplication, aadGraphDeprecationServicePrincipal, mfaServerDeprecation. Note that you must use the Prefer: include-unknown-enum-members request header to get the following value(s) in this evolvable enum: longLivedCredentials , aadConnectDeprecated , adalToMsalMigration , ownerlessApps , inactiveGuests , aadGraphDeprecationApplication , aadGraphDeprecationServicePrincipal , mfaServerDeprecation.
    recommendation_type: Optional[RecommendationType] = None
    # The current release type of the recommendation. The possible values are: preview, generallyAvailable, unknownFutureValue.
    release_type: Optional[str] = None
    # Description of the impact on users of the remediation. Only applies to recommendations with category set to identitySecureScore.
    remediation_impact: Optional[str] = None
    # The required licenses to view the recommendation. The possible values are: notApplicable, microsoftEntraIdFree, microsoftEntraIdP1, microsoftEntraIdP2, microsoftEntraIdGovernance, microsoftEntraWorkloadId, unknownFutureValue.
    required_licenses: Optional[RequiredLicenses] = None
    # The status property
    status: Optional[RecommendationStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RecommendationBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RecommendationBase
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.recommendation".casefold():
            from .recommendation import Recommendation

            return Recommendation()
        return RecommendationBase()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .action_step import ActionStep
        from .entity import Entity
        from .impacted_resource import ImpactedResource
        from .recommendation import Recommendation
        from .recommendation_category import RecommendationCategory
        from .recommendation_feature_areas import RecommendationFeatureAreas
        from .recommendation_priority import RecommendationPriority
        from .recommendation_status import RecommendationStatus
        from .recommendation_type import RecommendationType
        from .required_licenses import RequiredLicenses

        from .action_step import ActionStep
        from .entity import Entity
        from .impacted_resource import ImpactedResource
        from .recommendation import Recommendation
        from .recommendation_category import RecommendationCategory
        from .recommendation_feature_areas import RecommendationFeatureAreas
        from .recommendation_priority import RecommendationPriority
        from .recommendation_status import RecommendationStatus
        from .recommendation_type import RecommendationType
        from .required_licenses import RequiredLicenses

        fields: Dict[str, Callable[[Any], None]] = {
            "actionSteps": lambda n : setattr(self, 'action_steps', n.get_collection_of_object_values(ActionStep)),
            "benefits": lambda n : setattr(self, 'benefits', n.get_str_value()),
            "category": lambda n : setattr(self, 'category', n.get_enum_value(RecommendationCategory)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "currentScore": lambda n : setattr(self, 'current_score', n.get_float_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "featureAreas": lambda n : setattr(self, 'feature_areas', n.get_collection_of_enum_values(RecommendationFeatureAreas)),
            "impactStartDateTime": lambda n : setattr(self, 'impact_start_date_time', n.get_datetime_value()),
            "impactType": lambda n : setattr(self, 'impact_type', n.get_str_value()),
            "impactedResources": lambda n : setattr(self, 'impacted_resources', n.get_collection_of_object_values(ImpactedResource)),
            "insights": lambda n : setattr(self, 'insights', n.get_str_value()),
            "lastCheckedDateTime": lambda n : setattr(self, 'last_checked_date_time', n.get_datetime_value()),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "maxScore": lambda n : setattr(self, 'max_score', n.get_float_value()),
            "postponeUntilDateTime": lambda n : setattr(self, 'postpone_until_date_time', n.get_datetime_value()),
            "priority": lambda n : setattr(self, 'priority', n.get_enum_value(RecommendationPriority)),
            "recommendationType": lambda n : setattr(self, 'recommendation_type', n.get_enum_value(RecommendationType)),
            "releaseType": lambda n : setattr(self, 'release_type', n.get_str_value()),
            "remediationImpact": lambda n : setattr(self, 'remediation_impact', n.get_str_value()),
            "requiredLicenses": lambda n : setattr(self, 'required_licenses', n.get_enum_value(RequiredLicenses)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(RecommendationStatus)),
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
        writer.write_collection_of_object_values("actionSteps", self.action_steps)
        writer.write_str_value("benefits", self.benefits)
        writer.write_enum_value("category", self.category)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_float_value("currentScore", self.current_score)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_enum_values("featureAreas", self.feature_areas)
        writer.write_datetime_value("impactStartDateTime", self.impact_start_date_time)
        writer.write_str_value("impactType", self.impact_type)
        writer.write_collection_of_object_values("impactedResources", self.impacted_resources)
        writer.write_str_value("insights", self.insights)
        writer.write_datetime_value("lastCheckedDateTime", self.last_checked_date_time)
        writer.write_str_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_float_value("maxScore", self.max_score)
        writer.write_datetime_value("postponeUntilDateTime", self.postpone_until_date_time)
        writer.write_enum_value("priority", self.priority)
        writer.write_enum_value("recommendationType", self.recommendation_type)
        writer.write_str_value("releaseType", self.release_type)
        writer.write_str_value("remediationImpact", self.remediation_impact)
        writer.write_enum_value("requiredLicenses", self.required_licenses)
        writer.write_enum_value("status", self.status)
    

