from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

educational_activity = lazy_import('msgraph.generated.models.educational_activity')
entity = lazy_import('msgraph.generated.models.entity')
item_address = lazy_import('msgraph.generated.models.item_address')
item_email = lazy_import('msgraph.generated.models.item_email')
item_patent = lazy_import('msgraph.generated.models.item_patent')
item_phone = lazy_import('msgraph.generated.models.item_phone')
item_publication = lazy_import('msgraph.generated.models.item_publication')
language_proficiency = lazy_import('msgraph.generated.models.language_proficiency')
person_annotation = lazy_import('msgraph.generated.models.person_annotation')
person_annual_event = lazy_import('msgraph.generated.models.person_annual_event')
person_award = lazy_import('msgraph.generated.models.person_award')
person_certification = lazy_import('msgraph.generated.models.person_certification')
person_interest = lazy_import('msgraph.generated.models.person_interest')
person_name = lazy_import('msgraph.generated.models.person_name')
person_website = lazy_import('msgraph.generated.models.person_website')
project_participation = lazy_import('msgraph.generated.models.project_participation')
skill_proficiency = lazy_import('msgraph.generated.models.skill_proficiency')
user_account_information = lazy_import('msgraph.generated.models.user_account_information')
web_account = lazy_import('msgraph.generated.models.web_account')
work_position = lazy_import('msgraph.generated.models.work_position')

