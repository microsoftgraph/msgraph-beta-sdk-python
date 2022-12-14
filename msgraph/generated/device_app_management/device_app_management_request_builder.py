from __future__ import annotations
from dataclasses import dataclass
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

android_managed_app_protections_request_builder = lazy_import('msgraph.generated.device_app_management.android_managed_app_protections.android_managed_app_protections_request_builder')
android_managed_app_protection_item_request_builder = lazy_import('msgraph.generated.device_app_management.android_managed_app_protections.item.android_managed_app_protection_item_request_builder')
default_managed_app_protections_request_builder = lazy_import('msgraph.generated.device_app_management.default_managed_app_protections.default_managed_app_protections_request_builder')
default_managed_app_protection_item_request_builder = lazy_import('msgraph.generated.device_app_management.default_managed_app_protections.item.default_managed_app_protection_item_request_builder')
device_app_management_tasks_request_builder = lazy_import('msgraph.generated.device_app_management.device_app_management_tasks.device_app_management_tasks_request_builder')
device_app_management_task_item_request_builder = lazy_import('msgraph.generated.device_app_management.device_app_management_tasks.item.device_app_management_task_item_request_builder')
enterprise_code_signing_certificates_request_builder = lazy_import('msgraph.generated.device_app_management.enterprise_code_signing_certificates.enterprise_code_signing_certificates_request_builder')
enterprise_code_signing_certificate_item_request_builder = lazy_import('msgraph.generated.device_app_management.enterprise_code_signing_certificates.item.enterprise_code_signing_certificate_item_request_builder')
ios_lob_app_provisioning_configurations_request_builder = lazy_import('msgraph.generated.device_app_management.ios_lob_app_provisioning_configurations.ios_lob_app_provisioning_configurations_request_builder')
ios_lob_app_provisioning_configuration_item_request_builder = lazy_import('msgraph.generated.device_app_management.ios_lob_app_provisioning_configurations.item.ios_lob_app_provisioning_configuration_item_request_builder')
ios_managed_app_protections_request_builder = lazy_import('msgraph.generated.device_app_management.ios_managed_app_protections.ios_managed_app_protections_request_builder')
ios_managed_app_protection_item_request_builder = lazy_import('msgraph.generated.device_app_management.ios_managed_app_protections.item.ios_managed_app_protection_item_request_builder')
managed_app_policies_request_builder = lazy_import('msgraph.generated.device_app_management.managed_app_policies.managed_app_policies_request_builder')
managed_app_policy_item_request_builder = lazy_import('msgraph.generated.device_app_management.managed_app_policies.item.managed_app_policy_item_request_builder')
managed_app_registrations_request_builder = lazy_import('msgraph.generated.device_app_management.managed_app_registrations.managed_app_registrations_request_builder')
managed_app_registration_item_request_builder = lazy_import('msgraph.generated.device_app_management.managed_app_registrations.item.managed_app_registration_item_request_builder')
managed_app_statuses_request_builder = lazy_import('msgraph.generated.device_app_management.managed_app_statuses.managed_app_statuses_request_builder')
managed_app_status_item_request_builder = lazy_import('msgraph.generated.device_app_management.managed_app_statuses.item.managed_app_status_item_request_builder')
managed_e_book_categories_request_builder = lazy_import('msgraph.generated.device_app_management.managed_e_book_categories.managed_e_book_categories_request_builder')
managed_e_book_category_item_request_builder = lazy_import('msgraph.generated.device_app_management.managed_e_book_categories.item.managed_e_book_category_item_request_builder')
managed_e_books_request_builder = lazy_import('msgraph.generated.device_app_management.managed_e_books.managed_e_books_request_builder')
managed_e_book_item_request_builder = lazy_import('msgraph.generated.device_app_management.managed_e_books.item.managed_e_book_item_request_builder')
mdm_windows_information_protection_policies_request_builder = lazy_import('msgraph.generated.device_app_management.mdm_windows_information_protection_policies.mdm_windows_information_protection_policies_request_builder')
mdm_windows_information_protection_policy_item_request_builder = lazy_import('msgraph.generated.device_app_management.mdm_windows_information_protection_policies.item.mdm_windows_information_protection_policy_item_request_builder')
mobile_app_categories_request_builder = lazy_import('msgraph.generated.device_app_management.mobile_app_categories.mobile_app_categories_request_builder')
mobile_app_category_item_request_builder = lazy_import('msgraph.generated.device_app_management.mobile_app_categories.item.mobile_app_category_item_request_builder')
mobile_app_configurations_request_builder = lazy_import('msgraph.generated.device_app_management.mobile_app_configurations.mobile_app_configurations_request_builder')
managed_device_mobile_app_configuration_item_request_builder = lazy_import('msgraph.generated.device_app_management.mobile_app_configurations.item.managed_device_mobile_app_configuration_item_request_builder')
mobile_apps_request_builder = lazy_import('msgraph.generated.device_app_management.mobile_apps.mobile_apps_request_builder')
mobile_app_item_request_builder = lazy_import('msgraph.generated.device_app_management.mobile_apps.item.mobile_app_item_request_builder')
policy_sets_request_builder = lazy_import('msgraph.generated.device_app_management.policy_sets.policy_sets_request_builder')
policy_set_item_request_builder = lazy_import('msgraph.generated.device_app_management.policy_sets.item.policy_set_item_request_builder')
side_loading_keys_request_builder = lazy_import('msgraph.generated.device_app_management.side_loading_keys.side_loading_keys_request_builder')
side_loading_key_item_request_builder = lazy_import('msgraph.generated.device_app_management.side_loading_keys.item.side_loading_key_item_request_builder')
symantec_code_signing_certificate_request_builder = lazy_import('msgraph.generated.device_app_management.symantec_code_signing_certificate.symantec_code_signing_certificate_request_builder')
sync_microsoft_store_for_business_apps_request_builder = lazy_import('msgraph.generated.device_app_management.sync_microsoft_store_for_business_apps.sync_microsoft_store_for_business_apps_request_builder')
targeted_managed_app_configurations_request_builder = lazy_import('msgraph.generated.device_app_management.targeted_managed_app_configurations.targeted_managed_app_configurations_request_builder')
targeted_managed_app_configuration_item_request_builder = lazy_import('msgraph.generated.device_app_management.targeted_managed_app_configurations.item.targeted_managed_app_configuration_item_request_builder')
vpp_tokens_request_builder = lazy_import('msgraph.generated.device_app_management.vpp_tokens.vpp_tokens_request_builder')
vpp_token_item_request_builder = lazy_import('msgraph.generated.device_app_management.vpp_tokens.item.vpp_token_item_request_builder')
wdac_supplemental_policies_request_builder = lazy_import('msgraph.generated.device_app_management.wdac_supplemental_policies.wdac_supplemental_policies_request_builder')
windows_defender_application_control_supplemental_policy_item_request_builder = lazy_import('msgraph.generated.device_app_management.wdac_supplemental_policies.item.windows_defender_application_control_supplemental_policy_item_request_builder')
windows_information_protection_device_registrations_request_builder = lazy_import('msgraph.generated.device_app_management.windows_information_protection_device_registrations.windows_information_protection_device_registrations_request_builder')
windows_information_protection_device_registration_item_request_builder = lazy_import('msgraph.generated.device_app_management.windows_information_protection_device_registrations.item.windows_information_protection_device_registration_item_request_builder')
windows_information_protection_policies_request_builder = lazy_import('msgraph.generated.device_app_management.windows_information_protection_policies.windows_information_protection_policies_request_builder')
windows_information_protection_policy_item_request_builder = lazy_import('msgraph.generated.device_app_management.windows_information_protection_policies.item.windows_information_protection_policy_item_request_builder')
windows_information_protection_wipe_actions_request_builder = lazy_import('msgraph.generated.device_app_management.windows_information_protection_wipe_actions.windows_information_protection_wipe_actions_request_builder')
windows_information_protection_wipe_action_item_request_builder = lazy_import('msgraph.generated.device_app_management.windows_information_protection_wipe_actions.item.windows_information_protection_wipe_action_item_request_builder')
windows_managed_app_protections_request_builder = lazy_import('msgraph.generated.device_app_management.windows_managed_app_protections.windows_managed_app_protections_request_builder')
windows_managed_app_protection_item_request_builder = lazy_import('msgraph.generated.device_app_management.windows_managed_app_protections.item.windows_managed_app_protection_item_request_builder')
windows_management_app_request_builder = lazy_import('msgraph.generated.device_app_management.windows_management_app.windows_management_app_request_builder')
device_app_management = lazy_import('msgraph.generated.models.device_app_management')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class DeviceAppManagementRequestBuilder():
    """
    Provides operations to manage the deviceAppManagement singleton.
    """
    @property
    def android_managed_app_protections(self) -> android_managed_app_protections_request_builder.AndroidManagedAppProtectionsRequestBuilder:
        """
        Provides operations to manage the androidManagedAppProtections property of the microsoft.graph.deviceAppManagement entity.
        """
        return android_managed_app_protections_request_builder.AndroidManagedAppProtectionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def default_managed_app_protections(self) -> default_managed_app_protections_request_builder.DefaultManagedAppProtectionsRequestBuilder:
        """
        Provides operations to manage the defaultManagedAppProtections property of the microsoft.graph.deviceAppManagement entity.
        """
        return default_managed_app_protections_request_builder.DefaultManagedAppProtectionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_app_management_tasks(self) -> device_app_management_tasks_request_builder.DeviceAppManagementTasksRequestBuilder:
        """
        Provides operations to manage the deviceAppManagementTasks property of the microsoft.graph.deviceAppManagement entity.
        """
        return device_app_management_tasks_request_builder.DeviceAppManagementTasksRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def enterprise_code_signing_certificates(self) -> enterprise_code_signing_certificates_request_builder.EnterpriseCodeSigningCertificatesRequestBuilder:
        """
        Provides operations to manage the enterpriseCodeSigningCertificates property of the microsoft.graph.deviceAppManagement entity.
        """
        return enterprise_code_signing_certificates_request_builder.EnterpriseCodeSigningCertificatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def ios_lob_app_provisioning_configurations(self) -> ios_lob_app_provisioning_configurations_request_builder.IosLobAppProvisioningConfigurationsRequestBuilder:
        """
        Provides operations to manage the iosLobAppProvisioningConfigurations property of the microsoft.graph.deviceAppManagement entity.
        """
        return ios_lob_app_provisioning_configurations_request_builder.IosLobAppProvisioningConfigurationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def ios_managed_app_protections(self) -> ios_managed_app_protections_request_builder.IosManagedAppProtectionsRequestBuilder:
        """
        Provides operations to manage the iosManagedAppProtections property of the microsoft.graph.deviceAppManagement entity.
        """
        return ios_managed_app_protections_request_builder.IosManagedAppProtectionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def managed_app_policies(self) -> managed_app_policies_request_builder.ManagedAppPoliciesRequestBuilder:
        """
        Provides operations to manage the managedAppPolicies property of the microsoft.graph.deviceAppManagement entity.
        """
        return managed_app_policies_request_builder.ManagedAppPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def managed_app_registrations(self) -> managed_app_registrations_request_builder.ManagedAppRegistrationsRequestBuilder:
        """
        Provides operations to manage the managedAppRegistrations property of the microsoft.graph.deviceAppManagement entity.
        """
        return managed_app_registrations_request_builder.ManagedAppRegistrationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def managed_app_statuses(self) -> managed_app_statuses_request_builder.ManagedAppStatusesRequestBuilder:
        """
        Provides operations to manage the managedAppStatuses property of the microsoft.graph.deviceAppManagement entity.
        """
        return managed_app_statuses_request_builder.ManagedAppStatusesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def managed_e_book_categories(self) -> managed_e_book_categories_request_builder.ManagedEBookCategoriesRequestBuilder:
        """
        Provides operations to manage the managedEBookCategories property of the microsoft.graph.deviceAppManagement entity.
        """
        return managed_e_book_categories_request_builder.ManagedEBookCategoriesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def managed_e_books(self) -> managed_e_books_request_builder.ManagedEBooksRequestBuilder:
        """
        Provides operations to manage the managedEBooks property of the microsoft.graph.deviceAppManagement entity.
        """
        return managed_e_books_request_builder.ManagedEBooksRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mdm_windows_information_protection_policies(self) -> mdm_windows_information_protection_policies_request_builder.MdmWindowsInformationProtectionPoliciesRequestBuilder:
        """
        Provides operations to manage the mdmWindowsInformationProtectionPolicies property of the microsoft.graph.deviceAppManagement entity.
        """
        return mdm_windows_information_protection_policies_request_builder.MdmWindowsInformationProtectionPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mobile_app_categories(self) -> mobile_app_categories_request_builder.MobileAppCategoriesRequestBuilder:
        """
        Provides operations to manage the mobileAppCategories property of the microsoft.graph.deviceAppManagement entity.
        """
        return mobile_app_categories_request_builder.MobileAppCategoriesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mobile_app_configurations(self) -> mobile_app_configurations_request_builder.MobileAppConfigurationsRequestBuilder:
        """
        Provides operations to manage the mobileAppConfigurations property of the microsoft.graph.deviceAppManagement entity.
        """
        return mobile_app_configurations_request_builder.MobileAppConfigurationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mobile_apps(self) -> mobile_apps_request_builder.MobileAppsRequestBuilder:
        """
        Provides operations to manage the mobileApps property of the microsoft.graph.deviceAppManagement entity.
        """
        return mobile_apps_request_builder.MobileAppsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def policy_sets(self) -> policy_sets_request_builder.PolicySetsRequestBuilder:
        """
        Provides operations to manage the policySets property of the microsoft.graph.deviceAppManagement entity.
        """
        return policy_sets_request_builder.PolicySetsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def side_loading_keys(self) -> side_loading_keys_request_builder.SideLoadingKeysRequestBuilder:
        """
        Provides operations to manage the sideLoadingKeys property of the microsoft.graph.deviceAppManagement entity.
        """
        return side_loading_keys_request_builder.SideLoadingKeysRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def symantec_code_signing_certificate(self) -> symantec_code_signing_certificate_request_builder.SymantecCodeSigningCertificateRequestBuilder:
        """
        Provides operations to manage the symantecCodeSigningCertificate property of the microsoft.graph.deviceAppManagement entity.
        """
        return symantec_code_signing_certificate_request_builder.SymantecCodeSigningCertificateRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sync_microsoft_store_for_business_apps(self) -> sync_microsoft_store_for_business_apps_request_builder.SyncMicrosoftStoreForBusinessAppsRequestBuilder:
        """
        Provides operations to call the syncMicrosoftStoreForBusinessApps method.
        """
        return sync_microsoft_store_for_business_apps_request_builder.SyncMicrosoftStoreForBusinessAppsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def targeted_managed_app_configurations(self) -> targeted_managed_app_configurations_request_builder.TargetedManagedAppConfigurationsRequestBuilder:
        """
        Provides operations to manage the targetedManagedAppConfigurations property of the microsoft.graph.deviceAppManagement entity.
        """
        return targeted_managed_app_configurations_request_builder.TargetedManagedAppConfigurationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def vpp_tokens(self) -> vpp_tokens_request_builder.VppTokensRequestBuilder:
        """
        Provides operations to manage the vppTokens property of the microsoft.graph.deviceAppManagement entity.
        """
        return vpp_tokens_request_builder.VppTokensRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def wdac_supplemental_policies(self) -> wdac_supplemental_policies_request_builder.WdacSupplementalPoliciesRequestBuilder:
        """
        Provides operations to manage the wdacSupplementalPolicies property of the microsoft.graph.deviceAppManagement entity.
        """
        return wdac_supplemental_policies_request_builder.WdacSupplementalPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def windows_information_protection_device_registrations(self) -> windows_information_protection_device_registrations_request_builder.WindowsInformationProtectionDeviceRegistrationsRequestBuilder:
        """
        Provides operations to manage the windowsInformationProtectionDeviceRegistrations property of the microsoft.graph.deviceAppManagement entity.
        """
        return windows_information_protection_device_registrations_request_builder.WindowsInformationProtectionDeviceRegistrationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def windows_information_protection_policies(self) -> windows_information_protection_policies_request_builder.WindowsInformationProtectionPoliciesRequestBuilder:
        """
        Provides operations to manage the windowsInformationProtectionPolicies property of the microsoft.graph.deviceAppManagement entity.
        """
        return windows_information_protection_policies_request_builder.WindowsInformationProtectionPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def windows_information_protection_wipe_actions(self) -> windows_information_protection_wipe_actions_request_builder.WindowsInformationProtectionWipeActionsRequestBuilder:
        """
        Provides operations to manage the windowsInformationProtectionWipeActions property of the microsoft.graph.deviceAppManagement entity.
        """
        return windows_information_protection_wipe_actions_request_builder.WindowsInformationProtectionWipeActionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def windows_managed_app_protections(self) -> windows_managed_app_protections_request_builder.WindowsManagedAppProtectionsRequestBuilder:
        """
        Provides operations to manage the windowsManagedAppProtections property of the microsoft.graph.deviceAppManagement entity.
        """
        return windows_managed_app_protections_request_builder.WindowsManagedAppProtectionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def windows_management_app(self) -> windows_management_app_request_builder.WindowsManagementAppRequestBuilder:
        """
        Provides operations to manage the windowsManagementApp property of the microsoft.graph.deviceAppManagement entity.
        """
        return windows_management_app_request_builder.WindowsManagementAppRequestBuilder(self.request_adapter, self.path_parameters)
    
    def android_managed_app_protections_by_id(self,id: str) -> android_managed_app_protection_item_request_builder.AndroidManagedAppProtectionItemRequestBuilder:
        """
        Provides operations to manage the androidManagedAppProtections property of the microsoft.graph.deviceAppManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: android_managed_app_protection_item_request_builder.AndroidManagedAppProtectionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["androidManagedAppProtection%2Did"] = id
        return android_managed_app_protection_item_request_builder.AndroidManagedAppProtectionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new DeviceAppManagementRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/deviceAppManagement{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def default_managed_app_protections_by_id(self,id: str) -> default_managed_app_protection_item_request_builder.DefaultManagedAppProtectionItemRequestBuilder:
        """
        Provides operations to manage the defaultManagedAppProtections property of the microsoft.graph.deviceAppManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: default_managed_app_protection_item_request_builder.DefaultManagedAppProtectionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["defaultManagedAppProtection%2Did"] = id
        return default_managed_app_protection_item_request_builder.DefaultManagedAppProtectionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def device_app_management_tasks_by_id(self,id: str) -> device_app_management_task_item_request_builder.DeviceAppManagementTaskItemRequestBuilder:
        """
        Provides operations to manage the deviceAppManagementTasks property of the microsoft.graph.deviceAppManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: device_app_management_task_item_request_builder.DeviceAppManagementTaskItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["deviceAppManagementTask%2Did"] = id
        return device_app_management_task_item_request_builder.DeviceAppManagementTaskItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def enterprise_code_signing_certificates_by_id(self,id: str) -> enterprise_code_signing_certificate_item_request_builder.EnterpriseCodeSigningCertificateItemRequestBuilder:
        """
        Provides operations to manage the enterpriseCodeSigningCertificates property of the microsoft.graph.deviceAppManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: enterprise_code_signing_certificate_item_request_builder.EnterpriseCodeSigningCertificateItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["enterpriseCodeSigningCertificate%2Did"] = id
        return enterprise_code_signing_certificate_item_request_builder.EnterpriseCodeSigningCertificateItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[DeviceAppManagementRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[device_app_management.DeviceAppManagement]:
        """
        Get deviceAppManagement
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[device_app_management.DeviceAppManagement]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, device_app_management.DeviceAppManagement, response_handler, error_mapping)
    
    def ios_lob_app_provisioning_configurations_by_id(self,id: str) -> ios_lob_app_provisioning_configuration_item_request_builder.IosLobAppProvisioningConfigurationItemRequestBuilder:
        """
        Provides operations to manage the iosLobAppProvisioningConfigurations property of the microsoft.graph.deviceAppManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: ios_lob_app_provisioning_configuration_item_request_builder.IosLobAppProvisioningConfigurationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["iosLobAppProvisioningConfiguration%2Did"] = id
        return ios_lob_app_provisioning_configuration_item_request_builder.IosLobAppProvisioningConfigurationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def ios_managed_app_protections_by_id(self,id: str) -> ios_managed_app_protection_item_request_builder.IosManagedAppProtectionItemRequestBuilder:
        """
        Provides operations to manage the iosManagedAppProtections property of the microsoft.graph.deviceAppManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: ios_managed_app_protection_item_request_builder.IosManagedAppProtectionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["iosManagedAppProtection%2Did"] = id
        return ios_managed_app_protection_item_request_builder.IosManagedAppProtectionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def managed_app_policies_by_id(self,id: str) -> managed_app_policy_item_request_builder.ManagedAppPolicyItemRequestBuilder:
        """
        Provides operations to manage the managedAppPolicies property of the microsoft.graph.deviceAppManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: managed_app_policy_item_request_builder.ManagedAppPolicyItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["managedAppPolicy%2Did"] = id
        return managed_app_policy_item_request_builder.ManagedAppPolicyItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def managed_app_registrations_by_id(self,id: str) -> managed_app_registration_item_request_builder.ManagedAppRegistrationItemRequestBuilder:
        """
        Provides operations to manage the managedAppRegistrations property of the microsoft.graph.deviceAppManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: managed_app_registration_item_request_builder.ManagedAppRegistrationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["managedAppRegistration%2Did"] = id
        return managed_app_registration_item_request_builder.ManagedAppRegistrationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def managed_app_statuses_by_id(self,id: str) -> managed_app_status_item_request_builder.ManagedAppStatusItemRequestBuilder:
        """
        Provides operations to manage the managedAppStatuses property of the microsoft.graph.deviceAppManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: managed_app_status_item_request_builder.ManagedAppStatusItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["managedAppStatus%2Did"] = id
        return managed_app_status_item_request_builder.ManagedAppStatusItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def managed_e_book_categories_by_id(self,id: str) -> managed_e_book_category_item_request_builder.ManagedEBookCategoryItemRequestBuilder:
        """
        Provides operations to manage the managedEBookCategories property of the microsoft.graph.deviceAppManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: managed_e_book_category_item_request_builder.ManagedEBookCategoryItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["managedEBookCategory%2Did"] = id
        return managed_e_book_category_item_request_builder.ManagedEBookCategoryItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def managed_e_books_by_id(self,id: str) -> managed_e_book_item_request_builder.ManagedEBookItemRequestBuilder:
        """
        Provides operations to manage the managedEBooks property of the microsoft.graph.deviceAppManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: managed_e_book_item_request_builder.ManagedEBookItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["managedEBook%2Did"] = id
        return managed_e_book_item_request_builder.ManagedEBookItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def mdm_windows_information_protection_policies_by_id(self,id: str) -> mdm_windows_information_protection_policy_item_request_builder.MdmWindowsInformationProtectionPolicyItemRequestBuilder:
        """
        Provides operations to manage the mdmWindowsInformationProtectionPolicies property of the microsoft.graph.deviceAppManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: mdm_windows_information_protection_policy_item_request_builder.MdmWindowsInformationProtectionPolicyItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["mdmWindowsInformationProtectionPolicy%2Did"] = id
        return mdm_windows_information_protection_policy_item_request_builder.MdmWindowsInformationProtectionPolicyItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def mobile_app_categories_by_id(self,id: str) -> mobile_app_category_item_request_builder.MobileAppCategoryItemRequestBuilder:
        """
        Provides operations to manage the mobileAppCategories property of the microsoft.graph.deviceAppManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: mobile_app_category_item_request_builder.MobileAppCategoryItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["mobileAppCategory%2Did"] = id
        return mobile_app_category_item_request_builder.MobileAppCategoryItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def mobile_app_configurations_by_id(self,id: str) -> managed_device_mobile_app_configuration_item_request_builder.ManagedDeviceMobileAppConfigurationItemRequestBuilder:
        """
        Provides operations to manage the mobileAppConfigurations property of the microsoft.graph.deviceAppManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: managed_device_mobile_app_configuration_item_request_builder.ManagedDeviceMobileAppConfigurationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["managedDeviceMobileAppConfiguration%2Did"] = id
        return managed_device_mobile_app_configuration_item_request_builder.ManagedDeviceMobileAppConfigurationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def mobile_apps_by_id(self,id: str) -> mobile_app_item_request_builder.MobileAppItemRequestBuilder:
        """
        Provides operations to manage the mobileApps property of the microsoft.graph.deviceAppManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: mobile_app_item_request_builder.MobileAppItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["mobileApp%2Did"] = id
        return mobile_app_item_request_builder.MobileAppItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def patch(self,body: Optional[device_app_management.DeviceAppManagement] = None, request_configuration: Optional[DeviceAppManagementRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[device_app_management.DeviceAppManagement]:
        """
        Update deviceAppManagement
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[device_app_management.DeviceAppManagement]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, device_app_management.DeviceAppManagement, response_handler, error_mapping)
    
    def policy_sets_by_id(self,id: str) -> policy_set_item_request_builder.PolicySetItemRequestBuilder:
        """
        Provides operations to manage the policySets property of the microsoft.graph.deviceAppManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: policy_set_item_request_builder.PolicySetItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["policySet%2Did"] = id
        return policy_set_item_request_builder.PolicySetItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def side_loading_keys_by_id(self,id: str) -> side_loading_key_item_request_builder.SideLoadingKeyItemRequestBuilder:
        """
        Provides operations to manage the sideLoadingKeys property of the microsoft.graph.deviceAppManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: side_loading_key_item_request_builder.SideLoadingKeyItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["sideLoadingKey%2Did"] = id
        return side_loading_key_item_request_builder.SideLoadingKeyItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def targeted_managed_app_configurations_by_id(self,id: str) -> targeted_managed_app_configuration_item_request_builder.TargetedManagedAppConfigurationItemRequestBuilder:
        """
        Provides operations to manage the targetedManagedAppConfigurations property of the microsoft.graph.deviceAppManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: targeted_managed_app_configuration_item_request_builder.TargetedManagedAppConfigurationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["targetedManagedAppConfiguration%2Did"] = id
        return targeted_managed_app_configuration_item_request_builder.TargetedManagedAppConfigurationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def to_get_request_information(self,request_configuration: Optional[DeviceAppManagementRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get deviceAppManagement
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers["Accept"] = "application/json"
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def to_patch_request_information(self,body: Optional[device_app_management.DeviceAppManagement] = None, request_configuration: Optional[DeviceAppManagementRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update deviceAppManagement
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.PATCH
        request_info.headers["Accept"] = "application/json"
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def vpp_tokens_by_id(self,id: str) -> vpp_token_item_request_builder.VppTokenItemRequestBuilder:
        """
        Provides operations to manage the vppTokens property of the microsoft.graph.deviceAppManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: vpp_token_item_request_builder.VppTokenItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["vppToken%2Did"] = id
        return vpp_token_item_request_builder.VppTokenItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def wdac_supplemental_policies_by_id(self,id: str) -> windows_defender_application_control_supplemental_policy_item_request_builder.WindowsDefenderApplicationControlSupplementalPolicyItemRequestBuilder:
        """
        Provides operations to manage the wdacSupplementalPolicies property of the microsoft.graph.deviceAppManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: windows_defender_application_control_supplemental_policy_item_request_builder.WindowsDefenderApplicationControlSupplementalPolicyItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["windowsDefenderApplicationControlSupplementalPolicy%2Did"] = id
        return windows_defender_application_control_supplemental_policy_item_request_builder.WindowsDefenderApplicationControlSupplementalPolicyItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def windows_information_protection_device_registrations_by_id(self,id: str) -> windows_information_protection_device_registration_item_request_builder.WindowsInformationProtectionDeviceRegistrationItemRequestBuilder:
        """
        Provides operations to manage the windowsInformationProtectionDeviceRegistrations property of the microsoft.graph.deviceAppManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: windows_information_protection_device_registration_item_request_builder.WindowsInformationProtectionDeviceRegistrationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["windowsInformationProtectionDeviceRegistration%2Did"] = id
        return windows_information_protection_device_registration_item_request_builder.WindowsInformationProtectionDeviceRegistrationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def windows_information_protection_policies_by_id(self,id: str) -> windows_information_protection_policy_item_request_builder.WindowsInformationProtectionPolicyItemRequestBuilder:
        """
        Provides operations to manage the windowsInformationProtectionPolicies property of the microsoft.graph.deviceAppManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: windows_information_protection_policy_item_request_builder.WindowsInformationProtectionPolicyItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["windowsInformationProtectionPolicy%2Did"] = id
        return windows_information_protection_policy_item_request_builder.WindowsInformationProtectionPolicyItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def windows_information_protection_wipe_actions_by_id(self,id: str) -> windows_information_protection_wipe_action_item_request_builder.WindowsInformationProtectionWipeActionItemRequestBuilder:
        """
        Provides operations to manage the windowsInformationProtectionWipeActions property of the microsoft.graph.deviceAppManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: windows_information_protection_wipe_action_item_request_builder.WindowsInformationProtectionWipeActionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["windowsInformationProtectionWipeAction%2Did"] = id
        return windows_information_protection_wipe_action_item_request_builder.WindowsInformationProtectionWipeActionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def windows_managed_app_protections_by_id(self,id: str) -> windows_managed_app_protection_item_request_builder.WindowsManagedAppProtectionItemRequestBuilder:
        """
        Provides operations to manage the windowsManagedAppProtections property of the microsoft.graph.deviceAppManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: windows_managed_app_protection_item_request_builder.WindowsManagedAppProtectionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["windowsManagedAppProtection%2Did"] = id
        return windows_managed_app_protection_item_request_builder.WindowsManagedAppProtectionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @dataclass
    class DeviceAppManagementRequestBuilderGetQueryParameters():
        """
        Get deviceAppManagement
        """
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            Args:
                originalName: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise Exception("original_name cannot be undefined")
            if original_name == "expand":
                return "%24expand"
            if original_name == "select":
                return "%24select"
            return original_name
        
    
    @dataclass
    class DeviceAppManagementRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[DeviceAppManagementRequestBuilder.DeviceAppManagementRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class DeviceAppManagementRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

