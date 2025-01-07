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
    from ......models.device import Device
    from ......models.o_data_errors.o_data_error import ODataError

class DeviceInstancesWithDeviceIdRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the deviceInstances property of the microsoft.graph.deviceTemplate entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]], device_id: Optional[str] = None) -> None:
        """
        Instantiates a new DeviceInstancesWithDeviceIdRequestBuilder and sets the default values.
        param device_id: Alternate key of device
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        if isinstance(path_parameters, dict):
            path_parameters['deviceId'] = device_id
        super().__init__(request_adapter, "{+baseurl}/directory/templates/deviceTemplates/{deviceTemplate%2Did}/deviceInstances(deviceId='{deviceId}'){?%24expand,%24select}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[DeviceInstancesWithDeviceIdRequestBuilderGetQueryParameters]] = None) -> Optional[Device]:
        """
        Collection of device objects created based on this template.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Device]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.device import Device

        return await self.request_adapter.send_async(request_info, Device, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[DeviceInstancesWithDeviceIdRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Collection of device objects created based on this template.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> DeviceInstancesWithDeviceIdRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: DeviceInstancesWithDeviceIdRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return DeviceInstancesWithDeviceIdRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class DeviceInstancesWithDeviceIdRequestBuilderGetQueryParameters():
        """
        Collection of device objects created based on this template.
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
    class DeviceInstancesWithDeviceIdRequestBuilderGetRequestConfiguration(RequestConfiguration[DeviceInstancesWithDeviceIdRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

