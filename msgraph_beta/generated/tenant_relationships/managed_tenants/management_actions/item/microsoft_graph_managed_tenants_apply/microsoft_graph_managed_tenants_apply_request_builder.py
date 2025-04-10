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
    from ......models.managed_tenants.management_action_deployment_status import ManagementActionDeploymentStatus
    from ......models.o_data_errors.o_data_error import ODataError
    from .apply_post_request_body import ApplyPostRequestBody

class MicrosoftGraphManagedTenantsApplyRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to call the apply method.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new MicrosoftGraphManagedTenantsApplyRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/tenantRelationships/managedTenants/managementActions/{managementAction%2Did}/microsoft.graph.managedTenants.apply", path_parameters)
    
    async def post(self,body: ApplyPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[ManagementActionDeploymentStatus]:
        """
        Applies a management action against a specific managed tenant. Performing this operation makes the appropriate configurations and creates the appropriate policies. For example, when applying the required multifactor authentication for admins, management action creates a Microsoft Entra Conditional Access policy that requires multifactor authentication for all users that are assigned an administrative directory role.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ManagementActionDeploymentStatus]
        Find more info here: https://learn.microsoft.com/graph/api/managedtenants-managementaction-apply?view=graph-rest-beta
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.managed_tenants.management_action_deployment_status import ManagementActionDeploymentStatus

        return await self.request_adapter.send_async(request_info, ManagementActionDeploymentStatus, error_mapping)
    
    def to_post_request_information(self,body: ApplyPostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Applies a management action against a specific managed tenant. Performing this operation makes the appropriate configurations and creates the appropriate policies. For example, when applying the required multifactor authentication for admins, management action creates a Microsoft Entra Conditional Access policy that requires multifactor authentication for all users that are assigned an administrative directory role.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.POST, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> MicrosoftGraphManagedTenantsApplyRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: MicrosoftGraphManagedTenantsApplyRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return MicrosoftGraphManagedTenantsApplyRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class MicrosoftGraphManagedTenantsApplyRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

