from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import android_managed_store_auto_update_mode, mobile_app_assignment_settings

from . import mobile_app_assignment_settings

@dataclass
class AndroidManagedStoreAppAssignmentSettings(mobile_app_assignment_settings.MobileAppAssignmentSettings):
    odata_type = "#microsoft.graph.androidManagedStoreAppAssignmentSettings"
    # The track IDs to enable for this app assignment.
    android_managed_store_app_track_ids: Optional[List[str]] = None
    # Prioritization for automatic updates of Android Managed Store apps set on assignment.
    auto_update_mode: Optional[android_managed_store_auto_update_mode.AndroidManagedStoreAutoUpdateMode] = None
    
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
        from . import android_managed_store_auto_update_mode, mobile_app_assignment_settings

        fields: Dict[str, Callable[[Any], None]] = {
            "androidManagedStoreAppTrackIds": lambda n : setattr(self, 'android_managed_store_app_track_ids', n.get_collection_of_primitive_values(str)),
            "autoUpdateMode": lambda n : setattr(self, 'auto_update_mode', n.get_enum_value(android_managed_store_auto_update_mode.AndroidManagedStoreAutoUpdateMode)),
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
    

