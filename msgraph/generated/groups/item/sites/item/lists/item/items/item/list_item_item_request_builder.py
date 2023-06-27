from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .........models.list_item import ListItem
    from .........models.o_data_errors.o_data_error import ODataError
    from .activities.activities_request_builder import ActivitiesRequestBuilder
    from .analytics.analytics_request_builder import AnalyticsRequestBuilder
    from .created_by_user.created_by_user_request_builder import CreatedByUserRequestBuilder
    from .create_link.create_link_request_builder import CreateLinkRequestBuilder
    from .document_set_versions.document_set_versions_request_builder import DocumentSetVersionsRequestBuilder
    from .drive_item.drive_item_request_builder import DriveItemRequestBuilder
    from .fields.fields_request_builder import FieldsRequestBuilder
    from .get_activities_by_interval_with_start_date_time_with_end_date_time_with_interval.get_activities_by_interval_with_start_date_time_with_end_date_time_with_interval_request_builder import GetActivitiesByIntervalWithStartDateTimeWithEndDateTimeWithIntervalRequestBuilder
    from .last_modified_by_user.last_modified_by_user_request_builder import LastModifiedByUserRequestBuilder
    from .versions.versions_request_builder import VersionsRequestBuilder

class ListItemItemRequestBuilder():
    """
    Provides operations to manage the items property of the microsoft.graph.list entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new ListItemItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if not path_parameters:
            raise TypeError("path_parameters cannot be null.")
        if not request_adapter:
            raise TypeError("request_adapter cannot be null.")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/groups/{group%2Did}/sites/{site%2Did}/lists/{list%2Did}/items/{listItem%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[ListItemItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Removes an item from a [list][].
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .........models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[ListItemItemRequestBuilderGetRequestConfiguration] = None) -> Optional[ListItem]:
        """
        Returns the metadata for an [item][] in a [list][].
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ListItem]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .........models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .........models.list_item import ListItem

        return await self.request_adapter.send_async(request_info, ListItem, error_mapping)
    
    def get_activities_by_interval_with_start_date_time_with_end_date_time_with_interval(self,end_date_time: Optional[str] = None, interval: Optional[str] = None, start_date_time: Optional[str] = None) -> GetActivitiesByIntervalWithStartDateTimeWithEndDateTimeWithIntervalRequestBuilder:
        """
        Provides operations to call the getActivitiesByInterval method.
        Args:
            endDateTime: Usage: endDateTime='{endDateTime}'
            interval: Usage: interval='{interval}'
            startDateTime: Usage: startDateTime='{startDateTime}'
        Returns: GetActivitiesByIntervalWithStartDateTimeWithEndDateTimeWithIntervalRequestBuilder
        """
        if not end_date_time:
            raise TypeError("end_date_time cannot be null.")
        if not interval:
            raise TypeError("interval cannot be null.")
        if not start_date_time:
            raise TypeError("start_date_time cannot be null.")
        from .get_activities_by_interval_with_start_date_time_with_end_date_time_with_interval.get_activities_by_interval_with_start_date_time_with_end_date_time_with_interval_request_builder import GetActivitiesByIntervalWithStartDateTimeWithEndDateTimeWithIntervalRequestBuilder

        return GetActivitiesByIntervalWithStartDateTimeWithEndDateTimeWithIntervalRequestBuilder(self.request_adapter, self.path_parameters, end_date_time, interval, start_date_time)
    
    async def patch(self,body: Optional[ListItem] = None, request_configuration: Optional[ListItemItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[ListItem]:
        """
        Update the navigation property items in groups
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ListItem]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from .........models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .........models.list_item import ListItem

        return await self.request_adapter.send_async(request_info, ListItem, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[ListItemItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Removes an item from a [list][].
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
    
    def to_get_request_information(self,request_configuration: Optional[ListItemItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Returns the metadata for an [item][] in a [list][].
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
    
    def to_patch_request_information(self,body: Optional[ListItem] = None, request_configuration: Optional[ListItemItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property items in groups
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
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
    def activities(self) -> ActivitiesRequestBuilder:
        """
        Provides operations to manage the activities property of the microsoft.graph.listItem entity.
        """
        from .activities.activities_request_builder import ActivitiesRequestBuilder

        return ActivitiesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def analytics(self) -> AnalyticsRequestBuilder:
        """
        Provides operations to manage the analytics property of the microsoft.graph.listItem entity.
        """
        from .analytics.analytics_request_builder import AnalyticsRequestBuilder

        return AnalyticsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def created_by_user(self) -> CreatedByUserRequestBuilder:
        """
        Provides operations to manage the createdByUser property of the microsoft.graph.baseItem entity.
        """
        from .created_by_user.created_by_user_request_builder import CreatedByUserRequestBuilder

        return CreatedByUserRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def create_link(self) -> CreateLinkRequestBuilder:
        """
        Provides operations to call the createLink method.
        """
        from .create_link.create_link_request_builder import CreateLinkRequestBuilder

        return CreateLinkRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def document_set_versions(self) -> DocumentSetVersionsRequestBuilder:
        """
        Provides operations to manage the documentSetVersions property of the microsoft.graph.listItem entity.
        """
        from .document_set_versions.document_set_versions_request_builder import DocumentSetVersionsRequestBuilder

        return DocumentSetVersionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def drive_item(self) -> DriveItemRequestBuilder:
        """
        Provides operations to manage the driveItem property of the microsoft.graph.listItem entity.
        """
        from .drive_item.drive_item_request_builder import DriveItemRequestBuilder

        return DriveItemRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def fields(self) -> FieldsRequestBuilder:
        """
        Provides operations to manage the fields property of the microsoft.graph.listItem entity.
        """
        from .fields.fields_request_builder import FieldsRequestBuilder

        return FieldsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def last_modified_by_user(self) -> LastModifiedByUserRequestBuilder:
        """
        Provides operations to manage the lastModifiedByUser property of the microsoft.graph.baseItem entity.
        """
        from .last_modified_by_user.last_modified_by_user_request_builder import LastModifiedByUserRequestBuilder

        return LastModifiedByUserRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def versions(self) -> VersionsRequestBuilder:
        """
        Provides operations to manage the versions property of the microsoft.graph.listItem entity.
        """
        from .versions.versions_request_builder import VersionsRequestBuilder

        return VersionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class ListItemItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class ListItemItemRequestBuilderGetQueryParameters():
        """
        Returns the metadata for an [item][] in a [list][].
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            Args:
                originalName: The original query parameter name in the class.
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

    
    @dataclass
    class ListItemItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[ListItemItemRequestBuilder.ListItemItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class ListItemItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

