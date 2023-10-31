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
    from .......models.o_data_errors.o_data_error import ODataError
    from .attributes.attributes_request_builder import AttributesRequestBuilder

class GraphOnAttributeCollectionExternalUsersSelfServiceSignUpRequestBuilder(BaseRequestBuilder):
    """
    Casts the previous resource to onAttributeCollectionExternalUsersSelfServiceSignUp.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new GraphOnAttributeCollectionExternalUsersSelfServiceSignUpRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/identity/authenticationEventsFlows/{authenticationEventsFlow%2Did}/graph.externalUsersSelfServiceSignUpEventsFlow/onAttributeCollection/graph.onAttributeCollectionExternalUsersSelfServiceSignUp", path_parameters)
    
    async def get(self,request_configuration: Optional[GraphOnAttributeCollectionExternalUsersSelfServiceSignUpRequestBuilderGetRequestConfiguration] = None) -> bytes:
        """
        Get the items of type microsoft.graph.onAttributeCollectionExternalUsersSelfServiceSignUp in the microsoft.graph.onAttributeCollectionHandler collection
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: bytes
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_primitive_async(request_info, "bytes", error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[GraphOnAttributeCollectionExternalUsersSelfServiceSignUpRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get the items of type microsoft.graph.onAttributeCollectionExternalUsersSelfServiceSignUp in the microsoft.graph.onAttributeCollectionHandler collection
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers.try_add("Accept", "application/json, application/json")
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> GraphOnAttributeCollectionExternalUsersSelfServiceSignUpRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: GraphOnAttributeCollectionExternalUsersSelfServiceSignUpRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return GraphOnAttributeCollectionExternalUsersSelfServiceSignUpRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def attributes(self) -> AttributesRequestBuilder:
        """
        Provides operations to manage the attributes property of the microsoft.graph.onAttributeCollectionExternalUsersSelfServiceSignUp entity.
        """
        from .attributes.attributes_request_builder import AttributesRequestBuilder

        return AttributesRequestBuilder(self.request_adapter, self.path_parameters)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class GraphOnAttributeCollectionExternalUsersSelfServiceSignUpRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

