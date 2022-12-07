from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

apple_device_features_configuration_base = lazy_import('msgraph.generated.models.apple_device_features_configuration_base')
ip_range = lazy_import('msgraph.generated.models.ip_range')
key_value_pair = lazy_import('msgraph.generated.models.key_value_pair')
mac_o_s_associated_domains_item = lazy_import('msgraph.generated.models.mac_o_s_associated_domains_item')
mac_o_s_certificate_profile_base = lazy_import('msgraph.generated.models.mac_o_s_certificate_profile_base')
mac_o_s_content_caching_client_policy = lazy_import('msgraph.generated.models.mac_o_s_content_caching_client_policy')
mac_o_s_content_caching_parent_selection_policy = lazy_import('msgraph.generated.models.mac_o_s_content_caching_parent_selection_policy')
mac_o_s_content_caching_peer_policy = lazy_import('msgraph.generated.models.mac_o_s_content_caching_peer_policy')
mac_o_s_content_caching_type = lazy_import('msgraph.generated.models.mac_o_s_content_caching_type')
mac_o_s_launch_item = lazy_import('msgraph.generated.models.mac_o_s_launch_item')
mac_o_s_single_sign_on_extension = lazy_import('msgraph.generated.models.mac_o_s_single_sign_on_extension')
single_sign_on_extension = lazy_import('msgraph.generated.models.single_sign_on_extension')

