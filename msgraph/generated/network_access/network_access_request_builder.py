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
    from ..models.networkaccess.network_access_root import NetworkAccessRoot
    from ..models.o_data_errors.o_data_error import ODataError
    from .connectivity.connectivity_request_builder import ConnectivityRequestBuilder
    from .forwarding_policies.forwarding_policies_request_builder import ForwardingPoliciesRequestBuilder
    from .forwarding_profiles.forwarding_profiles_request_builder import ForwardingProfilesRequestBuilder
    from .logs.logs_request_builder import LogsRequestBuilder
    from .microsoft_graph_networkaccess_onboard.microsoft_graph_networkaccess_onboard_request_builder import MicrosoftGraphNetworkaccessOnboardRequestBuilder
    from .reports.reports_request_builder import ReportsRequestBuilder
    from .settings.settings_request_builder import SettingsRequestBuilder
    from .tenant_status.tenant_status_request_builder import TenantStatusRequestBuilder

class NetworkAccessRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the networkAccessRoot singleton.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new NetworkAccessRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/networkAccess{?%24select,%24expand}", path_parameters)
    
    async def get(self,request_configuration: Optional[NetworkAccessRequestBuilderGetRequestConfiguration] = None) -> Optional[NetworkAccessRoot]:
        """
        Get networkAccess
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[NetworkAccessRoot]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ..models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.networkaccess.network_access_root import NetworkAccessRoot

        return await self.request_adapter.send_async(request_info, NetworkAccessRoot, error_mapping)
    
    async def patch(self,body: Optional[NetworkAccessRoot] = None, request_configuration: Optional[NetworkAccessRequestBuilderPatchRequestConfiguration] = None) -> Optional[NetworkAccessRoot]:
        """
        Update networkAccess
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[NetworkAccessRoot]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ..models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.networkaccess.network_access_root import NetworkAccessRoot

        return await self.request_adapter.send_async(request_info, NetworkAccessRoot, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[NetworkAccessRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get networkAccess
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
        request_info.headers.try_add("Accept", "application/json;q=1")
        return request_info
    
    def to_patch_request_information(self,body: Optional[NetworkAccessRoot] = None, request_configuration: Optional[NetworkAccessRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update networkAccess
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
        request_info.headers.try_add("Accept", "application/json;q=1")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> NetworkAccessRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: NetworkAccessRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return NetworkAccessRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def connectivity(self) -> ConnectivityRequestBuilder:
        """
        Provides operations to manage the connectivity property of the microsoft.graph.networkaccess.networkAccessRoot entity.
        """
        from .connectivity.connectivity_request_builder import ConnectivityRequestBuilder

        return ConnectivityRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def forwarding_policies(self) -> ForwardingPoliciesRequestBuilder:
        """
        Provides operations to manage the forwardingPolicies property of the microsoft.graph.networkaccess.networkAccessRoot entity.
        """
        from .forwarding_policies.forwarding_policies_request_builder import ForwardingPoliciesRequestBuilder

        return ForwardingPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def forwarding_profiles(self) -> ForwardingProfilesRequestBuilder:
        """
        Provides operations to manage the forwardingProfiles property of the microsoft.graph.networkaccess.networkAccessRoot entity.
        """
        from .forwarding_profiles.forwarding_profiles_request_builder import ForwardingProfilesRequestBuilder

        return ForwardingProfilesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def logs(self) -> LogsRequestBuilder:
        """
        Provides operations to manage the logs property of the microsoft.graph.networkaccess.networkAccessRoot entity.
        """
        from .logs.logs_request_builder import LogsRequestBuilder

        return LogsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_networkaccess_onboard(self) -> MicrosoftGraphNetworkaccessOnboardRequestBuilder:
        """
        Provides operations to call the onboard method.
        """
        from .microsoft_graph_networkaccess_onboard.microsoft_graph_networkaccess_onboard_request_builder import MicrosoftGraphNetworkaccessOnboardRequestBuilder

        return MicrosoftGraphNetworkaccessOnboardRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reports(self) -> ReportsRequestBuilder:
        """
        Provides operations to manage the reports property of the microsoft.graph.networkaccess.networkAccessRoot entity.
        """
        from .reports.reports_request_builder import ReportsRequestBuilder

        return ReportsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def settings(self) -> SettingsRequestBuilder:
        """
        Provides operations to manage the settings property of the microsoft.graph.networkaccess.networkAccessRoot entity.
        """
        from .settings.settings_request_builder import SettingsRequestBuilder

        return SettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tenant_status(self) -> TenantStatusRequestBuilder:
        """
        Provides operations to manage the tenantStatus property of the microsoft.graph.networkaccess.networkAccessRoot entity.
        """
        from .tenant_status.tenant_status_request_builder import TenantStatusRequestBuilder

        return TenantStatusRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class NetworkAccessRequestBuilderGetQueryParameters():
        """
        Get networkAccess
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
    class NetworkAccessRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[NetworkAccessRequestBuilder.NetworkAccessRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class NetworkAccessRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

