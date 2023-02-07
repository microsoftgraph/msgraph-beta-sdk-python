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

user_settings = lazy_import('msgraph.generated.models.user_settings')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')
contact_merge_suggestions_request_builder = lazy_import('msgraph.generated.users.item.settings.contact_merge_suggestions.contact_merge_suggestions_request_builder')
item_insights_request_builder = lazy_import('msgraph.generated.users.item.settings.item_insights.item_insights_request_builder')
regional_and_language_settings_request_builder = lazy_import('msgraph.generated.users.item.settings.regional_and_language_settings.regional_and_language_settings_request_builder')
shift_preferences_request_builder = lazy_import('msgraph.generated.users.item.settings.shift_preferences.shift_preferences_request_builder')

class SettingsRequestBuilder():
    """
    Provides operations to manage the settings property of the microsoft.graph.user entity.
    """
    @property
    def contact_merge_suggestions(self) -> contact_merge_suggestions_request_builder.ContactMergeSuggestionsRequestBuilder:
        """
        Provides operations to manage the contactMergeSuggestions property of the microsoft.graph.userSettings entity.
        """
        return contact_merge_suggestions_request_builder.ContactMergeSuggestionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def item_insights(self) -> item_insights_request_builder.ItemInsightsRequestBuilder:
        """
        Provides operations to manage the itemInsights property of the microsoft.graph.userSettings entity.
        """
        return item_insights_request_builder.ItemInsightsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def regional_and_language_settings(self) -> regional_and_language_settings_request_builder.RegionalAndLanguageSettingsRequestBuilder:
        """
        Provides operations to manage the regionalAndLanguageSettings property of the microsoft.graph.userSettings entity.
        """
        return regional_and_language_settings_request_builder.RegionalAndLanguageSettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def shift_preferences(self) -> shift_preferences_request_builder.ShiftPreferencesRequestBuilder:
        """
        Provides operations to manage the shiftPreferences property of the microsoft.graph.userSettings entity.
        """
        return shift_preferences_request_builder.ShiftPreferencesRequestBuilder(self.request_adapter, self.path_parameters)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new SettingsRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/users/{user%2Did}/settings{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[SettingsRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property settings for users
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
    
    async def get(self,request_configuration: Optional[SettingsRequestBuilderGetRequestConfiguration] = None) -> Optional[user_settings.UserSettings]:
        """
        Get settings from users
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[user_settings.UserSettings]
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
        return await self.request_adapter.send_async(request_info, user_settings.UserSettings, error_mapping)
    
    async def patch(self,body: Optional[user_settings.UserSettings] = None, request_configuration: Optional[SettingsRequestBuilderPatchRequestConfiguration] = None) -> Optional[user_settings.UserSettings]:
        """
        Update the navigation property settings in users
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[user_settings.UserSettings]
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
        return await self.request_adapter.send_async(request_info, user_settings.UserSettings, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[SettingsRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property settings for users
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
    
    def to_get_request_information(self,request_configuration: Optional[SettingsRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get settings from users
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
    
    def to_patch_request_information(self,body: Optional[user_settings.UserSettings] = None, request_configuration: Optional[SettingsRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property settings in users
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
    
    @dataclass
    class SettingsRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class SettingsRequestBuilderGetQueryParameters():
        """
        Get settings from users
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
    class SettingsRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[SettingsRequestBuilder.SettingsRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class SettingsRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

