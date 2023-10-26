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
    from ....models.profile import Profile
    from .account.account_request_builder import AccountRequestBuilder
    from .addresses.addresses_request_builder import AddressesRequestBuilder
    from .anniversaries.anniversaries_request_builder import AnniversariesRequestBuilder
    from .awards.awards_request_builder import AwardsRequestBuilder
    from .certifications.certifications_request_builder import CertificationsRequestBuilder
    from .educational_activities.educational_activities_request_builder import EducationalActivitiesRequestBuilder
    from .emails.emails_request_builder import EmailsRequestBuilder
    from .interests.interests_request_builder import InterestsRequestBuilder
    from .languages.languages_request_builder import LanguagesRequestBuilder
    from .names.names_request_builder import NamesRequestBuilder
    from .notes.notes_request_builder import NotesRequestBuilder
    from .patents.patents_request_builder import PatentsRequestBuilder
    from .phones.phones_request_builder import PhonesRequestBuilder
    from .positions.positions_request_builder import PositionsRequestBuilder
    from .projects.projects_request_builder import ProjectsRequestBuilder
    from .publications.publications_request_builder import PublicationsRequestBuilder
    from .skills.skills_request_builder import SkillsRequestBuilder
    from .websites.websites_request_builder import WebsitesRequestBuilder
    from .web_accounts.web_accounts_request_builder import WebAccountsRequestBuilder

class ProfileRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the profile property of the microsoft.graph.user entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new ProfileRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/profile{?%24select,%24expand}", path_parameters)
    
    async def delete(self,request_configuration: Optional[ProfileRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Deletes a profile object from a user's account. This API is available in the following national cloud deployments.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        Find more info here: https://learn.microsoft.com/graph/api/profile-delete?view=graph-rest-1.0
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
    
    async def get(self,request_configuration: Optional[ProfileRequestBuilderGetRequestConfiguration] = None) -> Optional[Profile]:
        """
        Retrieve the properties and relationships of a profile object for a given user. The profile resource exposes various rich properties that are descriptive of the user as relationships, for example, anniversaries and education activities. To get one of these navigation properties, use the corresponding GET method on that property. See the methods exposed by profile. This API is available in the following national cloud deployments.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Profile]
        Find more info here: https://learn.microsoft.com/graph/api/profile-get?view=graph-rest-1.0
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
        from ....models.profile import Profile

        return await self.request_adapter.send_async(request_info, Profile, error_mapping)
    
    async def patch(self,body: Optional[Profile] = None, request_configuration: Optional[ProfileRequestBuilderPatchRequestConfiguration] = None) -> Optional[Profile]:
        """
        Update the navigation property profile in users
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Profile]
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
        from ....models.profile import Profile

        return await self.request_adapter.send_async(request_info, Profile, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[ProfileRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Deletes a profile object from a user's account. This API is available in the following national cloud deployments.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.DELETE
        request_info.headers.try_add("Accept", "application/json, application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[ProfileRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Retrieve the properties and relationships of a profile object for a given user. The profile resource exposes various rich properties that are descriptive of the user as relationships, for example, anniversaries and education activities. To get one of these navigation properties, use the corresponding GET method on that property. See the methods exposed by profile. This API is available in the following national cloud deployments.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers.try_add("Accept", "application/json;q=1")
        return request_info
    
    def to_patch_request_information(self,body: Optional[Profile] = None, request_configuration: Optional[ProfileRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property profile in users
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.PATCH
        request_info.headers.try_add("Accept", "application/json;q=1")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> ProfileRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ProfileRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return ProfileRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def account(self) -> AccountRequestBuilder:
        """
        Provides operations to manage the account property of the microsoft.graph.profile entity.
        """
        from .account.account_request_builder import AccountRequestBuilder

        return AccountRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def addresses(self) -> AddressesRequestBuilder:
        """
        Provides operations to manage the addresses property of the microsoft.graph.profile entity.
        """
        from .addresses.addresses_request_builder import AddressesRequestBuilder

        return AddressesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def anniversaries(self) -> AnniversariesRequestBuilder:
        """
        Provides operations to manage the anniversaries property of the microsoft.graph.profile entity.
        """
        from .anniversaries.anniversaries_request_builder import AnniversariesRequestBuilder

        return AnniversariesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def awards(self) -> AwardsRequestBuilder:
        """
        Provides operations to manage the awards property of the microsoft.graph.profile entity.
        """
        from .awards.awards_request_builder import AwardsRequestBuilder

        return AwardsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def certifications(self) -> CertificationsRequestBuilder:
        """
        Provides operations to manage the certifications property of the microsoft.graph.profile entity.
        """
        from .certifications.certifications_request_builder import CertificationsRequestBuilder

        return CertificationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def educational_activities(self) -> EducationalActivitiesRequestBuilder:
        """
        Provides operations to manage the educationalActivities property of the microsoft.graph.profile entity.
        """
        from .educational_activities.educational_activities_request_builder import EducationalActivitiesRequestBuilder

        return EducationalActivitiesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def emails(self) -> EmailsRequestBuilder:
        """
        Provides operations to manage the emails property of the microsoft.graph.profile entity.
        """
        from .emails.emails_request_builder import EmailsRequestBuilder

        return EmailsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def interests(self) -> InterestsRequestBuilder:
        """
        Provides operations to manage the interests property of the microsoft.graph.profile entity.
        """
        from .interests.interests_request_builder import InterestsRequestBuilder

        return InterestsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def languages(self) -> LanguagesRequestBuilder:
        """
        Provides operations to manage the languages property of the microsoft.graph.profile entity.
        """
        from .languages.languages_request_builder import LanguagesRequestBuilder

        return LanguagesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def names(self) -> NamesRequestBuilder:
        """
        Provides operations to manage the names property of the microsoft.graph.profile entity.
        """
        from .names.names_request_builder import NamesRequestBuilder

        return NamesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def notes(self) -> NotesRequestBuilder:
        """
        Provides operations to manage the notes property of the microsoft.graph.profile entity.
        """
        from .notes.notes_request_builder import NotesRequestBuilder

        return NotesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def patents(self) -> PatentsRequestBuilder:
        """
        Provides operations to manage the patents property of the microsoft.graph.profile entity.
        """
        from .patents.patents_request_builder import PatentsRequestBuilder

        return PatentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def phones(self) -> PhonesRequestBuilder:
        """
        Provides operations to manage the phones property of the microsoft.graph.profile entity.
        """
        from .phones.phones_request_builder import PhonesRequestBuilder

        return PhonesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def positions(self) -> PositionsRequestBuilder:
        """
        Provides operations to manage the positions property of the microsoft.graph.profile entity.
        """
        from .positions.positions_request_builder import PositionsRequestBuilder

        return PositionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def projects(self) -> ProjectsRequestBuilder:
        """
        Provides operations to manage the projects property of the microsoft.graph.profile entity.
        """
        from .projects.projects_request_builder import ProjectsRequestBuilder

        return ProjectsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def publications(self) -> PublicationsRequestBuilder:
        """
        Provides operations to manage the publications property of the microsoft.graph.profile entity.
        """
        from .publications.publications_request_builder import PublicationsRequestBuilder

        return PublicationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def skills(self) -> SkillsRequestBuilder:
        """
        Provides operations to manage the skills property of the microsoft.graph.profile entity.
        """
        from .skills.skills_request_builder import SkillsRequestBuilder

        return SkillsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def web_accounts(self) -> WebAccountsRequestBuilder:
        """
        Provides operations to manage the webAccounts property of the microsoft.graph.profile entity.
        """
        from .web_accounts.web_accounts_request_builder import WebAccountsRequestBuilder

        return WebAccountsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def websites(self) -> WebsitesRequestBuilder:
        """
        Provides operations to manage the websites property of the microsoft.graph.profile entity.
        """
        from .websites.websites_request_builder import WebsitesRequestBuilder

        return WebsitesRequestBuilder(self.request_adapter, self.path_parameters)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class ProfileRequestBuilderDeleteRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
    @dataclass
    class ProfileRequestBuilderGetQueryParameters():
        """
        Retrieve the properties and relationships of a profile object for a given user. The profile resource exposes various rich properties that are descriptive of the user as relationships, for example, anniversaries and education activities. To get one of these navigation properties, use the corresponding GET method on that property. See the methods exposed by profile. This API is available in the following national cloud deployments.
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
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
    class ProfileRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[ProfileRequestBuilder.ProfileRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class ProfileRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

