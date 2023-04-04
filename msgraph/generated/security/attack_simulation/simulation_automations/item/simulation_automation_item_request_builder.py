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
    from .....models import simulation_automation
    from .....models.o_data_errors import o_data_error
    from .runs import runs_request_builder
    from .runs.item import simulation_automation_run_item_request_builder

class SimulationAutomationItemRequestBuilder():
    """
    Provides operations to manage the simulationAutomations property of the microsoft.graph.attackSimulationRoot entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new SimulationAutomationItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/security/attackSimulation/simulationAutomations/{simulationAutomation%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[SimulationAutomationItemRequestBuilderDeleteRequestConfiguration] = None) -> bytes:
        """
        Delete navigation property simulationAutomations for security
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: bytes
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
        return await self.request_adapter.send_primitive_async(request_info, "bytes", error_mapping)
    
    async def get(self,request_configuration: Optional[SimulationAutomationItemRequestBuilderGetRequestConfiguration] = None) -> Optional[simulation_automation.SimulationAutomation]:
        """
        Represents simulation automation created to run on a tenant.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[simulation_automation.SimulationAutomation]
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
        from .....models import simulation_automation

        return await self.request_adapter.send_async(request_info, simulation_automation.SimulationAutomation, error_mapping)
    
    async def patch(self,body: Optional[simulation_automation.SimulationAutomation] = None, request_configuration: Optional[SimulationAutomationItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[simulation_automation.SimulationAutomation]:
        """
        Update the navigation property simulationAutomations in security
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[simulation_automation.SimulationAutomation]
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
        from .....models import simulation_automation

        return await self.request_adapter.send_async(request_info, simulation_automation.SimulationAutomation, error_mapping)
    
    def runs_by_id(self,id: str) -> simulation_automation_run_item_request_builder.SimulationAutomationRunItemRequestBuilder:
        """
        Provides operations to manage the runs property of the microsoft.graph.simulationAutomation entity.
        Args:
            id: Unique identifier of the item
        Returns: simulation_automation_run_item_request_builder.SimulationAutomationRunItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .runs.item import simulation_automation_run_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["simulationAutomationRun%2Did"] = id
        return simulation_automation_run_item_request_builder.SimulationAutomationRunItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def to_delete_request_information(self,request_configuration: Optional[SimulationAutomationItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property simulationAutomations for security
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
    
    def to_get_request_information(self,request_configuration: Optional[SimulationAutomationItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Represents simulation automation created to run on a tenant.
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
    
    def to_patch_request_information(self,body: Optional[simulation_automation.SimulationAutomation] = None, request_configuration: Optional[SimulationAutomationItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property simulationAutomations in security
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
    def runs(self) -> runs_request_builder.RunsRequestBuilder:
        """
        Provides operations to manage the runs property of the microsoft.graph.simulationAutomation entity.
        """
        from .runs import runs_request_builder

        return runs_request_builder.RunsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class SimulationAutomationItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class SimulationAutomationItemRequestBuilderGetQueryParameters():
        """
        Represents simulation automation created to run on a tenant.
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
    class SimulationAutomationItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[SimulationAutomationItemRequestBuilder.SimulationAutomationItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class SimulationAutomationItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

