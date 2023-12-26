from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ...models.android_managed_store_account_enterprise_settings import AndroidManagedStoreAccountEnterpriseSettings
    from ...models.o_data_errors.o_data_error import ODataError
    from .add_apps.add_apps_request_builder import AddAppsRequestBuilder
    from .approve_apps.approve_apps_request_builder import ApproveAppsRequestBuilder
    from .complete_signup.complete_signup_request_builder import CompleteSignupRequestBuilder
    from .create_google_play_web_token.create_google_play_web_token_request_builder import CreateGooglePlayWebTokenRequestBuilder
    from .request_signup_url.request_signup_url_request_builder import RequestSignupUrlRequestBuilder
    from .set_android_device_owner_fully_managed_enrollment_state.set_android_device_owner_fully_managed_enrollment_state_request_builder import SetAndroidDeviceOwnerFullyManagedEnrollmentStateRequestBuilder
    from .sync_apps.sync_apps_request_builder import SyncAppsRequestBuilder
    from .unbind.unbind_request_builder import UnbindRequestBuilder

class AndroidManagedStoreAccountEnterpriseSettingsRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the androidManagedStoreAccountEnterpriseSettings property of the microsoft.graph.deviceManagement entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new AndroidManagedStoreAccountEnterpriseSettingsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/deviceManagement/androidManagedStoreAccountEnterpriseSettings{?%24select,%24expand}", path_parameters)
    
    async def delete(self,request_configuration: Optional[AndroidManagedStoreAccountEnterpriseSettingsRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property androidManagedStoreAccountEnterpriseSettings for deviceManagement
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[AndroidManagedStoreAccountEnterpriseSettingsRequestBuilderGetRequestConfiguration] = None) -> Optional[AndroidManagedStoreAccountEnterpriseSettings]:
        """
        The singleton Android managed store account enterprise settings entity.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[AndroidManagedStoreAccountEnterpriseSettings]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.android_managed_store_account_enterprise_settings import AndroidManagedStoreAccountEnterpriseSettings

        return await self.request_adapter.send_async(request_info, AndroidManagedStoreAccountEnterpriseSettings, error_mapping)
    
    async def patch(self,body: Optional[AndroidManagedStoreAccountEnterpriseSettings] = None, request_configuration: Optional[AndroidManagedStoreAccountEnterpriseSettingsRequestBuilderPatchRequestConfiguration] = None) -> Optional[AndroidManagedStoreAccountEnterpriseSettings]:
        """
        Update the navigation property androidManagedStoreAccountEnterpriseSettings in deviceManagement
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[AndroidManagedStoreAccountEnterpriseSettings]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.android_managed_store_account_enterprise_settings import AndroidManagedStoreAccountEnterpriseSettings

        return await self.request_adapter.send_async(request_info, AndroidManagedStoreAccountEnterpriseSettings, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[AndroidManagedStoreAccountEnterpriseSettingsRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property androidManagedStoreAccountEnterpriseSettings for deviceManagement
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.DELETE
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[AndroidManagedStoreAccountEnterpriseSettingsRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        The singleton Android managed store account enterprise settings entity.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: Optional[AndroidManagedStoreAccountEnterpriseSettings] = None, request_configuration: Optional[AndroidManagedStoreAccountEnterpriseSettingsRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property androidManagedStoreAccountEnterpriseSettings in deviceManagement
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.PATCH
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> AndroidManagedStoreAccountEnterpriseSettingsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: AndroidManagedStoreAccountEnterpriseSettingsRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return AndroidManagedStoreAccountEnterpriseSettingsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def add_apps(self) -> AddAppsRequestBuilder:
        """
        Provides operations to call the addApps method.
        """
        from .add_apps.add_apps_request_builder import AddAppsRequestBuilder

        return AddAppsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def approve_apps(self) -> ApproveAppsRequestBuilder:
        """
        Provides operations to call the approveApps method.
        """
        from .approve_apps.approve_apps_request_builder import ApproveAppsRequestBuilder

        return ApproveAppsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def complete_signup(self) -> CompleteSignupRequestBuilder:
        """
        Provides operations to call the completeSignup method.
        """
        from .complete_signup.complete_signup_request_builder import CompleteSignupRequestBuilder

        return CompleteSignupRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def create_google_play_web_token(self) -> CreateGooglePlayWebTokenRequestBuilder:
        """
        Provides operations to call the createGooglePlayWebToken method.
        """
        from .create_google_play_web_token.create_google_play_web_token_request_builder import CreateGooglePlayWebTokenRequestBuilder

        return CreateGooglePlayWebTokenRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def request_signup_url(self) -> RequestSignupUrlRequestBuilder:
        """
        Provides operations to call the requestSignupUrl method.
        """
        from .request_signup_url.request_signup_url_request_builder import RequestSignupUrlRequestBuilder

        return RequestSignupUrlRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def set_android_device_owner_fully_managed_enrollment_state(self) -> SetAndroidDeviceOwnerFullyManagedEnrollmentStateRequestBuilder:
        """
        Provides operations to call the setAndroidDeviceOwnerFullyManagedEnrollmentState method.
        """
        from .set_android_device_owner_fully_managed_enrollment_state.set_android_device_owner_fully_managed_enrollment_state_request_builder import SetAndroidDeviceOwnerFullyManagedEnrollmentStateRequestBuilder

        return SetAndroidDeviceOwnerFullyManagedEnrollmentStateRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sync_apps(self) -> SyncAppsRequestBuilder:
        """
        Provides operations to call the syncApps method.
        """
        from .sync_apps.sync_apps_request_builder import SyncAppsRequestBuilder

        return SyncAppsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def unbind(self) -> UnbindRequestBuilder:
        """
        Provides operations to call the unbind method.
        """
        from .unbind.unbind_request_builder import UnbindRequestBuilder

        return UnbindRequestBuilder(self.request_adapter, self.path_parameters)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class AndroidManagedStoreAccountEnterpriseSettingsRequestBuilderDeleteRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
    @dataclass
    class AndroidManagedStoreAccountEnterpriseSettingsRequestBuilderGetQueryParameters():
        """
        The singleton Android managed store account enterprise settings entity.
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
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

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class AndroidManagedStoreAccountEnterpriseSettingsRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[AndroidManagedStoreAccountEnterpriseSettingsRequestBuilder.AndroidManagedStoreAccountEnterpriseSettingsRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class AndroidManagedStoreAccountEnterpriseSettingsRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

