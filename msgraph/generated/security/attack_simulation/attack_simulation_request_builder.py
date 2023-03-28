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
    from ...models import attack_simulation_root
    from ...models.o_data_errors import o_data_error
    from .operations import operations_request_builder
    from .operations.item import attack_simulation_operation_item_request_builder
    from .payloads import payloads_request_builder
    from .payloads.item import payload_item_request_builder
    from .simulation_automations import simulation_automations_request_builder
    from .simulation_automations.item import simulation_automation_item_request_builder
    from .simulations import simulations_request_builder
    from .simulations.item import simulation_item_request_builder

class AttackSimulationRequestBuilder():
    """
    Provides operations to manage the attackSimulation property of the microsoft.graph.security entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new AttackSimulationRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/security/attackSimulation{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[AttackSimulationRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property attackSimulation for security
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ...models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[AttackSimulationRequestBuilderGetRequestConfiguration] = None) -> Optional[attack_simulation_root.AttackSimulationRoot]:
        """
        Provides tenants capability to launch a simulated and realistic phishing attack and learn from it.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[attack_simulation_root.AttackSimulationRoot]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models import attack_simulation_root

        return await self.request_adapter.send_async(request_info, attack_simulation_root.AttackSimulationRoot, error_mapping)
    
    def operations_by_id(self,id: str) -> attack_simulation_operation_item_request_builder.AttackSimulationOperationItemRequestBuilder:
        """
        Provides operations to manage the operations property of the microsoft.graph.attackSimulationRoot entity.
        Args:
            id: Unique identifier of the item
        Returns: attack_simulation_operation_item_request_builder.AttackSimulationOperationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .operations.item import attack_simulation_operation_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["attackSimulationOperation%2Did"] = id
        return attack_simulation_operation_item_request_builder.AttackSimulationOperationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def patch(self,body: Optional[attack_simulation_root.AttackSimulationRoot] = None, request_configuration: Optional[AttackSimulationRequestBuilderPatchRequestConfiguration] = None) -> Optional[attack_simulation_root.AttackSimulationRoot]:
        """
        Update the navigation property attackSimulation in security
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[attack_simulation_root.AttackSimulationRoot]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ...models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models import attack_simulation_root

        return await self.request_adapter.send_async(request_info, attack_simulation_root.AttackSimulationRoot, error_mapping)
    
    def payloads_by_id(self,id: str) -> payload_item_request_builder.PayloadItemRequestBuilder:
        """
        Provides operations to manage the payloads property of the microsoft.graph.attackSimulationRoot entity.
        Args:
            id: Unique identifier of the item
        Returns: payload_item_request_builder.PayloadItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .payloads.item import payload_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["payload%2Did"] = id
        return payload_item_request_builder.PayloadItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def simulation_automations_by_id(self,id: str) -> simulation_automation_item_request_builder.SimulationAutomationItemRequestBuilder:
        """
        Provides operations to manage the simulationAutomations property of the microsoft.graph.attackSimulationRoot entity.
        Args:
            id: Unique identifier of the item
        Returns: simulation_automation_item_request_builder.SimulationAutomationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .simulation_automations.item import simulation_automation_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["simulationAutomation%2Did"] = id
        return simulation_automation_item_request_builder.SimulationAutomationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def simulations_by_id(self,id: str) -> simulation_item_request_builder.SimulationItemRequestBuilder:
        """
        Provides operations to manage the simulations property of the microsoft.graph.attackSimulationRoot entity.
        Args:
            id: Unique identifier of the item
        Returns: simulation_item_request_builder.SimulationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .simulations.item import simulation_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["simulation%2Did"] = id
        return simulation_item_request_builder.SimulationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def to_delete_request_information(self,request_configuration: Optional[AttackSimulationRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property attackSimulation for security
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
    
    def to_get_request_information(self,request_configuration: Optional[AttackSimulationRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Provides tenants capability to launch a simulated and realistic phishing attack and learn from it.
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
    
    def to_patch_request_information(self,body: Optional[attack_simulation_root.AttackSimulationRoot] = None, request_configuration: Optional[AttackSimulationRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property attackSimulation in security
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
    def operations(self) -> operations_request_builder.OperationsRequestBuilder:
        """
        Provides operations to manage the operations property of the microsoft.graph.attackSimulationRoot entity.
        """
        from .operations import operations_request_builder

        return operations_request_builder.OperationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def payloads(self) -> payloads_request_builder.PayloadsRequestBuilder:
        """
        Provides operations to manage the payloads property of the microsoft.graph.attackSimulationRoot entity.
        """
        from .payloads import payloads_request_builder

        return payloads_request_builder.PayloadsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def simulation_automations(self) -> simulation_automations_request_builder.SimulationAutomationsRequestBuilder:
        """
        Provides operations to manage the simulationAutomations property of the microsoft.graph.attackSimulationRoot entity.
        """
        from .simulation_automations import simulation_automations_request_builder

        return simulation_automations_request_builder.SimulationAutomationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def simulations(self) -> simulations_request_builder.SimulationsRequestBuilder:
        """
        Provides operations to manage the simulations property of the microsoft.graph.attackSimulationRoot entity.
        """
        from .simulations import simulations_request_builder

        return simulations_request_builder.SimulationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class AttackSimulationRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class AttackSimulationRequestBuilderGetQueryParameters():
        """
        Provides tenants capability to launch a simulated and realistic phishing attack and learn from it.
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
    class AttackSimulationRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[AttackSimulationRequestBuilder.AttackSimulationRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class AttackSimulationRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

