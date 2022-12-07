from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

task_report_summary = lazy_import('msgraph.generated.models.identity_governance.task_report_summary')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class SummaryWithStartDateTimeWithEndDateTimeRequestBuilder():
    """
    Provides operations to call the summary method.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None, end_date_time: Optional[datetime] = None, start_date_time: Optional[datetime] = None) -> None:
        """
        Instantiates a new SummaryWithStartDateTimeWithEndDateTimeRequestBuilder and sets the default values.
        Args:
            endDateTime: Usage: endDateTime={endDateTime}
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
            startDateTime: Usage: startDateTime={startDateTime}
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/identityGovernance/lifecycleWorkflows/deletedItems/workflows/{workflow%2Did}/taskReports/microsoft.graph.identityGovernance.summary(startDateTime={startDateTime},endDateTime={endDateTime})"

        url_tpl_params = get_path_parameters(path_parameters)
        url_tpl_params[""] = endDateTime
        url_tpl_params[""] = startDateTime
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def create_get_request_information(self,request_configuration: Optional[SummaryWithStartDateTimeWithEndDateTimeRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Invoke function summary
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
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    async def get(self,request_configuration: Optional[SummaryWithStartDateTimeWithEndDateTimeRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[task_report_summary.TaskReportSummary]:
        """
        Invoke function summary
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[task_report_summary.TaskReportSummary]
        """
        request_info = self.create_get_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, task_report_summary.TaskReportSummary, response_handler, error_mapping)
    
    @dataclass
    class SummaryWithStartDateTimeWithEndDateTimeRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

