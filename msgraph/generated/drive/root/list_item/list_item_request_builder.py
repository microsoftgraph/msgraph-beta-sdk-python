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

activities_request_builder = lazy_import('msgraph.generated.drive.root.list_item.activities.activities_request_builder')
item_activity_o_l_d_item_request_builder = lazy_import('msgraph.generated.drive.root.list_item.activities.item.item_activity_o_l_d_item_request_builder')
analytics_request_builder = lazy_import('msgraph.generated.drive.root.list_item.analytics.analytics_request_builder')
create_link_request_builder = lazy_import('msgraph.generated.drive.root.list_item.create_link.create_link_request_builder')
document_set_versions_request_builder = lazy_import('msgraph.generated.drive.root.list_item.document_set_versions.document_set_versions_request_builder')
document_set_version_item_request_builder = lazy_import('msgraph.generated.drive.root.list_item.document_set_versions.item.document_set_version_item_request_builder')
drive_item_request_builder = lazy_import('msgraph.generated.drive.root.list_item.drive_item.drive_item_request_builder')
fields_request_builder = lazy_import('msgraph.generated.drive.root.list_item.fields.fields_request_builder')
get_activities_by_interval_with_start_date_time_with_end_date_time_with_interval_request_builder = lazy_import('msgraph.generated.drive.root.list_item.get_activities_by_interval_with_start_date_time_with_end_date_time_with_interval.get_activities_by_interval_with_start_date_time_with_end_date_time_with_interval_request_builder')
versions_request_builder = lazy_import('msgraph.generated.drive.root.list_item.versions.versions_request_builder')
list_item_version_item_request_builder = lazy_import('msgraph.generated.drive.root.list_item.versions.item.list_item_version_item_request_builder')
list_item = lazy_import('msgraph.generated.models.list_item')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class ListItemRequestBuilder():
    """
    Provides operations to manage the listItem property of the microsoft.graph.driveItem entity.
    """
    @property
    def activities(self) -> activities_request_builder.ActivitiesRequestBuilder:
        """
        Provides operations to manage the activities property of the microsoft.graph.listItem entity.
        """
        return activities_request_builder.ActivitiesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def analytics(self) -> analytics_request_builder.AnalyticsRequestBuilder:
        """
        Provides operations to manage the analytics property of the microsoft.graph.listItem entity.
        """
        return analytics_request_builder.AnalyticsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def create_link(self) -> create_link_request_builder.CreateLinkRequestBuilder:
        """
        Provides operations to call the createLink method.
        """
        return create_link_request_builder.CreateLinkRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def document_set_versions(self) -> document_set_versions_request_builder.DocumentSetVersionsRequestBuilder:
        """
        Provides operations to manage the documentSetVersions property of the microsoft.graph.listItem entity.
        """
        return document_set_versions_request_builder.DocumentSetVersionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def drive_item(self) -> drive_item_request_builder.DriveItemRequestBuilder:
        """
        Provides operations to manage the driveItem property of the microsoft.graph.listItem entity.
        """
        return drive_item_request_builder.DriveItemRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def fields(self) -> fields_request_builder.FieldsRequestBuilder:
        """
        Provides operations to manage the fields property of the microsoft.graph.listItem entity.
        """
        return fields_request_builder.FieldsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def versions(self) -> versions_request_builder.VersionsRequestBuilder:
        """
        Provides operations to manage the versions property of the microsoft.graph.listItem entity.
        """
        return versions_request_builder.VersionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def activities_by_id(self,id: str) -> item_activity_o_l_d_item_request_builder.ItemActivityOLDItemRequestBuilder:
        """
        Provides operations to manage the activities property of the microsoft.graph.listItem entity.
        Args:
            id: Unique identifier of the item
        Returns: item_activity_o_l_d_item_request_builder.ItemActivityOLDItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["itemActivityOLD%2Did"] = id
        return item_activity_o_l_d_item_request_builder.ItemActivityOLDItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new ListItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/drive/root/listItem{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[ListItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property listItem for drive
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
    
    def document_set_versions_by_id(self,id: str) -> document_set_version_item_request_builder.DocumentSetVersionItemRequestBuilder:
        """
        Provides operations to manage the documentSetVersions property of the microsoft.graph.listItem entity.
        Args:
            id: Unique identifier of the item
        Returns: document_set_version_item_request_builder.DocumentSetVersionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["documentSetVersion%2Did"] = id
        return document_set_version_item_request_builder.DocumentSetVersionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[ListItemRequestBuilderGetRequestConfiguration] = None) -> Optional[list_item.ListItem]:
        """
        For drives in SharePoint, the associated document library list item. Read-only. Nullable.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[list_item.ListItem]
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
        return await self.request_adapter.send_async(request_info, list_item.ListItem, error_mapping)
    
    def get_activities_by_interval_with_start_date_time_with_end_date_time_with_interval(self,end_date_time: Optional[str] = None, interval: Optional[str] = None, start_date_time: Optional[str] = None) -> get_activities_by_interval_with_start_date_time_with_end_date_time_with_interval_request_builder.GetActivitiesByIntervalWithStartDateTimeWithEndDateTimeWithIntervalRequestBuilder:
        """
        Provides operations to call the getActivitiesByInterval method.
        Args:
            endDateTime: Usage: endDateTime='{endDateTime}'
            interval: Usage: interval='{interval}'
            startDateTime: Usage: startDateTime='{startDateTime}'
        Returns: get_activities_by_interval_with_start_date_time_with_end_date_time_with_interval_request_builder.GetActivitiesByIntervalWithStartDateTimeWithEndDateTimeWithIntervalRequestBuilder
        """
        if end_date_time is None:
            raise Exception("end_date_time cannot be undefined")
        if interval is None:
            raise Exception("interval cannot be undefined")
        if start_date_time is None:
            raise Exception("start_date_time cannot be undefined")
        return get_activities_by_interval_with_start_date_time_with_end_date_time_with_interval_request_builder.GetActivitiesByIntervalWithStartDateTimeWithEndDateTimeWithIntervalRequestBuilder(self.request_adapter, self.path_parameters, endDateTime, interval, startDateTime)
    
    async def patch(self,body: Optional[list_item.ListItem] = None, request_configuration: Optional[ListItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[list_item.ListItem]:
        """
        Update the navigation property listItem in drive
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[list_item.ListItem]
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
        return await self.request_adapter.send_async(request_info, list_item.ListItem, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[ListItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property listItem for drive
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
    
    def to_get_request_information(self,request_configuration: Optional[ListItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        For drives in SharePoint, the associated document library list item. Read-only. Nullable.
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
    
    def to_patch_request_information(self,body: Optional[list_item.ListItem] = None, request_configuration: Optional[ListItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property listItem in drive
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
    
    def versions_by_id(self,id: str) -> list_item_version_item_request_builder.ListItemVersionItemRequestBuilder:
        """
        Provides operations to manage the versions property of the microsoft.graph.listItem entity.
        Args:
            id: Unique identifier of the item
        Returns: list_item_version_item_request_builder.ListItemVersionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["listItemVersion%2Did"] = id
        return list_item_version_item_request_builder.ListItemVersionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @dataclass
    class ListItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class ListItemRequestBuilderGetQueryParameters():
        """
        For drives in SharePoint, the associated document library list item. Read-only. Nullable.
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
    class ListItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[ListItemRequestBuilder.ListItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class ListItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

