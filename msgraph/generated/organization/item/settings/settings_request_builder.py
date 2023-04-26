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
    from ....models import organization_settings
    from ....models.o_data_errors import o_data_error
    from .contact_insights import contact_insights_request_builder
    from .item_insights import item_insights_request_builder
    from .microsoft_application_data_access import microsoft_application_data_access_request_builder
    from .people_insights import people_insights_request_builder
    from .profile_card_properties import profile_card_properties_request_builder
    from .pronouns import pronouns_request_builder

class SettingsRequestBuilder():
    """
    Provides operations to manage the settings property of the microsoft.graph.organization entity.
    """
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
        self.url_template: str = "{+baseurl}/organization/{organization%2Did}/settings{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[SettingsRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property settings for organization
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
    
    async def get(self,request_configuration: Optional[SettingsRequestBuilderGetRequestConfiguration] = None) -> Optional[organization_settings.OrganizationSettings]:
        """
        Retrieve the properties and relationships of organizationSettings object. Nullable.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[organization_settings.OrganizationSettings]
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
        from ....models import organization_settings

        return await self.request_adapter.send_async(request_info, organization_settings.OrganizationSettings, error_mapping)
    
    async def patch(self,body: Optional[organization_settings.OrganizationSettings] = None, request_configuration: Optional[SettingsRequestBuilderPatchRequestConfiguration] = None) -> Optional[organization_settings.OrganizationSettings]:
        """
        Update the navigation property settings in organization
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[organization_settings.OrganizationSettings]
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
        from ....models import organization_settings

        return await self.request_adapter.send_async(request_info, organization_settings.OrganizationSettings, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[SettingsRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property settings for organization
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
        Retrieve the properties and relationships of organizationSettings object. Nullable.
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
    
    def to_patch_request_information(self,body: Optional[organization_settings.OrganizationSettings] = None, request_configuration: Optional[SettingsRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property settings in organization
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
    def contact_insights(self) -> contact_insights_request_builder.ContactInsightsRequestBuilder:
        """
        Provides operations to manage the contactInsights property of the microsoft.graph.organizationSettings entity.
        """
        from .contact_insights import contact_insights_request_builder

        return contact_insights_request_builder.ContactInsightsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def item_insights(self) -> item_insights_request_builder.ItemInsightsRequestBuilder:
        """
        Provides operations to manage the itemInsights property of the microsoft.graph.organizationSettings entity.
        """
        from .item_insights import item_insights_request_builder

        return item_insights_request_builder.ItemInsightsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_application_data_access(self) -> microsoft_application_data_access_request_builder.MicrosoftApplicationDataAccessRequestBuilder:
        """
        Provides operations to manage the microsoftApplicationDataAccess property of the microsoft.graph.organizationSettings entity.
        """
        from .microsoft_application_data_access import microsoft_application_data_access_request_builder

        return microsoft_application_data_access_request_builder.MicrosoftApplicationDataAccessRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def people_insights(self) -> people_insights_request_builder.PeopleInsightsRequestBuilder:
        """
        Provides operations to manage the peopleInsights property of the microsoft.graph.organizationSettings entity.
        """
        from .people_insights import people_insights_request_builder

        return people_insights_request_builder.PeopleInsightsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def profile_card_properties(self) -> profile_card_properties_request_builder.ProfileCardPropertiesRequestBuilder:
        """
        Provides operations to manage the profileCardProperties property of the microsoft.graph.organizationSettings entity.
        """
        from .profile_card_properties import profile_card_properties_request_builder

        return profile_card_properties_request_builder.ProfileCardPropertiesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def pronouns(self) -> pronouns_request_builder.PronounsRequestBuilder:
        """
        Provides operations to manage the pronouns property of the microsoft.graph.organizationSettings entity.
        """
        from .pronouns import pronouns_request_builder

        return pronouns_request_builder.PronounsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class SettingsRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class SettingsRequestBuilderGetQueryParameters():
        """
        Retrieve the properties and relationships of organizationSettings object. Nullable.
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
    class SettingsRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

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
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

