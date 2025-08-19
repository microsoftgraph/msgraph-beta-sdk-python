from __future__ import annotations
from collections.abc import Callable
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
from typing import Any, Optional, TYPE_CHECKING, Union
from warnings import warn

if TYPE_CHECKING:
    from .....models.o_data_errors.o_data_error import ODataError
    from .retrieve_discovered_apps_with_source_idprovisioning_policy_id_provisioning_policy_id_get_response import RetrieveDiscoveredAppsWithSourceIdprovisioningPolicyIdProvisioningPolicyIdGetResponse

class RetrieveDiscoveredAppsWithSourceIdprovisioningPolicyIdProvisioningPolicyIdRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to call the retrieveDiscoveredApps method.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]], source_id: Optional[str] = None) -> None:
        """
        Instantiates a new RetrieveDiscoveredAppsWithSourceIdprovisioningPolicyIdProvisioningPolicyIdRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        param source_id: Usage: sourceId='{sourceId}'
        Returns: None
        """
        if isinstance(path_parameters, dict):
            path_parameters['sourceId'] = source_id
        super().__init__(request_adapter, "{+baseurl}/deviceManagement/virtualEndpoint/cloudApps/retrieveDiscoveredApps(sourceId='{sourceId}',provisioningPolicyId='@provisioningPolicyId'){?%24count,%24filter,%24search,%24skip,%24top,provisioningPolicyId*}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[RetrieveDiscoveredAppsWithSourceIdprovisioningPolicyIdProvisioningPolicyIdRequestBuilderGetQueryParameters]] = None) -> Optional[RetrieveDiscoveredAppsWithSourceIdprovisioningPolicyIdProvisioningPolicyIdGetResponse]:
        """
        Get a list of cloudPcDiscoveredApp objects whose appdetails can be used to map to a cloudPcCloudApp object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[RetrieveDiscoveredAppsWithSourceIdprovisioningPolicyIdProvisioningPolicyIdGetResponse]
        Find more info here: https://learn.microsoft.com/graph/api/cloudpccloudapp-retrievediscoveredapps?view=graph-rest-beta
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .retrieve_discovered_apps_with_source_idprovisioning_policy_id_provisioning_policy_id_get_response import RetrieveDiscoveredAppsWithSourceIdprovisioningPolicyIdProvisioningPolicyIdGetResponse

        return await self.request_adapter.send_async(request_info, RetrieveDiscoveredAppsWithSourceIdprovisioningPolicyIdProvisioningPolicyIdGetResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[RetrieveDiscoveredAppsWithSourceIdprovisioningPolicyIdProvisioningPolicyIdRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Get a list of cloudPcDiscoveredApp objects whose appdetails can be used to map to a cloudPcCloudApp object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> RetrieveDiscoveredAppsWithSourceIdprovisioningPolicyIdProvisioningPolicyIdRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: RetrieveDiscoveredAppsWithSourceIdprovisioningPolicyIdProvisioningPolicyIdRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return RetrieveDiscoveredAppsWithSourceIdprovisioningPolicyIdProvisioningPolicyIdRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class RetrieveDiscoveredAppsWithSourceIdprovisioningPolicyIdProvisioningPolicyIdRequestBuilderGetQueryParameters():
        """
        Get a list of cloudPcDiscoveredApp objects whose appdetails can be used to map to a cloudPcCloudApp object.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "count":
                return "%24count"
            if original_name == "filter":
                return "%24filter"
            if original_name == "provisioning_policy_id":
                return "provisioningPolicyId"
            if original_name == "search":
                return "%24search"
            if original_name == "skip":
                return "%24skip"
            if original_name == "top":
                return "%24top"
            return original_name
        
        # Include count of items
        count: Optional[bool] = None

        # Filter items by property values
        filter: Optional[str] = None

        # Usage: provisioningPolicyId='@provisioningPolicyId'
        provisioning_policy_id: Optional[str] = None

        # Search items by search phrases
        search: Optional[str] = None

        # Skip the first n items
        skip: Optional[int] = None

        # Show only the first n items
        top: Optional[int] = None

    
    @dataclass
    class RetrieveDiscoveredAppsWithSourceIdprovisioningPolicyIdProvisioningPolicyIdRequestBuilderGetRequestConfiguration(RequestConfiguration[RetrieveDiscoveredAppsWithSourceIdprovisioningPolicyIdProvisioningPolicyIdRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

