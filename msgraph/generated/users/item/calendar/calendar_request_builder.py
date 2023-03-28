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
    from ....models import calendar
    from ....models.o_data_errors import o_data_error
    from .allowed_calendar_sharing_roles_with_user import allowed_calendar_sharing_roles_with_user_request_builder
    from .calendar_permissions import calendar_permissions_request_builder
    from .calendar_permissions.item import calendar_permission_item_request_builder
    from .calendar_view import calendar_view_request_builder
    from .calendar_view.item import event_item_request_builder
    from .events import events_request_builder
    from .events.item import event_item_request_builder
    from .get_schedule import get_schedule_request_builder
    from .multi_value_extended_properties import multi_value_extended_properties_request_builder
    from .multi_value_extended_properties.item import multi_value_legacy_extended_property_item_request_builder
    from .single_value_extended_properties import single_value_extended_properties_request_builder
    from .single_value_extended_properties.item import single_value_legacy_extended_property_item_request_builder

class CalendarRequestBuilder():
    """
    Provides operations to manage the calendar property of the microsoft.graph.user entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new CalendarRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/users/{user%2Did}/calendar{?%24select}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def allowed_calendar_sharing_roles_with_user(self,user: Optional[str] = None) -> allowed_calendar_sharing_roles_with_user_request_builder.AllowedCalendarSharingRolesWithUserRequestBuilder:
        """
        Provides operations to call the allowedCalendarSharingRoles method.
        Args:
            User: Usage: User='{User}'
        Returns: allowed_calendar_sharing_roles_with_user_request_builder.AllowedCalendarSharingRolesWithUserRequestBuilder
        """
        if user is None:
            raise Exception("user cannot be undefined")
        from .allowed_calendar_sharing_roles_with_user import allowed_calendar_sharing_roles_with_user_request_builder

        return allowed_calendar_sharing_roles_with_user_request_builder.AllowedCalendarSharingRolesWithUserRequestBuilder(self.request_adapter, self.path_parameters, user)
    
    def calendar_permissions_by_id(self,id: str) -> calendar_permission_item_request_builder.CalendarPermissionItemRequestBuilder:
        """
        Provides operations to manage the calendarPermissions property of the microsoft.graph.calendar entity.
        Args:
            id: Unique identifier of the item
        Returns: calendar_permission_item_request_builder.CalendarPermissionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .calendar_permissions.item import calendar_permission_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["calendarPermission%2Did"] = id
        return calendar_permission_item_request_builder.CalendarPermissionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def calendar_view_by_id(self,id: str) -> event_item_request_builder.EventItemRequestBuilder:
        """
        Provides operations to manage the calendarView property of the microsoft.graph.calendar entity.
        Args:
            id: Unique identifier of the item
        Returns: event_item_request_builder.EventItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .calendar_view.item import event_item_request_builder
        from .events.item import event_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["event%2Did"] = id
        return event_item_request_builder.EventItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def events_by_id(self,id: str) -> event_item_request_builder.EventItemRequestBuilder:
        """
        Provides operations to manage the events property of the microsoft.graph.calendar entity.
        Args:
            id: Unique identifier of the item
        Returns: event_item_request_builder.EventItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .calendar_view.item import event_item_request_builder
        from .events.item import event_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["event%2Did"] = id
        return event_item_request_builder.EventItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[CalendarRequestBuilderGetRequestConfiguration] = None) -> Optional[calendar.Calendar]:
        """
        Get the properties and relationships of a calendar object. The calendar can be one for a user, or the default calendar of a Microsoft 365 group. There are two scenarios where an app can get another user's calendar:
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[calendar.Calendar]
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
        from ....models import calendar

        return await self.request_adapter.send_async(request_info, calendar.Calendar, error_mapping)
    
    def multi_value_extended_properties_by_id(self,id: str) -> multi_value_legacy_extended_property_item_request_builder.MultiValueLegacyExtendedPropertyItemRequestBuilder:
        """
        Provides operations to manage the multiValueExtendedProperties property of the microsoft.graph.calendar entity.
        Args:
            id: Unique identifier of the item
        Returns: multi_value_legacy_extended_property_item_request_builder.MultiValueLegacyExtendedPropertyItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .multi_value_extended_properties.item import multi_value_legacy_extended_property_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["multiValueLegacyExtendedProperty%2Did"] = id
        return multi_value_legacy_extended_property_item_request_builder.MultiValueLegacyExtendedPropertyItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def patch(self,body: Optional[calendar.Calendar] = None, request_configuration: Optional[CalendarRequestBuilderPatchRequestConfiguration] = None) -> Optional[calendar.Calendar]:
        """
        Update the properties of a calendar object. The calendar can be one for a user, or the default calendar of a Microsoft 365 group.
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[calendar.Calendar]
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
        from ....models import calendar

        return await self.request_adapter.send_async(request_info, calendar.Calendar, error_mapping)
    
    def single_value_extended_properties_by_id(self,id: str) -> single_value_legacy_extended_property_item_request_builder.SingleValueLegacyExtendedPropertyItemRequestBuilder:
        """
        Provides operations to manage the singleValueExtendedProperties property of the microsoft.graph.calendar entity.
        Args:
            id: Unique identifier of the item
        Returns: single_value_legacy_extended_property_item_request_builder.SingleValueLegacyExtendedPropertyItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .single_value_extended_properties.item import single_value_legacy_extended_property_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["singleValueLegacyExtendedProperty%2Did"] = id
        return single_value_legacy_extended_property_item_request_builder.SingleValueLegacyExtendedPropertyItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def to_get_request_information(self,request_configuration: Optional[CalendarRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get the properties and relationships of a calendar object. The calendar can be one for a user, or the default calendar of a Microsoft 365 group. There are two scenarios where an app can get another user's calendar:
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
    
    def to_patch_request_information(self,body: Optional[calendar.Calendar] = None, request_configuration: Optional[CalendarRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the properties of a calendar object. The calendar can be one for a user, or the default calendar of a Microsoft 365 group.
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
    def calendar_permissions(self) -> calendar_permissions_request_builder.CalendarPermissionsRequestBuilder:
        """
        Provides operations to manage the calendarPermissions property of the microsoft.graph.calendar entity.
        """
        from .calendar_permissions import calendar_permissions_request_builder

        return calendar_permissions_request_builder.CalendarPermissionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def calendar_view(self) -> calendar_view_request_builder.CalendarViewRequestBuilder:
        """
        Provides operations to manage the calendarView property of the microsoft.graph.calendar entity.
        """
        from .calendar_view import calendar_view_request_builder

        return calendar_view_request_builder.CalendarViewRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def events(self) -> events_request_builder.EventsRequestBuilder:
        """
        Provides operations to manage the events property of the microsoft.graph.calendar entity.
        """
        from .events import events_request_builder

        return events_request_builder.EventsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_schedule(self) -> get_schedule_request_builder.GetScheduleRequestBuilder:
        """
        Provides operations to call the getSchedule method.
        """
        from .get_schedule import get_schedule_request_builder

        return get_schedule_request_builder.GetScheduleRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def multi_value_extended_properties(self) -> multi_value_extended_properties_request_builder.MultiValueExtendedPropertiesRequestBuilder:
        """
        Provides operations to manage the multiValueExtendedProperties property of the microsoft.graph.calendar entity.
        """
        from .multi_value_extended_properties import multi_value_extended_properties_request_builder

        return multi_value_extended_properties_request_builder.MultiValueExtendedPropertiesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def single_value_extended_properties(self) -> single_value_extended_properties_request_builder.SingleValueExtendedPropertiesRequestBuilder:
        """
        Provides operations to manage the singleValueExtendedProperties property of the microsoft.graph.calendar entity.
        """
        from .single_value_extended_properties import single_value_extended_properties_request_builder

        return single_value_extended_properties_request_builder.SingleValueExtendedPropertiesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class CalendarRequestBuilderGetQueryParameters():
        """
        Get the properties and relationships of a calendar object. The calendar can be one for a user, or the default calendar of a Microsoft 365 group. There are two scenarios where an app can get another user's calendar:
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
            if original_name == "select":
                return "%24select"
            return original_name
        
        # Select properties to be returned
        select: Optional[List[str]] = None

    
    @dataclass
    class CalendarRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[CalendarRequestBuilder.CalendarRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class CalendarRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

