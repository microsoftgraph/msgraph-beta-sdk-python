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
    from ...models import android_managed_store_account_enterprise_settings
    from ...models.o_data_errors import o_data_error
    from .add_apps import add_apps_request_builder
    from .approve_apps import approve_apps_request_builder
    from .complete_signup import complete_signup_request_builder
    from .create_google_play_web_token import create_google_play_web_token_request_builder
    from .request_signup_url import request_signup_url_request_builder
    from .set_android_device_owner_fully_managed_enrollment_state import set_android_device_owner_fully_managed_enrollment_state_request_builder
    from .sync_apps import sync_apps_request_builder
    from .unbind import unbind_request_builder

class AndroidManagedStoreAccountEnterpriseSettingsRequestBuilder():
    """
    Provides operations to manage the androidManagedStoreAccountEnterpriseSettings property of the microsoft.graph.deviceManagement entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new AndroidManagedStoreAccountEnterpriseSettingsRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/deviceManagement/androidManagedStoreAccountEnterpriseSettings{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[AndroidManagedStoreAccountEnterpriseSettingsRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property androidManagedStoreAccountEnterpriseSettings for deviceManagement
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ...models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[AndroidManagedStoreAccountEnterpriseSettingsRequestBuilderGetRequestConfiguration] = None) -> Optional[android_managed_store_account_enterprise_settings.AndroidManagedStoreAccountEnterpriseSettings]:
        """
        The singleton Android managed store account enterprise settings entity.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[android_managed_store_account_enterprise_settings.AndroidManagedStoreAccountEnterpriseSettings]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models import android_managed_store_account_enterprise_settings

        return await self.request_adapter.send_async(request_info, android_managed_store_account_enterprise_settings.AndroidManagedStoreAccountEnterpriseSettings, error_mapping)
    
    async def patch(self,body: Optional[android_managed_store_account_enterprise_settings.AndroidManagedStoreAccountEnterpriseSettings] = None, request_configuration: Optional[AndroidManagedStoreAccountEnterpriseSettingsRequestBuilderPatchRequestConfiguration] = None) -> Optional[android_managed_store_account_enterprise_settings.AndroidManagedStoreAccountEnterpriseSettings]:
        """
        Update the navigation property androidManagedStoreAccountEnterpriseSettings in deviceManagement
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[android_managed_store_account_enterprise_settings.AndroidManagedStoreAccountEnterpriseSettings]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ...models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models import android_managed_store_account_enterprise_settings

        return await self.request_adapter.send_async(request_info, android_managed_store_account_enterprise_settings.AndroidManagedStoreAccountEnterpriseSettings, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[AndroidManagedStoreAccountEnterpriseSettingsRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property androidManagedStoreAccountEnterpriseSettings for deviceManagement
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
    
    def to_get_request_information(self,request_configuration: Optional[AndroidManagedStoreAccountEnterpriseSettingsRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        The singleton Android managed store account enterprise settings entity.
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
    
    def to_patch_request_information(self,body: Optional[android_managed_store_account_enterprise_settings.AndroidManagedStoreAccountEnterpriseSettings] = None, request_configuration: Optional[AndroidManagedStoreAccountEnterpriseSettingsRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property androidManagedStoreAccountEnterpriseSettings in deviceManagement
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
    def add_apps(self) -> add_apps_request_builder.AddAppsRequestBuilder:
        """
        Provides operations to call the addApps method.
        """
        from .add_apps import add_apps_request_builder

        return add_apps_request_builder.AddAppsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def approve_apps(self) -> approve_apps_request_builder.ApproveAppsRequestBuilder:
        """
        Provides operations to call the approveApps method.
        """
        from .approve_apps import approve_apps_request_builder

        return approve_apps_request_builder.ApproveAppsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def complete_signup(self) -> complete_signup_request_builder.CompleteSignupRequestBuilder:
        """
        Provides operations to call the completeSignup method.
        """
        from .complete_signup import complete_signup_request_builder

        return complete_signup_request_builder.CompleteSignupRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def create_google_play_web_token(self) -> create_google_play_web_token_request_builder.CreateGooglePlayWebTokenRequestBuilder:
        """
        Provides operations to call the createGooglePlayWebToken method.
        """
        from .create_google_play_web_token import create_google_play_web_token_request_builder

        return create_google_play_web_token_request_builder.CreateGooglePlayWebTokenRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def request_signup_url(self) -> request_signup_url_request_builder.RequestSignupUrlRequestBuilder:
        """
        Provides operations to call the requestSignupUrl method.
        """
        from .request_signup_url import request_signup_url_request_builder

        return request_signup_url_request_builder.RequestSignupUrlRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def set_android_device_owner_fully_managed_enrollment_state(self) -> set_android_device_owner_fully_managed_enrollment_state_request_builder.SetAndroidDeviceOwnerFullyManagedEnrollmentStateRequestBuilder:
        """
        Provides operations to call the setAndroidDeviceOwnerFullyManagedEnrollmentState method.
        """
        from .set_android_device_owner_fully_managed_enrollment_state import set_android_device_owner_fully_managed_enrollment_state_request_builder

        return set_android_device_owner_fully_managed_enrollment_state_request_builder.SetAndroidDeviceOwnerFullyManagedEnrollmentStateRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sync_apps(self) -> sync_apps_request_builder.SyncAppsRequestBuilder:
        """
        Provides operations to call the syncApps method.
        """
        from .sync_apps import sync_apps_request_builder

        return sync_apps_request_builder.SyncAppsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def unbind(self) -> unbind_request_builder.UnbindRequestBuilder:
        """
        Provides operations to call the unbind method.
        """
        from .unbind import unbind_request_builder

        return unbind_request_builder.UnbindRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class AndroidManagedStoreAccountEnterpriseSettingsRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class AndroidManagedStoreAccountEnterpriseSettingsRequestBuilderGetQueryParameters():
        """
        The singleton Android managed store account enterprise settings entity.
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
    class AndroidManagedStoreAccountEnterpriseSettingsRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[AndroidManagedStoreAccountEnterpriseSettingsRequestBuilder.AndroidManagedStoreAccountEnterpriseSettingsRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class AndroidManagedStoreAccountEnterpriseSettingsRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

