from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class TodoSettings(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The isExternalJoinEnabled property
    is_external_join_enabled: Optional[bool] = None
    # The isExternalShareEnabled property
    is_external_share_enabled: Optional[bool] = None
    # The isPushNotificationEnabled property
    is_push_notification_enabled: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TodoSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TodoSettings
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return TodoSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "isExternalJoinEnabled": lambda n : setattr(self, 'is_external_join_enabled', n.get_bool_value()),
            "isExternalShareEnabled": lambda n : setattr(self, 'is_external_share_enabled', n.get_bool_value()),
            "isPushNotificationEnabled": lambda n : setattr(self, 'is_push_notification_enabled', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_bool_value("isExternalJoinEnabled", self.is_external_join_enabled)
        writer.write_bool_value("isExternalShareEnabled", self.is_external_share_enabled)
        writer.write_bool_value("isPushNotificationEnabled", self.is_push_notification_enabled)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

