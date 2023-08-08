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
    from ..models.device_local_credential_info import DeviceLocalCredentialInfo
    from ..models.device_local_credential_info_collection_response import DeviceLocalCredentialInfoCollectionResponse
    from ..models.o_data_errors.o_data_error import ODataError
    from .item.device_local_credential_info_item_request_builder import DeviceLocalCredentialInfoItemRequestBuilder

class DeviceLocalCredentialsRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the collection of deviceLocalCredentialInfo entities.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new DeviceLocalCredentialsRequestBuilder and sets the default values.
        Args:
            path_parameters: The raw url or the Url template parameters for the request.
            request_adapter: The request adapter to use to execute the requests.
        """
        super().__init__(request_adapter, "{+baseurl}/deviceLocalCredentials{?%24search,%24filter,%24orderby,%24select}", path_parameters)
    
    def by_device_local_credential_info_id(self,device_local_credential_info_id: str) -> DeviceLocalCredentialInfoItemRequestBuilder:
        """
        Provides operations to manage the collection of deviceLocalCredentialInfo entities.
        Args:
            device_local_credential_info_id: Unique identifier of the item
        Returns: DeviceLocalCredentialInfoItemRequestBuilder
        """
        if not device_local_credential_info_id:
            raise TypeError("device_local_credential_info_id cannot be null.")
        from .item.device_local_credential_info_item_request_builder import DeviceLocalCredentialInfoItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["deviceLocalCredentialInfo%2Did"] = device_local_credential_info_id
        return DeviceLocalCredentialInfoItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[DeviceLocalCredentialsRequestBuilderGetRequestConfiguration] = None) -> Optional[DeviceLocalCredentialInfoCollectionResponse]:
        """
        Get a list of the deviceLocalCredentialInfo objects and their properties excluding the credentials. 
        Args:
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[DeviceLocalCredentialInfoCollectionResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ..models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.device_local_credential_info_collection_response import DeviceLocalCredentialInfoCollectionResponse

        return await self.request_adapter.send_async(request_info, DeviceLocalCredentialInfoCollectionResponse, error_mapping)
    
    async def post(self,body: Optional[DeviceLocalCredentialInfo] = None, request_configuration: Optional[DeviceLocalCredentialsRequestBuilderPostRequestConfiguration] = None) -> Optional[DeviceLocalCredentialInfo]:
        """
        Add new entity to deviceLocalCredentials
        Args:
            body: The request body
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[DeviceLocalCredentialInfo]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ..models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.device_local_credential_info import DeviceLocalCredentialInfo

        return await self.request_adapter.send_async(request_info, DeviceLocalCredentialInfo, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[DeviceLocalCredentialsRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get a list of the deviceLocalCredentialInfo objects and their properties excluding the credentials. 
        Args:
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
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
    
    def to_post_request_information(self,body: Optional[DeviceLocalCredentialInfo] = None, request_configuration: Optional[DeviceLocalCredentialsRequestBuilderPostRequestConfiguration] = None) -> RequestInformation:
        """
        Add new entity to deviceLocalCredentials
        Args:
            body: The request body
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.POST
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    @dataclass
    class DeviceLocalCredentialsRequestBuilderGetQueryParameters():
        """
        Get a list of the deviceLocalCredentialInfo objects and their properties excluding the credentials. 
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            Args:
                original_name: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
                raise TypeError("original_name cannot be null.")
            if original_name == "filter":
                return "%24filter"
            if original_name == "orderby":
                return "%24orderby"
            if original_name == "search":
                return "%24search"
            if original_name == "select":
                return "%24select"
            return original_name
        
        # Filter items by property values
        filter: Optional[str] = None

        # Order items by property values
        orderby: Optional[List[str]] = None

        # Search items by search phrases
        search: Optional[str] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class DeviceLocalCredentialsRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[DeviceLocalCredentialsRequestBuilder.DeviceLocalCredentialsRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class DeviceLocalCredentialsRequestBuilderPostRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

