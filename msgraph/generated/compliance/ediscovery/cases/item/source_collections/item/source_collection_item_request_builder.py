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
    from .......models.ediscovery import source_collection
    from .......models.o_data_errors import o_data_error
    from .additional_sources import additional_sources_request_builder
    from .add_to_review_set_operation import add_to_review_set_operation_request_builder
    from .custodian_sources import custodian_sources_request_builder
    from .ediscovery_estimate_statistics import ediscovery_estimate_statistics_request_builder
    from .ediscovery_purge_data import ediscovery_purge_data_request_builder
    from .last_estimate_statistics_operation import last_estimate_statistics_operation_request_builder
    from .noncustodial_sources import noncustodial_sources_request_builder

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
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/compliance/ediscovery/cases/{case%2Did}/sourceCollections/{sourceCollection%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[SourceCollectionItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property sourceCollections for compliance
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .......models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[SourceCollectionItemRequestBuilderGetRequestConfiguration] = None) -> Optional[source_collection.SourceCollection]:
        """
        Returns a list of sourceCollection objects associated with this case.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[source_collection.SourceCollection]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .......models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .......models.ediscovery import source_collection

        return await self.request_adapter.send_async(request_info, source_collection.SourceCollection, error_mapping)
    
    async def patch(self,body: Optional[source_collection.SourceCollection] = None, request_configuration: Optional[SourceCollectionItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[source_collection.SourceCollection]:
        """
        Update the navigation property sourceCollections in compliance
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[source_collection.SourceCollection]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from .......models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .......models.ediscovery import source_collection

        return await self.request_adapter.send_async(request_info, source_collection.SourceCollection, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[SourceCollectionItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property sourceCollections for compliance
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
    
    def to_patch_request_information(self,body: Optional[source_collection.SourceCollection] = None, request_configuration: Optional[SourceCollectionItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property sourceCollections in compliance
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
    def additional_sources(self) -> additional_sources_request_builder.AdditionalSourcesRequestBuilder:
        """
        Provides operations to manage the additionalSources property of the microsoft.graph.ediscovery.sourceCollection entity.
        """
        from .additional_sources import additional_sources_request_builder

        return additional_sources_request_builder.AdditionalSourcesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def add_to_review_set_operation(self) -> add_to_review_set_operation_request_builder.AddToReviewSetOperationRequestBuilder:
        """
        Provides operations to manage the addToReviewSetOperation property of the microsoft.graph.ediscovery.sourceCollection entity.
        """
        from .add_to_review_set_operation import add_to_review_set_operation_request_builder

        return add_to_review_set_operation_request_builder.AddToReviewSetOperationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def custodian_sources(self) -> custodian_sources_request_builder.CustodianSourcesRequestBuilder:
        """
        Provides operations to manage the custodianSources property of the microsoft.graph.ediscovery.sourceCollection entity.
        """
        from .custodian_sources import custodian_sources_request_builder

        return custodian_sources_request_builder.CustodianSourcesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def ediscovery_estimate_statistics(self) -> ediscovery_estimate_statistics_request_builder.EdiscoveryEstimateStatisticsRequestBuilder:
        """
        Provides operations to call the estimateStatistics method.
        """
        from .ediscovery_estimate_statistics import ediscovery_estimate_statistics_request_builder

        return ediscovery_estimate_statistics_request_builder.EdiscoveryEstimateStatisticsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def ediscovery_purge_data(self) -> ediscovery_purge_data_request_builder.EdiscoveryPurgeDataRequestBuilder:
        """
        Provides operations to call the purgeData method.
        """
        from .ediscovery_purge_data import ediscovery_purge_data_request_builder

        return ediscovery_purge_data_request_builder.EdiscoveryPurgeDataRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def last_estimate_statistics_operation(self) -> last_estimate_statistics_operation_request_builder.LastEstimateStatisticsOperationRequestBuilder:
        """
        Provides operations to manage the lastEstimateStatisticsOperation property of the microsoft.graph.ediscovery.sourceCollection entity.
        """
        from .last_estimate_statistics_operation import last_estimate_statistics_operation_request_builder

        return last_estimate_statistics_operation_request_builder.LastEstimateStatisticsOperationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def noncustodial_sources(self) -> noncustodial_sources_request_builder.NoncustodialSourcesRequestBuilder:
        """
        Provides operations to manage the noncustodialSources property of the microsoft.graph.ediscovery.sourceCollection entity.
        """
        from .noncustodial_sources import noncustodial_sources_request_builder

        return noncustodial_sources_request_builder.NoncustodialSourcesRequestBuilder(self.request_adapter, self.path_parameters)
    
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

    

