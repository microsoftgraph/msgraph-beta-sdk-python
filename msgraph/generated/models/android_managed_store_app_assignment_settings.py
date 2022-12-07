from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

android_managed_store_auto_update_mode = lazy_import('msgraph.generated.models.android_managed_store_auto_update_mode')
mobile_app_assignment_settings = lazy_import('msgraph.generated.models.mobile_app_assignment_settings')

class AndroidManagedStoreAppAssignmentSettings(mobile_app_assignment_settings.MobileAppAssignmentSettings):
    @property
    def android_managed_store_app_track_ids(self,) -> Optional[List[str]]:
        """
        Gets the androidManagedStoreAppTrackIds property value. The track IDs to enable for this app assignment.
        Returns: Optional[List[str]]
        """
        return self._android_managed_store_app_track_ids
    
    @android_managed_store_app_track_ids.setter
    def android_managed_store_app_track_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the androidManagedStoreAppTrackIds property value. The track IDs to enable for this app assignment.
        Args:
            value: Value to set for the androidManagedStoreAppTrackIds property.
        """
        self._android_managed_store_app_track_ids = value
    
    @property
    def auto_update_mode(self,) -> Optional[android_managed_store_auto_update_mode.AndroidManagedStoreAutoUpdateMode]:
        """
        Gets the autoUpdateMode property value. Prioritization for automatic updates of Android Managed Store apps set on assignment.
        Returns: Optional[android_managed_store_auto_update_mode.AndroidManagedStoreAutoUpdateMode]
        """
        return self._auto_update_mode
    
    @auto_update_mode.setter
    def auto_update_mode(self,value: Optional[android_managed_store_auto_update_mode.AndroidManagedStoreAutoUpdateMode] = None) -> None:
        """
        Sets the autoUpdateMode property value. Prioritization for automatic updates of Android Managed Store apps set on assignment.
        Args:
            value: Value to set for the autoUpdateMode property.
        """
        self._auto_update_mode = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new AndroidManagedStoreAppAssignmentSettings and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.androidManagedStoreAppAssignmentSettings"
        # The track IDs to enable for this app assignment.
        self._android_managed_store_app_track_ids: Optional[List[str]] = None
        # Prioritization for automatic updates of Android Managed Store apps set on assignment.
        self._auto_update_mode: Optional[android_managed_store_auto_update_mode.AndroidManagedStoreAutoUpdateMode] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AndroidManagedStoreAppAssignmentSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AndroidManagedStoreAppAssignmentSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AndroidManagedStoreAppAssignmentSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "android_managed_store_app_track_ids": lambda n : setattr(self, 'android_managed_store_app_track_ids', n.get_collection_of_primitive_values(str)),
            "auto_update_mode": lambda n : setattr(self, 'auto_update_mode', n.get_enum_value(android_managed_store_auto_update_mode.AndroidManagedStoreAutoUpdateMode)),
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
        writer.write_collection_of_primitive_values("androidManagedStoreAppTrackIds", self.android_managed_store_app_track_ids)
        writer.write_enum_value("autoUpdateMode", self.auto_update_mode)
    

