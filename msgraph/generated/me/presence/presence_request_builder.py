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

clear_presence_request_builder = lazy_import('msgraph.generated.me.presence.clear_presence.clear_presence_request_builder')
clear_user_preferred_presence_request_builder = lazy_import('msgraph.generated.me.presence.clear_user_preferred_presence.clear_user_preferred_presence_request_builder')
set_presence_request_builder = lazy_import('msgraph.generated.me.presence.set_presence.set_presence_request_builder')
set_status_message_request_builder = lazy_import('msgraph.generated.me.presence.set_status_message.set_status_message_request_builder')
set_user_preferred_presence_request_builder = lazy_import('msgraph.generated.me.presence.set_user_preferred_presence.set_user_preferred_presence_request_builder')
presence = lazy_import('msgraph.generated.models.presence')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class PresenceRequestBuilder():
    """
    Provides operations to manage the presence property of the microsoft.graph.user entity.
    """
    @property
    def clear_presence(self) -> clear_presence_request_builder.ClearPresenceRequestBuilder:
        """
        Provides operations to call the clearPresence method.
        """
        return clear_presence_request_builder.ClearPresenceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def clear_user_preferred_presence(self) -> clear_user_preferred_presence_request_builder.ClearUserPreferredPresenceRequestBuilder:
        """
        Provides operations to call the clearUserPreferredPresence method.
        """
        return clear_user_preferred_presence_request_builder.ClearUserPreferredPresenceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def set_presence(self) -> set_presence_request_builder.SetPresenceRequestBuilder:
        """
        Provides operations to call the setPresence method.
        """
        return set_presence_request_builder.SetPresenceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def set_status_message(self) -> set_status_message_request_builder.SetStatusMessageRequestBuilder:
        """
        Provides operations to call the setStatusMessage method.
        """
        return set_status_message_request_builder.SetStatusMessageRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def set_user_preferred_presence(self) -> set_user_preferred_presence_request_builder.SetUserPreferredPresenceRequestBuilder:
        """
        Provides operations to call the setUserPreferredPresence method.
        """
        return set_user_preferred_presence_request_builder.SetUserPreferredPresenceRequestBuilder(self.request_adapter, self.path_parameters)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new PresenceRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/me/presence{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[PresenceRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property presence for me
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[PresenceRequestBuilderGetRequestConfiguration] = None) -> Optional[presence.Presence]:
        """
        Get a user's presence information.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[presence.Presence]
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
        return await self.request_adapter.send_async(request_info, presence.Presence, error_mapping)
    
    async def patch(self,body: Optional[presence.Presence] = None, request_configuration: Optional[PresenceRequestBuilderPatchRequestConfiguration] = None) -> Optional[presence.Presence]:
        """
        Update the navigation property presence in me
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[presence.Presence]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, presence.Presence, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[PresenceRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property presence for me
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
    
    def to_get_request_information(self,request_configuration: Optional[PresenceRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get a user's presence information.
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
    
    def to_patch_request_information(self,body: Optional[presence.Presence] = None, request_configuration: Optional[PresenceRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property presence in me
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
    
    @dataclass
    class PresenceRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class PresenceRequestBuilderGetQueryParameters():
        """
        Get a user's presence information.
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
    class PresenceRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[PresenceRequestBuilder.PresenceRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class PresenceRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

