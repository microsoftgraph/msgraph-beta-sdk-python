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
    from .......models.custom_callout_extension import CustomCalloutExtension
    from .......models.o_data_errors.o_data_error import ODataError

class CustomCalloutExtensionItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the accessPackageCustomWorkflowExtensions property of the microsoft.graph.accessPackageCatalog entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new CustomCalloutExtensionItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/identityGovernance/entitlementManagement/accessPackageCatalogs/{accessPackageCatalog%2Did}/accessPackageCustomWorkflowExtensions/{customCalloutExtension%2Did}{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete navigation property accessPackageCustomWorkflowExtensions for identityGovernance
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        warn(" as of 2022-10/PrivatePreview:MicrosofEntitlementManagementCustomextensions on 2023-03-01 and will be removed 2023-12-31", DeprecationWarning)
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
    
    async def get(self,request_configuration: Optional[RequestConfiguration[CustomCalloutExtensionItemRequestBuilderGetQueryParameters]] = None) -> Optional[CustomCalloutExtension]:
        """
        Read the properties and relationships of an accessPackageAssignmentRequestWorkflowExtension object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CustomCalloutExtension]
        Find more info here: https://learn.microsoft.com/graph/api/accesspackageassignmentrequestworkflowextension-get?view=graph-rest-beta
        """
        warn(" as of 2022-10/PrivatePreview:MicrosofEntitlementManagementCustomextensions on 2023-03-01 and will be removed 2023-12-31", DeprecationWarning)
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .......models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .......models.custom_callout_extension import CustomCalloutExtension

        return await self.request_adapter.send_async(request_info, CustomCalloutExtension, error_mapping)
    
    async def patch(self,body: CustomCalloutExtension, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[CustomCalloutExtension]:
        """
        Update the properties of an accessPackageAssignmentWorkflowExtension object.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CustomCalloutExtension]
        Find more info here: https://learn.microsoft.com/graph/api/accesspackageassignmentworkflowextension-update?view=graph-rest-beta
        """
        warn(" as of 2022-10/PrivatePreview:MicrosofEntitlementManagementCustomextensions on 2023-03-01 and will be removed 2023-12-31", DeprecationWarning)
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
        from .......models.custom_callout_extension import CustomCalloutExtension

        return await self.request_adapter.send_async(request_info, CustomCalloutExtension, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete navigation property accessPackageCustomWorkflowExtensions for identityGovernance
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        warn(" as of 2022-10/PrivatePreview:MicrosofEntitlementManagementCustomextensions on 2023-03-01 and will be removed 2023-12-31", DeprecationWarning)
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[CustomCalloutExtensionItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Read the properties and relationships of an accessPackageAssignmentRequestWorkflowExtension object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        warn(" as of 2022-10/PrivatePreview:MicrosofEntitlementManagementCustomextensions on 2023-03-01 and will be removed 2023-12-31", DeprecationWarning)
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: CustomCalloutExtension, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the properties of an accessPackageAssignmentWorkflowExtension object.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        warn(" as of 2022-10/PrivatePreview:MicrosofEntitlementManagementCustomextensions on 2023-03-01 and will be removed 2023-12-31", DeprecationWarning)
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PATCH, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> CustomCalloutExtensionItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: CustomCalloutExtensionItemRequestBuilder
        """
        warn(" as of 2022-10/PrivatePreview:MicrosofEntitlementManagementCustomextensions on 2023-03-01 and will be removed 2023-12-31", DeprecationWarning)
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return CustomCalloutExtensionItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class CustomCalloutExtensionItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class CustomCalloutExtensionItemRequestBuilderGetQueryParameters():
        """
        Read the properties and relationships of an accessPackageAssignmentRequestWorkflowExtension object.
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
    class CustomCalloutExtensionItemRequestBuilderGetRequestConfiguration(RequestConfiguration[CustomCalloutExtensionItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class CustomCalloutExtensionItemRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

