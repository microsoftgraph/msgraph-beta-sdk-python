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
    from ...models.networkaccess.settings import Settings
    from ...models.o_data_errors.o_data_error import ODataError
    from .conditional_access.conditional_access_request_builder import ConditionalAccessRequestBuilder
    from .cross_tenant_access.cross_tenant_access_request_builder import CrossTenantAccessRequestBuilder
    from .enriched_audit_logs.enriched_audit_logs_request_builder import EnrichedAuditLogsRequestBuilder
    from .forwarding_options.forwarding_options_request_builder import ForwardingOptionsRequestBuilder

class SettingsRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the settings property of the microsoft.graph.networkaccess.networkAccessRoot entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new SettingsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/networkAccess/settings{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete navigation property settings for networkAccess
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[SettingsRequestBuilderGetQueryParameters]] = None) -> Optional[Settings]:
        """
        Global Secure Access settings.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Settings]
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
        from ...models.networkaccess.settings import Settings

        return await self.request_adapter.send_async(request_info, Settings, error_mapping)
    
    async def patch(self,body: Settings, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[Settings]:
        """
        Update the navigation property settings in networkAccess
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Settings]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.networkaccess.settings import Settings

        return await self.request_adapter.send_async(request_info, Settings, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete navigation property settings for networkAccess
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[SettingsRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Global Secure Access settings.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: Settings, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the navigation property settings in networkAccess
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
    
    def with_url(self,raw_url: str) -> SettingsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: SettingsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return SettingsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def conditional_access(self) -> ConditionalAccessRequestBuilder:
        """
        Provides operations to manage the conditionalAccess property of the microsoft.graph.networkaccess.settings entity.
        """
        from .conditional_access.conditional_access_request_builder import ConditionalAccessRequestBuilder

        return ConditionalAccessRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def cross_tenant_access(self) -> CrossTenantAccessRequestBuilder:
        """
        Provides operations to manage the crossTenantAccess property of the microsoft.graph.networkaccess.settings entity.
        """
        from .cross_tenant_access.cross_tenant_access_request_builder import CrossTenantAccessRequestBuilder

        return CrossTenantAccessRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def enriched_audit_logs(self) -> EnrichedAuditLogsRequestBuilder:
        """
        Provides operations to manage the enrichedAuditLogs property of the microsoft.graph.networkaccess.settings entity.
        """
        from .enriched_audit_logs.enriched_audit_logs_request_builder import EnrichedAuditLogsRequestBuilder

        return EnrichedAuditLogsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def forwarding_options(self) -> ForwardingOptionsRequestBuilder:
        """
        Provides operations to manage the forwardingOptions property of the microsoft.graph.networkaccess.settings entity.
        """
        from .forwarding_options.forwarding_options_request_builder import ForwardingOptionsRequestBuilder

        return ForwardingOptionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class SettingsRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class SettingsRequestBuilderGetQueryParameters():
        """
        Global Secure Access settings.
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
    class SettingsRequestBuilderGetRequestConfiguration(RequestConfiguration[SettingsRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class SettingsRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

