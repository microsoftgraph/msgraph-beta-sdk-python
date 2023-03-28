from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import lifecycle_workflows_container
    from .. import access_review_set, app_consent_approval_route, entitlement_management, privileged_access_root, role_management_alert, terms_of_use_container

class IdentityGovernance(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new IdentityGovernance and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The accessReviews property
        self._access_reviews: Optional[access_review_set.AccessReviewSet] = None
        # The appConsent property
        self._app_consent: Optional[app_consent_approval_route.AppConsentApprovalRoute] = None
        # The entitlementManagement property
        self._entitlement_management: Optional[entitlement_management.EntitlementManagement] = None
        # The lifecycleWorkflows property
        self._lifecycle_workflows: Optional[lifecycle_workflows_container.LifecycleWorkflowsContainer] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The privilegedAccess property
        self._privileged_access: Optional[privileged_access_root.PrivilegedAccessRoot] = None
        # The roleManagementAlerts property
        self._role_management_alerts: Optional[role_management_alert.RoleManagementAlert] = None
        # The termsOfUse property
        self._terms_of_use: Optional[terms_of_use_container.TermsOfUseContainer] = None
    
    @property
    def access_reviews(self,) -> Optional[access_review_set.AccessReviewSet]:
        """
        Gets the accessReviews property value. The accessReviews property
        Returns: Optional[access_review_set.AccessReviewSet]
        """
        return self._access_reviews
    
    @access_reviews.setter
    def access_reviews(self,value: Optional[access_review_set.AccessReviewSet] = None) -> None:
        """
        Sets the accessReviews property value. The accessReviews property
        Args:
            value: Value to set for the access_reviews property.
        """
        self._access_reviews = value
    
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def app_consent(self,) -> Optional[app_consent_approval_route.AppConsentApprovalRoute]:
        """
        Gets the appConsent property value. The appConsent property
        Returns: Optional[app_consent_approval_route.AppConsentApprovalRoute]
        """
        return self._app_consent
    
    @app_consent.setter
    def app_consent(self,value: Optional[app_consent_approval_route.AppConsentApprovalRoute] = None) -> None:
        """
        Sets the appConsent property value. The appConsent property
        Args:
            value: Value to set for the app_consent property.
        """
        self._app_consent = value
    
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
    
    @property
    def entitlement_management(self,) -> Optional[entitlement_management.EntitlementManagement]:
        """
        Gets the entitlementManagement property value. The entitlementManagement property
        Returns: Optional[entitlement_management.EntitlementManagement]
        """
        return self._entitlement_management
    
    @entitlement_management.setter
    def entitlement_management(self,value: Optional[entitlement_management.EntitlementManagement] = None) -> None:
        """
        Sets the entitlementManagement property value. The entitlementManagement property
        Args:
            value: Value to set for the entitlement_management property.
        """
        self._entitlement_management = value
    
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
    
    @property
    def lifecycle_workflows(self,) -> Optional[lifecycle_workflows_container.LifecycleWorkflowsContainer]:
        """
        Gets the lifecycleWorkflows property value. The lifecycleWorkflows property
        Returns: Optional[lifecycle_workflows_container.LifecycleWorkflowsContainer]
        """
        return self._lifecycle_workflows
    
    @lifecycle_workflows.setter
    def lifecycle_workflows(self,value: Optional[lifecycle_workflows_container.LifecycleWorkflowsContainer] = None) -> None:
        """
        Sets the lifecycleWorkflows property value. The lifecycleWorkflows property
        Args:
            value: Value to set for the lifecycle_workflows property.
        """
        self._lifecycle_workflows = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the odata_type property.
        """
        self._odata_type = value
    
    @property
    def privileged_access(self,) -> Optional[privileged_access_root.PrivilegedAccessRoot]:
        """
        Gets the privilegedAccess property value. The privilegedAccess property
        Returns: Optional[privileged_access_root.PrivilegedAccessRoot]
        """
        return self._privileged_access
    
    @privileged_access.setter
    def privileged_access(self,value: Optional[privileged_access_root.PrivilegedAccessRoot] = None) -> None:
        """
        Sets the privilegedAccess property value. The privilegedAccess property
        Args:
            value: Value to set for the privileged_access property.
        """
        self._privileged_access = value
    
    @property
    def role_management_alerts(self,) -> Optional[role_management_alert.RoleManagementAlert]:
        """
        Gets the roleManagementAlerts property value. The roleManagementAlerts property
        Returns: Optional[role_management_alert.RoleManagementAlert]
        """
        return self._role_management_alerts
    
    @role_management_alerts.setter
    def role_management_alerts(self,value: Optional[role_management_alert.RoleManagementAlert] = None) -> None:
        """
        Sets the roleManagementAlerts property value. The roleManagementAlerts property
        Args:
            value: Value to set for the role_management_alerts property.
        """
        self._role_management_alerts = value
    
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
    
    @property
    def terms_of_use(self,) -> Optional[terms_of_use_container.TermsOfUseContainer]:
        """
        Gets the termsOfUse property value. The termsOfUse property
        Returns: Optional[terms_of_use_container.TermsOfUseContainer]
        """
        return self._terms_of_use
    
    @terms_of_use.setter
    def terms_of_use(self,value: Optional[terms_of_use_container.TermsOfUseContainer] = None) -> None:
        """
        Sets the termsOfUse property value. The termsOfUse property
        Args:
            value: Value to set for the terms_of_use property.
        """
        self._terms_of_use = value
    

