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

ti_indicator = lazy_import('msgraph.generated.models.ti_indicator')
ti_indicator_collection_response = lazy_import('msgraph.generated.models.ti_indicator_collection_response')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')
count_request_builder = lazy_import('msgraph.generated.security.ti_indicators.count.count_request_builder')
delete_ti_indicators_request_builder = lazy_import('msgraph.generated.security.ti_indicators.delete_ti_indicators.delete_ti_indicators_request_builder')
delete_ti_indicators_by_external_id_request_builder = lazy_import('msgraph.generated.security.ti_indicators.delete_ti_indicators_by_external_id.delete_ti_indicators_by_external_id_request_builder')
submit_ti_indicators_request_builder = lazy_import('msgraph.generated.security.ti_indicators.submit_ti_indicators.submit_ti_indicators_request_builder')
update_ti_indicators_request_builder = lazy_import('msgraph.generated.security.ti_indicators.update_ti_indicators.update_ti_indicators_request_builder')

class TiIndicatorsRequestBuilder():
    """
    Provides operations to manage the tiIndicators property of the microsoft.graph.security entity.
    """
    @property
    def count(self) -> count_request_builder.CountRequestBuilder:
        """
        Provides operations to count the resources in the collection.
        """
        return count_request_builder.CountRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def delete_ti_indicators(self) -> delete_ti_indicators_request_builder.DeleteTiIndicatorsRequestBuilder:
        """
        Provides operations to call the deleteTiIndicators method.
        """
        return delete_ti_indicators_request_builder.DeleteTiIndicatorsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def delete_ti_indicators_by_external_id(self) -> delete_ti_indicators_by_external_id_request_builder.DeleteTiIndicatorsByExternalIdRequestBuilder:
        """
        Provides operations to call the deleteTiIndicatorsByExternalId method.
        """
        return delete_ti_indicators_by_external_id_request_builder.DeleteTiIndicatorsByExternalIdRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def submit_ti_indicators(self) -> submit_ti_indicators_request_builder.SubmitTiIndicatorsRequestBuilder:
        """
        Provides operations to call the submitTiIndicators method.
        """
        return submit_ti_indicators_request_builder.SubmitTiIndicatorsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def update_ti_indicators(self) -> update_ti_indicators_request_builder.UpdateTiIndicatorsRequestBuilder:
        """
        Provides operations to call the updateTiIndicators method.
        """
        return update_ti_indicators_request_builder.UpdateTiIndicatorsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new TiIndicatorsRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/security/tiIndicators{?%24top,%24skip,%24search,%24filter,%24count,%24orderby,%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def create_get_request_information(self,request_configuration: Optional[TiIndicatorsRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Retrieve a list of tiIndicator objects.
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
    
    def create_post_request_information(self,body: Optional[ti_indicator.TiIndicator] = None, request_configuration: Optional[TiIndicatorsRequestBuilderPostRequestConfiguration] = None) -> RequestInformation:
        """
        Create a new tiIndicator object.
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
        request_info.http_method = Method.POST
        request_info.headers["Accept"] = "application/json"
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    async def get(self,request_configuration: Optional[TiIndicatorsRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[ti_indicator_collection_response.TiIndicatorCollectionResponse]:
        """
        Retrieve a list of tiIndicator objects.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[ti_indicator_collection_response.TiIndicatorCollectionResponse]
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
        return await self.request_adapter.send_async(request_info, ti_indicator_collection_response.TiIndicatorCollectionResponse, response_handler, error_mapping)
    
    async def post(self,body: Optional[ti_indicator.TiIndicator] = None, request_configuration: Optional[TiIndicatorsRequestBuilderPostRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[ti_indicator.TiIndicator]:
        """
        Create a new tiIndicator object.
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[ti_indicator.TiIndicator]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.create_post_request_information(
            body, request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, ti_indicator.TiIndicator, response_handler, error_mapping)
    
    @dataclass
    class TiIndicatorsRequestBuilderGetQueryParameters():
        """
        Retrieve a list of tiIndicator objects.
        """
        # Include count of items
        count: Optional[bool] = None

        # Expand related entities
        expand: Optional[List[str]] = None

        # Filter items by property values
        filter: Optional[str] = None

        # Order items by property values
        orderby: Optional[List[str]] = None

        # Search items by search phrases
        search: Optional[str] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

        # Skip the first n items
        skip: Optional[int] = None

        # Show only the first n items
        top: Optional[int] = None

        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            Args:
                originalName: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise Exception("original_name cannot be undefined")
            if original_name == "count":
                return "%24count"
            if original_name == "expand":
                return "%24expand"
            if original_name == "filter":
                return "%24filter"
            if original_name == "orderby":
                return "%24orderby"
            if original_name == "search":
                return "%24search"
            if original_name == "select":
                return "%24select"
            if original_name == "skip":
                return "%24skip"
            if original_name == "top":
                return "%24top"
            return original_name
        
    
    @dataclass
    class TiIndicatorsRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[TiIndicatorsRequestBuilder.TiIndicatorsRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class TiIndicatorsRequestBuilderPostRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

