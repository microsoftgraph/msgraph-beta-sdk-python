from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import lifecycle_workflows_container
    from .. import access_review_set, app_consent_approval_route, entitlement_management, privileged_access_root, role_management_alert, terms_of_use_container

@dataclass
class IdentityGovernance(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The accessReviews property
    access_reviews: Optional[access_review_set.AccessReviewSet] = None
    # The appConsent property
    app_consent: Optional[app_consent_approval_route.AppConsentApprovalRoute] = None
    # The entitlementManagement property
    entitlement_management: Optional[entitlement_management.EntitlementManagement] = None
    # The lifecycleWorkflows property
    lifecycle_workflows: Optional[lifecycle_workflows_container.LifecycleWorkflowsContainer] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The privilegedAccess property
    privileged_access: Optional[privileged_access_root.PrivilegedAccessRoot] = None
    # The roleManagementAlerts property
    role_management_alerts: Optional[role_management_alert.RoleManagementAlert] = None
    # The termsOfUse property
    terms_of_use: Optional[terms_of_use_container.TermsOfUseContainer] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IdentityGovernance:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IdentityGovernance
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return IdentityGovernance()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import lifecycle_workflows_container
        from .. import access_review_set, app_consent_approval_route, entitlement_management, privileged_access_root, role_management_alert, terms_of_use_container

        fields: Dict[str, Callable[[Any], None]] = {
            "accessReviews": lambda n : setattr(self, 'access_reviews', n.get_object_value(access_review_set.AccessReviewSet)),
            "appConsent": lambda n : setattr(self, 'app_consent', n.get_object_value(app_consent_approval_route.AppConsentApprovalRoute)),
            "entitlementManagement": lambda n : setattr(self, 'entitlement_management', n.get_object_value(entitlement_management.EntitlementManagement)),
            "lifecycleWorkflows": lambda n : setattr(self, 'lifecycle_workflows', n.get_object_value(lifecycle_workflows_container.LifecycleWorkflowsContainer)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "privilegedAccess": lambda n : setattr(self, 'privileged_access', n.get_object_value(privileged_access_root.PrivilegedAccessRoot)),
            "roleManagementAlerts": lambda n : setattr(self, 'role_management_alerts', n.get_object_value(role_management_alert.RoleManagementAlert)),
            "termsOfUse": lambda n : setattr(self, 'terms_of_use', n.get_object_value(terms_of_use_container.TermsOfUseContainer)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("accessReviews", self.access_reviews)
        writer.write_object_value("appConsent", self.app_consent)
        writer.write_object_value("entitlementManagement", self.entitlement_management)
        writer.write_object_value("lifecycleWorkflows", self.lifecycle_workflows)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("privilegedAccess", self.privileged_access)
        writer.write_object_value("roleManagementAlerts", self.role_management_alerts)
        writer.write_object_value("termsOfUse", self.terms_of_use)
        writer.write_additional_data_value(self.additional_data)
    

