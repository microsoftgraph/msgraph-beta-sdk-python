from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

activity_statistics = lazy_import('msgraph.generated.models.activity_statistics')
entity = lazy_import('msgraph.generated.models.entity')
settings = lazy_import('msgraph.generated.models.settings')

class UserAnalytics(entity.Entity):
    @property
    def activity_statistics(self,) -> Optional[List[activity_statistics.ActivityStatistics]]:
        """
        Gets the activityStatistics property value. The collection of work activities that a user spent time on during and outside of working hours. Read-only. Nullable.
        Returns: Optional[List[activity_statistics.ActivityStatistics]]
        """
        return self._activity_statistics
    
    @activity_statistics.setter
    def activity_statistics(self,value: Optional[List[activity_statistics.ActivityStatistics]] = None) -> None:
        """
        Sets the activityStatistics property value. The collection of work activities that a user spent time on during and outside of working hours. Read-only. Nullable.
        Args:
            value: Value to set for the activityStatistics property.
        """
        self._activity_statistics = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new userAnalytics and sets the default values.
        """
        super().__init__()
        # The collection of work activities that a user spent time on during and outside of working hours. Read-only. Nullable.
        self._activity_statistics: Optional[List[activity_statistics.ActivityStatistics]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The current settings for a user to use the analytics API.
        self._settings: Optional[settings.Settings] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserAnalytics:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserAnalytics
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UserAnalytics()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "activity_statistics": lambda n : setattr(self, 'activity_statistics', n.get_collection_of_object_values(activity_statistics.ActivityStatistics)),
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
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("activityStatistics", self.activity_statistics)
        writer.write_object_value("settings", self.settings)
    
    @property
    def settings(self,) -> Optional[settings.Settings]:
        """
        Gets the settings property value. The current settings for a user to use the analytics API.
        Returns: Optional[settings.Settings]
        """
        return self._settings
    
    @settings.setter
    def settings(self,value: Optional[settings.Settings] = None) -> None:
        """
        Sets the settings property value. The current settings for a user to use the analytics API.
        Args:
            value: Value to set for the settings property.
        """
        self._settings = value
    

