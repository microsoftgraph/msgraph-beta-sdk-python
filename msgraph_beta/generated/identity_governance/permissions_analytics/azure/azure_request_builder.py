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
    from ....models.o_data_errors.o_data_error import ODataError
    from ....models.permissions_analytics import PermissionsAnalytics
    from .findings.findings_request_builder import FindingsRequestBuilder
    from .permissions_creep_index_distributions.permissions_creep_index_distributions_request_builder import PermissionsCreepIndexDistributionsRequestBuilder

class AzureRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the azure property of the microsoft.graph.permissionsAnalyticsAggregation entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new AzureRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/identityGovernance/permissionsAnalytics/azure{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[AzureRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property azure for identityGovernance
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[AzureRequestBuilderGetRequestConfiguration] = None) -> Optional[PermissionsAnalytics]:
        """
        Azure permissions analytics findings.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PermissionsAnalytics]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.permissions_analytics import PermissionsAnalytics

        return await self.request_adapter.send_async(request_info, PermissionsAnalytics, error_mapping)
    
    async def patch(self,body: Optional[PermissionsAnalytics] = None, request_configuration: Optional[AzureRequestBuilderPatchRequestConfiguration] = None) -> Optional[PermissionsAnalytics]:
        """
        Update the navigation property azure in identityGovernance
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PermissionsAnalytics]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.permissions_analytics import PermissionsAnalytics

        return await self.request_adapter.send_async(request_info, PermissionsAnalytics, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[AzureRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property azure for identityGovernance
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, '{+baseurl}/identityGovernance/permissionsAnalytics/azure', self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[AzureRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Azure permissions analytics findings.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: Optional[PermissionsAnalytics] = None, request_configuration: Optional[AzureRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property azure in identityGovernance
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PATCH, '{+baseurl}/identityGovernance/permissionsAnalytics/azure', self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> AzureRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: AzureRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return AzureRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def findings(self) -> FindingsRequestBuilder:
        """
        Provides operations to manage the findings property of the microsoft.graph.permissionsAnalytics entity.
        """
        from .findings.findings_request_builder import FindingsRequestBuilder

        return FindingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def permissions_creep_index_distributions(self) -> PermissionsCreepIndexDistributionsRequestBuilder:
        """
        Provides operations to manage the permissionsCreepIndexDistributions property of the microsoft.graph.permissionsAnalytics entity.
        """
        from .permissions_creep_index_distributions.permissions_creep_index_distributions_request_builder import PermissionsCreepIndexDistributionsRequestBuilder

        return PermissionsCreepIndexDistributionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class AzureRequestBuilderDeleteRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
    @dataclass
    class AzureRequestBuilderGetQueryParameters():
        """
        Azure permissions analytics findings.
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
    class AzureRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[AzureRequestBuilder.AzureRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class AzureRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

