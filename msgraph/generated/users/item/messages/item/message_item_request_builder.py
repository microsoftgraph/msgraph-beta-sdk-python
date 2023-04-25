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
    from .....models import message
    from .....models.o_data_errors import o_data_error
    from .attachments import attachments_request_builder
    from .copy import copy_request_builder
    from .create_forward import create_forward_request_builder
    from .create_reply import create_reply_request_builder
    from .create_reply_all import create_reply_all_request_builder
    from .extensions import extensions_request_builder
    from .forward import forward_request_builder
    from .mark_as_junk import mark_as_junk_request_builder
    from .mark_as_not_junk import mark_as_not_junk_request_builder
    from .mentions import mentions_request_builder
    from .move import move_request_builder
    from .multi_value_extended_properties import multi_value_extended_properties_request_builder
    from .reply import reply_request_builder
    from .reply_all import reply_all_request_builder
    from .send import send_request_builder
    from .single_value_extended_properties import single_value_extended_properties_request_builder
    from .unsubscribe import unsubscribe_request_builder
    from .value import content_request_builder

class MessageItemRequestBuilder():
    """
    Provides operations to manage the messages property of the microsoft.graph.user entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new MessageItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/users/{user%2Did}/messages/{message%2Did}{?includeHiddenMessages*,%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[MessageItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property messages for users
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
    
    async def get(self,request_configuration: Optional[MessageItemRequestBuilderGetRequestConfiguration] = None) -> Optional[message.Message]:
        """
        The messages in a mailbox or folder. Read-only. Nullable.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[message.Message]
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
        from .....models import message

        return await self.request_adapter.send_async(request_info, message.Message, error_mapping)
    
    async def patch(self,body: Optional[message.Message] = None, request_configuration: Optional[MessageItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[message.Message]:
        """
        Update the navigation property messages in users
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[message.Message]
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
        from .....models import message

        return await self.request_adapter.send_async(request_info, message.Message, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[MessageItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property messages for users
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
    
    def to_get_request_information(self,request_configuration: Optional[MessageItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        The messages in a mailbox or folder. Read-only. Nullable.
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
    
    def to_patch_request_information(self,body: Optional[message.Message] = None, request_configuration: Optional[MessageItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property messages in users
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
        Provides operations to manage the attachments property of the microsoft.graph.message entity.
        """
        from .attachments import attachments_request_builder

        return attachments_request_builder.AttachmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def content(self) -> content_request_builder.ContentRequestBuilder:
        """
        Provides operations to manage the media for the user entity.
        """
        from .value import content_request_builder

        return content_request_builder.ContentRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def copy(self) -> copy_request_builder.CopyRequestBuilder:
        """
        Provides operations to call the copy method.
        """
        from .copy import copy_request_builder

        return copy_request_builder.CopyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def create_forward(self) -> create_forward_request_builder.CreateForwardRequestBuilder:
        """
        Provides operations to call the createForward method.
        """
        from .create_forward import create_forward_request_builder

        return create_forward_request_builder.CreateForwardRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def create_reply(self) -> create_reply_request_builder.CreateReplyRequestBuilder:
        """
        Provides operations to call the createReply method.
        """
        from .create_reply import create_reply_request_builder

        return create_reply_request_builder.CreateReplyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def create_reply_all(self) -> create_reply_all_request_builder.CreateReplyAllRequestBuilder:
        """
        Provides operations to call the createReplyAll method.
        """
        from .create_reply_all import create_reply_all_request_builder

        return create_reply_all_request_builder.CreateReplyAllRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def extensions(self) -> extensions_request_builder.ExtensionsRequestBuilder:
        """
        Provides operations to manage the extensions property of the microsoft.graph.message entity.
        """
        from .extensions import extensions_request_builder

        return extensions_request_builder.ExtensionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def forward(self) -> forward_request_builder.ForwardRequestBuilder:
        """
        Provides operations to call the forward method.
        """
        from .forward import forward_request_builder

        return forward_request_builder.ForwardRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mark_as_junk(self) -> mark_as_junk_request_builder.MarkAsJunkRequestBuilder:
        """
        Provides operations to call the markAsJunk method.
        """
        from .mark_as_junk import mark_as_junk_request_builder

        return mark_as_junk_request_builder.MarkAsJunkRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mark_as_not_junk(self) -> mark_as_not_junk_request_builder.MarkAsNotJunkRequestBuilder:
        """
        Provides operations to call the markAsNotJunk method.
        """
        from .mark_as_not_junk import mark_as_not_junk_request_builder

        return mark_as_not_junk_request_builder.MarkAsNotJunkRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mentions(self) -> mentions_request_builder.MentionsRequestBuilder:
        """
        Provides operations to manage the mentions property of the microsoft.graph.message entity.
        """
        from .mentions import mentions_request_builder

        return mentions_request_builder.MentionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def move(self) -> move_request_builder.MoveRequestBuilder:
        """
        Provides operations to call the move method.
        """
        from .move import move_request_builder

        return move_request_builder.MoveRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def multi_value_extended_properties(self) -> multi_value_extended_properties_request_builder.MultiValueExtendedPropertiesRequestBuilder:
        """
        Provides operations to manage the multiValueExtendedProperties property of the microsoft.graph.message entity.
        """
        from .multi_value_extended_properties import multi_value_extended_properties_request_builder

        return multi_value_extended_properties_request_builder.MultiValueExtendedPropertiesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reply(self) -> reply_request_builder.ReplyRequestBuilder:
        """
        Provides operations to call the reply method.
        """
        from .reply import reply_request_builder

        return reply_request_builder.ReplyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reply_all(self) -> reply_all_request_builder.ReplyAllRequestBuilder:
        """
        Provides operations to call the replyAll method.
        """
        from .reply_all import reply_all_request_builder

        return reply_all_request_builder.ReplyAllRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def send(self) -> send_request_builder.SendRequestBuilder:
        """
        Provides operations to call the send method.
        """
        from .send import send_request_builder

        return send_request_builder.SendRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def single_value_extended_properties(self) -> single_value_extended_properties_request_builder.SingleValueExtendedPropertiesRequestBuilder:
        """
        Provides operations to manage the singleValueExtendedProperties property of the microsoft.graph.message entity.
        """
        from .single_value_extended_properties import single_value_extended_properties_request_builder

        return single_value_extended_properties_request_builder.SingleValueExtendedPropertiesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def unsubscribe(self) -> unsubscribe_request_builder.UnsubscribeRequestBuilder:
        """
        Provides operations to call the unsubscribe method.
        """
        from .unsubscribe import unsubscribe_request_builder

        return unsubscribe_request_builder.UnsubscribeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class MessageItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class MessageItemRequestBuilderGetQueryParameters():
        """
        The messages in a mailbox or folder. Read-only. Nullable.
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
            if original_name == "include_hidden_messages":
                return "includeHiddenMessages"
            return original_name
        
        # Expand related entities
        expand: Optional[List[str]] = None

        # Include Hidden Messages
        include_hidden_messages: Optional[str] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

    
    @dataclass
    class MessageItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[MessageItemRequestBuilder.MessageItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class MessageItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

