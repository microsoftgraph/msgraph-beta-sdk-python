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
    from .....models.ediscovery.case import Case
    from .....models.o_data_errors.o_data_error import ODataError
    from .custodians.custodians_request_builder import CustodiansRequestBuilder
    from .legal_holds.legal_holds_request_builder import LegalHoldsRequestBuilder
    from .microsoft_graph_ediscovery_close.microsoft_graph_ediscovery_close_request_builder import MicrosoftGraphEdiscoveryCloseRequestBuilder
    from .microsoft_graph_ediscovery_reopen.microsoft_graph_ediscovery_reopen_request_builder import MicrosoftGraphEdiscoveryReopenRequestBuilder
    from .noncustodial_data_sources.noncustodial_data_sources_request_builder import NoncustodialDataSourcesRequestBuilder
    from .operations.operations_request_builder import OperationsRequestBuilder
    from .review_sets.review_sets_request_builder import ReviewSetsRequestBuilder
    from .settings.settings_request_builder import SettingsRequestBuilder
    from .source_collections.source_collections_request_builder import SourceCollectionsRequestBuilder
    from .tags.tags_request_builder import TagsRequestBuilder

class CaseItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the cases property of the microsoft.graph.ediscovery.ediscoveryroot entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new CaseItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/compliance/ediscovery/cases/{case%2Did}{?%24select,%24expand}", path_parameters)
    
    async def delete(self,request_configuration: Optional[CaseItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete a case object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        Find more info here: https://learn.microsoft.com/graph/api/ediscovery-case-delete?view=graph-rest-1.0
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[CaseItemRequestBuilderGetRequestConfiguration] = None) -> Optional[Case]:
        """
        Retrieve the properties and relationships of a case object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Case]
        Find more info here: https://learn.microsoft.com/graph/api/ediscovery-case-get?view=graph-rest-1.0
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.ediscovery.case import Case

        return await self.request_adapter.send_async(request_info, Case, error_mapping)
    
    async def patch(self,body: Optional[Case] = None, request_configuration: Optional[CaseItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[Case]:
        """
        Update the properties of a case object.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Case]
        Find more info here: https://learn.microsoft.com/graph/api/ediscovery-case-update?view=graph-rest-1.0
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.ediscovery.case import Case

        return await self.request_adapter.send_async(request_info, Case, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[CaseItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete a case object.
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
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[CaseItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Retrieve the properties and relationships of a case object.
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
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: Optional[Case] = None, request_configuration: Optional[CaseItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the properties of a case object.
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
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> CaseItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: CaseItemRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return CaseItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def custodians(self) -> CustodiansRequestBuilder:
        """
        Provides operations to manage the custodians property of the microsoft.graph.ediscovery.case entity.
        """
        from .custodians.custodians_request_builder import CustodiansRequestBuilder

        return CustodiansRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def legal_holds(self) -> LegalHoldsRequestBuilder:
        """
        Provides operations to manage the legalHolds property of the microsoft.graph.ediscovery.case entity.
        """
        from .legal_holds.legal_holds_request_builder import LegalHoldsRequestBuilder

        return LegalHoldsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_ediscovery_close(self) -> MicrosoftGraphEdiscoveryCloseRequestBuilder:
        """
        Provides operations to call the close method.
        """
        from .microsoft_graph_ediscovery_close.microsoft_graph_ediscovery_close_request_builder import MicrosoftGraphEdiscoveryCloseRequestBuilder

        return MicrosoftGraphEdiscoveryCloseRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_ediscovery_reopen(self) -> MicrosoftGraphEdiscoveryReopenRequestBuilder:
        """
        Provides operations to call the reopen method.
        """
        from .microsoft_graph_ediscovery_reopen.microsoft_graph_ediscovery_reopen_request_builder import MicrosoftGraphEdiscoveryReopenRequestBuilder

        return MicrosoftGraphEdiscoveryReopenRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def noncustodial_data_sources(self) -> NoncustodialDataSourcesRequestBuilder:
        """
        Provides operations to manage the noncustodialDataSources property of the microsoft.graph.ediscovery.case entity.
        """
        from .noncustodial_data_sources.noncustodial_data_sources_request_builder import NoncustodialDataSourcesRequestBuilder

        return NoncustodialDataSourcesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def operations(self) -> OperationsRequestBuilder:
        """
        Provides operations to manage the operations property of the microsoft.graph.ediscovery.case entity.
        """
        from .operations.operations_request_builder import OperationsRequestBuilder

        return OperationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def review_sets(self) -> ReviewSetsRequestBuilder:
        """
        Provides operations to manage the reviewSets property of the microsoft.graph.ediscovery.case entity.
        """
        from .review_sets.review_sets_request_builder import ReviewSetsRequestBuilder

        return ReviewSetsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def settings(self) -> SettingsRequestBuilder:
        """
        Provides operations to manage the settings property of the microsoft.graph.ediscovery.case entity.
        """
        from .settings.settings_request_builder import SettingsRequestBuilder

        return SettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def source_collections(self) -> SourceCollectionsRequestBuilder:
        """
        Provides operations to manage the sourceCollections property of the microsoft.graph.ediscovery.case entity.
        """
        from .source_collections.source_collections_request_builder import SourceCollectionsRequestBuilder

        return SourceCollectionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tags(self) -> TagsRequestBuilder:
        """
        Provides operations to manage the tags property of the microsoft.graph.ediscovery.case entity.
        """
        from .tags.tags_request_builder import TagsRequestBuilder

        return TagsRequestBuilder(self.request_adapter, self.path_parameters)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class CaseItemRequestBuilderDeleteRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
    @dataclass
    class CaseItemRequestBuilderGetQueryParameters():
        """
        Retrieve the properties and relationships of a case object.
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
    class CaseItemRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[CaseItemRequestBuilder.CaseItemRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class CaseItemRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

