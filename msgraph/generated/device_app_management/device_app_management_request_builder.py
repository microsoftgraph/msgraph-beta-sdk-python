from __future__ import annotations
from dataclasses import dataclass
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..models import device_app_management
    from ..models.o_data_errors import o_data_error
    from .android_managed_app_protections import android_managed_app_protections_request_builder
    from .default_managed_app_protections import default_managed_app_protections_request_builder
    from .device_app_management_tasks import device_app_management_tasks_request_builder
    from .enterprise_code_signing_certificates import enterprise_code_signing_certificates_request_builder
    from .ios_lob_app_provisioning_configurations import ios_lob_app_provisioning_configurations_request_builder
    from .ios_managed_app_protections import ios_managed_app_protections_request_builder
    from .managed_app_policies import managed_app_policies_request_builder
    from .managed_app_registrations import managed_app_registrations_request_builder
    from .managed_app_statuses import managed_app_statuses_request_builder
    from .managed_e_book_categories import managed_e_book_categories_request_builder
    from .managed_e_books import managed_e_books_request_builder
    from .mdm_windows_information_protection_policies import mdm_windows_information_protection_policies_request_builder
    from .mobile_app_categories import mobile_app_categories_request_builder
    from .mobile_app_configurations import mobile_app_configurations_request_builder
    from .mobile_apps import mobile_apps_request_builder
    from .policy_sets import policy_sets_request_builder
    from .symantec_code_signing_certificate import symantec_code_signing_certificate_request_builder
    from .sync_microsoft_store_for_business_apps import sync_microsoft_store_for_business_apps_request_builder
    from .targeted_managed_app_configurations import targeted_managed_app_configurations_request_builder
    from .vpp_tokens import vpp_tokens_request_builder
    from .wdac_supplemental_policies import wdac_supplemental_policies_request_builder
    from .windows_information_protection_device_registrations import windows_information_protection_device_registrations_request_builder
    from .windows_information_protection_policies import windows_information_protection_policies_request_builder
    from .windows_information_protection_wipe_actions import windows_information_protection_wipe_actions_request_builder
    from .windows_managed_app_protections import windows_managed_app_protections_request_builder
    from .windows_management_app import windows_management_app_request_builder

