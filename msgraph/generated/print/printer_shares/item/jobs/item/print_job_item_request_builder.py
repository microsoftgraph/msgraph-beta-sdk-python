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
    from ......models import print_job
    from ......models.o_data_errors import o_data_error
    from .abort import abort_request_builder
    from .cancel import cancel_request_builder
    from .cancel_print_job import cancel_print_job_request_builder
    from .documents import documents_request_builder
    from .redirect import redirect_request_builder
    from .start import start_request_builder
    from .start_print_job import start_print_job_request_builder
    from .tasks import tasks_request_builder

class PrintJobItemRequestBuilder():
    """
    Provides operations to manage the jobs property of the microsoft.graph.printerBase entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new PrintJobItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/print/printerShares/{printerShare%2Did}/jobs/{printJob%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[PrintJobItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property jobs for print
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ......models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[PrintJobItemRequestBuilderGetRequestConfiguration] = None) -> Optional[print_job.PrintJob]:
        """
        Get jobs from print
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[print_job.PrintJob]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ......models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models import print_job

        return await self.request_adapter.send_async(request_info, print_job.PrintJob, error_mapping)
    
    async def patch(self,body: Optional[print_job.PrintJob] = None, request_configuration: Optional[PrintJobItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[print_job.PrintJob]:
        """
        Update the navigation property jobs in print
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[print_job.PrintJob]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ......models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models import print_job

        return await self.request_adapter.send_async(request_info, print_job.PrintJob, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[PrintJobItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property jobs for print
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
    
    def to_get_request_information(self,request_configuration: Optional[PrintJobItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get jobs from print
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
    
    def to_patch_request_information(self,body: Optional[print_job.PrintJob] = None, request_configuration: Optional[PrintJobItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property jobs in print
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
    def abort(self) -> abort_request_builder.AbortRequestBuilder:
        """
        Provides operations to call the abort method.
        """
        from .abort import abort_request_builder

        return abort_request_builder.AbortRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def cancel(self) -> cancel_request_builder.CancelRequestBuilder:
        """
        Provides operations to call the cancel method.
        """
        from .cancel import cancel_request_builder

        return cancel_request_builder.CancelRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def cancel_print_job(self) -> cancel_print_job_request_builder.CancelPrintJobRequestBuilder:
        """
        Provides operations to call the cancelPrintJob method.
        """
        from .cancel_print_job import cancel_print_job_request_builder

        return cancel_print_job_request_builder.CancelPrintJobRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def documents(self) -> documents_request_builder.DocumentsRequestBuilder:
        """
        Provides operations to manage the documents property of the microsoft.graph.printJob entity.
        """
        from .documents import documents_request_builder

        return documents_request_builder.DocumentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def redirect(self) -> redirect_request_builder.RedirectRequestBuilder:
        """
        Provides operations to call the redirect method.
        """
        from .redirect import redirect_request_builder

        return redirect_request_builder.RedirectRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def start(self) -> start_request_builder.StartRequestBuilder:
        """
        Provides operations to call the start method.
        """
        from .start import start_request_builder

        return start_request_builder.StartRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def start_print_job(self) -> start_print_job_request_builder.StartPrintJobRequestBuilder:
        """
        Provides operations to call the startPrintJob method.
        """
        from .start_print_job import start_print_job_request_builder

        return start_print_job_request_builder.StartPrintJobRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tasks(self) -> tasks_request_builder.TasksRequestBuilder:
        """
        Provides operations to manage the tasks property of the microsoft.graph.printJob entity.
        """
        from .tasks import tasks_request_builder

        return tasks_request_builder.TasksRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class PrintJobItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class PrintJobItemRequestBuilderGetQueryParameters():
        """
        Get jobs from print
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
    class PrintJobItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[PrintJobItemRequestBuilder.PrintJobItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class PrintJobItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
