from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import access_review_schedule_settings, entity

from . import entity

class DirectoryRoleAccessReviewPolicy(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new DirectoryRoleAccessReviewPolicy and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The settings property
        self._settings: Optional[access_review_schedule_settings.AccessReviewScheduleSettings] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DirectoryRoleAccessReviewPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DirectoryRoleAccessReviewPolicy
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DirectoryRoleAccessReviewPolicy()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import access_review_schedule_settings, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "settings": lambda n : setattr(self, 'settings', n.get_object_value(access_review_schedule_settings.AccessReviewScheduleSettings)),
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
        writer.write_object_value("settings", self.settings)
    
    @property
    def settings(self,) -> Optional[access_review_schedule_settings.AccessReviewScheduleSettings]:
        """
        Gets the settings property value. The settings property
        Returns: Optional[access_review_schedule_settings.AccessReviewScheduleSettings]
        """
        return self._settings
    
    @settings.setter
    def settings(self,value: Optional[access_review_schedule_settings.AccessReviewScheduleSettings] = None) -> None:
        """
        Sets the settings property value. The settings property
        Args:
            value: Value to set for the settings property.
        """
        self._settings = value
    

