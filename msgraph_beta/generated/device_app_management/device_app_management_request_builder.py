from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.default_query_parameters import QueryParameters
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from warnings import warn

if TYPE_CHECKING:
    from ..models.device_app_management import DeviceAppManagement
    from ..models.o_data_errors.o_data_error import ODataError
    from .android_managed_app_protections.android_managed_app_protections_request_builder import AndroidManagedAppProtectionsRequestBuilder
    from .default_managed_app_protections.default_managed_app_protections_request_builder import DefaultManagedAppProtectionsRequestBuilder
    from .device_app_management_tasks.device_app_management_tasks_request_builder import DeviceAppManagementTasksRequestBuilder
    from .enterprise_code_signing_certificates.enterprise_code_signing_certificates_request_builder import EnterpriseCodeSigningCertificatesRequestBuilder
    from .ios_lob_app_provisioning_configurations.ios_lob_app_provisioning_configurations_request_builder import IosLobAppProvisioningConfigurationsRequestBuilder
    from .ios_managed_app_protections.ios_managed_app_protections_request_builder import IosManagedAppProtectionsRequestBuilder
    from .managed_app_policies.managed_app_policies_request_builder import ManagedAppPoliciesRequestBuilder
    from .managed_app_registrations.managed_app_registrations_request_builder import ManagedAppRegistrationsRequestBuilder
    from .managed_app_statuses.managed_app_statuses_request_builder import ManagedAppStatusesRequestBuilder
    from .managed_e_books.managed_e_books_request_builder import ManagedEBooksRequestBuilder
    from .managed_e_book_categories.managed_e_book_categories_request_builder import ManagedEBookCategoriesRequestBuilder
    from .mdm_windows_information_protection_policies.mdm_windows_information_protection_policies_request_builder import MdmWindowsInformationProtectionPoliciesRequestBuilder
    from .mobile_apps.mobile_apps_request_builder import MobileAppsRequestBuilder
    from .mobile_app_catalog_packages.mobile_app_catalog_packages_request_builder import MobileAppCatalogPackagesRequestBuilder
    from .mobile_app_categories.mobile_app_categories_request_builder import MobileAppCategoriesRequestBuilder
    from .mobile_app_configurations.mobile_app_configurations_request_builder import MobileAppConfigurationsRequestBuilder
    from .mobile_app_relationships.mobile_app_relationships_request_builder import MobileAppRelationshipsRequestBuilder
    from .policy_sets.policy_sets_request_builder import PolicySetsRequestBuilder
    from .symantec_code_signing_certificate.symantec_code_signing_certificate_request_builder import SymantecCodeSigningCertificateRequestBuilder
    from .sync_microsoft_store_for_business_apps.sync_microsoft_store_for_business_apps_request_builder import SyncMicrosoftStoreForBusinessAppsRequestBuilder
    from .targeted_managed_app_configurations.targeted_managed_app_configurations_request_builder import TargetedManagedAppConfigurationsRequestBuilder
    from .vpp_tokens.vpp_tokens_request_builder import VppTokensRequestBuilder
    from .wdac_supplemental_policies.wdac_supplemental_policies_request_builder import WdacSupplementalPoliciesRequestBuilder
    from .windows_information_protection_device_registrations.windows_information_protection_device_registrations_request_builder import WindowsInformationProtectionDeviceRegistrationsRequestBuilder
    from .windows_information_protection_policies.windows_information_protection_policies_request_builder import WindowsInformationProtectionPoliciesRequestBuilder
    from .windows_information_protection_wipe_actions.windows_information_protection_wipe_actions_request_builder import WindowsInformationProtectionWipeActionsRequestBuilder
    from .windows_managed_app_protections.windows_managed_app_protections_request_builder import WindowsManagedAppProtectionsRequestBuilder
    from .windows_management_app.windows_management_app_request_builder import WindowsManagementAppRequestBuilder

class DeviceAppManagementRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the deviceAppManagement singleton.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new DeviceAppManagementRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/deviceAppManagement{?%24expand,%24select}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[DeviceAppManagementRequestBuilderGetQueryParameters]] = None) -> Optional[DeviceAppManagement]:
        """
        Get deviceAppManagement
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[DeviceAppManagement]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ..models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.device_app_management import DeviceAppManagement

        return await self.request_adapter.send_async(request_info, DeviceAppManagement, error_mapping)
    
    async def patch(self,body: DeviceAppManagement, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[DeviceAppManagement]:
        """
        Update deviceAppManagement
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[DeviceAppManagement]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ..models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.device_app_management import DeviceAppManagement

        return await self.request_adapter.send_async(request_info, DeviceAppManagement, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[DeviceAppManagementRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Get deviceAppManagement
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: DeviceAppManagement, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update deviceAppManagement
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PATCH, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> DeviceAppManagementRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: DeviceAppManagementRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return DeviceAppManagementRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def android_managed_app_protections(self) -> AndroidManagedAppProtectionsRequestBuilder:
        """
        Provides operations to manage the androidManagedAppProtections property of the microsoft.graph.deviceAppManagement entity.
        """
        from .android_managed_app_protections.android_managed_app_protections_request_builder import AndroidManagedAppProtectionsRequestBuilder

        return AndroidManagedAppProtectionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def default_managed_app_protections(self) -> DefaultManagedAppProtectionsRequestBuilder:
        """
        Provides operations to manage the defaultManagedAppProtections property of the microsoft.graph.deviceAppManagement entity.
        """
        from .default_managed_app_protections.default_managed_app_protections_request_builder import DefaultManagedAppProtectionsRequestBuilder

        return DefaultManagedAppProtectionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_app_management_tasks(self) -> DeviceAppManagementTasksRequestBuilder:
        """
        Provides operations to manage the deviceAppManagementTasks property of the microsoft.graph.deviceAppManagement entity.
        """
        from .device_app_management_tasks.device_app_management_tasks_request_builder import DeviceAppManagementTasksRequestBuilder

        return DeviceAppManagementTasksRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def enterprise_code_signing_certificates(self) -> EnterpriseCodeSigningCertificatesRequestBuilder:
        """
        Provides operations to manage the enterpriseCodeSigningCertificates property of the microsoft.graph.deviceAppManagement entity.
        """
        from .enterprise_code_signing_certificates.enterprise_code_signing_certificates_request_builder import EnterpriseCodeSigningCertificatesRequestBuilder

        return EnterpriseCodeSigningCertificatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def ios_lob_app_provisioning_configurations(self) -> IosLobAppProvisioningConfigurationsRequestBuilder:
        """
        Provides operations to manage the iosLobAppProvisioningConfigurations property of the microsoft.graph.deviceAppManagement entity.
        """
        from .ios_lob_app_provisioning_configurations.ios_lob_app_provisioning_configurations_request_builder import IosLobAppProvisioningConfigurationsRequestBuilder

        return IosLobAppProvisioningConfigurationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def ios_managed_app_protections(self) -> IosManagedAppProtectionsRequestBuilder:
        """
        Provides operations to manage the iosManagedAppProtections property of the microsoft.graph.deviceAppManagement entity.
        """
        from .ios_managed_app_protections.ios_managed_app_protections_request_builder import IosManagedAppProtectionsRequestBuilder

        return IosManagedAppProtectionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def managed_app_policies(self) -> ManagedAppPoliciesRequestBuilder:
        """
        Provides operations to manage the managedAppPolicies property of the microsoft.graph.deviceAppManagement entity.
        """
        from .managed_app_policies.managed_app_policies_request_builder import ManagedAppPoliciesRequestBuilder

        return ManagedAppPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def managed_app_registrations(self) -> ManagedAppRegistrationsRequestBuilder:
        """
        Provides operations to manage the managedAppRegistrations property of the microsoft.graph.deviceAppManagement entity.
        """
        from .managed_app_registrations.managed_app_registrations_request_builder import ManagedAppRegistrationsRequestBuilder

        return ManagedAppRegistrationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def managed_app_statuses(self) -> ManagedAppStatusesRequestBuilder:
        """
        Provides operations to manage the managedAppStatuses property of the microsoft.graph.deviceAppManagement entity.
        """
        from .managed_app_statuses.managed_app_statuses_request_builder import ManagedAppStatusesRequestBuilder

        return ManagedAppStatusesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def managed_e_book_categories(self) -> ManagedEBookCategoriesRequestBuilder:
        """
        Provides operations to manage the managedEBookCategories property of the microsoft.graph.deviceAppManagement entity.
        """
        from .managed_e_book_categories.managed_e_book_categories_request_builder import ManagedEBookCategoriesRequestBuilder

        return ManagedEBookCategoriesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def managed_e_books(self) -> ManagedEBooksRequestBuilder:
        """
        Provides operations to manage the managedEBooks property of the microsoft.graph.deviceAppManagement entity.
        """
        from .managed_e_books.managed_e_books_request_builder import ManagedEBooksRequestBuilder

        return ManagedEBooksRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mdm_windows_information_protection_policies(self) -> MdmWindowsInformationProtectionPoliciesRequestBuilder:
        """
        Provides operations to manage the mdmWindowsInformationProtectionPolicies property of the microsoft.graph.deviceAppManagement entity.
        """
        from .mdm_windows_information_protection_policies.mdm_windows_information_protection_policies_request_builder import MdmWindowsInformationProtectionPoliciesRequestBuilder

        return MdmWindowsInformationProtectionPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mobile_app_catalog_packages(self) -> MobileAppCatalogPackagesRequestBuilder:
        """
        Provides operations to manage the mobileAppCatalogPackages property of the microsoft.graph.deviceAppManagement entity.
        """
        from .mobile_app_catalog_packages.mobile_app_catalog_packages_request_builder import MobileAppCatalogPackagesRequestBuilder

        return MobileAppCatalogPackagesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mobile_app_categories(self) -> MobileAppCategoriesRequestBuilder:
        """
        Provides operations to manage the mobileAppCategories property of the microsoft.graph.deviceAppManagement entity.
        """
        from .mobile_app_categories.mobile_app_categories_request_builder import MobileAppCategoriesRequestBuilder

        return MobileAppCategoriesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mobile_app_configurations(self) -> MobileAppConfigurationsRequestBuilder:
        """
        Provides operations to manage the mobileAppConfigurations property of the microsoft.graph.deviceAppManagement entity.
        """
        from .mobile_app_configurations.mobile_app_configurations_request_builder import MobileAppConfigurationsRequestBuilder

        return MobileAppConfigurationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mobile_app_relationships(self) -> MobileAppRelationshipsRequestBuilder:
        """
        Provides operations to manage the mobileAppRelationships property of the microsoft.graph.deviceAppManagement entity.
        """
        from .mobile_app_relationships.mobile_app_relationships_request_builder import MobileAppRelationshipsRequestBuilder

        return MobileAppRelationshipsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mobile_apps(self) -> MobileAppsRequestBuilder:
        """
        Provides operations to manage the mobileApps property of the microsoft.graph.deviceAppManagement entity.
        """
        from .mobile_apps.mobile_apps_request_builder import MobileAppsRequestBuilder

        return MobileAppsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def policy_sets(self) -> PolicySetsRequestBuilder:
        """
        Provides operations to manage the policySets property of the microsoft.graph.deviceAppManagement entity.
        """
        from .policy_sets.policy_sets_request_builder import PolicySetsRequestBuilder

        return PolicySetsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def symantec_code_signing_certificate(self) -> SymantecCodeSigningCertificateRequestBuilder:
        """
        Provides operations to manage the symantecCodeSigningCertificate property of the microsoft.graph.deviceAppManagement entity.
        """
        from .symantec_code_signing_certificate.symantec_code_signing_certificate_request_builder import SymantecCodeSigningCertificateRequestBuilder

        return SymantecCodeSigningCertificateRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sync_microsoft_store_for_business_apps(self) -> SyncMicrosoftStoreForBusinessAppsRequestBuilder:
        """
        Provides operations to call the syncMicrosoftStoreForBusinessApps method.
        """
        from .sync_microsoft_store_for_business_apps.sync_microsoft_store_for_business_apps_request_builder import SyncMicrosoftStoreForBusinessAppsRequestBuilder

        return SyncMicrosoftStoreForBusinessAppsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def targeted_managed_app_configurations(self) -> TargetedManagedAppConfigurationsRequestBuilder:
        """
        Provides operations to manage the targetedManagedAppConfigurations property of the microsoft.graph.deviceAppManagement entity.
        """
        from .targeted_managed_app_configurations.targeted_managed_app_configurations_request_builder import TargetedManagedAppConfigurationsRequestBuilder

        return TargetedManagedAppConfigurationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def vpp_tokens(self) -> VppTokensRequestBuilder:
        """
        Provides operations to manage the vppTokens property of the microsoft.graph.deviceAppManagement entity.
        """
        from .vpp_tokens.vpp_tokens_request_builder import VppTokensRequestBuilder

        return VppTokensRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def wdac_supplemental_policies(self) -> WdacSupplementalPoliciesRequestBuilder:
        """
        Provides operations to manage the wdacSupplementalPolicies property of the microsoft.graph.deviceAppManagement entity.
        """
        from .wdac_supplemental_policies.wdac_supplemental_policies_request_builder import WdacSupplementalPoliciesRequestBuilder

        return WdacSupplementalPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def windows_information_protection_device_registrations(self) -> WindowsInformationProtectionDeviceRegistrationsRequestBuilder:
        """
        Provides operations to manage the windowsInformationProtectionDeviceRegistrations property of the microsoft.graph.deviceAppManagement entity.
        """
        from .windows_information_protection_device_registrations.windows_information_protection_device_registrations_request_builder import WindowsInformationProtectionDeviceRegistrationsRequestBuilder

        return WindowsInformationProtectionDeviceRegistrationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def windows_information_protection_policies(self) -> WindowsInformationProtectionPoliciesRequestBuilder:
        """
        Provides operations to manage the windowsInformationProtectionPolicies property of the microsoft.graph.deviceAppManagement entity.
        """
        from .windows_information_protection_policies.windows_information_protection_policies_request_builder import WindowsInformationProtectionPoliciesRequestBuilder

        return WindowsInformationProtectionPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def windows_information_protection_wipe_actions(self) -> WindowsInformationProtectionWipeActionsRequestBuilder:
        """
        Provides operations to manage the windowsInformationProtectionWipeActions property of the microsoft.graph.deviceAppManagement entity.
        """
        from .windows_information_protection_wipe_actions.windows_information_protection_wipe_actions_request_builder import WindowsInformationProtectionWipeActionsRequestBuilder

        return WindowsInformationProtectionWipeActionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def windows_managed_app_protections(self) -> WindowsManagedAppProtectionsRequestBuilder:
        """
        Provides operations to manage the windowsManagedAppProtections property of the microsoft.graph.deviceAppManagement entity.
        """
        from .windows_managed_app_protections.windows_managed_app_protections_request_builder import WindowsManagedAppProtectionsRequestBuilder

        return WindowsManagedAppProtectionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def windows_management_app(self) -> WindowsManagementAppRequestBuilder:
        """
        Provides operations to manage the windowsManagementApp property of the microsoft.graph.deviceAppManagement entity.
        """
        from .windows_management_app.windows_management_app_request_builder import WindowsManagementAppRequestBuilder

        return WindowsManagementAppRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class DeviceAppManagementRequestBuilderGetQueryParameters():
        """
        Get deviceAppManagement
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
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
    class DeviceAppManagementRequestBuilderGetRequestConfiguration(RequestConfiguration[DeviceAppManagementRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class DeviceAppManagementRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

