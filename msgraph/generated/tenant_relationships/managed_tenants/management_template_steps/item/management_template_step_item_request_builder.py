from __future__ import annotations
from dataclasses import dataclass
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....models.managed_tenants import management_template_step
    from .....models.o_data_errors import o_data_error
    from .accepted_version import accepted_version_request_builder
    from .management_template import management_template_request_builder
    from .versions import versions_request_builder
    from .versions.item import management_template_step_version_item_request_builder

class ManagementTemplateStepItemRequestBuilder():
    """
    Provides operations to manage the managementTemplateSteps property of the microsoft.graph.managedTenants.managedTenant entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new ManagementTemplateStepItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/tenantRelationships/managedTenants/managementTemplateSteps/{managementTemplateStep%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[ManagementTemplateStepItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property managementTemplateSteps for tenantRelationships
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[ManagementTemplateStepItemRequestBuilderGetRequestConfiguration] = None) -> Optional[management_template_step.ManagementTemplateStep]:
        """
        Get managementTemplateSteps from tenantRelationships
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[management_template_step.ManagementTemplateStep]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.managed_tenants import management_template_step

        return await self.request_adapter.send_async(request_info, management_template_step.ManagementTemplateStep, error_mapping)
    
    async def patch(self,body: Optional[management_template_step.ManagementTemplateStep] = None, request_configuration: Optional[ManagementTemplateStepItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[management_template_step.ManagementTemplateStep]:
        """
        Update the navigation property managementTemplateSteps in tenantRelationships
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[management_template_step.ManagementTemplateStep]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from .....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.managed_tenants import management_template_step

        return await self.request_adapter.send_async(request_info, management_template_step.ManagementTemplateStep, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[ManagementTemplateStepItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property managementTemplateSteps for tenantRelationships
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
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
    
    def to_get_request_information(self,request_configuration: Optional[ManagementTemplateStepItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get managementTemplateSteps from tenantRelationships
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
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
    
    def to_patch_request_information(self,body: Optional[management_template_step.ManagementTemplateStep] = None, request_configuration: Optional[ManagementTemplateStepItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property managementTemplateSteps in tenantRelationships
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.PATCH
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def versions_by_id(self,id: str) -> management_template_step_version_item_request_builder.ManagementTemplateStepVersionItemRequestBuilder:
        """
        Provides operations to manage the versions property of the microsoft.graph.managedTenants.managementTemplateStep entity.
        Args:
            id: Unique identifier of the item
        Returns: management_template_step_version_item_request_builder.ManagementTemplateStepVersionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .versions.item import management_template_step_version_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["managementTemplateStepVersion%2Did"] = id
        return management_template_step_version_item_request_builder.ManagementTemplateStepVersionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @property
    def accepted_version(self) -> accepted_version_request_builder.AcceptedVersionRequestBuilder:
        """
        Provides operations to manage the acceptedVersion property of the microsoft.graph.managedTenants.managementTemplateStep entity.
        """
        from .accepted_version import accepted_version_request_builder

        return accepted_version_request_builder.AcceptedVersionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def management_template(self) -> management_template_request_builder.ManagementTemplateRequestBuilder:
        """
        Provides operations to manage the managementTemplate property of the microsoft.graph.managedTenants.managementTemplateStep entity.
        """
        from .management_template import management_template_request_builder

        return management_template_request_builder.ManagementTemplateRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def versions(self) -> versions_request_builder.VersionsRequestBuilder:
        """
        Provides operations to manage the versions property of the microsoft.graph.managedTenants.managementTemplateStep entity.
        """
        from .versions import versions_request_builder

        return versions_request_builder.VersionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class ManagementTemplateStepItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class ManagementTemplateStepItemRequestBuilderGetQueryParameters():
        """
        Get managementTemplateSteps from tenantRelationships
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            Args:
                originalName: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise Exception("original_name cannot be undefined")
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
    class ManagementTemplateStepItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[ManagementTemplateStepItemRequestBuilder.ManagementTemplateStepItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class ManagementTemplateStepItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

