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
    from ....models import managed_e_book
    from ....models.o_data_errors import o_data_error
    from .assign import assign_request_builder
    from .assignments import assignments_request_builder
    from .assignments.item import managed_e_book_assignment_item_request_builder
    from .categories import categories_request_builder
    from .categories.item import managed_e_book_category_item_request_builder
    from .device_states import device_states_request_builder
    from .device_states.item import device_install_state_item_request_builder
    from .install_summary import install_summary_request_builder
    from .user_state_summary import user_state_summary_request_builder
    from .user_state_summary.item import user_install_state_summary_item_request_builder

class ManagedEBookItemRequestBuilder():
    """
    Provides operations to manage the managedEBooks property of the microsoft.graph.deviceAppManagement entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new ManagedEBookItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/deviceAppManagement/managedEBooks/{managedEBook%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def assignments_by_id(self,id: str) -> managed_e_book_assignment_item_request_builder.ManagedEBookAssignmentItemRequestBuilder:
        """
        Provides operations to manage the assignments property of the microsoft.graph.managedEBook entity.
        Args:
            id: Unique identifier of the item
        Returns: managed_e_book_assignment_item_request_builder.ManagedEBookAssignmentItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .assignments.item import managed_e_book_assignment_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["managedEBookAssignment%2Did"] = id
        return managed_e_book_assignment_item_request_builder.ManagedEBookAssignmentItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def categories_by_id(self,id: str) -> managed_e_book_category_item_request_builder.ManagedEBookCategoryItemRequestBuilder:
        """
        Provides operations to manage the categories property of the microsoft.graph.managedEBook entity.
        Args:
            id: Unique identifier of the item
        Returns: managed_e_book_category_item_request_builder.ManagedEBookCategoryItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .categories.item import managed_e_book_category_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["managedEBookCategory%2Did"] = id
        return managed_e_book_category_item_request_builder.ManagedEBookCategoryItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def delete(self,request_configuration: Optional[ManagedEBookItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property managedEBooks for deviceAppManagement
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    def device_states_by_id(self,id: str) -> device_install_state_item_request_builder.DeviceInstallStateItemRequestBuilder:
        """
        Provides operations to manage the deviceStates property of the microsoft.graph.managedEBook entity.
        Args:
            id: Unique identifier of the item
        Returns: device_install_state_item_request_builder.DeviceInstallStateItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .device_states.item import device_install_state_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["deviceInstallState%2Did"] = id
        return device_install_state_item_request_builder.DeviceInstallStateItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[ManagedEBookItemRequestBuilderGetRequestConfiguration] = None) -> Optional[managed_e_book.ManagedEBook]:
        """
        The Managed eBook.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[managed_e_book.ManagedEBook]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models import managed_e_book

        return await self.request_adapter.send_async(request_info, managed_e_book.ManagedEBook, error_mapping)
    
    async def patch(self,body: Optional[managed_e_book.ManagedEBook] = None, request_configuration: Optional[ManagedEBookItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[managed_e_book.ManagedEBook]:
        """
        Update the navigation property managedEBooks in deviceAppManagement
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[managed_e_book.ManagedEBook]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models import managed_e_book

        return await self.request_adapter.send_async(request_info, managed_e_book.ManagedEBook, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[ManagedEBookItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property managedEBooks for deviceAppManagement
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
    
    def to_get_request_information(self,request_configuration: Optional[ManagedEBookItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        The Managed eBook.
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
    
    def to_patch_request_information(self,body: Optional[managed_e_book.ManagedEBook] = None, request_configuration: Optional[ManagedEBookItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property managedEBooks in deviceAppManagement
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
    
    def user_state_summary_by_id(self,id: str) -> user_install_state_summary_item_request_builder.UserInstallStateSummaryItemRequestBuilder:
        """
        Provides operations to manage the userStateSummary property of the microsoft.graph.managedEBook entity.
        Args:
            id: Unique identifier of the item
        Returns: user_install_state_summary_item_request_builder.UserInstallStateSummaryItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .user_state_summary.item import user_install_state_summary_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["userInstallStateSummary%2Did"] = id
        return user_install_state_summary_item_request_builder.UserInstallStateSummaryItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @property
    def assign(self) -> assign_request_builder.AssignRequestBuilder:
        """
        Provides operations to call the assign method.
        """
        from .assign import assign_request_builder

        return assign_request_builder.AssignRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def assignments(self) -> assignments_request_builder.AssignmentsRequestBuilder:
        """
        Provides operations to manage the assignments property of the microsoft.graph.managedEBook entity.
        """
        from .assignments import assignments_request_builder

        return assignments_request_builder.AssignmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def categories(self) -> categories_request_builder.CategoriesRequestBuilder:
        """
        Provides operations to manage the categories property of the microsoft.graph.managedEBook entity.
        """
        from .categories import categories_request_builder

        return categories_request_builder.CategoriesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_states(self) -> device_states_request_builder.DeviceStatesRequestBuilder:
        """
        Provides operations to manage the deviceStates property of the microsoft.graph.managedEBook entity.
        """
        from .device_states import device_states_request_builder

        return device_states_request_builder.DeviceStatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def install_summary(self) -> install_summary_request_builder.InstallSummaryRequestBuilder:
        """
        Provides operations to manage the installSummary property of the microsoft.graph.managedEBook entity.
        """
        from .install_summary import install_summary_request_builder

        return install_summary_request_builder.InstallSummaryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_state_summary(self) -> user_state_summary_request_builder.UserStateSummaryRequestBuilder:
        """
        Provides operations to manage the userStateSummary property of the microsoft.graph.managedEBook entity.
        """
        from .user_state_summary import user_state_summary_request_builder

        return user_state_summary_request_builder.UserStateSummaryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class ManagedEBookItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class ManagedEBookItemRequestBuilderGetQueryParameters():
        """
        The Managed eBook.
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
    class ManagedEBookItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[ManagedEBookItemRequestBuilder.ManagedEBookItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class ManagedEBookItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

