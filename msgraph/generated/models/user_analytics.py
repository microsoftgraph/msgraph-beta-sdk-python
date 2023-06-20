from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import activity_statistics, entity, settings

from . import entity

@dataclass
class UserAnalytics(entity.Entity):
    # The collection of work activities that a user spent time on during and outside of working hours. Read-only. Nullable.
    activity_statistics: Optional[List[activity_statistics.ActivityStatistics]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The current settings for a user to use the analytics API.
    settings: Optional[settings.Settings] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserAnalytics:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserAnalytics
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return UserAnalytics()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import activity_statistics, entity, settings

        from . import activity_statistics, entity, settings

        fields: Dict[str, Callable[[Any], None]] = {
            "activityStatistics": lambda n : setattr(self, 'activity_statistics', n.get_collection_of_object_values(activity_statistics.ActivityStatistics)),
            "settings": lambda n : setattr(self, 'settings', n.get_object_value(settings.Settings)),
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
        writer.write_collection_of_object_values("activityStatistics", self.activity_statistics)
        writer.write_object_value("settings", self.settings)
    

