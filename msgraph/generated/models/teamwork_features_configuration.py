from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class TeamworkFeaturesConfiguration(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Email address to send logs and feedback.
    email_to_send_logs_and_feedback: Optional[str] = None
    # True if auto screen shared is enabled.
    is_auto_screen_share_enabled: Optional[bool] = None
    # True if Bluetooth beaconing is enabled.
    is_bluetooth_beaconing_enabled: Optional[bool] = None
    # True if hiding meeting names is enabled.
    is_hide_meeting_names_enabled: Optional[bool] = None
    # True if sending logs and feedback is enabled.
    is_send_logs_and_feedback_enabled: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeamworkFeaturesConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TeamworkFeaturesConfiguration
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return TeamworkFeaturesConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "emailToSendLogsAndFeedback": lambda n : setattr(self, 'email_to_send_logs_and_feedback', n.get_str_value()),
            "isAutoScreenShareEnabled": lambda n : setattr(self, 'is_auto_screen_share_enabled', n.get_bool_value()),
            "isBluetoothBeaconingEnabled": lambda n : setattr(self, 'is_bluetooth_beaconing_enabled', n.get_bool_value()),
            "isHideMeetingNamesEnabled": lambda n : setattr(self, 'is_hide_meeting_names_enabled', n.get_bool_value()),
            "isSendLogsAndFeedbackEnabled": lambda n : setattr(self, 'is_send_logs_and_feedback_enabled', n.get_bool_value()),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("emailToSendLogsAndFeedback", self.email_to_send_logs_and_feedback)
        writer.write_bool_value("isAutoScreenShareEnabled", self.is_auto_screen_share_enabled)
        writer.write_bool_value("isBluetoothBeaconingEnabled", self.is_bluetooth_beaconing_enabled)
        writer.write_bool_value("isHideMeetingNamesEnabled", self.is_hide_meeting_names_enabled)
        writer.write_bool_value("isSendLogsAndFeedbackEnabled", self.is_send_logs_and_feedback_enabled)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

