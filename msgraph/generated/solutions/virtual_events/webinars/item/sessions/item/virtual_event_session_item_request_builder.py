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
    from .......models import virtual_event_session
    from .......models.o_data_errors import o_data_error
    from .alternative_recording import alternative_recording_request_builder
    from .attendance_reports import attendance_reports_request_builder
    from .attendee_report import attendee_report_request_builder
    from .meeting_attendance_report import meeting_attendance_report_request_builder
    from .recording import recording_request_builder
    from .registration import registration_request_builder
    from .transcripts import transcripts_request_builder
    from .virtual_appointment import virtual_appointment_request_builder

class VirtualEventSessionItemRequestBuilder():
    """
    Provides operations to manage the sessions property of the microsoft.graph.virtualEvent entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new VirtualEventSessionItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/solutions/virtualEvents/webinars/{virtualEventWebinar%2Did}/sessions/{virtualEventSession%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[VirtualEventSessionItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property sessions for solutions
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .......models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[VirtualEventSessionItemRequestBuilderGetRequestConfiguration] = None) -> Optional[virtual_event_session.VirtualEventSession]:
        """
        Get sessions from solutions
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[virtual_event_session.VirtualEventSession]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .......models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .......models import virtual_event_session

        return await self.request_adapter.send_async(request_info, virtual_event_session.VirtualEventSession, error_mapping)
    
    async def patch(self,body: Optional[virtual_event_session.VirtualEventSession] = None, request_configuration: Optional[VirtualEventSessionItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[virtual_event_session.VirtualEventSession]:
        """
        Update the navigation property sessions in solutions
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[virtual_event_session.VirtualEventSession]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from .......models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .......models import virtual_event_session

        return await self.request_adapter.send_async(request_info, virtual_event_session.VirtualEventSession, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[VirtualEventSessionItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property sessions for solutions
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
    
    def to_get_request_information(self,request_configuration: Optional[VirtualEventSessionItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get sessions from solutions
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
    
    def to_patch_request_information(self,body: Optional[virtual_event_session.VirtualEventSession] = None, request_configuration: Optional[VirtualEventSessionItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property sessions in solutions
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
    def alternative_recording(self) -> alternative_recording_request_builder.AlternativeRecordingRequestBuilder:
        """
        Provides operations to manage the media for the solutionsRoot entity.
        """
        from .alternative_recording import alternative_recording_request_builder

        return alternative_recording_request_builder.AlternativeRecordingRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def attendance_reports(self) -> attendance_reports_request_builder.AttendanceReportsRequestBuilder:
        """
        Provides operations to manage the attendanceReports property of the microsoft.graph.onlineMeeting entity.
        """
        from .attendance_reports import attendance_reports_request_builder

        return attendance_reports_request_builder.AttendanceReportsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def attendee_report(self) -> attendee_report_request_builder.AttendeeReportRequestBuilder:
        """
        Provides operations to manage the media for the solutionsRoot entity.
        """
        from .attendee_report import attendee_report_request_builder

        return attendee_report_request_builder.AttendeeReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def meeting_attendance_report(self) -> meeting_attendance_report_request_builder.MeetingAttendanceReportRequestBuilder:
        """
        Provides operations to manage the meetingAttendanceReport property of the microsoft.graph.onlineMeeting entity.
        """
        from .meeting_attendance_report import meeting_attendance_report_request_builder

        return meeting_attendance_report_request_builder.MeetingAttendanceReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def recording(self) -> recording_request_builder.RecordingRequestBuilder:
        """
        Provides operations to manage the media for the solutionsRoot entity.
        """
        from .recording import recording_request_builder

        return recording_request_builder.RecordingRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def registration(self) -> registration_request_builder.RegistrationRequestBuilder:
        """
        Provides operations to manage the registration property of the microsoft.graph.onlineMeeting entity.
        """
        from .registration import registration_request_builder

        return registration_request_builder.RegistrationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def transcripts(self) -> transcripts_request_builder.TranscriptsRequestBuilder:
        """
        Provides operations to manage the transcripts property of the microsoft.graph.onlineMeeting entity.
        """
        from .transcripts import transcripts_request_builder

        return transcripts_request_builder.TranscriptsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def virtual_appointment(self) -> virtual_appointment_request_builder.VirtualAppointmentRequestBuilder:
        """
        Provides operations to manage the virtualAppointment property of the microsoft.graph.onlineMeeting entity.
        """
        from .virtual_appointment import virtual_appointment_request_builder

        return virtual_appointment_request_builder.VirtualAppointmentRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class VirtualEventSessionItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class VirtualEventSessionItemRequestBuilderGetQueryParameters():
        """
        Get sessions from solutions
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
    class VirtualEventSessionItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[VirtualEventSessionItemRequestBuilder.VirtualEventSessionItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class VirtualEventSessionItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

