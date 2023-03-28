from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, insights_settings, microsoft_application_data_access_settings, profile_card_property, pronouns_settings

from . import entity

class OrganizationSettings(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new organizationSettings and sets the default values.
        """
        super().__init__()
        # Contains the properties that are configured by an administrator as a tenant-level privacy control whether to identify duplicate contacts among a user's contacts list and suggest the user to merge those contacts to have a cleaner contacts list. List contactInsights returns the settings to display or return contact insights in an organization.
        self._contact_insights: Optional[insights_settings.InsightsSettings] = None
        # Contains the properties that are configured by an administrator for the visibility of Microsoft Graph-derived insights, between a user and other items in Microsoft 365, such as documents or sites. List itemInsights returns the settings to display or return item insights in an organization.
        self._item_insights: Optional[insights_settings.InsightsSettings] = None
        # The microsoftApplicationDataAccess property
        self._microsoft_application_data_access: Optional[microsoft_application_data_access_settings.MicrosoftApplicationDataAccessSettings] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Contains the properties that are configured by an administrator for the visibility of a list of people relevant and working with a user in Microsoft 365. List peopleInsights returns the settings to display or return people insights in an organization.
        self._people_insights: Optional[insights_settings.InsightsSettings] = None
        # Contains a collection of the properties an administrator has defined as visible on the Microsoft 365 profile card. Get organization settings returns the properties configured for profile cards for the organization.
        self._profile_card_properties: Optional[List[profile_card_property.ProfileCardProperty]] = None
        # Represents administrator settings that manage the support of pronouns in an organization.
        self._pronouns: Optional[pronouns_settings.PronounsSettings] = None
    
    @property
    def contact_insights(self,) -> Optional[insights_settings.InsightsSettings]:
        """
        Gets the contactInsights property value. Contains the properties that are configured by an administrator as a tenant-level privacy control whether to identify duplicate contacts among a user's contacts list and suggest the user to merge those contacts to have a cleaner contacts list. List contactInsights returns the settings to display or return contact insights in an organization.
        Returns: Optional[insights_settings.InsightsSettings]
        """
        return self._contact_insights
    
    @contact_insights.setter
    def contact_insights(self,value: Optional[insights_settings.InsightsSettings] = None) -> None:
        """
        Sets the contactInsights property value. Contains the properties that are configured by an administrator as a tenant-level privacy control whether to identify duplicate contacts among a user's contacts list and suggest the user to merge those contacts to have a cleaner contacts list. List contactInsights returns the settings to display or return contact insights in an organization.
        Args:
            value: Value to set for the contact_insights property.
        """
        self._contact_insights = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OrganizationSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OrganizationSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return OrganizationSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
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
    
    @property
    def item_insights(self,) -> Optional[insights_settings.InsightsSettings]:
        """
        Gets the itemInsights property value. Contains the properties that are configured by an administrator for the visibility of Microsoft Graph-derived insights, between a user and other items in Microsoft 365, such as documents or sites. List itemInsights returns the settings to display or return item insights in an organization.
        Returns: Optional[insights_settings.InsightsSettings]
        """
        return self._item_insights
    
    @item_insights.setter
    def item_insights(self,value: Optional[insights_settings.InsightsSettings] = None) -> None:
        """
        Sets the itemInsights property value. Contains the properties that are configured by an administrator for the visibility of Microsoft Graph-derived insights, between a user and other items in Microsoft 365, such as documents or sites. List itemInsights returns the settings to display or return item insights in an organization.
        Args:
            value: Value to set for the item_insights property.
        """
        self._item_insights = value
    
    @property
    def microsoft_application_data_access(self,) -> Optional[microsoft_application_data_access_settings.MicrosoftApplicationDataAccessSettings]:
        """
        Gets the microsoftApplicationDataAccess property value. The microsoftApplicationDataAccess property
        Returns: Optional[microsoft_application_data_access_settings.MicrosoftApplicationDataAccessSettings]
        """
        return self._microsoft_application_data_access
    
    @microsoft_application_data_access.setter
    def microsoft_application_data_access(self,value: Optional[microsoft_application_data_access_settings.MicrosoftApplicationDataAccessSettings] = None) -> None:
        """
        Sets the microsoftApplicationDataAccess property value. The microsoftApplicationDataAccess property
        Args:
            value: Value to set for the microsoft_application_data_access property.
        """
        self._microsoft_application_data_access = value
    
    @property
    def people_insights(self,) -> Optional[insights_settings.InsightsSettings]:
        """
        Gets the peopleInsights property value. Contains the properties that are configured by an administrator for the visibility of a list of people relevant and working with a user in Microsoft 365. List peopleInsights returns the settings to display or return people insights in an organization.
        Returns: Optional[insights_settings.InsightsSettings]
        """
        return self._people_insights
    
    @people_insights.setter
    def people_insights(self,value: Optional[insights_settings.InsightsSettings] = None) -> None:
        """
        Sets the peopleInsights property value. Contains the properties that are configured by an administrator for the visibility of a list of people relevant and working with a user in Microsoft 365. List peopleInsights returns the settings to display or return people insights in an organization.
        Args:
            value: Value to set for the people_insights property.
        """
        self._people_insights = value
    
    @property
    def profile_card_properties(self,) -> Optional[List[profile_card_property.ProfileCardProperty]]:
        """
        Gets the profileCardProperties property value. Contains a collection of the properties an administrator has defined as visible on the Microsoft 365 profile card. Get organization settings returns the properties configured for profile cards for the organization.
        Returns: Optional[List[profile_card_property.ProfileCardProperty]]
        """
        return self._profile_card_properties
    
    @profile_card_properties.setter
    def profile_card_properties(self,value: Optional[List[profile_card_property.ProfileCardProperty]] = None) -> None:
        """
        Sets the profileCardProperties property value. Contains a collection of the properties an administrator has defined as visible on the Microsoft 365 profile card. Get organization settings returns the properties configured for profile cards for the organization.
        Args:
            value: Value to set for the profile_card_properties property.
        """
        self._profile_card_properties = value
    
    @property
    def pronouns(self,) -> Optional[pronouns_settings.PronounsSettings]:
        """
        Gets the pronouns property value. Represents administrator settings that manage the support of pronouns in an organization.
        Returns: Optional[pronouns_settings.PronounsSettings]
        """
        return self._pronouns
    
    @pronouns.setter
    def pronouns(self,value: Optional[pronouns_settings.PronounsSettings] = None) -> None:
        """
        Sets the pronouns property value. Represents administrator settings that manage the support of pronouns in an organization.
        Args:
            value: Value to set for the pronouns property.
        """
        self._pronouns = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("contactInsights", self.contact_insights)
        writer.write_object_value("itemInsights", self.item_insights)
        writer.write_object_value("microsoftApplicationDataAccess", self.microsoft_application_data_access)
        writer.write_object_value("peopleInsights", self.people_insights)
        writer.write_collection_of_object_values("profileCardProperties", self.profile_card_properties)
        writer.write_object_value("pronouns", self.pronouns)
    

