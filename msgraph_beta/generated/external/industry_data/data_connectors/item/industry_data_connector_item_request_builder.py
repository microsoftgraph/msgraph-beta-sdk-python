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
    from .....models.industry_data.industry_data_connector import IndustryDataConnector
    from .....models.o_data_errors.o_data_error import ODataError
    from .microsoft_graph_industry_data_validate.microsoft_graph_industry_data_validate_request_builder import MicrosoftGraphIndustryDataValidateRequestBuilder
    from .source_system.source_system_request_builder import SourceSystemRequestBuilder

class IndustryDataConnectorItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the dataConnectors property of the microsoft.graph.industryData.industryDataRoot entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new IndustryDataConnectorItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/external/industryData/dataConnectors/{industryDataConnector%2Did}{?%24select,%24expand}", path_parameters)
    
    async def delete(self,request_configuration: Optional[IndustryDataConnectorItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete an azureDataLakeConnector object. This API is available in the following national cloud deployments.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        Find more info here: https://learn.microsoft.com/graph/api/industrydata-azuredatalakeconnector-delete?view=graph-rest-1.0
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
    
    async def get(self,request_configuration: Optional[IndustryDataConnectorItemRequestBuilderGetRequestConfiguration] = None) -> Optional[IndustryDataConnector]:
        """
        Read the properties and relationships of an industryDataConnector object. This API is available in the following national cloud deployments.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[IndustryDataConnector]
        Find more info here: https://learn.microsoft.com/graph/api/industrydata-industrydataconnector-get?view=graph-rest-1.0
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
        from .....models.industry_data.industry_data_connector import IndustryDataConnector

        return await self.request_adapter.send_async(request_info, IndustryDataConnector, error_mapping)
    
    async def patch(self,body: Optional[IndustryDataConnector] = None, request_configuration: Optional[IndustryDataConnectorItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[IndustryDataConnector]:
        """
        Update the properties of an azureDataLakeConnector object. This API is available in the following national cloud deployments.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[IndustryDataConnector]
        Find more info here: https://learn.microsoft.com/graph/api/industrydata-azuredatalakeconnector-update?view=graph-rest-1.0
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
        from .....models.industry_data.industry_data_connector import IndustryDataConnector

        return await self.request_adapter.send_async(request_info, IndustryDataConnector, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[IndustryDataConnectorItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete an azureDataLakeConnector object. This API is available in the following national cloud deployments.
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
    
    def to_get_request_information(self,request_configuration: Optional[IndustryDataConnectorItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Read the properties and relationships of an industryDataConnector object. This API is available in the following national cloud deployments.
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
    
    def to_patch_request_information(self,body: Optional[IndustryDataConnector] = None, request_configuration: Optional[IndustryDataConnectorItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the properties of an azureDataLakeConnector object. This API is available in the following national cloud deployments.
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
    
    def with_url(self,raw_url: Optional[str] = None) -> IndustryDataConnectorItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: IndustryDataConnectorItemRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return IndustryDataConnectorItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def microsoft_graph_industry_data_validate(self) -> MicrosoftGraphIndustryDataValidateRequestBuilder:
        """
        Provides operations to call the validate method.
        """
        from .microsoft_graph_industry_data_validate.microsoft_graph_industry_data_validate_request_builder import MicrosoftGraphIndustryDataValidateRequestBuilder

        return MicrosoftGraphIndustryDataValidateRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def source_system(self) -> SourceSystemRequestBuilder:
        """
        Provides operations to manage the sourceSystem property of the microsoft.graph.industryData.industryDataConnector entity.
        """
        from .source_system.source_system_request_builder import SourceSystemRequestBuilder

        return SourceSystemRequestBuilder(self.request_adapter, self.path_parameters)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class IndustryDataConnectorItemRequestBuilderDeleteRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
    @dataclass
    class IndustryDataConnectorItemRequestBuilderGetQueryParameters():
        """
        Read the properties and relationships of an industryDataConnector object. This API is available in the following national cloud deployments.
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
    class IndustryDataConnectorItemRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[IndustryDataConnectorItemRequestBuilder.IndustryDataConnectorItemRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class IndustryDataConnectorItemRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

