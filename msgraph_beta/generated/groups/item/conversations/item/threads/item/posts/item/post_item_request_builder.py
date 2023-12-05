from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .........models.o_data_errors.o_data_error import ODataError
    from .........models.post import Post
    from .attachments.attachments_request_builder import AttachmentsRequestBuilder
    from .extensions.extensions_request_builder import ExtensionsRequestBuilder
    from .forward.forward_request_builder import ForwardRequestBuilder
    from .in_reply_to.in_reply_to_request_builder import InReplyToRequestBuilder
    from .mentions.mentions_request_builder import MentionsRequestBuilder
    from .reply.reply_request_builder import ReplyRequestBuilder

class PostItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the posts property of the microsoft.graph.conversationThread entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new PostItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/groups/{group%2Did}/conversations/{conversation%2Did}/threads/{conversationThread%2Did}/posts/{post%2Did}{?%24select,%24expand}", path_parameters)
    
    async def get(self,request_configuration: Optional[PostItemRequestBuilderGetRequestConfiguration] = None) -> Optional[Post]:
        """
        Get the properties and relationships of a post in a specified thread. You can specify both the parent conversation and the thread, or, you can specify the thread without referencing the parent conversation. Since the post resource supports extensions, you can also use the GET operation to get custom properties and extension data in a post instance.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Post]
        Find more info here: https://learn.microsoft.com/graph/api/post-get?view=graph-rest-1.0
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .........models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .........models.post import Post

        return await self.request_adapter.send_async(request_info, Post, error_mapping)
    
    async def patch(self,body: Optional[Post] = None, request_configuration: Optional[PostItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[Post]:
        """
        Update the navigation property posts in groups
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Post]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from .........models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .........models.post import Post

        return await self.request_adapter.send_async(request_info, Post, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[PostItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get the properties and relationships of a post in a specified thread. You can specify both the parent conversation and the thread, or, you can specify the thread without referencing the parent conversation. Since the post resource supports extensions, you can also use the GET operation to get custom properties and extension data in a post instance.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: Optional[Post] = None, request_configuration: Optional[PostItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property posts in groups
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.PATCH
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> PostItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: PostItemRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return PostItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def attachments(self) -> AttachmentsRequestBuilder:
        """
        Provides operations to manage the attachments property of the microsoft.graph.post entity.
        """
        from .attachments.attachments_request_builder import AttachmentsRequestBuilder

        return AttachmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def extensions(self) -> ExtensionsRequestBuilder:
        """
        Provides operations to manage the extensions property of the microsoft.graph.post entity.
        """
        from .extensions.extensions_request_builder import ExtensionsRequestBuilder

        return ExtensionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def forward(self) -> ForwardRequestBuilder:
        """
        Provides operations to call the forward method.
        """
        from .forward.forward_request_builder import ForwardRequestBuilder

        return ForwardRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def in_reply_to(self) -> InReplyToRequestBuilder:
        """
        Provides operations to manage the inReplyTo property of the microsoft.graph.post entity.
        """
        from .in_reply_to.in_reply_to_request_builder import InReplyToRequestBuilder

        return InReplyToRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mentions(self) -> MentionsRequestBuilder:
        """
        Provides operations to manage the mentions property of the microsoft.graph.post entity.
        """
        from .mentions.mentions_request_builder import MentionsRequestBuilder

        return MentionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reply(self) -> ReplyRequestBuilder:
        """
        Provides operations to call the reply method.
        """
        from .reply.reply_request_builder import ReplyRequestBuilder

        return ReplyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class PostItemRequestBuilderGetQueryParameters():
        """
        Get the properties and relationships of a post in a specified thread. You can specify both the parent conversation and the thread, or, you can specify the thread without referencing the parent conversation. Since the post resource supports extensions, you can also use the GET operation to get custom properties and extension data in a post instance.
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
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

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class PostItemRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[PostItemRequestBuilder.PostItemRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class PostItemRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

