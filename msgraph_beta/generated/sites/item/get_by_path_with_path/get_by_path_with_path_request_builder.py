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
    from ....models.o_data_errors.o_data_error import ODataError
    from ....models.site import Site
    from .analytics.analytics_request_builder import AnalyticsRequestBuilder
    from .columns.columns_request_builder import ColumnsRequestBuilder
    from .content_types.content_types_request_builder import ContentTypesRequestBuilder
    from .created_by_user.created_by_user_request_builder import CreatedByUserRequestBuilder
    from .drive.drive_request_builder import DriveRequestBuilder
    from .drives.drives_request_builder import DrivesRequestBuilder
    from .external_columns.external_columns_request_builder import ExternalColumnsRequestBuilder
    from .get_activities_by_interval_with_start_date_time_with_end_date_time_with_interval.get_activities_by_interval_with_start_date_time_with_end_date_time_with_interval_request_builder import GetActivitiesByIntervalWithStartDateTimeWithEndDateTimeWithIntervalRequestBuilder
    from .get_applicable_content_types_for_list_with_list_id.get_applicable_content_types_for_list_with_list_id_request_builder import GetApplicableContentTypesForListWithListIdRequestBuilder
    from .get_by_path_with_path1.get_by_path_with_path1_request_builder import GetByPathWithPath1RequestBuilder
    from .information_protection.information_protection_request_builder import InformationProtectionRequestBuilder
    from .items.items_request_builder import ItemsRequestBuilder
    from .last_modified_by_user.last_modified_by_user_request_builder import LastModifiedByUserRequestBuilder
    from .lists.lists_request_builder import ListsRequestBuilder
    from .onenote.onenote_request_builder import OnenoteRequestBuilder
    from .operations.operations_request_builder import OperationsRequestBuilder
    from .pages.pages_request_builder import PagesRequestBuilder
    from .permissions.permissions_request_builder import PermissionsRequestBuilder
    from .recycle_bin.recycle_bin_request_builder import RecycleBinRequestBuilder
    from .sites.sites_request_builder import SitesRequestBuilder
    from .term_store.term_store_request_builder import TermStoreRequestBuilder

class GetByPathWithPathRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to call the getByPath method.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]], path: Optional[str] = None) -> None:
        """
        Instantiates a new GetByPathWithPathRequestBuilder and sets the default values.
        param path: Usage: path='{path}'
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        if isinstance(path_parameters, dict):
            path_parameters['path'] = str(path)
        super().__init__(request_adapter, "{+baseurl}/sites/{site%2Did}/getByPath(path='{path}')", path_parameters)
    
    async def get(self,request_configuration: Optional[GetByPathWithPathRequestBuilderGetRequestConfiguration] = None) -> Optional[Site]:
        """
        Invoke function getByPath
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Site]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.site import Site

        return await self.request_adapter.send_async(request_info, Site, error_mapping)
    
    def get_activities_by_interval_with_start_date_time_with_end_date_time_with_interval(self,end_date_time: Optional[str] = None, interval: Optional[str] = None, start_date_time: Optional[str] = None) -> GetActivitiesByIntervalWithStartDateTimeWithEndDateTimeWithIntervalRequestBuilder:
        """
        Provides operations to call the getActivitiesByInterval method.
        param end_date_time: Usage: endDateTime='{endDateTime}'
        param interval: Usage: interval='{interval}'
        param start_date_time: Usage: startDateTime='{startDateTime}'
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
    
    def get_applicable_content_types_for_list_with_list_id(self,list_id: Optional[str] = None) -> GetApplicableContentTypesForListWithListIdRequestBuilder:
        """
        Provides operations to call the getApplicableContentTypesForList method.
        param list_id: Usage: listId='{listId}'
        Returns: GetApplicableContentTypesForListWithListIdRequestBuilder
        """
        if not list_id:
            raise TypeError("list_id cannot be null.")
        from .get_applicable_content_types_for_list_with_list_id.get_applicable_content_types_for_list_with_list_id_request_builder import GetApplicableContentTypesForListWithListIdRequestBuilder

        return GetApplicableContentTypesForListWithListIdRequestBuilder(self.request_adapter, self.path_parameters, list_id)
    
    def get_by_path_with_path1(self,path1: Optional[str] = None) -> GetByPathWithPath1RequestBuilder:
        """
        Provides operations to call the getByPath method.
        param path1: Usage: path='{path1}'
        Returns: GetByPathWithPath1RequestBuilder
        """
        if not path1:
            raise TypeError("path1 cannot be null.")
        from .get_by_path_with_path1.get_by_path_with_path1_request_builder import GetByPathWithPath1RequestBuilder

        return GetByPathWithPath1RequestBuilder(self.request_adapter, self.path_parameters, path1)
    
    def to_get_request_information(self,request_configuration: Optional[GetByPathWithPathRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Invoke function getByPath
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> GetByPathWithPathRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: GetByPathWithPathRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return GetByPathWithPathRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def analytics(self) -> AnalyticsRequestBuilder:
        """
        Provides operations to manage the analytics property of the microsoft.graph.site entity.
        """
        from .analytics.analytics_request_builder import AnalyticsRequestBuilder

        return AnalyticsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def columns(self) -> ColumnsRequestBuilder:
        """
        Provides operations to manage the columns property of the microsoft.graph.site entity.
        """
        from .columns.columns_request_builder import ColumnsRequestBuilder

        return ColumnsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def content_types(self) -> ContentTypesRequestBuilder:
        """
        Provides operations to manage the contentTypes property of the microsoft.graph.site entity.
        """
        from .content_types.content_types_request_builder import ContentTypesRequestBuilder

        return ContentTypesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def created_by_user(self) -> CreatedByUserRequestBuilder:
        """
        Provides operations to manage the createdByUser property of the microsoft.graph.baseItem entity.
        """
        from .created_by_user.created_by_user_request_builder import CreatedByUserRequestBuilder

        return CreatedByUserRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def drive(self) -> DriveRequestBuilder:
        """
        Provides operations to manage the drive property of the microsoft.graph.site entity.
        """
        from .drive.drive_request_builder import DriveRequestBuilder

        return DriveRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def drives(self) -> DrivesRequestBuilder:
        """
        Provides operations to manage the drives property of the microsoft.graph.site entity.
        """
        from .drives.drives_request_builder import DrivesRequestBuilder

        return DrivesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def external_columns(self) -> ExternalColumnsRequestBuilder:
        """
        Provides operations to manage the externalColumns property of the microsoft.graph.site entity.
        """
        from .external_columns.external_columns_request_builder import ExternalColumnsRequestBuilder

        return ExternalColumnsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def information_protection(self) -> InformationProtectionRequestBuilder:
        """
        Provides operations to manage the informationProtection property of the microsoft.graph.site entity.
        """
        from .information_protection.information_protection_request_builder import InformationProtectionRequestBuilder

        return InformationProtectionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def items(self) -> ItemsRequestBuilder:
        """
        Provides operations to manage the items property of the microsoft.graph.site entity.
        """
        from .items.items_request_builder import ItemsRequestBuilder

        return ItemsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def last_modified_by_user(self) -> LastModifiedByUserRequestBuilder:
        """
        Provides operations to manage the lastModifiedByUser property of the microsoft.graph.baseItem entity.
        """
        from .last_modified_by_user.last_modified_by_user_request_builder import LastModifiedByUserRequestBuilder

        return LastModifiedByUserRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def lists(self) -> ListsRequestBuilder:
        """
        Provides operations to manage the lists property of the microsoft.graph.site entity.
        """
        from .lists.lists_request_builder import ListsRequestBuilder

        return ListsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def onenote(self) -> OnenoteRequestBuilder:
        """
        Provides operations to manage the onenote property of the microsoft.graph.site entity.
        """
        from .onenote.onenote_request_builder import OnenoteRequestBuilder

        return OnenoteRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def operations(self) -> OperationsRequestBuilder:
        """
        Provides operations to manage the operations property of the microsoft.graph.site entity.
        """
        from .operations.operations_request_builder import OperationsRequestBuilder

        return OperationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def pages(self) -> PagesRequestBuilder:
        """
        Provides operations to manage the pages property of the microsoft.graph.site entity.
        """
        from .pages.pages_request_builder import PagesRequestBuilder

        return PagesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def permissions(self) -> PermissionsRequestBuilder:
        """
        Provides operations to manage the permissions property of the microsoft.graph.site entity.
        """
        from .permissions.permissions_request_builder import PermissionsRequestBuilder

        return PermissionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def recycle_bin(self) -> RecycleBinRequestBuilder:
        """
        Provides operations to manage the recycleBin property of the microsoft.graph.site entity.
        """
        from .recycle_bin.recycle_bin_request_builder import RecycleBinRequestBuilder

        return RecycleBinRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sites(self) -> SitesRequestBuilder:
        """
        Provides operations to manage the sites property of the microsoft.graph.site entity.
        """
        from .sites.sites_request_builder import SitesRequestBuilder

        return SitesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def term_store(self) -> TermStoreRequestBuilder:
        """
        Provides operations to manage the termStore property of the microsoft.graph.site entity.
        """
        from .term_store.term_store_request_builder import TermStoreRequestBuilder

        return TermStoreRequestBuilder(self.request_adapter, self.path_parameters)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class GetByPathWithPathRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