class Profile(entity.Entity):
    @property
    def account(self,) -> Optional[List[user_account_information.UserAccountInformation]]:
        """
        Gets the account property value. The account property
        Returns: Optional[List[user_account_information.UserAccountInformation]]
        """
        return self._account
    
    @account.setter
    def account(self,value: Optional[List[user_account_information.UserAccountInformation]] = None) -> None:
        """
        Sets the account property value. The account property
        Args:
            value: Value to set for the account property.
        """
        self._account = value
    
    @property
    def addresses(self,) -> Optional[List[item_address.ItemAddress]]:
        """
        Gets the addresses property value. Represents details of addresses associated with the user.
        Returns: Optional[List[item_address.ItemAddress]]
        """
        return self._addresses
    
    @addresses.setter
    def addresses(self,value: Optional[List[item_address.ItemAddress]] = None) -> None:
        """
        Sets the addresses property value. Represents details of addresses associated with the user.
        Args:
            value: Value to set for the addresses property.
        """
        self._addresses = value
    
    @property
    def anniversaries(self,) -> Optional[List[person_annual_event.PersonAnnualEvent]]:
        """
        Gets the anniversaries property value. Represents the details of meaningful dates associated with a person.
        Returns: Optional[List[person_annual_event.PersonAnnualEvent]]
        """
        return self._anniversaries
    
    @anniversaries.setter
    def anniversaries(self,value: Optional[List[person_annual_event.PersonAnnualEvent]] = None) -> None:
        """
        Sets the anniversaries property value. Represents the details of meaningful dates associated with a person.
        Args:
            value: Value to set for the anniversaries property.
        """
        self._anniversaries = value
    
    @property
    def awards(self,) -> Optional[List[person_award.PersonAward]]:
        """
        Gets the awards property value. Represents the details of awards or honors associated with a person.
        Returns: Optional[List[person_award.PersonAward]]
        """
        return self._awards
    
    @awards.setter
    def awards(self,value: Optional[List[person_award.PersonAward]] = None) -> None:
        """
        Sets the awards property value. Represents the details of awards or honors associated with a person.
        Args:
            value: Value to set for the awards property.
        """
        self._awards = value
    
    @property
    def certifications(self,) -> Optional[List[person_certification.PersonCertification]]:
        """
        Gets the certifications property value. Represents the details of certifications associated with a person.
        Returns: Optional[List[person_certification.PersonCertification]]
        """
        return self._certifications
    
    @certifications.setter
    def certifications(self,value: Optional[List[person_certification.PersonCertification]] = None) -> None:
        """
        Sets the certifications property value. Represents the details of certifications associated with a person.
        Args:
            value: Value to set for the certifications property.
        """
        self._certifications = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new profile and sets the default values.
        """
        super().__init__()
        # The account property
        self._account: Optional[List[user_account_information.UserAccountInformation]] = None
        # Represents details of addresses associated with the user.
        self._addresses: Optional[List[item_address.ItemAddress]] = None
        # Represents the details of meaningful dates associated with a person.
        self._anniversaries: Optional[List[person_annual_event.PersonAnnualEvent]] = None
        # Represents the details of awards or honors associated with a person.
        self._awards: Optional[List[person_award.PersonAward]] = None
        # Represents the details of certifications associated with a person.
        self._certifications: Optional[List[person_certification.PersonCertification]] = None
        # Represents data that a user has supplied related to undergraduate, graduate, postgraduate or other educational activities.
        self._educational_activities: Optional[List[educational_activity.EducationalActivity]] = None
        # Represents detailed information about email addresses associated with the user.
        self._emails: Optional[List[item_email.ItemEmail]] = None
        # Provides detailed information about interests the user has associated with themselves in various services.
        self._interests: Optional[List[person_interest.PersonInterest]] = None
        # Represents detailed information about languages that a user has added to their profile.
        self._languages: Optional[List[language_proficiency.LanguageProficiency]] = None
        # Represents the names a user has added to their profile.
        self._names: Optional[List[person_name.PersonName]] = None
        # Represents notes that a user has added to their profile.
        self._notes: Optional[List[person_annotation.PersonAnnotation]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Represents patents that a user has added to their profile.
        self._patents: Optional[List[item_patent.ItemPatent]] = None
        # Represents detailed information about phone numbers associated with a user in various services.
        self._phones: Optional[List[item_phone.ItemPhone]] = None
        # Represents detailed information about work positions associated with a user's profile.
        self._positions: Optional[List[work_position.WorkPosition]] = None
        # Represents detailed information about projects associated with a user.
        self._projects: Optional[List[project_participation.ProjectParticipation]] = None
        # Represents details of any publications a user has added to their profile.
        self._publications: Optional[List[item_publication.ItemPublication]] = None
        # Represents detailed information about skills associated with a user in various services.
        self._skills: Optional[List[skill_proficiency.SkillProficiency]] = None
        # Represents web accounts the user has indicated they use or has added to their user profile.
        self._web_accounts: Optional[List[web_account.WebAccount]] = None
        # Represents detailed information about websites associated with a user in various services.
        self._websites: Optional[List[person_website.PersonWebsite]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Profile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Profile
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Profile()
    
    @property
    def educational_activities(self,) -> Optional[List[educational_activity.EducationalActivity]]:
        """
        Gets the educationalActivities property value. Represents data that a user has supplied related to undergraduate, graduate, postgraduate or other educational activities.
        Returns: Optional[List[educational_activity.EducationalActivity]]
        """
        return self._educational_activities
    
    @educational_activities.setter
    def educational_activities(self,value: Optional[List[educational_activity.EducationalActivity]] = None) -> None:
        """
        Sets the educationalActivities property value. Represents data that a user has supplied related to undergraduate, graduate, postgraduate or other educational activities.
        Args:
            value: Value to set for the educationalActivities property.
        """
        self._educational_activities = value
    
    @property
    def emails(self,) -> Optional[List[item_email.ItemEmail]]:
        """
        Gets the emails property value. Represents detailed information about email addresses associated with the user.
        Returns: Optional[List[item_email.ItemEmail]]
        """
        return self._emails
    
    @emails.setter
    def emails(self,value: Optional[List[item_email.ItemEmail]] = None) -> None:
        """
        Sets the emails property value. Represents detailed information about email addresses associated with the user.
        Args:
            value: Value to set for the emails property.
        """
        self._emails = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "account": lambda n : setattr(self, 'account', n.get_collection_of_object_values(user_account_information.UserAccountInformation)),
            "addresses": lambda n : setattr(self, 'addresses', n.get_collection_of_object_values(item_address.ItemAddress)),
            "anniversaries": lambda n : setattr(self, 'anniversaries', n.get_collection_of_object_values(person_annual_event.PersonAnnualEvent)),
            "awards": lambda n : setattr(self, 'awards', n.get_collection_of_object_values(person_award.PersonAward)),
            "certifications": lambda n : setattr(self, 'certifications', n.get_collection_of_object_values(person_certification.PersonCertification)),
            "educational_activities": lambda n : setattr(self, 'educational_activities', n.get_collection_of_object_values(educational_activity.EducationalActivity)),
            "emails": lambda n : setattr(self, 'emails', n.get_collection_of_object_values(item_email.ItemEmail)),
            "interests": lambda n : setattr(self, 'interests', n.get_collection_of_object_values(person_interest.PersonInterest)),
            "languages": lambda n : setattr(self, 'languages', n.get_collection_of_object_values(language_proficiency.LanguageProficiency)),
            "names": lambda n : setattr(self, 'names', n.get_collection_of_object_values(person_name.PersonName)),
            "notes": lambda n : setattr(self, 'notes', n.get_collection_of_object_values(person_annotation.PersonAnnotation)),
            "patents": lambda n : setattr(self, 'patents', n.get_collection_of_object_values(item_patent.ItemPatent)),
            "phones": lambda n : setattr(self, 'phones', n.get_collection_of_object_values(item_phone.ItemPhone)),
            "positions": lambda n : setattr(self, 'positions', n.get_collection_of_object_values(work_position.WorkPosition)),
            "projects": lambda n : setattr(self, 'projects', n.get_collection_of_object_values(project_participation.ProjectParticipation)),
            "publications": lambda n : setattr(self, 'publications', n.get_collection_of_object_values(item_publication.ItemPublication)),
            "skills": lambda n : setattr(self, 'skills', n.get_collection_of_object_values(skill_proficiency.SkillProficiency)),
            "web_accounts": lambda n : setattr(self, 'web_accounts', n.get_collection_of_object_values(web_account.WebAccount)),
            "websites": lambda n : setattr(self, 'websites', n.get_collection_of_object_values(person_website.PersonWebsite)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def interests(self,) -> Optional[List[person_interest.PersonInterest]]:
        """
        Gets the interests property value. Provides detailed information about interests the user has associated with themselves in various services.
        Returns: Optional[List[person_interest.PersonInterest]]
        """
        return self._interests
    
    @interests.setter
    def interests(self,value: Optional[List[person_interest.PersonInterest]] = None) -> None:
        """
        Sets the interests property value. Provides detailed information about interests the user has associated with themselves in various services.
        Args:
            value: Value to set for the interests property.
        """
        self._interests = value
    
    @property
    def languages(self,) -> Optional[List[language_proficiency.LanguageProficiency]]:
        """
        Gets the languages property value. Represents detailed information about languages that a user has added to their profile.
        Returns: Optional[List[language_proficiency.LanguageProficiency]]
        """
        return self._languages
    
    @languages.setter
    def languages(self,value: Optional[List[language_proficiency.LanguageProficiency]] = None) -> None:
        """
        Sets the languages property value. Represents detailed information about languages that a user has added to their profile.
        Args:
            value: Value to set for the languages property.
        """
        self._languages = value
    
    @property
    def names(self,) -> Optional[List[person_name.PersonName]]:
        """
        Gets the names property value. Represents the names a user has added to their profile.
        Returns: Optional[List[person_name.PersonName]]
        """
        return self._names
    
    @names.setter
    def names(self,value: Optional[List[person_name.PersonName]] = None) -> None:
        """
        Sets the names property value. Represents the names a user has added to their profile.
        Args:
            value: Value to set for the names property.
        """
        self._names = value
    
    @property
    def notes(self,) -> Optional[List[person_annotation.PersonAnnotation]]:
        """
        Gets the notes property value. Represents notes that a user has added to their profile.
        Returns: Optional[List[person_annotation.PersonAnnotation]]
        """
        return self._notes
    
    @notes.setter
    def notes(self,value: Optional[List[person_annotation.PersonAnnotation]] = None) -> None:
        """
        Sets the notes property value. Represents notes that a user has added to their profile.
        Args:
            value: Value to set for the notes property.
        """
        self._notes = value
    
    @property
    def patents(self,) -> Optional[List[item_patent.ItemPatent]]:
        """
        Gets the patents property value. Represents patents that a user has added to their profile.
        Returns: Optional[List[item_patent.ItemPatent]]
        """
        return self._patents
    
    @patents.setter
    def patents(self,value: Optional[List[item_patent.ItemPatent]] = None) -> None:
        """
        Sets the patents property value. Represents patents that a user has added to their profile.
        Args:
            value: Value to set for the patents property.
        """
        self._patents = value
    
    @property
    def phones(self,) -> Optional[List[item_phone.ItemPhone]]:
        """
        Gets the phones property value. Represents detailed information about phone numbers associated with a user in various services.
        Returns: Optional[List[item_phone.ItemPhone]]
        """
        return self._phones
    
    @phones.setter
    def phones(self,value: Optional[List[item_phone.ItemPhone]] = None) -> None:
        """
        Sets the phones property value. Represents detailed information about phone numbers associated with a user in various services.
        Args:
            value: Value to set for the phones property.
        """
        self._phones = value
    
    @property
    def positions(self,) -> Optional[List[work_position.WorkPosition]]:
        """
        Gets the positions property value. Represents detailed information about work positions associated with a user's profile.
        Returns: Optional[List[work_position.WorkPosition]]
        """
        return self._positions
    
    @positions.setter
    def positions(self,value: Optional[List[work_position.WorkPosition]] = None) -> None:
        """
        Sets the positions property value. Represents detailed information about work positions associated with a user's profile.
        Args:
            value: Value to set for the positions property.
        """
        self._positions = value
    
    @property
    def projects(self,) -> Optional[List[project_participation.ProjectParticipation]]:
        """
        Gets the projects property value. Represents detailed information about projects associated with a user.
        Returns: Optional[List[project_participation.ProjectParticipation]]
        """
        return self._projects
    
    @projects.setter
    def projects(self,value: Optional[List[project_participation.ProjectParticipation]] = None) -> None:
        """
        Sets the projects property value. Represents detailed information about projects associated with a user.
        Args:
            value: Value to set for the projects property.
        """
        self._projects = value
    
    @property
    def publications(self,) -> Optional[List[item_publication.ItemPublication]]:
        """
        Gets the publications property value. Represents details of any publications a user has added to their profile.
        Returns: Optional[List[item_publication.ItemPublication]]
        """
        return self._publications
    
    @publications.setter
    def publications(self,value: Optional[List[item_publication.ItemPublication]] = None) -> None:
        """
        Sets the publications property value. Represents details of any publications a user has added to their profile.
        Args:
            value: Value to set for the publications property.
        """
        self._publications = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("account", self.account)
        writer.write_collection_of_object_values("addresses", self.addresses)
        writer.write_collection_of_object_values("anniversaries", self.anniversaries)
        writer.write_collection_of_object_values("awards", self.awards)
        writer.write_collection_of_object_values("certifications", self.certifications)
        writer.write_collection_of_object_values("educationalActivities", self.educational_activities)
        writer.write_collection_of_object_values("emails", self.emails)
        writer.write_collection_of_object_values("interests", self.interests)
        writer.write_collection_of_object_values("languages", self.languages)
        writer.write_collection_of_object_values("names", self.names)
        writer.write_collection_of_object_values("notes", self.notes)
        writer.write_collection_of_object_values("patents", self.patents)
        writer.write_collection_of_object_values("phones", self.phones)
        writer.write_collection_of_object_values("positions", self.positions)
        writer.write_collection_of_object_values("projects", self.projects)
        writer.write_collection_of_object_values("publications", self.publications)
        writer.write_collection_of_object_values("skills", self.skills)
        writer.write_collection_of_object_values("webAccounts", self.web_accounts)
        writer.write_collection_of_object_values("websites", self.websites)
    
    @property
    def skills(self,) -> Optional[List[skill_proficiency.SkillProficiency]]:
        """
        Gets the skills property value. Represents detailed information about skills associated with a user in various services.
        Returns: Optional[List[skill_proficiency.SkillProficiency]]
        """
        return self._skills
    
    @skills.setter
    def skills(self,value: Optional[List[skill_proficiency.SkillProficiency]] = None) -> None:
        """
        Sets the skills property value. Represents detailed information about skills associated with a user in various services.
        Args:
            value: Value to set for the skills property.
        """
        self._skills = value
    
    @property
    def web_accounts(self,) -> Optional[List[web_account.WebAccount]]:
        """
        Gets the webAccounts property value. Represents web accounts the user has indicated they use or has added to their user profile.
        Returns: Optional[List[web_account.WebAccount]]
        """
        return self._web_accounts
    
    @web_accounts.setter
    def web_accounts(self,value: Optional[List[web_account.WebAccount]] = None) -> None:
        """
        Sets the webAccounts property value. Represents web accounts the user has indicated they use or has added to their user profile.
        Args:
            value: Value to set for the webAccounts property.
        """
        self._web_accounts = value
    
    @property
    def websites(self,) -> Optional[List[person_website.PersonWebsite]]:
        """
        Gets the websites property value. Represents detailed information about websites associated with a user in various services.
        Returns: Optional[List[person_website.PersonWebsite]]
        """
        return self._websites
    
    @websites.setter
    def websites(self,value: Optional[List[person_website.PersonWebsite]] = None) -> None:
        """
        Sets the websites property value. Represents detailed information about websites associated with a user in various services.
        Args:
            value: Value to set for the websites property.
        """
        self._websites = value
    

