from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..models.o_data_errors.o_data_error import ODataError
    from ..models.workplace import Workplace
    from .sensor_devices.sensor_devices_request_builder import SensorDevicesRequestBuilder
    from .sensor_devices_with_device_id.sensor_devices_with_device_id_request_builder import SensorDevicesWithDeviceIdRequestBuilder

class WorkplaceRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the workplace singleton.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new WorkplaceRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/workplace{?%24expand,%24select}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration] = None) -> Optional[Workplace]:
        """
        Get workplace
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Workplace]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ..models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.workplace import Workplace

        return await self.request_adapter.send_async(request_info, Workplace, error_mapping)
    
    async def patch(self,body: Optional[Workplace] = None, request_configuration: Optional[RequestConfiguration] = None) -> Optional[Workplace]:
        """
        Update workplace
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Workplace]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ..models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.workplace import Workplace

        return await self.request_adapter.send_async(request_info, Workplace, error_mapping)
    
    def sensor_devices_with_device_id(self,device_id: Optional[str] = None) -> SensorDevicesWithDeviceIdRequestBuilder:
        """
        Provides operations to manage the sensorDevices property of the microsoft.graph.workplace entity.
        param device_id: Alternate key of workplaceSensorDevice
        Returns: SensorDevicesWithDeviceIdRequestBuilder
        """
        if not device_id:
            raise TypeError("device_id cannot be null.")
        from .sensor_devices_with_device_id.sensor_devices_with_device_id_request_builder import SensorDevicesWithDeviceIdRequestBuilder

        return SensorDevicesWithDeviceIdRequestBuilder(self.request_adapter, self.path_parameters, device_id)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        Get workplace
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: Optional[Workplace] = None, request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        Update workplace
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PATCH, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> WorkplaceRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WorkplaceRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return WorkplaceRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def sensor_devices(self) -> SensorDevicesRequestBuilder:
        """
        Provides operations to manage the sensorDevices property of the microsoft.graph.workplace entity.
        """
        from .sensor_devices.sensor_devices_request_builder import SensorDevicesRequestBuilder

        return SensorDevicesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class WorkplaceRequestBuilderGetQueryParameters():
        """
        Get workplace
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
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

    

