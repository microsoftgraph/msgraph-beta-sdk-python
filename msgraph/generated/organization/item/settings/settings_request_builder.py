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
    from ....models.organization_settings import OrganizationSettings
    from .contact_insights.contact_insights_request_builder import ContactInsightsRequestBuilder
    from .item_insights.item_insights_request_builder import ItemInsightsRequestBuilder
    from .microsoft_application_data_access.microsoft_application_data_access_request_builder import MicrosoftApplicationDataAccessRequestBuilder
    from .people_insights.people_insights_request_builder import PeopleInsightsRequestBuilder
    from .profile_card_properties.profile_card_properties_request_builder import ProfileCardPropertiesRequestBuilder
    from .pronouns.pronouns_request_builder import PronounsRequestBuilder

class SettingsRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the settings property of the microsoft.graph.organization entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new SettingsRequestBuilder and sets the default values.
        Args:
            path_parameters: The raw url or the Url template parameters for the request.
            request_adapter: The request adapter to use to execute the requests.
        """
        super().__init__(request_adapter, "{+baseurl}/organization/{organization%2Did}/settings{?%24select,%24expand}", path_parameters)
    
    async def delete(self,request_configuration: Optional[SettingsRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property settings for organization
        Args:
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[SettingsRequestBuilderGetRequestConfiguration] = None) -> Optional[OrganizationSettings]:
        """
        Retrieve the properties and relationships of an organizationSettings object, including profileCardProperties. This operation does not return insightsSettings. Depending on the type of insights, you can get their settings by using list itemInsights or list peopleInsights. This operation does not return microsoftApplicationDataAccessSettings. To get microsoftApplicationDataAccessSettings, use list microsoftApplicationDataAccessSettings.
        Args:
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[OrganizationSettings]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.organization_settings import OrganizationSettings

        return await self.request_adapter.send_async(request_info, OrganizationSettings, error_mapping)
    
    async def patch(self,body: Optional[OrganizationSettings] = None, request_configuration: Optional[SettingsRequestBuilderPatchRequestConfiguration] = None) -> Optional[OrganizationSettings]:
        """
        Update the navigation property settings in organization
        Args:
            body: The request body
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[OrganizationSettings]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.organization_settings import OrganizationSettings

        return await self.request_adapter.send_async(request_info, OrganizationSettings, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[SettingsRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property settings for organization
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
    
    def to_get_request_information(self,request_configuration: Optional[SettingsRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Retrieve the properties and relationships of an organizationSettings object, including profileCardProperties. This operation does not return insightsSettings. Depending on the type of insights, you can get their settings by using list itemInsights or list peopleInsights. This operation does not return microsoftApplicationDataAccessSettings. To get microsoftApplicationDataAccessSettings, use list microsoftApplicationDataAccessSettings.
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
    
    def to_patch_request_information(self,body: Optional[OrganizationSettings] = None, request_configuration: Optional[SettingsRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property settings in organization
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
    def contact_insights(self) -> ContactInsightsRequestBuilder:
        """
        Provides operations to manage the contactInsights property of the microsoft.graph.organizationSettings entity.
        """
        from .contact_insights.contact_insights_request_builder import ContactInsightsRequestBuilder

        return ContactInsightsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def item_insights(self) -> ItemInsightsRequestBuilder:
        """
        Provides operations to manage the itemInsights property of the microsoft.graph.organizationSettings entity.
        """
        from .item_insights.item_insights_request_builder import ItemInsightsRequestBuilder

        return ItemInsightsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_application_data_access(self) -> MicrosoftApplicationDataAccessRequestBuilder:
        """
        Provides operations to manage the microsoftApplicationDataAccess property of the microsoft.graph.organizationSettings entity.
        """
        from .microsoft_application_data_access.microsoft_application_data_access_request_builder import MicrosoftApplicationDataAccessRequestBuilder

        return MicrosoftApplicationDataAccessRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def people_insights(self) -> PeopleInsightsRequestBuilder:
        """
        Provides operations to manage the peopleInsights property of the microsoft.graph.organizationSettings entity.
        """
        from .people_insights.people_insights_request_builder import PeopleInsightsRequestBuilder

        return PeopleInsightsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def profile_card_properties(self) -> ProfileCardPropertiesRequestBuilder:
        """
        Provides operations to manage the profileCardProperties property of the microsoft.graph.organizationSettings entity.
        """
        from .profile_card_properties.profile_card_properties_request_builder import ProfileCardPropertiesRequestBuilder

        return ProfileCardPropertiesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def pronouns(self) -> PronounsRequestBuilder:
        """
        Provides operations to manage the pronouns property of the microsoft.graph.organizationSettings entity.
        """
        from .pronouns.pronouns_request_builder import PronounsRequestBuilder

        return PronounsRequestBuilder(self.request_adapter, self.path_parameters)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class SettingsRequestBuilderDeleteRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
    @dataclass
    class SettingsRequestBuilderGetQueryParameters():
        """
        Retrieve the properties and relationships of an organizationSettings object, including profileCardProperties. This operation does not return insightsSettings. Depending on the type of insights, you can get their settings by using list itemInsights or list peopleInsights. This operation does not return microsoftApplicationDataAccessSettings. To get microsoftApplicationDataAccessSettings, use list microsoftApplicationDataAccessSettings.
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
    class SettingsRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[SettingsRequestBuilder.SettingsRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class SettingsRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

