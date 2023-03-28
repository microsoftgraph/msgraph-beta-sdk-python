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
    from ...models import profile
    from ...models.o_data_errors import o_data_error
    from .account import account_request_builder
    from .account.item import user_account_information_item_request_builder
    from .addresses import addresses_request_builder
    from .addresses.item import item_address_item_request_builder
    from .anniversaries import anniversaries_request_builder
    from .anniversaries.item import person_annual_event_item_request_builder
    from .awards import awards_request_builder
    from .awards.item import person_award_item_request_builder
    from .certifications import certifications_request_builder
    from .certifications.item import person_certification_item_request_builder
    from .educational_activities import educational_activities_request_builder
    from .educational_activities.item import educational_activity_item_request_builder
    from .emails import emails_request_builder
    from .emails.item import item_email_item_request_builder
    from .interests import interests_request_builder
    from .interests.item import person_interest_item_request_builder
    from .languages import languages_request_builder
    from .languages.item import language_proficiency_item_request_builder
    from .names import names_request_builder
    from .names.item import person_name_item_request_builder
    from .notes import notes_request_builder
    from .notes.item import person_annotation_item_request_builder
    from .patents import patents_request_builder
    from .patents.item import item_patent_item_request_builder
    from .phones import phones_request_builder
    from .phones.item import item_phone_item_request_builder
    from .positions import positions_request_builder
    from .positions.item import work_position_item_request_builder
    from .projects import projects_request_builder
    from .projects.item import project_participation_item_request_builder
    from .publications import publications_request_builder
    from .publications.item import item_publication_item_request_builder
    from .skills import skills_request_builder
    from .skills.item import skill_proficiency_item_request_builder
    from .web_accounts import web_accounts_request_builder
    from .web_accounts.item import web_account_item_request_builder
    from .websites import websites_request_builder
    from .websites.item import person_website_item_request_builder

