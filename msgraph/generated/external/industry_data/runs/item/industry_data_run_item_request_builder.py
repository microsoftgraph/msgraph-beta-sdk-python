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
    from .....models.industry_data import industry_data_run
    from .....models.o_data_errors import o_data_error
    from .activities import activities_request_builder
    from .industry_data_get_statistics import industry_data_get_statistics_request_builder

class IndustryDataRunItemRequestBuilder():
    """
    Provides operations to manage the runs property of the microsoft.graph.industryData.industryDataRoot entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new IndustryDataRunItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/external/industryData/runs/{industryDataRun%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def get(self,request_configuration: Optional[IndustryDataRunItemRequestBuilderGetRequestConfiguration] = None) -> Optional[industry_data_run.IndustryDataRun]:
        """
        Set of ephemeral runs which present the point-in-time that diagnostic state of activities performed by the system. Read-only.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[industry_data_run.IndustryDataRun]
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
        from .....models.industry_data import industry_data_run

        return await self.request_adapter.send_async(request_info, industry_data_run.IndustryDataRun, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[IndustryDataRunItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Set of ephemeral runs which present the point-in-time that diagnostic state of activities performed by the system. Read-only.
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
    
    @property
    def activities(self) -> activities_request_builder.ActivitiesRequestBuilder:
        """
        Provides operations to manage the activities property of the microsoft.graph.industryData.industryDataRun entity.
        """
        from .activities import activities_request_builder

        return activities_request_builder.ActivitiesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def industry_data_get_statistics(self) -> industry_data_get_statistics_request_builder.IndustryDataGetStatisticsRequestBuilder:
        """
        Provides operations to call the getStatistics method.
        """
        from .industry_data_get_statistics import industry_data_get_statistics_request_builder

        return industry_data_get_statistics_request_builder.IndustryDataGetStatisticsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class IndustryDataRunItemRequestBuilderGetQueryParameters():
        """
        Set of ephemeral runs which present the point-in-time that diagnostic state of activities performed by the system. Read-only.
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
    class IndustryDataRunItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[IndustryDataRunItemRequestBuilder.IndustryDataRunItemRequestBuilderGetQueryParameters] = None

    

