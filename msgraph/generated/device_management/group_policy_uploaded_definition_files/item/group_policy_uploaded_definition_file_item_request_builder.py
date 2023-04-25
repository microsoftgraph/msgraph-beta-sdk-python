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
    from ....models import group_policy_uploaded_definition_file
    from ....models.o_data_errors import o_data_error
    from .add_language_files import add_language_files_request_builder
    from .group_policy_operations import group_policy_operations_request_builder
    from .remove import remove_request_builder
    from .remove_language_files import remove_language_files_request_builder
    from .update_language_files import update_language_files_request_builder
    from .upload_new_version import upload_new_version_request_builder

class GroupPolicyUploadedDefinitionFileItemRequestBuilder():
    """
    Provides operations to manage the groupPolicyUploadedDefinitionFiles property of the microsoft.graph.deviceManagement entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new GroupPolicyUploadedDefinitionFileItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/deviceManagement/groupPolicyUploadedDefinitionFiles/{groupPolicyUploadedDefinitionFile%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[GroupPolicyUploadedDefinitionFileItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property groupPolicyUploadedDefinitionFiles for deviceManagement
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
    
    async def get(self,request_configuration: Optional[GroupPolicyUploadedDefinitionFileItemRequestBuilderGetRequestConfiguration] = None) -> Optional[group_policy_uploaded_definition_file.GroupPolicyUploadedDefinitionFile]:
        """
        The available group policy uploaded definition files for this account.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[group_policy_uploaded_definition_file.GroupPolicyUploadedDefinitionFile]
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
        from ....models import group_policy_uploaded_definition_file

        return await self.request_adapter.send_async(request_info, group_policy_uploaded_definition_file.GroupPolicyUploadedDefinitionFile, error_mapping)
    
    async def patch(self,body: Optional[group_policy_uploaded_definition_file.GroupPolicyUploadedDefinitionFile] = None, request_configuration: Optional[GroupPolicyUploadedDefinitionFileItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[group_policy_uploaded_definition_file.GroupPolicyUploadedDefinitionFile]:
        """
        Update the navigation property groupPolicyUploadedDefinitionFiles in deviceManagement
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[group_policy_uploaded_definition_file.GroupPolicyUploadedDefinitionFile]
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
        from ....models import group_policy_uploaded_definition_file

        return await self.request_adapter.send_async(request_info, group_policy_uploaded_definition_file.GroupPolicyUploadedDefinitionFile, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[GroupPolicyUploadedDefinitionFileItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property groupPolicyUploadedDefinitionFiles for deviceManagement
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
    
    def to_get_request_information(self,request_configuration: Optional[GroupPolicyUploadedDefinitionFileItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        The available group policy uploaded definition files for this account.
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
    
    def to_patch_request_information(self,body: Optional[group_policy_uploaded_definition_file.GroupPolicyUploadedDefinitionFile] = None, request_configuration: Optional[GroupPolicyUploadedDefinitionFileItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property groupPolicyUploadedDefinitionFiles in deviceManagement
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
    def add_language_files(self) -> add_language_files_request_builder.AddLanguageFilesRequestBuilder:
        """
        Provides operations to call the addLanguageFiles method.
        """
        from .add_language_files import add_language_files_request_builder

        return add_language_files_request_builder.AddLanguageFilesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def group_policy_operations(self) -> group_policy_operations_request_builder.GroupPolicyOperationsRequestBuilder:
        """
        Provides operations to manage the groupPolicyOperations property of the microsoft.graph.groupPolicyUploadedDefinitionFile entity.
        """
        from .group_policy_operations import group_policy_operations_request_builder

        return group_policy_operations_request_builder.GroupPolicyOperationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def remove(self) -> remove_request_builder.RemoveRequestBuilder:
        """
        Provides operations to call the remove method.
        """
        from .remove import remove_request_builder

        return remove_request_builder.RemoveRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def remove_language_files(self) -> remove_language_files_request_builder.RemoveLanguageFilesRequestBuilder:
        """
        Provides operations to call the removeLanguageFiles method.
        """
        from .remove_language_files import remove_language_files_request_builder

        return remove_language_files_request_builder.RemoveLanguageFilesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def update_language_files(self) -> update_language_files_request_builder.UpdateLanguageFilesRequestBuilder:
        """
        Provides operations to call the updateLanguageFiles method.
        """
        from .update_language_files import update_language_files_request_builder

        return update_language_files_request_builder.UpdateLanguageFilesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def upload_new_version(self) -> upload_new_version_request_builder.UploadNewVersionRequestBuilder:
        """
        Provides operations to call the uploadNewVersion method.
        """
        from .upload_new_version import upload_new_version_request_builder

        return upload_new_version_request_builder.UploadNewVersionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class GroupPolicyUploadedDefinitionFileItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class GroupPolicyUploadedDefinitionFileItemRequestBuilderGetQueryParameters():
        """
        The available group policy uploaded definition files for this account.
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
    class GroupPolicyUploadedDefinitionFileItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[GroupPolicyUploadedDefinitionFileItemRequestBuilder.GroupPolicyUploadedDefinitionFileItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class GroupPolicyUploadedDefinitionFileItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

