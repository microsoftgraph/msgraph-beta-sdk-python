from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import allowed_audiences, educational_activity, entity, identity_set, inference_data, item_address, item_email, item_patent, item_phone, item_publication, language_proficiency, person_annotation, person_annual_event, person_award, person_certification, person_data_sources, person_interest, person_name, person_responsibility, person_website, project_participation, skill_proficiency, user_account_information, web_account, work_position

from . import entity

@dataclass
class ItemFacet(entity.Entity):
    # The audiences that are able to see the values contained within the associated entity. Possible values are: me, family, contacts, groupMembers, organization, federatedOrganizations, everyone, unknownFutureValue.
    allowed_audiences: Optional[allowed_audiences.AllowedAudiences] = None
    # The createdBy property
    created_by: Optional[identity_set.IdentitySet] = None
    # Provides the dateTimeOffset for when the entity was created.
    created_date_time: Optional[datetime] = None
    # Contains inference detail if the entity is inferred by the creating or modifying application.
    inference: Optional[inference_data.InferenceData] = None
    # The isSearchable property
    is_searchable: Optional[bool] = None
    # The lastModifiedBy property
    last_modified_by: Optional[identity_set.IdentitySet] = None
    # Provides the dateTimeOffset for when the entity was created.
    last_modified_date_time: Optional[datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Where the values within an entity originated if synced from another service.
    source: Optional[person_data_sources.PersonDataSources] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ItemFacet:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ItemFacet
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.educationalActivity".casefold():
            from . import educational_activity

            return educational_activity.EducationalActivity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.itemAddress".casefold():
            from . import item_address

            return item_address.ItemAddress()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.itemEmail".casefold():
            from . import item_email

            return item_email.ItemEmail()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.itemPatent".casefold():
            from . import item_patent

            return item_patent.ItemPatent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.itemPhone".casefold():
            from . import item_phone

            return item_phone.ItemPhone()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.itemPublication".casefold():
            from . import item_publication

            return item_publication.ItemPublication()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.languageProficiency".casefold():
            from . import language_proficiency

            return language_proficiency.LanguageProficiency()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.personAnnotation".casefold():
            from . import person_annotation

            return person_annotation.PersonAnnotation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.personAnnualEvent".casefold():
            from . import person_annual_event

            return person_annual_event.PersonAnnualEvent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.personAward".casefold():
            from . import person_award

            return person_award.PersonAward()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.personCertification".casefold():
            from . import person_certification

            return person_certification.PersonCertification()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.personInterest".casefold():
            from . import person_interest

            return person_interest.PersonInterest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.personName".casefold():
            from . import person_name

            return person_name.PersonName()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.personResponsibility".casefold():
            from . import person_responsibility

            return person_responsibility.PersonResponsibility()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.personWebsite".casefold():
            from . import person_website

            return person_website.PersonWebsite()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.projectParticipation".casefold():
            from . import project_participation

            return project_participation.ProjectParticipation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.skillProficiency".casefold():
            from . import skill_proficiency

            return skill_proficiency.SkillProficiency()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userAccountInformation".casefold():
            from . import user_account_information

            return user_account_information.UserAccountInformation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.webAccount".casefold():
            from . import web_account

            return web_account.WebAccount()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workPosition".casefold():
            from . import work_position

            return work_position.WorkPosition()
        return ItemFacet()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import allowed_audiences, educational_activity, entity, identity_set, inference_data, item_address, item_email, item_patent, item_phone, item_publication, language_proficiency, person_annotation, person_annual_event, person_award, person_certification, person_data_sources, person_interest, person_name, person_responsibility, person_website, project_participation, skill_proficiency, user_account_information, web_account, work_position

        from . import allowed_audiences, educational_activity, entity, identity_set, inference_data, item_address, item_email, item_patent, item_phone, item_publication, language_proficiency, person_annotation, person_annual_event, person_award, person_certification, person_data_sources, person_interest, person_name, person_responsibility, person_website, project_participation, skill_proficiency, user_account_information, web_account, work_position

        fields: Dict[str, Callable[[Any], None]] = {
            "allowedAudiences": lambda n : setattr(self, 'allowed_audiences', n.get_enum_value(allowed_audiences.AllowedAudiences)),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(identity_set.IdentitySet)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "inference": lambda n : setattr(self, 'inference', n.get_object_value(inference_data.InferenceData)),
            "isSearchable": lambda n : setattr(self, 'is_searchable', n.get_bool_value()),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(identity_set.IdentitySet)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "source": lambda n : setattr(self, 'source', n.get_object_value(person_data_sources.PersonDataSources)),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_enum_value("allowedAudiences", self.allowed_audiences)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("inference", self.inference)
        writer.write_bool_value("isSearchable", self.is_searchable)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_object_value("source", self.source)
    

