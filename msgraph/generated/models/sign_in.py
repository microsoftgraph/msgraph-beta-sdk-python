from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

applied_authentication_event_listener = lazy_import('msgraph.generated.models.applied_authentication_event_listener')
applied_conditional_access_policy = lazy_import('msgraph.generated.models.applied_conditional_access_policy')
authentication_app_device_details = lazy_import('msgraph.generated.models.authentication_app_device_details')
authentication_app_policy_details = lazy_import('msgraph.generated.models.authentication_app_policy_details')
authentication_context = lazy_import('msgraph.generated.models.authentication_context')
authentication_detail = lazy_import('msgraph.generated.models.authentication_detail')
authentication_requirement_policy = lazy_import('msgraph.generated.models.authentication_requirement_policy')
client_credential_type = lazy_import('msgraph.generated.models.client_credential_type')
conditional_access_status = lazy_import('msgraph.generated.models.conditional_access_status')
device_detail = lazy_import('msgraph.generated.models.device_detail')
entity = lazy_import('msgraph.generated.models.entity')
incoming_token_type = lazy_import('msgraph.generated.models.incoming_token_type')
key_value = lazy_import('msgraph.generated.models.key_value')
mfa_detail = lazy_import('msgraph.generated.models.mfa_detail')
network_location_detail = lazy_import('msgraph.generated.models.network_location_detail')
private_link_details = lazy_import('msgraph.generated.models.private_link_details')
protocol_type = lazy_import('msgraph.generated.models.protocol_type')
risk_detail = lazy_import('msgraph.generated.models.risk_detail')
risk_level = lazy_import('msgraph.generated.models.risk_level')
risk_state = lazy_import('msgraph.generated.models.risk_state')
session_lifetime_policy = lazy_import('msgraph.generated.models.session_lifetime_policy')
sign_in_access_type = lazy_import('msgraph.generated.models.sign_in_access_type')
sign_in_identifier_type = lazy_import('msgraph.generated.models.sign_in_identifier_type')
sign_in_location = lazy_import('msgraph.generated.models.sign_in_location')
sign_in_status = lazy_import('msgraph.generated.models.sign_in_status')
sign_in_user_type = lazy_import('msgraph.generated.models.sign_in_user_type')
token_issuer_type = lazy_import('msgraph.generated.models.token_issuer_type')

