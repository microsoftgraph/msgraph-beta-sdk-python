from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ....models.device_management.alert_record import AlertRecord
    from ....models.device_management.alert_record_collection_response import AlertRecordCollectionResponse
    from ....models.o_data_errors.o_data_error import ODataError
    from .count.count_request_builder import CountRequestBuilder
    from .item.alert_record_item_request_builder import AlertRecordItemRequestBuilder
    from .microsoft_graph_device_management_change_alert_records_portal_notification_as_sent.microsoft_graph_device_management_change_alert_records_portal_notification_as_sent_request_builder import MicrosoftGraphDeviceManagementChangeAlertRecordsPortalNotificationAsSentRequestBuilder
    from .microsoft_graph_device_management_get_portal_notifications.microsoft_graph_device_management_get_portal_notifications_request_builder import MicrosoftGraphDeviceManagementGetPortalNotificationsRequestBuilder

class AlertRecordsRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the alertRecords property of the microsoft.graph.deviceManagement.monitoring entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new AlertRecordsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/deviceManagement/monitoring/alertRecords{?%24count,%24expand,%24filter,%24orderby,%24search,%24select,%24skip,%24top}", path_parameters)
    
    def by_alert_record_id(self,alert_record_id: str) -> AlertRecordItemRequestBuilder:
        """
        Provides operations to manage the alertRecords property of the microsoft.graph.deviceManagement.monitoring entity.
        param alert_record_id: The unique identifier of alertRecord
        Returns: AlertRecordItemRequestBuilder
        """
        if not alert_record_id:
            raise TypeError("alert_record_id cannot be null.")
        from .item.alert_record_item_request_builder import AlertRecordItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["alertRecord%2Did"] = alert_record_id
        return AlertRecordItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration] = None) -> Optional[AlertRecordCollectionResponse]:
        """
        Get a list of the alertRecord objects and their properties.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[AlertRecordCollectionResponse]
        Find more info here: https://learn.microsoft.com/graph/api/devicemanagement-alertrecord-list?view=graph-rest-1.0
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
        from ....models.device_management.alert_record_collection_response import AlertRecordCollectionResponse

        return await self.request_adapter.send_async(request_info, AlertRecordCollectionResponse, error_mapping)
    
    async def post(self,body: Optional[AlertRecord] = None, request_configuration: Optional[RequestConfiguration] = None) -> Optional[AlertRecord]:
        """
        Create new navigation property to alertRecords for deviceManagement
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[AlertRecord]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.device_management.alert_record import AlertRecord

        return await self.request_adapter.send_async(request_info, AlertRecord, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        Get a list of the alertRecord objects and their properties.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: Optional[AlertRecord] = None, request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        Create new navigation property to alertRecords for deviceManagement
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.POST, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> AlertRecordsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: AlertRecordsRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return AlertRecordsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def count(self) -> CountRequestBuilder:
        """
        Provides operations to count the resources in the collection.
        """
        from .count.count_request_builder import CountRequestBuilder

        return CountRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_device_management_change_alert_records_portal_notification_as_sent(self) -> MicrosoftGraphDeviceManagementChangeAlertRecordsPortalNotificationAsSentRequestBuilder:
        """
        Provides operations to call the changeAlertRecordsPortalNotificationAsSent method.
        """
        from .microsoft_graph_device_management_change_alert_records_portal_notification_as_sent.microsoft_graph_device_management_change_alert_records_portal_notification_as_sent_request_builder import MicrosoftGraphDeviceManagementChangeAlertRecordsPortalNotificationAsSentRequestBuilder

        return MicrosoftGraphDeviceManagementChangeAlertRecordsPortalNotificationAsSentRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_device_management_get_portal_notifications(self) -> MicrosoftGraphDeviceManagementGetPortalNotificationsRequestBuilder:
        """
        Provides operations to call the getPortalNotifications method.
        """
        from .microsoft_graph_device_management_get_portal_notifications.microsoft_graph_device_management_get_portal_notifications_request_builder import MicrosoftGraphDeviceManagementGetPortalNotificationsRequestBuilder

        return MicrosoftGraphDeviceManagementGetPortalNotificationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class AlertRecordsRequestBuilderGetQueryParameters():
        """
        Get a list of the alertRecord objects and their properties.
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
                raise TypeError("original_name cannot be null.")
            if original_name == "count":
                return "%24count"
            if original_name == "expand":
                return "%24expand"
            if original_name == "filter":
                return "%24filter"
            if original_name == "orderby":
                return "%24orderby"
            if original_name == "search":
                return "%24search"
            if original_name == "select":
                return "%24select"
            if original_name == "skip":
                return "%24skip"
            if original_name == "top":
                return "%24top"
            return original_name
        
        # Include count of items
        count: Optional[bool] = None

        # Expand related entities
        expand: Optional[List[str]] = None

        # Filter items by property values
        filter: Optional[str] = None

        # Order items by property values
        orderby: Optional[List[str]] = None

        # Search items by search phrases
        search: Optional[str] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

        # Skip the first n items
        skip: Optional[int] = None

        # Show only the first n items
        top: Optional[int] = None

    

