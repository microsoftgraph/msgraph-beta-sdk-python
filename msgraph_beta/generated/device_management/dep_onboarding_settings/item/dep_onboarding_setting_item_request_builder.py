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
    from ....models.dep_onboarding_setting import DepOnboardingSetting
    from ....models.o_data_errors.o_data_error import ODataError
    from .default_ios_enrollment_profile.default_ios_enrollment_profile_request_builder import DefaultIosEnrollmentProfileRequestBuilder
    from .default_mac_os_enrollment_profile.default_mac_os_enrollment_profile_request_builder import DefaultMacOsEnrollmentProfileRequestBuilder
    from .enrollment_profiles.enrollment_profiles_request_builder import EnrollmentProfilesRequestBuilder
    from .generate_encryption_public_key.generate_encryption_public_key_request_builder import GenerateEncryptionPublicKeyRequestBuilder
    from .get_encryption_public_key.get_encryption_public_key_request_builder import GetEncryptionPublicKeyRequestBuilder
    from .imported_apple_device_identities.imported_apple_device_identities_request_builder import ImportedAppleDeviceIdentitiesRequestBuilder
    from .share_for_school_data_sync_service.share_for_school_data_sync_service_request_builder import ShareForSchoolDataSyncServiceRequestBuilder
    from .sync_with_apple_device_enrollment_program.sync_with_apple_device_enrollment_program_request_builder import SyncWithAppleDeviceEnrollmentProgramRequestBuilder
    from .unshare_for_school_data_sync_service.unshare_for_school_data_sync_service_request_builder import UnshareForSchoolDataSyncServiceRequestBuilder
    from .upload_dep_token.upload_dep_token_request_builder import UploadDepTokenRequestBuilder

class DepOnboardingSettingItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the depOnboardingSettings property of the microsoft.graph.deviceManagement entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new DepOnboardingSettingItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/deviceManagement/depOnboardingSettings/{depOnboardingSetting%2Did}{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete navigation property depOnboardingSettings for deviceManagement
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[DepOnboardingSettingItemRequestBuilderGetQueryParameters]] = None) -> Optional[DepOnboardingSetting]:
        """
        This collections of multiple DEP tokens per-tenant.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[DepOnboardingSetting]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.dep_onboarding_setting import DepOnboardingSetting

        return await self.request_adapter.send_async(request_info, DepOnboardingSetting, error_mapping)
    
    async def patch(self,body: DepOnboardingSetting, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[DepOnboardingSetting]:
        """
        Update the navigation property depOnboardingSettings in deviceManagement
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[DepOnboardingSetting]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.dep_onboarding_setting import DepOnboardingSetting

        return await self.request_adapter.send_async(request_info, DepOnboardingSetting, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete navigation property depOnboardingSettings for deviceManagement
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[DepOnboardingSettingItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        This collections of multiple DEP tokens per-tenant.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: DepOnboardingSetting, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the navigation property depOnboardingSettings in deviceManagement
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
    
    def with_url(self,raw_url: str) -> DepOnboardingSettingItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: DepOnboardingSettingItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return DepOnboardingSettingItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def default_ios_enrollment_profile(self) -> DefaultIosEnrollmentProfileRequestBuilder:
        """
        Provides operations to manage the defaultIosEnrollmentProfile property of the microsoft.graph.depOnboardingSetting entity.
        """
        from .default_ios_enrollment_profile.default_ios_enrollment_profile_request_builder import DefaultIosEnrollmentProfileRequestBuilder

        return DefaultIosEnrollmentProfileRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def default_mac_os_enrollment_profile(self) -> DefaultMacOsEnrollmentProfileRequestBuilder:
        """
        Provides operations to manage the defaultMacOsEnrollmentProfile property of the microsoft.graph.depOnboardingSetting entity.
        """
        from .default_mac_os_enrollment_profile.default_mac_os_enrollment_profile_request_builder import DefaultMacOsEnrollmentProfileRequestBuilder

        return DefaultMacOsEnrollmentProfileRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def enrollment_profiles(self) -> EnrollmentProfilesRequestBuilder:
        """
        Provides operations to manage the enrollmentProfiles property of the microsoft.graph.depOnboardingSetting entity.
        """
        from .enrollment_profiles.enrollment_profiles_request_builder import EnrollmentProfilesRequestBuilder

        return EnrollmentProfilesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def generate_encryption_public_key(self) -> GenerateEncryptionPublicKeyRequestBuilder:
        """
        Provides operations to call the generateEncryptionPublicKey method.
        """
        from .generate_encryption_public_key.generate_encryption_public_key_request_builder import GenerateEncryptionPublicKeyRequestBuilder

        return GenerateEncryptionPublicKeyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_encryption_public_key(self) -> GetEncryptionPublicKeyRequestBuilder:
        """
        Provides operations to call the getEncryptionPublicKey method.
        """
        from .get_encryption_public_key.get_encryption_public_key_request_builder import GetEncryptionPublicKeyRequestBuilder

        return GetEncryptionPublicKeyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def imported_apple_device_identities(self) -> ImportedAppleDeviceIdentitiesRequestBuilder:
        """
        Provides operations to manage the importedAppleDeviceIdentities property of the microsoft.graph.depOnboardingSetting entity.
        """
        from .imported_apple_device_identities.imported_apple_device_identities_request_builder import ImportedAppleDeviceIdentitiesRequestBuilder

        return ImportedAppleDeviceIdentitiesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def share_for_school_data_sync_service(self) -> ShareForSchoolDataSyncServiceRequestBuilder:
        """
        Provides operations to call the shareForSchoolDataSyncService method.
        """
        from .share_for_school_data_sync_service.share_for_school_data_sync_service_request_builder import ShareForSchoolDataSyncServiceRequestBuilder

        return ShareForSchoolDataSyncServiceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sync_with_apple_device_enrollment_program(self) -> SyncWithAppleDeviceEnrollmentProgramRequestBuilder:
        """
        Provides operations to call the syncWithAppleDeviceEnrollmentProgram method.
        """
        from .sync_with_apple_device_enrollment_program.sync_with_apple_device_enrollment_program_request_builder import SyncWithAppleDeviceEnrollmentProgramRequestBuilder

        return SyncWithAppleDeviceEnrollmentProgramRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def unshare_for_school_data_sync_service(self) -> UnshareForSchoolDataSyncServiceRequestBuilder:
        """
        Provides operations to call the unshareForSchoolDataSyncService method.
        """
        from .unshare_for_school_data_sync_service.unshare_for_school_data_sync_service_request_builder import UnshareForSchoolDataSyncServiceRequestBuilder

        return UnshareForSchoolDataSyncServiceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def upload_dep_token(self) -> UploadDepTokenRequestBuilder:
        """
        Provides operations to call the uploadDepToken method.
        """
        from .upload_dep_token.upload_dep_token_request_builder import UploadDepTokenRequestBuilder

        return UploadDepTokenRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class DepOnboardingSettingItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class DepOnboardingSettingItemRequestBuilderGetQueryParameters():
        """
        This collections of multiple DEP tokens per-tenant.
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
    class DepOnboardingSettingItemRequestBuilderGetRequestConfiguration(RequestConfiguration[DepOnboardingSettingItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class DepOnboardingSettingItemRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

