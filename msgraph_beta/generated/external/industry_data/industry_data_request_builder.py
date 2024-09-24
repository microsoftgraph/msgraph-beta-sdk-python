from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.default_query_parameters import QueryParameters
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from warnings import warn

if TYPE_CHECKING:
    from ...models.industry_data.industry_data_root import IndustryDataRoot
    from ...models.o_data_errors.o_data_error import ODataError
    from .data_connectors.data_connectors_request_builder import DataConnectorsRequestBuilder
    from .inbound_flows.inbound_flows_request_builder import InboundFlowsRequestBuilder
    from .operations.operations_request_builder import OperationsRequestBuilder
    from .outbound_provisioning_flow_sets.outbound_provisioning_flow_sets_request_builder import OutboundProvisioningFlowSetsRequestBuilder
    from .reference_definitions.reference_definitions_request_builder import ReferenceDefinitionsRequestBuilder
    from .role_groups.role_groups_request_builder import RoleGroupsRequestBuilder
    from .runs.runs_request_builder import RunsRequestBuilder
    from .source_systems.source_systems_request_builder import SourceSystemsRequestBuilder
    from .years.years_request_builder import YearsRequestBuilder

class IndustryDataRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the industryData property of the microsoft.graph.externalConnectors.external entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new IndustryDataRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/external/industryData{?%24expand,%24select}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[IndustryDataRequestBuilderGetQueryParameters]] = None) -> Optional[IndustryDataRoot]:
        """
        Get industryData from external
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[IndustryDataRoot]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.industry_data.industry_data_root import IndustryDataRoot

        return await self.request_adapter.send_async(request_info, IndustryDataRoot, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[IndustryDataRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Get industryData from external
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> IndustryDataRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: IndustryDataRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return IndustryDataRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def data_connectors(self) -> DataConnectorsRequestBuilder:
        """
        Provides operations to manage the dataConnectors property of the microsoft.graph.industryData.industryDataRoot entity.
        """
        from .data_connectors.data_connectors_request_builder import DataConnectorsRequestBuilder

        return DataConnectorsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def inbound_flows(self) -> InboundFlowsRequestBuilder:
        """
        Provides operations to manage the inboundFlows property of the microsoft.graph.industryData.industryDataRoot entity.
        """
        from .inbound_flows.inbound_flows_request_builder import InboundFlowsRequestBuilder

        return InboundFlowsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def operations(self) -> OperationsRequestBuilder:
        """
        Provides operations to manage the operations property of the microsoft.graph.industryData.industryDataRoot entity.
        """
        from .operations.operations_request_builder import OperationsRequestBuilder

        return OperationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def outbound_provisioning_flow_sets(self) -> OutboundProvisioningFlowSetsRequestBuilder:
        """
        Provides operations to manage the outboundProvisioningFlowSets property of the microsoft.graph.industryData.industryDataRoot entity.
        """
        from .outbound_provisioning_flow_sets.outbound_provisioning_flow_sets_request_builder import OutboundProvisioningFlowSetsRequestBuilder

        return OutboundProvisioningFlowSetsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reference_definitions(self) -> ReferenceDefinitionsRequestBuilder:
        """
        Provides operations to manage the referenceDefinitions property of the microsoft.graph.industryData.industryDataRoot entity.
        """
        from .reference_definitions.reference_definitions_request_builder import ReferenceDefinitionsRequestBuilder

        return ReferenceDefinitionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def role_groups(self) -> RoleGroupsRequestBuilder:
        """
        Provides operations to manage the roleGroups property of the microsoft.graph.industryData.industryDataRoot entity.
        """
        from .role_groups.role_groups_request_builder import RoleGroupsRequestBuilder

        return RoleGroupsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def runs(self) -> RunsRequestBuilder:
        """
        Provides operations to manage the runs property of the microsoft.graph.industryData.industryDataRoot entity.
        """
        from .runs.runs_request_builder import RunsRequestBuilder

        return RunsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def source_systems(self) -> SourceSystemsRequestBuilder:
        """
        Provides operations to manage the sourceSystems property of the microsoft.graph.industryData.industryDataRoot entity.
        """
        from .source_systems.source_systems_request_builder import SourceSystemsRequestBuilder

        return SourceSystemsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def years(self) -> YearsRequestBuilder:
        """
        Provides operations to manage the years property of the microsoft.graph.industryData.industryDataRoot entity.
        """
        from .years.years_request_builder import YearsRequestBuilder

        return YearsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class IndustryDataRequestBuilderGetQueryParameters():
        """
        Get industryData from external
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
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

    
    @dataclass
    class IndustryDataRequestBuilderGetRequestConfiguration(RequestConfiguration[IndustryDataRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

