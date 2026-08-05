from __future__ import annotations
from collections.abc import Callable
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
from typing import Any, Optional, TYPE_CHECKING, Union
from warnings import warn

if TYPE_CHECKING:
    from .......models.microsoft_apps_file_storage_container_app_usage import MicrosoftAppsFileStorageContainerAppUsage
    from .......models.o_data_errors.o_data_error import ODataError

class MicrosoftAppsFileStorageContainerAppUsageAppItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the usageByApp property of the microsoft.graph.microsoftAppsFileStorageContainerGeoUsage entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new MicrosoftAppsFileStorageContainerAppUsageAppItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/reports/microsoftAppsFileStorageContainerUsageSummary/usageByDataLocation/{microsoftAppsFileStorageContainerGeoUsage%2DdataLocationCode}/usageByApp/{microsoftAppsFileStorageContainerAppUsage%2DappId}{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete navigation property usageByApp for reports
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .......models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[MicrosoftAppsFileStorageContainerAppUsageAppItemRequestBuilderGetQueryParameters]] = None) -> Optional[MicrosoftAppsFileStorageContainerAppUsage]:
        """
        Storage usage data broken down by application within this geographic location. Expandable using $expand=usageByApp.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[MicrosoftAppsFileStorageContainerAppUsage]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .......models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .......models.microsoft_apps_file_storage_container_app_usage import MicrosoftAppsFileStorageContainerAppUsage

        return await self.request_adapter.send_async(request_info, MicrosoftAppsFileStorageContainerAppUsage, error_mapping)
    
    async def patch(self,body: MicrosoftAppsFileStorageContainerAppUsage, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[MicrosoftAppsFileStorageContainerAppUsage]:
        """
        Update the navigation property usageByApp in reports
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[MicrosoftAppsFileStorageContainerAppUsage]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from .......models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .......models.microsoft_apps_file_storage_container_app_usage import MicrosoftAppsFileStorageContainerAppUsage

        return await self.request_adapter.send_async(request_info, MicrosoftAppsFileStorageContainerAppUsage, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete navigation property usageByApp for reports
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[MicrosoftAppsFileStorageContainerAppUsageAppItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Storage usage data broken down by application within this geographic location. Expandable using $expand=usageByApp.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: MicrosoftAppsFileStorageContainerAppUsage, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the navigation property usageByApp in reports
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PATCH, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> MicrosoftAppsFileStorageContainerAppUsageAppItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: MicrosoftAppsFileStorageContainerAppUsageAppItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return MicrosoftAppsFileStorageContainerAppUsageAppItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class MicrosoftAppsFileStorageContainerAppUsageAppItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class MicrosoftAppsFileStorageContainerAppUsageAppItemRequestBuilderGetQueryParameters():
        """
        Storage usage data broken down by application within this geographic location. Expandable using $expand=usageByApp.
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
        expand: Optional[list[str]] = None

        # Select properties to be returned
        select: Optional[list[str]] = None

    
    @dataclass
    class MicrosoftAppsFileStorageContainerAppUsageAppItemRequestBuilderGetRequestConfiguration(RequestConfiguration[MicrosoftAppsFileStorageContainerAppUsageAppItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class MicrosoftAppsFileStorageContainerAppUsageAppItemRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

