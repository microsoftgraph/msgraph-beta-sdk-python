from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

ios_single_sign_on_extension = lazy_import('msgraph.generated.models.ios_single_sign_on_extension')

class IosKerberosSingleSignOnExtension(ios_single_sign_on_extension.IosSingleSignOnExtension):
    @property
    def active_directory_site_code(self,) -> Optional[str]:
        """
        Gets the activeDirectorySiteCode property value. Gets or sets the Active Directory site.
        Returns: Optional[str]
        """
        return self._active_directory_site_code
    
    @active_directory_site_code.setter
    def active_directory_site_code(self,value: Optional[str] = None) -> None:
        """
        Sets the activeDirectorySiteCode property value. Gets or sets the Active Directory site.
        Args:
            value: Value to set for the activeDirectorySiteCode property.
        """
        self._active_directory_site_code = value
    
    @property
    def block_active_directory_site_auto_discovery(self,) -> Optional[bool]:
        """
        Gets the blockActiveDirectorySiteAutoDiscovery property value. Enables or disables whether the Kerberos extension can automatically determine its site name.
        Returns: Optional[bool]
        """
        return self._block_active_directory_site_auto_discovery
    
    @block_active_directory_site_auto_discovery.setter
    def block_active_directory_site_auto_discovery(self,value: Optional[bool] = None) -> None:
        """
        Sets the blockActiveDirectorySiteAutoDiscovery property value. Enables or disables whether the Kerberos extension can automatically determine its site name.
        Args:
            value: Value to set for the blockActiveDirectorySiteAutoDiscovery property.
        """
        self._block_active_directory_site_auto_discovery = value
    
    @property
    def block_automatic_login(self,) -> Optional[bool]:
        """
        Gets the blockAutomaticLogin property value. Enables or disables Keychain usage.
        Returns: Optional[bool]
        """
        return self._block_automatic_login
    
    @block_automatic_login.setter
    def block_automatic_login(self,value: Optional[bool] = None) -> None:
        """
        Sets the blockAutomaticLogin property value. Enables or disables Keychain usage.
        Args:
            value: Value to set for the blockAutomaticLogin property.
        """
        self._block_automatic_login = value
    
    @property
    def cache_name(self,) -> Optional[str]:
        """
        Gets the cacheName property value. Gets or sets the Generic Security Services name of the Kerberos cache to use for this profile.
        Returns: Optional[str]
        """
        return self._cache_name
    
    @cache_name.setter
    def cache_name(self,value: Optional[str] = None) -> None:
        """
        Sets the cacheName property value. Gets or sets the Generic Security Services name of the Kerberos cache to use for this profile.
        Args:
            value: Value to set for the cacheName property.
        """
        self._cache_name = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new IosKerberosSingleSignOnExtension and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.iosKerberosSingleSignOnExtension"
        # Gets or sets the Active Directory site.
        self._active_directory_site_code: Optional[str] = None
        # Enables or disables whether the Kerberos extension can automatically determine its site name.
        self._block_active_directory_site_auto_discovery: Optional[bool] = None
        # Enables or disables Keychain usage.
        self._block_automatic_login: Optional[bool] = None
        # Gets or sets the Generic Security Services name of the Kerberos cache to use for this profile.
        self._cache_name: Optional[str] = None
        # Gets or sets a list of app Bundle IDs allowed to access the Kerberos Ticket Granting Ticket.
        self._credential_bundle_id_access_control_list: Optional[List[str]] = None
        # Gets or sets a list of realms for custom domain-realm mapping. Realms are case sensitive.
        self._domain_realms: Optional[List[str]] = None
        # Gets or sets a list of hosts or domain names for which the app extension performs SSO.
        self._domains: Optional[List[str]] = None
        # When true, this profile's realm will be selected as the default. Necessary if multiple Kerberos-type profiles are configured.
        self._is_default_realm: Optional[bool] = None
        # When set to True, the Kerberos extension allows managed apps, and any apps entered with the app bundle ID to access the credential. When set to False, the Kerberos extension allows all apps to access the credential. Available for devices running iOS and iPadOS versions 14 and later.
        self._managed_apps_in_bundle_id_a_c_l_included: Optional[bool] = None
        # Enables or disables password changes.
        self._password_block_modification: Optional[bool] = None
        # Gets or sets the URL that the user will be sent to when they initiate a password change.
        self._password_change_url: Optional[str] = None
        # Enables or disables password syncing. This won't affect users logged in with a mobile account on macOS.
        self._password_enable_local_sync: Optional[bool] = None
        # Overrides the default password expiration in days. For most domains, this value is calculated automatically.
        self._password_expiration_days: Optional[int] = None
        # Gets or sets the number of days until the user is notified that their password will expire (default is 15).
        self._password_expiration_notification_days: Optional[int] = None
        # Gets or sets the minimum number of days until a user can change their password again.
        self._password_minimum_age_days: Optional[int] = None
        # Gets or sets the minimum length of a password.
        self._password_minimum_length: Optional[int] = None
        # Gets or sets the number of previous passwords to block.
        self._password_previous_password_block_count: Optional[int] = None
        # Enables or disables whether passwords must meet Active Directory's complexity requirements.
        self._password_require_active_directory_complexity: Optional[bool] = None
        # Gets or sets a description of the password complexity requirements.
        self._password_requirements_description: Optional[str] = None
        # Gets or sets the case-sensitive realm name for this profile.
        self._realm: Optional[str] = None
        # Gets or sets whether to require authentication via Touch ID, Face ID, or a passcode to access the keychain entry.
        self._require_user_presence: Optional[bool] = None
        # Text displayed to the user at the Kerberos sign in window. Available for devices running iOS and iPadOS versions 14 and later.
        self._sign_in_help_text: Optional[str] = None
        # Gets or sets the principle user name to use for this profile. The realm name does not need to be included.
        self._user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IosKerberosSingleSignOnExtension:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IosKerberosSingleSignOnExtension
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return IosKerberosSingleSignOnExtension()
    
    @property
    def credential_bundle_id_access_control_list(self,) -> Optional[List[str]]:
        """
        Gets the credentialBundleIdAccessControlList property value. Gets or sets a list of app Bundle IDs allowed to access the Kerberos Ticket Granting Ticket.
        Returns: Optional[List[str]]
        """
        return self._credential_bundle_id_access_control_list
    
    @credential_bundle_id_access_control_list.setter
    def credential_bundle_id_access_control_list(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the credentialBundleIdAccessControlList property value. Gets or sets a list of app Bundle IDs allowed to access the Kerberos Ticket Granting Ticket.
        Args:
            value: Value to set for the credentialBundleIdAccessControlList property.
        """
        self._credential_bundle_id_access_control_list = value
    
    @property
    def domain_realms(self,) -> Optional[List[str]]:
        """
        Gets the domainRealms property value. Gets or sets a list of realms for custom domain-realm mapping. Realms are case sensitive.
        Returns: Optional[List[str]]
        """
        return self._domain_realms
    
    @domain_realms.setter
    def domain_realms(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the domainRealms property value. Gets or sets a list of realms for custom domain-realm mapping. Realms are case sensitive.
        Args:
            value: Value to set for the domainRealms property.
        """
        self._domain_realms = value
    
    @property
    def domains(self,) -> Optional[List[str]]:
        """
        Gets the domains property value. Gets or sets a list of hosts or domain names for which the app extension performs SSO.
        Returns: Optional[List[str]]
        """
        return self._domains
    
    @domains.setter
    def domains(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the domains property value. Gets or sets a list of hosts or domain names for which the app extension performs SSO.
        Args:
            value: Value to set for the domains property.
        """
        self._domains = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "active_directory_site_code": lambda n : setattr(self, 'active_directory_site_code', n.get_str_value()),
            "block_active_directory_site_auto_discovery": lambda n : setattr(self, 'block_active_directory_site_auto_discovery', n.get_bool_value()),
            "block_automatic_login": lambda n : setattr(self, 'block_automatic_login', n.get_bool_value()),
            "cache_name": lambda n : setattr(self, 'cache_name', n.get_str_value()),
            "credential_bundle_id_access_control_list": lambda n : setattr(self, 'credential_bundle_id_access_control_list', n.get_collection_of_primitive_values(str)),
            "domain_realms": lambda n : setattr(self, 'domain_realms', n.get_collection_of_primitive_values(str)),
            "domains": lambda n : setattr(self, 'domains', n.get_collection_of_primitive_values(str)),
            "is_default_realm": lambda n : setattr(self, 'is_default_realm', n.get_bool_value()),
            "managed_apps_in_bundle_id_a_c_l_included": lambda n : setattr(self, 'managed_apps_in_bundle_id_a_c_l_included', n.get_bool_value()),
            "password_block_modification": lambda n : setattr(self, 'password_block_modification', n.get_bool_value()),
            "password_change_url": lambda n : setattr(self, 'password_change_url', n.get_str_value()),
            "password_enable_local_sync": lambda n : setattr(self, 'password_enable_local_sync', n.get_bool_value()),
            "password_expiration_days": lambda n : setattr(self, 'password_expiration_days', n.get_int_value()),
            "password_expiration_notification_days": lambda n : setattr(self, 'password_expiration_notification_days', n.get_int_value()),
            "password_minimum_age_days": lambda n : setattr(self, 'password_minimum_age_days', n.get_int_value()),
            "password_minimum_length": lambda n : setattr(self, 'password_minimum_length', n.get_int_value()),
            "password_previous_password_block_count": lambda n : setattr(self, 'password_previous_password_block_count', n.get_int_value()),
            "password_require_active_directory_complexity": lambda n : setattr(self, 'password_require_active_directory_complexity', n.get_bool_value()),
            "password_requirements_description": lambda n : setattr(self, 'password_requirements_description', n.get_str_value()),
            "realm": lambda n : setattr(self, 'realm', n.get_str_value()),
            "require_user_presence": lambda n : setattr(self, 'require_user_presence', n.get_bool_value()),
            "sign_in_help_text": lambda n : setattr(self, 'sign_in_help_text', n.get_str_value()),
            "user_principal_name": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_default_realm(self,) -> Optional[bool]:
        """
        Gets the isDefaultRealm property value. When true, this profile's realm will be selected as the default. Necessary if multiple Kerberos-type profiles are configured.
        Returns: Optional[bool]
        """
        return self._is_default_realm
    
    @is_default_realm.setter
    def is_default_realm(self,value: Optional[bool] = None) -> None:
        """
        Sets the isDefaultRealm property value. When true, this profile's realm will be selected as the default. Necessary if multiple Kerberos-type profiles are configured.
        Args:
            value: Value to set for the isDefaultRealm property.
        """
        self._is_default_realm = value
    
    @property
    def managed_apps_in_bundle_id_a_c_l_included(self,) -> Optional[bool]:
        """
        Gets the managedAppsInBundleIdACLIncluded property value. When set to True, the Kerberos extension allows managed apps, and any apps entered with the app bundle ID to access the credential. When set to False, the Kerberos extension allows all apps to access the credential. Available for devices running iOS and iPadOS versions 14 and later.
        Returns: Optional[bool]
        """
        return self._managed_apps_in_bundle_id_a_c_l_included
    
    @managed_apps_in_bundle_id_a_c_l_included.setter
    def managed_apps_in_bundle_id_a_c_l_included(self,value: Optional[bool] = None) -> None:
        """
        Sets the managedAppsInBundleIdACLIncluded property value. When set to True, the Kerberos extension allows managed apps, and any apps entered with the app bundle ID to access the credential. When set to False, the Kerberos extension allows all apps to access the credential. Available for devices running iOS and iPadOS versions 14 and later.
        Args:
            value: Value to set for the managedAppsInBundleIdACLIncluded property.
        """
        self._managed_apps_in_bundle_id_a_c_l_included = value
    
    @property
    def password_block_modification(self,) -> Optional[bool]:
        """
        Gets the passwordBlockModification property value. Enables or disables password changes.
        Returns: Optional[bool]
        """
        return self._password_block_modification
    
    @password_block_modification.setter
    def password_block_modification(self,value: Optional[bool] = None) -> None:
        """
        Sets the passwordBlockModification property value. Enables or disables password changes.
        Args:
            value: Value to set for the passwordBlockModification property.
        """
        self._password_block_modification = value
    
    @property
    def password_change_url(self,) -> Optional[str]:
        """
        Gets the passwordChangeUrl property value. Gets or sets the URL that the user will be sent to when they initiate a password change.
        Returns: Optional[str]
        """
        return self._password_change_url
    
    @password_change_url.setter
    def password_change_url(self,value: Optional[str] = None) -> None:
        """
        Sets the passwordChangeUrl property value. Gets or sets the URL that the user will be sent to when they initiate a password change.
        Args:
            value: Value to set for the passwordChangeUrl property.
        """
        self._password_change_url = value
    
    @property
    def password_enable_local_sync(self,) -> Optional[bool]:
        """
        Gets the passwordEnableLocalSync property value. Enables or disables password syncing. This won't affect users logged in with a mobile account on macOS.
        Returns: Optional[bool]
        """
        return self._password_enable_local_sync
    
    @password_enable_local_sync.setter
    def password_enable_local_sync(self,value: Optional[bool] = None) -> None:
        """
        Sets the passwordEnableLocalSync property value. Enables or disables password syncing. This won't affect users logged in with a mobile account on macOS.
        Args:
            value: Value to set for the passwordEnableLocalSync property.
        """
        self._password_enable_local_sync = value
    
    @property
    def password_expiration_days(self,) -> Optional[int]:
        """
        Gets the passwordExpirationDays property value. Overrides the default password expiration in days. For most domains, this value is calculated automatically.
        Returns: Optional[int]
        """
        return self._password_expiration_days
    
    @password_expiration_days.setter
    def password_expiration_days(self,value: Optional[int] = None) -> None:
        """
        Sets the passwordExpirationDays property value. Overrides the default password expiration in days. For most domains, this value is calculated automatically.
        Args:
            value: Value to set for the passwordExpirationDays property.
        """
        self._password_expiration_days = value
    
    @property
    def password_expiration_notification_days(self,) -> Optional[int]:
        """
        Gets the passwordExpirationNotificationDays property value. Gets or sets the number of days until the user is notified that their password will expire (default is 15).
        Returns: Optional[int]
        """
        return self._password_expiration_notification_days
    
    @password_expiration_notification_days.setter
    def password_expiration_notification_days(self,value: Optional[int] = None) -> None:
        """
        Sets the passwordExpirationNotificationDays property value. Gets or sets the number of days until the user is notified that their password will expire (default is 15).
        Args:
            value: Value to set for the passwordExpirationNotificationDays property.
        """
        self._password_expiration_notification_days = value
    
    @property
    def password_minimum_age_days(self,) -> Optional[int]:
        """
        Gets the passwordMinimumAgeDays property value. Gets or sets the minimum number of days until a user can change their password again.
        Returns: Optional[int]
        """
        return self._password_minimum_age_days
    
    @password_minimum_age_days.setter
    def password_minimum_age_days(self,value: Optional[int] = None) -> None:
        """
        Sets the passwordMinimumAgeDays property value. Gets or sets the minimum number of days until a user can change their password again.
        Args:
            value: Value to set for the passwordMinimumAgeDays property.
        """
        self._password_minimum_age_days = value
    
    @property
    def password_minimum_length(self,) -> Optional[int]:
        """
        Gets the passwordMinimumLength property value. Gets or sets the minimum length of a password.
        Returns: Optional[int]
        """
        return self._password_minimum_length
    
    @password_minimum_length.setter
    def password_minimum_length(self,value: Optional[int] = None) -> None:
        """
        Sets the passwordMinimumLength property value. Gets or sets the minimum length of a password.
        Args:
            value: Value to set for the passwordMinimumLength property.
        """
        self._password_minimum_length = value
    
    @property
    def password_previous_password_block_count(self,) -> Optional[int]:
        """
        Gets the passwordPreviousPasswordBlockCount property value. Gets or sets the number of previous passwords to block.
        Returns: Optional[int]
        """
        return self._password_previous_password_block_count
    
    @password_previous_password_block_count.setter
    def password_previous_password_block_count(self,value: Optional[int] = None) -> None:
        """
        Sets the passwordPreviousPasswordBlockCount property value. Gets or sets the number of previous passwords to block.
        Args:
            value: Value to set for the passwordPreviousPasswordBlockCount property.
        """
        self._password_previous_password_block_count = value
    
    @property
    def password_require_active_directory_complexity(self,) -> Optional[bool]:
        """
        Gets the passwordRequireActiveDirectoryComplexity property value. Enables or disables whether passwords must meet Active Directory's complexity requirements.
        Returns: Optional[bool]
        """
        return self._password_require_active_directory_complexity
    
    @password_require_active_directory_complexity.setter
    def password_require_active_directory_complexity(self,value: Optional[bool] = None) -> None:
        """
        Sets the passwordRequireActiveDirectoryComplexity property value. Enables or disables whether passwords must meet Active Directory's complexity requirements.
        Args:
            value: Value to set for the passwordRequireActiveDirectoryComplexity property.
        """
        self._password_require_active_directory_complexity = value
    
    @property
    def password_requirements_description(self,) -> Optional[str]:
        """
        Gets the passwordRequirementsDescription property value. Gets or sets a description of the password complexity requirements.
        Returns: Optional[str]
        """
        return self._password_requirements_description
    
    @password_requirements_description.setter
    def password_requirements_description(self,value: Optional[str] = None) -> None:
        """
        Sets the passwordRequirementsDescription property value. Gets or sets a description of the password complexity requirements.
        Args:
            value: Value to set for the passwordRequirementsDescription property.
        """
        self._password_requirements_description = value
    
    @property
    def realm(self,) -> Optional[str]:
        """
        Gets the realm property value. Gets or sets the case-sensitive realm name for this profile.
        Returns: Optional[str]
        """
        return self._realm
    
    @realm.setter
    def realm(self,value: Optional[str] = None) -> None:
        """
        Sets the realm property value. Gets or sets the case-sensitive realm name for this profile.
        Args:
            value: Value to set for the realm property.
        """
        self._realm = value
    
    @property
    def require_user_presence(self,) -> Optional[bool]:
        """
        Gets the requireUserPresence property value. Gets or sets whether to require authentication via Touch ID, Face ID, or a passcode to access the keychain entry.
        Returns: Optional[bool]
        """
        return self._require_user_presence
    
    @require_user_presence.setter
    def require_user_presence(self,value: Optional[bool] = None) -> None:
        """
        Sets the requireUserPresence property value. Gets or sets whether to require authentication via Touch ID, Face ID, or a passcode to access the keychain entry.
        Args:
            value: Value to set for the requireUserPresence property.
        """
        self._require_user_presence = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("activeDirectorySiteCode", self.active_directory_site_code)
        writer.write_bool_value("blockActiveDirectorySiteAutoDiscovery", self.block_active_directory_site_auto_discovery)
        writer.write_bool_value("blockAutomaticLogin", self.block_automatic_login)
        writer.write_str_value("cacheName", self.cache_name)
        writer.write_collection_of_primitive_values("credentialBundleIdAccessControlList", self.credential_bundle_id_access_control_list)
        writer.write_collection_of_primitive_values("domainRealms", self.domain_realms)
        writer.write_collection_of_primitive_values("domains", self.domains)
        writer.write_bool_value("isDefaultRealm", self.is_default_realm)
        writer.write_bool_value("managedAppsInBundleIdACLIncluded", self.managed_apps_in_bundle_id_a_c_l_included)
        writer.write_bool_value("passwordBlockModification", self.password_block_modification)
        writer.write_str_value("passwordChangeUrl", self.password_change_url)
        writer.write_bool_value("passwordEnableLocalSync", self.password_enable_local_sync)
        writer.write_int_value("passwordExpirationDays", self.password_expiration_days)
        writer.write_int_value("passwordExpirationNotificationDays", self.password_expiration_notification_days)
        writer.write_int_value("passwordMinimumAgeDays", self.password_minimum_age_days)
        writer.write_int_value("passwordMinimumLength", self.password_minimum_length)
        writer.write_int_value("passwordPreviousPasswordBlockCount", self.password_previous_password_block_count)
        writer.write_bool_value("passwordRequireActiveDirectoryComplexity", self.password_require_active_directory_complexity)
        writer.write_str_value("passwordRequirementsDescription", self.password_requirements_description)
        writer.write_str_value("realm", self.realm)
        writer.write_bool_value("requireUserPresence", self.require_user_presence)
        writer.write_str_value("signInHelpText", self.sign_in_help_text)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
    
    @property
    def sign_in_help_text(self,) -> Optional[str]:
        """
        Gets the signInHelpText property value. Text displayed to the user at the Kerberos sign in window. Available for devices running iOS and iPadOS versions 14 and later.
        Returns: Optional[str]
        """
        return self._sign_in_help_text
    
    @sign_in_help_text.setter
    def sign_in_help_text(self,value: Optional[str] = None) -> None:
        """
        Sets the signInHelpText property value. Text displayed to the user at the Kerberos sign in window. Available for devices running iOS and iPadOS versions 14 and later.
        Args:
            value: Value to set for the signInHelpText property.
        """
        self._sign_in_help_text = value
    
    @property
    def user_principal_name(self,) -> Optional[str]:
        """
        Gets the userPrincipalName property value. Gets or sets the principle user name to use for this profile. The realm name does not need to be included.
        Returns: Optional[str]
        """
        return self._user_principal_name
    
    @user_principal_name.setter
    def user_principal_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userPrincipalName property value. Gets or sets the principle user name to use for this profile. The realm name does not need to be included.
        Args:
            value: Value to set for the userPrincipalName property.
        """
        self._user_principal_name = value
    

