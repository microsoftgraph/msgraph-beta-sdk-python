from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import applied_conditional_access_policy_result, authentication_strength, conditional_access_conditions, conditional_access_rule_satisfied

class AppliedConditionalAccessPolicy(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new appliedConditionalAccessPolicy and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The custom authentication strength enforced in a Conditional Access policy.
        self._authentication_strength: Optional[authentication_strength.AuthenticationStrength] = None
        # Refers to the conditional access policy conditions that are not satisfied. The possible values are: none, application, users, devicePlatform, location, clientType, signInRisk, userRisk, time, deviceState, client,ipAddressSeenByAzureAD,ipAddressSeenByResourceProvider,unknownFutureValue,servicePrincipals,servicePrincipalRisk. Note that you must use the Prefer: include-unknown-enum-members request header to get the following values in this evolvable enum: servicePrincipals,servicePrincipalRisk.
        self._conditions_not_satisfied: Optional[conditional_access_conditions.ConditionalAccessConditions] = None
        # Refers to the conditional access policy conditions that are satisfied. The possible values are: none, application, users, devicePlatform, location, clientType, signInRisk, userRisk, time, deviceState, client,ipAddressSeenByAzureAD,ipAddressSeenByResourceProvider,unknownFutureValue,servicePrincipals,servicePrincipalRisk. Note that you must use the Prefer: include-unknown-enum-members request header to get the following values in this evolvable enum: servicePrincipals,servicePrincipalRisk.
        self._conditions_satisfied: Optional[conditional_access_conditions.ConditionalAccessConditions] = None
        # Name of the conditional access policy.
        self._display_name: Optional[str] = None
        # Refers to the grant controls enforced by the conditional access policy (example: 'Require multi-factor authentication').
        self._enforced_grant_controls: Optional[List[str]] = None
        # Refers to the session controls enforced by the conditional access policy (example: 'Require app enforced controls').
        self._enforced_session_controls: Optional[List[str]] = None
        # List of key-value pairs containing each matched exclude condition in the conditional access policy. Example: [{'devicePlatform' : 'DevicePlatform'}] means the policy didn’t apply, because the DevicePlatform condition was a match.
        self._exclude_rules_satisfied: Optional[List[conditional_access_rule_satisfied.ConditionalAccessRuleSatisfied]] = None
        # Identifier of the conditional access policy.
        self._id: Optional[str] = None
        # List of key-value pairs containing each matched include condition in the conditional access policy. Example: [{ 'application' : 'AllApps'}, {'users': 'Group'}], meaning Application condition was a match because AllApps are included and Users condition was a match because the user was part of the included Group rule.
        self._include_rules_satisfied: Optional[List[conditional_access_rule_satisfied.ConditionalAccessRuleSatisfied]] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Indicates the result of the CA policy that was triggered. Possible values are: success, failure, notApplied (Policy isn't applied because policy conditions were not met),notEnabled (This is due to the policy in disabled state), unknown, unknownFutureValue, reportOnlySuccess, reportOnlyFailure, reportOnlyNotApplied, reportOnlyInterrupted. Note that you must use the Prefer: include-unknown-enum-members request header to get the following values in this evolvable enum: reportOnlySuccess, reportOnlyFailure, reportOnlyNotApplied, reportOnlyInterrupted.
        self._result: Optional[applied_conditional_access_policy_result.AppliedConditionalAccessPolicyResult] = None
        # Refers to the session controls that a sign-in activity did not satisfy. (Example: Application enforced Restrictions).
        self._session_controls_not_satisfied: Optional[List[str]] = None
    
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
    def authentication_strength(self,) -> Optional[authentication_strength.AuthenticationStrength]:
        """
        Gets the authenticationStrength property value. The custom authentication strength enforced in a Conditional Access policy.
        Returns: Optional[authentication_strength.AuthenticationStrength]
        """
        return self._authentication_strength
    
    @authentication_strength.setter
    def authentication_strength(self,value: Optional[authentication_strength.AuthenticationStrength] = None) -> None:
        """
        Sets the authenticationStrength property value. The custom authentication strength enforced in a Conditional Access policy.
        Args:
            value: Value to set for the authentication_strength property.
        """
        self._authentication_strength = value
    
    @property
    def conditions_not_satisfied(self,) -> Optional[conditional_access_conditions.ConditionalAccessConditions]:
        """
        Gets the conditionsNotSatisfied property value. Refers to the conditional access policy conditions that are not satisfied. The possible values are: none, application, users, devicePlatform, location, clientType, signInRisk, userRisk, time, deviceState, client,ipAddressSeenByAzureAD,ipAddressSeenByResourceProvider,unknownFutureValue,servicePrincipals,servicePrincipalRisk. Note that you must use the Prefer: include-unknown-enum-members request header to get the following values in this evolvable enum: servicePrincipals,servicePrincipalRisk.
        Returns: Optional[conditional_access_conditions.ConditionalAccessConditions]
        """
        return self._conditions_not_satisfied
    
    @conditions_not_satisfied.setter
    def conditions_not_satisfied(self,value: Optional[conditional_access_conditions.ConditionalAccessConditions] = None) -> None:
        """
        Sets the conditionsNotSatisfied property value. Refers to the conditional access policy conditions that are not satisfied. The possible values are: none, application, users, devicePlatform, location, clientType, signInRisk, userRisk, time, deviceState, client,ipAddressSeenByAzureAD,ipAddressSeenByResourceProvider,unknownFutureValue,servicePrincipals,servicePrincipalRisk. Note that you must use the Prefer: include-unknown-enum-members request header to get the following values in this evolvable enum: servicePrincipals,servicePrincipalRisk.
        Args:
            value: Value to set for the conditions_not_satisfied property.
        """
        self._conditions_not_satisfied = value
    
    @property
    def conditions_satisfied(self,) -> Optional[conditional_access_conditions.ConditionalAccessConditions]:
        """
        Gets the conditionsSatisfied property value. Refers to the conditional access policy conditions that are satisfied. The possible values are: none, application, users, devicePlatform, location, clientType, signInRisk, userRisk, time, deviceState, client,ipAddressSeenByAzureAD,ipAddressSeenByResourceProvider,unknownFutureValue,servicePrincipals,servicePrincipalRisk. Note that you must use the Prefer: include-unknown-enum-members request header to get the following values in this evolvable enum: servicePrincipals,servicePrincipalRisk.
        Returns: Optional[conditional_access_conditions.ConditionalAccessConditions]
        """
        return self._conditions_satisfied
    
    @conditions_satisfied.setter
    def conditions_satisfied(self,value: Optional[conditional_access_conditions.ConditionalAccessConditions] = None) -> None:
        """
        Sets the conditionsSatisfied property value. Refers to the conditional access policy conditions that are satisfied. The possible values are: none, application, users, devicePlatform, location, clientType, signInRisk, userRisk, time, deviceState, client,ipAddressSeenByAzureAD,ipAddressSeenByResourceProvider,unknownFutureValue,servicePrincipals,servicePrincipalRisk. Note that you must use the Prefer: include-unknown-enum-members request header to get the following values in this evolvable enum: servicePrincipals,servicePrincipalRisk.
        Args:
            value: Value to set for the conditions_satisfied property.
        """
        self._conditions_satisfied = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AppliedConditionalAccessPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AppliedConditionalAccessPolicy
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AppliedConditionalAccessPolicy()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Name of the conditional access policy.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Name of the conditional access policy.
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    @property
    def enforced_grant_controls(self,) -> Optional[List[str]]:
        """
        Gets the enforcedGrantControls property value. Refers to the grant controls enforced by the conditional access policy (example: 'Require multi-factor authentication').
        Returns: Optional[List[str]]
        """
        return self._enforced_grant_controls
    
    @enforced_grant_controls.setter
    def enforced_grant_controls(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the enforcedGrantControls property value. Refers to the grant controls enforced by the conditional access policy (example: 'Require multi-factor authentication').
        Args:
            value: Value to set for the enforced_grant_controls property.
        """
        self._enforced_grant_controls = value
    
    @property
    def enforced_session_controls(self,) -> Optional[List[str]]:
        """
        Gets the enforcedSessionControls property value. Refers to the session controls enforced by the conditional access policy (example: 'Require app enforced controls').
        Returns: Optional[List[str]]
        """
        return self._enforced_session_controls
    
    @enforced_session_controls.setter
    def enforced_session_controls(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the enforcedSessionControls property value. Refers to the session controls enforced by the conditional access policy (example: 'Require app enforced controls').
        Args:
            value: Value to set for the enforced_session_controls property.
        """
        self._enforced_session_controls = value
    
    @property
    def exclude_rules_satisfied(self,) -> Optional[List[conditional_access_rule_satisfied.ConditionalAccessRuleSatisfied]]:
        """
        Gets the excludeRulesSatisfied property value. List of key-value pairs containing each matched exclude condition in the conditional access policy. Example: [{'devicePlatform' : 'DevicePlatform'}] means the policy didn’t apply, because the DevicePlatform condition was a match.
        Returns: Optional[List[conditional_access_rule_satisfied.ConditionalAccessRuleSatisfied]]
        """
        return self._exclude_rules_satisfied
    
    @exclude_rules_satisfied.setter
    def exclude_rules_satisfied(self,value: Optional[List[conditional_access_rule_satisfied.ConditionalAccessRuleSatisfied]] = None) -> None:
        """
        Sets the excludeRulesSatisfied property value. List of key-value pairs containing each matched exclude condition in the conditional access policy. Example: [{'devicePlatform' : 'DevicePlatform'}] means the policy didn’t apply, because the DevicePlatform condition was a match.
        Args:
            value: Value to set for the exclude_rules_satisfied property.
        """
        self._exclude_rules_satisfied = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import applied_conditional_access_policy_result, authentication_strength, conditional_access_conditions, conditional_access_rule_satisfied

        fields: Dict[str, Callable[[Any], None]] = {
            "authenticationStrength": lambda n : setattr(self, 'authentication_strength', n.get_object_value(authentication_strength.AuthenticationStrength)),
            "conditionsNotSatisfied": lambda n : setattr(self, 'conditions_not_satisfied', n.get_enum_value(conditional_access_conditions.ConditionalAccessConditions)),
            "conditionsSatisfied": lambda n : setattr(self, 'conditions_satisfied', n.get_enum_value(conditional_access_conditions.ConditionalAccessConditions)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "enforcedGrantControls": lambda n : setattr(self, 'enforced_grant_controls', n.get_collection_of_primitive_values(str)),
            "enforcedSessionControls": lambda n : setattr(self, 'enforced_session_controls', n.get_collection_of_primitive_values(str)),
            "excludeRulesSatisfied": lambda n : setattr(self, 'exclude_rules_satisfied', n.get_collection_of_object_values(conditional_access_rule_satisfied.ConditionalAccessRuleSatisfied)),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "includeRulesSatisfied": lambda n : setattr(self, 'include_rules_satisfied', n.get_collection_of_object_values(conditional_access_rule_satisfied.ConditionalAccessRuleSatisfied)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "result": lambda n : setattr(self, 'result', n.get_enum_value(applied_conditional_access_policy_result.AppliedConditionalAccessPolicyResult)),
            "sessionControlsNotSatisfied": lambda n : setattr(self, 'session_controls_not_satisfied', n.get_collection_of_primitive_values(str)),
        }
        return fields
    
    @property
    def id(self,) -> Optional[str]:
        """
        Gets the id property value. Identifier of the conditional access policy.
        Returns: Optional[str]
        """
        return self._id
    
    @id.setter
    def id(self,value: Optional[str] = None) -> None:
        """
        Sets the id property value. Identifier of the conditional access policy.
        Args:
            value: Value to set for the id property.
        """
        self._id = value
    
    @property
    def include_rules_satisfied(self,) -> Optional[List[conditional_access_rule_satisfied.ConditionalAccessRuleSatisfied]]:
        """
        Gets the includeRulesSatisfied property value. List of key-value pairs containing each matched include condition in the conditional access policy. Example: [{ 'application' : 'AllApps'}, {'users': 'Group'}], meaning Application condition was a match because AllApps are included and Users condition was a match because the user was part of the included Group rule.
        Returns: Optional[List[conditional_access_rule_satisfied.ConditionalAccessRuleSatisfied]]
        """
        return self._include_rules_satisfied
    
    @include_rules_satisfied.setter
    def include_rules_satisfied(self,value: Optional[List[conditional_access_rule_satisfied.ConditionalAccessRuleSatisfied]] = None) -> None:
        """
        Sets the includeRulesSatisfied property value. List of key-value pairs containing each matched include condition in the conditional access policy. Example: [{ 'application' : 'AllApps'}, {'users': 'Group'}], meaning Application condition was a match because AllApps are included and Users condition was a match because the user was part of the included Group rule.
        Args:
            value: Value to set for the include_rules_satisfied property.
        """
        self._include_rules_satisfied = value
    
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
    def result(self,) -> Optional[applied_conditional_access_policy_result.AppliedConditionalAccessPolicyResult]:
        """
        Gets the result property value. Indicates the result of the CA policy that was triggered. Possible values are: success, failure, notApplied (Policy isn't applied because policy conditions were not met),notEnabled (This is due to the policy in disabled state), unknown, unknownFutureValue, reportOnlySuccess, reportOnlyFailure, reportOnlyNotApplied, reportOnlyInterrupted. Note that you must use the Prefer: include-unknown-enum-members request header to get the following values in this evolvable enum: reportOnlySuccess, reportOnlyFailure, reportOnlyNotApplied, reportOnlyInterrupted.
        Returns: Optional[applied_conditional_access_policy_result.AppliedConditionalAccessPolicyResult]
        """
        return self._result
    
    @result.setter
    def result(self,value: Optional[applied_conditional_access_policy_result.AppliedConditionalAccessPolicyResult] = None) -> None:
        """
        Sets the result property value. Indicates the result of the CA policy that was triggered. Possible values are: success, failure, notApplied (Policy isn't applied because policy conditions were not met),notEnabled (This is due to the policy in disabled state), unknown, unknownFutureValue, reportOnlySuccess, reportOnlyFailure, reportOnlyNotApplied, reportOnlyInterrupted. Note that you must use the Prefer: include-unknown-enum-members request header to get the following values in this evolvable enum: reportOnlySuccess, reportOnlyFailure, reportOnlyNotApplied, reportOnlyInterrupted.
        Args:
            value: Value to set for the result property.
        """
        self._result = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("authenticationStrength", self.authentication_strength)
        writer.write_enum_value("conditionsNotSatisfied", self.conditions_not_satisfied)
        writer.write_enum_value("conditionsSatisfied", self.conditions_satisfied)
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
    
    @property
    def session_controls_not_satisfied(self,) -> Optional[List[str]]:
        """
        Gets the sessionControlsNotSatisfied property value. Refers to the session controls that a sign-in activity did not satisfy. (Example: Application enforced Restrictions).
        Returns: Optional[List[str]]
        """
        return self._session_controls_not_satisfied
    
    @session_controls_not_satisfied.setter
    def session_controls_not_satisfied(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the sessionControlsNotSatisfied property value. Refers to the session controls that a sign-in activity did not satisfy. (Example: Application enforced Restrictions).
        Args:
            value: Value to set for the session_controls_not_satisfied property.
        """
        self._session_controls_not_satisfied = value
    

