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
    from .......models.o_data_errors.o_data_error import ODataError
    from .......models.windows_updates.mdm_app_setting import MdmAppSetting

class MdmAppSettingMdmAppItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the mdmAppSettings property of the microsoft.graph.windowsUpdates.tenantSetting entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new MdmAppSettingMdmAppItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/admin/windows/updates/tenantSettings/mdmAppSettings/{mdmAppSetting%2DmdmAppId}{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete navigation property mdmAppSettings for admin
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
    
    async def get(self,request_configuration: Optional[RequestConfiguration[MdmAppSettingMdmAppItemRequestBuilderGetQueryParameters]] = None) -> Optional[MdmAppSetting]:
        """
        Get an mdmAppSetting resource by its mdmAppId within the current tenant.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[MdmAppSetting]
        Find more info here: https://learn.microsoft.com/graph/api/windowsupdates-mdmappsetting-get?view=graph-rest-beta
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
        from .......models.windows_updates.mdm_app_setting import MdmAppSetting

        return await self.request_adapter.send_async(request_info, MdmAppSetting, error_mapping)
    
    async def patch(self,body: MdmAppSetting, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[MdmAppSetting]:
        """
        Update an mdmAppSetting resource within the current tenant. The mdmAppId is identified by the request URL and can't be changed by this operation.
        param body: Per-MDM-application settings for a tenant, identified by a unique MDM app ID (GUID-formatted string).
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[MdmAppSetting]
        Find more info here: https://learn.microsoft.com/graph/api/windowsupdates-mdmappsetting-update?view=graph-rest-beta
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
        from .......models.windows_updates.mdm_app_setting import MdmAppSetting

        return await self.request_adapter.send_async(request_info, MdmAppSetting, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete navigation property mdmAppSettings for admin
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[MdmAppSettingMdmAppItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Get an mdmAppSetting resource by its mdmAppId within the current tenant.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: MdmAppSetting, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update an mdmAppSetting resource within the current tenant. The mdmAppId is identified by the request URL and can't be changed by this operation.
        param body: Per-MDM-application settings for a tenant, identified by a unique MDM app ID (GUID-formatted string).
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
    
    def with_url(self,raw_url: str) -> MdmAppSettingMdmAppItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: MdmAppSettingMdmAppItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return MdmAppSettingMdmAppItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class MdmAppSettingMdmAppItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class MdmAppSettingMdmAppItemRequestBuilderGetQueryParameters():
        """
        Get an mdmAppSetting resource by its mdmAppId within the current tenant.
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
    class MdmAppSettingMdmAppItemRequestBuilderGetRequestConfiguration(RequestConfiguration[MdmAppSettingMdmAppItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class MdmAppSettingMdmAppItemRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

