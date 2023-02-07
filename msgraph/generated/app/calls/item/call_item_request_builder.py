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

audio_routing_groups_request_builder = lazy_import('msgraph.generated.app.calls.item.audio_routing_groups.audio_routing_groups_request_builder')
audio_routing_group_item_request_builder = lazy_import('msgraph.generated.app.calls.item.audio_routing_groups.item.audio_routing_group_item_request_builder')
content_sharing_sessions_request_builder = lazy_import('msgraph.generated.app.calls.item.content_sharing_sessions.content_sharing_sessions_request_builder')
content_sharing_session_item_request_builder = lazy_import('msgraph.generated.app.calls.item.content_sharing_sessions.item.content_sharing_session_item_request_builder')
microsoft_graph_add_large_gallery_view_request_builder = lazy_import('msgraph.generated.app.calls.item.microsoft_graph_add_large_gallery_view.microsoft_graph_add_large_gallery_view_request_builder')
microsoft_graph_answer_request_builder = lazy_import('msgraph.generated.app.calls.item.microsoft_graph_answer.microsoft_graph_answer_request_builder')
microsoft_graph_cancel_media_processing_request_builder = lazy_import('msgraph.generated.app.calls.item.microsoft_graph_cancel_media_processing.microsoft_graph_cancel_media_processing_request_builder')
microsoft_graph_change_screen_sharing_role_request_builder = lazy_import('msgraph.generated.app.calls.item.microsoft_graph_change_screen_sharing_role.microsoft_graph_change_screen_sharing_role_request_builder')
microsoft_graph_keep_alive_request_builder = lazy_import('msgraph.generated.app.calls.item.microsoft_graph_keep_alive.microsoft_graph_keep_alive_request_builder')
microsoft_graph_mute_request_builder = lazy_import('msgraph.generated.app.calls.item.microsoft_graph_mute.microsoft_graph_mute_request_builder')
microsoft_graph_play_prompt_request_builder = lazy_import('msgraph.generated.app.calls.item.microsoft_graph_play_prompt.microsoft_graph_play_prompt_request_builder')
microsoft_graph_record_request_builder = lazy_import('msgraph.generated.app.calls.item.microsoft_graph_record.microsoft_graph_record_request_builder')
microsoft_graph_record_response_request_builder = lazy_import('msgraph.generated.app.calls.item.microsoft_graph_record_response.microsoft_graph_record_response_request_builder')
microsoft_graph_redirect_request_builder = lazy_import('msgraph.generated.app.calls.item.microsoft_graph_redirect.microsoft_graph_redirect_request_builder')
microsoft_graph_reject_request_builder = lazy_import('msgraph.generated.app.calls.item.microsoft_graph_reject.microsoft_graph_reject_request_builder')
microsoft_graph_subscribe_to_tone_request_builder = lazy_import('msgraph.generated.app.calls.item.microsoft_graph_subscribe_to_tone.microsoft_graph_subscribe_to_tone_request_builder')
microsoft_graph_transfer_request_builder = lazy_import('msgraph.generated.app.calls.item.microsoft_graph_transfer.microsoft_graph_transfer_request_builder')
microsoft_graph_unmute_request_builder = lazy_import('msgraph.generated.app.calls.item.microsoft_graph_unmute.microsoft_graph_unmute_request_builder')
microsoft_graph_update_recording_status_request_builder = lazy_import('msgraph.generated.app.calls.item.microsoft_graph_update_recording_status.microsoft_graph_update_recording_status_request_builder')
operations_request_builder = lazy_import('msgraph.generated.app.calls.item.operations.operations_request_builder')
comms_operation_item_request_builder = lazy_import('msgraph.generated.app.calls.item.operations.item.comms_operation_item_request_builder')
participants_request_builder = lazy_import('msgraph.generated.app.calls.item.participants.participants_request_builder')
participant_item_request_builder = lazy_import('msgraph.generated.app.calls.item.participants.item.participant_item_request_builder')
call = lazy_import('msgraph.generated.models.call')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class CallItemRequestBuilder():
    """
    Provides operations to manage the calls property of the microsoft.graph.commsApplication entity.
    """
    @property
    def audio_routing_groups(self) -> audio_routing_groups_request_builder.AudioRoutingGroupsRequestBuilder:
        """
        Provides operations to manage the audioRoutingGroups property of the microsoft.graph.call entity.
        """
        return audio_routing_groups_request_builder.AudioRoutingGroupsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def content_sharing_sessions(self) -> content_sharing_sessions_request_builder.ContentSharingSessionsRequestBuilder:
        """
        Provides operations to manage the contentSharingSessions property of the microsoft.graph.call entity.
        """
        return content_sharing_sessions_request_builder.ContentSharingSessionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_add_large_gallery_view(self) -> microsoft_graph_add_large_gallery_view_request_builder.MicrosoftGraphAddLargeGalleryViewRequestBuilder:
        """
        Provides operations to call the addLargeGalleryView method.
        """
        return microsoft_graph_add_large_gallery_view_request_builder.MicrosoftGraphAddLargeGalleryViewRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_answer(self) -> microsoft_graph_answer_request_builder.MicrosoftGraphAnswerRequestBuilder:
        """
        Provides operations to call the answer method.
        """
        return microsoft_graph_answer_request_builder.MicrosoftGraphAnswerRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_cancel_media_processing(self) -> microsoft_graph_cancel_media_processing_request_builder.MicrosoftGraphCancelMediaProcessingRequestBuilder:
        """
        Provides operations to call the cancelMediaProcessing method.
        """
        return microsoft_graph_cancel_media_processing_request_builder.MicrosoftGraphCancelMediaProcessingRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_change_screen_sharing_role(self) -> microsoft_graph_change_screen_sharing_role_request_builder.MicrosoftGraphChangeScreenSharingRoleRequestBuilder:
        """
        Provides operations to call the changeScreenSharingRole method.
        """
        return microsoft_graph_change_screen_sharing_role_request_builder.MicrosoftGraphChangeScreenSharingRoleRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_keep_alive(self) -> microsoft_graph_keep_alive_request_builder.MicrosoftGraphKeepAliveRequestBuilder:
        """
        Provides operations to call the keepAlive method.
        """
        return microsoft_graph_keep_alive_request_builder.MicrosoftGraphKeepAliveRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_mute(self) -> microsoft_graph_mute_request_builder.MicrosoftGraphMuteRequestBuilder:
        """
        Provides operations to call the mute method.
        """
        return microsoft_graph_mute_request_builder.MicrosoftGraphMuteRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_play_prompt(self) -> microsoft_graph_play_prompt_request_builder.MicrosoftGraphPlayPromptRequestBuilder:
        """
        Provides operations to call the playPrompt method.
        """
        return microsoft_graph_play_prompt_request_builder.MicrosoftGraphPlayPromptRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_record(self) -> microsoft_graph_record_request_builder.MicrosoftGraphRecordRequestBuilder:
        """
        Provides operations to call the record method.
        """
        return microsoft_graph_record_request_builder.MicrosoftGraphRecordRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_record_response(self) -> microsoft_graph_record_response_request_builder.MicrosoftGraphRecordResponseRequestBuilder:
        """
        Provides operations to call the recordResponse method.
        """
        return microsoft_graph_record_response_request_builder.MicrosoftGraphRecordResponseRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_redirect(self) -> microsoft_graph_redirect_request_builder.MicrosoftGraphRedirectRequestBuilder:
        """
        Provides operations to call the redirect method.
        """
        return microsoft_graph_redirect_request_builder.MicrosoftGraphRedirectRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_reject(self) -> microsoft_graph_reject_request_builder.MicrosoftGraphRejectRequestBuilder:
        """
        Provides operations to call the reject method.
        """
        return microsoft_graph_reject_request_builder.MicrosoftGraphRejectRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_subscribe_to_tone(self) -> microsoft_graph_subscribe_to_tone_request_builder.MicrosoftGraphSubscribeToToneRequestBuilder:
        """
        Provides operations to call the subscribeToTone method.
        """
        return microsoft_graph_subscribe_to_tone_request_builder.MicrosoftGraphSubscribeToToneRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_transfer(self) -> microsoft_graph_transfer_request_builder.MicrosoftGraphTransferRequestBuilder:
        """
        Provides operations to call the transfer method.
        """
        return microsoft_graph_transfer_request_builder.MicrosoftGraphTransferRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_unmute(self) -> microsoft_graph_unmute_request_builder.MicrosoftGraphUnmuteRequestBuilder:
        """
        Provides operations to call the unmute method.
        """
        return microsoft_graph_unmute_request_builder.MicrosoftGraphUnmuteRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_update_recording_status(self) -> microsoft_graph_update_recording_status_request_builder.MicrosoftGraphUpdateRecordingStatusRequestBuilder:
        """
        Provides operations to call the updateRecordingStatus method.
        """
        return microsoft_graph_update_recording_status_request_builder.MicrosoftGraphUpdateRecordingStatusRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def operations(self) -> operations_request_builder.OperationsRequestBuilder:
        """
        Provides operations to manage the operations property of the microsoft.graph.call entity.
        """
        return operations_request_builder.OperationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def participants(self) -> participants_request_builder.ParticipantsRequestBuilder:
        """
        Provides operations to manage the participants property of the microsoft.graph.call entity.
        """
        return participants_request_builder.ParticipantsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def audio_routing_groups_by_id(self,id: str) -> audio_routing_group_item_request_builder.AudioRoutingGroupItemRequestBuilder:
        """
        Provides operations to manage the audioRoutingGroups property of the microsoft.graph.call entity.
        Args:
            id: Unique identifier of the item
        Returns: audio_routing_group_item_request_builder.AudioRoutingGroupItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["audioRoutingGroup%2Did"] = id
        return audio_routing_group_item_request_builder.AudioRoutingGroupItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new CallItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/app/calls/{call%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def content_sharing_sessions_by_id(self,id: str) -> content_sharing_session_item_request_builder.ContentSharingSessionItemRequestBuilder:
        """
        Provides operations to manage the contentSharingSessions property of the microsoft.graph.call entity.
        Args:
            id: Unique identifier of the item
        Returns: content_sharing_session_item_request_builder.ContentSharingSessionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["contentSharingSession%2Did"] = id
        return content_sharing_session_item_request_builder.ContentSharingSessionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def delete(self,request_configuration: Optional[CallItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property calls for app
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
    
    async def get(self,request_configuration: Optional[CallItemRequestBuilderGetRequestConfiguration] = None) -> Optional[call.Call]:
        """
        Get calls from app
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[call.Call]
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
        return await self.request_adapter.send_async(request_info, call.Call, error_mapping)
    
    def operations_by_id(self,id: str) -> comms_operation_item_request_builder.CommsOperationItemRequestBuilder:
        """
        Provides operations to manage the operations property of the microsoft.graph.call entity.
        Args:
            id: Unique identifier of the item
        Returns: comms_operation_item_request_builder.CommsOperationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["commsOperation%2Did"] = id
        return comms_operation_item_request_builder.CommsOperationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def participants_by_id(self,id: str) -> participant_item_request_builder.ParticipantItemRequestBuilder:
        """
        Provides operations to manage the participants property of the microsoft.graph.call entity.
        Args:
            id: Unique identifier of the item
        Returns: participant_item_request_builder.ParticipantItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["participant%2Did"] = id
        return participant_item_request_builder.ParticipantItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def patch(self,body: Optional[call.Call] = None, request_configuration: Optional[CallItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[call.Call]:
        """
        Update the navigation property calls in app
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[call.Call]
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
        return await self.request_adapter.send_async(request_info, call.Call, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[CallItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property calls for app
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
    
    def to_get_request_information(self,request_configuration: Optional[CallItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get calls from app
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
    
    def to_patch_request_information(self,body: Optional[call.Call] = None, request_configuration: Optional[CallItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property calls in app
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
    class CallItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class CallItemRequestBuilderGetQueryParameters():
        """
        Get calls from app
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
    class CallItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[CallItemRequestBuilder.CallItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class CallItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

