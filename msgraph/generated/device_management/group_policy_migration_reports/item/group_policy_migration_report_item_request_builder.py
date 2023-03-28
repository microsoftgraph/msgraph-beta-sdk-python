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
    from ....models import group_policy_migration_report
    from ....models.o_data_errors import o_data_error
    from .group_policy_setting_mappings import group_policy_setting_mappings_request_builder
    from .group_policy_setting_mappings.item import group_policy_setting_mapping_item_request_builder
    from .unsupported_group_policy_extensions import unsupported_group_policy_extensions_request_builder
    from .unsupported_group_policy_extensions.item import unsupported_group_policy_extension_item_request_builder
    from .update_scope_tags import update_scope_tags_request_builder

class GroupPolicyMigrationReportItemRequestBuilder():
    """
    Provides operations to manage the groupPolicyMigrationReports property of the microsoft.graph.deviceManagement entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new GroupPolicyMigrationReportItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/deviceManagement/groupPolicyMigrationReports/{groupPolicyMigrationReport%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[GroupPolicyMigrationReportItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property groupPolicyMigrationReports for deviceManagement
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[GroupPolicyMigrationReportItemRequestBuilderGetRequestConfiguration] = None) -> Optional[group_policy_migration_report.GroupPolicyMigrationReport]:
        """
        A list of Group Policy migration reports.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[group_policy_migration_report.GroupPolicyMigrationReport]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models import group_policy_migration_report

        return await self.request_adapter.send_async(request_info, group_policy_migration_report.GroupPolicyMigrationReport, error_mapping)
    
    def group_policy_setting_mappings_by_id(self,id: str) -> group_policy_setting_mapping_item_request_builder.GroupPolicySettingMappingItemRequestBuilder:
        """
        Provides operations to manage the groupPolicySettingMappings property of the microsoft.graph.groupPolicyMigrationReport entity.
        Args:
            id: Unique identifier of the item
        Returns: group_policy_setting_mapping_item_request_builder.GroupPolicySettingMappingItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .group_policy_setting_mappings.item import group_policy_setting_mapping_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["groupPolicySettingMapping%2Did"] = id
        return group_policy_setting_mapping_item_request_builder.GroupPolicySettingMappingItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def patch(self,body: Optional[group_policy_migration_report.GroupPolicyMigrationReport] = None, request_configuration: Optional[GroupPolicyMigrationReportItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[group_policy_migration_report.GroupPolicyMigrationReport]:
        """
        Update the navigation property groupPolicyMigrationReports in deviceManagement
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[group_policy_migration_report.GroupPolicyMigrationReport]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models import group_policy_migration_report

        return await self.request_adapter.send_async(request_info, group_policy_migration_report.GroupPolicyMigrationReport, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[GroupPolicyMigrationReportItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property groupPolicyMigrationReports for deviceManagement
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
    
    def to_get_request_information(self,request_configuration: Optional[GroupPolicyMigrationReportItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        A list of Group Policy migration reports.
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
    
    def to_patch_request_information(self,body: Optional[group_policy_migration_report.GroupPolicyMigrationReport] = None, request_configuration: Optional[GroupPolicyMigrationReportItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property groupPolicyMigrationReports in deviceManagement
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
    
    def unsupported_group_policy_extensions_by_id(self,id: str) -> unsupported_group_policy_extension_item_request_builder.UnsupportedGroupPolicyExtensionItemRequestBuilder:
        """
        Provides operations to manage the unsupportedGroupPolicyExtensions property of the microsoft.graph.groupPolicyMigrationReport entity.
        Args:
            id: Unique identifier of the item
        Returns: unsupported_group_policy_extension_item_request_builder.UnsupportedGroupPolicyExtensionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .unsupported_group_policy_extensions.item import unsupported_group_policy_extension_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["unsupportedGroupPolicyExtension%2Did"] = id
        return unsupported_group_policy_extension_item_request_builder.UnsupportedGroupPolicyExtensionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @property
    def group_policy_setting_mappings(self) -> group_policy_setting_mappings_request_builder.GroupPolicySettingMappingsRequestBuilder:
        """
        Provides operations to manage the groupPolicySettingMappings property of the microsoft.graph.groupPolicyMigrationReport entity.
        """
        from .group_policy_setting_mappings import group_policy_setting_mappings_request_builder

        return group_policy_setting_mappings_request_builder.GroupPolicySettingMappingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def unsupported_group_policy_extensions(self) -> unsupported_group_policy_extensions_request_builder.UnsupportedGroupPolicyExtensionsRequestBuilder:
        """
        Provides operations to manage the unsupportedGroupPolicyExtensions property of the microsoft.graph.groupPolicyMigrationReport entity.
        """
        from .unsupported_group_policy_extensions import unsupported_group_policy_extensions_request_builder

        return unsupported_group_policy_extensions_request_builder.UnsupportedGroupPolicyExtensionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def update_scope_tags(self) -> update_scope_tags_request_builder.UpdateScopeTagsRequestBuilder:
        """
        Provides operations to call the updateScopeTags method.
        """
        from .update_scope_tags import update_scope_tags_request_builder

        return update_scope_tags_request_builder.UpdateScopeTagsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class GroupPolicyMigrationReportItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class GroupPolicyMigrationReportItemRequestBuilderGetQueryParameters():
        """
        A list of Group Policy migration reports.
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
    class GroupPolicyMigrationReportItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[GroupPolicyMigrationReportItemRequestBuilder.GroupPolicyMigrationReportItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class GroupPolicyMigrationReportItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

