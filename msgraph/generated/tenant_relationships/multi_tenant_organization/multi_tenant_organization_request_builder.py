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
    from ...models.multi_tenant_organization import MultiTenantOrganization
    from ...models.o_data_errors.o_data_error import ODataError
    from .join_request.join_request_request_builder import JoinRequestRequestBuilder
    from .tenants.tenants_request_builder import TenantsRequestBuilder

class MultiTenantOrganizationRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the multiTenantOrganization property of the microsoft.graph.tenantRelationship entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new MultiTenantOrganizationRequestBuilder and sets the default values.
        Args:
            path_parameters: The raw url or the Url template parameters for the request.
            request_adapter: The request adapter to use to execute the requests.
        """
        super().__init__(request_adapter, "{+baseurl}/tenantRelationships/multiTenantOrganization{?%24select,%24expand}", path_parameters)
    
    async def delete(self,request_configuration: Optional[MultiTenantOrganizationRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property multiTenantOrganization for tenantRelationships
        Args:
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[MultiTenantOrganizationRequestBuilderGetRequestConfiguration] = None) -> Optional[MultiTenantOrganization]:
        """
        Get multiTenantOrganization from tenantRelationships
        Args:
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[MultiTenantOrganization]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.multi_tenant_organization import MultiTenantOrganization

        return await self.request_adapter.send_async(request_info, MultiTenantOrganization, error_mapping)
    
    async def put(self,body: Optional[MultiTenantOrganization] = None, request_configuration: Optional[MultiTenantOrganizationRequestBuilderPutRequestConfiguration] = None) -> Optional[MultiTenantOrganization]:
        """
        Update the navigation property multiTenantOrganization in tenantRelationships
        Args:
            body: The request body
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[MultiTenantOrganization]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.multi_tenant_organization import MultiTenantOrganization

        return await self.request_adapter.send_async(request_info, MultiTenantOrganization, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[MultiTenantOrganizationRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property multiTenantOrganization for tenantRelationships
        Args:
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.DELETE
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[MultiTenantOrganizationRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get multiTenantOrganization from tenantRelationships
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
    
    def to_put_request_information(self,body: Optional[MultiTenantOrganization] = None, request_configuration: Optional[MultiTenantOrganizationRequestBuilderPutRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property multiTenantOrganization in tenantRelationships
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
        request_info.http_method = Method.PUT
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    @property
    def join_request(self) -> JoinRequestRequestBuilder:
        """
        Provides operations to manage the joinRequest property of the microsoft.graph.multiTenantOrganization entity.
        """
        from .join_request.join_request_request_builder import JoinRequestRequestBuilder

        return JoinRequestRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tenants(self) -> TenantsRequestBuilder:
        """
        Provides operations to manage the tenants property of the microsoft.graph.multiTenantOrganization entity.
        """
        from .tenants.tenants_request_builder import TenantsRequestBuilder

        return TenantsRequestBuilder(self.request_adapter, self.path_parameters)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class MultiTenantOrganizationRequestBuilderDeleteRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
    @dataclass
    class MultiTenantOrganizationRequestBuilderGetQueryParameters():
        """
        Get multiTenantOrganization from tenantRelationships
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
            if original_name == "expand":
                return "%24expand"
            if original_name == "select":
                return "%24select"
            return original_name
        
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class MultiTenantOrganizationRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[MultiTenantOrganizationRequestBuilder.MultiTenantOrganizationRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class MultiTenantOrganizationRequestBuilderPutRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

