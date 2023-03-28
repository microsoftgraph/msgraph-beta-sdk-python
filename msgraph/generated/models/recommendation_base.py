from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import action_step, entity, impacted_resource, recommendation, recommendation_category, recommendation_feature_areas, recommendation_priority, recommendation_status, recommendation_type

from . import entity

class RecommendationBase(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new recommendationBase and sets the default values.
        """
        super().__init__()
        # List of actions to take to complete a recommendation.
        self._action_steps: Optional[List[action_step.ActionStep]] = None
        # An explanation of why completing the recommendation will benefit you. Corresponds to the Value section of a recommendation shown in the Azure AD portal.
        self._benefits: Optional[str] = None
        # The category property
        self._category: Optional[recommendation_category.RecommendationCategory] = None
        # The date and time when the recommendation was detected as applicable to your directory.
        self._created_date_time: Optional[datetime] = None
        # The number of points the tenant has attained. Only applies to recommendations with category set to identitySecureScore.
        self._current_score: Optional[float] = None
        # The title of the recommendation.
        self._display_name: Optional[str] = None
        # The directory feature that the recommendation is related to.
        self._feature_areas: Optional[List[recommendation_feature_areas.RecommendationFeatureAreas]] = None
        # The future date and time when a recommendation should be completed.
        self._impact_start_date_time: Optional[datetime] = None
        # Indicates the scope of impact of a recommendation. Tenant level indicates that the recommendation impacts the whole tenant. Other possible values include users, applications.
        self._impact_type: Optional[str] = None
        # The list of directory objects associated with the recommendation.
        self._impacted_resources: Optional[List[impacted_resource.ImpactedResource]] = None
        # Describes why a recommendation uniquely applies to your directory. Corresponds to the Description section of a recommendation shown in the Azure AD portal.
        self._insights: Optional[str] = None
        # The most recent date and time a recommendation was deemed applicable to your directory.
        self._last_checked_date_time: Optional[datetime] = None
        # Name of the user who last updated the status of the recommendation.
        self._last_modified_by: Optional[str] = None
        # The date and time the status of a recommendation was last updated.
        self._last_modified_date_time: Optional[datetime] = None
        # The maximum number of points attainable. Only applies to recommendations with category set to identitySecureScore.
        self._max_score: Optional[float] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The future date and time when the status of a postponed recommendation will be active again.
        self._postpone_until_date_time: Optional[datetime] = None
        # The priority property
        self._priority: Optional[recommendation_priority.RecommendationPriority] = None
        # Friendly shortname to identify the recommendation. The possible values are: adfsAppsMigration, enableDesktopSSO, enablePHS, enableProvisioning, switchFromPerUserMFA, tenantMFA, thirdPartyApps, turnOffPerUserMFA, useAuthenticatorApp, useMyApps, staleApps, staleAppCreds, applicationCredentialExpiry, servicePrincipalKeyExpiry, adminMFAV2, blockLegacyAuthentication, integratedApps, mfaRegistrationV2, pwagePolicyNew, passwordHashSync, oneAdmin, roleOverlap, selfServicePasswordReset, signinRiskPolicy, userRiskPolicy, verifyAppPublisher, privateLinkForAAD, appRoleAssignmentsGroups, appRoleAssignmentsUsers, managedIdentity, overprivilegedApps, unknownFutureValue.
        self._recommendation_type: Optional[recommendation_type.RecommendationType] = None
        # Description of the impact on users of the remediation. Only applies to recommendations with category set to identitySecureScore.
        self._remediation_impact: Optional[str] = None
        # The status property
        self._status: Optional[recommendation_status.RecommendationStatus] = None
    
    @property
    def action_steps(self,) -> Optional[List[action_step.ActionStep]]:
        """
        Gets the actionSteps property value. List of actions to take to complete a recommendation.
        Returns: Optional[List[action_step.ActionStep]]
        """
        return self._action_steps
    
    @action_steps.setter
    def action_steps(self,value: Optional[List[action_step.ActionStep]] = None) -> None:
        """
        Sets the actionSteps property value. List of actions to take to complete a recommendation.
        Args:
            value: Value to set for the action_steps property.
        """
        self._action_steps = value
    
    @property
    def benefits(self,) -> Optional[str]:
        """
        Gets the benefits property value. An explanation of why completing the recommendation will benefit you. Corresponds to the Value section of a recommendation shown in the Azure AD portal.
        Returns: Optional[str]
        """
        return self._benefits
    
    @benefits.setter
    def benefits(self,value: Optional[str] = None) -> None:
        """
        Sets the benefits property value. An explanation of why completing the recommendation will benefit you. Corresponds to the Value section of a recommendation shown in the Azure AD portal.
        Args:
            value: Value to set for the benefits property.
        """
        self._benefits = value
    
    @property
    def category(self,) -> Optional[recommendation_category.RecommendationCategory]:
        """
        Gets the category property value. The category property
        Returns: Optional[recommendation_category.RecommendationCategory]
        """
        return self._category
    
    @category.setter
    def category(self,value: Optional[recommendation_category.RecommendationCategory] = None) -> None:
        """
        Sets the category property value. The category property
        Args:
            value: Value to set for the category property.
        """
        self._category = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The date and time when the recommendation was detected as applicable to your directory.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The date and time when the recommendation was detected as applicable to your directory.
        Args:
            value: Value to set for the created_date_time property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RecommendationBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RecommendationBase
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.recommendation":
                from . import recommendation

                return recommendation.Recommendation()
        return RecommendationBase()
    
    @property
    def current_score(self,) -> Optional[float]:
        """
        Gets the currentScore property value. The number of points the tenant has attained. Only applies to recommendations with category set to identitySecureScore.
        Returns: Optional[float]
        """
        return self._current_score
    
    @current_score.setter
    def current_score(self,value: Optional[float] = None) -> None:
        """
        Sets the currentScore property value. The number of points the tenant has attained. Only applies to recommendations with category set to identitySecureScore.
        Args:
            value: Value to set for the current_score property.
        """
        self._current_score = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The title of the recommendation.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The title of the recommendation.
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    @property
    def feature_areas(self,) -> Optional[List[recommendation_feature_areas.RecommendationFeatureAreas]]:
        """
        Gets the featureAreas property value. The directory feature that the recommendation is related to.
        Returns: Optional[List[recommendation_feature_areas.RecommendationFeatureAreas]]
        """
        return self._feature_areas
    
    @feature_areas.setter
    def feature_areas(self,value: Optional[List[recommendation_feature_areas.RecommendationFeatureAreas]] = None) -> None:
        """
        Sets the featureAreas property value. The directory feature that the recommendation is related to.
        Args:
            value: Value to set for the feature_areas property.
        """
        self._feature_areas = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import action_step, entity, impacted_resource, recommendation, recommendation_category, recommendation_feature_areas, recommendation_priority, recommendation_status, recommendation_type

        fields: Dict[str, Callable[[Any], None]] = {
            "actionSteps": lambda n : setattr(self, 'action_steps', n.get_collection_of_object_values(action_step.ActionStep)),
            "benefits": lambda n : setattr(self, 'benefits', n.get_str_value()),
            "category": lambda n : setattr(self, 'category', n.get_enum_value(recommendation_category.RecommendationCategory)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "currentScore": lambda n : setattr(self, 'current_score', n.get_float_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "featureAreas": lambda n : setattr(self, 'feature_areas', n.get_collection_of_enum_values(recommendation_feature_areas.RecommendationFeatureAreas)),
            "impactedResources": lambda n : setattr(self, 'impacted_resources', n.get_collection_of_object_values(impacted_resource.ImpactedResource)),
            "impactStartDateTime": lambda n : setattr(self, 'impact_start_date_time', n.get_datetime_value()),
            "impactType": lambda n : setattr(self, 'impact_type', n.get_str_value()),
            "insights": lambda n : setattr(self, 'insights', n.get_str_value()),
            "lastCheckedDateTime": lambda n : setattr(self, 'last_checked_date_time', n.get_datetime_value()),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "maxScore": lambda n : setattr(self, 'max_score', n.get_float_value()),
            "postponeUntilDateTime": lambda n : setattr(self, 'postpone_until_date_time', n.get_datetime_value()),
            "priority": lambda n : setattr(self, 'priority', n.get_enum_value(recommendation_priority.RecommendationPriority)),
            "recommendationType": lambda n : setattr(self, 'recommendation_type', n.get_enum_value(recommendation_type.RecommendationType)),
            "remediationImpact": lambda n : setattr(self, 'remediation_impact', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(recommendation_status.RecommendationStatus)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def impact_start_date_time(self,) -> Optional[datetime]:
        """
        Gets the impactStartDateTime property value. The future date and time when a recommendation should be completed.
        Returns: Optional[datetime]
        """
        return self._impact_start_date_time
    
    @impact_start_date_time.setter
    def impact_start_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the impactStartDateTime property value. The future date and time when a recommendation should be completed.
        Args:
            value: Value to set for the impact_start_date_time property.
        """
        self._impact_start_date_time = value
    
    @property
    def impact_type(self,) -> Optional[str]:
        """
        Gets the impactType property value. Indicates the scope of impact of a recommendation. Tenant level indicates that the recommendation impacts the whole tenant. Other possible values include users, applications.
        Returns: Optional[str]
        """
        return self._impact_type
    
    @impact_type.setter
    def impact_type(self,value: Optional[str] = None) -> None:
        """
        Sets the impactType property value. Indicates the scope of impact of a recommendation. Tenant level indicates that the recommendation impacts the whole tenant. Other possible values include users, applications.
        Args:
            value: Value to set for the impact_type property.
        """
        self._impact_type = value
    
    @property
    def impacted_resources(self,) -> Optional[List[impacted_resource.ImpactedResource]]:
        """
        Gets the impactedResources property value. The list of directory objects associated with the recommendation.
        Returns: Optional[List[impacted_resource.ImpactedResource]]
        """
        return self._impacted_resources
    
    @impacted_resources.setter
    def impacted_resources(self,value: Optional[List[impacted_resource.ImpactedResource]] = None) -> None:
        """
        Sets the impactedResources property value. The list of directory objects associated with the recommendation.
        Args:
            value: Value to set for the impacted_resources property.
        """
        self._impacted_resources = value
    
    @property
    def insights(self,) -> Optional[str]:
        """
        Gets the insights property value. Describes why a recommendation uniquely applies to your directory. Corresponds to the Description section of a recommendation shown in the Azure AD portal.
        Returns: Optional[str]
        """
        return self._insights
    
    @insights.setter
    def insights(self,value: Optional[str] = None) -> None:
        """
        Sets the insights property value. Describes why a recommendation uniquely applies to your directory. Corresponds to the Description section of a recommendation shown in the Azure AD portal.
        Args:
            value: Value to set for the insights property.
        """
        self._insights = value
    
    @property
    def last_checked_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastCheckedDateTime property value. The most recent date and time a recommendation was deemed applicable to your directory.
        Returns: Optional[datetime]
        """
        return self._last_checked_date_time
    
    @last_checked_date_time.setter
    def last_checked_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastCheckedDateTime property value. The most recent date and time a recommendation was deemed applicable to your directory.
        Args:
            value: Value to set for the last_checked_date_time property.
        """
        self._last_checked_date_time = value
    
    @property
    def last_modified_by(self,) -> Optional[str]:
        """
        Gets the lastModifiedBy property value. Name of the user who last updated the status of the recommendation.
        Returns: Optional[str]
        """
        return self._last_modified_by
    
    @last_modified_by.setter
    def last_modified_by(self,value: Optional[str] = None) -> None:
        """
        Sets the lastModifiedBy property value. Name of the user who last updated the status of the recommendation.
        Args:
            value: Value to set for the last_modified_by property.
        """
        self._last_modified_by = value
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. The date and time the status of a recommendation was last updated.
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. The date and time the status of a recommendation was last updated.
        Args:
            value: Value to set for the last_modified_date_time property.
        """
        self._last_modified_date_time = value
    
    @property
    def max_score(self,) -> Optional[float]:
        """
        Gets the maxScore property value. The maximum number of points attainable. Only applies to recommendations with category set to identitySecureScore.
        Returns: Optional[float]
        """
        return self._max_score
    
    @max_score.setter
    def max_score(self,value: Optional[float] = None) -> None:
        """
        Sets the maxScore property value. The maximum number of points attainable. Only applies to recommendations with category set to identitySecureScore.
        Args:
            value: Value to set for the max_score property.
        """
        self._max_score = value
    
    @property
    def postpone_until_date_time(self,) -> Optional[datetime]:
        """
        Gets the postponeUntilDateTime property value. The future date and time when the status of a postponed recommendation will be active again.
        Returns: Optional[datetime]
        """
        return self._postpone_until_date_time
    
    @postpone_until_date_time.setter
    def postpone_until_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the postponeUntilDateTime property value. The future date and time when the status of a postponed recommendation will be active again.
        Args:
            value: Value to set for the postpone_until_date_time property.
        """
        self._postpone_until_date_time = value
    
    @property
    def priority(self,) -> Optional[recommendation_priority.RecommendationPriority]:
        """
        Gets the priority property value. The priority property
        Returns: Optional[recommendation_priority.RecommendationPriority]
        """
        return self._priority
    
    @priority.setter
    def priority(self,value: Optional[recommendation_priority.RecommendationPriority] = None) -> None:
        """
        Sets the priority property value. The priority property
        Args:
            value: Value to set for the priority property.
        """
        self._priority = value
    
    @property
    def recommendation_type(self,) -> Optional[recommendation_type.RecommendationType]:
        """
        Gets the recommendationType property value. Friendly shortname to identify the recommendation. The possible values are: adfsAppsMigration, enableDesktopSSO, enablePHS, enableProvisioning, switchFromPerUserMFA, tenantMFA, thirdPartyApps, turnOffPerUserMFA, useAuthenticatorApp, useMyApps, staleApps, staleAppCreds, applicationCredentialExpiry, servicePrincipalKeyExpiry, adminMFAV2, blockLegacyAuthentication, integratedApps, mfaRegistrationV2, pwagePolicyNew, passwordHashSync, oneAdmin, roleOverlap, selfServicePasswordReset, signinRiskPolicy, userRiskPolicy, verifyAppPublisher, privateLinkForAAD, appRoleAssignmentsGroups, appRoleAssignmentsUsers, managedIdentity, overprivilegedApps, unknownFutureValue.
        Returns: Optional[recommendation_type.RecommendationType]
        """
        return self._recommendation_type
    
    @recommendation_type.setter
    def recommendation_type(self,value: Optional[recommendation_type.RecommendationType] = None) -> None:
        """
        Sets the recommendationType property value. Friendly shortname to identify the recommendation. The possible values are: adfsAppsMigration, enableDesktopSSO, enablePHS, enableProvisioning, switchFromPerUserMFA, tenantMFA, thirdPartyApps, turnOffPerUserMFA, useAuthenticatorApp, useMyApps, staleApps, staleAppCreds, applicationCredentialExpiry, servicePrincipalKeyExpiry, adminMFAV2, blockLegacyAuthentication, integratedApps, mfaRegistrationV2, pwagePolicyNew, passwordHashSync, oneAdmin, roleOverlap, selfServicePasswordReset, signinRiskPolicy, userRiskPolicy, verifyAppPublisher, privateLinkForAAD, appRoleAssignmentsGroups, appRoleAssignmentsUsers, managedIdentity, overprivilegedApps, unknownFutureValue.
        Args:
            value: Value to set for the recommendation_type property.
        """
        self._recommendation_type = value
    
    @property
    def remediation_impact(self,) -> Optional[str]:
        """
        Gets the remediationImpact property value. Description of the impact on users of the remediation. Only applies to recommendations with category set to identitySecureScore.
        Returns: Optional[str]
        """
        return self._remediation_impact
    
    @remediation_impact.setter
    def remediation_impact(self,value: Optional[str] = None) -> None:
        """
        Sets the remediationImpact property value. Description of the impact on users of the remediation. Only applies to recommendations with category set to identitySecureScore.
        Args:
            value: Value to set for the remediation_impact property.
        """
        self._remediation_impact = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("actionSteps", self.action_steps)
        writer.write_str_value("benefits", self.benefits)
        writer.write_enum_value("category", self.category)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_float_value("currentScore", self.current_score)
        writer.write_str_value("displayName", self.display_name)
        writer.write_enum_value("featureAreas", self.feature_areas)
        writer.write_collection_of_object_values("impactedResources", self.impacted_resources)
        writer.write_datetime_value("impactStartDateTime", self.impact_start_date_time)
        writer.write_str_value("impactType", self.impact_type)
        writer.write_str_value("insights", self.insights)
        writer.write_datetime_value("lastCheckedDateTime", self.last_checked_date_time)
        writer.write_str_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_float_value("maxScore", self.max_score)
        writer.write_datetime_value("postponeUntilDateTime", self.postpone_until_date_time)
        writer.write_enum_value("priority", self.priority)
        writer.write_enum_value("recommendationType", self.recommendation_type)
        writer.write_str_value("remediationImpact", self.remediation_impact)
        writer.write_enum_value("status", self.status)
    
    @property
    def status(self,) -> Optional[recommendation_status.RecommendationStatus]:
        """
        Gets the status property value. The status property
        Returns: Optional[recommendation_status.RecommendationStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[recommendation_status.RecommendationStatus] = None) -> None:
        """
        Sets the status property value. The status property
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    

