from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

contact_merge_suggestions = lazy_import('msgraph.generated.models.contact_merge_suggestions')
entity = lazy_import('msgraph.generated.models.entity')
regional_and_language_settings = lazy_import('msgraph.generated.models.regional_and_language_settings')
shift_preferences = lazy_import('msgraph.generated.models.shift_preferences')
user_insights_settings = lazy_import('msgraph.generated.models.user_insights_settings')

class UserSettings(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new userSettings and sets the default values.
        """
        super().__init__()
        # The user's settings for the visibility of merge suggestion for the duplicate contacts in the user's contact list.
        self._contact_merge_suggestions: Optional[contact_merge_suggestions.ContactMergeSuggestions] = None
        # Reflects the Office Delve organization level setting. When set to true, the organization doesn't have access to Office Delve. This setting is read-only and can only be changed by administrators in the SharePoint admin center.
        self._contribution_to_content_discovery_as_organization_disabled: Optional[bool] = None
        # When set to true, documents in the user's Office Delve are disabled. Users can control this setting in Office Delve.
        self._contribution_to_content_discovery_disabled: Optional[bool] = None
        # The user's settings for the visibility of meeting hour insights, and insights derived between a user and other items in Microsoft 365, such as documents or sites. Get userInsightsSettings through this navigation property.
        self._item_insights: Optional[user_insights_settings.UserInsightsSettings] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The user's preferences for languages, regional locale and date/time formatting.
        self._regional_and_language_settings: Optional[regional_and_language_settings.RegionalAndLanguageSettings] = None
        # The shift preferences for the user.
        self._shift_preferences: Optional[shift_preferences.ShiftPreferences] = None
    
    @property
    def contact_merge_suggestions(self,) -> Optional[contact_merge_suggestions.ContactMergeSuggestions]:
        """
        Gets the contactMergeSuggestions property value. The user's settings for the visibility of merge suggestion for the duplicate contacts in the user's contact list.
        Returns: Optional[contact_merge_suggestions.ContactMergeSuggestions]
        """
        return self._contact_merge_suggestions
    
    @contact_merge_suggestions.setter
    def contact_merge_suggestions(self,value: Optional[contact_merge_suggestions.ContactMergeSuggestions] = None) -> None:
        """
        Sets the contactMergeSuggestions property value. The user's settings for the visibility of merge suggestion for the duplicate contacts in the user's contact list.
        Args:
            value: Value to set for the contactMergeSuggestions property.
        """
        self._contact_merge_suggestions = value
    
    @property
    def contribution_to_content_discovery_as_organization_disabled(self,) -> Optional[bool]:
        """
        Gets the contributionToContentDiscoveryAsOrganizationDisabled property value. Reflects the Office Delve organization level setting. When set to true, the organization doesn't have access to Office Delve. This setting is read-only and can only be changed by administrators in the SharePoint admin center.
        Returns: Optional[bool]
        """
        return self._contribution_to_content_discovery_as_organization_disabled
    
    @contribution_to_content_discovery_as_organization_disabled.setter
    def contribution_to_content_discovery_as_organization_disabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the contributionToContentDiscoveryAsOrganizationDisabled property value. Reflects the Office Delve organization level setting. When set to true, the organization doesn't have access to Office Delve. This setting is read-only and can only be changed by administrators in the SharePoint admin center.
        Args:
            value: Value to set for the contributionToContentDiscoveryAsOrganizationDisabled property.
        """
        self._contribution_to_content_discovery_as_organization_disabled = value
    
    @property
    def contribution_to_content_discovery_disabled(self,) -> Optional[bool]:
        """
        Gets the contributionToContentDiscoveryDisabled property value. When set to true, documents in the user's Office Delve are disabled. Users can control this setting in Office Delve.
        Returns: Optional[bool]
        """
        return self._contribution_to_content_discovery_disabled
    
    @contribution_to_content_discovery_disabled.setter
    def contribution_to_content_discovery_disabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the contributionToContentDiscoveryDisabled property value. When set to true, documents in the user's Office Delve are disabled. Users can control this setting in Office Delve.
        Args:
            value: Value to set for the contributionToContentDiscoveryDisabled property.
        """
        self._contribution_to_content_discovery_disabled = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UserSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "contact_merge_suggestions": lambda n : setattr(self, 'contact_merge_suggestions', n.get_object_value(contact_merge_suggestions.ContactMergeSuggestions)),
            "contribution_to_content_discovery_as_organization_disabled": lambda n : setattr(self, 'contribution_to_content_discovery_as_organization_disabled', n.get_bool_value()),
            "contribution_to_content_discovery_disabled": lambda n : setattr(self, 'contribution_to_content_discovery_disabled', n.get_bool_value()),
            "item_insights": lambda n : setattr(self, 'item_insights', n.get_object_value(user_insights_settings.UserInsightsSettings)),
            "regional_and_language_settings": lambda n : setattr(self, 'regional_and_language_settings', n.get_object_value(regional_and_language_settings.RegionalAndLanguageSettings)),
            "shift_preferences": lambda n : setattr(self, 'shift_preferences', n.get_object_value(shift_preferences.ShiftPreferences)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def item_insights(self,) -> Optional[user_insights_settings.UserInsightsSettings]:
        """
        Gets the itemInsights property value. The user's settings for the visibility of meeting hour insights, and insights derived between a user and other items in Microsoft 365, such as documents or sites. Get userInsightsSettings through this navigation property.
        Returns: Optional[user_insights_settings.UserInsightsSettings]
        """
        return self._item_insights
    
    @item_insights.setter
    def item_insights(self,value: Optional[user_insights_settings.UserInsightsSettings] = None) -> None:
        """
        Sets the itemInsights property value. The user's settings for the visibility of meeting hour insights, and insights derived between a user and other items in Microsoft 365, such as documents or sites. Get userInsightsSettings through this navigation property.
        Args:
            value: Value to set for the itemInsights property.
        """
        self._item_insights = value
    
    @property
    def regional_and_language_settings(self,) -> Optional[regional_and_language_settings.RegionalAndLanguageSettings]:
        """
        Gets the regionalAndLanguageSettings property value. The user's preferences for languages, regional locale and date/time formatting.
        Returns: Optional[regional_and_language_settings.RegionalAndLanguageSettings]
        """
        return self._regional_and_language_settings
    
    @regional_and_language_settings.setter
    def regional_and_language_settings(self,value: Optional[regional_and_language_settings.RegionalAndLanguageSettings] = None) -> None:
        """
        Sets the regionalAndLanguageSettings property value. The user's preferences for languages, regional locale and date/time formatting.
        Args:
            value: Value to set for the regionalAndLanguageSettings property.
        """
        self._regional_and_language_settings = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("contactMergeSuggestions", self.contact_merge_suggestions)
        writer.write_bool_value("contributionToContentDiscoveryAsOrganizationDisabled", self.contribution_to_content_discovery_as_organization_disabled)
        writer.write_bool_value("contributionToContentDiscoveryDisabled", self.contribution_to_content_discovery_disabled)
        writer.write_object_value("itemInsights", self.item_insights)
        writer.write_object_value("regionalAndLanguageSettings", self.regional_and_language_settings)
        writer.write_object_value("shiftPreferences", self.shift_preferences)
    
    @property
    def shift_preferences(self,) -> Optional[shift_preferences.ShiftPreferences]:
        """
        Gets the shiftPreferences property value. The shift preferences for the user.
        Returns: Optional[shift_preferences.ShiftPreferences]
        """
        return self._shift_preferences
    
    @shift_preferences.setter
    def shift_preferences(self,value: Optional[shift_preferences.ShiftPreferences] = None) -> None:
        """
        Sets the shiftPreferences property value. The shift preferences for the user.
        Args:
            value: Value to set for the shiftPreferences property.
        """
        self._shift_preferences = value
    

