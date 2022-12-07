from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
insights_settings = lazy_import('msgraph.generated.models.insights_settings')
microsoft_application_data_access_settings = lazy_import('msgraph.generated.models.microsoft_application_data_access_settings')
profile_card_property = lazy_import('msgraph.generated.models.profile_card_property')

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
            value: Value to set for the contactInsights property.
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
        fields = {
            "contact_insights": lambda n : setattr(self, 'contact_insights', n.get_object_value(insights_settings.InsightsSettings)),
            "item_insights": lambda n : setattr(self, 'item_insights', n.get_object_value(insights_settings.InsightsSettings)),
            "microsoft_application_data_access": lambda n : setattr(self, 'microsoft_application_data_access', n.get_object_value(microsoft_application_data_access_settings.MicrosoftApplicationDataAccessSettings)),
            "people_insights": lambda n : setattr(self, 'people_insights', n.get_object_value(insights_settings.InsightsSettings)),
            "profile_card_properties": lambda n : setattr(self, 'profile_card_properties', n.get_collection_of_object_values(profile_card_property.ProfileCardProperty)),
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
            value: Value to set for the itemInsights property.
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
            value: Value to set for the microsoftApplicationDataAccess property.
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
            value: Value to set for the peopleInsights property.
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
            value: Value to set for the profileCardProperties property.
        """
        self._profile_card_properties = value
    
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
    

