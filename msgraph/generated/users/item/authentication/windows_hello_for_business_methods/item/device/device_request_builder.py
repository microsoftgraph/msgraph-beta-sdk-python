from __future__ import annotations
from dataclasses import dataclass
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device = lazy_import('msgraph.generated.models.device')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')
check_member_groups_request_builder = lazy_import('msgraph.generated.users.item.authentication.windows_hello_for_business_methods.item.device.check_member_groups.check_member_groups_request_builder')
check_member_objects_request_builder = lazy_import('msgraph.generated.users.item.authentication.windows_hello_for_business_methods.item.device.check_member_objects.check_member_objects_request_builder')
commands_request_builder = lazy_import('msgraph.generated.users.item.authentication.windows_hello_for_business_methods.item.device.commands.commands_request_builder')
command_item_request_builder = lazy_import('msgraph.generated.users.item.authentication.windows_hello_for_business_methods.item.device.commands.item.command_item_request_builder')
extensions_request_builder = lazy_import('msgraph.generated.users.item.authentication.windows_hello_for_business_methods.item.device.extensions.extensions_request_builder')
extension_item_request_builder = lazy_import('msgraph.generated.users.item.authentication.windows_hello_for_business_methods.item.device.extensions.item.extension_item_request_builder')
get_member_groups_request_builder = lazy_import('msgraph.generated.users.item.authentication.windows_hello_for_business_methods.item.device.get_member_groups.get_member_groups_request_builder')
get_member_objects_request_builder = lazy_import('msgraph.generated.users.item.authentication.windows_hello_for_business_methods.item.device.get_member_objects.get_member_objects_request_builder')
member_of_request_builder = lazy_import('msgraph.generated.users.item.authentication.windows_hello_for_business_methods.item.device.member_of.member_of_request_builder')
directory_object_item_request_builder = lazy_import('msgraph.generated.users.item.authentication.windows_hello_for_business_methods.item.device.member_of.item.directory_object_item_request_builder')
registered_owners_request_builder = lazy_import('msgraph.generated.users.item.authentication.windows_hello_for_business_methods.item.device.registered_owners.registered_owners_request_builder')
directory_object_item_request_builder = lazy_import('msgraph.generated.users.item.authentication.windows_hello_for_business_methods.item.device.registered_owners.item.directory_object_item_request_builder')
registered_users_request_builder = lazy_import('msgraph.generated.users.item.authentication.windows_hello_for_business_methods.item.device.registered_users.registered_users_request_builder')
directory_object_item_request_builder = lazy_import('msgraph.generated.users.item.authentication.windows_hello_for_business_methods.item.device.registered_users.item.directory_object_item_request_builder')
restore_request_builder = lazy_import('msgraph.generated.users.item.authentication.windows_hello_for_business_methods.item.device.restore.restore_request_builder')
transitive_member_of_request_builder = lazy_import('msgraph.generated.users.item.authentication.windows_hello_for_business_methods.item.device.transitive_member_of.transitive_member_of_request_builder')
directory_object_item_request_builder = lazy_import('msgraph.generated.users.item.authentication.windows_hello_for_business_methods.item.device.transitive_member_of.item.directory_object_item_request_builder')
usage_rights_request_builder = lazy_import('msgraph.generated.users.item.authentication.windows_hello_for_business_methods.item.device.usage_rights.usage_rights_request_builder')
usage_right_item_request_builder = lazy_import('msgraph.generated.users.item.authentication.windows_hello_for_business_methods.item.device.usage_rights.item.usage_right_item_request_builder')

