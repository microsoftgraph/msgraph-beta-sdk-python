from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class TeamworkFeaturesConfiguration(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new teamworkFeaturesConfiguration and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Email address to send logs and feedback.
        self._email_to_send_logs_and_feedback: Optional[str] = None
        # True if auto screen shared is enabled.
        self._is_auto_screen_share_enabled: Optional[bool] = None
        # True if Bluetooth beaconing is enabled.
        self._is_bluetooth_beaconing_enabled: Optional[bool] = None
        # True if hiding meeting names is enabled.
        self._is_hide_meeting_names_enabled: Optional[bool] = None
        # True if sending logs and feedback is enabled.
        self._is_send_logs_and_feedback_enabled: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeamworkFeaturesConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TeamworkFeaturesConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TeamworkFeaturesConfiguration()
    
    @property
    def email_to_send_logs_and_feedback(self,) -> Optional[str]:
        """
        Gets the emailToSendLogsAndFeedback property value. Email address to send logs and feedback.
        Returns: Optional[str]
        """
        return self._email_to_send_logs_and_feedback
    
    @email_to_send_logs_and_feedback.setter
    def email_to_send_logs_and_feedback(self,value: Optional[str] = None) -> None:
        """
        Sets the emailToSendLogsAndFeedback property value. Email address to send logs and feedback.
        Args:
            value: Value to set for the emailToSendLogsAndFeedback property.
        """
        self._email_to_send_logs_and_feedback = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "email_to_send_logs_and_feedback": lambda n : setattr(self, 'email_to_send_logs_and_feedback', n.get_str_value()),
            "is_auto_screen_share_enabled": lambda n : setattr(self, 'is_auto_screen_share_enabled', n.get_bool_value()),
            "is_bluetooth_beaconing_enabled": lambda n : setattr(self, 'is_bluetooth_beaconing_enabled', n.get_bool_value()),
            "is_hide_meeting_names_enabled": lambda n : setattr(self, 'is_hide_meeting_names_enabled', n.get_bool_value()),
            "is_send_logs_and_feedback_enabled": lambda n : setattr(self, 'is_send_logs_and_feedback_enabled', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def is_auto_screen_share_enabled(self,) -> Optional[bool]:
        """
        Gets the isAutoScreenShareEnabled property value. True if auto screen shared is enabled.
        Returns: Optional[bool]
        """
        return self._is_auto_screen_share_enabled
    
    @is_auto_screen_share_enabled.setter
    def is_auto_screen_share_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isAutoScreenShareEnabled property value. True if auto screen shared is enabled.
        Args:
            value: Value to set for the isAutoScreenShareEnabled property.
        """
        self._is_auto_screen_share_enabled = value
    
    @property
    def is_bluetooth_beaconing_enabled(self,) -> Optional[bool]:
        """
        Gets the isBluetoothBeaconingEnabled property value. True if Bluetooth beaconing is enabled.
        Returns: Optional[bool]
        """
        return self._is_bluetooth_beaconing_enabled
    
    @is_bluetooth_beaconing_enabled.setter
    def is_bluetooth_beaconing_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isBluetoothBeaconingEnabled property value. True if Bluetooth beaconing is enabled.
        Args:
            value: Value to set for the isBluetoothBeaconingEnabled property.
        """
        self._is_bluetooth_beaconing_enabled = value
    
    @property
    def is_hide_meeting_names_enabled(self,) -> Optional[bool]:
        """
        Gets the isHideMeetingNamesEnabled property value. True if hiding meeting names is enabled.
        Returns: Optional[bool]
        """
        return self._is_hide_meeting_names_enabled
    
    @is_hide_meeting_names_enabled.setter
    def is_hide_meeting_names_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isHideMeetingNamesEnabled property value. True if hiding meeting names is enabled.
        Args:
            value: Value to set for the isHideMeetingNamesEnabled property.
        """
        self._is_hide_meeting_names_enabled = value
    
    @property
    def is_send_logs_and_feedback_enabled(self,) -> Optional[bool]:
        """
        Gets the isSendLogsAndFeedbackEnabled property value. True if sending logs and feedback is enabled.
        Returns: Optional[bool]
        """
        return self._is_send_logs_and_feedback_enabled
    
    @is_send_logs_and_feedback_enabled.setter
    def is_send_logs_and_feedback_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isSendLogsAndFeedbackEnabled property value. True if sending logs and feedback is enabled.
        Args:
            value: Value to set for the isSendLogsAndFeedbackEnabled property.
        """
        self._is_send_logs_and_feedback_enabled = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("emailToSendLogsAndFeedback", self.email_to_send_logs_and_feedback)
        writer.write_bool_value("isAutoScreenShareEnabled", self.is_auto_screen_share_enabled)
        writer.write_bool_value("isBluetoothBeaconingEnabled", self.is_bluetooth_beaconing_enabled)
        writer.write_bool_value("isHideMeetingNamesEnabled", self.is_hide_meeting_names_enabled)
        writer.write_bool_value("isSendLogsAndFeedbackEnabled", self.is_send_logs_and_feedback_enabled)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

