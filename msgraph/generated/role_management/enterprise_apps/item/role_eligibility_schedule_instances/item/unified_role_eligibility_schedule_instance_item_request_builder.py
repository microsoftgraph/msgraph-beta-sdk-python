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
    from ......models import unified_role_eligibility_schedule_instance
    from ......models.o_data_errors import o_data_error
    from .app_scope import app_scope_request_builder
    from .directory_scope import directory_scope_request_builder
    from .principal import principal_request_builder
    from .role_definition import role_definition_request_builder

class UnifiedRoleEligibilityScheduleInstanceItemRequestBuilder():
    """
    Provides operations to manage the roleEligibilityScheduleInstances property of the microsoft.graph.rbacApplication entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new UnifiedRoleEligibilityScheduleInstanceItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/roleManagement/enterpriseApps/{rbacApplication%2Did}/roleEligibilityScheduleInstances/{unifiedRoleEligibilityScheduleInstance%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[UnifiedRoleEligibilityScheduleInstanceItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property roleEligibilityScheduleInstances for roleManagement
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ......models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[UnifiedRoleEligibilityScheduleInstanceItemRequestBuilderGetRequestConfiguration] = None) -> Optional[unified_role_eligibility_schedule_instance.UnifiedRoleEligibilityScheduleInstance]:
        """
        Get roleEligibilityScheduleInstances from roleManagement
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[unified_role_eligibility_schedule_instance.UnifiedRoleEligibilityScheduleInstance]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ......models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models import unified_role_eligibility_schedule_instance

        return await self.request_adapter.send_async(request_info, unified_role_eligibility_schedule_instance.UnifiedRoleEligibilityScheduleInstance, error_mapping)
    
    async def patch(self,body: Optional[unified_role_eligibility_schedule_instance.UnifiedRoleEligibilityScheduleInstance] = None, request_configuration: Optional[UnifiedRoleEligibilityScheduleInstanceItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[unified_role_eligibility_schedule_instance.UnifiedRoleEligibilityScheduleInstance]:
        """
        Update the navigation property roleEligibilityScheduleInstances in roleManagement
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[unified_role_eligibility_schedule_instance.UnifiedRoleEligibilityScheduleInstance]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ......models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models import unified_role_eligibility_schedule_instance

        return await self.request_adapter.send_async(request_info, unified_role_eligibility_schedule_instance.UnifiedRoleEligibilityScheduleInstance, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[UnifiedRoleEligibilityScheduleInstanceItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property roleEligibilityScheduleInstances for roleManagement
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
    
    def to_get_request_information(self,request_configuration: Optional[UnifiedRoleEligibilityScheduleInstanceItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get roleEligibilityScheduleInstances from roleManagement
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
    
    def to_patch_request_information(self,body: Optional[unified_role_eligibility_schedule_instance.UnifiedRoleEligibilityScheduleInstance] = None, request_configuration: Optional[UnifiedRoleEligibilityScheduleInstanceItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property roleEligibilityScheduleInstances in roleManagement
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
    
    @property
    def app_scope(self) -> app_scope_request_builder.AppScopeRequestBuilder:
        """
        Provides operations to manage the appScope property of the microsoft.graph.unifiedRoleScheduleInstanceBase entity.
        """
        from .app_scope import app_scope_request_builder

        return app_scope_request_builder.AppScopeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def directory_scope(self) -> directory_scope_request_builder.DirectoryScopeRequestBuilder:
        """
        Provides operations to manage the directoryScope property of the microsoft.graph.unifiedRoleScheduleInstanceBase entity.
        """
        from .directory_scope import directory_scope_request_builder

        return directory_scope_request_builder.DirectoryScopeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def principal(self) -> principal_request_builder.PrincipalRequestBuilder:
        """
        Provides operations to manage the principal property of the microsoft.graph.unifiedRoleScheduleInstanceBase entity.
        """
        from .principal import principal_request_builder

        return principal_request_builder.PrincipalRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def role_definition(self) -> role_definition_request_builder.RoleDefinitionRequestBuilder:
        """
        Provides operations to manage the roleDefinition property of the microsoft.graph.unifiedRoleScheduleInstanceBase entity.
        """
        from .role_definition import role_definition_request_builder

        return role_definition_request_builder.RoleDefinitionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class UnifiedRoleEligibilityScheduleInstanceItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class UnifiedRoleEligibilityScheduleInstanceItemRequestBuilderGetQueryParameters():
        """
        Get roleEligibilityScheduleInstances from roleManagement
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
    class UnifiedRoleEligibilityScheduleInstanceItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[UnifiedRoleEligibilityScheduleInstanceItemRequestBuilder.UnifiedRoleEligibilityScheduleInstanceItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class UnifiedRoleEligibilityScheduleInstanceItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
