from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..access_review_set import AccessReviewSet
    from ..app_consent_approval_route import AppConsentApprovalRoute
    from ..entitlement_management import EntitlementManagement
    from ..permissions_analytics_aggregation import PermissionsAnalyticsAggregation
    from ..permissions_management import PermissionsManagement
    from ..privileged_access_root import PrivilegedAccessRoot
    from ..role_management_alert import RoleManagementAlert
    from ..terms_of_use_container import TermsOfUseContainer
    from .lifecycle_workflows_container import LifecycleWorkflowsContainer

@dataclass
class IdentityGovernance(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The accessReviews property
    access_reviews: Optional[AccessReviewSet] = None
    # The appConsent property
    app_consent: Optional[AppConsentApprovalRoute] = None
    # The entitlementManagement property
    entitlement_management: Optional[EntitlementManagement] = None
    # The lifecycleWorkflows property
    lifecycle_workflows: Optional[LifecycleWorkflowsContainer] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The permissionsAnalytics property
    permissions_analytics: Optional[PermissionsAnalyticsAggregation] = None
    # The permissionsManagement property
    permissions_management: Optional[PermissionsManagement] = None
    # The privilegedAccess property
    privileged_access: Optional[PrivilegedAccessRoot] = None
    # The roleManagementAlerts property
    role_management_alerts: Optional[RoleManagementAlert] = None
    # The termsOfUse property
    terms_of_use: Optional[TermsOfUseContainer] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> IdentityGovernance:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IdentityGovernance
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return IdentityGovernance()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..access_review_set import AccessReviewSet
        from ..app_consent_approval_route import AppConsentApprovalRoute
        from ..entitlement_management import EntitlementManagement
        from ..permissions_analytics_aggregation import PermissionsAnalyticsAggregation
        from ..permissions_management import PermissionsManagement
        from ..privileged_access_root import PrivilegedAccessRoot
        from ..role_management_alert import RoleManagementAlert
        from ..terms_of_use_container import TermsOfUseContainer
        from .lifecycle_workflows_container import LifecycleWorkflowsContainer

        from ..access_review_set import AccessReviewSet
        from ..app_consent_approval_route import AppConsentApprovalRoute
        from ..entitlement_management import EntitlementManagement
        from ..permissions_analytics_aggregation import PermissionsAnalyticsAggregation
        from ..permissions_management import PermissionsManagement
        from ..privileged_access_root import PrivilegedAccessRoot
        from ..role_management_alert import RoleManagementAlert
        from ..terms_of_use_container import TermsOfUseContainer
        from .lifecycle_workflows_container import LifecycleWorkflowsContainer

        fields: Dict[str, Callable[[Any], None]] = {
            "accessReviews": lambda n : setattr(self, 'access_reviews', n.get_object_value(AccessReviewSet)),
            "appConsent": lambda n : setattr(self, 'app_consent', n.get_object_value(AppConsentApprovalRoute)),
            "entitlementManagement": lambda n : setattr(self, 'entitlement_management', n.get_object_value(EntitlementManagement)),
            "lifecycleWorkflows": lambda n : setattr(self, 'lifecycle_workflows', n.get_object_value(LifecycleWorkflowsContainer)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "permissionsAnalytics": lambda n : setattr(self, 'permissions_analytics', n.get_object_value(PermissionsAnalyticsAggregation)),
            "permissionsManagement": lambda n : setattr(self, 'permissions_management', n.get_object_value(PermissionsManagement)),
            "privilegedAccess": lambda n : setattr(self, 'privileged_access', n.get_object_value(PrivilegedAccessRoot)),
            "roleManagementAlerts": lambda n : setattr(self, 'role_management_alerts', n.get_object_value(RoleManagementAlert)),
            "termsOfUse": lambda n : setattr(self, 'terms_of_use', n.get_object_value(TermsOfUseContainer)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_object_value("accessReviews", self.access_reviews)
        writer.write_object_value("appConsent", self.app_consent)
        writer.write_object_value("entitlementManagement", self.entitlement_management)
        writer.write_object_value("lifecycleWorkflows", self.lifecycle_workflows)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("permissionsAnalytics", self.permissions_analytics)
        writer.write_object_value("permissionsManagement", self.permissions_management)
        writer.write_object_value("privilegedAccess", self.privileged_access)
        writer.write_object_value("roleManagementAlerts", self.role_management_alerts)
        writer.write_object_value("termsOfUse", self.terms_of_use)
        writer.write_additional_data_value(self.additional_data)
    