class DeviceAppManagementRequestBuilder():
    """
    Provides operations to manage the deviceAppManagement singleton.
    """
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
    
    async def get(self,request_configuration: Optional[DeviceAppManagementRequestBuilderGetRequestConfiguration] = None) -> Optional[device_app_management.DeviceAppManagement]:
        """
        Get deviceAppManagement
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[device_app_management.DeviceAppManagement]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ..models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models import device_app_management

        return await self.request_adapter.send_async(request_info, device_app_management.DeviceAppManagement, error_mapping)
    
    async def patch(self,body: Optional[device_app_management.DeviceAppManagement] = None, request_configuration: Optional[DeviceAppManagementRequestBuilderPatchRequestConfiguration] = None) -> Optional[device_app_management.DeviceAppManagement]:
        """
        Update deviceAppManagement
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[device_app_management.DeviceAppManagement]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ..models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models import device_app_management

        return await self.request_adapter.send_async(request_info, device_app_management.DeviceAppManagement, error_mapping)
    
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
        request_info.headers["Accept"] = ["application/json"]
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
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    @property
    def android_managed_app_protections(self) -> android_managed_app_protections_request_builder.AndroidManagedAppProtectionsRequestBuilder:
        """
        Provides operations to manage the androidManagedAppProtections property of the microsoft.graph.deviceAppManagement entity.
        """
        from .android_managed_app_protections import android_managed_app_protections_request_builder

        return android_managed_app_protections_request_builder.AndroidManagedAppProtectionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def default_managed_app_protections(self) -> default_managed_app_protections_request_builder.DefaultManagedAppProtectionsRequestBuilder:
        """
        Provides operations to manage the defaultManagedAppProtections property of the microsoft.graph.deviceAppManagement entity.
        """
        from .default_managed_app_protections import default_managed_app_protections_request_builder

        return default_managed_app_protections_request_builder.DefaultManagedAppProtectionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_app_management_tasks(self) -> device_app_management_tasks_request_builder.DeviceAppManagementTasksRequestBuilder:
        """
        Provides operations to manage the deviceAppManagementTasks property of the microsoft.graph.deviceAppManagement entity.
        """
        from .device_app_management_tasks import device_app_management_tasks_request_builder

        return device_app_management_tasks_request_builder.DeviceAppManagementTasksRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def enterprise_code_signing_certificates(self) -> enterprise_code_signing_certificates_request_builder.EnterpriseCodeSigningCertificatesRequestBuilder:
        """
        Provides operations to manage the enterpriseCodeSigningCertificates property of the microsoft.graph.deviceAppManagement entity.
        """
        from .enterprise_code_signing_certificates import enterprise_code_signing_certificates_request_builder

        return enterprise_code_signing_certificates_request_builder.EnterpriseCodeSigningCertificatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def ios_lob_app_provisioning_configurations(self) -> ios_lob_app_provisioning_configurations_request_builder.IosLobAppProvisioningConfigurationsRequestBuilder:
        """
        Provides operations to manage the iosLobAppProvisioningConfigurations property of the microsoft.graph.deviceAppManagement entity.
        """
        from .ios_lob_app_provisioning_configurations import ios_lob_app_provisioning_configurations_request_builder

        return ios_lob_app_provisioning_configurations_request_builder.IosLobAppProvisioningConfigurationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def ios_managed_app_protections(self) -> ios_managed_app_protections_request_builder.IosManagedAppProtectionsRequestBuilder:
        """
        Provides operations to manage the iosManagedAppProtections property of the microsoft.graph.deviceAppManagement entity.
        """
        from .ios_managed_app_protections import ios_managed_app_protections_request_builder

        return ios_managed_app_protections_request_builder.IosManagedAppProtectionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def managed_app_policies(self) -> managed_app_policies_request_builder.ManagedAppPoliciesRequestBuilder:
        """
        Provides operations to manage the managedAppPolicies property of the microsoft.graph.deviceAppManagement entity.
        """
        from .managed_app_policies import managed_app_policies_request_builder

        return managed_app_policies_request_builder.ManagedAppPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def managed_app_registrations(self) -> managed_app_registrations_request_builder.ManagedAppRegistrationsRequestBuilder:
        """
        Provides operations to manage the managedAppRegistrations property of the microsoft.graph.deviceAppManagement entity.
        """
        from .managed_app_registrations import managed_app_registrations_request_builder

        return managed_app_registrations_request_builder.ManagedAppRegistrationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def managed_app_statuses(self) -> managed_app_statuses_request_builder.ManagedAppStatusesRequestBuilder:
        """
        Provides operations to manage the managedAppStatuses property of the microsoft.graph.deviceAppManagement entity.
        """
        from .managed_app_statuses import managed_app_statuses_request_builder

        return managed_app_statuses_request_builder.ManagedAppStatusesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def managed_e_book_categories(self) -> managed_e_book_categories_request_builder.ManagedEBookCategoriesRequestBuilder:
        """
        Provides operations to manage the managedEBookCategories property of the microsoft.graph.deviceAppManagement entity.
        """
        from .managed_e_book_categories import managed_e_book_categories_request_builder

        return managed_e_book_categories_request_builder.ManagedEBookCategoriesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def managed_e_books(self) -> managed_e_books_request_builder.ManagedEBooksRequestBuilder:
        """
        Provides operations to manage the managedEBooks property of the microsoft.graph.deviceAppManagement entity.
        """
        from .managed_e_books import managed_e_books_request_builder

        return managed_e_books_request_builder.ManagedEBooksRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mdm_windows_information_protection_policies(self) -> mdm_windows_information_protection_policies_request_builder.MdmWindowsInformationProtectionPoliciesRequestBuilder:
        """
        Provides operations to manage the mdmWindowsInformationProtectionPolicies property of the microsoft.graph.deviceAppManagement entity.
        """
        from .mdm_windows_information_protection_policies import mdm_windows_information_protection_policies_request_builder

        return mdm_windows_information_protection_policies_request_builder.MdmWindowsInformationProtectionPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mobile_app_categories(self) -> mobile_app_categories_request_builder.MobileAppCategoriesRequestBuilder:
        """
        Provides operations to manage the mobileAppCategories property of the microsoft.graph.deviceAppManagement entity.
        """
        from .mobile_app_categories import mobile_app_categories_request_builder

        return mobile_app_categories_request_builder.MobileAppCategoriesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mobile_app_configurations(self) -> mobile_app_configurations_request_builder.MobileAppConfigurationsRequestBuilder:
        """
        Provides operations to manage the mobileAppConfigurations property of the microsoft.graph.deviceAppManagement entity.
        """
        from .mobile_app_configurations import mobile_app_configurations_request_builder

        return mobile_app_configurations_request_builder.MobileAppConfigurationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mobile_apps(self) -> mobile_apps_request_builder.MobileAppsRequestBuilder:
        """
        Provides operations to manage the mobileApps property of the microsoft.graph.deviceAppManagement entity.
        """
        from .mobile_apps import mobile_apps_request_builder

        return mobile_apps_request_builder.MobileAppsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def policy_sets(self) -> policy_sets_request_builder.PolicySetsRequestBuilder:
        """
        Provides operations to manage the policySets property of the microsoft.graph.deviceAppManagement entity.
        """
        from .policy_sets import policy_sets_request_builder

        return policy_sets_request_builder.PolicySetsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def symantec_code_signing_certificate(self) -> symantec_code_signing_certificate_request_builder.SymantecCodeSigningCertificateRequestBuilder:
        """
        Provides operations to manage the symantecCodeSigningCertificate property of the microsoft.graph.deviceAppManagement entity.
        """
        from .symantec_code_signing_certificate import symantec_code_signing_certificate_request_builder

        return symantec_code_signing_certificate_request_builder.SymantecCodeSigningCertificateRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sync_microsoft_store_for_business_apps(self) -> sync_microsoft_store_for_business_apps_request_builder.SyncMicrosoftStoreForBusinessAppsRequestBuilder:
        """
        Provides operations to call the syncMicrosoftStoreForBusinessApps method.
        """
        from .sync_microsoft_store_for_business_apps import sync_microsoft_store_for_business_apps_request_builder

        return sync_microsoft_store_for_business_apps_request_builder.SyncMicrosoftStoreForBusinessAppsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def targeted_managed_app_configurations(self) -> targeted_managed_app_configurations_request_builder.TargetedManagedAppConfigurationsRequestBuilder:
        """
        Provides operations to manage the targetedManagedAppConfigurations property of the microsoft.graph.deviceAppManagement entity.
        """
        from .targeted_managed_app_configurations import targeted_managed_app_configurations_request_builder

        return targeted_managed_app_configurations_request_builder.TargetedManagedAppConfigurationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def vpp_tokens(self) -> vpp_tokens_request_builder.VppTokensRequestBuilder:
        """
        Provides operations to manage the vppTokens property of the microsoft.graph.deviceAppManagement entity.
        """
        from .vpp_tokens import vpp_tokens_request_builder

        return vpp_tokens_request_builder.VppTokensRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def wdac_supplemental_policies(self) -> wdac_supplemental_policies_request_builder.WdacSupplementalPoliciesRequestBuilder:
        """
        Provides operations to manage the wdacSupplementalPolicies property of the microsoft.graph.deviceAppManagement entity.
        """
        from .wdac_supplemental_policies import wdac_supplemental_policies_request_builder

        return wdac_supplemental_policies_request_builder.WdacSupplementalPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def windows_information_protection_device_registrations(self) -> windows_information_protection_device_registrations_request_builder.WindowsInformationProtectionDeviceRegistrationsRequestBuilder:
        """
        Provides operations to manage the windowsInformationProtectionDeviceRegistrations property of the microsoft.graph.deviceAppManagement entity.
        """
        from .windows_information_protection_device_registrations import windows_information_protection_device_registrations_request_builder

        return windows_information_protection_device_registrations_request_builder.WindowsInformationProtectionDeviceRegistrationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def windows_information_protection_policies(self) -> windows_information_protection_policies_request_builder.WindowsInformationProtectionPoliciesRequestBuilder:
        """
        Provides operations to manage the windowsInformationProtectionPolicies property of the microsoft.graph.deviceAppManagement entity.
        """
        from .windows_information_protection_policies import windows_information_protection_policies_request_builder

        return windows_information_protection_policies_request_builder.WindowsInformationProtectionPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def windows_information_protection_wipe_actions(self) -> windows_information_protection_wipe_actions_request_builder.WindowsInformationProtectionWipeActionsRequestBuilder:
        """
        Provides operations to manage the windowsInformationProtectionWipeActions property of the microsoft.graph.deviceAppManagement entity.
        """
        from .windows_information_protection_wipe_actions import windows_information_protection_wipe_actions_request_builder

        return windows_information_protection_wipe_actions_request_builder.WindowsInformationProtectionWipeActionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def windows_managed_app_protections(self) -> windows_managed_app_protections_request_builder.WindowsManagedAppProtectionsRequestBuilder:
        """
        Provides operations to manage the windowsManagedAppProtections property of the microsoft.graph.deviceAppManagement entity.
        """
        from .windows_managed_app_protections import windows_managed_app_protections_request_builder

        return windows_managed_app_protections_request_builder.WindowsManagedAppProtectionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def windows_management_app(self) -> windows_management_app_request_builder.WindowsManagementAppRequestBuilder:
        """
        Provides operations to manage the windowsManagementApp property of the microsoft.graph.deviceAppManagement entity.
        """
        from .windows_management_app import windows_management_app_request_builder

        return windows_management_app_request_builder.WindowsManagementAppRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class DeviceAppManagementRequestBuilderGetQueryParameters():
        """
        Get deviceAppManagement
        """
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
        
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

    
    @dataclass
    class DeviceAppManagementRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

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
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

