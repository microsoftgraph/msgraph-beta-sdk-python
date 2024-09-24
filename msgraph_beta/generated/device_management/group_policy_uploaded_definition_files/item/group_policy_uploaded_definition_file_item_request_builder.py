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
    from ....models.group_policy_uploaded_definition_file import GroupPolicyUploadedDefinitionFile
    from ....models.o_data_errors.o_data_error import ODataError
    from .add_language_files.add_language_files_request_builder import AddLanguageFilesRequestBuilder
    from .definitions.definitions_request_builder import DefinitionsRequestBuilder
    from .group_policy_operations.group_policy_operations_request_builder import GroupPolicyOperationsRequestBuilder
    from .remove.remove_request_builder import RemoveRequestBuilder
    from .remove_language_files.remove_language_files_request_builder import RemoveLanguageFilesRequestBuilder
    from .update_language_files.update_language_files_request_builder import UpdateLanguageFilesRequestBuilder
    from .upload_new_version.upload_new_version_request_builder import UploadNewVersionRequestBuilder

class GroupPolicyUploadedDefinitionFileItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the groupPolicyUploadedDefinitionFiles property of the microsoft.graph.deviceManagement entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new GroupPolicyUploadedDefinitionFileItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/deviceManagement/groupPolicyUploadedDefinitionFiles/{groupPolicyUploadedDefinitionFile%2Did}{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete navigation property groupPolicyUploadedDefinitionFiles for deviceManagement
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
    
    async def get(self,request_configuration: Optional[RequestConfiguration[GroupPolicyUploadedDefinitionFileItemRequestBuilderGetQueryParameters]] = None) -> Optional[GroupPolicyUploadedDefinitionFile]:
        """
        The available group policy uploaded definition files for this account.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[GroupPolicyUploadedDefinitionFile]
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
        from ....models.group_policy_uploaded_definition_file import GroupPolicyUploadedDefinitionFile

        return await self.request_adapter.send_async(request_info, GroupPolicyUploadedDefinitionFile, error_mapping)
    
    async def patch(self,body: GroupPolicyUploadedDefinitionFile, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[GroupPolicyUploadedDefinitionFile]:
        """
        Update the navigation property groupPolicyUploadedDefinitionFiles in deviceManagement
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[GroupPolicyUploadedDefinitionFile]
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
        from ....models.group_policy_uploaded_definition_file import GroupPolicyUploadedDefinitionFile

        return await self.request_adapter.send_async(request_info, GroupPolicyUploadedDefinitionFile, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete navigation property groupPolicyUploadedDefinitionFiles for deviceManagement
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[GroupPolicyUploadedDefinitionFileItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        The available group policy uploaded definition files for this account.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: GroupPolicyUploadedDefinitionFile, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the navigation property groupPolicyUploadedDefinitionFiles in deviceManagement
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
    
    def with_url(self,raw_url: str) -> GroupPolicyUploadedDefinitionFileItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: GroupPolicyUploadedDefinitionFileItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return GroupPolicyUploadedDefinitionFileItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def add_language_files(self) -> AddLanguageFilesRequestBuilder:
        """
        Provides operations to call the addLanguageFiles method.
        """
        from .add_language_files.add_language_files_request_builder import AddLanguageFilesRequestBuilder

        return AddLanguageFilesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def definitions(self) -> DefinitionsRequestBuilder:
        """
        Provides operations to manage the definitions property of the microsoft.graph.groupPolicyDefinitionFile entity.
        """
        from .definitions.definitions_request_builder import DefinitionsRequestBuilder

        return DefinitionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def group_policy_operations(self) -> GroupPolicyOperationsRequestBuilder:
        """
        Provides operations to manage the groupPolicyOperations property of the microsoft.graph.groupPolicyUploadedDefinitionFile entity.
        """
        from .group_policy_operations.group_policy_operations_request_builder import GroupPolicyOperationsRequestBuilder

        return GroupPolicyOperationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def remove(self) -> RemoveRequestBuilder:
        """
        Provides operations to call the remove method.
        """
        from .remove.remove_request_builder import RemoveRequestBuilder

        return RemoveRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def remove_language_files(self) -> RemoveLanguageFilesRequestBuilder:
        """
        Provides operations to call the removeLanguageFiles method.
        """
        from .remove_language_files.remove_language_files_request_builder import RemoveLanguageFilesRequestBuilder

        return RemoveLanguageFilesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def update_language_files(self) -> UpdateLanguageFilesRequestBuilder:
        """
        Provides operations to call the updateLanguageFiles method.
        """
        from .update_language_files.update_language_files_request_builder import UpdateLanguageFilesRequestBuilder

        return UpdateLanguageFilesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def upload_new_version(self) -> UploadNewVersionRequestBuilder:
        """
        Provides operations to call the uploadNewVersion method.
        """
        from .upload_new_version.upload_new_version_request_builder import UploadNewVersionRequestBuilder

        return UploadNewVersionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class GroupPolicyUploadedDefinitionFileItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class GroupPolicyUploadedDefinitionFileItemRequestBuilderGetQueryParameters():
        """
        The available group policy uploaded definition files for this account.
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
    class GroupPolicyUploadedDefinitionFileItemRequestBuilderGetRequestConfiguration(RequestConfiguration[GroupPolicyUploadedDefinitionFileItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class GroupPolicyUploadedDefinitionFileItemRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

