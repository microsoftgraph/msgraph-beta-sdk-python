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

account_request_builder = lazy_import('msgraph.generated.me.profile.account.account_request_builder')
user_account_information_item_request_builder = lazy_import('msgraph.generated.me.profile.account.item.user_account_information_item_request_builder')
addresses_request_builder = lazy_import('msgraph.generated.me.profile.addresses.addresses_request_builder')
item_address_item_request_builder = lazy_import('msgraph.generated.me.profile.addresses.item.item_address_item_request_builder')
anniversaries_request_builder = lazy_import('msgraph.generated.me.profile.anniversaries.anniversaries_request_builder')
person_annual_event_item_request_builder = lazy_import('msgraph.generated.me.profile.anniversaries.item.person_annual_event_item_request_builder')
awards_request_builder = lazy_import('msgraph.generated.me.profile.awards.awards_request_builder')
person_award_item_request_builder = lazy_import('msgraph.generated.me.profile.awards.item.person_award_item_request_builder')
certifications_request_builder = lazy_import('msgraph.generated.me.profile.certifications.certifications_request_builder')
person_certification_item_request_builder = lazy_import('msgraph.generated.me.profile.certifications.item.person_certification_item_request_builder')
educational_activities_request_builder = lazy_import('msgraph.generated.me.profile.educational_activities.educational_activities_request_builder')
educational_activity_item_request_builder = lazy_import('msgraph.generated.me.profile.educational_activities.item.educational_activity_item_request_builder')
emails_request_builder = lazy_import('msgraph.generated.me.profile.emails.emails_request_builder')
item_email_item_request_builder = lazy_import('msgraph.generated.me.profile.emails.item.item_email_item_request_builder')
interests_request_builder = lazy_import('msgraph.generated.me.profile.interests.interests_request_builder')
person_interest_item_request_builder = lazy_import('msgraph.generated.me.profile.interests.item.person_interest_item_request_builder')
languages_request_builder = lazy_import('msgraph.generated.me.profile.languages.languages_request_builder')
language_proficiency_item_request_builder = lazy_import('msgraph.generated.me.profile.languages.item.language_proficiency_item_request_builder')
names_request_builder = lazy_import('msgraph.generated.me.profile.names.names_request_builder')
person_name_item_request_builder = lazy_import('msgraph.generated.me.profile.names.item.person_name_item_request_builder')
notes_request_builder = lazy_import('msgraph.generated.me.profile.notes.notes_request_builder')
person_annotation_item_request_builder = lazy_import('msgraph.generated.me.profile.notes.item.person_annotation_item_request_builder')
patents_request_builder = lazy_import('msgraph.generated.me.profile.patents.patents_request_builder')
item_patent_item_request_builder = lazy_import('msgraph.generated.me.profile.patents.item.item_patent_item_request_builder')
phones_request_builder = lazy_import('msgraph.generated.me.profile.phones.phones_request_builder')
item_phone_item_request_builder = lazy_import('msgraph.generated.me.profile.phones.item.item_phone_item_request_builder')
positions_request_builder = lazy_import('msgraph.generated.me.profile.positions.positions_request_builder')
work_position_item_request_builder = lazy_import('msgraph.generated.me.profile.positions.item.work_position_item_request_builder')
projects_request_builder = lazy_import('msgraph.generated.me.profile.projects.projects_request_builder')
project_participation_item_request_builder = lazy_import('msgraph.generated.me.profile.projects.item.project_participation_item_request_builder')
publications_request_builder = lazy_import('msgraph.generated.me.profile.publications.publications_request_builder')
item_publication_item_request_builder = lazy_import('msgraph.generated.me.profile.publications.item.item_publication_item_request_builder')
skills_request_builder = lazy_import('msgraph.generated.me.profile.skills.skills_request_builder')
skill_proficiency_item_request_builder = lazy_import('msgraph.generated.me.profile.skills.item.skill_proficiency_item_request_builder')
web_accounts_request_builder = lazy_import('msgraph.generated.me.profile.web_accounts.web_accounts_request_builder')
web_account_item_request_builder = lazy_import('msgraph.generated.me.profile.web_accounts.item.web_account_item_request_builder')
websites_request_builder = lazy_import('msgraph.generated.me.profile.websites.websites_request_builder')
person_website_item_request_builder = lazy_import('msgraph.generated.me.profile.websites.item.person_website_item_request_builder')
profile = lazy_import('msgraph.generated.models.profile')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class ProfileRequestBuilder():
    """
    Provides operations to manage the profile property of the microsoft.graph.user entity.
    """
    @property
    def account(self) -> account_request_builder.AccountRequestBuilder:
        """
        Provides operations to manage the account property of the microsoft.graph.profile entity.
        """
        return account_request_builder.AccountRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def addresses(self) -> addresses_request_builder.AddressesRequestBuilder:
        """
        Provides operations to manage the addresses property of the microsoft.graph.profile entity.
        """
        return addresses_request_builder.AddressesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def anniversaries(self) -> anniversaries_request_builder.AnniversariesRequestBuilder:
        """
        Provides operations to manage the anniversaries property of the microsoft.graph.profile entity.
        """
        return anniversaries_request_builder.AnniversariesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def awards(self) -> awards_request_builder.AwardsRequestBuilder:
        """
        Provides operations to manage the awards property of the microsoft.graph.profile entity.
        """
        return awards_request_builder.AwardsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def certifications(self) -> certifications_request_builder.CertificationsRequestBuilder:
        """
        Provides operations to manage the certifications property of the microsoft.graph.profile entity.
        """
        return certifications_request_builder.CertificationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def educational_activities(self) -> educational_activities_request_builder.EducationalActivitiesRequestBuilder:
        """
        Provides operations to manage the educationalActivities property of the microsoft.graph.profile entity.
        """
        return educational_activities_request_builder.EducationalActivitiesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def emails(self) -> emails_request_builder.EmailsRequestBuilder:
        """
        Provides operations to manage the emails property of the microsoft.graph.profile entity.
        """
        return emails_request_builder.EmailsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def interests(self) -> interests_request_builder.InterestsRequestBuilder:
        """
        Provides operations to manage the interests property of the microsoft.graph.profile entity.
        """
        return interests_request_builder.InterestsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def languages(self) -> languages_request_builder.LanguagesRequestBuilder:
        """
        Provides operations to manage the languages property of the microsoft.graph.profile entity.
        """
        return languages_request_builder.LanguagesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def names(self) -> names_request_builder.NamesRequestBuilder:
        """
        Provides operations to manage the names property of the microsoft.graph.profile entity.
        """
        return names_request_builder.NamesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def notes(self) -> notes_request_builder.NotesRequestBuilder:
        """
        Provides operations to manage the notes property of the microsoft.graph.profile entity.
        """
        return notes_request_builder.NotesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def patents(self) -> patents_request_builder.PatentsRequestBuilder:
        """
        Provides operations to manage the patents property of the microsoft.graph.profile entity.
        """
        return patents_request_builder.PatentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def phones(self) -> phones_request_builder.PhonesRequestBuilder:
        """
        Provides operations to manage the phones property of the microsoft.graph.profile entity.
        """
        return phones_request_builder.PhonesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def positions(self) -> positions_request_builder.PositionsRequestBuilder:
        """
        Provides operations to manage the positions property of the microsoft.graph.profile entity.
        """
        return positions_request_builder.PositionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def projects(self) -> projects_request_builder.ProjectsRequestBuilder:
        """
        Provides operations to manage the projects property of the microsoft.graph.profile entity.
        """
        return projects_request_builder.ProjectsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def publications(self) -> publications_request_builder.PublicationsRequestBuilder:
        """
        Provides operations to manage the publications property of the microsoft.graph.profile entity.
        """
        return publications_request_builder.PublicationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def skills(self) -> skills_request_builder.SkillsRequestBuilder:
        """
        Provides operations to manage the skills property of the microsoft.graph.profile entity.
        """
        return skills_request_builder.SkillsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def web_accounts(self) -> web_accounts_request_builder.WebAccountsRequestBuilder:
        """
        Provides operations to manage the webAccounts property of the microsoft.graph.profile entity.
        """
        return web_accounts_request_builder.WebAccountsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def websites(self) -> websites_request_builder.WebsitesRequestBuilder:
        """
        Provides operations to manage the websites property of the microsoft.graph.profile entity.
        """
        return websites_request_builder.WebsitesRequestBuilder(self.request_adapter, self.path_parameters)
    
    def account_by_id(self,id: str) -> user_account_information_item_request_builder.UserAccountInformationItemRequestBuilder:
        """
        Provides operations to manage the account property of the microsoft.graph.profile entity.
        Args:
            id: Unique identifier of the item
        Returns: user_account_information_item_request_builder.UserAccountInformationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
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
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["personCertification%2Did"] = id
        return person_certification_item_request_builder.PersonCertificationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
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
    
    def create_delete_request_information(self,request_configuration: Optional[ProfileRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
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
    
    def create_get_request_information(self,request_configuration: Optional[ProfileRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
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
        request_info.headers["Accept"] = "application/json"
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def create_patch_request_information(self,body: Optional[profile.Profile] = None, request_configuration: Optional[ProfileRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
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
        request_info.headers["Accept"] = "application/json"
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    async def delete(self,request_configuration: Optional[ProfileRequestBuilderDeleteRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> None:
        """
        Deletes a profile object from a user's account.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        """
        request_info = self.create_delete_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, response_handler, error_mapping)
    
    def educational_activities_by_id(self,id: str) -> educational_activity_item_request_builder.EducationalActivityItemRequestBuilder:
        """
        Provides operations to manage the educationalActivities property of the microsoft.graph.profile entity.
        Args:
            id: Unique identifier of the item
        Returns: educational_activity_item_request_builder.EducationalActivityItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
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
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["itemEmail%2Did"] = id
        return item_email_item_request_builder.ItemEmailItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[ProfileRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[profile.Profile]:
        """
        Retrieve the properties and relationships of a profile object for a given user. The **profile** resource exposes various rich properties that are descriptive of the user as relationships, for example, anniversaries and education activities. To get one of these navigation properties, use the corresponding GET method on that property. See the methods exposed by **profile**.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[profile.Profile]
        """
        request_info = self.create_get_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, profile.Profile, response_handler, error_mapping)
    
    def interests_by_id(self,id: str) -> person_interest_item_request_builder.PersonInterestItemRequestBuilder:
        """
        Provides operations to manage the interests property of the microsoft.graph.profile entity.
        Args:
            id: Unique identifier of the item
        Returns: person_interest_item_request_builder.PersonInterestItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
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
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["personAnnotation%2Did"] = id
        return person_annotation_item_request_builder.PersonAnnotationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def patch(self,body: Optional[profile.Profile] = None, request_configuration: Optional[ProfileRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[profile.Profile]:
        """
        Update the navigation property profile in me
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[profile.Profile]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.create_patch_request_information(
            body, request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, profile.Profile, response_handler, error_mapping)
    
    def patents_by_id(self,id: str) -> item_patent_item_request_builder.ItemPatentItemRequestBuilder:
        """
        Provides operations to manage the patents property of the microsoft.graph.profile entity.
        Args:
            id: Unique identifier of the item
        Returns: item_patent_item_request_builder.ItemPatentItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
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
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["skillProficiency%2Did"] = id
        return skill_proficiency_item_request_builder.SkillProficiencyItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def web_accounts_by_id(self,id: str) -> web_account_item_request_builder.WebAccountItemRequestBuilder:
        """
        Provides operations to manage the webAccounts property of the microsoft.graph.profile entity.
        Args:
            id: Unique identifier of the item
        Returns: web_account_item_request_builder.WebAccountItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
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
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["personWebsite%2Did"] = id
        return person_website_item_request_builder.PersonWebsiteItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @dataclass
    class ProfileRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class ProfileRequestBuilderGetQueryParameters():
        """
        Retrieve the properties and relationships of a profile object for a given user. The **profile** resource exposes various rich properties that are descriptive of the user as relationships, for example, anniversaries and education activities. To get one of these navigation properties, use the corresponding GET method on that property. See the methods exposed by **profile**.
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
    class ProfileRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

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
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

