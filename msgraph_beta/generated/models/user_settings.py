from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .contact_merge_suggestions import ContactMergeSuggestions
    from .entity import Entity
    from .exchange_settings import ExchangeSettings
    from .regional_and_language_settings import RegionalAndLanguageSettings
    from .shift_preferences import ShiftPreferences
    from .user_insights_settings import UserInsightsSettings
    from .user_storage import UserStorage
    from .windows_setting import WindowsSetting

from .entity import Entity

@dataclass
class UserSettings(Entity, Parsable):
    # The user's settings for the visibility of merge suggestion for the duplicate contacts in the user's contact list.
    contact_merge_suggestions: Optional[ContactMergeSuggestions] = None
    # Reflects the Office Delve organization level setting. When set to true, the organization doesn't have access to Office Delve. This setting is read-only and can only be changed by administrators in the SharePoint admin center.
    contribution_to_content_discovery_as_organization_disabled: Optional[bool] = None
    # When set to true, documents in the user's Office Delve are disabled. Users can control this setting in Office Delve.
    contribution_to_content_discovery_disabled: Optional[bool] = None
    # The Exchange settings for mailbox discovery.
    exchange: Optional[ExchangeSettings] = None
    # The user's settings for the visibility of meeting hour insights, and insights derived between a user and other items in Microsoft 365, such as documents or sites. Get userInsightsSettings through this navigation property.
    item_insights: Optional[UserInsightsSettings] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The user's preferences for languages, regional locale and date/time formatting.
    regional_and_language_settings: Optional[RegionalAndLanguageSettings] = None
    # The shift preferences for the user.
    shift_preferences: Optional[ShiftPreferences] = None
    # The storage property
    storage: Optional[UserStorage] = None
    # The Windows settings of the user stored in the cloud.
    windows: Optional[list[WindowsSetting]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UserSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UserSettings()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .contact_merge_suggestions import ContactMergeSuggestions
        from .entity import Entity
        from .exchange_settings import ExchangeSettings
        from .regional_and_language_settings import RegionalAndLanguageSettings
        from .shift_preferences import ShiftPreferences
        from .user_insights_settings import UserInsightsSettings
        from .user_storage import UserStorage
        from .windows_setting import WindowsSetting

        from .contact_merge_suggestions import ContactMergeSuggestions
        from .entity import Entity
        from .exchange_settings import ExchangeSettings
        from .regional_and_language_settings import RegionalAndLanguageSettings
        from .shift_preferences import ShiftPreferences
        from .user_insights_settings import UserInsightsSettings
        from .user_storage import UserStorage
        from .windows_setting import WindowsSetting

        fields: dict[str, Callable[[Any], None]] = {
            "contactMergeSuggestions": lambda n : setattr(self, 'contact_merge_suggestions', n.get_object_value(ContactMergeSuggestions)),
            "contributionToContentDiscoveryAsOrganizationDisabled": lambda n : setattr(self, 'contribution_to_content_discovery_as_organization_disabled', n.get_bool_value()),
            "contributionToContentDiscoveryDisabled": lambda n : setattr(self, 'contribution_to_content_discovery_disabled', n.get_bool_value()),
            "exchange": lambda n : setattr(self, 'exchange', n.get_object_value(ExchangeSettings)),
            "itemInsights": lambda n : setattr(self, 'item_insights', n.get_object_value(UserInsightsSettings)),
            "regionalAndLanguageSettings": lambda n : setattr(self, 'regional_and_language_settings', n.get_object_value(RegionalAndLanguageSettings)),
            "shiftPreferences": lambda n : setattr(self, 'shift_preferences', n.get_object_value(ShiftPreferences)),
            "storage": lambda n : setattr(self, 'storage', n.get_object_value(UserStorage)),
            "windows": lambda n : setattr(self, 'windows', n.get_collection_of_object_values(WindowsSetting)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_object_value("contactMergeSuggestions", self.contact_merge_suggestions)
        writer.write_bool_value("contributionToContentDiscoveryAsOrganizationDisabled", self.contribution_to_content_discovery_as_organization_disabled)
        writer.write_bool_value("contributionToContentDiscoveryDisabled", self.contribution_to_content_discovery_disabled)
        writer.write_object_value("exchange", self.exchange)
        writer.write_object_value("itemInsights", self.item_insights)
        writer.write_object_value("regionalAndLanguageSettings", self.regional_and_language_settings)
        writer.write_object_value("shiftPreferences", self.shift_preferences)
        writer.write_object_value("storage", self.storage)
        writer.write_collection_of_object_values("windows", self.windows)
    