class SignIn(entity.Entity):
    @property
    def app_display_name(self,) -> Optional[str]:
        """
        Gets the appDisplayName property value. The application name displayed in the Azure Portal. Supports $filter (eq and startsWith operators only).
        Returns: Optional[str]
        """
        return self._app_display_name
    
    @app_display_name.setter
    def app_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the appDisplayName property value. The application name displayed in the Azure Portal. Supports $filter (eq and startsWith operators only).
        Args:
            value: Value to set for the appDisplayName property.
        """
        self._app_display_name = value
    
    @property
    def app_id(self,) -> Optional[str]:
        """
        Gets the appId property value. The application identifier in Azure Active Directory. Supports $filter (eq operator only).
        Returns: Optional[str]
        """
        return self._app_id
    
    @app_id.setter
    def app_id(self,value: Optional[str] = None) -> None:
        """
        Sets the appId property value. The application identifier in Azure Active Directory. Supports $filter (eq operator only).
        Args:
            value: Value to set for the appId property.
        """
        self._app_id = value
    
    @property
    def applied_conditional_access_policies(self,) -> Optional[List[applied_conditional_access_policy.AppliedConditionalAccessPolicy]]:
        """
        Gets the appliedConditionalAccessPolicies property value. A list of conditional access policies that are triggered by the corresponding sign-in activity.
        Returns: Optional[List[applied_conditional_access_policy.AppliedConditionalAccessPolicy]]
        """
        return self._applied_conditional_access_policies
    
    @applied_conditional_access_policies.setter
    def applied_conditional_access_policies(self,value: Optional[List[applied_conditional_access_policy.AppliedConditionalAccessPolicy]] = None) -> None:
        """
        Sets the appliedConditionalAccessPolicies property value. A list of conditional access policies that are triggered by the corresponding sign-in activity.
        Args:
            value: Value to set for the appliedConditionalAccessPolicies property.
        """
        self._applied_conditional_access_policies = value
    
    @property
    def applied_event_listeners(self,) -> Optional[List[applied_authentication_event_listener.AppliedAuthenticationEventListener]]:
        """
        Gets the appliedEventListeners property value. The appliedEventListeners property
        Returns: Optional[List[applied_authentication_event_listener.AppliedAuthenticationEventListener]]
        """
        return self._applied_event_listeners
    
    @applied_event_listeners.setter
    def applied_event_listeners(self,value: Optional[List[applied_authentication_event_listener.AppliedAuthenticationEventListener]] = None) -> None:
        """
        Sets the appliedEventListeners property value. The appliedEventListeners property
        Args:
            value: Value to set for the appliedEventListeners property.
        """
        self._applied_event_listeners = value
    
    @property
    def authentication_app_device_details(self,) -> Optional[authentication_app_device_details.AuthenticationAppDeviceDetails]:
        """
        Gets the authenticationAppDeviceDetails property value. Provides details about the app and device used during an Azure AD authentication step.
        Returns: Optional[authentication_app_device_details.AuthenticationAppDeviceDetails]
        """
        return self._authentication_app_device_details
    
    @authentication_app_device_details.setter
    def authentication_app_device_details(self,value: Optional[authentication_app_device_details.AuthenticationAppDeviceDetails] = None) -> None:
        """
        Sets the authenticationAppDeviceDetails property value. Provides details about the app and device used during an Azure AD authentication step.
        Args:
            value: Value to set for the authenticationAppDeviceDetails property.
        """
        self._authentication_app_device_details = value
    
    @property
    def authentication_app_policy_evaluation_details(self,) -> Optional[List[authentication_app_policy_details.AuthenticationAppPolicyDetails]]:
        """
        Gets the authenticationAppPolicyEvaluationDetails property value. Provides details of the Azure AD policies applied to a user and client authentication app during an authentication step.
        Returns: Optional[List[authentication_app_policy_details.AuthenticationAppPolicyDetails]]
        """
        return self._authentication_app_policy_evaluation_details
    
    @authentication_app_policy_evaluation_details.setter
    def authentication_app_policy_evaluation_details(self,value: Optional[List[authentication_app_policy_details.AuthenticationAppPolicyDetails]] = None) -> None:
        """
        Sets the authenticationAppPolicyEvaluationDetails property value. Provides details of the Azure AD policies applied to a user and client authentication app during an authentication step.
        Args:
            value: Value to set for the authenticationAppPolicyEvaluationDetails property.
        """
        self._authentication_app_policy_evaluation_details = value
    
    @property
    def authentication_context_class_references(self,) -> Optional[List[authentication_context.AuthenticationContext]]:
        """
        Gets the authenticationContextClassReferences property value. Contains a collection of values that represent the conditional access authentication contexts applied to the sign-in.
        Returns: Optional[List[authentication_context.AuthenticationContext]]
        """
        return self._authentication_context_class_references
    
    @authentication_context_class_references.setter
    def authentication_context_class_references(self,value: Optional[List[authentication_context.AuthenticationContext]] = None) -> None:
        """
        Sets the authenticationContextClassReferences property value. Contains a collection of values that represent the conditional access authentication contexts applied to the sign-in.
        Args:
            value: Value to set for the authenticationContextClassReferences property.
        """
        self._authentication_context_class_references = value
    
    @property
    def authentication_details(self,) -> Optional[List[authentication_detail.AuthenticationDetail]]:
        """
        Gets the authenticationDetails property value. The result of the authentication attempt and additional details on the authentication method.
        Returns: Optional[List[authentication_detail.AuthenticationDetail]]
        """
        return self._authentication_details
    
    @authentication_details.setter
    def authentication_details(self,value: Optional[List[authentication_detail.AuthenticationDetail]] = None) -> None:
        """
        Sets the authenticationDetails property value. The result of the authentication attempt and additional details on the authentication method.
        Args:
            value: Value to set for the authenticationDetails property.
        """
        self._authentication_details = value
    
    @property
    def authentication_methods_used(self,) -> Optional[List[str]]:
        """
        Gets the authenticationMethodsUsed property value. The authentication methods used. Possible values: SMS, Authenticator App, App Verification code, Password, FIDO, PTA, or PHS.
        Returns: Optional[List[str]]
        """
        return self._authentication_methods_used
    
    @authentication_methods_used.setter
    def authentication_methods_used(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the authenticationMethodsUsed property value. The authentication methods used. Possible values: SMS, Authenticator App, App Verification code, Password, FIDO, PTA, or PHS.
        Args:
            value: Value to set for the authenticationMethodsUsed property.
        """
        self._authentication_methods_used = value
    
    @property
    def authentication_processing_details(self,) -> Optional[List[key_value.KeyValue]]:
        """
        Gets the authenticationProcessingDetails property value. Additional authentication processing details, such as the agent name in case of PTA/PHS or Server/farm name in case of federated authentication.
        Returns: Optional[List[key_value.KeyValue]]
        """
        return self._authentication_processing_details
    
    @authentication_processing_details.setter
    def authentication_processing_details(self,value: Optional[List[key_value.KeyValue]] = None) -> None:
        """
        Sets the authenticationProcessingDetails property value. Additional authentication processing details, such as the agent name in case of PTA/PHS or Server/farm name in case of federated authentication.
        Args:
            value: Value to set for the authenticationProcessingDetails property.
        """
        self._authentication_processing_details = value
    
    @property
    def authentication_protocol(self,) -> Optional[protocol_type.ProtocolType]:
        """
        Gets the authenticationProtocol property value. Lists the protocol type or grant type used in the authentication. The possible values are: none, oAuth2, ropc, wsFederation, saml20, deviceCode, unknownFutureValue. For authentications that use protocols other than the possible values listed, the protocol type is listed as none.
        Returns: Optional[protocol_type.ProtocolType]
        """
        return self._authentication_protocol
    
    @authentication_protocol.setter
    def authentication_protocol(self,value: Optional[protocol_type.ProtocolType] = None) -> None:
        """
        Sets the authenticationProtocol property value. Lists the protocol type or grant type used in the authentication. The possible values are: none, oAuth2, ropc, wsFederation, saml20, deviceCode, unknownFutureValue. For authentications that use protocols other than the possible values listed, the protocol type is listed as none.
        Args:
            value: Value to set for the authenticationProtocol property.
        """
        self._authentication_protocol = value
    
    @property
    def authentication_requirement(self,) -> Optional[str]:
        """
        Gets the authenticationRequirement property value. This holds the highest level of authentication needed through all the sign-in steps, for sign-in to succeed. Supports $filter (eq and startsWith operators only).
        Returns: Optional[str]
        """
        return self._authentication_requirement
    
    @authentication_requirement.setter
    def authentication_requirement(self,value: Optional[str] = None) -> None:
        """
        Sets the authenticationRequirement property value. This holds the highest level of authentication needed through all the sign-in steps, for sign-in to succeed. Supports $filter (eq and startsWith operators only).
        Args:
            value: Value to set for the authenticationRequirement property.
        """
        self._authentication_requirement = value
    
    @property
    def authentication_requirement_policies(self,) -> Optional[List[authentication_requirement_policy.AuthenticationRequirementPolicy]]:
        """
        Gets the authenticationRequirementPolicies property value. Sources of authentication requirement, such as conditional access, per-user MFA, identity protection, and security defaults.
        Returns: Optional[List[authentication_requirement_policy.AuthenticationRequirementPolicy]]
        """
        return self._authentication_requirement_policies
    
    @authentication_requirement_policies.setter
    def authentication_requirement_policies(self,value: Optional[List[authentication_requirement_policy.AuthenticationRequirementPolicy]] = None) -> None:
        """
        Sets the authenticationRequirementPolicies property value. Sources of authentication requirement, such as conditional access, per-user MFA, identity protection, and security defaults.
        Args:
            value: Value to set for the authenticationRequirementPolicies property.
        """
        self._authentication_requirement_policies = value
    
    @property
    def autonomous_system_number(self,) -> Optional[int]:
        """
        Gets the autonomousSystemNumber property value. The Autonomous System Number (ASN) of the network used by the actor.
        Returns: Optional[int]
        """
        return self._autonomous_system_number
    
    @autonomous_system_number.setter
    def autonomous_system_number(self,value: Optional[int] = None) -> None:
        """
        Sets the autonomousSystemNumber property value. The Autonomous System Number (ASN) of the network used by the actor.
        Args:
            value: Value to set for the autonomousSystemNumber property.
        """
        self._autonomous_system_number = value
    
    @property
    def azure_resource_id(self,) -> Optional[str]:
        """
        Gets the azureResourceId property value. Contains a fully qualified Azure Resource Manager ID of an Azure resource accessed during the sign-in.
        Returns: Optional[str]
        """
        return self._azure_resource_id
    
    @azure_resource_id.setter
    def azure_resource_id(self,value: Optional[str] = None) -> None:
        """
        Sets the azureResourceId property value. Contains a fully qualified Azure Resource Manager ID of an Azure resource accessed during the sign-in.
        Args:
            value: Value to set for the azureResourceId property.
        """
        self._azure_resource_id = value
    
    @property
    def client_app_used(self,) -> Optional[str]:
        """
        Gets the clientAppUsed property value. The legacy client used for sign-in activity. For example: Browser, Exchange ActiveSync, Modern clients, IMAP, MAPI, SMTP, or POP. Supports $filter (eq operator only).
        Returns: Optional[str]
        """
        return self._client_app_used
    
    @client_app_used.setter
    def client_app_used(self,value: Optional[str] = None) -> None:
        """
        Sets the clientAppUsed property value. The legacy client used for sign-in activity. For example: Browser, Exchange ActiveSync, Modern clients, IMAP, MAPI, SMTP, or POP. Supports $filter (eq operator only).
        Args:
            value: Value to set for the clientAppUsed property.
        """
        self._client_app_used = value
    
    @property
    def client_credential_type(self,) -> Optional[client_credential_type.ClientCredentialType]:
        """
        Gets the clientCredentialType property value. Describes the credential type that a user client or service principal provided to Azure AD to authenticate itself. You may wish to review clientCredentialType to track and eliminate less secure credential types or to watch for clients and service principals using anomalous credential types. The possible values are: none, clientSecret, clientAssertion, federatedIdentityCredential, managedIdentity, certificate, unknownFutureValue.
        Returns: Optional[client_credential_type.ClientCredentialType]
        """
        return self._client_credential_type
    
    @client_credential_type.setter
    def client_credential_type(self,value: Optional[client_credential_type.ClientCredentialType] = None) -> None:
        """
        Sets the clientCredentialType property value. Describes the credential type that a user client or service principal provided to Azure AD to authenticate itself. You may wish to review clientCredentialType to track and eliminate less secure credential types or to watch for clients and service principals using anomalous credential types. The possible values are: none, clientSecret, clientAssertion, federatedIdentityCredential, managedIdentity, certificate, unknownFutureValue.
        Args:
            value: Value to set for the clientCredentialType property.
        """
        self._client_credential_type = value
    
    @property
    def conditional_access_status(self,) -> Optional[conditional_access_status.ConditionalAccessStatus]:
        """
        Gets the conditionalAccessStatus property value. The status of the conditional access policy triggered. Possible values: success, failure, notApplied, or unknownFutureValue. Supports $filter (eq operator only).
        Returns: Optional[conditional_access_status.ConditionalAccessStatus]
        """
        return self._conditional_access_status
    
    @conditional_access_status.setter
    def conditional_access_status(self,value: Optional[conditional_access_status.ConditionalAccessStatus] = None) -> None:
        """
        Sets the conditionalAccessStatus property value. The status of the conditional access policy triggered. Possible values: success, failure, notApplied, or unknownFutureValue. Supports $filter (eq operator only).
        Args:
            value: Value to set for the conditionalAccessStatus property.
        """
        self._conditional_access_status = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new SignIn and sets the default values.
        """
        super().__init__()
        # The application name displayed in the Azure Portal. Supports $filter (eq and startsWith operators only).
        self._app_display_name: Optional[str] = None
        # The application identifier in Azure Active Directory. Supports $filter (eq operator only).
        self._app_id: Optional[str] = None
        # A list of conditional access policies that are triggered by the corresponding sign-in activity.
        self._applied_conditional_access_policies: Optional[List[applied_conditional_access_policy.AppliedConditionalAccessPolicy]] = None
        # The appliedEventListeners property
        self._applied_event_listeners: Optional[List[applied_authentication_event_listener.AppliedAuthenticationEventListener]] = None
        # Provides details about the app and device used during an Azure AD authentication step.
        self._authentication_app_device_details: Optional[authentication_app_device_details.AuthenticationAppDeviceDetails] = None
        # Provides details of the Azure AD policies applied to a user and client authentication app during an authentication step.
        self._authentication_app_policy_evaluation_details: Optional[List[authentication_app_policy_details.AuthenticationAppPolicyDetails]] = None
        # Contains a collection of values that represent the conditional access authentication contexts applied to the sign-in.
        self._authentication_context_class_references: Optional[List[authentication_context.AuthenticationContext]] = None
        # The result of the authentication attempt and additional details on the authentication method.
        self._authentication_details: Optional[List[authentication_detail.AuthenticationDetail]] = None
        # The authentication methods used. Possible values: SMS, Authenticator App, App Verification code, Password, FIDO, PTA, or PHS.
        self._authentication_methods_used: Optional[List[str]] = None
        # Additional authentication processing details, such as the agent name in case of PTA/PHS or Server/farm name in case of federated authentication.
        self._authentication_processing_details: Optional[List[key_value.KeyValue]] = None
        # Lists the protocol type or grant type used in the authentication. The possible values are: none, oAuth2, ropc, wsFederation, saml20, deviceCode, unknownFutureValue. For authentications that use protocols other than the possible values listed, the protocol type is listed as none.
        self._authentication_protocol: Optional[protocol_type.ProtocolType] = None
        # This holds the highest level of authentication needed through all the sign-in steps, for sign-in to succeed. Supports $filter (eq and startsWith operators only).
        self._authentication_requirement: Optional[str] = None
        # Sources of authentication requirement, such as conditional access, per-user MFA, identity protection, and security defaults.
        self._authentication_requirement_policies: Optional[List[authentication_requirement_policy.AuthenticationRequirementPolicy]] = None
        # The Autonomous System Number (ASN) of the network used by the actor.
        self._autonomous_system_number: Optional[int] = None
        # Contains a fully qualified Azure Resource Manager ID of an Azure resource accessed during the sign-in.
        self._azure_resource_id: Optional[str] = None
        # The legacy client used for sign-in activity. For example: Browser, Exchange ActiveSync, Modern clients, IMAP, MAPI, SMTP, or POP. Supports $filter (eq operator only).
        self._client_app_used: Optional[str] = None
        # Describes the credential type that a user client or service principal provided to Azure AD to authenticate itself. You may wish to review clientCredentialType to track and eliminate less secure credential types or to watch for clients and service principals using anomalous credential types. The possible values are: none, clientSecret, clientAssertion, federatedIdentityCredential, managedIdentity, certificate, unknownFutureValue.
        self._client_credential_type: Optional[client_credential_type.ClientCredentialType] = None
        # The status of the conditional access policy triggered. Possible values: success, failure, notApplied, or unknownFutureValue. Supports $filter (eq operator only).
        self._conditional_access_status: Optional[conditional_access_status.ConditionalAccessStatus] = None
        # The identifier that's sent from the client when sign-in is initiated. This is used for troubleshooting the corresponding sign-in activity when calling for support. Supports $filter (eq operator only).
        self._correlation_id: Optional[str] = None
        # The date and time the sign-in was initiated. The Timestamp type is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Supports $orderby and $filter (eq, le, and ge operators only).
        self._created_date_time: Optional[datetime] = None
        # Describes the type of cross-tenant access used by the actor to access the resource. Possible values are: none, b2bCollaboration, b2bDirectConnect, microsoftSupport, serviceProvider, unknownFutureValue. If the sign in did not cross tenant boundaries, the value is none.
        self._cross_tenant_access_type: Optional[sign_in_access_type.SignInAccessType] = None
        # The device information from where the sign-in occurred. Includes information such as deviceId, OS, and browser. Supports $filter (eq and startsWith operators only) on browser and operatingSystem properties.
        self._device_detail: Optional[device_detail.DeviceDetail] = None
        # Contains the identifier of an application's federated identity credential, if a federated identity credential was used to sign in.
        self._federated_credential_id: Optional[str] = None
        # During a failed sign in, a user may click a button in the Azure portal to mark the failed event for tenant admins. If a user clicked the button to flag the failed sign in, this value is true.
        self._flagged_for_review: Optional[bool] = None
        # The tenant identifier of the user initiating the sign in. Not applicable in Managed Identity or service principal sign ins.
        self._home_tenant_id: Optional[str] = None
        # For user sign ins, the identifier of the tenant that the user is a member of. Only populated in cases where the home tenant has provided affirmative consent to Azure AD to show the tenant content.
        self._home_tenant_name: Optional[str] = None
        # Indicates the token types that were presented to Azure AD to authenticate the actor in the sign in. The possible values are: none, primaryRefreshToken, saml11, saml20, unknownFutureValue, remoteDesktopToken.  NOTE Azure AD may have also used token types not listed in this Enum type to authenticate the actor. Do not infer the lack of a token if it is not one of the types listed. Also, please note that you must use the Prefer: include-unknown-enum-members request header to get the following value(s) in this evolvable enum: remoteDesktopToken.
        self._incoming_token_type: Optional[incoming_token_type.IncomingTokenType] = None
        # The IP address of the client from where the sign-in occurred. Supports $filter (eq and startsWith operators only).
        self._ip_address: Optional[str] = None
        # The IP address a user used to reach a resource provider, used to determine Conditional Access compliance for some policies. For example, when a user interacts with Exchange Online, the IP address Exchange receives from the user may be recorded here. This value is often null.
        self._ip_address_from_resource_provider: Optional[str] = None
        # Indicates whether a user sign in is interactive. In interactive sign in, the user provides an authentication factor to Azure AD. These factors include passwords, responses to MFA challenges, biometric factors, or QR codes that a user provides to Azure AD or an associated app. In non-interactive sign in, the user doesn't provide an authentication factor. Instead, the client app uses a token or code to authenticate or access a resource on behalf of a user. Non-interactive sign ins are commonly used for a client to sign in on a user's behalf in a process transparent to the user.
        self._is_interactive: Optional[bool] = None
        # Shows whether the sign in event was subject to an Azure AD tenant restriction policy.
        self._is_tenant_restricted: Optional[bool] = None
        # The city, state, and 2 letter country code from where the sign-in occurred. Supports $filter (eq and startsWith operators only) on city, state, and countryOrRegion properties.
        self._location: Optional[sign_in_location.SignInLocation] = None
        # The mfaDetail property
        self._mfa_detail: Optional[mfa_detail.MfaDetail] = None
        # The network location details including the type of network used and its names.
        self._network_location_details: Optional[List[network_location_detail.NetworkLocationDetail]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The request identifier of the first request in the authentication sequence. Supports $filter (eq operator only).
        self._original_request_id: Optional[str] = None
        # Contains information about the Azure AD Private Link policy that is associated with the sign in event.
        self._private_link_details: Optional[private_link_details.PrivateLinkDetails] = None
        # The request processing time in milliseconds in AD STS.
        self._processing_time_in_milliseconds: Optional[int] = None
        # The name of the resource that the user signed in to. Supports $filter (eq operator only).
        self._resource_display_name: Optional[str] = None
        # The identifier of the resource that the user signed in to. Supports $filter (eq operator only).
        self._resource_id: Optional[str] = None
        # The identifier of the service principal representing the target resource in the sign-in event.
        self._resource_service_principal_id: Optional[str] = None
        # The tenant identifier of the resource referenced in the sign in.
        self._resource_tenant_id: Optional[str] = None
        # The reason behind a specific state of a risky user, sign-in, or a risk event. Possible values: none, adminGeneratedTemporaryPassword, userPerformedSecuredPasswordChange, userPerformedSecuredPasswordReset, adminConfirmedSigninSafe, aiConfirmedSigninSafe, userPassedMFADrivenByRiskBasedPolicy, adminDismissedAllRiskForUser, adminConfirmedSigninCompromised, or unknownFutureValue. The value none means that no action has been performed on the user or sign-in so far. Supports $filter (eq operator only). Note: Details for this property are only available for Azure AD Premium P2 customers. All other customers are returned hidden.
        self._risk_detail: Optional[risk_detail.RiskDetail] = None
        # The list of risk event types associated with the sign-in. Possible values: unlikelyTravel, anonymizedIPAddress, maliciousIPAddress, unfamiliarFeatures, malwareInfectedIPAddress, suspiciousIPAddress, leakedCredentials, investigationsThreatIntelligence,  generic, or unknownFutureValue. Supports $filter (eq and startsWith operators only).
        self._risk_event_types_v2: Optional[List[str]] = None
        # The aggregated risk level. Possible values: none, low, medium, high, hidden, or unknownFutureValue. The value hidden means the user or sign-in was not enabled for Azure AD Identity Protection. Supports $filter (eq operator only). Note: Details for this property are only available for Azure AD Premium P2 customers. All other customers are returned hidden.
        self._risk_level_aggregated: Optional[risk_level.RiskLevel] = None
        # The risk level during sign-in. Possible values: none, low, medium, high, hidden, or unknownFutureValue. The value hidden means the user or sign-in was not enabled for Azure AD Identity Protection. Supports $filter (eq operator only). Note: Details for this property are only available for Azure AD Premium P2 customers. All other customers are returned hidden.
        self._risk_level_during_sign_in: Optional[risk_level.RiskLevel] = None
        # The risk state of a risky user, sign-in, or a risk event. Possible values: none, confirmedSafe, remediated, dismissed, atRisk, confirmedCompromised, or unknownFutureValue. Supports $filter (eq operator only).
        self._risk_state: Optional[risk_state.RiskState] = None
        # The unique identifier of the key credential used by the service principal to authenticate.
        self._service_principal_credential_key_id: Optional[str] = None
        # The certificate thumbprint of the certificate used by the service principal to authenticate.
        self._service_principal_credential_thumbprint: Optional[str] = None
        # The application identifier used for sign-in. This field is populated when you are signing in using an application. Supports $filter (eq and startsWith operators only).
        self._service_principal_id: Optional[str] = None
        # The application name used for sign-in. This field is populated when you are signing in using an application. Supports $filter (eq and startsWith operators only).
        self._service_principal_name: Optional[str] = None
        # Any conditional access session management policies that were applied during the sign-in event.
        self._session_lifetime_policies: Optional[List[session_lifetime_policy.SessionLifetimePolicy]] = None
        # Indicates the category of sign in that the event represents. For user sign ins, the category can be interactiveUser or nonInteractiveUser and corresponds to the value for the isInteractive property on the signin resource. For managed identity sign ins, the category is managedIdentity. For service principal sign ins, the category is servicePrincipal. Possible values are: interactiveUser, nonInteractiveUser, servicePrincipal, managedIdentity, unknownFutureValue. Supports $filter (eq, ne).
        self._sign_in_event_types: Optional[List[str]] = None
        # The identification that the user provided to sign in. It may be the userPrincipalName but it's also populated when a user signs in using other identifiers.
        self._sign_in_identifier: Optional[str] = None
        # The type of sign in identifier. Possible values are: userPrincipalName, phoneNumber, proxyAddress, qrCode, onPremisesUserPrincipalName, unknownFutureValue.
        self._sign_in_identifier_type: Optional[sign_in_identifier_type.SignInIdentifierType] = None
        # The sign-in status. Includes the error code and description of the error (in case of a sign-in failure). Supports $filter (eq operator only) on errorCode property.
        self._status: Optional[sign_in_status.SignInStatus] = None
        # The name of the identity provider. For example, sts.microsoft.com. Supports $filter (eq operator only).
        self._token_issuer_name: Optional[str] = None
        # The type of identity provider. The possible values are: AzureAD, ADFederationServices, UnknownFutureValue, AzureADBackupAuth, ADFederationServicesMFAAdapter, NPSExtension. Note that you must use the Prefer: include-unknown-enum-members request header to get the following values in this evolvable enum: AzureADBackupAuth , ADFederationServicesMFAAdapter , NPSExtension.
        self._token_issuer_type: Optional[token_issuer_type.TokenIssuerType] = None
        # A unique base64 encoded request identifier used to track tokens issued by Azure AD as they are redeemed at resource providers.
        self._unique_token_identifier: Optional[str] = None
        # The user agent information related to sign-in. Supports $filter (eq and startsWith operators only).
        self._user_agent: Optional[str] = None
        # The display name of the user. Supports $filter (eq and startsWith operators only).
        self._user_display_name: Optional[str] = None
        # The identifier of the user. Supports $filter (eq operator only).
        self._user_id: Optional[str] = None
        # The UPN of the user. Supports $filter (eq and startsWith operators only).
        self._user_principal_name: Optional[str] = None
        # Identifies whether the user is a member or guest in the tenant. Possible values are: member, guest, unknownFutureValue.
        self._user_type: Optional[sign_in_user_type.SignInUserType] = None
    
    @property
    def correlation_id(self,) -> Optional[str]:
        """
        Gets the correlationId property value. The identifier that's sent from the client when sign-in is initiated. This is used for troubleshooting the corresponding sign-in activity when calling for support. Supports $filter (eq operator only).
        Returns: Optional[str]
        """
        return self._correlation_id
    
    @correlation_id.setter
    def correlation_id(self,value: Optional[str] = None) -> None:
        """
        Sets the correlationId property value. The identifier that's sent from the client when sign-in is initiated. This is used for troubleshooting the corresponding sign-in activity when calling for support. Supports $filter (eq operator only).
        Args:
            value: Value to set for the correlationId property.
        """
        self._correlation_id = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The date and time the sign-in was initiated. The Timestamp type is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Supports $orderby and $filter (eq, le, and ge operators only).
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The date and time the sign-in was initiated. The Timestamp type is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Supports $orderby and $filter (eq, le, and ge operators only).
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SignIn:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SignIn
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SignIn()
    
    @property
    def cross_tenant_access_type(self,) -> Optional[sign_in_access_type.SignInAccessType]:
        """
        Gets the crossTenantAccessType property value. Describes the type of cross-tenant access used by the actor to access the resource. Possible values are: none, b2bCollaboration, b2bDirectConnect, microsoftSupport, serviceProvider, unknownFutureValue. If the sign in did not cross tenant boundaries, the value is none.
        Returns: Optional[sign_in_access_type.SignInAccessType]
        """
        return self._cross_tenant_access_type
    
    @cross_tenant_access_type.setter
    def cross_tenant_access_type(self,value: Optional[sign_in_access_type.SignInAccessType] = None) -> None:
        """
        Sets the crossTenantAccessType property value. Describes the type of cross-tenant access used by the actor to access the resource. Possible values are: none, b2bCollaboration, b2bDirectConnect, microsoftSupport, serviceProvider, unknownFutureValue. If the sign in did not cross tenant boundaries, the value is none.
        Args:
            value: Value to set for the crossTenantAccessType property.
        """
        self._cross_tenant_access_type = value
    
    @property
    def device_detail(self,) -> Optional[device_detail.DeviceDetail]:
        """
        Gets the deviceDetail property value. The device information from where the sign-in occurred. Includes information such as deviceId, OS, and browser. Supports $filter (eq and startsWith operators only) on browser and operatingSystem properties.
        Returns: Optional[device_detail.DeviceDetail]
        """
        return self._device_detail
    
    @device_detail.setter
    def device_detail(self,value: Optional[device_detail.DeviceDetail] = None) -> None:
        """
        Sets the deviceDetail property value. The device information from where the sign-in occurred. Includes information such as deviceId, OS, and browser. Supports $filter (eq and startsWith operators only) on browser and operatingSystem properties.
        Args:
            value: Value to set for the deviceDetail property.
        """
        self._device_detail = value
    
    @property
    def federated_credential_id(self,) -> Optional[str]:
        """
        Gets the federatedCredentialId property value. Contains the identifier of an application's federated identity credential, if a federated identity credential was used to sign in.
        Returns: Optional[str]
        """
        return self._federated_credential_id
    
    @federated_credential_id.setter
    def federated_credential_id(self,value: Optional[str] = None) -> None:
        """
        Sets the federatedCredentialId property value. Contains the identifier of an application's federated identity credential, if a federated identity credential was used to sign in.
        Args:
            value: Value to set for the federatedCredentialId property.
        """
        self._federated_credential_id = value
    
    @property
    def flagged_for_review(self,) -> Optional[bool]:
        """
        Gets the flaggedForReview property value. During a failed sign in, a user may click a button in the Azure portal to mark the failed event for tenant admins. If a user clicked the button to flag the failed sign in, this value is true.
        Returns: Optional[bool]
        """
        return self._flagged_for_review
    
    @flagged_for_review.setter
    def flagged_for_review(self,value: Optional[bool] = None) -> None:
        """
        Sets the flaggedForReview property value. During a failed sign in, a user may click a button in the Azure portal to mark the failed event for tenant admins. If a user clicked the button to flag the failed sign in, this value is true.
        Args:
            value: Value to set for the flaggedForReview property.
        """
        self._flagged_for_review = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "app_display_name": lambda n : setattr(self, 'app_display_name', n.get_str_value()),
            "app_id": lambda n : setattr(self, 'app_id', n.get_str_value()),
            "applied_conditional_access_policies": lambda n : setattr(self, 'applied_conditional_access_policies', n.get_collection_of_object_values(applied_conditional_access_policy.AppliedConditionalAccessPolicy)),
            "applied_event_listeners": lambda n : setattr(self, 'applied_event_listeners', n.get_collection_of_object_values(applied_authentication_event_listener.AppliedAuthenticationEventListener)),
            "authentication_app_device_details": lambda n : setattr(self, 'authentication_app_device_details', n.get_object_value(authentication_app_device_details.AuthenticationAppDeviceDetails)),
            "authentication_app_policy_evaluation_details": lambda n : setattr(self, 'authentication_app_policy_evaluation_details', n.get_collection_of_object_values(authentication_app_policy_details.AuthenticationAppPolicyDetails)),
            "authentication_context_class_references": lambda n : setattr(self, 'authentication_context_class_references', n.get_collection_of_object_values(authentication_context.AuthenticationContext)),
            "authentication_details": lambda n : setattr(self, 'authentication_details', n.get_collection_of_object_values(authentication_detail.AuthenticationDetail)),
            "authentication_methods_used": lambda n : setattr(self, 'authentication_methods_used', n.get_collection_of_primitive_values(str)),
            "authentication_processing_details": lambda n : setattr(self, 'authentication_processing_details', n.get_collection_of_object_values(key_value.KeyValue)),
            "authentication_protocol": lambda n : setattr(self, 'authentication_protocol', n.get_enum_value(protocol_type.ProtocolType)),
            "authentication_requirement": lambda n : setattr(self, 'authentication_requirement', n.get_str_value()),
            "authentication_requirement_policies": lambda n : setattr(self, 'authentication_requirement_policies', n.get_collection_of_object_values(authentication_requirement_policy.AuthenticationRequirementPolicy)),
            "autonomous_system_number": lambda n : setattr(self, 'autonomous_system_number', n.get_int_value()),
            "azure_resource_id": lambda n : setattr(self, 'azure_resource_id', n.get_str_value()),
            "client_app_used": lambda n : setattr(self, 'client_app_used', n.get_str_value()),
            "client_credential_type": lambda n : setattr(self, 'client_credential_type', n.get_enum_value(client_credential_type.ClientCredentialType)),
            "conditional_access_status": lambda n : setattr(self, 'conditional_access_status', n.get_enum_value(conditional_access_status.ConditionalAccessStatus)),
            "correlation_id": lambda n : setattr(self, 'correlation_id', n.get_str_value()),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "cross_tenant_access_type": lambda n : setattr(self, 'cross_tenant_access_type', n.get_enum_value(sign_in_access_type.SignInAccessType)),
            "device_detail": lambda n : setattr(self, 'device_detail', n.get_object_value(device_detail.DeviceDetail)),
            "federated_credential_id": lambda n : setattr(self, 'federated_credential_id', n.get_str_value()),
            "flagged_for_review": lambda n : setattr(self, 'flagged_for_review', n.get_bool_value()),
            "home_tenant_id": lambda n : setattr(self, 'home_tenant_id', n.get_str_value()),
            "home_tenant_name": lambda n : setattr(self, 'home_tenant_name', n.get_str_value()),
            "incoming_token_type": lambda n : setattr(self, 'incoming_token_type', n.get_enum_value(incoming_token_type.IncomingTokenType)),
            "ip_address": lambda n : setattr(self, 'ip_address', n.get_str_value()),
            "ip_address_from_resource_provider": lambda n : setattr(self, 'ip_address_from_resource_provider', n.get_str_value()),
            "is_interactive": lambda n : setattr(self, 'is_interactive', n.get_bool_value()),
            "is_tenant_restricted": lambda n : setattr(self, 'is_tenant_restricted', n.get_bool_value()),
            "location": lambda n : setattr(self, 'location', n.get_object_value(sign_in_location.SignInLocation)),
            "mfa_detail": lambda n : setattr(self, 'mfa_detail', n.get_object_value(mfa_detail.MfaDetail)),
            "network_location_details": lambda n : setattr(self, 'network_location_details', n.get_collection_of_object_values(network_location_detail.NetworkLocationDetail)),
            "original_request_id": lambda n : setattr(self, 'original_request_id', n.get_str_value()),
            "private_link_details": lambda n : setattr(self, 'private_link_details', n.get_object_value(private_link_details.PrivateLinkDetails)),
            "processing_time_in_milliseconds": lambda n : setattr(self, 'processing_time_in_milliseconds', n.get_int_value()),
            "resource_display_name": lambda n : setattr(self, 'resource_display_name', n.get_str_value()),
            "resource_id": lambda n : setattr(self, 'resource_id', n.get_str_value()),
            "resource_service_principal_id": lambda n : setattr(self, 'resource_service_principal_id', n.get_str_value()),
            "resource_tenant_id": lambda n : setattr(self, 'resource_tenant_id', n.get_str_value()),
            "risk_detail": lambda n : setattr(self, 'risk_detail', n.get_enum_value(risk_detail.RiskDetail)),
            "risk_event_types_v2": lambda n : setattr(self, 'risk_event_types_v2', n.get_collection_of_primitive_values(str)),
            "risk_level_aggregated": lambda n : setattr(self, 'risk_level_aggregated', n.get_enum_value(risk_level.RiskLevel)),
            "risk_level_during_sign_in": lambda n : setattr(self, 'risk_level_during_sign_in', n.get_enum_value(risk_level.RiskLevel)),
            "risk_state": lambda n : setattr(self, 'risk_state', n.get_enum_value(risk_state.RiskState)),
            "service_principal_credential_key_id": lambda n : setattr(self, 'service_principal_credential_key_id', n.get_str_value()),
            "service_principal_credential_thumbprint": lambda n : setattr(self, 'service_principal_credential_thumbprint', n.get_str_value()),
            "service_principal_id": lambda n : setattr(self, 'service_principal_id', n.get_str_value()),
            "service_principal_name": lambda n : setattr(self, 'service_principal_name', n.get_str_value()),
            "session_lifetime_policies": lambda n : setattr(self, 'session_lifetime_policies', n.get_collection_of_object_values(session_lifetime_policy.SessionLifetimePolicy)),
            "sign_in_event_types": lambda n : setattr(self, 'sign_in_event_types', n.get_collection_of_primitive_values(str)),
            "sign_in_identifier": lambda n : setattr(self, 'sign_in_identifier', n.get_str_value()),
            "sign_in_identifier_type": lambda n : setattr(self, 'sign_in_identifier_type', n.get_enum_value(sign_in_identifier_type.SignInIdentifierType)),
            "status": lambda n : setattr(self, 'status', n.get_object_value(sign_in_status.SignInStatus)),
            "token_issuer_name": lambda n : setattr(self, 'token_issuer_name', n.get_str_value()),
            "token_issuer_type": lambda n : setattr(self, 'token_issuer_type', n.get_enum_value(token_issuer_type.TokenIssuerType)),
            "unique_token_identifier": lambda n : setattr(self, 'unique_token_identifier', n.get_str_value()),
            "user_agent": lambda n : setattr(self, 'user_agent', n.get_str_value()),
            "user_display_name": lambda n : setattr(self, 'user_display_name', n.get_str_value()),
            "user_id": lambda n : setattr(self, 'user_id', n.get_str_value()),
            "user_principal_name": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
            "user_type": lambda n : setattr(self, 'user_type', n.get_enum_value(sign_in_user_type.SignInUserType)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def home_tenant_id(self,) -> Optional[str]:
        """
        Gets the homeTenantId property value. The tenant identifier of the user initiating the sign in. Not applicable in Managed Identity or service principal sign ins.
        Returns: Optional[str]
        """
        return self._home_tenant_id
    
    @home_tenant_id.setter
    def home_tenant_id(self,value: Optional[str] = None) -> None:
        """
        Sets the homeTenantId property value. The tenant identifier of the user initiating the sign in. Not applicable in Managed Identity or service principal sign ins.
        Args:
            value: Value to set for the homeTenantId property.
        """
        self._home_tenant_id = value
    
    @property
    def home_tenant_name(self,) -> Optional[str]:
        """
        Gets the homeTenantName property value. For user sign ins, the identifier of the tenant that the user is a member of. Only populated in cases where the home tenant has provided affirmative consent to Azure AD to show the tenant content.
        Returns: Optional[str]
        """
        return self._home_tenant_name
    
    @home_tenant_name.setter
    def home_tenant_name(self,value: Optional[str] = None) -> None:
        """
        Sets the homeTenantName property value. For user sign ins, the identifier of the tenant that the user is a member of. Only populated in cases where the home tenant has provided affirmative consent to Azure AD to show the tenant content.
        Args:
            value: Value to set for the homeTenantName property.
        """
        self._home_tenant_name = value
    
    @property
    def incoming_token_type(self,) -> Optional[incoming_token_type.IncomingTokenType]:
        """
        Gets the incomingTokenType property value. Indicates the token types that were presented to Azure AD to authenticate the actor in the sign in. The possible values are: none, primaryRefreshToken, saml11, saml20, unknownFutureValue, remoteDesktopToken.  NOTE Azure AD may have also used token types not listed in this Enum type to authenticate the actor. Do not infer the lack of a token if it is not one of the types listed. Also, please note that you must use the Prefer: include-unknown-enum-members request header to get the following value(s) in this evolvable enum: remoteDesktopToken.
        Returns: Optional[incoming_token_type.IncomingTokenType]
        """
        return self._incoming_token_type
    
    @incoming_token_type.setter
    def incoming_token_type(self,value: Optional[incoming_token_type.IncomingTokenType] = None) -> None:
        """
        Sets the incomingTokenType property value. Indicates the token types that were presented to Azure AD to authenticate the actor in the sign in. The possible values are: none, primaryRefreshToken, saml11, saml20, unknownFutureValue, remoteDesktopToken.  NOTE Azure AD may have also used token types not listed in this Enum type to authenticate the actor. Do not infer the lack of a token if it is not one of the types listed. Also, please note that you must use the Prefer: include-unknown-enum-members request header to get the following value(s) in this evolvable enum: remoteDesktopToken.
        Args:
            value: Value to set for the incomingTokenType property.
        """
        self._incoming_token_type = value
    
    @property
    def ip_address(self,) -> Optional[str]:
        """
        Gets the ipAddress property value. The IP address of the client from where the sign-in occurred. Supports $filter (eq and startsWith operators only).
        Returns: Optional[str]
        """
        return self._ip_address
    
    @ip_address.setter
    def ip_address(self,value: Optional[str] = None) -> None:
        """
        Sets the ipAddress property value. The IP address of the client from where the sign-in occurred. Supports $filter (eq and startsWith operators only).
        Args:
            value: Value to set for the ipAddress property.
        """
        self._ip_address = value
    
    @property
    def ip_address_from_resource_provider(self,) -> Optional[str]:
        """
        Gets the ipAddressFromResourceProvider property value. The IP address a user used to reach a resource provider, used to determine Conditional Access compliance for some policies. For example, when a user interacts with Exchange Online, the IP address Exchange receives from the user may be recorded here. This value is often null.
        Returns: Optional[str]
        """
        return self._ip_address_from_resource_provider
    
    @ip_address_from_resource_provider.setter
    def ip_address_from_resource_provider(self,value: Optional[str] = None) -> None:
        """
        Sets the ipAddressFromResourceProvider property value. The IP address a user used to reach a resource provider, used to determine Conditional Access compliance for some policies. For example, when a user interacts with Exchange Online, the IP address Exchange receives from the user may be recorded here. This value is often null.
        Args:
            value: Value to set for the ipAddressFromResourceProvider property.
        """
        self._ip_address_from_resource_provider = value
    
    @property
    def is_interactive(self,) -> Optional[bool]:
        """
        Gets the isInteractive property value. Indicates whether a user sign in is interactive. In interactive sign in, the user provides an authentication factor to Azure AD. These factors include passwords, responses to MFA challenges, biometric factors, or QR codes that a user provides to Azure AD or an associated app. In non-interactive sign in, the user doesn't provide an authentication factor. Instead, the client app uses a token or code to authenticate or access a resource on behalf of a user. Non-interactive sign ins are commonly used for a client to sign in on a user's behalf in a process transparent to the user.
        Returns: Optional[bool]
        """
        return self._is_interactive
    
    @is_interactive.setter
    def is_interactive(self,value: Optional[bool] = None) -> None:
        """
        Sets the isInteractive property value. Indicates whether a user sign in is interactive. In interactive sign in, the user provides an authentication factor to Azure AD. These factors include passwords, responses to MFA challenges, biometric factors, or QR codes that a user provides to Azure AD or an associated app. In non-interactive sign in, the user doesn't provide an authentication factor. Instead, the client app uses a token or code to authenticate or access a resource on behalf of a user. Non-interactive sign ins are commonly used for a client to sign in on a user's behalf in a process transparent to the user.
        Args:
            value: Value to set for the isInteractive property.
        """
        self._is_interactive = value
    
    @property
    def is_tenant_restricted(self,) -> Optional[bool]:
        """
        Gets the isTenantRestricted property value. Shows whether the sign in event was subject to an Azure AD tenant restriction policy.
        Returns: Optional[bool]
        """
        return self._is_tenant_restricted
    
    @is_tenant_restricted.setter
    def is_tenant_restricted(self,value: Optional[bool] = None) -> None:
        """
        Sets the isTenantRestricted property value. Shows whether the sign in event was subject to an Azure AD tenant restriction policy.
        Args:
            value: Value to set for the isTenantRestricted property.
        """
        self._is_tenant_restricted = value
    
    @property
    def location(self,) -> Optional[sign_in_location.SignInLocation]:
        """
        Gets the location property value. The city, state, and 2 letter country code from where the sign-in occurred. Supports $filter (eq and startsWith operators only) on city, state, and countryOrRegion properties.
        Returns: Optional[sign_in_location.SignInLocation]
        """
        return self._location
    
    @location.setter
    def location(self,value: Optional[sign_in_location.SignInLocation] = None) -> None:
        """
        Sets the location property value. The city, state, and 2 letter country code from where the sign-in occurred. Supports $filter (eq and startsWith operators only) on city, state, and countryOrRegion properties.
        Args:
            value: Value to set for the location property.
        """
        self._location = value
    
    @property
    def mfa_detail(self,) -> Optional[mfa_detail.MfaDetail]:
        """
        Gets the mfaDetail property value. The mfaDetail property
        Returns: Optional[mfa_detail.MfaDetail]
        """
        return self._mfa_detail
    
    @mfa_detail.setter
    def mfa_detail(self,value: Optional[mfa_detail.MfaDetail] = None) -> None:
        """
        Sets the mfaDetail property value. The mfaDetail property
        Args:
            value: Value to set for the mfaDetail property.
        """
        self._mfa_detail = value
    
    @property
    def network_location_details(self,) -> Optional[List[network_location_detail.NetworkLocationDetail]]:
        """
        Gets the networkLocationDetails property value. The network location details including the type of network used and its names.
        Returns: Optional[List[network_location_detail.NetworkLocationDetail]]
        """
        return self._network_location_details
    
    @network_location_details.setter
    def network_location_details(self,value: Optional[List[network_location_detail.NetworkLocationDetail]] = None) -> None:
        """
        Sets the networkLocationDetails property value. The network location details including the type of network used and its names.
        Args:
            value: Value to set for the networkLocationDetails property.
        """
        self._network_location_details = value
    
    @property
    def original_request_id(self,) -> Optional[str]:
        """
        Gets the originalRequestId property value. The request identifier of the first request in the authentication sequence. Supports $filter (eq operator only).
        Returns: Optional[str]
        """
        return self._original_request_id
    
    @original_request_id.setter
    def original_request_id(self,value: Optional[str] = None) -> None:
        """
        Sets the originalRequestId property value. The request identifier of the first request in the authentication sequence. Supports $filter (eq operator only).
        Args:
            value: Value to set for the originalRequestId property.
        """
        self._original_request_id = value
    
    @property
    def private_link_details(self,) -> Optional[private_link_details.PrivateLinkDetails]:
        """
        Gets the privateLinkDetails property value. Contains information about the Azure AD Private Link policy that is associated with the sign in event.
        Returns: Optional[private_link_details.PrivateLinkDetails]
        """
        return self._private_link_details
    
    @private_link_details.setter
    def private_link_details(self,value: Optional[private_link_details.PrivateLinkDetails] = None) -> None:
        """
        Sets the privateLinkDetails property value. Contains information about the Azure AD Private Link policy that is associated with the sign in event.
        Args:
            value: Value to set for the privateLinkDetails property.
        """
        self._private_link_details = value
    
    @property
    def processing_time_in_milliseconds(self,) -> Optional[int]:
        """
        Gets the processingTimeInMilliseconds property value. The request processing time in milliseconds in AD STS.
        Returns: Optional[int]
        """
        return self._processing_time_in_milliseconds
    
    @processing_time_in_milliseconds.setter
    def processing_time_in_milliseconds(self,value: Optional[int] = None) -> None:
        """
        Sets the processingTimeInMilliseconds property value. The request processing time in milliseconds in AD STS.
        Args:
            value: Value to set for the processingTimeInMilliseconds property.
        """
        self._processing_time_in_milliseconds = value
    
    @property
    def resource_display_name(self,) -> Optional[str]:
        """
        Gets the resourceDisplayName property value. The name of the resource that the user signed in to. Supports $filter (eq operator only).
        Returns: Optional[str]
        """
        return self._resource_display_name
    
    @resource_display_name.setter
    def resource_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the resourceDisplayName property value. The name of the resource that the user signed in to. Supports $filter (eq operator only).
        Args:
            value: Value to set for the resourceDisplayName property.
        """
        self._resource_display_name = value
    
    @property
    def resource_id(self,) -> Optional[str]:
        """
        Gets the resourceId property value. The identifier of the resource that the user signed in to. Supports $filter (eq operator only).
        Returns: Optional[str]
        """
        return self._resource_id
    
    @resource_id.setter
    def resource_id(self,value: Optional[str] = None) -> None:
        """
        Sets the resourceId property value. The identifier of the resource that the user signed in to. Supports $filter (eq operator only).
        Args:
            value: Value to set for the resourceId property.
        """
        self._resource_id = value
    
    @property
    def resource_service_principal_id(self,) -> Optional[str]:
        """
        Gets the resourceServicePrincipalId property value. The identifier of the service principal representing the target resource in the sign-in event.
        Returns: Optional[str]
        """
        return self._resource_service_principal_id
    
    @resource_service_principal_id.setter
    def resource_service_principal_id(self,value: Optional[str] = None) -> None:
        """
        Sets the resourceServicePrincipalId property value. The identifier of the service principal representing the target resource in the sign-in event.
        Args:
            value: Value to set for the resourceServicePrincipalId property.
        """
        self._resource_service_principal_id = value
    
    @property
    def resource_tenant_id(self,) -> Optional[str]:
        """
        Gets the resourceTenantId property value. The tenant identifier of the resource referenced in the sign in.
        Returns: Optional[str]
        """
        return self._resource_tenant_id
    
    @resource_tenant_id.setter
    def resource_tenant_id(self,value: Optional[str] = None) -> None:
        """
        Sets the resourceTenantId property value. The tenant identifier of the resource referenced in the sign in.
        Args:
            value: Value to set for the resourceTenantId property.
        """
        self._resource_tenant_id = value
    
    @property
    def risk_detail(self,) -> Optional[risk_detail.RiskDetail]:
        """
        Gets the riskDetail property value. The reason behind a specific state of a risky user, sign-in, or a risk event. Possible values: none, adminGeneratedTemporaryPassword, userPerformedSecuredPasswordChange, userPerformedSecuredPasswordReset, adminConfirmedSigninSafe, aiConfirmedSigninSafe, userPassedMFADrivenByRiskBasedPolicy, adminDismissedAllRiskForUser, adminConfirmedSigninCompromised, or unknownFutureValue. The value none means that no action has been performed on the user or sign-in so far. Supports $filter (eq operator only). Note: Details for this property are only available for Azure AD Premium P2 customers. All other customers are returned hidden.
        Returns: Optional[risk_detail.RiskDetail]
        """
        return self._risk_detail
    
    @risk_detail.setter
    def risk_detail(self,value: Optional[risk_detail.RiskDetail] = None) -> None:
        """
        Sets the riskDetail property value. The reason behind a specific state of a risky user, sign-in, or a risk event. Possible values: none, adminGeneratedTemporaryPassword, userPerformedSecuredPasswordChange, userPerformedSecuredPasswordReset, adminConfirmedSigninSafe, aiConfirmedSigninSafe, userPassedMFADrivenByRiskBasedPolicy, adminDismissedAllRiskForUser, adminConfirmedSigninCompromised, or unknownFutureValue. The value none means that no action has been performed on the user or sign-in so far. Supports $filter (eq operator only). Note: Details for this property are only available for Azure AD Premium P2 customers. All other customers are returned hidden.
        Args:
            value: Value to set for the riskDetail property.
        """
        self._risk_detail = value
    
    @property
    def risk_event_types_v2(self,) -> Optional[List[str]]:
        """
        Gets the riskEventTypes_v2 property value. The list of risk event types associated with the sign-in. Possible values: unlikelyTravel, anonymizedIPAddress, maliciousIPAddress, unfamiliarFeatures, malwareInfectedIPAddress, suspiciousIPAddress, leakedCredentials, investigationsThreatIntelligence,  generic, or unknownFutureValue. Supports $filter (eq and startsWith operators only).
        Returns: Optional[List[str]]
        """
        return self._risk_event_types_v2
    
    @risk_event_types_v2.setter
    def risk_event_types_v2(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the riskEventTypes_v2 property value. The list of risk event types associated with the sign-in. Possible values: unlikelyTravel, anonymizedIPAddress, maliciousIPAddress, unfamiliarFeatures, malwareInfectedIPAddress, suspiciousIPAddress, leakedCredentials, investigationsThreatIntelligence,  generic, or unknownFutureValue. Supports $filter (eq and startsWith operators only).
        Args:
            value: Value to set for the riskEventTypes_v2 property.
        """
        self._risk_event_types_v2 = value
    
    @property
    def risk_level_aggregated(self,) -> Optional[risk_level.RiskLevel]:
        """
        Gets the riskLevelAggregated property value. The aggregated risk level. Possible values: none, low, medium, high, hidden, or unknownFutureValue. The value hidden means the user or sign-in was not enabled for Azure AD Identity Protection. Supports $filter (eq operator only). Note: Details for this property are only available for Azure AD Premium P2 customers. All other customers are returned hidden.
        Returns: Optional[risk_level.RiskLevel]
        """
        return self._risk_level_aggregated
    
    @risk_level_aggregated.setter
    def risk_level_aggregated(self,value: Optional[risk_level.RiskLevel] = None) -> None:
        """
        Sets the riskLevelAggregated property value. The aggregated risk level. Possible values: none, low, medium, high, hidden, or unknownFutureValue. The value hidden means the user or sign-in was not enabled for Azure AD Identity Protection. Supports $filter (eq operator only). Note: Details for this property are only available for Azure AD Premium P2 customers. All other customers are returned hidden.
        Args:
            value: Value to set for the riskLevelAggregated property.
        """
        self._risk_level_aggregated = value
    
    @property
    def risk_level_during_sign_in(self,) -> Optional[risk_level.RiskLevel]:
        """
        Gets the riskLevelDuringSignIn property value. The risk level during sign-in. Possible values: none, low, medium, high, hidden, or unknownFutureValue. The value hidden means the user or sign-in was not enabled for Azure AD Identity Protection. Supports $filter (eq operator only). Note: Details for this property are only available for Azure AD Premium P2 customers. All other customers are returned hidden.
        Returns: Optional[risk_level.RiskLevel]
        """
        return self._risk_level_during_sign_in
    
    @risk_level_during_sign_in.setter
    def risk_level_during_sign_in(self,value: Optional[risk_level.RiskLevel] = None) -> None:
        """
        Sets the riskLevelDuringSignIn property value. The risk level during sign-in. Possible values: none, low, medium, high, hidden, or unknownFutureValue. The value hidden means the user or sign-in was not enabled for Azure AD Identity Protection. Supports $filter (eq operator only). Note: Details for this property are only available for Azure AD Premium P2 customers. All other customers are returned hidden.
        Args:
            value: Value to set for the riskLevelDuringSignIn property.
        """
        self._risk_level_during_sign_in = value
    
    @property
    def risk_state(self,) -> Optional[risk_state.RiskState]:
        """
        Gets the riskState property value. The risk state of a risky user, sign-in, or a risk event. Possible values: none, confirmedSafe, remediated, dismissed, atRisk, confirmedCompromised, or unknownFutureValue. Supports $filter (eq operator only).
        Returns: Optional[risk_state.RiskState]
        """
        return self._risk_state
    
    @risk_state.setter
    def risk_state(self,value: Optional[risk_state.RiskState] = None) -> None:
        """
        Sets the riskState property value. The risk state of a risky user, sign-in, or a risk event. Possible values: none, confirmedSafe, remediated, dismissed, atRisk, confirmedCompromised, or unknownFutureValue. Supports $filter (eq operator only).
        Args:
            value: Value to set for the riskState property.
        """
        self._risk_state = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("appDisplayName", self.app_display_name)
        writer.write_str_value("appId", self.app_id)
        writer.write_collection_of_object_values("appliedConditionalAccessPolicies", self.applied_conditional_access_policies)
        writer.write_collection_of_object_values("appliedEventListeners", self.applied_event_listeners)
        writer.write_object_value("authenticationAppDeviceDetails", self.authentication_app_device_details)
        writer.write_collection_of_object_values("authenticationAppPolicyEvaluationDetails", self.authentication_app_policy_evaluation_details)
        writer.write_collection_of_object_values("authenticationContextClassReferences", self.authentication_context_class_references)
        writer.write_collection_of_object_values("authenticationDetails", self.authentication_details)
        writer.write_collection_of_primitive_values("authenticationMethodsUsed", self.authentication_methods_used)
        writer.write_collection_of_object_values("authenticationProcessingDetails", self.authentication_processing_details)
        writer.write_enum_value("authenticationProtocol", self.authentication_protocol)
        writer.write_str_value("authenticationRequirement", self.authentication_requirement)
        writer.write_collection_of_object_values("authenticationRequirementPolicies", self.authentication_requirement_policies)
        writer.write_int_value("autonomousSystemNumber", self.autonomous_system_number)
        writer.write_str_value("azureResourceId", self.azure_resource_id)
        writer.write_str_value("clientAppUsed", self.client_app_used)
        writer.write_enum_value("clientCredentialType", self.client_credential_type)
        writer.write_enum_value("conditionalAccessStatus", self.conditional_access_status)
        writer.write_str_value("correlationId", self.correlation_id)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_enum_value("crossTenantAccessType", self.cross_tenant_access_type)
        writer.write_object_value("deviceDetail", self.device_detail)
        writer.write_str_value("federatedCredentialId", self.federated_credential_id)
        writer.write_bool_value("flaggedForReview", self.flagged_for_review)
        writer.write_str_value("homeTenantId", self.home_tenant_id)
        writer.write_str_value("homeTenantName", self.home_tenant_name)
        writer.write_enum_value("incomingTokenType", self.incoming_token_type)
        writer.write_str_value("ipAddress", self.ip_address)
        writer.write_str_value("ipAddressFromResourceProvider", self.ip_address_from_resource_provider)
        writer.write_bool_value("isInteractive", self.is_interactive)
        writer.write_bool_value("isTenantRestricted", self.is_tenant_restricted)
        writer.write_object_value("location", self.location)
        writer.write_object_value("mfaDetail", self.mfa_detail)
        writer.write_collection_of_object_values("networkLocationDetails", self.network_location_details)
        writer.write_str_value("originalRequestId", self.original_request_id)
        writer.write_object_value("privateLinkDetails", self.private_link_details)
        writer.write_int_value("processingTimeInMilliseconds", self.processing_time_in_milliseconds)
        writer.write_str_value("resourceDisplayName", self.resource_display_name)
        writer.write_str_value("resourceId", self.resource_id)
        writer.write_str_value("resourceServicePrincipalId", self.resource_service_principal_id)
        writer.write_str_value("resourceTenantId", self.resource_tenant_id)
        writer.write_enum_value("riskDetail", self.risk_detail)
        writer.write_collection_of_primitive_values("riskEventTypes_v2", self.risk_event_types_v2)
        writer.write_enum_value("riskLevelAggregated", self.risk_level_aggregated)
        writer.write_enum_value("riskLevelDuringSignIn", self.risk_level_during_sign_in)
        writer.write_enum_value("riskState", self.risk_state)
        writer.write_str_value("servicePrincipalCredentialKeyId", self.service_principal_credential_key_id)
        writer.write_str_value("servicePrincipalCredentialThumbprint", self.service_principal_credential_thumbprint)
        writer.write_str_value("servicePrincipalId", self.service_principal_id)
        writer.write_str_value("servicePrincipalName", self.service_principal_name)
        writer.write_collection_of_object_values("sessionLifetimePolicies", self.session_lifetime_policies)
        writer.write_collection_of_primitive_values("signInEventTypes", self.sign_in_event_types)
        writer.write_str_value("signInIdentifier", self.sign_in_identifier)
        writer.write_enum_value("signInIdentifierType", self.sign_in_identifier_type)
        writer.write_object_value("status", self.status)
        writer.write_str_value("tokenIssuerName", self.token_issuer_name)
        writer.write_enum_value("tokenIssuerType", self.token_issuer_type)
        writer.write_str_value("uniqueTokenIdentifier", self.unique_token_identifier)
        writer.write_str_value("userAgent", self.user_agent)
        writer.write_str_value("userDisplayName", self.user_display_name)
        writer.write_str_value("userId", self.user_id)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
        writer.write_enum_value("userType", self.user_type)
    
    @property
    def service_principal_credential_key_id(self,) -> Optional[str]:
        """
        Gets the servicePrincipalCredentialKeyId property value. The unique identifier of the key credential used by the service principal to authenticate.
        Returns: Optional[str]
        """
        return self._service_principal_credential_key_id
    
    @service_principal_credential_key_id.setter
    def service_principal_credential_key_id(self,value: Optional[str] = None) -> None:
        """
        Sets the servicePrincipalCredentialKeyId property value. The unique identifier of the key credential used by the service principal to authenticate.
        Args:
            value: Value to set for the servicePrincipalCredentialKeyId property.
        """
        self._service_principal_credential_key_id = value
    
    @property
    def service_principal_credential_thumbprint(self,) -> Optional[str]:
        """
        Gets the servicePrincipalCredentialThumbprint property value. The certificate thumbprint of the certificate used by the service principal to authenticate.
        Returns: Optional[str]
        """
        return self._service_principal_credential_thumbprint
    
    @service_principal_credential_thumbprint.setter
    def service_principal_credential_thumbprint(self,value: Optional[str] = None) -> None:
        """
        Sets the servicePrincipalCredentialThumbprint property value. The certificate thumbprint of the certificate used by the service principal to authenticate.
        Args:
            value: Value to set for the servicePrincipalCredentialThumbprint property.
        """
        self._service_principal_credential_thumbprint = value
    
    @property
    def service_principal_id(self,) -> Optional[str]:
        """
        Gets the servicePrincipalId property value. The application identifier used for sign-in. This field is populated when you are signing in using an application. Supports $filter (eq and startsWith operators only).
        Returns: Optional[str]
        """
        return self._service_principal_id
    
    @service_principal_id.setter
    def service_principal_id(self,value: Optional[str] = None) -> None:
        """
        Sets the servicePrincipalId property value. The application identifier used for sign-in. This field is populated when you are signing in using an application. Supports $filter (eq and startsWith operators only).
        Args:
            value: Value to set for the servicePrincipalId property.
        """
        self._service_principal_id = value
    
    @property
    def service_principal_name(self,) -> Optional[str]:
        """
        Gets the servicePrincipalName property value. The application name used for sign-in. This field is populated when you are signing in using an application. Supports $filter (eq and startsWith operators only).
        Returns: Optional[str]
        """
        return self._service_principal_name
    
    @service_principal_name.setter
    def service_principal_name(self,value: Optional[str] = None) -> None:
        """
        Sets the servicePrincipalName property value. The application name used for sign-in. This field is populated when you are signing in using an application. Supports $filter (eq and startsWith operators only).
        Args:
            value: Value to set for the servicePrincipalName property.
        """
        self._service_principal_name = value
    
    @property
    def session_lifetime_policies(self,) -> Optional[List[session_lifetime_policy.SessionLifetimePolicy]]:
        """
        Gets the sessionLifetimePolicies property value. Any conditional access session management policies that were applied during the sign-in event.
        Returns: Optional[List[session_lifetime_policy.SessionLifetimePolicy]]
        """
        return self._session_lifetime_policies
    
    @session_lifetime_policies.setter
    def session_lifetime_policies(self,value: Optional[List[session_lifetime_policy.SessionLifetimePolicy]] = None) -> None:
        """
        Sets the sessionLifetimePolicies property value. Any conditional access session management policies that were applied during the sign-in event.
        Args:
            value: Value to set for the sessionLifetimePolicies property.
        """
        self._session_lifetime_policies = value
    
    @property
    def sign_in_event_types(self,) -> Optional[List[str]]:
        """
        Gets the signInEventTypes property value. Indicates the category of sign in that the event represents. For user sign ins, the category can be interactiveUser or nonInteractiveUser and corresponds to the value for the isInteractive property on the signin resource. For managed identity sign ins, the category is managedIdentity. For service principal sign ins, the category is servicePrincipal. Possible values are: interactiveUser, nonInteractiveUser, servicePrincipal, managedIdentity, unknownFutureValue. Supports $filter (eq, ne).
        Returns: Optional[List[str]]
        """
        return self._sign_in_event_types
    
    @sign_in_event_types.setter
    def sign_in_event_types(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the signInEventTypes property value. Indicates the category of sign in that the event represents. For user sign ins, the category can be interactiveUser or nonInteractiveUser and corresponds to the value for the isInteractive property on the signin resource. For managed identity sign ins, the category is managedIdentity. For service principal sign ins, the category is servicePrincipal. Possible values are: interactiveUser, nonInteractiveUser, servicePrincipal, managedIdentity, unknownFutureValue. Supports $filter (eq, ne).
        Args:
            value: Value to set for the signInEventTypes property.
        """
        self._sign_in_event_types = value
    
    @property
    def sign_in_identifier(self,) -> Optional[str]:
        """
        Gets the signInIdentifier property value. The identification that the user provided to sign in. It may be the userPrincipalName but it's also populated when a user signs in using other identifiers.
        Returns: Optional[str]
        """
        return self._sign_in_identifier
    
    @sign_in_identifier.setter
    def sign_in_identifier(self,value: Optional[str] = None) -> None:
        """
        Sets the signInIdentifier property value. The identification that the user provided to sign in. It may be the userPrincipalName but it's also populated when a user signs in using other identifiers.
        Args:
            value: Value to set for the signInIdentifier property.
        """
        self._sign_in_identifier = value
    
    @property
    def sign_in_identifier_type(self,) -> Optional[sign_in_identifier_type.SignInIdentifierType]:
        """
        Gets the signInIdentifierType property value. The type of sign in identifier. Possible values are: userPrincipalName, phoneNumber, proxyAddress, qrCode, onPremisesUserPrincipalName, unknownFutureValue.
        Returns: Optional[sign_in_identifier_type.SignInIdentifierType]
        """
        return self._sign_in_identifier_type
    
    @sign_in_identifier_type.setter
    def sign_in_identifier_type(self,value: Optional[sign_in_identifier_type.SignInIdentifierType] = None) -> None:
        """
        Sets the signInIdentifierType property value. The type of sign in identifier. Possible values are: userPrincipalName, phoneNumber, proxyAddress, qrCode, onPremisesUserPrincipalName, unknownFutureValue.
        Args:
            value: Value to set for the signInIdentifierType property.
        """
        self._sign_in_identifier_type = value
    
    @property
    def status(self,) -> Optional[sign_in_status.SignInStatus]:
        """
        Gets the status property value. The sign-in status. Includes the error code and description of the error (in case of a sign-in failure). Supports $filter (eq operator only) on errorCode property.
        Returns: Optional[sign_in_status.SignInStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[sign_in_status.SignInStatus] = None) -> None:
        """
        Sets the status property value. The sign-in status. Includes the error code and description of the error (in case of a sign-in failure). Supports $filter (eq operator only) on errorCode property.
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    
    @property
    def token_issuer_name(self,) -> Optional[str]:
        """
        Gets the tokenIssuerName property value. The name of the identity provider. For example, sts.microsoft.com. Supports $filter (eq operator only).
        Returns: Optional[str]
        """
        return self._token_issuer_name
    
    @token_issuer_name.setter
    def token_issuer_name(self,value: Optional[str] = None) -> None:
        """
        Sets the tokenIssuerName property value. The name of the identity provider. For example, sts.microsoft.com. Supports $filter (eq operator only).
        Args:
            value: Value to set for the tokenIssuerName property.
        """
        self._token_issuer_name = value
    
    @property
    def token_issuer_type(self,) -> Optional[token_issuer_type.TokenIssuerType]:
        """
        Gets the tokenIssuerType property value. The type of identity provider. The possible values are: AzureAD, ADFederationServices, UnknownFutureValue, AzureADBackupAuth, ADFederationServicesMFAAdapter, NPSExtension. Note that you must use the Prefer: include-unknown-enum-members request header to get the following values in this evolvable enum: AzureADBackupAuth , ADFederationServicesMFAAdapter , NPSExtension.
        Returns: Optional[token_issuer_type.TokenIssuerType]
        """
        return self._token_issuer_type
    
    @token_issuer_type.setter
    def token_issuer_type(self,value: Optional[token_issuer_type.TokenIssuerType] = None) -> None:
        """
        Sets the tokenIssuerType property value. The type of identity provider. The possible values are: AzureAD, ADFederationServices, UnknownFutureValue, AzureADBackupAuth, ADFederationServicesMFAAdapter, NPSExtension. Note that you must use the Prefer: include-unknown-enum-members request header to get the following values in this evolvable enum: AzureADBackupAuth , ADFederationServicesMFAAdapter , NPSExtension.
        Args:
            value: Value to set for the tokenIssuerType property.
        """
        self._token_issuer_type = value
    
    @property
    def unique_token_identifier(self,) -> Optional[str]:
        """
        Gets the uniqueTokenIdentifier property value. A unique base64 encoded request identifier used to track tokens issued by Azure AD as they are redeemed at resource providers.
        Returns: Optional[str]
        """
        return self._unique_token_identifier
    
    @unique_token_identifier.setter
    def unique_token_identifier(self,value: Optional[str] = None) -> None:
        """
        Sets the uniqueTokenIdentifier property value. A unique base64 encoded request identifier used to track tokens issued by Azure AD as they are redeemed at resource providers.
        Args:
            value: Value to set for the uniqueTokenIdentifier property.
        """
        self._unique_token_identifier = value
    
    @property
    def user_agent(self,) -> Optional[str]:
        """
        Gets the userAgent property value. The user agent information related to sign-in. Supports $filter (eq and startsWith operators only).
        Returns: Optional[str]
        """
        return self._user_agent
    
    @user_agent.setter
    def user_agent(self,value: Optional[str] = None) -> None:
        """
        Sets the userAgent property value. The user agent information related to sign-in. Supports $filter (eq and startsWith operators only).
        Args:
            value: Value to set for the userAgent property.
        """
        self._user_agent = value
    
    @property
    def user_display_name(self,) -> Optional[str]:
        """
        Gets the userDisplayName property value. The display name of the user. Supports $filter (eq and startsWith operators only).
        Returns: Optional[str]
        """
        return self._user_display_name
    
    @user_display_name.setter
    def user_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userDisplayName property value. The display name of the user. Supports $filter (eq and startsWith operators only).
        Args:
            value: Value to set for the userDisplayName property.
        """
        self._user_display_name = value
    
    @property
    def user_id(self,) -> Optional[str]:
        """
        Gets the userId property value. The identifier of the user. Supports $filter (eq operator only).
        Returns: Optional[str]
        """
        return self._user_id
    
    @user_id.setter
    def user_id(self,value: Optional[str] = None) -> None:
        """
        Sets the userId property value. The identifier of the user. Supports $filter (eq operator only).
        Args:
            value: Value to set for the userId property.
        """
        self._user_id = value
    
    @property
    def user_principal_name(self,) -> Optional[str]:
        """
        Gets the userPrincipalName property value. The UPN of the user. Supports $filter (eq and startsWith operators only).
        Returns: Optional[str]
        """
        return self._user_principal_name
    
    @user_principal_name.setter
    def user_principal_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userPrincipalName property value. The UPN of the user. Supports $filter (eq and startsWith operators only).
        Args:
            value: Value to set for the userPrincipalName property.
        """
        self._user_principal_name = value
    
    @property
    def user_type(self,) -> Optional[sign_in_user_type.SignInUserType]:
        """
        Gets the userType property value. Identifies whether the user is a member or guest in the tenant. Possible values are: member, guest, unknownFutureValue.
        Returns: Optional[sign_in_user_type.SignInUserType]
        """
        return self._user_type
    
    @user_type.setter
    def user_type(self,value: Optional[sign_in_user_type.SignInUserType] = None) -> None:
        """
        Sets the userType property value. Identifies whether the user is a member or guest in the tenant. Possible values are: member, guest, unknownFutureValue.
        Args:
            value: Value to set for the userType property.
        """
        self._user_type = value
    

