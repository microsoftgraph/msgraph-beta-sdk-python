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

default_ios_enrollment_profile_request_builder = lazy_import('msgraph.generated.device_management.dep_onboarding_settings.item.default_ios_enrollment_profile.default_ios_enrollment_profile_request_builder')
default_mac_os_enrollment_profile_request_builder = lazy_import('msgraph.generated.device_management.dep_onboarding_settings.item.default_mac_os_enrollment_profile.default_mac_os_enrollment_profile_request_builder')
enrollment_profiles_request_builder = lazy_import('msgraph.generated.device_management.dep_onboarding_settings.item.enrollment_profiles.enrollment_profiles_request_builder')
enrollment_profile_item_request_builder = lazy_import('msgraph.generated.device_management.dep_onboarding_settings.item.enrollment_profiles.item.enrollment_profile_item_request_builder')
generate_encryption_public_key_request_builder = lazy_import('msgraph.generated.device_management.dep_onboarding_settings.item.generate_encryption_public_key.generate_encryption_public_key_request_builder')
get_encryption_public_key_request_builder = lazy_import('msgraph.generated.device_management.dep_onboarding_settings.item.get_encryption_public_key.get_encryption_public_key_request_builder')
imported_apple_device_identities_request_builder = lazy_import('msgraph.generated.device_management.dep_onboarding_settings.item.imported_apple_device_identities.imported_apple_device_identities_request_builder')
imported_apple_device_identity_item_request_builder = lazy_import('msgraph.generated.device_management.dep_onboarding_settings.item.imported_apple_device_identities.item.imported_apple_device_identity_item_request_builder')
share_for_school_data_sync_service_request_builder = lazy_import('msgraph.generated.device_management.dep_onboarding_settings.item.share_for_school_data_sync_service.share_for_school_data_sync_service_request_builder')
sync_with_apple_device_enrollment_program_request_builder = lazy_import('msgraph.generated.device_management.dep_onboarding_settings.item.sync_with_apple_device_enrollment_program.sync_with_apple_device_enrollment_program_request_builder')
unshare_for_school_data_sync_service_request_builder = lazy_import('msgraph.generated.device_management.dep_onboarding_settings.item.unshare_for_school_data_sync_service.unshare_for_school_data_sync_service_request_builder')
upload_dep_token_request_builder = lazy_import('msgraph.generated.device_management.dep_onboarding_settings.item.upload_dep_token.upload_dep_token_request_builder')
dep_onboarding_setting = lazy_import('msgraph.generated.models.dep_onboarding_setting')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class DepOnboardingSettingItemRequestBuilder():
    """
    Provides operations to manage the depOnboardingSettings property of the microsoft.graph.deviceManagement entity.
    """
    @property
    def default_ios_enrollment_profile(self) -> default_ios_enrollment_profile_request_builder.DefaultIosEnrollmentProfileRequestBuilder:
        """
        Provides operations to manage the defaultIosEnrollmentProfile property of the microsoft.graph.depOnboardingSetting entity.
        """
        return default_ios_enrollment_profile_request_builder.DefaultIosEnrollmentProfileRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def default_mac_os_enrollment_profile(self) -> default_mac_os_enrollment_profile_request_builder.DefaultMacOsEnrollmentProfileRequestBuilder:
        """
        Provides operations to manage the defaultMacOsEnrollmentProfile property of the microsoft.graph.depOnboardingSetting entity.
        """
        return default_mac_os_enrollment_profile_request_builder.DefaultMacOsEnrollmentProfileRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def enrollment_profiles(self) -> enrollment_profiles_request_builder.EnrollmentProfilesRequestBuilder:
        """
        Provides operations to manage the enrollmentProfiles property of the microsoft.graph.depOnboardingSetting entity.
        """
        return enrollment_profiles_request_builder.EnrollmentProfilesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def generate_encryption_public_key(self) -> generate_encryption_public_key_request_builder.GenerateEncryptionPublicKeyRequestBuilder:
        """
        Provides operations to call the generateEncryptionPublicKey method.
        """
        return generate_encryption_public_key_request_builder.GenerateEncryptionPublicKeyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def imported_apple_device_identities(self) -> imported_apple_device_identities_request_builder.ImportedAppleDeviceIdentitiesRequestBuilder:
        """
        Provides operations to manage the importedAppleDeviceIdentities property of the microsoft.graph.depOnboardingSetting entity.
        """
        return imported_apple_device_identities_request_builder.ImportedAppleDeviceIdentitiesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def share_for_school_data_sync_service(self) -> share_for_school_data_sync_service_request_builder.ShareForSchoolDataSyncServiceRequestBuilder:
        """
        Provides operations to call the shareForSchoolDataSyncService method.
        """
        return share_for_school_data_sync_service_request_builder.ShareForSchoolDataSyncServiceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sync_with_apple_device_enrollment_program(self) -> sync_with_apple_device_enrollment_program_request_builder.SyncWithAppleDeviceEnrollmentProgramRequestBuilder:
        """
        Provides operations to call the syncWithAppleDeviceEnrollmentProgram method.
        """
        return sync_with_apple_device_enrollment_program_request_builder.SyncWithAppleDeviceEnrollmentProgramRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def unshare_for_school_data_sync_service(self) -> unshare_for_school_data_sync_service_request_builder.UnshareForSchoolDataSyncServiceRequestBuilder:
        """
        Provides operations to call the unshareForSchoolDataSyncService method.
        """
        return unshare_for_school_data_sync_service_request_builder.UnshareForSchoolDataSyncServiceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def upload_dep_token(self) -> upload_dep_token_request_builder.UploadDepTokenRequestBuilder:
        """
        Provides operations to call the uploadDepToken method.
        """
        return upload_dep_token_request_builder.UploadDepTokenRequestBuilder(self.request_adapter, self.path_parameters)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new DepOnboardingSettingItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/deviceManagement/depOnboardingSettings/{depOnboardingSetting%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def create_delete_request_information(self,request_configuration: Optional[DepOnboardingSettingItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property depOnboardingSettings for deviceManagement
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.DELETE
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def create_get_request_information(self,request_configuration: Optional[DepOnboardingSettingItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        This collections of multiple DEP tokens per-tenant.
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
    
    def create_patch_request_information(self,body: Optional[dep_onboarding_setting.DepOnboardingSetting] = None, request_configuration: Optional[DepOnboardingSettingItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property depOnboardingSettings in deviceManagement
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
    
    async def delete(self,request_configuration: Optional[DepOnboardingSettingItemRequestBuilderDeleteRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> None:
        """
        Delete navigation property depOnboardingSettings for deviceManagement
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        """
        request_info = self.create_delete_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, response_handler, error_mapping)
    
    def enrollment_profiles_by_id(self,id: str) -> enrollment_profile_item_request_builder.EnrollmentProfileItemRequestBuilder:
        """
        Provides operations to manage the enrollmentProfiles property of the microsoft.graph.depOnboardingSetting entity.
        Args:
            id: Unique identifier of the item
        Returns: enrollment_profile_item_request_builder.EnrollmentProfileItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["enrollmentProfile%2Did"] = id
        return enrollment_profile_item_request_builder.EnrollmentProfileItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[DepOnboardingSettingItemRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[dep_onboarding_setting.DepOnboardingSetting]:
        """
        This collections of multiple DEP tokens per-tenant.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[dep_onboarding_setting.DepOnboardingSetting]
        """
        request_info = self.create_get_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, dep_onboarding_setting.DepOnboardingSetting, response_handler, error_mapping)
    
    def get_encryption_public_key(self,) -> get_encryption_public_key_request_builder.GetEncryptionPublicKeyRequestBuilder:
        """
        Provides operations to call the getEncryptionPublicKey method.
        Returns: get_encryption_public_key_request_builder.GetEncryptionPublicKeyRequestBuilder
        """
        return get_encryption_public_key_request_builder.GetEncryptionPublicKeyRequestBuilder(self.request_adapter, self.path_parameters)
    
    def imported_apple_device_identities_by_id(self,id: str) -> imported_apple_device_identity_item_request_builder.ImportedAppleDeviceIdentityItemRequestBuilder:
        """
        Provides operations to manage the importedAppleDeviceIdentities property of the microsoft.graph.depOnboardingSetting entity.
        Args:
            id: Unique identifier of the item
        Returns: imported_apple_device_identity_item_request_builder.ImportedAppleDeviceIdentityItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["importedAppleDeviceIdentity%2Did"] = id
        return imported_apple_device_identity_item_request_builder.ImportedAppleDeviceIdentityItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def patch(self,body: Optional[dep_onboarding_setting.DepOnboardingSetting] = None, request_configuration: Optional[DepOnboardingSettingItemRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[dep_onboarding_setting.DepOnboardingSetting]:
        """
        Update the navigation property depOnboardingSettings in deviceManagement
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[dep_onboarding_setting.DepOnboardingSetting]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.create_patch_request_information(
            body, request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, dep_onboarding_setting.DepOnboardingSetting, response_handler, error_mapping)
    
    @dataclass
    class DepOnboardingSettingItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class DepOnboardingSettingItemRequestBuilderGetQueryParameters():
        """
        This collections of multiple DEP tokens per-tenant.
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
    class DepOnboardingSettingItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[DepOnboardingSettingItemRequestBuilder.DepOnboardingSettingItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class DepOnboardingSettingItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

