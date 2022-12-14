from __future__ import annotations
from dataclasses import dataclass
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

site_sources_request_builder = lazy_import('msgraph.generated.compliance.ediscovery.cases.item.legal_holds.item.site_sources.site_sources_request_builder')
site_source_item_request_builder = lazy_import('msgraph.generated.compliance.ediscovery.cases.item.legal_holds.item.site_sources.item.site_source_item_request_builder')
unified_group_sources_request_builder = lazy_import('msgraph.generated.compliance.ediscovery.cases.item.legal_holds.item.unified_group_sources.unified_group_sources_request_builder')
unified_group_source_item_request_builder = lazy_import('msgraph.generated.compliance.ediscovery.cases.item.legal_holds.item.unified_group_sources.item.unified_group_source_item_request_builder')
user_sources_request_builder = lazy_import('msgraph.generated.compliance.ediscovery.cases.item.legal_holds.item.user_sources.user_sources_request_builder')
user_source_item_request_builder = lazy_import('msgraph.generated.compliance.ediscovery.cases.item.legal_holds.item.user_sources.item.user_source_item_request_builder')
legal_hold = lazy_import('msgraph.generated.models.ediscovery.legal_hold')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class LegalHoldItemRequestBuilder():
    """
    Provides operations to manage the legalHolds property of the microsoft.graph.ediscovery.case entity.
    """
    @property
    def site_sources(self) -> site_sources_request_builder.SiteSourcesRequestBuilder:
        """
        Provides operations to manage the siteSources property of the microsoft.graph.ediscovery.legalHold entity.
        """
        return site_sources_request_builder.SiteSourcesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def unified_group_sources(self) -> unified_group_sources_request_builder.UnifiedGroupSourcesRequestBuilder:
        """
        Provides operations to manage the unifiedGroupSources property of the microsoft.graph.ediscovery.legalHold entity.
        """
        return unified_group_sources_request_builder.UnifiedGroupSourcesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_sources(self) -> user_sources_request_builder.UserSourcesRequestBuilder:
        """
        Provides operations to manage the userSources property of the microsoft.graph.ediscovery.legalHold entity.
        """
        return user_sources_request_builder.UserSourcesRequestBuilder(self.request_adapter, self.path_parameters)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new LegalHoldItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/compliance/ediscovery/cases/{case%2Did}/legalHolds/{legalHold%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def create_delete_request_information(self,request_configuration: Optional[LegalHoldItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property legalHolds for compliance
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
    
    def create_get_request_information(self,request_configuration: Optional[LegalHoldItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Returns a list of case legalHold objects for this case.  Nullable.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers["Accept"] = "application/json"
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def create_patch_request_information(self,body: Optional[legal_hold.LegalHold] = None, request_configuration: Optional[LegalHoldItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property legalHolds in compliance
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
        request_info.headers["Accept"] = "application/json"
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    async def delete(self,request_configuration: Optional[LegalHoldItemRequestBuilderDeleteRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> None:
        """
        Delete navigation property legalHolds for compliance
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        """
        request_info = self.create_delete_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, response_handler, error_mapping)
    
    async def get(self,request_configuration: Optional[LegalHoldItemRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[legal_hold.LegalHold]:
        """
        Returns a list of case legalHold objects for this case.  Nullable.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[legal_hold.LegalHold]
        """
        request_info = self.create_get_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, legal_hold.LegalHold, response_handler, error_mapping)
    
    async def patch(self,body: Optional[legal_hold.LegalHold] = None, request_configuration: Optional[LegalHoldItemRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[legal_hold.LegalHold]:
        """
        Update the navigation property legalHolds in compliance
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[legal_hold.LegalHold]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.create_patch_request_information(
            body, request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, legal_hold.LegalHold, response_handler, error_mapping)
    
    def site_sources_by_id(self,id: str) -> site_source_item_request_builder.SiteSourceItemRequestBuilder:
        """
        Provides operations to manage the siteSources property of the microsoft.graph.ediscovery.legalHold entity.
        Args:
            id: Unique identifier of the item
        Returns: site_source_item_request_builder.SiteSourceItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["siteSource%2Did"] = id
        return site_source_item_request_builder.SiteSourceItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def unified_group_sources_by_id(self,id: str) -> unified_group_source_item_request_builder.UnifiedGroupSourceItemRequestBuilder:
        """
        Provides operations to manage the unifiedGroupSources property of the microsoft.graph.ediscovery.legalHold entity.
        Args:
            id: Unique identifier of the item
        Returns: unified_group_source_item_request_builder.UnifiedGroupSourceItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["unifiedGroupSource%2Did"] = id
        return unified_group_source_item_request_builder.UnifiedGroupSourceItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def user_sources_by_id(self,id: str) -> user_source_item_request_builder.UserSourceItemRequestBuilder:
        """
        Provides operations to manage the userSources property of the microsoft.graph.ediscovery.legalHold entity.
        Args:
            id: Unique identifier of the item
        Returns: user_source_item_request_builder.UserSourceItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["userSource%2Did"] = id
        return user_source_item_request_builder.UserSourceItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @dataclass
    class LegalHoldItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class LegalHoldItemRequestBuilderGetQueryParameters():
        """
        Returns a list of case legalHold objects for this case.  Nullable.
        """
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

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
        
    
    @dataclass
    class LegalHoldItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[LegalHoldItemRequestBuilder.LegalHoldItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class LegalHoldItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

