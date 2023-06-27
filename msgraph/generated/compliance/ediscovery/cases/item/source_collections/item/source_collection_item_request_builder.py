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
    from .......models.ediscovery.source_collection import SourceCollection
    from .......models.o_data_errors.o_data_error import ODataError
    from .additional_sources.additional_sources_request_builder import AdditionalSourcesRequestBuilder
    from .add_to_review_set_operation.add_to_review_set_operation_request_builder import AddToReviewSetOperationRequestBuilder
    from .custodian_sources.custodian_sources_request_builder import CustodianSourcesRequestBuilder
    from .last_estimate_statistics_operation.last_estimate_statistics_operation_request_builder import LastEstimateStatisticsOperationRequestBuilder
    from .microsoft_graph_ediscovery_estimate_statistics.microsoft_graph_ediscovery_estimate_statistics_request_builder import MicrosoftGraphEdiscoveryEstimateStatisticsRequestBuilder
    from .microsoft_graph_ediscovery_purge_data.microsoft_graph_ediscovery_purge_data_request_builder import MicrosoftGraphEdiscoveryPurgeDataRequestBuilder
    from .noncustodial_sources.noncustodial_sources_request_builder import NoncustodialSourcesRequestBuilder

class SourceCollectionItemRequestBuilder():
    """
    Provides operations to manage the sourceCollections property of the microsoft.graph.ediscovery.case entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new SourceCollectionItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if not path_parameters:
            raise TypeError("path_parameters cannot be null.")
        if not request_adapter:
            raise TypeError("request_adapter cannot be null.")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/compliance/ediscovery/cases/{case%2Did}/sourceCollections/{sourceCollection%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[SourceCollectionItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete a sourceCollection object.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
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
    
    async def get(self,request_configuration: Optional[SourceCollectionItemRequestBuilderGetRequestConfiguration] = None) -> Optional[SourceCollection]:
        """
        Returns a list of sourceCollection objects associated with this case.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[SourceCollection]
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
        from .......models.ediscovery.source_collection import SourceCollection

        return await self.request_adapter.send_async(request_info, SourceCollection, error_mapping)
    
    async def patch(self,body: Optional[SourceCollection] = None, request_configuration: Optional[SourceCollectionItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[SourceCollection]:
        """
        Update the properties of a sourceCollection object.
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[SourceCollection]
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
        from .......models.ediscovery.source_collection import SourceCollection

        return await self.request_adapter.send_async(request_info, SourceCollection, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[SourceCollectionItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete a sourceCollection object.
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
    
    def to_get_request_information(self,request_configuration: Optional[SourceCollectionItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Returns a list of sourceCollection objects associated with this case.
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
    
    def to_patch_request_information(self,body: Optional[SourceCollection] = None, request_configuration: Optional[SourceCollectionItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the properties of a sourceCollection object.
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
    def additional_sources(self) -> AdditionalSourcesRequestBuilder:
        """
        Provides operations to manage the additionalSources property of the microsoft.graph.ediscovery.sourceCollection entity.
        """
        from .additional_sources.additional_sources_request_builder import AdditionalSourcesRequestBuilder

        return AdditionalSourcesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def add_to_review_set_operation(self) -> AddToReviewSetOperationRequestBuilder:
        """
        Provides operations to manage the addToReviewSetOperation property of the microsoft.graph.ediscovery.sourceCollection entity.
        """
        from .add_to_review_set_operation.add_to_review_set_operation_request_builder import AddToReviewSetOperationRequestBuilder

        return AddToReviewSetOperationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def custodian_sources(self) -> CustodianSourcesRequestBuilder:
        """
        Provides operations to manage the custodianSources property of the microsoft.graph.ediscovery.sourceCollection entity.
        """
        from .custodian_sources.custodian_sources_request_builder import CustodianSourcesRequestBuilder

        return CustodianSourcesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def last_estimate_statistics_operation(self) -> LastEstimateStatisticsOperationRequestBuilder:
        """
        Provides operations to manage the lastEstimateStatisticsOperation property of the microsoft.graph.ediscovery.sourceCollection entity.
        """
        from .last_estimate_statistics_operation.last_estimate_statistics_operation_request_builder import LastEstimateStatisticsOperationRequestBuilder

        return LastEstimateStatisticsOperationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_ediscovery_estimate_statistics(self) -> MicrosoftGraphEdiscoveryEstimateStatisticsRequestBuilder:
        """
        Provides operations to call the estimateStatistics method.
        """
        from .microsoft_graph_ediscovery_estimate_statistics.microsoft_graph_ediscovery_estimate_statistics_request_builder import MicrosoftGraphEdiscoveryEstimateStatisticsRequestBuilder

        return MicrosoftGraphEdiscoveryEstimateStatisticsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_ediscovery_purge_data(self) -> MicrosoftGraphEdiscoveryPurgeDataRequestBuilder:
        """
        Provides operations to call the purgeData method.
        """
        from .microsoft_graph_ediscovery_purge_data.microsoft_graph_ediscovery_purge_data_request_builder import MicrosoftGraphEdiscoveryPurgeDataRequestBuilder

        return MicrosoftGraphEdiscoveryPurgeDataRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def noncustodial_sources(self) -> NoncustodialSourcesRequestBuilder:
        """
        Provides operations to manage the noncustodialSources property of the microsoft.graph.ediscovery.sourceCollection entity.
        """
        from .noncustodial_sources.noncustodial_sources_request_builder import NoncustodialSourcesRequestBuilder

        return NoncustodialSourcesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class SourceCollectionItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class SourceCollectionItemRequestBuilderGetQueryParameters():
        """
        Returns a list of sourceCollection objects associated with this case.
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
    class SourceCollectionItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[SourceCollectionItemRequestBuilder.SourceCollectionItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class SourceCollectionItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

