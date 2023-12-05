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
    from ....models.multi_tenant_organization_member import MultiTenantOrganizationMember
    from ....models.multi_tenant_organization_member_collection_response import MultiTenantOrganizationMemberCollectionResponse
    from ....models.o_data_errors.o_data_error import ODataError
    from .count.count_request_builder import CountRequestBuilder
    from .item.multi_tenant_organization_member_item_request_builder import MultiTenantOrganizationMemberItemRequestBuilder

class TenantsRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the tenants property of the microsoft.graph.multiTenantOrganization entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new TenantsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/tenantRelationships/multiTenantOrganization/tenants{?%24top,%24skip,%24search,%24filter,%24count,%24orderby,%24select,%24expand}", path_parameters)
    
    def by_multi_tenant_organization_member_id(self,multi_tenant_organization_member_id: str) -> MultiTenantOrganizationMemberItemRequestBuilder:
        """
        Provides operations to manage the tenants property of the microsoft.graph.multiTenantOrganization entity.
        param multi_tenant_organization_member_id: The unique identifier of multiTenantOrganizationMember
        Returns: MultiTenantOrganizationMemberItemRequestBuilder
        """
        if not multi_tenant_organization_member_id:
            raise TypeError("multi_tenant_organization_member_id cannot be null.")
        from .item.multi_tenant_organization_member_item_request_builder import MultiTenantOrganizationMemberItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["multiTenantOrganizationMember%2Did"] = multi_tenant_organization_member_id
        return MultiTenantOrganizationMemberItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[TenantsRequestBuilderGetRequestConfiguration] = None) -> Optional[MultiTenantOrganizationMemberCollectionResponse]:
        """
        List the tenants and their properties in the multi-tenant organization.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[MultiTenantOrganizationMemberCollectionResponse]
        Find more info here: https://learn.microsoft.com/graph/api/multitenantorganization-list-tenants?view=graph-rest-1.0
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.multi_tenant_organization_member_collection_response import MultiTenantOrganizationMemberCollectionResponse

        return await self.request_adapter.send_async(request_info, MultiTenantOrganizationMemberCollectionResponse, error_mapping)
    
    async def post(self,body: Optional[MultiTenantOrganizationMember] = None, request_configuration: Optional[TenantsRequestBuilderPostRequestConfiguration] = None) -> Optional[MultiTenantOrganizationMember]:
        """
        Add a tenant to a multitenant organization. The administrator of an owner tenant has the permissions to add tenants to the multitenant organization. The added tenant is in the pending state until the administrator of the added tenant joins the multitenant organization by submitting a join request. A tenant can be part of only one multitenant organization.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[MultiTenantOrganizationMember]
        Find more info here: https://learn.microsoft.com/graph/api/multitenantorganization-post-tenants?view=graph-rest-1.0
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.multi_tenant_organization_member import MultiTenantOrganizationMember

        return await self.request_adapter.send_async(request_info, MultiTenantOrganizationMember, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[TenantsRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        List the tenants and their properties in the multi-tenant organization.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: Optional[MultiTenantOrganizationMember] = None, request_configuration: Optional[TenantsRequestBuilderPostRequestConfiguration] = None) -> RequestInformation:
        """
        Add a tenant to a multitenant organization. The administrator of an owner tenant has the permissions to add tenants to the multitenant organization. The added tenant is in the pending state until the administrator of the added tenant joins the multitenant organization by submitting a join request. A tenant can be part of only one multitenant organization.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.POST
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> TenantsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: TenantsRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return TenantsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def count(self) -> CountRequestBuilder:
        """
        Provides operations to count the resources in the collection.
        """
        from .count.count_request_builder import CountRequestBuilder

        return CountRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class TenantsRequestBuilderGetQueryParameters():
        """
        List the tenants and their properties in the multi-tenant organization.
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
                raise TypeError("original_name cannot be null.")
            if original_name == "count":
                return "%24count"
            if original_name == "expand":
                return "%24expand"
            if original_name == "filter":
                return "%24filter"
            if original_name == "orderby":
                return "%24orderby"
            if original_name == "search":
                return "%24search"
            if original_name == "select":
                return "%24select"
            if original_name == "skip":
                return "%24skip"
            if original_name == "top":
                return "%24top"
            return original_name
        
        # Include count of items
        count: Optional[bool] = None

        # Expand related entities
        expand: Optional[List[str]] = None

        # Filter items by property values
        filter: Optional[str] = None

        # Order items by property values
        orderby: Optional[List[str]] = None

        # Search items by search phrases
        search: Optional[str] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

        # Skip the first n items
        skip: Optional[int] = None

        # Show only the first n items
        top: Optional[int] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class TenantsRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[TenantsRequestBuilder.TenantsRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class TenantsRequestBuilderPostRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