class DeviceRequestBuilder():
    """
    Provides operations to manage the device property of the microsoft.graph.windowsHelloForBusinessAuthenticationMethod entity.
    """
    def check_member_groups(self) -> check_member_groups_request_builder.CheckMemberGroupsRequestBuilder:
        """
        Provides operations to call the checkMemberGroups method.
        """
        return check_member_groups_request_builder.CheckMemberGroupsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def check_member_objects(self) -> check_member_objects_request_builder.CheckMemberObjectsRequestBuilder:
        """
        Provides operations to call the checkMemberObjects method.
        """
        return check_member_objects_request_builder.CheckMemberObjectsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def commands(self) -> commands_request_builder.CommandsRequestBuilder:
        """
        Provides operations to manage the commands property of the microsoft.graph.device entity.
        """
        return commands_request_builder.CommandsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def extensions(self) -> extensions_request_builder.ExtensionsRequestBuilder:
        """
        Provides operations to manage the extensions property of the microsoft.graph.device entity.
        """
        return extensions_request_builder.ExtensionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def get_member_groups(self) -> get_member_groups_request_builder.GetMemberGroupsRequestBuilder:
        """
        Provides operations to call the getMemberGroups method.
        """
        return get_member_groups_request_builder.GetMemberGroupsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def get_member_objects(self) -> get_member_objects_request_builder.GetMemberObjectsRequestBuilder:
        """
        Provides operations to call the getMemberObjects method.
        """
        return get_member_objects_request_builder.GetMemberObjectsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def member_of(self) -> member_of_request_builder.MemberOfRequestBuilder:
        """
        Provides operations to manage the memberOf property of the microsoft.graph.device entity.
        """
        return member_of_request_builder.MemberOfRequestBuilder(self.request_adapter, self.path_parameters)
    
    def registered_owners(self) -> registered_owners_request_builder.RegisteredOwnersRequestBuilder:
        """
        Provides operations to manage the registeredOwners property of the microsoft.graph.device entity.
        """
        return registered_owners_request_builder.RegisteredOwnersRequestBuilder(self.request_adapter, self.path_parameters)
    
    def registered_users(self) -> registered_users_request_builder.RegisteredUsersRequestBuilder:
        """
        Provides operations to manage the registeredUsers property of the microsoft.graph.device entity.
        """
        return registered_users_request_builder.RegisteredUsersRequestBuilder(self.request_adapter, self.path_parameters)
    
    def restore(self) -> restore_request_builder.RestoreRequestBuilder:
        """
        Provides operations to call the restore method.
        """
        return restore_request_builder.RestoreRequestBuilder(self.request_adapter, self.path_parameters)
    
    def transitive_member_of(self) -> transitive_member_of_request_builder.TransitiveMemberOfRequestBuilder:
        """
        Provides operations to manage the transitiveMemberOf property of the microsoft.graph.device entity.
        """
        return transitive_member_of_request_builder.TransitiveMemberOfRequestBuilder(self.request_adapter, self.path_parameters)
    
    def usage_rights(self) -> usage_rights_request_builder.UsageRightsRequestBuilder:
        """
        Provides operations to manage the usageRights property of the microsoft.graph.device entity.
        """
        return usage_rights_request_builder.UsageRightsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def commands_by_id(self,id: str) -> command_item_request_builder.CommandItemRequestBuilder:
        """
        Provides operations to manage the commands property of the microsoft.graph.device entity.
        Args:
            id: Unique identifier of the item
        Returns: command_item_request_builder.CommandItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["command%2Did"] = id
        return command_item_request_builder.CommandItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new DeviceRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/users/{user%2Did}/authentication/windowsHelloForBusinessMethods/{windowsHelloForBusinessAuthenticationMethod%2Did}/device{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def create_delete_request_information(self,request_configuration: Optional[DeviceRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property device for users
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
    
    def create_get_request_information(self,request_configuration: Optional[DeviceRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        The registered device on which this Windows Hello for Business key resides. Supports $expand. When you get a user's Windows Hello for Business registration information, this property is returned only on a single GET and when you specify ?$expand. For example, GET /users/admin@contoso.com/authentication/windowsHelloForBusinessMethods/_jpuR-TGZtk6aQCLF3BQjA2?$expand=device.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers["Accept"] = "application/json"
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def create_patch_request_information(self,body: Optional[device.Device] = None, request_configuration: Optional[DeviceRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property device in users
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
        request_info.headers["Accept"] = "application/json"
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    async def delete(self,request_configuration: Optional[DeviceRequestBuilderDeleteRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> None:
        """
        Delete navigation property device for users
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        """
        request_info = self.create_delete_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, response_handler, error_mapping)
    
    def extensions_by_id(self,id: str) -> extension_item_request_builder.ExtensionItemRequestBuilder:
        """
        Provides operations to manage the extensions property of the microsoft.graph.device entity.
        Args:
            id: Unique identifier of the item
        Returns: extension_item_request_builder.ExtensionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["extension%2Did"] = id
        return extension_item_request_builder.ExtensionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[DeviceRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[device.Device]:
        """
        The registered device on which this Windows Hello for Business key resides. Supports $expand. When you get a user's Windows Hello for Business registration information, this property is returned only on a single GET and when you specify ?$expand. For example, GET /users/admin@contoso.com/authentication/windowsHelloForBusinessMethods/_jpuR-TGZtk6aQCLF3BQjA2?$expand=device.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[device.Device]
        """
        request_info = self.create_get_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, device.Device, response_handler, error_mapping)
    
    def member_of_by_id(self,id: str) -> directory_object_item_request_builder.DirectoryObjectItemRequestBuilder:
        """
        Provides operations to manage the memberOf property of the microsoft.graph.device entity.
        Args:
            id: Unique identifier of the item
        Returns: directory_object_item_request_builder.DirectoryObjectItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["directoryObject%2Did"] = id
        return directory_object_item_request_builder.DirectoryObjectItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def patch(self,body: Optional[device.Device] = None, request_configuration: Optional[DeviceRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[device.Device]:
        """
        Update the navigation property device in users
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[device.Device]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.create_patch_request_information(
            body, request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, device.Device, response_handler, error_mapping)
    
    def registered_owners_by_id(self,id: str) -> directory_object_item_request_builder.DirectoryObjectItemRequestBuilder:
        """
        Gets an item from the msgraph.generated.users.item.authentication.windowsHelloForBusinessMethods.item.device.registeredOwners.item collection
        Args:
            id: Unique identifier of the item
        Returns: directory_object_item_request_builder.DirectoryObjectItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["directoryObject%2Did"] = id
        return directory_object_item_request_builder.DirectoryObjectItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def registered_users_by_id(self,id: str) -> directory_object_item_request_builder.DirectoryObjectItemRequestBuilder:
        """
        Provides operations to manage the registeredUsers property of the microsoft.graph.device entity.
        Args:
            id: Unique identifier of the item
        Returns: directory_object_item_request_builder.DirectoryObjectItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["directoryObject%2Did"] = id
        return directory_object_item_request_builder.DirectoryObjectItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def transitive_member_of_by_id(self,id: str) -> directory_object_item_request_builder.DirectoryObjectItemRequestBuilder:
        """
        Provides operations to manage the transitiveMemberOf property of the microsoft.graph.device entity.
        Args:
            id: Unique identifier of the item
        Returns: directory_object_item_request_builder.DirectoryObjectItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["directoryObject%2Did"] = id
        return directory_object_item_request_builder.DirectoryObjectItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def usage_rights_by_id(self,id: str) -> usage_right_item_request_builder.UsageRightItemRequestBuilder:
        """
        Provides operations to manage the usageRights property of the microsoft.graph.device entity.
        Args:
            id: Unique identifier of the item
        Returns: usage_right_item_request_builder.UsageRightItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["usageRight%2Did"] = id
        return usage_right_item_request_builder.UsageRightItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @dataclass
    class DeviceRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class DeviceRequestBuilderGetQueryParameters():
        """
        The registered device on which this Windows Hello for Business key resides. Supports $expand. When you get a user's Windows Hello for Business registration information, this property is returned only on a single GET and when you specify ?$expand. For example, GET /users/admin@contoso.com/authentication/windowsHelloForBusinessMethods/_jpuR-TGZtk6aQCLF3BQjA2?$expand=device.
        """
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

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
        
    
    @dataclass
    class DeviceRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[DeviceRequestBuilder.DeviceRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class DeviceRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

