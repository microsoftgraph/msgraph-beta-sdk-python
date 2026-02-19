from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .count.count_request_builder import CountRequestBuilder
    from .item.aggregated_environment_kind_item_request_builder import AggregatedEnvironmentKindItemRequestBuilder

class AggregationsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /security/zones/{zone-id}/aggregations
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new AggregationsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/security/zones/{zone%2Did}/aggregations", path_parameters)
    
    def by_aggregated_environment_kind(self,aggregated_environment_kind: str) -> AggregatedEnvironmentKindItemRequestBuilder:
        """
        Provides operations to manage the aggregations property of the microsoft.graph.security.zone entity.
        param aggregated_environment_kind: The unique identifier of aggregatedEnvironment
        Returns: AggregatedEnvironmentKindItemRequestBuilder
        """
        if aggregated_environment_kind is None:
            raise TypeError("aggregated_environment_kind cannot be null.")
        from .item.aggregated_environment_kind_item_request_builder import AggregatedEnvironmentKindItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["aggregatedEnvironment%2Dkind"] = aggregated_environment_kind
        return AggregatedEnvironmentKindItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @property
    def count(self) -> CountRequestBuilder:
        """
        Provides operations to count the resources in the collection.
        """
        from .count.count_request_builder import CountRequestBuilder

        return CountRequestBuilder(self.request_adapter, self.path_parameters)
    

