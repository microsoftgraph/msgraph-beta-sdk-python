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
    from .....models.ediscovery import case
    from .....models.o_data_errors import o_data_error
    from .custodians import custodians_request_builder
    from .custodians.item import custodian_item_request_builder
    from .ediscovery_close import ediscovery_close_request_builder
    from .ediscovery_reopen import ediscovery_reopen_request_builder
    from .legal_holds import legal_holds_request_builder
    from .legal_holds.item import legal_hold_item_request_builder
    from .noncustodial_data_sources import noncustodial_data_sources_request_builder
    from .noncustodial_data_sources.item import noncustodial_data_source_item_request_builder
    from .operations import operations_request_builder
    from .operations.item import case_operation_item_request_builder
    from .review_sets import review_sets_request_builder
    from .review_sets.item import review_set_item_request_builder
    from .settings import settings_request_builder
    from .source_collections import source_collections_request_builder
    from .source_collections.item import source_collection_item_request_builder
    from .tags import tags_request_builder
    from .tags.item import tag_item_request_builder

class CaseItemRequestBuilder():
    """
    Provides operations to manage the cases property of the microsoft.graph.ediscovery.ediscoveryroot entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new CaseItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/compliance/ediscovery/cases/{case%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def custodians_by_id(self,id: str) -> custodian_item_request_builder.CustodianItemRequestBuilder:
        """
        Provides operations to manage the custodians property of the microsoft.graph.ediscovery.case entity.
        Args:
            id: Unique identifier of the item
        Returns: custodian_item_request_builder.CustodianItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .custodians.item import custodian_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["custodian%2Did"] = id
        return custodian_item_request_builder.CustodianItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def delete(self,request_configuration: Optional[CaseItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property cases for compliance
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[CaseItemRequestBuilderGetRequestConfiguration] = None) -> Optional[case.Case]:
        """
        Get cases from compliance
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[case.Case]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.ediscovery import case

        return await self.request_adapter.send_async(request_info, case.Case, error_mapping)
    
    def legal_holds_by_id(self,id: str) -> legal_hold_item_request_builder.LegalHoldItemRequestBuilder:
        """
        Provides operations to manage the legalHolds property of the microsoft.graph.ediscovery.case entity.
        Args:
            id: Unique identifier of the item
        Returns: legal_hold_item_request_builder.LegalHoldItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .legal_holds.item import legal_hold_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["legalHold%2Did"] = id
        return legal_hold_item_request_builder.LegalHoldItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def noncustodial_data_sources_by_id(self,id: str) -> noncustodial_data_source_item_request_builder.NoncustodialDataSourceItemRequestBuilder:
        """
        Provides operations to manage the noncustodialDataSources property of the microsoft.graph.ediscovery.case entity.
        Args:
            id: Unique identifier of the item
        Returns: noncustodial_data_source_item_request_builder.NoncustodialDataSourceItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .noncustodial_data_sources.item import noncustodial_data_source_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["noncustodialDataSource%2Did"] = id
        return noncustodial_data_source_item_request_builder.NoncustodialDataSourceItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def operations_by_id(self,id: str) -> case_operation_item_request_builder.CaseOperationItemRequestBuilder:
        """
        Provides operations to manage the operations property of the microsoft.graph.ediscovery.case entity.
        Args:
            id: Unique identifier of the item
        Returns: case_operation_item_request_builder.CaseOperationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .operations.item import case_operation_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["caseOperation%2Did"] = id
        return case_operation_item_request_builder.CaseOperationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def patch(self,body: Optional[case.Case] = None, request_configuration: Optional[CaseItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[case.Case]:
        """
        Update the navigation property cases in compliance
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[case.Case]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from .....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.ediscovery import case

        return await self.request_adapter.send_async(request_info, case.Case, error_mapping)
    
    def review_sets_by_id(self,id: str) -> review_set_item_request_builder.ReviewSetItemRequestBuilder:
        """
        Provides operations to manage the reviewSets property of the microsoft.graph.ediscovery.case entity.
        Args:
            id: Unique identifier of the item
        Returns: review_set_item_request_builder.ReviewSetItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .review_sets.item import review_set_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["reviewSet%2Did"] = id
        return review_set_item_request_builder.ReviewSetItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def source_collections_by_id(self,id: str) -> source_collection_item_request_builder.SourceCollectionItemRequestBuilder:
        """
        Provides operations to manage the sourceCollections property of the microsoft.graph.ediscovery.case entity.
        Args:
            id: Unique identifier of the item
        Returns: source_collection_item_request_builder.SourceCollectionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .source_collections.item import source_collection_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["sourceCollection%2Did"] = id
        return source_collection_item_request_builder.SourceCollectionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def tags_by_id(self,id: str) -> tag_item_request_builder.TagItemRequestBuilder:
        """
        Provides operations to manage the tags property of the microsoft.graph.ediscovery.case entity.
        Args:
            id: Unique identifier of the item
        Returns: tag_item_request_builder.TagItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .tags.item import tag_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["tag%2Did"] = id
        return tag_item_request_builder.TagItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def to_delete_request_information(self,request_configuration: Optional[CaseItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property cases for compliance
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
    
    def to_get_request_information(self,request_configuration: Optional[CaseItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get cases from compliance
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
    
    def to_patch_request_information(self,body: Optional[case.Case] = None, request_configuration: Optional[CaseItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property cases in compliance
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
    def custodians(self) -> custodians_request_builder.CustodiansRequestBuilder:
        """
        Provides operations to manage the custodians property of the microsoft.graph.ediscovery.case entity.
        """
        from .custodians import custodians_request_builder

        return custodians_request_builder.CustodiansRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def ediscovery_close(self) -> ediscovery_close_request_builder.EdiscoveryCloseRequestBuilder:
        """
        Provides operations to call the close method.
        """
        from .ediscovery_close import ediscovery_close_request_builder

        return ediscovery_close_request_builder.EdiscoveryCloseRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def ediscovery_reopen(self) -> ediscovery_reopen_request_builder.EdiscoveryReopenRequestBuilder:
        """
        Provides operations to call the reopen method.
        """
        from .ediscovery_reopen import ediscovery_reopen_request_builder

        return ediscovery_reopen_request_builder.EdiscoveryReopenRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def legal_holds(self) -> legal_holds_request_builder.LegalHoldsRequestBuilder:
        """
        Provides operations to manage the legalHolds property of the microsoft.graph.ediscovery.case entity.
        """
        from .legal_holds import legal_holds_request_builder

        return legal_holds_request_builder.LegalHoldsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def noncustodial_data_sources(self) -> noncustodial_data_sources_request_builder.NoncustodialDataSourcesRequestBuilder:
        """
        Provides operations to manage the noncustodialDataSources property of the microsoft.graph.ediscovery.case entity.
        """
        from .noncustodial_data_sources import noncustodial_data_sources_request_builder

        return noncustodial_data_sources_request_builder.NoncustodialDataSourcesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def operations(self) -> operations_request_builder.OperationsRequestBuilder:
        """
        Provides operations to manage the operations property of the microsoft.graph.ediscovery.case entity.
        """
        from .operations import operations_request_builder

        return operations_request_builder.OperationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def review_sets(self) -> review_sets_request_builder.ReviewSetsRequestBuilder:
        """
        Provides operations to manage the reviewSets property of the microsoft.graph.ediscovery.case entity.
        """
        from .review_sets import review_sets_request_builder

        return review_sets_request_builder.ReviewSetsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def settings(self) -> settings_request_builder.SettingsRequestBuilder:
        """
        Provides operations to manage the settings property of the microsoft.graph.ediscovery.case entity.
        """
        from .settings import settings_request_builder

        return settings_request_builder.SettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def source_collections(self) -> source_collections_request_builder.SourceCollectionsRequestBuilder:
        """
        Provides operations to manage the sourceCollections property of the microsoft.graph.ediscovery.case entity.
        """
        from .source_collections import source_collections_request_builder

        return source_collections_request_builder.SourceCollectionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tags(self) -> tags_request_builder.TagsRequestBuilder:
        """
        Provides operations to manage the tags property of the microsoft.graph.ediscovery.case entity.
        """
        from .tags import tags_request_builder

        return tags_request_builder.TagsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class CaseItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class CaseItemRequestBuilderGetQueryParameters():
        """
        Get cases from compliance
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
    class CaseItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[CaseItemRequestBuilder.CaseItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class CaseItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

