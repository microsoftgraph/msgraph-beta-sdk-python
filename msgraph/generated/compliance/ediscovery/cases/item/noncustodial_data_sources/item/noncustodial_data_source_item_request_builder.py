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
    from .......models.ediscovery.noncustodial_data_source import NoncustodialDataSource
    from .......models.o_data_errors.o_data_error import ODataError
    from .data_source.data_source_request_builder import DataSourceRequestBuilder
    from .last_index_operation.last_index_operation_request_builder import LastIndexOperationRequestBuilder
    from .microsoft_graph_ediscovery_apply_hold.microsoft_graph_ediscovery_apply_hold_request_builder import MicrosoftGraphEdiscoveryApplyHoldRequestBuilder
    from .microsoft_graph_ediscovery_release.microsoft_graph_ediscovery_release_request_builder import MicrosoftGraphEdiscoveryReleaseRequestBuilder
    from .microsoft_graph_ediscovery_remove_hold.microsoft_graph_ediscovery_remove_hold_request_builder import MicrosoftGraphEdiscoveryRemoveHoldRequestBuilder
    from .microsoft_graph_ediscovery_update_index.microsoft_graph_ediscovery_update_index_request_builder import MicrosoftGraphEdiscoveryUpdateIndexRequestBuilder

class NoncustodialDataSourceItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the noncustodialDataSources property of the microsoft.graph.ediscovery.case entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new NoncustodialDataSourceItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/compliance/ediscovery/cases/{case%2Did}/noncustodialDataSources/{noncustodialDataSource%2Did}{?%24select,%24expand}", path_parameters)
    
    async def delete(self,request_configuration: Optional[NoncustodialDataSourceItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property noncustodialDataSources for compliance
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[NoncustodialDataSourceItemRequestBuilderGetRequestConfiguration] = None) -> Optional[NoncustodialDataSource]:
        """
        Read the properties and relationships of a noncustodialDataSource object. This API is available in the following national cloud deployments.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[NoncustodialDataSource]
        Find more info here: https://learn.microsoft.com/graph/api/ediscovery-noncustodialdatasource-get?view=graph-rest-1.0
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .......models.ediscovery.noncustodial_data_source import NoncustodialDataSource

        return await self.request_adapter.send_async(request_info, NoncustodialDataSource, error_mapping)
    
    async def patch(self,body: Optional[NoncustodialDataSource] = None, request_configuration: Optional[NoncustodialDataSourceItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[NoncustodialDataSource]:
        """
        Update the navigation property noncustodialDataSources in compliance
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[NoncustodialDataSource]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from .......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .......models.ediscovery.noncustodial_data_source import NoncustodialDataSource

        return await self.request_adapter.send_async(request_info, NoncustodialDataSource, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[NoncustodialDataSourceItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property noncustodialDataSources for compliance
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
        request_info.headers.try_add("Accept", "application/json, application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[NoncustodialDataSourceItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Read the properties and relationships of a noncustodialDataSource object. This API is available in the following national cloud deployments.
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
    
    def to_patch_request_information(self,body: Optional[NoncustodialDataSource] = None, request_configuration: Optional[NoncustodialDataSourceItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property noncustodialDataSources in compliance
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
    
    def with_url(self,raw_url: Optional[str] = None) -> NoncustodialDataSourceItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: NoncustodialDataSourceItemRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return NoncustodialDataSourceItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def data_source(self) -> DataSourceRequestBuilder:
        """
        Provides operations to manage the dataSource property of the microsoft.graph.ediscovery.noncustodialDataSource entity.
        """
        from .data_source.data_source_request_builder import DataSourceRequestBuilder

        return DataSourceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def last_index_operation(self) -> LastIndexOperationRequestBuilder:
        """
        Provides operations to manage the lastIndexOperation property of the microsoft.graph.ediscovery.dataSourceContainer entity.
        """
        from .last_index_operation.last_index_operation_request_builder import LastIndexOperationRequestBuilder

        return LastIndexOperationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_ediscovery_apply_hold(self) -> MicrosoftGraphEdiscoveryApplyHoldRequestBuilder:
        """
        Provides operations to call the applyHold method.
        """
        from .microsoft_graph_ediscovery_apply_hold.microsoft_graph_ediscovery_apply_hold_request_builder import MicrosoftGraphEdiscoveryApplyHoldRequestBuilder

        return MicrosoftGraphEdiscoveryApplyHoldRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_ediscovery_release(self) -> MicrosoftGraphEdiscoveryReleaseRequestBuilder:
        """
        Provides operations to call the release method.
        """
        from .microsoft_graph_ediscovery_release.microsoft_graph_ediscovery_release_request_builder import MicrosoftGraphEdiscoveryReleaseRequestBuilder

        return MicrosoftGraphEdiscoveryReleaseRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_ediscovery_remove_hold(self) -> MicrosoftGraphEdiscoveryRemoveHoldRequestBuilder:
        """
        Provides operations to call the removeHold method.
        """
        from .microsoft_graph_ediscovery_remove_hold.microsoft_graph_ediscovery_remove_hold_request_builder import MicrosoftGraphEdiscoveryRemoveHoldRequestBuilder

        return MicrosoftGraphEdiscoveryRemoveHoldRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_ediscovery_update_index(self) -> MicrosoftGraphEdiscoveryUpdateIndexRequestBuilder:
        """
        Provides operations to call the updateIndex method.
        """
        from .microsoft_graph_ediscovery_update_index.microsoft_graph_ediscovery_update_index_request_builder import MicrosoftGraphEdiscoveryUpdateIndexRequestBuilder

        return MicrosoftGraphEdiscoveryUpdateIndexRequestBuilder(self.request_adapter, self.path_parameters)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class NoncustodialDataSourceItemRequestBuilderDeleteRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
    @dataclass
    class NoncustodialDataSourceItemRequestBuilderGetQueryParameters():
        """
        Read the properties and relationships of a noncustodialDataSource object. This API is available in the following national cloud deployments.
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
    class NoncustodialDataSourceItemRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[NoncustodialDataSourceItemRequestBuilder.NoncustodialDataSourceItemRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class NoncustodialDataSourceItemRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

