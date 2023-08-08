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
    from ......models.o_data_errors.o_data_error import ODataError
    from ......models.workbook import Workbook
    from .application.application_request_builder import ApplicationRequestBuilder
    from .close_session.close_session_request_builder import CloseSessionRequestBuilder
    from .comments.comments_request_builder import CommentsRequestBuilder
    from .create_session.create_session_request_builder import CreateSessionRequestBuilder
    from .functions.functions_request_builder import FunctionsRequestBuilder
    from .names.names_request_builder import NamesRequestBuilder
    from .operations.operations_request_builder import OperationsRequestBuilder
    from .refresh_session.refresh_session_request_builder import RefreshSessionRequestBuilder
    from .session_info_resource_with_key.session_info_resource_with_key_request_builder import SessionInfoResourceWithKeyRequestBuilder
    from .table_row_operation_result_with_key.table_row_operation_result_with_key_request_builder import TableRowOperationResultWithKeyRequestBuilder
    from .tables.tables_request_builder import TablesRequestBuilder
    from .worksheets.worksheets_request_builder import WorksheetsRequestBuilder

class WorkbookRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the workbook property of the microsoft.graph.driveItem entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new WorkbookRequestBuilder and sets the default values.
        Args:
            path_parameters: The raw url or the Url template parameters for the request.
            request_adapter: The request adapter to use to execute the requests.
        """
        super().__init__(request_adapter, "{+baseurl}/drives/{drive%2Did}/items/{driveItem%2Did}/workbook{?%24select,%24expand}", path_parameters)
    
    async def delete(self,request_configuration: Optional[WorkbookRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property workbook for drives
        Args:
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[WorkbookRequestBuilderGetRequestConfiguration] = None) -> Optional[Workbook]:
        """
        For files that are Excel spreadsheets, accesses the workbook API to work with the spreadsheet's contents. Nullable.
        Args:
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Workbook]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.workbook import Workbook

        return await self.request_adapter.send_async(request_info, Workbook, error_mapping)
    
    async def patch(self,body: Optional[Workbook] = None, request_configuration: Optional[WorkbookRequestBuilderPatchRequestConfiguration] = None) -> Optional[Workbook]:
        """
        Update the navigation property workbook in drives
        Args:
            body: The request body
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Workbook]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.workbook import Workbook

        return await self.request_adapter.send_async(request_info, Workbook, error_mapping)
    
    def session_info_resource_with_key(self,key: Optional[str] = None) -> SessionInfoResourceWithKeyRequestBuilder:
        """
        Provides operations to call the sessionInfoResource method.
        Args:
            key: Usage: key='{key}'
        Returns: SessionInfoResourceWithKeyRequestBuilder
        """
        if not key:
            raise TypeError("key cannot be null.")
        from .session_info_resource_with_key.session_info_resource_with_key_request_builder import SessionInfoResourceWithKeyRequestBuilder

        return SessionInfoResourceWithKeyRequestBuilder(self.request_adapter, self.path_parameters, key)
    
    def table_row_operation_result_with_key(self,key: Optional[str] = None) -> TableRowOperationResultWithKeyRequestBuilder:
        """
        Provides operations to call the tableRowOperationResult method.
        Args:
            key: Usage: key='{key}'
        Returns: TableRowOperationResultWithKeyRequestBuilder
        """
        if not key:
            raise TypeError("key cannot be null.")
        from .table_row_operation_result_with_key.table_row_operation_result_with_key_request_builder import TableRowOperationResultWithKeyRequestBuilder

        return TableRowOperationResultWithKeyRequestBuilder(self.request_adapter, self.path_parameters, key)
    
    def to_delete_request_information(self,request_configuration: Optional[WorkbookRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property workbook for drives
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
    
    def to_get_request_information(self,request_configuration: Optional[WorkbookRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        For files that are Excel spreadsheets, accesses the workbook API to work with the spreadsheet's contents. Nullable.
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
    
    def to_patch_request_information(self,body: Optional[Workbook] = None, request_configuration: Optional[WorkbookRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property workbook in drives
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
    def application(self) -> ApplicationRequestBuilder:
        """
        Provides operations to manage the application property of the microsoft.graph.workbook entity.
        """
        from .application.application_request_builder import ApplicationRequestBuilder

        return ApplicationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def close_session(self) -> CloseSessionRequestBuilder:
        """
        Provides operations to call the closeSession method.
        """
        from .close_session.close_session_request_builder import CloseSessionRequestBuilder

        return CloseSessionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def comments(self) -> CommentsRequestBuilder:
        """
        Provides operations to manage the comments property of the microsoft.graph.workbook entity.
        """
        from .comments.comments_request_builder import CommentsRequestBuilder

        return CommentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def create_session(self) -> CreateSessionRequestBuilder:
        """
        Provides operations to call the createSession method.
        """
        from .create_session.create_session_request_builder import CreateSessionRequestBuilder

        return CreateSessionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def functions(self) -> FunctionsRequestBuilder:
        """
        Provides operations to manage the functions property of the microsoft.graph.workbook entity.
        """
        from .functions.functions_request_builder import FunctionsRequestBuilder

        return FunctionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def names(self) -> NamesRequestBuilder:
        """
        Provides operations to manage the names property of the microsoft.graph.workbook entity.
        """
        from .names.names_request_builder import NamesRequestBuilder

        return NamesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def operations(self) -> OperationsRequestBuilder:
        """
        Provides operations to manage the operations property of the microsoft.graph.workbook entity.
        """
        from .operations.operations_request_builder import OperationsRequestBuilder

        return OperationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def refresh_session(self) -> RefreshSessionRequestBuilder:
        """
        Provides operations to call the refreshSession method.
        """
        from .refresh_session.refresh_session_request_builder import RefreshSessionRequestBuilder

        return RefreshSessionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tables(self) -> TablesRequestBuilder:
        """
        Provides operations to manage the tables property of the microsoft.graph.workbook entity.
        """
        from .tables.tables_request_builder import TablesRequestBuilder

        return TablesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def worksheets(self) -> WorksheetsRequestBuilder:
        """
        Provides operations to manage the worksheets property of the microsoft.graph.workbook entity.
        """
        from .worksheets.worksheets_request_builder import WorksheetsRequestBuilder

        return WorksheetsRequestBuilder(self.request_adapter, self.path_parameters)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class WorkbookRequestBuilderDeleteRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
    @dataclass
    class WorkbookRequestBuilderGetQueryParameters():
        """
        For files that are Excel spreadsheets, accesses the workbook API to work with the spreadsheet's contents. Nullable.
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
    class WorkbookRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[WorkbookRequestBuilder.WorkbookRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class WorkbookRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

