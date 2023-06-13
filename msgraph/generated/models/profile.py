from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import educational_activity, entity, item_address, item_email, item_patent, item_phone, item_publication, language_proficiency, person_annotation, person_annual_event, person_award, person_certification, person_interest, person_name, person_website, project_participation, skill_proficiency, user_account_information, web_account, work_position

from . import entity

@dataclass
class Profile(entity.Entity):
    # The account property
    account: Optional[List[user_account_information.UserAccountInformation]] = None
    # Represents details of addresses associated with the user.
    addresses: Optional[List[item_address.ItemAddress]] = None
    # Represents the details of meaningful dates associated with a person.
    anniversaries: Optional[List[person_annual_event.PersonAnnualEvent]] = None
    # Represents the details of awards or honors associated with a person.
    awards: Optional[List[person_award.PersonAward]] = None
    # Represents the details of certifications associated with a person.
    certifications: Optional[List[person_certification.PersonCertification]] = None
    # Represents data that a user has supplied related to undergraduate, graduate, postgraduate or other educational activities.
    educational_activities: Optional[List[educational_activity.EducationalActivity]] = None
    # Represents detailed information about email addresses associated with the user.
    emails: Optional[List[item_email.ItemEmail]] = None
    # Provides detailed information about interests the user has associated with themselves in various services.
    interests: Optional[List[person_interest.PersonInterest]] = None
    # Represents detailed information about languages that a user has added to their profile.
    languages: Optional[List[language_proficiency.LanguageProficiency]] = None
    # Represents the names a user has added to their profile.
    names: Optional[List[person_name.PersonName]] = None
    # Represents notes that a user has added to their profile.
    notes: Optional[List[person_annotation.PersonAnnotation]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Represents patents that a user has added to their profile.
    patents: Optional[List[item_patent.ItemPatent]] = None
    # Represents detailed information about phone numbers associated with a user in various services.
    phones: Optional[List[item_phone.ItemPhone]] = None
    # Represents detailed information about work positions associated with a user's profile.
    positions: Optional[List[work_position.WorkPosition]] = None
    # Represents detailed information about projects associated with a user.
    projects: Optional[List[project_participation.ProjectParticipation]] = None
    # Represents details of any publications a user has added to their profile.
    publications: Optional[List[item_publication.ItemPublication]] = None
    # Represents detailed information about skills associated with a user in various services.
    skills: Optional[List[skill_proficiency.SkillProficiency]] = None
    # Represents web accounts the user has indicated they use or has added to their user profile.
    web_accounts: Optional[List[web_account.WebAccount]] = None
    # Represents detailed information about websites associated with a user in various services.
    websites: Optional[List[person_website.PersonWebsite]] = None
    
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
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import educational_activity, entity, item_address, item_email, item_patent, item_phone, item_publication, language_proficiency, person_annotation, person_annual_event, person_award, person_certification, person_interest, person_name, person_website, project_participation, skill_proficiency, user_account_information, web_account, work_position

        fields: Dict[str, Callable[[Any], None]] = {
            "account": lambda n : setattr(self, 'account', n.get_collection_of_object_values(user_account_information.UserAccountInformation)),
            "addresses": lambda n : setattr(self, 'addresses', n.get_collection_of_object_values(item_address.ItemAddress)),
            "anniversaries": lambda n : setattr(self, 'anniversaries', n.get_collection_of_object_values(person_annual_event.PersonAnnualEvent)),
            "awards": lambda n : setattr(self, 'awards', n.get_collection_of_object_values(person_award.PersonAward)),
            "certifications": lambda n : setattr(self, 'certifications', n.get_collection_of_object_values(person_certification.PersonCertification)),
            "educationalActivities": lambda n : setattr(self, 'educational_activities', n.get_collection_of_object_values(educational_activity.EducationalActivity)),
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
            "websites": lambda n : setattr(self, 'websites', n.get_collection_of_object_values(person_website.PersonWebsite)),
            "webAccounts": lambda n : setattr(self, 'web_accounts', n.get_collection_of_object_values(web_account.WebAccount)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
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
        writer.write_collection_of_object_values("websites", self.websites)
        writer.write_collection_of_object_values("webAccounts", self.web_accounts)
    

