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

attachments_request_builder = lazy_import('msgraph.generated.groups.item.conversations.item.threads.item.posts.item.in_reply_to.attachments.attachments_request_builder')
attachment_item_request_builder = lazy_import('msgraph.generated.groups.item.conversations.item.threads.item.posts.item.in_reply_to.attachments.item.attachment_item_request_builder')
extensions_request_builder = lazy_import('msgraph.generated.groups.item.conversations.item.threads.item.posts.item.in_reply_to.extensions.extensions_request_builder')
extension_item_request_builder = lazy_import('msgraph.generated.groups.item.conversations.item.threads.item.posts.item.in_reply_to.extensions.item.extension_item_request_builder')
forward_request_builder = lazy_import('msgraph.generated.groups.item.conversations.item.threads.item.posts.item.in_reply_to.forward.forward_request_builder')
mentions_request_builder = lazy_import('msgraph.generated.groups.item.conversations.item.threads.item.posts.item.in_reply_to.mentions.mentions_request_builder')
mention_item_request_builder = lazy_import('msgraph.generated.groups.item.conversations.item.threads.item.posts.item.in_reply_to.mentions.item.mention_item_request_builder')
multi_value_extended_properties_request_builder = lazy_import('msgraph.generated.groups.item.conversations.item.threads.item.posts.item.in_reply_to.multi_value_extended_properties.multi_value_extended_properties_request_builder')
multi_value_legacy_extended_property_item_request_builder = lazy_import('msgraph.generated.groups.item.conversations.item.threads.item.posts.item.in_reply_to.multi_value_extended_properties.item.multi_value_legacy_extended_property_item_request_builder')
reply_request_builder = lazy_import('msgraph.generated.groups.item.conversations.item.threads.item.posts.item.in_reply_to.reply.reply_request_builder')
single_value_extended_properties_request_builder = lazy_import('msgraph.generated.groups.item.conversations.item.threads.item.posts.item.in_reply_to.single_value_extended_properties.single_value_extended_properties_request_builder')
single_value_legacy_extended_property_item_request_builder = lazy_import('msgraph.generated.groups.item.conversations.item.threads.item.posts.item.in_reply_to.single_value_extended_properties.item.single_value_legacy_extended_property_item_request_builder')
post = lazy_import('msgraph.generated.models.post')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class InReplyToRequestBuilder():
    """
    Provides operations to manage the inReplyTo property of the microsoft.graph.post entity.
    """
    @property
    def attachments(self) -> attachments_request_builder.AttachmentsRequestBuilder:
        """
        Provides operations to manage the attachments property of the microsoft.graph.post entity.
        """
        return attachments_request_builder.AttachmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def extensions(self) -> extensions_request_builder.ExtensionsRequestBuilder:
        """
        Provides operations to manage the extensions property of the microsoft.graph.post entity.
        """
        return extensions_request_builder.ExtensionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def forward(self) -> forward_request_builder.ForwardRequestBuilder:
        """
        Provides operations to call the forward method.
        """
        return forward_request_builder.ForwardRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mentions(self) -> mentions_request_builder.MentionsRequestBuilder:
        """
        Provides operations to manage the mentions property of the microsoft.graph.post entity.
        """
        return mentions_request_builder.MentionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def multi_value_extended_properties(self) -> multi_value_extended_properties_request_builder.MultiValueExtendedPropertiesRequestBuilder:
        """
        Provides operations to manage the multiValueExtendedProperties property of the microsoft.graph.post entity.
        """
        return multi_value_extended_properties_request_builder.MultiValueExtendedPropertiesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reply(self) -> reply_request_builder.ReplyRequestBuilder:
        """
        Provides operations to call the reply method.
        """
        return reply_request_builder.ReplyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def single_value_extended_properties(self) -> single_value_extended_properties_request_builder.SingleValueExtendedPropertiesRequestBuilder:
        """
        Provides operations to manage the singleValueExtendedProperties property of the microsoft.graph.post entity.
        """
        return single_value_extended_properties_request_builder.SingleValueExtendedPropertiesRequestBuilder(self.request_adapter, self.path_parameters)
    
    def attachments_by_id(self,id: str) -> attachment_item_request_builder.AttachmentItemRequestBuilder:
        """
        Provides operations to manage the attachments property of the microsoft.graph.post entity.
        Args:
            id: Unique identifier of the item
        Returns: attachment_item_request_builder.AttachmentItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["attachment%2Did"] = id
        return attachment_item_request_builder.AttachmentItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new InReplyToRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/groups/{group%2Did}/conversations/{conversation%2Did}/threads/{conversationThread%2Did}/posts/{post%2Did}/inReplyTo{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def extensions_by_id(self,id: str) -> extension_item_request_builder.ExtensionItemRequestBuilder:
        """
        Provides operations to manage the extensions property of the microsoft.graph.post entity.
        Args:
            id: Unique identifier of the item
        Returns: extension_item_request_builder.ExtensionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["extension%2Did"] = id
        return extension_item_request_builder.ExtensionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[InReplyToRequestBuilderGetRequestConfiguration] = None) -> Optional[post.Post]:
        """
        The earlier post that this post is replying to in the conversationThread. Read-only. Supports $expand.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[post.Post]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, post.Post, error_mapping)
    
    def mentions_by_id(self,id: str) -> mention_item_request_builder.MentionItemRequestBuilder:
        """
        Provides operations to manage the mentions property of the microsoft.graph.post entity.
        Args:
            id: Unique identifier of the item
        Returns: mention_item_request_builder.MentionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["mention%2Did"] = id
        return mention_item_request_builder.MentionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def multi_value_extended_properties_by_id(self,id: str) -> multi_value_legacy_extended_property_item_request_builder.MultiValueLegacyExtendedPropertyItemRequestBuilder:
        """
        Provides operations to manage the multiValueExtendedProperties property of the microsoft.graph.post entity.
        Args:
            id: Unique identifier of the item
        Returns: multi_value_legacy_extended_property_item_request_builder.MultiValueLegacyExtendedPropertyItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["multiValueLegacyExtendedProperty%2Did"] = id
        return multi_value_legacy_extended_property_item_request_builder.MultiValueLegacyExtendedPropertyItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def single_value_extended_properties_by_id(self,id: str) -> single_value_legacy_extended_property_item_request_builder.SingleValueLegacyExtendedPropertyItemRequestBuilder:
        """
        Provides operations to manage the singleValueExtendedProperties property of the microsoft.graph.post entity.
        Args:
            id: Unique identifier of the item
        Returns: single_value_legacy_extended_property_item_request_builder.SingleValueLegacyExtendedPropertyItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["singleValueLegacyExtendedProperty%2Did"] = id
        return single_value_legacy_extended_property_item_request_builder.SingleValueLegacyExtendedPropertyItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def to_get_request_information(self,request_configuration: Optional[InReplyToRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        The earlier post that this post is replying to in the conversationThread. Read-only. Supports $expand.
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
    
    @dataclass
    class InReplyToRequestBuilderGetQueryParameters():
        """
        The earlier post that this post is replying to in the conversationThread. Read-only. Supports $expand.
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
    class InReplyToRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[InReplyToRequestBuilder.InReplyToRequestBuilderGetQueryParameters] = None

    

