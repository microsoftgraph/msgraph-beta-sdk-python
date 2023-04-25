from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from . import api_application, app_management_policy, app_role, certification, connector_group, directory_object, extension_property, federated_identity_credential, home_realm_discovery_policy, informational_url, key_credential, on_premises_publishing, optional_claims, parental_control_settings, password_credential, public_client_application, request_signature_verification, required_resource_access, service_principal_lock_configuration, spa_application, synchronization, token_issuance_policy, token_lifetime_policy, verified_publisher, web_application, windows_application

from . import directory_object

class Application(directory_object.DirectoryObject):
    def __init__(self,) -> None:
        """
        Instantiates a new Application and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.application"
        # Specifies settings for an application that implements a web API.
        self._api: Optional[api_application.ApiApplication] = None
        # The unique identifier for the application that is assigned by Azure AD. Not nullable. Read-only. Supports $filter (eq).
        self._app_id: Optional[str] = None
        # The appManagementPolicy applied to this application.
        self._app_management_policies: Optional[List[app_management_policy.AppManagementPolicy]] = None
        # The collection of roles defined for the application. With app role assignments, these roles can be assigned to users, groups, or service principals associated with other applications. Not nullable.
        self._app_roles: Optional[List[app_role.AppRole]] = None
        # Specifies the certification status of the application.
        self._certification: Optional[certification.Certification] = None
        # The connectorGroup the application is using with Azure AD Application Proxy. Nullable.
        self._connector_group: Optional[connector_group.ConnectorGroup] = None
        # The date and time the application was registered. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.  Supports $filter (eq, ne, not, ge, le, in, and eq on null values) and $orderBy.
        self._created_date_time: Optional[datetime] = None
        # Supports $filter (/$count eq 0, /$count ne 0). Read-only.
        self._created_on_behalf_of: Optional[directory_object.DirectoryObject] = None
        # The default redirect URI. If specified and there is no explicit redirect URI in the sign-in request for SAML and OIDC flows, Azure AD sends the token to this redirect URI. Azure AD also sends the token to this default URI in SAML IdP-initiated single sign-on. The value must match one of the configured redirect URIs for the application.
        self._default_redirect_uri: Optional[str] = None
        # Free text field to provide a description of the application object to end users. The maximum allowed size is 1024 characters. Returned by default. Supports $filter (eq, ne, not, ge, le, startsWith) and $search.
        self._description: Optional[str] = None
        # Specifies whether Microsoft has disabled the registered application. Possible values are: null (default value), NotDisabled, and DisabledDueToViolationOfServicesAgreement (reasons may include suspicious, abusive, or malicious activity, or a violation of the Microsoft Services Agreement).  Supports $filter (eq, ne, not).
        self._disabled_by_microsoft_status: Optional[str] = None
        # The display name for the application. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values), $search, and $orderBy.
        self._display_name: Optional[str] = None
        # Read-only. Nullable. Supports $expand and $filter (/$count eq 0, /$count ne 0).
        self._extension_properties: Optional[List[extension_property.ExtensionProperty]] = None
        # Federated identities for applications. Supports $expand and $filter (startsWith, /$count eq 0, /$count ne 0).
        self._federated_identity_credentials: Optional[List[federated_identity_credential.FederatedIdentityCredential]] = None
        # Configures the groups claim issued in a user or OAuth 2.0 access token that the application expects. To set this attribute, use one of the following string values: None, SecurityGroup (for security groups and Azure AD roles), All (this gets all security groups, distribution groups, and Azure AD directory roles that the signed-in user is a member of).
        self._group_membership_claims: Optional[str] = None
        # The homeRealmDiscoveryPolicies property
        self._home_realm_discovery_policies: Optional[List[home_realm_discovery_policy.HomeRealmDiscoveryPolicy]] = None
        # Also known as App ID URI, this value is set when an application is used as a resource app. The identifierUris acts as the prefix for the scopes you'll reference in your API's code, and it must be globally unique. You can use the default value provided, which is in the form api://<application-client-id>, or specify a more readable URI like https://contoso.com/api. For more information on valid identifierUris patterns and best practices, see Azure AD application registration security best practices. Not nullable. Supports $filter (eq, ne, ge, le, startsWith).
        self._identifier_uris: Optional[List[str]] = None
        # Basic profile information of the application, such as it's marketing, support, terms of service, and privacy statement URLs. The terms of service and privacy statement are surfaced to users through the user consent experience. For more information, see How to: Add Terms of service and privacy statement for registered Azure AD apps. Supports $filter (eq, ne, not, ge, le, and eq on null values).
        self._info: Optional[informational_url.InformationalUrl] = None
        # Specifies whether this application supports device authentication without a user. The default is false.
        self._is_device_only_auth_supported: Optional[bool] = None
        # Specifies the fallback application type as public client, such as an installed application running on a mobile device. The default value is false which means the fallback application type is confidential client such as a web app. There are certain scenarios where Azure AD cannot determine the client application type. For example, the ROPC flow where the application is configured without specifying a redirect URI. In those cases Azure AD interprets the application type based on the value of this property.
        self._is_fallback_public_client: Optional[bool] = None
        # The collection of key credentials associated with the application. Not nullable. Supports $filter (eq, not, ge, le).
        self._key_credentials: Optional[List[key_credential.KeyCredential]] = None
        # The main logo for the application. Not nullable.
        self._logo: Optional[bytes] = None
        # Notes relevant for the management of the application.
        self._notes: Optional[str] = None
        # Represents the set of properties required for configuring Application Proxy for this application. Configuring these properties allows you to publish your on-premises application for secure remote access.
        self._on_premises_publishing: Optional[on_premises_publishing.OnPremisesPublishing] = None
        # Application developers can configure optional claims in their Azure AD applications to specify the claims that are sent to their application by the Microsoft security token service. For more information, see How to: Provide optional claims to your app.
        self._optional_claims: Optional[optional_claims.OptionalClaims] = None
        # Directory objects that are owners of the application. Read-only. Nullable. Supports $expand and $filter (/$count eq 0, /$count ne 0, /$count eq 1, /$count ne 1).
        self._owners: Optional[List[directory_object.DirectoryObject]] = None
        # Specifies parental control settings for an application.
        self._parental_control_settings: Optional[parental_control_settings.ParentalControlSettings] = None
        # The collection of password credentials associated with the application. Not nullable.
        self._password_credentials: Optional[List[password_credential.PasswordCredential]] = None
        # Specifies settings for installed clients such as desktop or mobile devices.
        self._public_client: Optional[public_client_application.PublicClientApplication] = None
        # The verified publisher domain for the application. Read-only. Supports $filter (eq, ne, ge, le, startsWith).
        self._publisher_domain: Optional[str] = None
        # Specifies whether this application requires Azure AD to verify the signed authentication requests.
        self._request_signature_verification: Optional[request_signature_verification.RequestSignatureVerification] = None
        # Specifies the resources that the application needs to access. This property also specifies the set of delegated permissions and application roles that it needs for each of those resources. This configuration of access to the required resources drives the consent experience. No more than 50 resource services (APIs) can be configured. Beginning mid-October 2021, the total number of required permissions must not exceed 400. For more information, see Limits on requested permissions per app. Not nullable. Supports $filter (eq, not, ge, le).
        self._required_resource_access: Optional[List[required_resource_access.RequiredResourceAccess]] = None
        # The URL where the service exposes SAML metadata for federation. This property is valid only for single-tenant applications. Nullable.
        self._saml_metadata_url: Optional[str] = None
        # References application or service contact information from a Service or Asset Management database. Nullable.
        self._service_management_reference: Optional[str] = None
        # Specifies whether sensitive properties of a multi-tenant application should be locked for editing after the application is provisioned in a tenant. Nullable. null by default.
        self._service_principal_lock_configuration: Optional[service_principal_lock_configuration.ServicePrincipalLockConfiguration] = None
        # Specifies the Microsoft accounts that are supported for the current application. The possible values are: AzureADMyOrg, AzureADMultipleOrgs, AzureADandPersonalMicrosoftAccount (default), and PersonalMicrosoftAccount. See more in the table. The value of this object also limits the number of permissions an app can request. For more information, see Limits on requested permissions per app. The value for this property has implications on other app object properties. As a result, if you change this property, you may need to change other properties first. For more information, see Validation differences for signInAudience.Supports $filter (eq, ne, not).
        self._sign_in_audience: Optional[str] = None
        # Specifies settings for a single-page application, including sign out URLs and redirect URIs for authorization codes and access tokens.
        self._spa: Optional[spa_application.SpaApplication] = None
        # Represents the capability for Azure Active Directory (Azure AD) identity synchronization through the Microsoft Graph API.
        self._synchronization: Optional[synchronization.Synchronization] = None
        # Custom strings that can be used to categorize and identify the application. Not nullable. Strings added here will also appear in the tags property of any associated service principals.Supports $filter (eq, not, ge, le, startsWith) and $search.
        self._tags: Optional[List[str]] = None
        # Specifies the keyId of a public key from the keyCredentials collection. When configured, Azure AD encrypts all the tokens it emits by using the key this property points to. The application code that receives the encrypted token must use the matching private key to decrypt the token before it can be used for the signed-in user.
        self._token_encryption_key_id: Optional[UUID] = None
        # The tokenIssuancePolicies property
        self._token_issuance_policies: Optional[List[token_issuance_policy.TokenIssuancePolicy]] = None
        # The tokenLifetimePolicies assigned to this application. Supports $expand.
        self._token_lifetime_policies: Optional[List[token_lifetime_policy.TokenLifetimePolicy]] = None
        # The unique identifier that can be assigned to an application as an alternative identifier. Immutable. Read-only.
        self._unique_name: Optional[str] = None
        # Specifies the verified publisher of the application. For more information about how publisher verification helps support application security, trustworthiness, and compliance, see Publisher verification.
        self._verified_publisher: Optional[verified_publisher.VerifiedPublisher] = None
        # Specifies settings for a web application.
        self._web: Optional[web_application.WebApplication] = None
        # Specifies settings for apps running Microsoft Windows and published in the Microsoft Store or Xbox games store.
        self._windows: Optional[windows_application.WindowsApplication] = None
    
    @property
    def api(self,) -> Optional[api_application.ApiApplication]:
        """
        Gets the api property value. Specifies settings for an application that implements a web API.
        Returns: Optional[api_application.ApiApplication]
        """
        return self._api
    
    @api.setter
    def api(self,value: Optional[api_application.ApiApplication] = None) -> None:
        """
        Sets the api property value. Specifies settings for an application that implements a web API.
        Args:
            value: Value to set for the api property.
        """
        self._api = value
    
    @property
    def app_id(self,) -> Optional[str]:
        """
        Gets the appId property value. The unique identifier for the application that is assigned by Azure AD. Not nullable. Read-only. Supports $filter (eq).
        Returns: Optional[str]
        """
        return self._app_id
    
    @app_id.setter
    def app_id(self,value: Optional[str] = None) -> None:
        """
        Sets the appId property value. The unique identifier for the application that is assigned by Azure AD. Not nullable. Read-only. Supports $filter (eq).
        Args:
            value: Value to set for the app_id property.
        """
        self._app_id = value
    
    @property
    def app_management_policies(self,) -> Optional[List[app_management_policy.AppManagementPolicy]]:
        """
        Gets the appManagementPolicies property value. The appManagementPolicy applied to this application.
        Returns: Optional[List[app_management_policy.AppManagementPolicy]]
        """
        return self._app_management_policies
    
    @app_management_policies.setter
    def app_management_policies(self,value: Optional[List[app_management_policy.AppManagementPolicy]] = None) -> None:
        """
        Sets the appManagementPolicies property value. The appManagementPolicy applied to this application.
        Args:
            value: Value to set for the app_management_policies property.
        """
        self._app_management_policies = value
    
    @property
    def app_roles(self,) -> Optional[List[app_role.AppRole]]:
        """
        Gets the appRoles property value. The collection of roles defined for the application. With app role assignments, these roles can be assigned to users, groups, or service principals associated with other applications. Not nullable.
        Returns: Optional[List[app_role.AppRole]]
        """
        return self._app_roles
    
    @app_roles.setter
    def app_roles(self,value: Optional[List[app_role.AppRole]] = None) -> None:
        """
        Sets the appRoles property value. The collection of roles defined for the application. With app role assignments, these roles can be assigned to users, groups, or service principals associated with other applications. Not nullable.
        Args:
            value: Value to set for the app_roles property.
        """
        self._app_roles = value
    
    @property
    def certification(self,) -> Optional[certification.Certification]:
        """
        Gets the certification property value. Specifies the certification status of the application.
        Returns: Optional[certification.Certification]
        """
        return self._certification
    
    @certification.setter
    def certification(self,value: Optional[certification.Certification] = None) -> None:
        """
        Sets the certification property value. Specifies the certification status of the application.
        Args:
            value: Value to set for the certification property.
        """
        self._certification = value
    
    @property
    def connector_group(self,) -> Optional[connector_group.ConnectorGroup]:
        """
        Gets the connectorGroup property value. The connectorGroup the application is using with Azure AD Application Proxy. Nullable.
        Returns: Optional[connector_group.ConnectorGroup]
        """
        return self._connector_group
    
    @connector_group.setter
    def connector_group(self,value: Optional[connector_group.ConnectorGroup] = None) -> None:
        """
        Sets the connectorGroup property value. The connectorGroup the application is using with Azure AD Application Proxy. Nullable.
        Args:
            value: Value to set for the connector_group property.
        """
        self._connector_group = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The date and time the application was registered. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.  Supports $filter (eq, ne, not, ge, le, in, and eq on null values) and $orderBy.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The date and time the application was registered. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.  Supports $filter (eq, ne, not, ge, le, in, and eq on null values) and $orderBy.
        Args:
            value: Value to set for the created_date_time property.
        """
        self._created_date_time = value
    
    @property
    def created_on_behalf_of(self,) -> Optional[directory_object.DirectoryObject]:
        """
        Gets the createdOnBehalfOf property value. Supports $filter (/$count eq 0, /$count ne 0). Read-only.
        Returns: Optional[directory_object.DirectoryObject]
        """
        return self._created_on_behalf_of
    
    @created_on_behalf_of.setter
    def created_on_behalf_of(self,value: Optional[directory_object.DirectoryObject] = None) -> None:
        """
        Sets the createdOnBehalfOf property value. Supports $filter (/$count eq 0, /$count ne 0). Read-only.
        Args:
            value: Value to set for the created_on_behalf_of property.
        """
        self._created_on_behalf_of = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Application:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Application
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Application()
    
    @property
    def default_redirect_uri(self,) -> Optional[str]:
        """
        Gets the defaultRedirectUri property value. The default redirect URI. If specified and there is no explicit redirect URI in the sign-in request for SAML and OIDC flows, Azure AD sends the token to this redirect URI. Azure AD also sends the token to this default URI in SAML IdP-initiated single sign-on. The value must match one of the configured redirect URIs for the application.
        Returns: Optional[str]
        """
        return self._default_redirect_uri
    
    @default_redirect_uri.setter
    def default_redirect_uri(self,value: Optional[str] = None) -> None:
        """
        Sets the defaultRedirectUri property value. The default redirect URI. If specified and there is no explicit redirect URI in the sign-in request for SAML and OIDC flows, Azure AD sends the token to this redirect URI. Azure AD also sends the token to this default URI in SAML IdP-initiated single sign-on. The value must match one of the configured redirect URIs for the application.
        Args:
            value: Value to set for the default_redirect_uri property.
        """
        self._default_redirect_uri = value
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. Free text field to provide a description of the application object to end users. The maximum allowed size is 1024 characters. Returned by default. Supports $filter (eq, ne, not, ge, le, startsWith) and $search.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. Free text field to provide a description of the application object to end users. The maximum allowed size is 1024 characters. Returned by default. Supports $filter (eq, ne, not, ge, le, startsWith) and $search.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def disabled_by_microsoft_status(self,) -> Optional[str]:
        """
        Gets the disabledByMicrosoftStatus property value. Specifies whether Microsoft has disabled the registered application. Possible values are: null (default value), NotDisabled, and DisabledDueToViolationOfServicesAgreement (reasons may include suspicious, abusive, or malicious activity, or a violation of the Microsoft Services Agreement).  Supports $filter (eq, ne, not).
        Returns: Optional[str]
        """
        return self._disabled_by_microsoft_status
    
    @disabled_by_microsoft_status.setter
    def disabled_by_microsoft_status(self,value: Optional[str] = None) -> None:
        """
        Sets the disabledByMicrosoftStatus property value. Specifies whether Microsoft has disabled the registered application. Possible values are: null (default value), NotDisabled, and DisabledDueToViolationOfServicesAgreement (reasons may include suspicious, abusive, or malicious activity, or a violation of the Microsoft Services Agreement).  Supports $filter (eq, ne, not).
        Args:
            value: Value to set for the disabled_by_microsoft_status property.
        """
        self._disabled_by_microsoft_status = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The display name for the application. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values), $search, and $orderBy.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display name for the application. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values), $search, and $orderBy.
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    @property
    def extension_properties(self,) -> Optional[List[extension_property.ExtensionProperty]]:
        """
        Gets the extensionProperties property value. Read-only. Nullable. Supports $expand and $filter (/$count eq 0, /$count ne 0).
        Returns: Optional[List[extension_property.ExtensionProperty]]
        """
        return self._extension_properties
    
    @extension_properties.setter
    def extension_properties(self,value: Optional[List[extension_property.ExtensionProperty]] = None) -> None:
        """
        Sets the extensionProperties property value. Read-only. Nullable. Supports $expand and $filter (/$count eq 0, /$count ne 0).
        Args:
            value: Value to set for the extension_properties property.
        """
        self._extension_properties = value
    
    @property
    def federated_identity_credentials(self,) -> Optional[List[federated_identity_credential.FederatedIdentityCredential]]:
        """
        Gets the federatedIdentityCredentials property value. Federated identities for applications. Supports $expand and $filter (startsWith, /$count eq 0, /$count ne 0).
        Returns: Optional[List[federated_identity_credential.FederatedIdentityCredential]]
        """
        return self._federated_identity_credentials
    
    @federated_identity_credentials.setter
    def federated_identity_credentials(self,value: Optional[List[federated_identity_credential.FederatedIdentityCredential]] = None) -> None:
        """
        Sets the federatedIdentityCredentials property value. Federated identities for applications. Supports $expand and $filter (startsWith, /$count eq 0, /$count ne 0).
        Args:
            value: Value to set for the federated_identity_credentials property.
        """
        self._federated_identity_credentials = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import api_application, app_management_policy, app_role, certification, connector_group, directory_object, extension_property, federated_identity_credential, home_realm_discovery_policy, informational_url, key_credential, on_premises_publishing, optional_claims, parental_control_settings, password_credential, public_client_application, request_signature_verification, required_resource_access, service_principal_lock_configuration, spa_application, synchronization, token_issuance_policy, token_lifetime_policy, verified_publisher, web_application, windows_application

        fields: Dict[str, Callable[[Any], None]] = {
            "api": lambda n : setattr(self, 'api', n.get_object_value(api_application.ApiApplication)),
            "appId": lambda n : setattr(self, 'app_id', n.get_str_value()),
            "appManagementPolicies": lambda n : setattr(self, 'app_management_policies', n.get_collection_of_object_values(app_management_policy.AppManagementPolicy)),
            "appRoles": lambda n : setattr(self, 'app_roles', n.get_collection_of_object_values(app_role.AppRole)),
            "certification": lambda n : setattr(self, 'certification', n.get_object_value(certification.Certification)),
            "connectorGroup": lambda n : setattr(self, 'connector_group', n.get_object_value(connector_group.ConnectorGroup)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "createdOnBehalfOf": lambda n : setattr(self, 'created_on_behalf_of', n.get_object_value(directory_object.DirectoryObject)),
            "defaultRedirectUri": lambda n : setattr(self, 'default_redirect_uri', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "disabledByMicrosoftStatus": lambda n : setattr(self, 'disabled_by_microsoft_status', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "extensionProperties": lambda n : setattr(self, 'extension_properties', n.get_collection_of_object_values(extension_property.ExtensionProperty)),
            "federatedIdentityCredentials": lambda n : setattr(self, 'federated_identity_credentials', n.get_collection_of_object_values(federated_identity_credential.FederatedIdentityCredential)),
            "groupMembershipClaims": lambda n : setattr(self, 'group_membership_claims', n.get_str_value()),
            "homeRealmDiscoveryPolicies": lambda n : setattr(self, 'home_realm_discovery_policies', n.get_collection_of_object_values(home_realm_discovery_policy.HomeRealmDiscoveryPolicy)),
            "identifierUris": lambda n : setattr(self, 'identifier_uris', n.get_collection_of_primitive_values(str)),
            "info": lambda n : setattr(self, 'info', n.get_object_value(informational_url.InformationalUrl)),
            "isDeviceOnlyAuthSupported": lambda n : setattr(self, 'is_device_only_auth_supported', n.get_bool_value()),
            "isFallbackPublicClient": lambda n : setattr(self, 'is_fallback_public_client', n.get_bool_value()),
            "keyCredentials": lambda n : setattr(self, 'key_credentials', n.get_collection_of_object_values(key_credential.KeyCredential)),
            "logo": lambda n : setattr(self, 'logo', n.get_bytes_value()),
            "notes": lambda n : setattr(self, 'notes', n.get_str_value()),
            "onPremisesPublishing": lambda n : setattr(self, 'on_premises_publishing', n.get_object_value(on_premises_publishing.OnPremisesPublishing)),
            "optionalClaims": lambda n : setattr(self, 'optional_claims', n.get_object_value(optional_claims.OptionalClaims)),
            "owners": lambda n : setattr(self, 'owners', n.get_collection_of_object_values(directory_object.DirectoryObject)),
            "parentalControlSettings": lambda n : setattr(self, 'parental_control_settings', n.get_object_value(parental_control_settings.ParentalControlSettings)),
            "passwordCredentials": lambda n : setattr(self, 'password_credentials', n.get_collection_of_object_values(password_credential.PasswordCredential)),
            "publicClient": lambda n : setattr(self, 'public_client', n.get_object_value(public_client_application.PublicClientApplication)),
            "publisherDomain": lambda n : setattr(self, 'publisher_domain', n.get_str_value()),
            "requestSignatureVerification": lambda n : setattr(self, 'request_signature_verification', n.get_object_value(request_signature_verification.RequestSignatureVerification)),
            "requiredResourceAccess": lambda n : setattr(self, 'required_resource_access', n.get_collection_of_object_values(required_resource_access.RequiredResourceAccess)),
            "samlMetadataUrl": lambda n : setattr(self, 'saml_metadata_url', n.get_str_value()),
            "serviceManagementReference": lambda n : setattr(self, 'service_management_reference', n.get_str_value()),
            "servicePrincipalLockConfiguration": lambda n : setattr(self, 'service_principal_lock_configuration', n.get_object_value(service_principal_lock_configuration.ServicePrincipalLockConfiguration)),
            "signInAudience": lambda n : setattr(self, 'sign_in_audience', n.get_str_value()),
            "spa": lambda n : setattr(self, 'spa', n.get_object_value(spa_application.SpaApplication)),
            "synchronization": lambda n : setattr(self, 'synchronization', n.get_object_value(synchronization.Synchronization)),
            "tags": lambda n : setattr(self, 'tags', n.get_collection_of_primitive_values(str)),
            "tokenEncryptionKeyId": lambda n : setattr(self, 'token_encryption_key_id', n.get_uuid_value()),
            "tokenIssuancePolicies": lambda n : setattr(self, 'token_issuance_policies', n.get_collection_of_object_values(token_issuance_policy.TokenIssuancePolicy)),
            "tokenLifetimePolicies": lambda n : setattr(self, 'token_lifetime_policies', n.get_collection_of_object_values(token_lifetime_policy.TokenLifetimePolicy)),
            "uniqueName": lambda n : setattr(self, 'unique_name', n.get_str_value()),
            "verifiedPublisher": lambda n : setattr(self, 'verified_publisher', n.get_object_value(verified_publisher.VerifiedPublisher)),
            "web": lambda n : setattr(self, 'web', n.get_object_value(web_application.WebApplication)),
            "windows": lambda n : setattr(self, 'windows', n.get_object_value(windows_application.WindowsApplication)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def group_membership_claims(self,) -> Optional[str]:
        """
        Gets the groupMembershipClaims property value. Configures the groups claim issued in a user or OAuth 2.0 access token that the application expects. To set this attribute, use one of the following string values: None, SecurityGroup (for security groups and Azure AD roles), All (this gets all security groups, distribution groups, and Azure AD directory roles that the signed-in user is a member of).
        Returns: Optional[str]
        """
        return self._group_membership_claims
    
    @group_membership_claims.setter
    def group_membership_claims(self,value: Optional[str] = None) -> None:
        """
        Sets the groupMembershipClaims property value. Configures the groups claim issued in a user or OAuth 2.0 access token that the application expects. To set this attribute, use one of the following string values: None, SecurityGroup (for security groups and Azure AD roles), All (this gets all security groups, distribution groups, and Azure AD directory roles that the signed-in user is a member of).
        Args:
            value: Value to set for the group_membership_claims property.
        """
        self._group_membership_claims = value
    
    @property
    def home_realm_discovery_policies(self,) -> Optional[List[home_realm_discovery_policy.HomeRealmDiscoveryPolicy]]:
        """
        Gets the homeRealmDiscoveryPolicies property value. The homeRealmDiscoveryPolicies property
        Returns: Optional[List[home_realm_discovery_policy.HomeRealmDiscoveryPolicy]]
        """
        return self._home_realm_discovery_policies
    
    @home_realm_discovery_policies.setter
    def home_realm_discovery_policies(self,value: Optional[List[home_realm_discovery_policy.HomeRealmDiscoveryPolicy]] = None) -> None:
        """
        Sets the homeRealmDiscoveryPolicies property value. The homeRealmDiscoveryPolicies property
        Args:
            value: Value to set for the home_realm_discovery_policies property.
        """
        self._home_realm_discovery_policies = value
    
    @property
    def identifier_uris(self,) -> Optional[List[str]]:
        """
        Gets the identifierUris property value. Also known as App ID URI, this value is set when an application is used as a resource app. The identifierUris acts as the prefix for the scopes you'll reference in your API's code, and it must be globally unique. You can use the default value provided, which is in the form api://<application-client-id>, or specify a more readable URI like https://contoso.com/api. For more information on valid identifierUris patterns and best practices, see Azure AD application registration security best practices. Not nullable. Supports $filter (eq, ne, ge, le, startsWith).
        Returns: Optional[List[str]]
        """
        return self._identifier_uris
    
    @identifier_uris.setter
    def identifier_uris(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the identifierUris property value. Also known as App ID URI, this value is set when an application is used as a resource app. The identifierUris acts as the prefix for the scopes you'll reference in your API's code, and it must be globally unique. You can use the default value provided, which is in the form api://<application-client-id>, or specify a more readable URI like https://contoso.com/api. For more information on valid identifierUris patterns and best practices, see Azure AD application registration security best practices. Not nullable. Supports $filter (eq, ne, ge, le, startsWith).
        Args:
            value: Value to set for the identifier_uris property.
        """
        self._identifier_uris = value
    
    @property
    def info(self,) -> Optional[informational_url.InformationalUrl]:
        """
        Gets the info property value. Basic profile information of the application, such as it's marketing, support, terms of service, and privacy statement URLs. The terms of service and privacy statement are surfaced to users through the user consent experience. For more information, see How to: Add Terms of service and privacy statement for registered Azure AD apps. Supports $filter (eq, ne, not, ge, le, and eq on null values).
        Returns: Optional[informational_url.InformationalUrl]
        """
        return self._info
    
    @info.setter
    def info(self,value: Optional[informational_url.InformationalUrl] = None) -> None:
        """
        Sets the info property value. Basic profile information of the application, such as it's marketing, support, terms of service, and privacy statement URLs. The terms of service and privacy statement are surfaced to users through the user consent experience. For more information, see How to: Add Terms of service and privacy statement for registered Azure AD apps. Supports $filter (eq, ne, not, ge, le, and eq on null values).
        Args:
            value: Value to set for the info property.
        """
        self._info = value
    
    @property
    def is_device_only_auth_supported(self,) -> Optional[bool]:
        """
        Gets the isDeviceOnlyAuthSupported property value. Specifies whether this application supports device authentication without a user. The default is false.
        Returns: Optional[bool]
        """
        return self._is_device_only_auth_supported
    
    @is_device_only_auth_supported.setter
    def is_device_only_auth_supported(self,value: Optional[bool] = None) -> None:
        """
        Sets the isDeviceOnlyAuthSupported property value. Specifies whether this application supports device authentication without a user. The default is false.
        Args:
            value: Value to set for the is_device_only_auth_supported property.
        """
        self._is_device_only_auth_supported = value
    
    @property
    def is_fallback_public_client(self,) -> Optional[bool]:
        """
        Gets the isFallbackPublicClient property value. Specifies the fallback application type as public client, such as an installed application running on a mobile device. The default value is false which means the fallback application type is confidential client such as a web app. There are certain scenarios where Azure AD cannot determine the client application type. For example, the ROPC flow where the application is configured without specifying a redirect URI. In those cases Azure AD interprets the application type based on the value of this property.
        Returns: Optional[bool]
        """
        return self._is_fallback_public_client
    
    @is_fallback_public_client.setter
    def is_fallback_public_client(self,value: Optional[bool] = None) -> None:
        """
        Sets the isFallbackPublicClient property value. Specifies the fallback application type as public client, such as an installed application running on a mobile device. The default value is false which means the fallback application type is confidential client such as a web app. There are certain scenarios where Azure AD cannot determine the client application type. For example, the ROPC flow where the application is configured without specifying a redirect URI. In those cases Azure AD interprets the application type based on the value of this property.
        Args:
            value: Value to set for the is_fallback_public_client property.
        """
        self._is_fallback_public_client = value
    
    @property
    def key_credentials(self,) -> Optional[List[key_credential.KeyCredential]]:
        """
        Gets the keyCredentials property value. The collection of key credentials associated with the application. Not nullable. Supports $filter (eq, not, ge, le).
        Returns: Optional[List[key_credential.KeyCredential]]
        """
        return self._key_credentials
    
    @key_credentials.setter
    def key_credentials(self,value: Optional[List[key_credential.KeyCredential]] = None) -> None:
        """
        Sets the keyCredentials property value. The collection of key credentials associated with the application. Not nullable. Supports $filter (eq, not, ge, le).
        Args:
            value: Value to set for the key_credentials property.
        """
        self._key_credentials = value
    
    @property
    def logo(self,) -> Optional[bytes]:
        """
        Gets the logo property value. The main logo for the application. Not nullable.
        Returns: Optional[bytes]
        """
        return self._logo
    
    @logo.setter
    def logo(self,value: Optional[bytes] = None) -> None:
        """
        Sets the logo property value. The main logo for the application. Not nullable.
        Args:
            value: Value to set for the logo property.
        """
        self._logo = value
    
    @property
    def notes(self,) -> Optional[str]:
        """
        Gets the notes property value. Notes relevant for the management of the application.
        Returns: Optional[str]
        """
        return self._notes
    
    @notes.setter
    def notes(self,value: Optional[str] = None) -> None:
        """
        Sets the notes property value. Notes relevant for the management of the application.
        Args:
            value: Value to set for the notes property.
        """
        self._notes = value
    
    @property
    def on_premises_publishing(self,) -> Optional[on_premises_publishing.OnPremisesPublishing]:
        """
        Gets the onPremisesPublishing property value. Represents the set of properties required for configuring Application Proxy for this application. Configuring these properties allows you to publish your on-premises application for secure remote access.
        Returns: Optional[on_premises_publishing.OnPremisesPublishing]
        """
        return self._on_premises_publishing
    
    @on_premises_publishing.setter
    def on_premises_publishing(self,value: Optional[on_premises_publishing.OnPremisesPublishing] = None) -> None:
        """
        Sets the onPremisesPublishing property value. Represents the set of properties required for configuring Application Proxy for this application. Configuring these properties allows you to publish your on-premises application for secure remote access.
        Args:
            value: Value to set for the on_premises_publishing property.
        """
        self._on_premises_publishing = value
    
    @property
    def optional_claims(self,) -> Optional[optional_claims.OptionalClaims]:
        """
        Gets the optionalClaims property value. Application developers can configure optional claims in their Azure AD applications to specify the claims that are sent to their application by the Microsoft security token service. For more information, see How to: Provide optional claims to your app.
        Returns: Optional[optional_claims.OptionalClaims]
        """
        return self._optional_claims
    
    @optional_claims.setter
    def optional_claims(self,value: Optional[optional_claims.OptionalClaims] = None) -> None:
        """
        Sets the optionalClaims property value. Application developers can configure optional claims in their Azure AD applications to specify the claims that are sent to their application by the Microsoft security token service. For more information, see How to: Provide optional claims to your app.
        Args:
            value: Value to set for the optional_claims property.
        """
        self._optional_claims = value
    
    @property
    def owners(self,) -> Optional[List[directory_object.DirectoryObject]]:
        """
        Gets the owners property value. Directory objects that are owners of the application. Read-only. Nullable. Supports $expand and $filter (/$count eq 0, /$count ne 0, /$count eq 1, /$count ne 1).
        Returns: Optional[List[directory_object.DirectoryObject]]
        """
        return self._owners
    
    @owners.setter
    def owners(self,value: Optional[List[directory_object.DirectoryObject]] = None) -> None:
        """
        Sets the owners property value. Directory objects that are owners of the application. Read-only. Nullable. Supports $expand and $filter (/$count eq 0, /$count ne 0, /$count eq 1, /$count ne 1).
        Args:
            value: Value to set for the owners property.
        """
        self._owners = value
    
    @property
    def parental_control_settings(self,) -> Optional[parental_control_settings.ParentalControlSettings]:
        """
        Gets the parentalControlSettings property value. Specifies parental control settings for an application.
        Returns: Optional[parental_control_settings.ParentalControlSettings]
        """
        return self._parental_control_settings
    
    @parental_control_settings.setter
    def parental_control_settings(self,value: Optional[parental_control_settings.ParentalControlSettings] = None) -> None:
        """
        Sets the parentalControlSettings property value. Specifies parental control settings for an application.
        Args:
            value: Value to set for the parental_control_settings property.
        """
        self._parental_control_settings = value
    
    @property
    def password_credentials(self,) -> Optional[List[password_credential.PasswordCredential]]:
        """
        Gets the passwordCredentials property value. The collection of password credentials associated with the application. Not nullable.
        Returns: Optional[List[password_credential.PasswordCredential]]
        """
        return self._password_credentials
    
    @password_credentials.setter
    def password_credentials(self,value: Optional[List[password_credential.PasswordCredential]] = None) -> None:
        """
        Sets the passwordCredentials property value. The collection of password credentials associated with the application. Not nullable.
        Args:
            value: Value to set for the password_credentials property.
        """
        self._password_credentials = value
    
    @property
    def public_client(self,) -> Optional[public_client_application.PublicClientApplication]:
        """
        Gets the publicClient property value. Specifies settings for installed clients such as desktop or mobile devices.
        Returns: Optional[public_client_application.PublicClientApplication]
        """
        return self._public_client
    
    @public_client.setter
    def public_client(self,value: Optional[public_client_application.PublicClientApplication] = None) -> None:
        """
        Sets the publicClient property value. Specifies settings for installed clients such as desktop or mobile devices.
        Args:
            value: Value to set for the public_client property.
        """
        self._public_client = value
    
    @property
    def publisher_domain(self,) -> Optional[str]:
        """
        Gets the publisherDomain property value. The verified publisher domain for the application. Read-only. Supports $filter (eq, ne, ge, le, startsWith).
        Returns: Optional[str]
        """
        return self._publisher_domain
    
    @publisher_domain.setter
    def publisher_domain(self,value: Optional[str] = None) -> None:
        """
        Sets the publisherDomain property value. The verified publisher domain for the application. Read-only. Supports $filter (eq, ne, ge, le, startsWith).
        Args:
            value: Value to set for the publisher_domain property.
        """
        self._publisher_domain = value
    
    @property
    def request_signature_verification(self,) -> Optional[request_signature_verification.RequestSignatureVerification]:
        """
        Gets the requestSignatureVerification property value. Specifies whether this application requires Azure AD to verify the signed authentication requests.
        Returns: Optional[request_signature_verification.RequestSignatureVerification]
        """
        return self._request_signature_verification
    
    @request_signature_verification.setter
    def request_signature_verification(self,value: Optional[request_signature_verification.RequestSignatureVerification] = None) -> None:
        """
        Sets the requestSignatureVerification property value. Specifies whether this application requires Azure AD to verify the signed authentication requests.
        Args:
            value: Value to set for the request_signature_verification property.
        """
        self._request_signature_verification = value
    
    @property
    def required_resource_access(self,) -> Optional[List[required_resource_access.RequiredResourceAccess]]:
        """
        Gets the requiredResourceAccess property value. Specifies the resources that the application needs to access. This property also specifies the set of delegated permissions and application roles that it needs for each of those resources. This configuration of access to the required resources drives the consent experience. No more than 50 resource services (APIs) can be configured. Beginning mid-October 2021, the total number of required permissions must not exceed 400. For more information, see Limits on requested permissions per app. Not nullable. Supports $filter (eq, not, ge, le).
        Returns: Optional[List[required_resource_access.RequiredResourceAccess]]
        """
        return self._required_resource_access
    
    @required_resource_access.setter
    def required_resource_access(self,value: Optional[List[required_resource_access.RequiredResourceAccess]] = None) -> None:
        """
        Sets the requiredResourceAccess property value. Specifies the resources that the application needs to access. This property also specifies the set of delegated permissions and application roles that it needs for each of those resources. This configuration of access to the required resources drives the consent experience. No more than 50 resource services (APIs) can be configured. Beginning mid-October 2021, the total number of required permissions must not exceed 400. For more information, see Limits on requested permissions per app. Not nullable. Supports $filter (eq, not, ge, le).
        Args:
            value: Value to set for the required_resource_access property.
        """
        self._required_resource_access = value
    
    @property
    def saml_metadata_url(self,) -> Optional[str]:
        """
        Gets the samlMetadataUrl property value. The URL where the service exposes SAML metadata for federation. This property is valid only for single-tenant applications. Nullable.
        Returns: Optional[str]
        """
        return self._saml_metadata_url
    
    @saml_metadata_url.setter
    def saml_metadata_url(self,value: Optional[str] = None) -> None:
        """
        Sets the samlMetadataUrl property value. The URL where the service exposes SAML metadata for federation. This property is valid only for single-tenant applications. Nullable.
        Args:
            value: Value to set for the saml_metadata_url property.
        """
        self._saml_metadata_url = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("api", self.api)
        writer.write_str_value("appId", self.app_id)
        writer.write_collection_of_object_values("appManagementPolicies", self.app_management_policies)
        writer.write_collection_of_object_values("appRoles", self.app_roles)
        writer.write_object_value("certification", self.certification)
        writer.write_object_value("connectorGroup", self.connector_group)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("createdOnBehalfOf", self.created_on_behalf_of)
        writer.write_str_value("defaultRedirectUri", self.default_redirect_uri)
        writer.write_str_value("description", self.description)
        writer.write_str_value("disabledByMicrosoftStatus", self.disabled_by_microsoft_status)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("extensionProperties", self.extension_properties)
        writer.write_collection_of_object_values("federatedIdentityCredentials", self.federated_identity_credentials)
        writer.write_str_value("groupMembershipClaims", self.group_membership_claims)
        writer.write_collection_of_object_values("homeRealmDiscoveryPolicies", self.home_realm_discovery_policies)
        writer.write_collection_of_primitive_values("identifierUris", self.identifier_uris)
        writer.write_object_value("info", self.info)
        writer.write_bool_value("isDeviceOnlyAuthSupported", self.is_device_only_auth_supported)
        writer.write_bool_value("isFallbackPublicClient", self.is_fallback_public_client)
        writer.write_collection_of_object_values("keyCredentials", self.key_credentials)
        writer.write_object_value("logo", self.logo)
        writer.write_str_value("notes", self.notes)
        writer.write_object_value("onPremisesPublishing", self.on_premises_publishing)
        writer.write_object_value("optionalClaims", self.optional_claims)
        writer.write_collection_of_object_values("owners", self.owners)
        writer.write_object_value("parentalControlSettings", self.parental_control_settings)
        writer.write_collection_of_object_values("passwordCredentials", self.password_credentials)
        writer.write_object_value("publicClient", self.public_client)
        writer.write_str_value("publisherDomain", self.publisher_domain)
        writer.write_object_value("requestSignatureVerification", self.request_signature_verification)
        writer.write_collection_of_object_values("requiredResourceAccess", self.required_resource_access)
        writer.write_str_value("samlMetadataUrl", self.saml_metadata_url)
        writer.write_str_value("serviceManagementReference", self.service_management_reference)
        writer.write_object_value("servicePrincipalLockConfiguration", self.service_principal_lock_configuration)
        writer.write_str_value("signInAudience", self.sign_in_audience)
        writer.write_object_value("spa", self.spa)
        writer.write_object_value("synchronization", self.synchronization)
        writer.write_collection_of_primitive_values("tags", self.tags)
        writer.write_uuid_value("tokenEncryptionKeyId", self.token_encryption_key_id)
        writer.write_collection_of_object_values("tokenIssuancePolicies", self.token_issuance_policies)
        writer.write_collection_of_object_values("tokenLifetimePolicies", self.token_lifetime_policies)
        writer.write_str_value("uniqueName", self.unique_name)
        writer.write_object_value("verifiedPublisher", self.verified_publisher)
        writer.write_object_value("web", self.web)
        writer.write_object_value("windows", self.windows)
    
    @property
    def service_management_reference(self,) -> Optional[str]:
        """
        Gets the serviceManagementReference property value. References application or service contact information from a Service or Asset Management database. Nullable.
        Returns: Optional[str]
        """
        return self._service_management_reference
    
    @service_management_reference.setter
    def service_management_reference(self,value: Optional[str] = None) -> None:
        """
        Sets the serviceManagementReference property value. References application or service contact information from a Service or Asset Management database. Nullable.
        Args:
            value: Value to set for the service_management_reference property.
        """
        self._service_management_reference = value
    
    @property
    def service_principal_lock_configuration(self,) -> Optional[service_principal_lock_configuration.ServicePrincipalLockConfiguration]:
        """
        Gets the servicePrincipalLockConfiguration property value. Specifies whether sensitive properties of a multi-tenant application should be locked for editing after the application is provisioned in a tenant. Nullable. null by default.
        Returns: Optional[service_principal_lock_configuration.ServicePrincipalLockConfiguration]
        """
        return self._service_principal_lock_configuration
    
    @service_principal_lock_configuration.setter
    def service_principal_lock_configuration(self,value: Optional[service_principal_lock_configuration.ServicePrincipalLockConfiguration] = None) -> None:
        """
        Sets the servicePrincipalLockConfiguration property value. Specifies whether sensitive properties of a multi-tenant application should be locked for editing after the application is provisioned in a tenant. Nullable. null by default.
        Args:
            value: Value to set for the service_principal_lock_configuration property.
        """
        self._service_principal_lock_configuration = value
    
    @property
    def sign_in_audience(self,) -> Optional[str]:
        """
        Gets the signInAudience property value. Specifies the Microsoft accounts that are supported for the current application. The possible values are: AzureADMyOrg, AzureADMultipleOrgs, AzureADandPersonalMicrosoftAccount (default), and PersonalMicrosoftAccount. See more in the table. The value of this object also limits the number of permissions an app can request. For more information, see Limits on requested permissions per app. The value for this property has implications on other app object properties. As a result, if you change this property, you may need to change other properties first. For more information, see Validation differences for signInAudience.Supports $filter (eq, ne, not).
        Returns: Optional[str]
        """
        return self._sign_in_audience
    
    @sign_in_audience.setter
    def sign_in_audience(self,value: Optional[str] = None) -> None:
        """
        Sets the signInAudience property value. Specifies the Microsoft accounts that are supported for the current application. The possible values are: AzureADMyOrg, AzureADMultipleOrgs, AzureADandPersonalMicrosoftAccount (default), and PersonalMicrosoftAccount. See more in the table. The value of this object also limits the number of permissions an app can request. For more information, see Limits on requested permissions per app. The value for this property has implications on other app object properties. As a result, if you change this property, you may need to change other properties first. For more information, see Validation differences for signInAudience.Supports $filter (eq, ne, not).
        Args:
            value: Value to set for the sign_in_audience property.
        """
        self._sign_in_audience = value
    
    @property
    def spa(self,) -> Optional[spa_application.SpaApplication]:
        """
        Gets the spa property value. Specifies settings for a single-page application, including sign out URLs and redirect URIs for authorization codes and access tokens.
        Returns: Optional[spa_application.SpaApplication]
        """
        return self._spa
    
    @spa.setter
    def spa(self,value: Optional[spa_application.SpaApplication] = None) -> None:
        """
        Sets the spa property value. Specifies settings for a single-page application, including sign out URLs and redirect URIs for authorization codes and access tokens.
        Args:
            value: Value to set for the spa property.
        """
        self._spa = value
    
    @property
    def synchronization(self,) -> Optional[synchronization.Synchronization]:
        """
        Gets the synchronization property value. Represents the capability for Azure Active Directory (Azure AD) identity synchronization through the Microsoft Graph API.
        Returns: Optional[synchronization.Synchronization]
        """
        return self._synchronization
    
    @synchronization.setter
    def synchronization(self,value: Optional[synchronization.Synchronization] = None) -> None:
        """
        Sets the synchronization property value. Represents the capability for Azure Active Directory (Azure AD) identity synchronization through the Microsoft Graph API.
        Args:
            value: Value to set for the synchronization property.
        """
        self._synchronization = value
    
    @property
    def tags(self,) -> Optional[List[str]]:
        """
        Gets the tags property value. Custom strings that can be used to categorize and identify the application. Not nullable. Strings added here will also appear in the tags property of any associated service principals.Supports $filter (eq, not, ge, le, startsWith) and $search.
        Returns: Optional[List[str]]
        """
        return self._tags
    
    @tags.setter
    def tags(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the tags property value. Custom strings that can be used to categorize and identify the application. Not nullable. Strings added here will also appear in the tags property of any associated service principals.Supports $filter (eq, not, ge, le, startsWith) and $search.
        Args:
            value: Value to set for the tags property.
        """
        self._tags = value
    
    @property
    def token_encryption_key_id(self,) -> Optional[UUID]:
        """
        Gets the tokenEncryptionKeyId property value. Specifies the keyId of a public key from the keyCredentials collection. When configured, Azure AD encrypts all the tokens it emits by using the key this property points to. The application code that receives the encrypted token must use the matching private key to decrypt the token before it can be used for the signed-in user.
        Returns: Optional[UUID]
        """
        return self._token_encryption_key_id
    
    @token_encryption_key_id.setter
    def token_encryption_key_id(self,value: Optional[UUID] = None) -> None:
        """
        Sets the tokenEncryptionKeyId property value. Specifies the keyId of a public key from the keyCredentials collection. When configured, Azure AD encrypts all the tokens it emits by using the key this property points to. The application code that receives the encrypted token must use the matching private key to decrypt the token before it can be used for the signed-in user.
        Args:
            value: Value to set for the token_encryption_key_id property.
        """
        self._token_encryption_key_id = value
    
    @property
    def token_issuance_policies(self,) -> Optional[List[token_issuance_policy.TokenIssuancePolicy]]:
        """
        Gets the tokenIssuancePolicies property value. The tokenIssuancePolicies property
        Returns: Optional[List[token_issuance_policy.TokenIssuancePolicy]]
        """
        return self._token_issuance_policies
    
    @token_issuance_policies.setter
    def token_issuance_policies(self,value: Optional[List[token_issuance_policy.TokenIssuancePolicy]] = None) -> None:
        """
        Sets the tokenIssuancePolicies property value. The tokenIssuancePolicies property
        Args:
            value: Value to set for the token_issuance_policies property.
        """
        self._token_issuance_policies = value
    
    @property
    def token_lifetime_policies(self,) -> Optional[List[token_lifetime_policy.TokenLifetimePolicy]]:
        """
        Gets the tokenLifetimePolicies property value. The tokenLifetimePolicies assigned to this application. Supports $expand.
        Returns: Optional[List[token_lifetime_policy.TokenLifetimePolicy]]
        """
        return self._token_lifetime_policies
    
    @token_lifetime_policies.setter
    def token_lifetime_policies(self,value: Optional[List[token_lifetime_policy.TokenLifetimePolicy]] = None) -> None:
        """
        Sets the tokenLifetimePolicies property value. The tokenLifetimePolicies assigned to this application. Supports $expand.
        Args:
            value: Value to set for the token_lifetime_policies property.
        """
        self._token_lifetime_policies = value
    
    @property
    def unique_name(self,) -> Optional[str]:
        """
        Gets the uniqueName property value. The unique identifier that can be assigned to an application as an alternative identifier. Immutable. Read-only.
        Returns: Optional[str]
        """
        return self._unique_name
    
    @unique_name.setter
    def unique_name(self,value: Optional[str] = None) -> None:
        """
        Sets the uniqueName property value. The unique identifier that can be assigned to an application as an alternative identifier. Immutable. Read-only.
        Args:
            value: Value to set for the unique_name property.
        """
        self._unique_name = value
    
    @property
    def verified_publisher(self,) -> Optional[verified_publisher.VerifiedPublisher]:
        """
        Gets the verifiedPublisher property value. Specifies the verified publisher of the application. For more information about how publisher verification helps support application security, trustworthiness, and compliance, see Publisher verification.
        Returns: Optional[verified_publisher.VerifiedPublisher]
        """
        return self._verified_publisher
    
    @verified_publisher.setter
    def verified_publisher(self,value: Optional[verified_publisher.VerifiedPublisher] = None) -> None:
        """
        Sets the verifiedPublisher property value. Specifies the verified publisher of the application. For more information about how publisher verification helps support application security, trustworthiness, and compliance, see Publisher verification.
        Args:
            value: Value to set for the verified_publisher property.
        """
        self._verified_publisher = value
    
    @property
    def web(self,) -> Optional[web_application.WebApplication]:
        """
        Gets the web property value. Specifies settings for a web application.
        Returns: Optional[web_application.WebApplication]
        """
        return self._web
    
    @web.setter
    def web(self,value: Optional[web_application.WebApplication] = None) -> None:
        """
        Sets the web property value. Specifies settings for a web application.
        Args:
            value: Value to set for the web property.
        """
        self._web = value
    
    @property
    def windows(self,) -> Optional[windows_application.WindowsApplication]:
        """
        Gets the windows property value. Specifies settings for apps running Microsoft Windows and published in the Microsoft Store or Xbox games store.
        Returns: Optional[windows_application.WindowsApplication]
        """
        return self._windows
    
    @windows.setter
    def windows(self,value: Optional[windows_application.WindowsApplication] = None) -> None:
        """
        Sets the windows property value. Specifies settings for apps running Microsoft Windows and published in the Microsoft Store or Xbox games store.
        Args:
            value: Value to set for the windows property.
        """
        self._windows = value
    

