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
    from ...models.industry_data import industry_data_root
    from ...models.o_data_errors import o_data_error
    from .data_connectors import data_connectors_request_builder
    from .data_connectors.item import industry_data_connector_item_request_builder
    from .inbound_flows import inbound_flows_request_builder
    from .inbound_flows.item import inbound_flow_item_request_builder
    from .operations import operations_request_builder
    from .operations.item import long_running_operation_item_request_builder
    from .reference_definitions import reference_definitions_request_builder
    from .reference_definitions.item import reference_definition_item_request_builder
    from .role_groups import role_groups_request_builder
    from .role_groups.item import role_group_item_request_builder
    from .runs import runs_request_builder
    from .runs.item import industry_data_run_item_request_builder
    from .source_systems import source_systems_request_builder
    from .source_systems.item import source_system_definition_item_request_builder
    from .years import years_request_builder
    from .years.item import year_time_period_definition_item_request_builder

class IndustryDataRequestBuilder():
    """
    Provides operations to manage the industryData property of the microsoft.graph.externalConnectors.external entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new IndustryDataRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/external/industryData{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def data_connectors_by_id(self,id: str) -> industry_data_connector_item_request_builder.IndustryDataConnectorItemRequestBuilder:
        """
        Provides operations to manage the dataConnectors property of the microsoft.graph.industryData.industryDataRoot entity.
        Args:
            id: Unique identifier of the item
        Returns: industry_data_connector_item_request_builder.IndustryDataConnectorItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .data_connectors.item import industry_data_connector_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["industryDataConnector%2Did"] = id
        return industry_data_connector_item_request_builder.IndustryDataConnectorItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[IndustryDataRequestBuilderGetRequestConfiguration] = None) -> Optional[industry_data_root.IndustryDataRoot]:
        """
        Get industryData from external
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[industry_data_root.IndustryDataRoot]
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
        from ...models.industry_data import industry_data_root

        return await self.request_adapter.send_async(request_info, industry_data_root.IndustryDataRoot, error_mapping)
    
    def inbound_flows_by_id(self,id: str) -> inbound_flow_item_request_builder.InboundFlowItemRequestBuilder:
        """
        Provides operations to manage the inboundFlows property of the microsoft.graph.industryData.industryDataRoot entity.
        Args:
            id: Unique identifier of the item
        Returns: inbound_flow_item_request_builder.InboundFlowItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .inbound_flows.item import inbound_flow_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["inboundFlow%2Did"] = id
        return inbound_flow_item_request_builder.InboundFlowItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def operations_by_id(self,id: str) -> long_running_operation_item_request_builder.LongRunningOperationItemRequestBuilder:
        """
        Provides operations to manage the operations property of the microsoft.graph.industryData.industryDataRoot entity.
        Args:
            id: Unique identifier of the item
        Returns: long_running_operation_item_request_builder.LongRunningOperationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .operations.item import long_running_operation_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["longRunningOperation%2Did"] = id
        return long_running_operation_item_request_builder.LongRunningOperationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def reference_definitions_by_id(self,id: str) -> reference_definition_item_request_builder.ReferenceDefinitionItemRequestBuilder:
        """
        Provides operations to manage the referenceDefinitions property of the microsoft.graph.industryData.industryDataRoot entity.
        Args:
            id: Unique identifier of the item
        Returns: reference_definition_item_request_builder.ReferenceDefinitionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .reference_definitions.item import reference_definition_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["referenceDefinition%2Did"] = id
        return reference_definition_item_request_builder.ReferenceDefinitionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def role_groups_by_id(self,id: str) -> role_group_item_request_builder.RoleGroupItemRequestBuilder:
        """
        Provides operations to manage the roleGroups property of the microsoft.graph.industryData.industryDataRoot entity.
        Args:
            id: Unique identifier of the item
        Returns: role_group_item_request_builder.RoleGroupItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .role_groups.item import role_group_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["roleGroup%2Did"] = id
        return role_group_item_request_builder.RoleGroupItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def runs_by_id(self,id: str) -> industry_data_run_item_request_builder.IndustryDataRunItemRequestBuilder:
        """
        Provides operations to manage the runs property of the microsoft.graph.industryData.industryDataRoot entity.
        Args:
            id: Unique identifier of the item
        Returns: industry_data_run_item_request_builder.IndustryDataRunItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .runs.item import industry_data_run_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["industryDataRun%2Did"] = id
        return industry_data_run_item_request_builder.IndustryDataRunItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def source_systems_by_id(self,id: str) -> source_system_definition_item_request_builder.SourceSystemDefinitionItemRequestBuilder:
        """
        Provides operations to manage the sourceSystems property of the microsoft.graph.industryData.industryDataRoot entity.
        Args:
            id: Unique identifier of the item
        Returns: source_system_definition_item_request_builder.SourceSystemDefinitionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .source_systems.item import source_system_definition_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["sourceSystemDefinition%2Did"] = id
        return source_system_definition_item_request_builder.SourceSystemDefinitionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def to_get_request_information(self,request_configuration: Optional[IndustryDataRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get industryData from external
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
    
    def years_by_id(self,id: str) -> year_time_period_definition_item_request_builder.YearTimePeriodDefinitionItemRequestBuilder:
        """
        Provides operations to manage the years property of the microsoft.graph.industryData.industryDataRoot entity.
        Args:
            id: Unique identifier of the item
        Returns: year_time_period_definition_item_request_builder.YearTimePeriodDefinitionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .years.item import year_time_period_definition_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["yearTimePeriodDefinition%2Did"] = id
        return year_time_period_definition_item_request_builder.YearTimePeriodDefinitionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @property
    def data_connectors(self) -> data_connectors_request_builder.DataConnectorsRequestBuilder:
        """
        Provides operations to manage the dataConnectors property of the microsoft.graph.industryData.industryDataRoot entity.
        """
        from .data_connectors import data_connectors_request_builder

        return data_connectors_request_builder.DataConnectorsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def inbound_flows(self) -> inbound_flows_request_builder.InboundFlowsRequestBuilder:
        """
        Provides operations to manage the inboundFlows property of the microsoft.graph.industryData.industryDataRoot entity.
        """
        from .inbound_flows import inbound_flows_request_builder

        return inbound_flows_request_builder.InboundFlowsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def operations(self) -> operations_request_builder.OperationsRequestBuilder:
        """
        Provides operations to manage the operations property of the microsoft.graph.industryData.industryDataRoot entity.
        """
        from .operations import operations_request_builder

        return operations_request_builder.OperationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reference_definitions(self) -> reference_definitions_request_builder.ReferenceDefinitionsRequestBuilder:
        """
        Provides operations to manage the referenceDefinitions property of the microsoft.graph.industryData.industryDataRoot entity.
        """
        from .reference_definitions import reference_definitions_request_builder

        return reference_definitions_request_builder.ReferenceDefinitionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def role_groups(self) -> role_groups_request_builder.RoleGroupsRequestBuilder:
        """
        Provides operations to manage the roleGroups property of the microsoft.graph.industryData.industryDataRoot entity.
        """
        from .role_groups import role_groups_request_builder

        return role_groups_request_builder.RoleGroupsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def runs(self) -> runs_request_builder.RunsRequestBuilder:
        """
        Provides operations to manage the runs property of the microsoft.graph.industryData.industryDataRoot entity.
        """
        from .runs import runs_request_builder

        return runs_request_builder.RunsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def source_systems(self) -> source_systems_request_builder.SourceSystemsRequestBuilder:
        """
        Provides operations to manage the sourceSystems property of the microsoft.graph.industryData.industryDataRoot entity.
        """
        from .source_systems import source_systems_request_builder

        return source_systems_request_builder.SourceSystemsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def years(self) -> years_request_builder.YearsRequestBuilder:
        """
        Provides operations to manage the years property of the microsoft.graph.industryData.industryDataRoot entity.
        """
        from .years import years_request_builder

        return years_request_builder.YearsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class IndustryDataRequestBuilderGetQueryParameters():
        """
        Get industryData from external
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
    class IndustryDataRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[IndustryDataRequestBuilder.IndustryDataRequestBuilderGetQueryParameters] = None

    

