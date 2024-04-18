from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from warnings import warn

if TYPE_CHECKING:
    from .....models.networkaccess.branch_site import BranchSite
    from .....models.o_data_errors.o_data_error import ODataError
    from .connectivity_configuration.connectivity_configuration_request_builder import ConnectivityConfigurationRequestBuilder
    from .device_links.device_links_request_builder import DeviceLinksRequestBuilder
    from .forwarding_profiles.forwarding_profiles_request_builder import ForwardingProfilesRequestBuilder

class BranchSiteItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the branches property of the microsoft.graph.networkaccess.connectivity entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new BranchSiteItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/networkAccess/connectivity/branches/{branchSite%2Did}{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration] = None) -> None:
        """
        Delete a specific branch.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        Find more info here: https://learn.microsoft.com/graph/api/networkaccess-branchsite-delete?view=graph-rest-1.0
        """
        warn("The Branches API is deprecated and will stop returning data on March 20, 2024. Please use the new Remote Network API. as of 2022-06/PrivatePreview:NetworkAccess", DeprecationWarning)
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration] = None) -> Optional[BranchSite]:
        """
        Retrieve information about a specific branch.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[BranchSite]
        Find more info here: https://learn.microsoft.com/graph/api/networkaccess-branchsite-get?view=graph-rest-1.0
        """
        warn("The Branches API is deprecated and will stop returning data on March 20, 2024. Please use the new Remote Network API. as of 2022-06/PrivatePreview:NetworkAccess", DeprecationWarning)
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.networkaccess.branch_site import BranchSite

        return await self.request_adapter.send_async(request_info, BranchSite, error_mapping)
    
    async def patch(self,body: Optional[BranchSite] = None, request_configuration: Optional[RequestConfiguration] = None) -> Optional[BranchSite]:
        """
        Update the configuration or properties of a specific branch.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[BranchSite]
        Find more info here: https://learn.microsoft.com/graph/api/networkaccess-branchsite-update?view=graph-rest-1.0
        """
        warn("The Branches API is deprecated and will stop returning data on March 20, 2024. Please use the new Remote Network API. as of 2022-06/PrivatePreview:NetworkAccess", DeprecationWarning)
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.networkaccess.branch_site import BranchSite

        return await self.request_adapter.send_async(request_info, BranchSite, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        Delete a specific branch.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        warn("The Branches API is deprecated and will stop returning data on March 20, 2024. Please use the new Remote Network API. as of 2022-06/PrivatePreview:NetworkAccess", DeprecationWarning)
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        Retrieve information about a specific branch.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        warn("The Branches API is deprecated and will stop returning data on March 20, 2024. Please use the new Remote Network API. as of 2022-06/PrivatePreview:NetworkAccess", DeprecationWarning)
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: Optional[BranchSite] = None, request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        Update the configuration or properties of a specific branch.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        warn("The Branches API is deprecated and will stop returning data on March 20, 2024. Please use the new Remote Network API. as of 2022-06/PrivatePreview:NetworkAccess", DeprecationWarning)
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PATCH, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> BranchSiteItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: BranchSiteItemRequestBuilder
        """
        warn("The Branches API is deprecated and will stop returning data on March 20, 2024. Please use the new Remote Network API. as of 2022-06/PrivatePreview:NetworkAccess", DeprecationWarning)
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return BranchSiteItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def connectivity_configuration(self) -> ConnectivityConfigurationRequestBuilder:
        """
        Provides operations to manage the connectivityConfiguration property of the microsoft.graph.networkaccess.branchSite entity.
        """
        from .connectivity_configuration.connectivity_configuration_request_builder import ConnectivityConfigurationRequestBuilder

        return ConnectivityConfigurationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_links(self) -> DeviceLinksRequestBuilder:
        """
        Provides operations to manage the deviceLinks property of the microsoft.graph.networkaccess.branchSite entity.
        """
        from .device_links.device_links_request_builder import DeviceLinksRequestBuilder

        return DeviceLinksRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def forwarding_profiles(self) -> ForwardingProfilesRequestBuilder:
        """
        Provides operations to manage the forwardingProfiles property of the microsoft.graph.networkaccess.branchSite entity.
        """
        from .forwarding_profiles.forwarding_profiles_request_builder import ForwardingProfilesRequestBuilder

        return ForwardingProfilesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class BranchSiteItemRequestBuilderGetQueryParameters():
        """
        Retrieve information about a specific branch.
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

    

