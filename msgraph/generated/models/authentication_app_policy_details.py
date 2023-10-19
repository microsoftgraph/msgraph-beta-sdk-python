from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authentication_app_admin_configuration import AuthenticationAppAdminConfiguration
    from .authentication_app_evaluation import AuthenticationAppEvaluation
    from .authentication_app_policy_status import AuthenticationAppPolicyStatus

@dataclass
class AuthenticationAppPolicyDetails(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The admin configuration of the policy on the user's authentication app. For a policy that does not impact the success/failure of the authentication, the evaluation defaults to notApplicable. The possible values are: notApplicable, enabled, disabled, unknownFutureValue.
    admin_configuration: Optional[AuthenticationAppAdminConfiguration] = None
    # Evaluates the success/failure of the authentication based on the admin configuration of the policy on the user's client authentication app. The possible values are: success, failure, unknownFutureValue.
    authentication_evaluation: Optional[AuthenticationAppEvaluation] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The name of the policy enforced on the user's authentication app.
    policy_name: Optional[str] = None
    # Refers to whether the policy executed as expected on the user's client authentication app. The possible values are: unknown, appLockOutOfDate, appLockEnabled, appLockDisabled, appContextOutOfDate, appContextShown, appContextNotShown, locationContextOutOfDate, locationContextShown, locationContextNotShown, numberMatchOutOfDate, numberMatchCorrectNumberEntered, numberMatchIncorrectNumberEntered, numberMatchDeny, tamperResistantHardwareOutOfDate, tamperResistantHardwareUsed, tamperResistantHardwareNotUsed, unknownFutureValue.
    status: Optional[AuthenticationAppPolicyStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AuthenticationAppPolicyDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AuthenticationAppPolicyDetails
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AuthenticationAppPolicyDetails()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .authentication_app_admin_configuration import AuthenticationAppAdminConfiguration
        from .authentication_app_evaluation import AuthenticationAppEvaluation
        from .authentication_app_policy_status import AuthenticationAppPolicyStatus

        from .authentication_app_admin_configuration import AuthenticationAppAdminConfiguration
        from .authentication_app_evaluation import AuthenticationAppEvaluation
        from .authentication_app_policy_status import AuthenticationAppPolicyStatus

        fields: Dict[str, Callable[[Any], None]] = {
            "adminConfiguration": lambda n : setattr(self, 'admin_configuration', n.get_enum_value(AuthenticationAppAdminConfiguration)),
            "authenticationEvaluation": lambda n : setattr(self, 'authentication_evaluation', n.get_enum_value(AuthenticationAppEvaluation)),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "policyName": lambda n : setattr(self, 'policy_name', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(AuthenticationAppPolicyStatus)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_enum_value("adminConfiguration", self.admin_configuration)
        writer.write_enum_value("authenticationEvaluation", self.authentication_evaluation)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_str_value("policyName", self.policy_name)
        writer.write_enum_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    

