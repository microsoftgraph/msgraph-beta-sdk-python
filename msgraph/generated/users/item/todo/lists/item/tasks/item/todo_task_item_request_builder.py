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
    from ........models import todo_task
    from ........models.o_data_errors import o_data_error
    from .attachments import attachments_request_builder
    from .attachments.item import attachment_base_item_request_builder
    from .attachment_sessions import attachment_sessions_request_builder
    from .attachment_sessions.item import attachment_session_item_request_builder
    from .checklist_items import checklist_items_request_builder
    from .checklist_items.item import checklist_item_item_request_builder
    from .extensions import extensions_request_builder
    from .extensions.item import extension_item_request_builder
    from .linked_resources import linked_resources_request_builder
    from .linked_resources.item import linked_resource_item_request_builder

class TodoTaskItemRequestBuilder():
    """
    Provides operations to manage the tasks property of the microsoft.graph.todoTaskList entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new TodoTaskItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/users/{user%2Did}/todo/lists/{todoTaskList%2Did}/tasks/{todoTask%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def attachments_by_id(self,id: str) -> attachment_base_item_request_builder.AttachmentBaseItemRequestBuilder:
        """
        Provides operations to manage the attachments property of the microsoft.graph.todoTask entity.
        Args:
            id: Unique identifier of the item
        Returns: attachment_base_item_request_builder.AttachmentBaseItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .attachments.item import attachment_base_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["attachmentBase%2Did"] = id
        return attachment_base_item_request_builder.AttachmentBaseItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def attachment_sessions_by_id(self,id: str) -> attachment_session_item_request_builder.AttachmentSessionItemRequestBuilder:
        """
        Provides operations to manage the attachmentSessions property of the microsoft.graph.todoTask entity.
        Args:
            id: Unique identifier of the item
        Returns: attachment_session_item_request_builder.AttachmentSessionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .attachment_sessions.item import attachment_session_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["attachmentSession%2Did"] = id
        return attachment_session_item_request_builder.AttachmentSessionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def checklist_items_by_id(self,id: str) -> checklist_item_item_request_builder.ChecklistItemItemRequestBuilder:
        """
        Provides operations to manage the checklistItems property of the microsoft.graph.todoTask entity.
        Args:
            id: Unique identifier of the item
        Returns: checklist_item_item_request_builder.ChecklistItemItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .checklist_items.item import checklist_item_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["checklistItem%2Did"] = id
        return checklist_item_item_request_builder.ChecklistItemItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def delete(self,request_configuration: Optional[TodoTaskItemRequestBuilderDeleteRequestConfiguration] = None) -> bytes:
        """
        Delete navigation property tasks for users
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: bytes
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ........models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_primitive_async(request_info, "bytes", error_mapping)
    
    def extensions_by_id(self,id: str) -> extension_item_request_builder.ExtensionItemRequestBuilder:
        """
        Provides operations to manage the extensions property of the microsoft.graph.todoTask entity.
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
    
    async def get(self,request_configuration: Optional[TodoTaskItemRequestBuilderGetRequestConfiguration] = None) -> Optional[todo_task.TodoTask]:
        """
        The tasks in this task list. Read-only. Nullable.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[todo_task.TodoTask]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ........models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ........models import todo_task

        return await self.request_adapter.send_async(request_info, todo_task.TodoTask, error_mapping)
    
    def linked_resources_by_id(self,id: str) -> linked_resource_item_request_builder.LinkedResourceItemRequestBuilder:
        """
        Provides operations to manage the linkedResources property of the microsoft.graph.todoTask entity.
        Args:
            id: Unique identifier of the item
        Returns: linked_resource_item_request_builder.LinkedResourceItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .linked_resources.item import linked_resource_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["linkedResource%2Did"] = id
        return linked_resource_item_request_builder.LinkedResourceItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def patch(self,body: Optional[todo_task.TodoTask] = None, request_configuration: Optional[TodoTaskItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[todo_task.TodoTask]:
        """
        Update the navigation property tasks in users
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[todo_task.TodoTask]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ........models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ........models import todo_task

        return await self.request_adapter.send_async(request_info, todo_task.TodoTask, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[TodoTaskItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property tasks for users
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
    
    def to_get_request_information(self,request_configuration: Optional[TodoTaskItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        The tasks in this task list. Read-only. Nullable.
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
    
    def to_patch_request_information(self,body: Optional[todo_task.TodoTask] = None, request_configuration: Optional[TodoTaskItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property tasks in users
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
    def attachments(self) -> attachments_request_builder.AttachmentsRequestBuilder:
        """
        Provides operations to manage the attachments property of the microsoft.graph.todoTask entity.
        """
        from .attachments import attachments_request_builder

        return attachments_request_builder.AttachmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def attachment_sessions(self) -> attachment_sessions_request_builder.AttachmentSessionsRequestBuilder:
        """
        Provides operations to manage the attachmentSessions property of the microsoft.graph.todoTask entity.
        """
        from .attachment_sessions import attachment_sessions_request_builder

        return attachment_sessions_request_builder.AttachmentSessionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def checklist_items(self) -> checklist_items_request_builder.ChecklistItemsRequestBuilder:
        """
        Provides operations to manage the checklistItems property of the microsoft.graph.todoTask entity.
        """
        from .checklist_items import checklist_items_request_builder

        return checklist_items_request_builder.ChecklistItemsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def extensions(self) -> extensions_request_builder.ExtensionsRequestBuilder:
        """
        Provides operations to manage the extensions property of the microsoft.graph.todoTask entity.
        """
        from .extensions import extensions_request_builder

        return extensions_request_builder.ExtensionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def linked_resources(self) -> linked_resources_request_builder.LinkedResourcesRequestBuilder:
        """
        Provides operations to manage the linkedResources property of the microsoft.graph.todoTask entity.
        """
        from .linked_resources import linked_resources_request_builder

        return linked_resources_request_builder.LinkedResourcesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class TodoTaskItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class TodoTaskItemRequestBuilderGetQueryParameters():
        """
        The tasks in this task list. Read-only. Nullable.
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
    class TodoTaskItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[TodoTaskItemRequestBuilder.TodoTaskItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class TodoTaskItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

