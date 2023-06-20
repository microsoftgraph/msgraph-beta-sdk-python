from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, insights_settings, microsoft_application_data_access_settings, profile_card_property, pronouns_settings

from . import entity

@dataclass
class OrganizationSettings(entity.Entity):
    # Contains the properties that are configured by an administrator as a tenant-level privacy control whether to identify duplicate contacts among a user's contacts list and suggest the user to merge those contacts to have a cleaner contacts list. List contactInsights returns the settings to display or return contact insights in an organization.
    contact_insights: Optional[insights_settings.InsightsSettings] = None
    # Contains the properties that are configured by an administrator for the visibility of Microsoft Graph-derived insights, between a user and other items in Microsoft 365, such as documents or sites. List itemInsights returns the settings to display or return item insights in an organization.
    item_insights: Optional[insights_settings.InsightsSettings] = None
    # The microsoftApplicationDataAccess property
    microsoft_application_data_access: Optional[microsoft_application_data_access_settings.MicrosoftApplicationDataAccessSettings] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Contains the properties that are configured by an administrator for the visibility of a list of people relevant and working with a user in Microsoft 365. List peopleInsights returns the settings to display or return people insights in an organization.
    people_insights: Optional[insights_settings.InsightsSettings] = None
    # Contains a collection of the properties an administrator has defined as visible on the Microsoft 365 profile card. Get organization settings returns the properties configured for profile cards for the organization.
    profile_card_properties: Optional[List[profile_card_property.ProfileCardProperty]] = None
    # Represents administrator settings that manage the support of pronouns in an organization.
    pronouns: Optional[pronouns_settings.PronounsSettings] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OrganizationSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OrganizationSettings
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return OrganizationSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, insights_settings, microsoft_application_data_access_settings, profile_card_property, pronouns_settings

        from . import entity, insights_settings, microsoft_application_data_access_settings, profile_card_property, pronouns_settings

        fields: Dict[str, Callable[[Any], None]] = {
            "contactInsights": lambda n : setattr(self, 'contact_insights', n.get_object_value(insights_settings.InsightsSettings)),
            "itemInsights": lambda n : setattr(self, 'item_insights', n.get_object_value(insights_settings.InsightsSettings)),
            "microsoftApplicationDataAccess": lambda n : setattr(self, 'microsoft_application_data_access', n.get_object_value(microsoft_application_data_access_settings.MicrosoftApplicationDataAccessSettings)),
            "peopleInsights": lambda n : setattr(self, 'people_insights', n.get_object_value(insights_settings.InsightsSettings)),
            "profileCardProperties": lambda n : setattr(self, 'profile_card_properties', n.get_collection_of_object_values(profile_card_property.ProfileCardProperty)),
            "pronouns": lambda n : setattr(self, 'pronouns', n.get_object_value(pronouns_settings.PronounsSettings)),
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
        writer.write_object_value("contactInsights", self.contact_insights)
        writer.write_object_value("itemInsights", self.item_insights)
        writer.write_object_value("microsoftApplicationDataAccess", self.microsoft_application_data_access)
        writer.write_object_value("peopleInsights", self.people_insights)
        writer.write_collection_of_object_values("profileCardProperties", self.profile_card_properties)
        writer.write_object_value("pronouns", self.pronouns)
    

