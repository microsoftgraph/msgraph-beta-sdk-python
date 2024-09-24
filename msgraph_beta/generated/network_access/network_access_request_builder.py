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
    from ..models.networkaccess.network_access_root import NetworkAccessRoot
    from ..models.o_data_errors.o_data_error import ODataError
    from .alerts.alerts_request_builder import AlertsRequestBuilder
    from .connectivity.connectivity_request_builder import ConnectivityRequestBuilder
    from .filtering_policies.filtering_policies_request_builder import FilteringPoliciesRequestBuilder
    from .filtering_profiles.filtering_profiles_request_builder import FilteringProfilesRequestBuilder
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
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new NetworkAccessRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/networkAccess{?%24expand,%24select}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[NetworkAccessRequestBuilderGetQueryParameters]] = None) -> Optional[NetworkAccessRoot]:
        """
        Get networkAccess
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[NetworkAccessRoot]
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
        from ..models.networkaccess.network_access_root import NetworkAccessRoot

        return await self.request_adapter.send_async(request_info, NetworkAccessRoot, error_mapping)
    
    async def patch(self,body: NetworkAccessRoot, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[NetworkAccessRoot]:
        """
        Update networkAccess
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[NetworkAccessRoot]
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
        from ..models.networkaccess.network_access_root import NetworkAccessRoot

        return await self.request_adapter.send_async(request_info, NetworkAccessRoot, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[NetworkAccessRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Get networkAccess
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: NetworkAccessRoot, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update networkAccess
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
    
    def with_url(self,raw_url: str) -> NetworkAccessRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: NetworkAccessRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return NetworkAccessRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def alerts(self) -> AlertsRequestBuilder:
        """
        Provides operations to manage the alerts property of the microsoft.graph.networkaccess.networkAccessRoot entity.
        """
        from .alerts.alerts_request_builder import AlertsRequestBuilder

        return AlertsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def connectivity(self) -> ConnectivityRequestBuilder:
        """
        Provides operations to manage the connectivity property of the microsoft.graph.networkaccess.networkAccessRoot entity.
        """
        from .connectivity.connectivity_request_builder import ConnectivityRequestBuilder

        return ConnectivityRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def filtering_policies(self) -> FilteringPoliciesRequestBuilder:
        """
        Provides operations to manage the filteringPolicies property of the microsoft.graph.networkaccess.networkAccessRoot entity.
        """
        from .filtering_policies.filtering_policies_request_builder import FilteringPoliciesRequestBuilder

        return FilteringPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def filtering_profiles(self) -> FilteringProfilesRequestBuilder:
        """
        Provides operations to manage the filteringProfiles property of the microsoft.graph.networkaccess.networkAccessRoot entity.
        """
        from .filtering_profiles.filtering_profiles_request_builder import FilteringProfilesRequestBuilder

        return FilteringProfilesRequestBuilder(self.request_adapter, self.path_parameters)
    
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
    class NetworkAccessRequestBuilderGetRequestConfiguration(RequestConfiguration[NetworkAccessRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class NetworkAccessRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

