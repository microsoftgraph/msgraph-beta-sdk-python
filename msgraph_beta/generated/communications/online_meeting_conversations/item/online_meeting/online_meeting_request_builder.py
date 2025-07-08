from __future__ import annotations
from collections.abc import Callable
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
from typing import Any, Optional, TYPE_CHECKING, Union
from warnings import warn

if TYPE_CHECKING:
    from .....models.online_meeting import OnlineMeeting
    from .....models.o_data_errors.o_data_error import ODataError
    from .alternative_recording.alternative_recording_request_builder import AlternativeRecordingRequestBuilder
    from .attendee_report.attendee_report_request_builder import AttendeeReportRequestBuilder
    from .broadcast_recording.broadcast_recording_request_builder import BroadcastRecordingRequestBuilder
    from .recording.recording_request_builder import RecordingRequestBuilder

class OnlineMeetingRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the onlineMeeting property of the microsoft.graph.onlineMeetingEngagementConversation entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new OnlineMeetingRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/communications/onlineMeetingConversations/{onlineMeetingEngagementConversation%2Did}/onlineMeeting{?%24expand,%24select}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[OnlineMeetingRequestBuilderGetQueryParameters]] = None) -> Optional[OnlineMeeting]:
        """
        The online meeting associated with the conversation.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[OnlineMeeting]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.online_meeting import OnlineMeeting

        return await self.request_adapter.send_async(request_info, OnlineMeeting, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[OnlineMeetingRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        The online meeting associated with the conversation.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> OnlineMeetingRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: OnlineMeetingRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return OnlineMeetingRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def alternative_recording(self) -> AlternativeRecordingRequestBuilder:
        """
        Provides operations to manage the media for the cloudCommunications entity.
        """
        from .alternative_recording.alternative_recording_request_builder import AlternativeRecordingRequestBuilder

        return AlternativeRecordingRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def attendee_report(self) -> AttendeeReportRequestBuilder:
        """
        Provides operations to manage the media for the cloudCommunications entity.
        """
        from .attendee_report.attendee_report_request_builder import AttendeeReportRequestBuilder

        return AttendeeReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def broadcast_recording(self) -> BroadcastRecordingRequestBuilder:
        """
        Provides operations to manage the media for the cloudCommunications entity.
        """
        from .broadcast_recording.broadcast_recording_request_builder import BroadcastRecordingRequestBuilder

        return BroadcastRecordingRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def recording(self) -> RecordingRequestBuilder:
        """
        Provides operations to manage the media for the cloudCommunications entity.
        """
        from .recording.recording_request_builder import RecordingRequestBuilder

        return RecordingRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class OnlineMeetingRequestBuilderGetQueryParameters():
        """
        The online meeting associated with the conversation.
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
        expand: Optional[list[str]] = None

        # Select properties to be returned
        select: Optional[list[str]] = None

    
    @dataclass
    class OnlineMeetingRequestBuilderGetRequestConfiguration(RequestConfiguration[OnlineMeetingRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

