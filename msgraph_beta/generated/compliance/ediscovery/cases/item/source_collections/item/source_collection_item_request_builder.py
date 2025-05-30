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
    from .......models.ediscovery.source_collection import SourceCollection
    from .......models.o_data_errors.o_data_error import ODataError
    from .additional_sources.additional_sources_request_builder import AdditionalSourcesRequestBuilder
    from .add_to_review_set_operation.add_to_review_set_operation_request_builder import AddToReviewSetOperationRequestBuilder
    from .custodian_sources.custodian_sources_request_builder import CustodianSourcesRequestBuilder
    from .last_estimate_statistics_operation.last_estimate_statistics_operation_request_builder import LastEstimateStatisticsOperationRequestBuilder
    from .microsoft_graph_ediscovery_estimate_statistics.microsoft_graph_ediscovery_estimate_statistics_request_builder import MicrosoftGraphEdiscoveryEstimateStatisticsRequestBuilder
    from .microsoft_graph_ediscovery_purge_data.microsoft_graph_ediscovery_purge_data_request_builder import MicrosoftGraphEdiscoveryPurgeDataRequestBuilder
    from .noncustodial_sources.noncustodial_sources_request_builder import NoncustodialSourcesRequestBuilder

class SourceCollectionItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the sourceCollections property of the microsoft.graph.ediscovery.case entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new SourceCollectionItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/compliance/ediscovery/cases/{case%2Did}/sourceCollections/{sourceCollection%2Did}{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete a sourceCollection object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        Find more info here: https://learn.microsoft.com/graph/api/ediscovery-sourcecollection-delete?view=graph-rest-beta
        """
        warn("The ediscovery Apis are deprecated under /compliance and will stop returning data from February 01, 2023. Please use the new ediscovery Apis under /security. as of 2022-12/ediscoveryNamespace on 2022-12-05 and will be removed 2023-02-01", DeprecationWarning)
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .......models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[SourceCollectionItemRequestBuilderGetQueryParameters]] = None) -> Optional[SourceCollection]:
        """
        Returns a list of sourceCollection objects associated with this case.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[SourceCollection]
        """
        warn("The ediscovery Apis are deprecated under /compliance and will stop returning data from February 01, 2023. Please use the new ediscovery Apis under /security. as of 2022-12/ediscoveryNamespace on 2022-12-05 and will be removed 2023-02-01", DeprecationWarning)
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .......models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .......models.ediscovery.source_collection import SourceCollection

        return await self.request_adapter.send_async(request_info, SourceCollection, error_mapping)
    
    async def patch(self,body: SourceCollection, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[SourceCollection]:
        """
        Update the properties of a sourceCollection object.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[SourceCollection]
        Find more info here: https://learn.microsoft.com/graph/api/ediscovery-sourcecollection-update?view=graph-rest-beta
        """
        warn("The ediscovery Apis are deprecated under /compliance and will stop returning data from February 01, 2023. Please use the new ediscovery Apis under /security. as of 2022-12/ediscoveryNamespace on 2022-12-05 and will be removed 2023-02-01", DeprecationWarning)
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from .......models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .......models.ediscovery.source_collection import SourceCollection

        return await self.request_adapter.send_async(request_info, SourceCollection, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete a sourceCollection object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        warn("The ediscovery Apis are deprecated under /compliance and will stop returning data from February 01, 2023. Please use the new ediscovery Apis under /security. as of 2022-12/ediscoveryNamespace on 2022-12-05 and will be removed 2023-02-01", DeprecationWarning)
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[SourceCollectionItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Returns a list of sourceCollection objects associated with this case.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        warn("The ediscovery Apis are deprecated under /compliance and will stop returning data from February 01, 2023. Please use the new ediscovery Apis under /security. as of 2022-12/ediscoveryNamespace on 2022-12-05 and will be removed 2023-02-01", DeprecationWarning)
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: SourceCollection, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the properties of a sourceCollection object.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        warn("The ediscovery Apis are deprecated under /compliance and will stop returning data from February 01, 2023. Please use the new ediscovery Apis under /security. as of 2022-12/ediscoveryNamespace on 2022-12-05 and will be removed 2023-02-01", DeprecationWarning)
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PATCH, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> SourceCollectionItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: SourceCollectionItemRequestBuilder
        """
        warn("The ediscovery Apis are deprecated under /compliance and will stop returning data from February 01, 2023. Please use the new ediscovery Apis under /security. as of 2022-12/ediscoveryNamespace on 2022-12-05 and will be removed 2023-02-01", DeprecationWarning)
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return SourceCollectionItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def add_to_review_set_operation(self) -> AddToReviewSetOperationRequestBuilder:
        """
        Provides operations to manage the addToReviewSetOperation property of the microsoft.graph.ediscovery.sourceCollection entity.
        """
        from .add_to_review_set_operation.add_to_review_set_operation_request_builder import AddToReviewSetOperationRequestBuilder

        return AddToReviewSetOperationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def additional_sources(self) -> AdditionalSourcesRequestBuilder:
        """
        Provides operations to manage the additionalSources property of the microsoft.graph.ediscovery.sourceCollection entity.
        """
        from .additional_sources.additional_sources_request_builder import AdditionalSourcesRequestBuilder

        return AdditionalSourcesRequestBuilder(self.request_adapter, self.path_parameters)
    
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
    class SourceCollectionItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class SourceCollectionItemRequestBuilderGetQueryParameters():
        """
        Returns a list of sourceCollection objects associated with this case.
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
        expand: Optional[list[str]] = None

        # Select properties to be returned
        select: Optional[list[str]] = None

    
    @dataclass
    class SourceCollectionItemRequestBuilderGetRequestConfiguration(RequestConfiguration[SourceCollectionItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class SourceCollectionItemRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

