from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ....models.o_data_errors.o_data_error import ODataError
    from ....models.online_meeting import OnlineMeeting
    from .alternative_recording.alternative_recording_request_builder import AlternativeRecordingRequestBuilder
    from .attendance_reports.attendance_reports_request_builder import AttendanceReportsRequestBuilder
    from .attendee_report.attendee_report_request_builder import AttendeeReportRequestBuilder
    from .broadcast_recording.broadcast_recording_request_builder import BroadcastRecordingRequestBuilder
    from .get_virtual_appointment_join_web_url.get_virtual_appointment_join_web_url_request_builder import GetVirtualAppointmentJoinWebUrlRequestBuilder
    from .meeting_attendance_report.meeting_attendance_report_request_builder import MeetingAttendanceReportRequestBuilder
    from .recording.recording_request_builder import RecordingRequestBuilder
    from .recordings.recordings_request_builder import RecordingsRequestBuilder
    from .registration.registration_request_builder import RegistrationRequestBuilder
    from .transcripts.transcripts_request_builder import TranscriptsRequestBuilder
    from .virtual_appointment.virtual_appointment_request_builder import VirtualAppointmentRequestBuilder

class OnlineMeetingItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the onlineMeetings property of the microsoft.graph.commsApplication entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new OnlineMeetingItemRequestBuilder and sets the default values.
        Args:
            path_parameters: The raw url or the Url template parameters for the request.
            request_adapter: The request adapter to use to execute the requests.
        """
        super().__init__(request_adapter, "{+baseurl}/app/onlineMeetings/{onlineMeeting%2Did}{?%24select,%24expand}", path_parameters)
    
    async def delete(self,request_configuration: Optional[OnlineMeetingItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property onlineMeetings for app
        Args:
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[OnlineMeetingItemRequestBuilderGetRequestConfiguration] = None) -> Optional[OnlineMeeting]:
        """
        Get onlineMeetings from app
        Args:
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[OnlineMeeting]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.online_meeting import OnlineMeeting

        return await self.request_adapter.send_async(request_info, OnlineMeeting, error_mapping)
    
    async def patch(self,body: Optional[OnlineMeeting] = None, request_configuration: Optional[OnlineMeetingItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[OnlineMeeting]:
        """
        Update the navigation property onlineMeetings in app
        Args:
            body: The request body
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[OnlineMeeting]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.online_meeting import OnlineMeeting

        return await self.request_adapter.send_async(request_info, OnlineMeeting, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[OnlineMeetingItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property onlineMeetings for app
        Args:
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
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
    
    def to_get_request_information(self,request_configuration: Optional[OnlineMeetingItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get onlineMeetings from app
        Args:
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
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
    
    def to_patch_request_information(self,body: Optional[OnlineMeeting] = None, request_configuration: Optional[OnlineMeetingItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property onlineMeetings in app
        Args:
            body: The request body
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
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
    def alternative_recording(self) -> AlternativeRecordingRequestBuilder:
        """
        Provides operations to manage the media for the commsApplication entity.
        """
        from .alternative_recording.alternative_recording_request_builder import AlternativeRecordingRequestBuilder

        return AlternativeRecordingRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def attendance_reports(self) -> AttendanceReportsRequestBuilder:
        """
        Provides operations to manage the attendanceReports property of the microsoft.graph.onlineMeeting entity.
        """
        from .attendance_reports.attendance_reports_request_builder import AttendanceReportsRequestBuilder

        return AttendanceReportsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def attendee_report(self) -> AttendeeReportRequestBuilder:
        """
        Provides operations to manage the media for the commsApplication entity.
        """
        from .attendee_report.attendee_report_request_builder import AttendeeReportRequestBuilder

        return AttendeeReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def broadcast_recording(self) -> BroadcastRecordingRequestBuilder:
        """
        Provides operations to manage the media for the commsApplication entity.
        """
        from .broadcast_recording.broadcast_recording_request_builder import BroadcastRecordingRequestBuilder

        return BroadcastRecordingRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_virtual_appointment_join_web_url(self) -> GetVirtualAppointmentJoinWebUrlRequestBuilder:
        """
        Provides operations to call the getVirtualAppointmentJoinWebUrl method.
        """
        from .get_virtual_appointment_join_web_url.get_virtual_appointment_join_web_url_request_builder import GetVirtualAppointmentJoinWebUrlRequestBuilder

        return GetVirtualAppointmentJoinWebUrlRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def meeting_attendance_report(self) -> MeetingAttendanceReportRequestBuilder:
        """
        Provides operations to manage the meetingAttendanceReport property of the microsoft.graph.onlineMeeting entity.
        """
        from .meeting_attendance_report.meeting_attendance_report_request_builder import MeetingAttendanceReportRequestBuilder

        return MeetingAttendanceReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def recording(self) -> RecordingRequestBuilder:
        """
        Provides operations to manage the media for the commsApplication entity.
        """
        from .recording.recording_request_builder import RecordingRequestBuilder

        return RecordingRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def recordings(self) -> RecordingsRequestBuilder:
        """
        Provides operations to manage the recordings property of the microsoft.graph.onlineMeeting entity.
        """
        from .recordings.recordings_request_builder import RecordingsRequestBuilder

        return RecordingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def registration(self) -> RegistrationRequestBuilder:
        """
        Provides operations to manage the registration property of the microsoft.graph.onlineMeeting entity.
        """
        from .registration.registration_request_builder import RegistrationRequestBuilder

        return RegistrationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def transcripts(self) -> TranscriptsRequestBuilder:
        """
        Provides operations to manage the transcripts property of the microsoft.graph.onlineMeeting entity.
        """
        from .transcripts.transcripts_request_builder import TranscriptsRequestBuilder

        return TranscriptsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def virtual_appointment(self) -> VirtualAppointmentRequestBuilder:
        """
        Provides operations to manage the virtualAppointment property of the microsoft.graph.onlineMeeting entity.
        """
        from .virtual_appointment.virtual_appointment_request_builder import VirtualAppointmentRequestBuilder

        return VirtualAppointmentRequestBuilder(self.request_adapter, self.path_parameters)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class OnlineMeetingItemRequestBuilderDeleteRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
    @dataclass
    class OnlineMeetingItemRequestBuilderGetQueryParameters():
        """
        Get onlineMeetings from app
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            Args:
                original_name: The original query parameter name in the class.
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
    class OnlineMeetingItemRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[OnlineMeetingItemRequestBuilder.OnlineMeetingItemRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class OnlineMeetingItemRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

