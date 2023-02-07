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

alternative_recording_request_builder = lazy_import('msgraph.generated.app.online_meetings.item.alternative_recording.alternative_recording_request_builder')
attendance_reports_request_builder = lazy_import('msgraph.generated.app.online_meetings.item.attendance_reports.attendance_reports_request_builder')
meeting_attendance_report_item_request_builder = lazy_import('msgraph.generated.app.online_meetings.item.attendance_reports.item.meeting_attendance_report_item_request_builder')
attendee_report_request_builder = lazy_import('msgraph.generated.app.online_meetings.item.attendee_report.attendee_report_request_builder')
meeting_attendance_report_request_builder = lazy_import('msgraph.generated.app.online_meetings.item.meeting_attendance_report.meeting_attendance_report_request_builder')
recording_request_builder = lazy_import('msgraph.generated.app.online_meetings.item.recording.recording_request_builder')
registration_request_builder = lazy_import('msgraph.generated.app.online_meetings.item.registration.registration_request_builder')
transcripts_request_builder = lazy_import('msgraph.generated.app.online_meetings.item.transcripts.transcripts_request_builder')
call_transcript_item_request_builder = lazy_import('msgraph.generated.app.online_meetings.item.transcripts.item.call_transcript_item_request_builder')
virtual_appointment_request_builder = lazy_import('msgraph.generated.app.online_meetings.item.virtual_appointment.virtual_appointment_request_builder')
online_meeting = lazy_import('msgraph.generated.models.online_meeting')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class OnlineMeetingItemRequestBuilder():
    """
    Provides operations to manage the onlineMeetings property of the microsoft.graph.commsApplication entity.
    """
    @property
    def alternative_recording(self) -> alternative_recording_request_builder.AlternativeRecordingRequestBuilder:
        """
        Provides operations to manage the media for the commsApplication entity.
        """
        return alternative_recording_request_builder.AlternativeRecordingRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def attendance_reports(self) -> attendance_reports_request_builder.AttendanceReportsRequestBuilder:
        """
        Provides operations to manage the attendanceReports property of the microsoft.graph.onlineMeeting entity.
        """
        return attendance_reports_request_builder.AttendanceReportsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def attendee_report(self) -> attendee_report_request_builder.AttendeeReportRequestBuilder:
        """
        Provides operations to manage the media for the commsApplication entity.
        """
        return attendee_report_request_builder.AttendeeReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def meeting_attendance_report(self) -> meeting_attendance_report_request_builder.MeetingAttendanceReportRequestBuilder:
        """
        Provides operations to manage the meetingAttendanceReport property of the microsoft.graph.onlineMeeting entity.
        """
        return meeting_attendance_report_request_builder.MeetingAttendanceReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def recording(self) -> recording_request_builder.RecordingRequestBuilder:
        """
        Provides operations to manage the media for the commsApplication entity.
        """
        return recording_request_builder.RecordingRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def registration(self) -> registration_request_builder.RegistrationRequestBuilder:
        """
        Provides operations to manage the registration property of the microsoft.graph.onlineMeeting entity.
        """
        return registration_request_builder.RegistrationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def transcripts(self) -> transcripts_request_builder.TranscriptsRequestBuilder:
        """
        Provides operations to manage the transcripts property of the microsoft.graph.onlineMeeting entity.
        """
        return transcripts_request_builder.TranscriptsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def virtual_appointment(self) -> virtual_appointment_request_builder.VirtualAppointmentRequestBuilder:
        """
        Provides operations to manage the virtualAppointment property of the microsoft.graph.onlineMeeting entity.
        """
        return virtual_appointment_request_builder.VirtualAppointmentRequestBuilder(self.request_adapter, self.path_parameters)
    
    def attendance_reports_by_id(self,id: str) -> meeting_attendance_report_item_request_builder.MeetingAttendanceReportItemRequestBuilder:
        """
        Provides operations to manage the attendanceReports property of the microsoft.graph.onlineMeeting entity.
        Args:
            id: Unique identifier of the item
        Returns: meeting_attendance_report_item_request_builder.MeetingAttendanceReportItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["meetingAttendanceReport%2Did"] = id
        return meeting_attendance_report_item_request_builder.MeetingAttendanceReportItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new OnlineMeetingItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/app/onlineMeetings/{onlineMeeting%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[OnlineMeetingItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property onlineMeetings for app
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
    
    async def get(self,request_configuration: Optional[OnlineMeetingItemRequestBuilderGetRequestConfiguration] = None) -> Optional[online_meeting.OnlineMeeting]:
        """
        Get onlineMeetings from app
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[online_meeting.OnlineMeeting]
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
        return await self.request_adapter.send_async(request_info, online_meeting.OnlineMeeting, error_mapping)
    
    async def patch(self,body: Optional[online_meeting.OnlineMeeting] = None, request_configuration: Optional[OnlineMeetingItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[online_meeting.OnlineMeeting]:
        """
        Update the navigation property onlineMeetings in app
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[online_meeting.OnlineMeeting]
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
        return await self.request_adapter.send_async(request_info, online_meeting.OnlineMeeting, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[OnlineMeetingItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property onlineMeetings for app
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
    
    def to_get_request_information(self,request_configuration: Optional[OnlineMeetingItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get onlineMeetings from app
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
    
    def to_patch_request_information(self,body: Optional[online_meeting.OnlineMeeting] = None, request_configuration: Optional[OnlineMeetingItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property onlineMeetings in app
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
    
    def transcripts_by_id(self,id: str) -> call_transcript_item_request_builder.CallTranscriptItemRequestBuilder:
        """
        Provides operations to manage the transcripts property of the microsoft.graph.onlineMeeting entity.
        Args:
            id: Unique identifier of the item
        Returns: call_transcript_item_request_builder.CallTranscriptItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["callTranscript%2Did"] = id
        return call_transcript_item_request_builder.CallTranscriptItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @dataclass
    class OnlineMeetingItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class OnlineMeetingItemRequestBuilderGetQueryParameters():
        """
        Get onlineMeetings from app
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
    class OnlineMeetingItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[OnlineMeetingItemRequestBuilder.OnlineMeetingItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class OnlineMeetingItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

