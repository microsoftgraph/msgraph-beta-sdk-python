from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .applied_conditional_access_policy_result import AppliedConditionalAccessPolicyResult
    from .authentication_strength import AuthenticationStrength
    from .conditional_access_conditions import ConditionalAccessConditions
    from .conditional_access_rule_satisfied import ConditionalAccessRuleSatisfied

@dataclass
class AppliedConditionalAccessPolicy(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The custom authentication strength enforced in a Conditional Access policy.
    authentication_strength: Optional[AuthenticationStrength] = None
    # Refers to the conditional access policy conditions that aren't satisfied. The possible values are: none, application, users, devicePlatform, location, clientType, signInRisk, userRisk, time, deviceState, client,ipAddressSeenByAzureAD,ipAddressSeenByResourceProvider,unknownFutureValue,servicePrincipals,servicePrincipalRisk, authenticationFlows, insiderRisk . You must use the Prefer: include-unknown-enum-members request header to get the following values in this evolvable enum: servicePrincipals,servicePrincipalRisk, authenticationFlows, insiderRisk. conditionalAccessConditions is a multi-valued enumeration and the property can contain multiple values in a comma-separated list.
    conditions_not_satisfied: Optional[List[ConditionalAccessConditions]] = None
    # Refers to the conditional access policy conditions that are satisfied. The possible values are: none, application, users, devicePlatform, location, clientType, signInRisk, userRisk, time, deviceState, client,ipAddressSeenByAzureAD,ipAddressSeenByResourceProvider,unknownFutureValue,servicePrincipals,servicePrincipalRisk, authenticationFlows, insiderRisk. You must use the Prefer: include-unknown-enum-members request header to get the following values in this evolvable enum: servicePrincipals,servicePrincipalRisk, authenticationFlows, insiderRisk. conditionalAccessConditions is a multi-valued enumeration and the property can contain multiple values in a comma-separated list.
    conditions_satisfied: Optional[List[ConditionalAccessConditions]] = None
    # Name of the conditional access policy.
    display_name: Optional[str] = None
    # Refers to the grant controls enforced by the conditional access policy (example: 'Require multi-factor authentication').
    enforced_grant_controls: Optional[List[str]] = None
    # Refers to the session controls enforced by the conditional access policy (example: 'Require app enforced controls').
    enforced_session_controls: Optional[List[str]] = None
    # List of key-value pairs containing each matched exclude condition in the conditional access policy. Example: [{'devicePlatform' : 'DevicePlatform'}] means the policy didn't apply, because the DevicePlatform condition was a match.
    exclude_rules_satisfied: Optional[List[ConditionalAccessRuleSatisfied]] = None
    # Identifier of the conditional access policy.
    id: Optional[str] = None
    # List of key-value pairs containing each matched include condition in the conditional access policy. Example: [{ 'application' : 'AllApps'}, {'users': 'Group'}], meaning Application condition was a match because AllApps are included and Users condition was a match because the user was part of the included Group rule.
    include_rules_satisfied: Optional[List[ConditionalAccessRuleSatisfied]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates the result of the CA policy that was triggered. Possible values are: success, failure, notApplied (Policy isn't applied because policy conditions weren't met),notEnabled (This is due to the policy in disabled state), unknown, unknownFutureValue, reportOnlySuccess, reportOnlyFailure, reportOnlyNotApplied, reportOnlyInterrupted. You must use the Prefer: include-unknown-enum-members request header to get the following values in this evolvable enum: reportOnlySuccess, reportOnlyFailure, reportOnlyNotApplied, reportOnlyInterrupted.
    result: Optional[AppliedConditionalAccessPolicyResult] = None
    # Refers to the session controls that a sign-in activity didn't satisfy. (Example: Application enforced Restrictions).
    session_controls_not_satisfied: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AppliedConditionalAccessPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AppliedConditionalAccessPolicy
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AppliedConditionalAccessPolicy()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .applied_conditional_access_policy_result import AppliedConditionalAccessPolicyResult
        from .authentication_strength import AuthenticationStrength
        from .conditional_access_conditions import ConditionalAccessConditions
        from .conditional_access_rule_satisfied import ConditionalAccessRuleSatisfied

        from .applied_conditional_access_policy_result import AppliedConditionalAccessPolicyResult
        from .authentication_strength import AuthenticationStrength
        from .conditional_access_conditions import ConditionalAccessConditions
        from .conditional_access_rule_satisfied import ConditionalAccessRuleSatisfied

        fields: Dict[str, Callable[[Any], None]] = {
            "authenticationStrength": lambda n : setattr(self, 'authentication_strength', n.get_object_value(AuthenticationStrength)),
            "conditionsNotSatisfied": lambda n : setattr(self, 'conditions_not_satisfied', n.get_collection_of_enum_values(ConditionalAccessConditions)),
            "conditionsSatisfied": lambda n : setattr(self, 'conditions_satisfied', n.get_collection_of_enum_values(ConditionalAccessConditions)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "enforcedGrantControls": lambda n : setattr(self, 'enforced_grant_controls', n.get_collection_of_primitive_values(str)),
            "enforcedSessionControls": lambda n : setattr(self, 'enforced_session_controls', n.get_collection_of_primitive_values(str)),
            "excludeRulesSatisfied": lambda n : setattr(self, 'exclude_rules_satisfied', n.get_collection_of_object_values(ConditionalAccessRuleSatisfied)),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "includeRulesSatisfied": lambda n : setattr(self, 'include_rules_satisfied', n.get_collection_of_object_values(ConditionalAccessRuleSatisfied)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "result": lambda n : setattr(self, 'result', n.get_enum_value(AppliedConditionalAccessPolicyResult)),
            "sessionControlsNotSatisfied": lambda n : setattr(self, 'session_controls_not_satisfied', n.get_collection_of_primitive_values(str)),
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
        writer.write_object_value("authenticationStrength", self.authentication_strength)
        writer.write_collection_of_enum_values("conditionsNotSatisfied", self.conditions_not_satisfied)
        writer.write_collection_of_enum_values("conditionsSatisfied", self.conditions_satisfied)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_primitive_values("enforcedGrantControls", self.enforced_grant_controls)
        writer.write_collection_of_primitive_values("enforcedSessionControls", self.enforced_session_controls)
        writer.write_collection_of_object_values("excludeRulesSatisfied", self.exclude_rules_satisfied)
        writer.write_str_value("id", self.id)
        writer.write_collection_of_object_values("includeRulesSatisfied", self.include_rules_satisfied)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("result", self.result)
        writer.write_collection_of_primitive_values("sessionControlsNotSatisfied", self.session_controls_not_satisfied)
        writer.write_additional_data_value(self.additional_data)
    