class ProfileRequestBuilder():
    """
    Provides operations to manage the profile property of the microsoft.graph.user entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new ProfileRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/me/profile{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def account_by_id(self,id: str) -> user_account_information_item_request_builder.UserAccountInformationItemRequestBuilder:
        """
        Provides operations to manage the account property of the microsoft.graph.profile entity.
        Args:
            id: Unique identifier of the item
        Returns: user_account_information_item_request_builder.UserAccountInformationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .account.item import user_account_information_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["userAccountInformation%2Did"] = id
        return user_account_information_item_request_builder.UserAccountInformationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def addresses_by_id(self,id: str) -> item_address_item_request_builder.ItemAddressItemRequestBuilder:
        """
        Provides operations to manage the addresses property of the microsoft.graph.profile entity.
        Args:
            id: Unique identifier of the item
        Returns: item_address_item_request_builder.ItemAddressItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .addresses.item import item_address_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["itemAddress%2Did"] = id
        return item_address_item_request_builder.ItemAddressItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def anniversaries_by_id(self,id: str) -> person_annual_event_item_request_builder.PersonAnnualEventItemRequestBuilder:
        """
        Provides operations to manage the anniversaries property of the microsoft.graph.profile entity.
        Args:
            id: Unique identifier of the item
        Returns: person_annual_event_item_request_builder.PersonAnnualEventItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .anniversaries.item import person_annual_event_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["personAnnualEvent%2Did"] = id
        return person_annual_event_item_request_builder.PersonAnnualEventItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def awards_by_id(self,id: str) -> person_award_item_request_builder.PersonAwardItemRequestBuilder:
        """
        Provides operations to manage the awards property of the microsoft.graph.profile entity.
        Args:
            id: Unique identifier of the item
        Returns: person_award_item_request_builder.PersonAwardItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .awards.item import person_award_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["personAward%2Did"] = id
        return person_award_item_request_builder.PersonAwardItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def certifications_by_id(self,id: str) -> person_certification_item_request_builder.PersonCertificationItemRequestBuilder:
        """
        Provides operations to manage the certifications property of the microsoft.graph.profile entity.
        Args:
            id: Unique identifier of the item
        Returns: person_certification_item_request_builder.PersonCertificationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .certifications.item import person_certification_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["personCertification%2Did"] = id
        return person_certification_item_request_builder.PersonCertificationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def delete(self,request_configuration: Optional[ProfileRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Deletes a profile object from a user's account.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ...models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    def educational_activities_by_id(self,id: str) -> educational_activity_item_request_builder.EducationalActivityItemRequestBuilder:
        """
        Provides operations to manage the educationalActivities property of the microsoft.graph.profile entity.
        Args:
            id: Unique identifier of the item
        Returns: educational_activity_item_request_builder.EducationalActivityItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .educational_activities.item import educational_activity_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["educationalActivity%2Did"] = id
        return educational_activity_item_request_builder.EducationalActivityItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def emails_by_id(self,id: str) -> item_email_item_request_builder.ItemEmailItemRequestBuilder:
        """
        Provides operations to manage the emails property of the microsoft.graph.profile entity.
        Args:
            id: Unique identifier of the item
        Returns: item_email_item_request_builder.ItemEmailItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .emails.item import item_email_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["itemEmail%2Did"] = id
        return item_email_item_request_builder.ItemEmailItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[ProfileRequestBuilderGetRequestConfiguration] = None) -> Optional[profile.Profile]:
        """
        Retrieve the properties and relationships of a profile object for a given user. The **profile** resource exposes various rich properties that are descriptive of the user as relationships, for example, anniversaries and education activities. To get one of these navigation properties, use the corresponding GET method on that property. See the methods exposed by **profile**.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[profile.Profile]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models import profile

        return await self.request_adapter.send_async(request_info, profile.Profile, error_mapping)
    
    def interests_by_id(self,id: str) -> person_interest_item_request_builder.PersonInterestItemRequestBuilder:
        """
        Provides operations to manage the interests property of the microsoft.graph.profile entity.
        Args:
            id: Unique identifier of the item
        Returns: person_interest_item_request_builder.PersonInterestItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .interests.item import person_interest_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["personInterest%2Did"] = id
        return person_interest_item_request_builder.PersonInterestItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def languages_by_id(self,id: str) -> language_proficiency_item_request_builder.LanguageProficiencyItemRequestBuilder:
        """
        Provides operations to manage the languages property of the microsoft.graph.profile entity.
        Args:
            id: Unique identifier of the item
        Returns: language_proficiency_item_request_builder.LanguageProficiencyItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .languages.item import language_proficiency_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["languageProficiency%2Did"] = id
        return language_proficiency_item_request_builder.LanguageProficiencyItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def names_by_id(self,id: str) -> person_name_item_request_builder.PersonNameItemRequestBuilder:
        """
        Provides operations to manage the names property of the microsoft.graph.profile entity.
        Args:
            id: Unique identifier of the item
        Returns: person_name_item_request_builder.PersonNameItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .names.item import person_name_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["personName%2Did"] = id
        return person_name_item_request_builder.PersonNameItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def notes_by_id(self,id: str) -> person_annotation_item_request_builder.PersonAnnotationItemRequestBuilder:
        """
        Provides operations to manage the notes property of the microsoft.graph.profile entity.
        Args:
            id: Unique identifier of the item
        Returns: person_annotation_item_request_builder.PersonAnnotationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .notes.item import person_annotation_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["personAnnotation%2Did"] = id
        return person_annotation_item_request_builder.PersonAnnotationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def patch(self,body: Optional[profile.Profile] = None, request_configuration: Optional[ProfileRequestBuilderPatchRequestConfiguration] = None) -> Optional[profile.Profile]:
        """
        Update the navigation property profile in me
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[profile.Profile]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ...models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models import profile

        return await self.request_adapter.send_async(request_info, profile.Profile, error_mapping)
    
    def patents_by_id(self,id: str) -> item_patent_item_request_builder.ItemPatentItemRequestBuilder:
        """
        Provides operations to manage the patents property of the microsoft.graph.profile entity.
        Args:
            id: Unique identifier of the item
        Returns: item_patent_item_request_builder.ItemPatentItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .patents.item import item_patent_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["itemPatent%2Did"] = id
        return item_patent_item_request_builder.ItemPatentItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def phones_by_id(self,id: str) -> item_phone_item_request_builder.ItemPhoneItemRequestBuilder:
        """
        Provides operations to manage the phones property of the microsoft.graph.profile entity.
        Args:
            id: Unique identifier of the item
        Returns: item_phone_item_request_builder.ItemPhoneItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .phones.item import item_phone_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["itemPhone%2Did"] = id
        return item_phone_item_request_builder.ItemPhoneItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def positions_by_id(self,id: str) -> work_position_item_request_builder.WorkPositionItemRequestBuilder:
        """
        Provides operations to manage the positions property of the microsoft.graph.profile entity.
        Args:
            id: Unique identifier of the item
        Returns: work_position_item_request_builder.WorkPositionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .positions.item import work_position_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["workPosition%2Did"] = id
        return work_position_item_request_builder.WorkPositionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def projects_by_id(self,id: str) -> project_participation_item_request_builder.ProjectParticipationItemRequestBuilder:
        """
        Provides operations to manage the projects property of the microsoft.graph.profile entity.
        Args:
            id: Unique identifier of the item
        Returns: project_participation_item_request_builder.ProjectParticipationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .projects.item import project_participation_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["projectParticipation%2Did"] = id
        return project_participation_item_request_builder.ProjectParticipationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def publications_by_id(self,id: str) -> item_publication_item_request_builder.ItemPublicationItemRequestBuilder:
        """
        Provides operations to manage the publications property of the microsoft.graph.profile entity.
        Args:
            id: Unique identifier of the item
        Returns: item_publication_item_request_builder.ItemPublicationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .publications.item import item_publication_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["itemPublication%2Did"] = id
        return item_publication_item_request_builder.ItemPublicationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def skills_by_id(self,id: str) -> skill_proficiency_item_request_builder.SkillProficiencyItemRequestBuilder:
        """
        Provides operations to manage the skills property of the microsoft.graph.profile entity.
        Args:
            id: Unique identifier of the item
        Returns: skill_proficiency_item_request_builder.SkillProficiencyItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .skills.item import skill_proficiency_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["skillProficiency%2Did"] = id
        return skill_proficiency_item_request_builder.SkillProficiencyItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def to_delete_request_information(self,request_configuration: Optional[ProfileRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Deletes a profile object from a user's account.
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
    
    def to_get_request_information(self,request_configuration: Optional[ProfileRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Retrieve the properties and relationships of a profile object for a given user. The **profile** resource exposes various rich properties that are descriptive of the user as relationships, for example, anniversaries and education activities. To get one of these navigation properties, use the corresponding GET method on that property. See the methods exposed by **profile**.
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
    
    def to_patch_request_information(self,body: Optional[profile.Profile] = None, request_configuration: Optional[ProfileRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property profile in me
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
    
    def web_accounts_by_id(self,id: str) -> web_account_item_request_builder.WebAccountItemRequestBuilder:
        """
        Provides operations to manage the webAccounts property of the microsoft.graph.profile entity.
        Args:
            id: Unique identifier of the item
        Returns: web_account_item_request_builder.WebAccountItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .web_accounts.item import web_account_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["webAccount%2Did"] = id
        return web_account_item_request_builder.WebAccountItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def websites_by_id(self,id: str) -> person_website_item_request_builder.PersonWebsiteItemRequestBuilder:
        """
        Provides operations to manage the websites property of the microsoft.graph.profile entity.
        Args:
            id: Unique identifier of the item
        Returns: person_website_item_request_builder.PersonWebsiteItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .websites.item import person_website_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["personWebsite%2Did"] = id
        return person_website_item_request_builder.PersonWebsiteItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @property
    def account(self) -> account_request_builder.AccountRequestBuilder:
        """
        Provides operations to manage the account property of the microsoft.graph.profile entity.
        """
        from .account import account_request_builder

        return account_request_builder.AccountRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def addresses(self) -> addresses_request_builder.AddressesRequestBuilder:
        """
        Provides operations to manage the addresses property of the microsoft.graph.profile entity.
        """
        from .addresses import addresses_request_builder

        return addresses_request_builder.AddressesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def anniversaries(self) -> anniversaries_request_builder.AnniversariesRequestBuilder:
        """
        Provides operations to manage the anniversaries property of the microsoft.graph.profile entity.
        """
        from .anniversaries import anniversaries_request_builder

        return anniversaries_request_builder.AnniversariesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def awards(self) -> awards_request_builder.AwardsRequestBuilder:
        """
        Provides operations to manage the awards property of the microsoft.graph.profile entity.
        """
        from .awards import awards_request_builder

        return awards_request_builder.AwardsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def certifications(self) -> certifications_request_builder.CertificationsRequestBuilder:
        """
        Provides operations to manage the certifications property of the microsoft.graph.profile entity.
        """
        from .certifications import certifications_request_builder

        return certifications_request_builder.CertificationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def educational_activities(self) -> educational_activities_request_builder.EducationalActivitiesRequestBuilder:
        """
        Provides operations to manage the educationalActivities property of the microsoft.graph.profile entity.
        """
        from .educational_activities import educational_activities_request_builder

        return educational_activities_request_builder.EducationalActivitiesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def emails(self) -> emails_request_builder.EmailsRequestBuilder:
        """
        Provides operations to manage the emails property of the microsoft.graph.profile entity.
        """
        from .emails import emails_request_builder

        return emails_request_builder.EmailsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def interests(self) -> interests_request_builder.InterestsRequestBuilder:
        """
        Provides operations to manage the interests property of the microsoft.graph.profile entity.
        """
        from .interests import interests_request_builder

        return interests_request_builder.InterestsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def languages(self) -> languages_request_builder.LanguagesRequestBuilder:
        """
        Provides operations to manage the languages property of the microsoft.graph.profile entity.
        """
        from .languages import languages_request_builder

        return languages_request_builder.LanguagesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def names(self) -> names_request_builder.NamesRequestBuilder:
        """
        Provides operations to manage the names property of the microsoft.graph.profile entity.
        """
        from .names import names_request_builder

        return names_request_builder.NamesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def notes(self) -> notes_request_builder.NotesRequestBuilder:
        """
        Provides operations to manage the notes property of the microsoft.graph.profile entity.
        """
        from .notes import notes_request_builder

        return notes_request_builder.NotesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def patents(self) -> patents_request_builder.PatentsRequestBuilder:
        """
        Provides operations to manage the patents property of the microsoft.graph.profile entity.
        """
        from .patents import patents_request_builder

        return patents_request_builder.PatentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def phones(self) -> phones_request_builder.PhonesRequestBuilder:
        """
        Provides operations to manage the phones property of the microsoft.graph.profile entity.
        """
        from .phones import phones_request_builder

        return phones_request_builder.PhonesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def positions(self) -> positions_request_builder.PositionsRequestBuilder:
        """
        Provides operations to manage the positions property of the microsoft.graph.profile entity.
        """
        from .positions import positions_request_builder

        return positions_request_builder.PositionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def projects(self) -> projects_request_builder.ProjectsRequestBuilder:
        """
        Provides operations to manage the projects property of the microsoft.graph.profile entity.
        """
        from .projects import projects_request_builder

        return projects_request_builder.ProjectsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def publications(self) -> publications_request_builder.PublicationsRequestBuilder:
        """
        Provides operations to manage the publications property of the microsoft.graph.profile entity.
        """
        from .publications import publications_request_builder

        return publications_request_builder.PublicationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def skills(self) -> skills_request_builder.SkillsRequestBuilder:
        """
        Provides operations to manage the skills property of the microsoft.graph.profile entity.
        """
        from .skills import skills_request_builder

        return skills_request_builder.SkillsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def web_accounts(self) -> web_accounts_request_builder.WebAccountsRequestBuilder:
        """
        Provides operations to manage the webAccounts property of the microsoft.graph.profile entity.
        """
        from .web_accounts import web_accounts_request_builder

        return web_accounts_request_builder.WebAccountsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def websites(self) -> websites_request_builder.WebsitesRequestBuilder:
        """
        Provides operations to manage the websites property of the microsoft.graph.profile entity.
        """
        from .websites import websites_request_builder

        return websites_request_builder.WebsitesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class ProfileRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class ProfileRequestBuilderGetQueryParameters():
        """
        Retrieve the properties and relationships of a profile object for a given user. The **profile** resource exposes various rich properties that are descriptive of the user as relationships, for example, anniversaries and education activities. To get one of these navigation properties, use the corresponding GET method on that property. See the methods exposed by **profile**.
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
    class ProfileRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[ProfileRequestBuilder.ProfileRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class ProfileRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