class MacOSDeviceFeaturesConfiguration(apple_device_features_configuration_base.AppleDeviceFeaturesConfigurationBase):
    @property
    def admin_show_host_info(self,) -> Optional[bool]:
        """
        Gets the adminShowHostInfo property value. Whether to show admin host information on the login window.
        Returns: Optional[bool]
        """
        return self._admin_show_host_info
    
    @admin_show_host_info.setter
    def admin_show_host_info(self,value: Optional[bool] = None) -> None:
        """
        Sets the adminShowHostInfo property value. Whether to show admin host information on the login window.
        Args:
            value: Value to set for the adminShowHostInfo property.
        """
        self._admin_show_host_info = value
    
    @property
    def app_associated_domains(self,) -> Optional[List[mac_o_s_associated_domains_item.MacOSAssociatedDomainsItem]]:
        """
        Gets the appAssociatedDomains property value. Gets or sets a list that maps apps to their associated domains. Application identifiers must be unique. This collection can contain a maximum of 500 elements.
        Returns: Optional[List[mac_o_s_associated_domains_item.MacOSAssociatedDomainsItem]]
        """
        return self._app_associated_domains
    
    @app_associated_domains.setter
    def app_associated_domains(self,value: Optional[List[mac_o_s_associated_domains_item.MacOSAssociatedDomainsItem]] = None) -> None:
        """
        Sets the appAssociatedDomains property value. Gets or sets a list that maps apps to their associated domains. Application identifiers must be unique. This collection can contain a maximum of 500 elements.
        Args:
            value: Value to set for the appAssociatedDomains property.
        """
        self._app_associated_domains = value
    
    @property
    def associated_domains(self,) -> Optional[List[key_value_pair.KeyValuePair]]:
        """
        Gets the associatedDomains property value. DEPRECATED: use appAssociatedDomains instead. Gets or sets a list that maps apps to their associated domains. The key should match the app's ID, and the value should be a string in the form of 'service:domain' where domain is a fully qualified hostname (e.g. webcredentials:example.com). This collection can contain a maximum of 500 elements.
        Returns: Optional[List[key_value_pair.KeyValuePair]]
        """
        return self._associated_domains
    
    @associated_domains.setter
    def associated_domains(self,value: Optional[List[key_value_pair.KeyValuePair]] = None) -> None:
        """
        Sets the associatedDomains property value. DEPRECATED: use appAssociatedDomains instead. Gets or sets a list that maps apps to their associated domains. The key should match the app's ID, and the value should be a string in the form of 'service:domain' where domain is a fully qualified hostname (e.g. webcredentials:example.com). This collection can contain a maximum of 500 elements.
        Args:
            value: Value to set for the associatedDomains property.
        """
        self._associated_domains = value
    
    @property
    def authorized_users_list_hidden(self,) -> Optional[bool]:
        """
        Gets the authorizedUsersListHidden property value. Whether to show the name and password dialog or a list of users on the login window.
        Returns: Optional[bool]
        """
        return self._authorized_users_list_hidden
    
    @authorized_users_list_hidden.setter
    def authorized_users_list_hidden(self,value: Optional[bool] = None) -> None:
        """
        Sets the authorizedUsersListHidden property value. Whether to show the name and password dialog or a list of users on the login window.
        Args:
            value: Value to set for the authorizedUsersListHidden property.
        """
        self._authorized_users_list_hidden = value
    
    @property
    def authorized_users_list_hide_admin_users(self,) -> Optional[bool]:
        """
        Gets the authorizedUsersListHideAdminUsers property value. Whether to hide admin users in the authorized users list on the login window.
        Returns: Optional[bool]
        """
        return self._authorized_users_list_hide_admin_users
    
    @authorized_users_list_hide_admin_users.setter
    def authorized_users_list_hide_admin_users(self,value: Optional[bool] = None) -> None:
        """
        Sets the authorizedUsersListHideAdminUsers property value. Whether to hide admin users in the authorized users list on the login window.
        Args:
            value: Value to set for the authorizedUsersListHideAdminUsers property.
        """
        self._authorized_users_list_hide_admin_users = value
    
    @property
    def authorized_users_list_hide_local_users(self,) -> Optional[bool]:
        """
        Gets the authorizedUsersListHideLocalUsers property value. Whether to show only network and system users in the authorized users list on the login window.
        Returns: Optional[bool]
        """
        return self._authorized_users_list_hide_local_users
    
    @authorized_users_list_hide_local_users.setter
    def authorized_users_list_hide_local_users(self,value: Optional[bool] = None) -> None:
        """
        Sets the authorizedUsersListHideLocalUsers property value. Whether to show only network and system users in the authorized users list on the login window.
        Args:
            value: Value to set for the authorizedUsersListHideLocalUsers property.
        """
        self._authorized_users_list_hide_local_users = value
    
    @property
    def authorized_users_list_hide_mobile_accounts(self,) -> Optional[bool]:
        """
        Gets the authorizedUsersListHideMobileAccounts property value. Whether to hide mobile users in the authorized users list on the login window.
        Returns: Optional[bool]
        """
        return self._authorized_users_list_hide_mobile_accounts
    
    @authorized_users_list_hide_mobile_accounts.setter
    def authorized_users_list_hide_mobile_accounts(self,value: Optional[bool] = None) -> None:
        """
        Sets the authorizedUsersListHideMobileAccounts property value. Whether to hide mobile users in the authorized users list on the login window.
        Args:
            value: Value to set for the authorizedUsersListHideMobileAccounts property.
        """
        self._authorized_users_list_hide_mobile_accounts = value
    
    @property
    def authorized_users_list_include_network_users(self,) -> Optional[bool]:
        """
        Gets the authorizedUsersListIncludeNetworkUsers property value. Whether to show network users in the authorized users list on the login window.
        Returns: Optional[bool]
        """
        return self._authorized_users_list_include_network_users
    
    @authorized_users_list_include_network_users.setter
    def authorized_users_list_include_network_users(self,value: Optional[bool] = None) -> None:
        """
        Sets the authorizedUsersListIncludeNetworkUsers property value. Whether to show network users in the authorized users list on the login window.
        Args:
            value: Value to set for the authorizedUsersListIncludeNetworkUsers property.
        """
        self._authorized_users_list_include_network_users = value
    
    @property
    def authorized_users_list_show_other_managed_users(self,) -> Optional[bool]:
        """
        Gets the authorizedUsersListShowOtherManagedUsers property value. Whether to show other users in the authorized users list on the login window.
        Returns: Optional[bool]
        """
        return self._authorized_users_list_show_other_managed_users
    
    @authorized_users_list_show_other_managed_users.setter
    def authorized_users_list_show_other_managed_users(self,value: Optional[bool] = None) -> None:
        """
        Sets the authorizedUsersListShowOtherManagedUsers property value. Whether to show other users in the authorized users list on the login window.
        Args:
            value: Value to set for the authorizedUsersListShowOtherManagedUsers property.
        """
        self._authorized_users_list_show_other_managed_users = value
    
    @property
    def auto_launch_items(self,) -> Optional[List[mac_o_s_launch_item.MacOSLaunchItem]]:
        """
        Gets the autoLaunchItems property value. List of applications, files, folders, and other items to launch when the user logs in. This collection can contain a maximum of 500 elements.
        Returns: Optional[List[mac_o_s_launch_item.MacOSLaunchItem]]
        """
        return self._auto_launch_items
    
    @auto_launch_items.setter
    def auto_launch_items(self,value: Optional[List[mac_o_s_launch_item.MacOSLaunchItem]] = None) -> None:
        """
        Sets the autoLaunchItems property value. List of applications, files, folders, and other items to launch when the user logs in. This collection can contain a maximum of 500 elements.
        Args:
            value: Value to set for the autoLaunchItems property.
        """
        self._auto_launch_items = value
    
    @property
    def console_access_disabled(self,) -> Optional[bool]:
        """
        Gets the consoleAccessDisabled property value. Whether the Other user will disregard use of the console special user name.
        Returns: Optional[bool]
        """
        return self._console_access_disabled
    
    @console_access_disabled.setter
    def console_access_disabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the consoleAccessDisabled property value. Whether the Other user will disregard use of the console special user name.
        Args:
            value: Value to set for the consoleAccessDisabled property.
        """
        self._console_access_disabled = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new MacOSDeviceFeaturesConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.macOSDeviceFeaturesConfiguration"
        # Whether to show admin host information on the login window.
        self._admin_show_host_info: Optional[bool] = None
        # Gets or sets a list that maps apps to their associated domains. Application identifiers must be unique. This collection can contain a maximum of 500 elements.
        self._app_associated_domains: Optional[List[mac_o_s_associated_domains_item.MacOSAssociatedDomainsItem]] = None
        # DEPRECATED: use appAssociatedDomains instead. Gets or sets a list that maps apps to their associated domains. The key should match the app's ID, and the value should be a string in the form of 'service:domain' where domain is a fully qualified hostname (e.g. webcredentials:example.com). This collection can contain a maximum of 500 elements.
        self._associated_domains: Optional[List[key_value_pair.KeyValuePair]] = None
        # Whether to show the name and password dialog or a list of users on the login window.
        self._authorized_users_list_hidden: Optional[bool] = None
        # Whether to hide admin users in the authorized users list on the login window.
        self._authorized_users_list_hide_admin_users: Optional[bool] = None
        # Whether to show only network and system users in the authorized users list on the login window.
        self._authorized_users_list_hide_local_users: Optional[bool] = None
        # Whether to hide mobile users in the authorized users list on the login window.
        self._authorized_users_list_hide_mobile_accounts: Optional[bool] = None
        # Whether to show network users in the authorized users list on the login window.
        self._authorized_users_list_include_network_users: Optional[bool] = None
        # Whether to show other users in the authorized users list on the login window.
        self._authorized_users_list_show_other_managed_users: Optional[bool] = None
        # List of applications, files, folders, and other items to launch when the user logs in. This collection can contain a maximum of 500 elements.
        self._auto_launch_items: Optional[List[mac_o_s_launch_item.MacOSLaunchItem]] = None
        # Whether the Other user will disregard use of the console special user name.
        self._console_access_disabled: Optional[bool] = None
        # Prevents content caches from purging content to free up disk space for other apps.
        self._content_caching_block_deletion: Optional[bool] = None
        # A list of custom IP ranges content caches will use to listen for clients. This collection can contain a maximum of 500 elements.
        self._content_caching_client_listen_ranges: Optional[List[ip_range.IpRange]] = None
        # Determines which clients a content cache will serve.
        self._content_caching_client_policy: Optional[mac_o_s_content_caching_client_policy.MacOSContentCachingClientPolicy] = None
        # The path to the directory used to store cached content. The value must be (or end with) /Library/Application Support/Apple/AssetCache/Data
        self._content_caching_data_path: Optional[str] = None
        # Disables internet connection sharing.
        self._content_caching_disable_connection_sharing: Optional[bool] = None
        # Enables content caching and prevents it from being disabled by the user.
        self._content_caching_enabled: Optional[bool] = None
        # Forces internet connection sharing. contentCachingDisableConnectionSharing overrides this setting.
        self._content_caching_force_connection_sharing: Optional[bool] = None
        # Prevent the device from sleeping if content caching is enabled.
        self._content_caching_keep_awake: Optional[bool] = None
        # Enables logging of IP addresses and ports of clients that request cached content.
        self._content_caching_log_client_identities: Optional[bool] = None
        # The maximum number of bytes of disk space that will be used for the content cache. A value of 0 (default) indicates unlimited disk space.
        self._content_caching_max_size_bytes: Optional[int] = None
        # A list of IP addresses representing parent content caches.
        self._content_caching_parents: Optional[List[str]] = None
        # Determines how content caches select a parent cache.
        self._content_caching_parent_selection_policy: Optional[mac_o_s_content_caching_parent_selection_policy.MacOSContentCachingParentSelectionPolicy] = None
        # A list of custom IP ranges content caches will use to query for content from peers caches. This collection can contain a maximum of 500 elements.
        self._content_caching_peer_filter_ranges: Optional[List[ip_range.IpRange]] = None
        # A list of custom IP ranges content caches will use to listen for peer caches. This collection can contain a maximum of 500 elements.
        self._content_caching_peer_listen_ranges: Optional[List[ip_range.IpRange]] = None
        # Determines which content caches other content caches will peer with.
        self._content_caching_peer_policy: Optional[mac_o_s_content_caching_peer_policy.MacOSContentCachingPeerPolicy] = None
        # Sets the port used for content caching. If the value is 0, a random available port will be selected. Valid values 0 to 65535
        self._content_caching_port: Optional[int] = None
        # A list of custom IP ranges that Apple's content caching service should use to match clients to content caches. This collection can contain a maximum of 500 elements.
        self._content_caching_public_ranges: Optional[List[ip_range.IpRange]] = None
        # Display content caching alerts as system notifications.
        self._content_caching_show_alerts: Optional[bool] = None
        # Indicates the type of content allowed to be cached by Apple's content caching service.
        self._content_caching_type: Optional[mac_o_s_content_caching_type.MacOSContentCachingType] = None
        # Custom text to be displayed on the login window.
        self._login_window_text: Optional[str] = None
        # Whether the Log Out menu item on the login window will be disabled while the user is logged in.
        self._log_out_disabled_while_logged_in: Optional[bool] = None
        # Gets or sets a single sign-on extension profile.
        self._mac_o_s_single_sign_on_extension: Optional[mac_o_s_single_sign_on_extension.MacOSSingleSignOnExtension] = None
        # Whether the Power Off menu item on the login window will be disabled while the user is logged in.
        self._power_off_disabled_while_logged_in: Optional[bool] = None
        # Whether to hide the Restart button item on the login window.
        self._restart_disabled: Optional[bool] = None
        # Whether the Restart menu item on the login window will be disabled while the user is logged in.
        self._restart_disabled_while_logged_in: Optional[bool] = None
        # Whether to disable the immediate screen lock functions.
        self._screen_lock_disable_immediate: Optional[bool] = None
        # Whether to hide the Shut Down button item on the login window.
        self._shut_down_disabled: Optional[bool] = None
        # Whether the Shut Down menu item on the login window will be disabled while the user is logged in.
        self._shut_down_disabled_while_logged_in: Optional[bool] = None
        # Gets or sets a single sign-on extension profile. Deprecated: use MacOSSingleSignOnExtension instead.
        self._single_sign_on_extension: Optional[single_sign_on_extension.SingleSignOnExtension] = None
        # PKINIT Certificate for the authentication with single sign-on extensions.
        self._single_sign_on_extension_pkinit_certificate: Optional[mac_o_s_certificate_profile_base.MacOSCertificateProfileBase] = None
        # Whether to hide the Sleep menu item on the login window.
        self._sleep_disabled: Optional[bool] = None
    
    @property
    def content_caching_block_deletion(self,) -> Optional[bool]:
        """
        Gets the contentCachingBlockDeletion property value. Prevents content caches from purging content to free up disk space for other apps.
        Returns: Optional[bool]
        """
        return self._content_caching_block_deletion
    
    @content_caching_block_deletion.setter
    def content_caching_block_deletion(self,value: Optional[bool] = None) -> None:
        """
        Sets the contentCachingBlockDeletion property value. Prevents content caches from purging content to free up disk space for other apps.
        Args:
            value: Value to set for the contentCachingBlockDeletion property.
        """
        self._content_caching_block_deletion = value
    
    @property
    def content_caching_client_listen_ranges(self,) -> Optional[List[ip_range.IpRange]]:
        """
        Gets the contentCachingClientListenRanges property value. A list of custom IP ranges content caches will use to listen for clients. This collection can contain a maximum of 500 elements.
        Returns: Optional[List[ip_range.IpRange]]
        """
        return self._content_caching_client_listen_ranges
    
    @content_caching_client_listen_ranges.setter
    def content_caching_client_listen_ranges(self,value: Optional[List[ip_range.IpRange]] = None) -> None:
        """
        Sets the contentCachingClientListenRanges property value. A list of custom IP ranges content caches will use to listen for clients. This collection can contain a maximum of 500 elements.
        Args:
            value: Value to set for the contentCachingClientListenRanges property.
        """
        self._content_caching_client_listen_ranges = value
    
    @property
    def content_caching_client_policy(self,) -> Optional[mac_o_s_content_caching_client_policy.MacOSContentCachingClientPolicy]:
        """
        Gets the contentCachingClientPolicy property value. Determines which clients a content cache will serve.
        Returns: Optional[mac_o_s_content_caching_client_policy.MacOSContentCachingClientPolicy]
        """
        return self._content_caching_client_policy
    
    @content_caching_client_policy.setter
    def content_caching_client_policy(self,value: Optional[mac_o_s_content_caching_client_policy.MacOSContentCachingClientPolicy] = None) -> None:
        """
        Sets the contentCachingClientPolicy property value. Determines which clients a content cache will serve.
        Args:
            value: Value to set for the contentCachingClientPolicy property.
        """
        self._content_caching_client_policy = value
    
    @property
    def content_caching_data_path(self,) -> Optional[str]:
        """
        Gets the contentCachingDataPath property value. The path to the directory used to store cached content. The value must be (or end with) /Library/Application Support/Apple/AssetCache/Data
        Returns: Optional[str]
        """
        return self._content_caching_data_path
    
    @content_caching_data_path.setter
    def content_caching_data_path(self,value: Optional[str] = None) -> None:
        """
        Sets the contentCachingDataPath property value. The path to the directory used to store cached content. The value must be (or end with) /Library/Application Support/Apple/AssetCache/Data
        Args:
            value: Value to set for the contentCachingDataPath property.
        """
        self._content_caching_data_path = value
    
    @property
    def content_caching_disable_connection_sharing(self,) -> Optional[bool]:
        """
        Gets the contentCachingDisableConnectionSharing property value. Disables internet connection sharing.
        Returns: Optional[bool]
        """
        return self._content_caching_disable_connection_sharing
    
    @content_caching_disable_connection_sharing.setter
    def content_caching_disable_connection_sharing(self,value: Optional[bool] = None) -> None:
        """
        Sets the contentCachingDisableConnectionSharing property value. Disables internet connection sharing.
        Args:
            value: Value to set for the contentCachingDisableConnectionSharing property.
        """
        self._content_caching_disable_connection_sharing = value
    
    @property
    def content_caching_enabled(self,) -> Optional[bool]:
        """
        Gets the contentCachingEnabled property value. Enables content caching and prevents it from being disabled by the user.
        Returns: Optional[bool]
        """
        return self._content_caching_enabled
    
    @content_caching_enabled.setter
    def content_caching_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the contentCachingEnabled property value. Enables content caching and prevents it from being disabled by the user.
        Args:
            value: Value to set for the contentCachingEnabled property.
        """
        self._content_caching_enabled = value
    
    @property
    def content_caching_force_connection_sharing(self,) -> Optional[bool]:
        """
        Gets the contentCachingForceConnectionSharing property value. Forces internet connection sharing. contentCachingDisableConnectionSharing overrides this setting.
        Returns: Optional[bool]
        """
        return self._content_caching_force_connection_sharing
    
    @content_caching_force_connection_sharing.setter
    def content_caching_force_connection_sharing(self,value: Optional[bool] = None) -> None:
        """
        Sets the contentCachingForceConnectionSharing property value. Forces internet connection sharing. contentCachingDisableConnectionSharing overrides this setting.
        Args:
            value: Value to set for the contentCachingForceConnectionSharing property.
        """
        self._content_caching_force_connection_sharing = value
    
    @property
    def content_caching_keep_awake(self,) -> Optional[bool]:
        """
        Gets the contentCachingKeepAwake property value. Prevent the device from sleeping if content caching is enabled.
        Returns: Optional[bool]
        """
        return self._content_caching_keep_awake
    
    @content_caching_keep_awake.setter
    def content_caching_keep_awake(self,value: Optional[bool] = None) -> None:
        """
        Sets the contentCachingKeepAwake property value. Prevent the device from sleeping if content caching is enabled.
        Args:
            value: Value to set for the contentCachingKeepAwake property.
        """
        self._content_caching_keep_awake = value
    
    @property
    def content_caching_log_client_identities(self,) -> Optional[bool]:
        """
        Gets the contentCachingLogClientIdentities property value. Enables logging of IP addresses and ports of clients that request cached content.
        Returns: Optional[bool]
        """
        return self._content_caching_log_client_identities
    
    @content_caching_log_client_identities.setter
    def content_caching_log_client_identities(self,value: Optional[bool] = None) -> None:
        """
        Sets the contentCachingLogClientIdentities property value. Enables logging of IP addresses and ports of clients that request cached content.
        Args:
            value: Value to set for the contentCachingLogClientIdentities property.
        """
        self._content_caching_log_client_identities = value
    
    @property
    def content_caching_max_size_bytes(self,) -> Optional[int]:
        """
        Gets the contentCachingMaxSizeBytes property value. The maximum number of bytes of disk space that will be used for the content cache. A value of 0 (default) indicates unlimited disk space.
        Returns: Optional[int]
        """
        return self._content_caching_max_size_bytes
    
    @content_caching_max_size_bytes.setter
    def content_caching_max_size_bytes(self,value: Optional[int] = None) -> None:
        """
        Sets the contentCachingMaxSizeBytes property value. The maximum number of bytes of disk space that will be used for the content cache. A value of 0 (default) indicates unlimited disk space.
        Args:
            value: Value to set for the contentCachingMaxSizeBytes property.
        """
        self._content_caching_max_size_bytes = value
    
    @property
    def content_caching_parents(self,) -> Optional[List[str]]:
        """
        Gets the contentCachingParents property value. A list of IP addresses representing parent content caches.
        Returns: Optional[List[str]]
        """
        return self._content_caching_parents
    
    @content_caching_parents.setter
    def content_caching_parents(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the contentCachingParents property value. A list of IP addresses representing parent content caches.
        Args:
            value: Value to set for the contentCachingParents property.
        """
        self._content_caching_parents = value
    
    @property
    def content_caching_parent_selection_policy(self,) -> Optional[mac_o_s_content_caching_parent_selection_policy.MacOSContentCachingParentSelectionPolicy]:
        """
        Gets the contentCachingParentSelectionPolicy property value. Determines how content caches select a parent cache.
        Returns: Optional[mac_o_s_content_caching_parent_selection_policy.MacOSContentCachingParentSelectionPolicy]
        """
        return self._content_caching_parent_selection_policy
    
    @content_caching_parent_selection_policy.setter
    def content_caching_parent_selection_policy(self,value: Optional[mac_o_s_content_caching_parent_selection_policy.MacOSContentCachingParentSelectionPolicy] = None) -> None:
        """
        Sets the contentCachingParentSelectionPolicy property value. Determines how content caches select a parent cache.
        Args:
            value: Value to set for the contentCachingParentSelectionPolicy property.
        """
        self._content_caching_parent_selection_policy = value
    
    @property
    def content_caching_peer_filter_ranges(self,) -> Optional[List[ip_range.IpRange]]:
        """
        Gets the contentCachingPeerFilterRanges property value. A list of custom IP ranges content caches will use to query for content from peers caches. This collection can contain a maximum of 500 elements.
        Returns: Optional[List[ip_range.IpRange]]
        """
        return self._content_caching_peer_filter_ranges
    
    @content_caching_peer_filter_ranges.setter
    def content_caching_peer_filter_ranges(self,value: Optional[List[ip_range.IpRange]] = None) -> None:
        """
        Sets the contentCachingPeerFilterRanges property value. A list of custom IP ranges content caches will use to query for content from peers caches. This collection can contain a maximum of 500 elements.
        Args:
            value: Value to set for the contentCachingPeerFilterRanges property.
        """
        self._content_caching_peer_filter_ranges = value
    
    @property
    def content_caching_peer_listen_ranges(self,) -> Optional[List[ip_range.IpRange]]:
        """
        Gets the contentCachingPeerListenRanges property value. A list of custom IP ranges content caches will use to listen for peer caches. This collection can contain a maximum of 500 elements.
        Returns: Optional[List[ip_range.IpRange]]
        """
        return self._content_caching_peer_listen_ranges
    
    @content_caching_peer_listen_ranges.setter
    def content_caching_peer_listen_ranges(self,value: Optional[List[ip_range.IpRange]] = None) -> None:
        """
        Sets the contentCachingPeerListenRanges property value. A list of custom IP ranges content caches will use to listen for peer caches. This collection can contain a maximum of 500 elements.
        Args:
            value: Value to set for the contentCachingPeerListenRanges property.
        """
        self._content_caching_peer_listen_ranges = value
    
    @property
    def content_caching_peer_policy(self,) -> Optional[mac_o_s_content_caching_peer_policy.MacOSContentCachingPeerPolicy]:
        """
        Gets the contentCachingPeerPolicy property value. Determines which content caches other content caches will peer with.
        Returns: Optional[mac_o_s_content_caching_peer_policy.MacOSContentCachingPeerPolicy]
        """
        return self._content_caching_peer_policy
    
    @content_caching_peer_policy.setter
    def content_caching_peer_policy(self,value: Optional[mac_o_s_content_caching_peer_policy.MacOSContentCachingPeerPolicy] = None) -> None:
        """
        Sets the contentCachingPeerPolicy property value. Determines which content caches other content caches will peer with.
        Args:
            value: Value to set for the contentCachingPeerPolicy property.
        """
        self._content_caching_peer_policy = value
    
    @property
    def content_caching_port(self,) -> Optional[int]:
        """
        Gets the contentCachingPort property value. Sets the port used for content caching. If the value is 0, a random available port will be selected. Valid values 0 to 65535
        Returns: Optional[int]
        """
        return self._content_caching_port
    
    @content_caching_port.setter
    def content_caching_port(self,value: Optional[int] = None) -> None:
        """
        Sets the contentCachingPort property value. Sets the port used for content caching. If the value is 0, a random available port will be selected. Valid values 0 to 65535
        Args:
            value: Value to set for the contentCachingPort property.
        """
        self._content_caching_port = value
    
    @property
    def content_caching_public_ranges(self,) -> Optional[List[ip_range.IpRange]]:
        """
        Gets the contentCachingPublicRanges property value. A list of custom IP ranges that Apple's content caching service should use to match clients to content caches. This collection can contain a maximum of 500 elements.
        Returns: Optional[List[ip_range.IpRange]]
        """
        return self._content_caching_public_ranges
    
    @content_caching_public_ranges.setter
    def content_caching_public_ranges(self,value: Optional[List[ip_range.IpRange]] = None) -> None:
        """
        Sets the contentCachingPublicRanges property value. A list of custom IP ranges that Apple's content caching service should use to match clients to content caches. This collection can contain a maximum of 500 elements.
        Args:
            value: Value to set for the contentCachingPublicRanges property.
        """
        self._content_caching_public_ranges = value
    
    @property
    def content_caching_show_alerts(self,) -> Optional[bool]:
        """
        Gets the contentCachingShowAlerts property value. Display content caching alerts as system notifications.
        Returns: Optional[bool]
        """
        return self._content_caching_show_alerts
    
    @content_caching_show_alerts.setter
    def content_caching_show_alerts(self,value: Optional[bool] = None) -> None:
        """
        Sets the contentCachingShowAlerts property value. Display content caching alerts as system notifications.
        Args:
            value: Value to set for the contentCachingShowAlerts property.
        """
        self._content_caching_show_alerts = value
    
    @property
    def content_caching_type(self,) -> Optional[mac_o_s_content_caching_type.MacOSContentCachingType]:
        """
        Gets the contentCachingType property value. Indicates the type of content allowed to be cached by Apple's content caching service.
        Returns: Optional[mac_o_s_content_caching_type.MacOSContentCachingType]
        """
        return self._content_caching_type
    
    @content_caching_type.setter
    def content_caching_type(self,value: Optional[mac_o_s_content_caching_type.MacOSContentCachingType] = None) -> None:
        """
        Sets the contentCachingType property value. Indicates the type of content allowed to be cached by Apple's content caching service.
        Args:
            value: Value to set for the contentCachingType property.
        """
        self._content_caching_type = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MacOSDeviceFeaturesConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MacOSDeviceFeaturesConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MacOSDeviceFeaturesConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "admin_show_host_info": lambda n : setattr(self, 'admin_show_host_info', n.get_bool_value()),
            "app_associated_domains": lambda n : setattr(self, 'app_associated_domains', n.get_collection_of_object_values(mac_o_s_associated_domains_item.MacOSAssociatedDomainsItem)),
            "associated_domains": lambda n : setattr(self, 'associated_domains', n.get_collection_of_object_values(key_value_pair.KeyValuePair)),
            "authorized_users_list_hidden": lambda n : setattr(self, 'authorized_users_list_hidden', n.get_bool_value()),
            "authorized_users_list_hide_admin_users": lambda n : setattr(self, 'authorized_users_list_hide_admin_users', n.get_bool_value()),
            "authorized_users_list_hide_local_users": lambda n : setattr(self, 'authorized_users_list_hide_local_users', n.get_bool_value()),
            "authorized_users_list_hide_mobile_accounts": lambda n : setattr(self, 'authorized_users_list_hide_mobile_accounts', n.get_bool_value()),
            "authorized_users_list_include_network_users": lambda n : setattr(self, 'authorized_users_list_include_network_users', n.get_bool_value()),
            "authorized_users_list_show_other_managed_users": lambda n : setattr(self, 'authorized_users_list_show_other_managed_users', n.get_bool_value()),
            "auto_launch_items": lambda n : setattr(self, 'auto_launch_items', n.get_collection_of_object_values(mac_o_s_launch_item.MacOSLaunchItem)),
            "console_access_disabled": lambda n : setattr(self, 'console_access_disabled', n.get_bool_value()),
            "content_caching_block_deletion": lambda n : setattr(self, 'content_caching_block_deletion', n.get_bool_value()),
            "content_caching_client_listen_ranges": lambda n : setattr(self, 'content_caching_client_listen_ranges', n.get_collection_of_object_values(ip_range.IpRange)),
            "content_caching_client_policy": lambda n : setattr(self, 'content_caching_client_policy', n.get_enum_value(mac_o_s_content_caching_client_policy.MacOSContentCachingClientPolicy)),
            "content_caching_data_path": lambda n : setattr(self, 'content_caching_data_path', n.get_str_value()),
            "content_caching_disable_connection_sharing": lambda n : setattr(self, 'content_caching_disable_connection_sharing', n.get_bool_value()),
            "content_caching_enabled": lambda n : setattr(self, 'content_caching_enabled', n.get_bool_value()),
            "content_caching_force_connection_sharing": lambda n : setattr(self, 'content_caching_force_connection_sharing', n.get_bool_value()),
            "content_caching_keep_awake": lambda n : setattr(self, 'content_caching_keep_awake', n.get_bool_value()),
            "content_caching_log_client_identities": lambda n : setattr(self, 'content_caching_log_client_identities', n.get_bool_value()),
            "content_caching_max_size_bytes": lambda n : setattr(self, 'content_caching_max_size_bytes', n.get_int_value()),
            "content_caching_parents": lambda n : setattr(self, 'content_caching_parents', n.get_collection_of_primitive_values(str)),
            "content_caching_parent_selection_policy": lambda n : setattr(self, 'content_caching_parent_selection_policy', n.get_enum_value(mac_o_s_content_caching_parent_selection_policy.MacOSContentCachingParentSelectionPolicy)),
            "content_caching_peer_filter_ranges": lambda n : setattr(self, 'content_caching_peer_filter_ranges', n.get_collection_of_object_values(ip_range.IpRange)),
            "content_caching_peer_listen_ranges": lambda n : setattr(self, 'content_caching_peer_listen_ranges', n.get_collection_of_object_values(ip_range.IpRange)),
            "content_caching_peer_policy": lambda n : setattr(self, 'content_caching_peer_policy', n.get_enum_value(mac_o_s_content_caching_peer_policy.MacOSContentCachingPeerPolicy)),
            "content_caching_port": lambda n : setattr(self, 'content_caching_port', n.get_int_value()),
            "content_caching_public_ranges": lambda n : setattr(self, 'content_caching_public_ranges', n.get_collection_of_object_values(ip_range.IpRange)),
            "content_caching_show_alerts": lambda n : setattr(self, 'content_caching_show_alerts', n.get_bool_value()),
            "content_caching_type": lambda n : setattr(self, 'content_caching_type', n.get_enum_value(mac_o_s_content_caching_type.MacOSContentCachingType)),
            "login_window_text": lambda n : setattr(self, 'login_window_text', n.get_str_value()),
            "log_out_disabled_while_logged_in": lambda n : setattr(self, 'log_out_disabled_while_logged_in', n.get_bool_value()),
            "mac_o_s_single_sign_on_extension": lambda n : setattr(self, 'mac_o_s_single_sign_on_extension', n.get_object_value(mac_o_s_single_sign_on_extension.MacOSSingleSignOnExtension)),
            "power_off_disabled_while_logged_in": lambda n : setattr(self, 'power_off_disabled_while_logged_in', n.get_bool_value()),
            "restart_disabled": lambda n : setattr(self, 'restart_disabled', n.get_bool_value()),
            "restart_disabled_while_logged_in": lambda n : setattr(self, 'restart_disabled_while_logged_in', n.get_bool_value()),
            "screen_lock_disable_immediate": lambda n : setattr(self, 'screen_lock_disable_immediate', n.get_bool_value()),
            "shut_down_disabled": lambda n : setattr(self, 'shut_down_disabled', n.get_bool_value()),
            "shut_down_disabled_while_logged_in": lambda n : setattr(self, 'shut_down_disabled_while_logged_in', n.get_bool_value()),
            "single_sign_on_extension": lambda n : setattr(self, 'single_sign_on_extension', n.get_object_value(single_sign_on_extension.SingleSignOnExtension)),
            "single_sign_on_extension_pkinit_certificate": lambda n : setattr(self, 'single_sign_on_extension_pkinit_certificate', n.get_object_value(mac_o_s_certificate_profile_base.MacOSCertificateProfileBase)),
            "sleep_disabled": lambda n : setattr(self, 'sleep_disabled', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def login_window_text(self,) -> Optional[str]:
        """
        Gets the loginWindowText property value. Custom text to be displayed on the login window.
        Returns: Optional[str]
        """
        return self._login_window_text
    
    @login_window_text.setter
    def login_window_text(self,value: Optional[str] = None) -> None:
        """
        Sets the loginWindowText property value. Custom text to be displayed on the login window.
        Args:
            value: Value to set for the loginWindowText property.
        """
        self._login_window_text = value
    
    @property
    def log_out_disabled_while_logged_in(self,) -> Optional[bool]:
        """
        Gets the logOutDisabledWhileLoggedIn property value. Whether the Log Out menu item on the login window will be disabled while the user is logged in.
        Returns: Optional[bool]
        """
        return self._log_out_disabled_while_logged_in
    
    @log_out_disabled_while_logged_in.setter
    def log_out_disabled_while_logged_in(self,value: Optional[bool] = None) -> None:
        """
        Sets the logOutDisabledWhileLoggedIn property value. Whether the Log Out menu item on the login window will be disabled while the user is logged in.
        Args:
            value: Value to set for the logOutDisabledWhileLoggedIn property.
        """
        self._log_out_disabled_while_logged_in = value
    
    @property
    def mac_o_s_single_sign_on_extension(self,) -> Optional[mac_o_s_single_sign_on_extension.MacOSSingleSignOnExtension]:
        """
        Gets the macOSSingleSignOnExtension property value. Gets or sets a single sign-on extension profile.
        Returns: Optional[mac_o_s_single_sign_on_extension.MacOSSingleSignOnExtension]
        """
        return self._mac_o_s_single_sign_on_extension
    
    @mac_o_s_single_sign_on_extension.setter
    def mac_o_s_single_sign_on_extension(self,value: Optional[mac_o_s_single_sign_on_extension.MacOSSingleSignOnExtension] = None) -> None:
        """
        Sets the macOSSingleSignOnExtension property value. Gets or sets a single sign-on extension profile.
        Args:
            value: Value to set for the macOSSingleSignOnExtension property.
        """
        self._mac_o_s_single_sign_on_extension = value
    
    @property
    def power_off_disabled_while_logged_in(self,) -> Optional[bool]:
        """
        Gets the powerOffDisabledWhileLoggedIn property value. Whether the Power Off menu item on the login window will be disabled while the user is logged in.
        Returns: Optional[bool]
        """
        return self._power_off_disabled_while_logged_in
    
    @power_off_disabled_while_logged_in.setter
    def power_off_disabled_while_logged_in(self,value: Optional[bool] = None) -> None:
        """
        Sets the powerOffDisabledWhileLoggedIn property value. Whether the Power Off menu item on the login window will be disabled while the user is logged in.
        Args:
            value: Value to set for the powerOffDisabledWhileLoggedIn property.
        """
        self._power_off_disabled_while_logged_in = value
    
    @property
    def restart_disabled(self,) -> Optional[bool]:
        """
        Gets the restartDisabled property value. Whether to hide the Restart button item on the login window.
        Returns: Optional[bool]
        """
        return self._restart_disabled
    
    @restart_disabled.setter
    def restart_disabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the restartDisabled property value. Whether to hide the Restart button item on the login window.
        Args:
            value: Value to set for the restartDisabled property.
        """
        self._restart_disabled = value
    
    @property
    def restart_disabled_while_logged_in(self,) -> Optional[bool]:
        """
        Gets the restartDisabledWhileLoggedIn property value. Whether the Restart menu item on the login window will be disabled while the user is logged in.
        Returns: Optional[bool]
        """
        return self._restart_disabled_while_logged_in
    
    @restart_disabled_while_logged_in.setter
    def restart_disabled_while_logged_in(self,value: Optional[bool] = None) -> None:
        """
        Sets the restartDisabledWhileLoggedIn property value. Whether the Restart menu item on the login window will be disabled while the user is logged in.
        Args:
            value: Value to set for the restartDisabledWhileLoggedIn property.
        """
        self._restart_disabled_while_logged_in = value
    
    @property
    def screen_lock_disable_immediate(self,) -> Optional[bool]:
        """
        Gets the screenLockDisableImmediate property value. Whether to disable the immediate screen lock functions.
        Returns: Optional[bool]
        """
        return self._screen_lock_disable_immediate
    
    @screen_lock_disable_immediate.setter
    def screen_lock_disable_immediate(self,value: Optional[bool] = None) -> None:
        """
        Sets the screenLockDisableImmediate property value. Whether to disable the immediate screen lock functions.
        Args:
            value: Value to set for the screenLockDisableImmediate property.
        """
        self._screen_lock_disable_immediate = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_bool_value("adminShowHostInfo", self.admin_show_host_info)
        writer.write_collection_of_object_values("appAssociatedDomains", self.app_associated_domains)
        writer.write_collection_of_object_values("associatedDomains", self.associated_domains)
        writer.write_bool_value("authorizedUsersListHidden", self.authorized_users_list_hidden)
        writer.write_bool_value("authorizedUsersListHideAdminUsers", self.authorized_users_list_hide_admin_users)
        writer.write_bool_value("authorizedUsersListHideLocalUsers", self.authorized_users_list_hide_local_users)
        writer.write_bool_value("authorizedUsersListHideMobileAccounts", self.authorized_users_list_hide_mobile_accounts)
        writer.write_bool_value("authorizedUsersListIncludeNetworkUsers", self.authorized_users_list_include_network_users)
        writer.write_bool_value("authorizedUsersListShowOtherManagedUsers", self.authorized_users_list_show_other_managed_users)
        writer.write_collection_of_object_values("autoLaunchItems", self.auto_launch_items)
        writer.write_bool_value("consoleAccessDisabled", self.console_access_disabled)
        writer.write_bool_value("contentCachingBlockDeletion", self.content_caching_block_deletion)
        writer.write_collection_of_object_values("contentCachingClientListenRanges", self.content_caching_client_listen_ranges)
        writer.write_enum_value("contentCachingClientPolicy", self.content_caching_client_policy)
        writer.write_str_value("contentCachingDataPath", self.content_caching_data_path)
        writer.write_bool_value("contentCachingDisableConnectionSharing", self.content_caching_disable_connection_sharing)
        writer.write_bool_value("contentCachingEnabled", self.content_caching_enabled)
        writer.write_bool_value("contentCachingForceConnectionSharing", self.content_caching_force_connection_sharing)
        writer.write_bool_value("contentCachingKeepAwake", self.content_caching_keep_awake)
        writer.write_bool_value("contentCachingLogClientIdentities", self.content_caching_log_client_identities)
        writer.write_int_value("contentCachingMaxSizeBytes", self.content_caching_max_size_bytes)
        writer.write_collection_of_primitive_values("contentCachingParents", self.content_caching_parents)
        writer.write_enum_value("contentCachingParentSelectionPolicy", self.content_caching_parent_selection_policy)
        writer.write_collection_of_object_values("contentCachingPeerFilterRanges", self.content_caching_peer_filter_ranges)
        writer.write_collection_of_object_values("contentCachingPeerListenRanges", self.content_caching_peer_listen_ranges)
        writer.write_enum_value("contentCachingPeerPolicy", self.content_caching_peer_policy)
        writer.write_int_value("contentCachingPort", self.content_caching_port)
        writer.write_collection_of_object_values("contentCachingPublicRanges", self.content_caching_public_ranges)
        writer.write_bool_value("contentCachingShowAlerts", self.content_caching_show_alerts)
        writer.write_enum_value("contentCachingType", self.content_caching_type)
        writer.write_str_value("loginWindowText", self.login_window_text)
        writer.write_bool_value("logOutDisabledWhileLoggedIn", self.log_out_disabled_while_logged_in)
        writer.write_object_value("macOSSingleSignOnExtension", self.mac_o_s_single_sign_on_extension)
        writer.write_bool_value("powerOffDisabledWhileLoggedIn", self.power_off_disabled_while_logged_in)
        writer.write_bool_value("restartDisabled", self.restart_disabled)
        writer.write_bool_value("restartDisabledWhileLoggedIn", self.restart_disabled_while_logged_in)
        writer.write_bool_value("screenLockDisableImmediate", self.screen_lock_disable_immediate)
        writer.write_bool_value("shutDownDisabled", self.shut_down_disabled)
        writer.write_bool_value("shutDownDisabledWhileLoggedIn", self.shut_down_disabled_while_logged_in)
        writer.write_object_value("singleSignOnExtension", self.single_sign_on_extension)
        writer.write_object_value("singleSignOnExtensionPkinitCertificate", self.single_sign_on_extension_pkinit_certificate)
        writer.write_bool_value("sleepDisabled", self.sleep_disabled)
    
    @property
    def shut_down_disabled(self,) -> Optional[bool]:
        """
        Gets the shutDownDisabled property value. Whether to hide the Shut Down button item on the login window.
        Returns: Optional[bool]
        """
        return self._shut_down_disabled
    
    @shut_down_disabled.setter
    def shut_down_disabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the shutDownDisabled property value. Whether to hide the Shut Down button item on the login window.
        Args:
            value: Value to set for the shutDownDisabled property.
        """
        self._shut_down_disabled = value
    
    @property
    def shut_down_disabled_while_logged_in(self,) -> Optional[bool]:
        """
        Gets the shutDownDisabledWhileLoggedIn property value. Whether the Shut Down menu item on the login window will be disabled while the user is logged in.
        Returns: Optional[bool]
        """
        return self._shut_down_disabled_while_logged_in
    
    @shut_down_disabled_while_logged_in.setter
    def shut_down_disabled_while_logged_in(self,value: Optional[bool] = None) -> None:
        """
        Sets the shutDownDisabledWhileLoggedIn property value. Whether the Shut Down menu item on the login window will be disabled while the user is logged in.
        Args:
            value: Value to set for the shutDownDisabledWhileLoggedIn property.
        """
        self._shut_down_disabled_while_logged_in = value
    
    @property
    def single_sign_on_extension(self,) -> Optional[single_sign_on_extension.SingleSignOnExtension]:
        """
        Gets the singleSignOnExtension property value. Gets or sets a single sign-on extension profile. Deprecated: use MacOSSingleSignOnExtension instead.
        Returns: Optional[single_sign_on_extension.SingleSignOnExtension]
        """
        return self._single_sign_on_extension
    
    @single_sign_on_extension.setter
    def single_sign_on_extension(self,value: Optional[single_sign_on_extension.SingleSignOnExtension] = None) -> None:
        """
        Sets the singleSignOnExtension property value. Gets or sets a single sign-on extension profile. Deprecated: use MacOSSingleSignOnExtension instead.
        Args:
            value: Value to set for the singleSignOnExtension property.
        """
        self._single_sign_on_extension = value
    
    @property
    def single_sign_on_extension_pkinit_certificate(self,) -> Optional[mac_o_s_certificate_profile_base.MacOSCertificateProfileBase]:
        """
        Gets the singleSignOnExtensionPkinitCertificate property value. PKINIT Certificate for the authentication with single sign-on extensions.
        Returns: Optional[mac_o_s_certificate_profile_base.MacOSCertificateProfileBase]
        """
        return self._single_sign_on_extension_pkinit_certificate
    
    @single_sign_on_extension_pkinit_certificate.setter
    def single_sign_on_extension_pkinit_certificate(self,value: Optional[mac_o_s_certificate_profile_base.MacOSCertificateProfileBase] = None) -> None:
        """
        Sets the singleSignOnExtensionPkinitCertificate property value. PKINIT Certificate for the authentication with single sign-on extensions.
        Args:
            value: Value to set for the singleSignOnExtensionPkinitCertificate property.
        """
        self._single_sign_on_extension_pkinit_certificate = value
    
    @property
    def sleep_disabled(self,) -> Optional[bool]:
        """
        Gets the sleepDisabled property value. Whether to hide the Sleep menu item on the login window.
        Returns: Optional[bool]
        """
        return self._sleep_disabled
    
    @sleep_disabled.setter
    def sleep_disabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the sleepDisabled property value. Whether to hide the Sleep menu item on the login window.
        Args:
            value: Value to set for the sleepDisabled property.
        """
        self._sleep_disabled = value
    

