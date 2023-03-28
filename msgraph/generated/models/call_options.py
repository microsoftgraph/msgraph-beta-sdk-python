from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import incoming_call_options, outgoing_call_options

class CallOptions(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new callOptions and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Indicates whether to hide the app after the call is escalated.
        self._hide_bot_after_escalation: Optional[bool] = None
        # Indicates whether content sharing notifications should be enabled for the call.
        self._is_content_sharing_notification_enabled: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
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
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CallOptions:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CallOptions
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.incomingCallOptions":
                from . import incoming_call_options

                return incoming_call_options.IncomingCallOptions()
            if mapping_value == "#microsoft.graph.outgoingCallOptions":
                from . import outgoing_call_options

                return outgoing_call_options.OutgoingCallOptions()
        return CallOptions()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import incoming_call_options, outgoing_call_options

        fields: Dict[str, Callable[[Any], None]] = {
            "hideBotAfterEscalation": lambda n : setattr(self, 'hide_bot_after_escalation', n.get_bool_value()),
            "isContentSharingNotificationEnabled": lambda n : setattr(self, 'is_content_sharing_notification_enabled', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def hide_bot_after_escalation(self,) -> Optional[bool]:
        """
        Gets the hideBotAfterEscalation property value. Indicates whether to hide the app after the call is escalated.
        Returns: Optional[bool]
        """
        return self._hide_bot_after_escalation
    
    @hide_bot_after_escalation.setter
    def hide_bot_after_escalation(self,value: Optional[bool] = None) -> None:
        """
        Sets the hideBotAfterEscalation property value. Indicates whether to hide the app after the call is escalated.
        Args:
            value: Value to set for the hide_bot_after_escalation property.
        """
        self._hide_bot_after_escalation = value
    
    @property
    def is_content_sharing_notification_enabled(self,) -> Optional[bool]:
        """
        Gets the isContentSharingNotificationEnabled property value. Indicates whether content sharing notifications should be enabled for the call.
        Returns: Optional[bool]
        """
        return self._is_content_sharing_notification_enabled
    
    @is_content_sharing_notification_enabled.setter
    def is_content_sharing_notification_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isContentSharingNotificationEnabled property value. Indicates whether content sharing notifications should be enabled for the call.
        Args:
            value: Value to set for the is_content_sharing_notification_enabled property.
        """
        self._is_content_sharing_notification_enabled = value
    
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
            value: Value to set for the odata_type property.
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
        writer.write_bool_value("hideBotAfterEscalation", self.hide_bot_after_escalation)
        writer.write_bool_value("isContentSharingNotificationEnabled", self.is_content_sharing_notification_enabled)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

