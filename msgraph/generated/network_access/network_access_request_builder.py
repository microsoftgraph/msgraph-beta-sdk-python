from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..models.networkaccess import network_access_root
    from ..models.o_data_errors import o_data_error
    from .connectivity import connectivity_request_builder
    from .forwarding_policies import forwarding_policies_request_builder
    from .forwarding_profiles import forwarding_profiles_request_builder
    from .logs import logs_request_builder
    from .microsoft_graph_networkaccess_onboard import microsoft_graph_networkaccess_onboard_request_builder
    from .reports import reports_request_builder
    from .settings import settings_request_builder
    from .tenant_status import tenant_status_request_builder

class NetworkAccessRequestBuilder():
    """
    Provides operations to manage the networkAccessRoot singleton.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new NetworkAccessRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if not path_parameters:
            raise TypeError("path_parameters cannot be null.")
        if not request_adapter:
            raise TypeError("request_adapter cannot be null.")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/networkAccess{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def get(self,request_configuration: Optional[NetworkAccessRequestBuilderGetRequestConfiguration] = None) -> Optional[network_access_root.NetworkAccessRoot]:
        """
        Get networkAccess
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[network_access_root.NetworkAccessRoot]
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
        from ..models.networkaccess import network_access_root

        return await self.request_adapter.send_async(request_info, network_access_root.NetworkAccessRoot, error_mapping)
    
    async def patch(self,body: Optional[network_access_root.NetworkAccessRoot] = None, request_configuration: Optional[NetworkAccessRequestBuilderPatchRequestConfiguration] = None) -> Optional[network_access_root.NetworkAccessRoot]:
        """
        Update networkAccess
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[network_access_root.NetworkAccessRoot]
        """
        if not body:
            raise TypeError("body cannot be null.")
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
        from ..models.networkaccess import network_access_root

        return await self.request_adapter.send_async(request_info, network_access_root.NetworkAccessRoot, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[NetworkAccessRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get networkAccess
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
    
    def to_patch_request_information(self,body: Optional[network_access_root.NetworkAccessRoot] = None, request_configuration: Optional[NetworkAccessRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update networkAccess
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
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
    def connectivity(self) -> connectivity_request_builder.ConnectivityRequestBuilder:
        """
        Provides operations to manage the connectivity property of the microsoft.graph.networkaccess.networkAccessRoot entity.
        """
        from .connectivity import connectivity_request_builder

        return connectivity_request_builder.ConnectivityRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def forwarding_policies(self) -> forwarding_policies_request_builder.ForwardingPoliciesRequestBuilder:
        """
        Provides operations to manage the forwardingPolicies property of the microsoft.graph.networkaccess.networkAccessRoot entity.
        """
        from .forwarding_policies import forwarding_policies_request_builder

        return forwarding_policies_request_builder.ForwardingPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def forwarding_profiles(self) -> forwarding_profiles_request_builder.ForwardingProfilesRequestBuilder:
        """
        Provides operations to manage the forwardingProfiles property of the microsoft.graph.networkaccess.networkAccessRoot entity.
        """
        from .forwarding_profiles import forwarding_profiles_request_builder

        return forwarding_profiles_request_builder.ForwardingProfilesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def logs(self) -> logs_request_builder.LogsRequestBuilder:
        """
        Provides operations to manage the logs property of the microsoft.graph.networkaccess.networkAccessRoot entity.
        """
        from .logs import logs_request_builder

        return logs_request_builder.LogsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_networkaccess_onboard(self) -> microsoft_graph_networkaccess_onboard_request_builder.MicrosoftGraphNetworkaccessOnboardRequestBuilder:
        """
        Provides operations to call the onboard method.
        """
        from .microsoft_graph_networkaccess_onboard import microsoft_graph_networkaccess_onboard_request_builder

        return microsoft_graph_networkaccess_onboard_request_builder.MicrosoftGraphNetworkaccessOnboardRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reports(self) -> reports_request_builder.ReportsRequestBuilder:
        """
        Provides operations to manage the reports property of the microsoft.graph.networkaccess.networkAccessRoot entity.
        """
        from .reports import reports_request_builder

        return reports_request_builder.ReportsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def settings(self) -> settings_request_builder.SettingsRequestBuilder:
        """
        Provides operations to manage the settings property of the microsoft.graph.networkaccess.networkAccessRoot entity.
        """
        from .settings import settings_request_builder

        return settings_request_builder.SettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tenant_status(self) -> tenant_status_request_builder.TenantStatusRequestBuilder:
        """
        Provides operations to manage the tenantStatus property of the microsoft.graph.networkaccess.networkAccessRoot entity.
        """
        from .tenant_status import tenant_status_request_builder

        return tenant_status_request_builder.TenantStatusRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class NetworkAccessRequestBuilderGetQueryParameters():
        """
        Get networkAccess
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            Args:
                originalName: The original query parameter name in the class.
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

    
    @dataclass
    class NetworkAccessRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[NetworkAccessRequestBuilder.NetworkAccessRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class NetworkAccessRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

