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
    from ..........models import time_card
    from ..........models.o_data_errors import o_data_error
    from .clock_out import clock_out_request_builder
    from .confirm import confirm_request_builder
    from .end_break import end_break_request_builder
    from .start_break import start_break_request_builder

class TimeCardItemRequestBuilder():
    """
    Provides operations to manage the timeCards property of the microsoft.graph.schedule entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new TimeCardItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/teamwork/teamTemplates/{teamTemplate%2Did}/definitions/{teamTemplateDefinition%2Did}/teamDefinition/schedule/timeCards/{timeCard%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[TimeCardItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property timeCards for teamwork
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ..........models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[TimeCardItemRequestBuilderGetRequestConfiguration] = None) -> Optional[time_card.TimeCard]:
        """
        Get timeCards from teamwork
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[time_card.TimeCard]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ..........models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..........models import time_card

        return await self.request_adapter.send_async(request_info, time_card.TimeCard, error_mapping)
    
    async def patch(self,body: Optional[time_card.TimeCard] = None, request_configuration: Optional[TimeCardItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[time_card.TimeCard]:
        """
        Update the navigation property timeCards in teamwork
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[time_card.TimeCard]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ..........models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..........models import time_card

        return await self.request_adapter.send_async(request_info, time_card.TimeCard, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[TimeCardItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property timeCards for teamwork
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
    
    def to_get_request_information(self,request_configuration: Optional[TimeCardItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get timeCards from teamwork
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
    
    def to_patch_request_information(self,body: Optional[time_card.TimeCard] = None, request_configuration: Optional[TimeCardItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property timeCards in teamwork
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
    def clock_out(self) -> clock_out_request_builder.ClockOutRequestBuilder:
        """
        Provides operations to call the clockOut method.
        """
        from .clock_out import clock_out_request_builder

        return clock_out_request_builder.ClockOutRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def confirm(self) -> confirm_request_builder.ConfirmRequestBuilder:
        """
        Provides operations to call the confirm method.
        """
        from .confirm import confirm_request_builder

        return confirm_request_builder.ConfirmRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def end_break(self) -> end_break_request_builder.EndBreakRequestBuilder:
        """
        Provides operations to call the endBreak method.
        """
        from .end_break import end_break_request_builder

        return end_break_request_builder.EndBreakRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def start_break(self) -> start_break_request_builder.StartBreakRequestBuilder:
        """
        Provides operations to call the startBreak method.
        """
        from .start_break import start_break_request_builder

        return start_break_request_builder.StartBreakRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class TimeCardItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class TimeCardItemRequestBuilderGetQueryParameters():
        """
        Get timeCards from teamwork
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
    class TimeCardItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[TimeCardItemRequestBuilder.TimeCardItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class TimeCardItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

