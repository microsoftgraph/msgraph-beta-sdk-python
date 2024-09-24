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
    from ....models.group_policy_migration_report import GroupPolicyMigrationReport
    from ....models.o_data_errors.o_data_error import ODataError
    from .group_policy_setting_mappings.group_policy_setting_mappings_request_builder import GroupPolicySettingMappingsRequestBuilder
    from .unsupported_group_policy_extensions.unsupported_group_policy_extensions_request_builder import UnsupportedGroupPolicyExtensionsRequestBuilder
    from .update_scope_tags.update_scope_tags_request_builder import UpdateScopeTagsRequestBuilder

class GroupPolicyMigrationReportItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the groupPolicyMigrationReports property of the microsoft.graph.deviceManagement entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new GroupPolicyMigrationReportItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/deviceManagement/groupPolicyMigrationReports/{groupPolicyMigrationReport%2Did}{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete navigation property groupPolicyMigrationReports for deviceManagement
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[GroupPolicyMigrationReportItemRequestBuilderGetQueryParameters]] = None) -> Optional[GroupPolicyMigrationReport]:
        """
        A list of Group Policy migration reports.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[GroupPolicyMigrationReport]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.group_policy_migration_report import GroupPolicyMigrationReport

        return await self.request_adapter.send_async(request_info, GroupPolicyMigrationReport, error_mapping)
    
    async def patch(self,body: GroupPolicyMigrationReport, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[GroupPolicyMigrationReport]:
        """
        Update the navigation property groupPolicyMigrationReports in deviceManagement
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[GroupPolicyMigrationReport]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.group_policy_migration_report import GroupPolicyMigrationReport

        return await self.request_adapter.send_async(request_info, GroupPolicyMigrationReport, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete navigation property groupPolicyMigrationReports for deviceManagement
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[GroupPolicyMigrationReportItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        A list of Group Policy migration reports.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: GroupPolicyMigrationReport, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the navigation property groupPolicyMigrationReports in deviceManagement
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
    
    def with_url(self,raw_url: str) -> GroupPolicyMigrationReportItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: GroupPolicyMigrationReportItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return GroupPolicyMigrationReportItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def group_policy_setting_mappings(self) -> GroupPolicySettingMappingsRequestBuilder:
        """
        Provides operations to manage the groupPolicySettingMappings property of the microsoft.graph.groupPolicyMigrationReport entity.
        """
        from .group_policy_setting_mappings.group_policy_setting_mappings_request_builder import GroupPolicySettingMappingsRequestBuilder

        return GroupPolicySettingMappingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def unsupported_group_policy_extensions(self) -> UnsupportedGroupPolicyExtensionsRequestBuilder:
        """
        Provides operations to manage the unsupportedGroupPolicyExtensions property of the microsoft.graph.groupPolicyMigrationReport entity.
        """
        from .unsupported_group_policy_extensions.unsupported_group_policy_extensions_request_builder import UnsupportedGroupPolicyExtensionsRequestBuilder

        return UnsupportedGroupPolicyExtensionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def update_scope_tags(self) -> UpdateScopeTagsRequestBuilder:
        """
        Provides operations to call the updateScopeTags method.
        """
        from .update_scope_tags.update_scope_tags_request_builder import UpdateScopeTagsRequestBuilder

        return UpdateScopeTagsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class GroupPolicyMigrationReportItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class GroupPolicyMigrationReportItemRequestBuilderGetQueryParameters():
        """
        A list of Group Policy migration reports.
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
    class GroupPolicyMigrationReportItemRequestBuilderGetRequestConfiguration(RequestConfiguration[GroupPolicyMigrationReportItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class GroupPolicyMigrationReportItemRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

