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
    from ....models import device
    from ....models.o_data_errors import o_data_error
    from .check_member_groups import check_member_groups_request_builder
    from .check_member_objects import check_member_objects_request_builder
    from .commands import commands_request_builder
    from .commands.item import command_item_request_builder
    from .extensions import extensions_request_builder
    from .extensions.item import extension_item_request_builder
    from .get_member_groups import get_member_groups_request_builder
    from .get_member_objects import get_member_objects_request_builder
    from .member_of import member_of_request_builder
    from .member_of.item import directory_object_item_request_builder
    from .registered_owners import registered_owners_request_builder
    from .registered_owners.item import directory_object_item_request_builder
    from .registered_users import registered_users_request_builder
    from .registered_users.item import directory_object_item_request_builder
    from .restore import restore_request_builder
    from .transitive_member_of import transitive_member_of_request_builder
    from .transitive_member_of.item import directory_object_item_request_builder
    from .usage_rights import usage_rights_request_builder
    from .usage_rights.item import usage_right_item_request_builder

class DeviceItemRequestBuilder():
    """
    Provides operations to manage the devices property of the microsoft.graph.user entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new DeviceItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/me/devices/{device%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def commands_by_id(self,id: str) -> command_item_request_builder.CommandItemRequestBuilder:
        """
        Provides operations to manage the commands property of the microsoft.graph.device entity.
        Args:
            id: Unique identifier of the item
        Returns: command_item_request_builder.CommandItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .commands.item import command_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["command%2Did"] = id
        return command_item_request_builder.CommandItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def delete(self,request_configuration: Optional[DeviceItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property devices for me
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
    
    def extensions_by_id(self,id: str) -> extension_item_request_builder.ExtensionItemRequestBuilder:
        """
        Provides operations to manage the extensions property of the microsoft.graph.device entity.
        Args:
            id: Unique identifier of the item
        Returns: extension_item_request_builder.ExtensionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .extensions.item import extension_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["extension%2Did"] = id
        return extension_item_request_builder.ExtensionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[DeviceItemRequestBuilderGetRequestConfiguration] = None) -> Optional[device.Device]:
        """
        Get devices from me
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[device.Device]
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
        from ....models import device

        return await self.request_adapter.send_async(request_info, device.Device, error_mapping)
    
    def member_of_by_id(self,id: str) -> directory_object_item_request_builder.DirectoryObjectItemRequestBuilder:
        """
        Provides operations to manage the memberOf property of the microsoft.graph.device entity.
        Args:
            id: Unique identifier of the item
        Returns: directory_object_item_request_builder.DirectoryObjectItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .member_of.item import directory_object_item_request_builder
        from .registered_owners.item import directory_object_item_request_builder
        from .registered_users.item import directory_object_item_request_builder
        from .transitive_member_of.item import directory_object_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["directoryObject%2Did"] = id
        return directory_object_item_request_builder.DirectoryObjectItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def patch(self,body: Optional[device.Device] = None, request_configuration: Optional[DeviceItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[device.Device]:
        """
        Update the navigation property devices in me
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[device.Device]
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
        from ....models import device

        return await self.request_adapter.send_async(request_info, device.Device, error_mapping)
    
    def registered_owners_by_id(self,id: str) -> directory_object_item_request_builder.DirectoryObjectItemRequestBuilder:
        """
        Gets an item from the msgraph.generated.me.devices.item.registeredOwners.item collection
        Args:
            id: Unique identifier of the item
        Returns: directory_object_item_request_builder.DirectoryObjectItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .member_of.item import directory_object_item_request_builder
        from .registered_owners.item import directory_object_item_request_builder
        from .registered_users.item import directory_object_item_request_builder
        from .transitive_member_of.item import directory_object_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["directoryObject%2Did"] = id
        return directory_object_item_request_builder.DirectoryObjectItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def registered_users_by_id(self,id: str) -> directory_object_item_request_builder.DirectoryObjectItemRequestBuilder:
        """
        Gets an item from the msgraph.generated.me.devices.item.registeredUsers.item collection
        Args:
            id: Unique identifier of the item
        Returns: directory_object_item_request_builder.DirectoryObjectItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .member_of.item import directory_object_item_request_builder
        from .registered_owners.item import directory_object_item_request_builder
        from .registered_users.item import directory_object_item_request_builder
        from .transitive_member_of.item import directory_object_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["directoryObject%2Did"] = id
        return directory_object_item_request_builder.DirectoryObjectItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def to_delete_request_information(self,request_configuration: Optional[DeviceItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property devices for me
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
    
    def to_get_request_information(self,request_configuration: Optional[DeviceItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get devices from me
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
    
    def to_patch_request_information(self,body: Optional[device.Device] = None, request_configuration: Optional[DeviceItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property devices in me
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
    
    def transitive_member_of_by_id(self,id: str) -> directory_object_item_request_builder.DirectoryObjectItemRequestBuilder:
        """
        Provides operations to manage the transitiveMemberOf property of the microsoft.graph.device entity.
        Args:
            id: Unique identifier of the item
        Returns: directory_object_item_request_builder.DirectoryObjectItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .member_of.item import directory_object_item_request_builder
        from .registered_owners.item import directory_object_item_request_builder
        from .registered_users.item import directory_object_item_request_builder
        from .transitive_member_of.item import directory_object_item_request_builder

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
        from .usage_rights.item import usage_right_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["usageRight%2Did"] = id
        return usage_right_item_request_builder.UsageRightItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @property
    def check_member_groups(self) -> check_member_groups_request_builder.CheckMemberGroupsRequestBuilder:
        """
        Provides operations to call the checkMemberGroups method.
        """
        from .check_member_groups import check_member_groups_request_builder

        return check_member_groups_request_builder.CheckMemberGroupsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def check_member_objects(self) -> check_member_objects_request_builder.CheckMemberObjectsRequestBuilder:
        """
        Provides operations to call the checkMemberObjects method.
        """
        from .check_member_objects import check_member_objects_request_builder

        return check_member_objects_request_builder.CheckMemberObjectsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def commands(self) -> commands_request_builder.CommandsRequestBuilder:
        """
        Provides operations to manage the commands property of the microsoft.graph.device entity.
        """
        from .commands import commands_request_builder

        return commands_request_builder.CommandsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def extensions(self) -> extensions_request_builder.ExtensionsRequestBuilder:
        """
        Provides operations to manage the extensions property of the microsoft.graph.device entity.
        """
        from .extensions import extensions_request_builder

        return extensions_request_builder.ExtensionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_member_groups(self) -> get_member_groups_request_builder.GetMemberGroupsRequestBuilder:
        """
        Provides operations to call the getMemberGroups method.
        """
        from .get_member_groups import get_member_groups_request_builder

        return get_member_groups_request_builder.GetMemberGroupsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_member_objects(self) -> get_member_objects_request_builder.GetMemberObjectsRequestBuilder:
        """
        Provides operations to call the getMemberObjects method.
        """
        from .get_member_objects import get_member_objects_request_builder

        return get_member_objects_request_builder.GetMemberObjectsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def member_of(self) -> member_of_request_builder.MemberOfRequestBuilder:
        """
        Provides operations to manage the memberOf property of the microsoft.graph.device entity.
        """
        from .member_of import member_of_request_builder

        return member_of_request_builder.MemberOfRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def registered_owners(self) -> registered_owners_request_builder.RegisteredOwnersRequestBuilder:
        """
        Provides operations to manage the registeredOwners property of the microsoft.graph.device entity.
        """
        from .registered_owners import registered_owners_request_builder

        return registered_owners_request_builder.RegisteredOwnersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def registered_users(self) -> registered_users_request_builder.RegisteredUsersRequestBuilder:
        """
        Provides operations to manage the registeredUsers property of the microsoft.graph.device entity.
        """
        from .registered_users import registered_users_request_builder

        return registered_users_request_builder.RegisteredUsersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def restore(self) -> restore_request_builder.RestoreRequestBuilder:
        """
        Provides operations to call the restore method.
        """
        from .restore import restore_request_builder

        return restore_request_builder.RestoreRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def transitive_member_of(self) -> transitive_member_of_request_builder.TransitiveMemberOfRequestBuilder:
        """
        Provides operations to manage the transitiveMemberOf property of the microsoft.graph.device entity.
        """
        from .transitive_member_of import transitive_member_of_request_builder

        return transitive_member_of_request_builder.TransitiveMemberOfRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def usage_rights(self) -> usage_rights_request_builder.UsageRightsRequestBuilder:
        """
        Provides operations to manage the usageRights property of the microsoft.graph.device entity.
        """
        from .usage_rights import usage_rights_request_builder

        return usage_rights_request_builder.UsageRightsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class DeviceItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class DeviceItemRequestBuilderGetQueryParameters():
        """
        Get devices from me
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
    class DeviceItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[DeviceItemRequestBuilder.DeviceItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class DeviceItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

