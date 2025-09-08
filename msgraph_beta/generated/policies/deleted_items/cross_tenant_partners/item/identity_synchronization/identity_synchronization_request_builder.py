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
    from ......models.cross_tenant_identity_sync_policy_partner import CrossTenantIdentitySyncPolicyPartner
    from ......models.o_data_errors.o_data_error import ODataError
    from .restore.restore_request_builder import RestoreRequestBuilder

class IdentitySynchronizationRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the identitySynchronization property of the microsoft.graph.crossTenantAccessPolicyConfigurationPartner entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new IdentitySynchronizationRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/policies/deletedItems/crossTenantPartners/{crossTenantAccessPolicyConfigurationPartner%2DtenantId}/identitySynchronization{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete navigation property identitySynchronization for policies
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[IdentitySynchronizationRequestBuilderGetQueryParameters]] = None) -> Optional[CrossTenantIdentitySyncPolicyPartner]:
        """
        Defines the cross-tenant policy for the synchronization of users from a partner tenant. Use this user synchronization policy to streamline collaboration between users in a multitenant organization by automating the creation, update, and deletion of users from one tenant to another.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CrossTenantIdentitySyncPolicyPartner]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.cross_tenant_identity_sync_policy_partner import CrossTenantIdentitySyncPolicyPartner

        return await self.request_adapter.send_async(request_info, CrossTenantIdentitySyncPolicyPartner, error_mapping)
    
    async def put(self,body: CrossTenantIdentitySyncPolicyPartner, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[CrossTenantIdentitySyncPolicyPartner]:
        """
        Update the navigation property identitySynchronization in policies
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CrossTenantIdentitySyncPolicyPartner]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.cross_tenant_identity_sync_policy_partner import CrossTenantIdentitySyncPolicyPartner

        return await self.request_adapter.send_async(request_info, CrossTenantIdentitySyncPolicyPartner, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete navigation property identitySynchronization for policies
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[IdentitySynchronizationRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Defines the cross-tenant policy for the synchronization of users from a partner tenant. Use this user synchronization policy to streamline collaboration between users in a multitenant organization by automating the creation, update, and deletion of users from one tenant to another.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_put_request_information(self,body: CrossTenantIdentitySyncPolicyPartner, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the navigation property identitySynchronization in policies
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PUT, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> IdentitySynchronizationRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: IdentitySynchronizationRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return IdentitySynchronizationRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def restore(self) -> RestoreRequestBuilder:
        """
        Provides operations to call the restore method.
        """
        from .restore.restore_request_builder import RestoreRequestBuilder

        return RestoreRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class IdentitySynchronizationRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class IdentitySynchronizationRequestBuilderGetQueryParameters():
        """
        Defines the cross-tenant policy for the synchronization of users from a partner tenant. Use this user synchronization policy to streamline collaboration between users in a multitenant organization by automating the creation, update, and deletion of users from one tenant to another.
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
    class IdentitySynchronizationRequestBuilderGetRequestConfiguration(RequestConfiguration[IdentitySynchronizationRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class IdentitySynchronizationRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

