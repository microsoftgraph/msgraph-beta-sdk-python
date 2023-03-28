from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import authentication_event_handler_result, authentication_event_type

class AppliedAuthenticationEventListener(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new appliedAuthenticationEventListener and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The type of authentication event that triggered the custom extension request. The possible values are: tokenIssuanceStart, pageRenderStart, unknownFutureValue.
        self._event_type: Optional[authentication_event_type.AuthenticationEventType] = None
        # ID of the Event Listener that was executed.
        self._executed_listener_id: Optional[str] = None
        # The result from the listening client, such as an Azure Logic App and Azure Functions, of this authentication event.
        self._handler_result: Optional[authentication_event_handler_result.AuthenticationEventHandlerResult] = None
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AppliedAuthenticationEventListener:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AppliedAuthenticationEventListener
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AppliedAuthenticationEventListener()
    
    @property
    def event_type(self,) -> Optional[authentication_event_type.AuthenticationEventType]:
        """
        Gets the eventType property value. The type of authentication event that triggered the custom extension request. The possible values are: tokenIssuanceStart, pageRenderStart, unknownFutureValue.
        Returns: Optional[authentication_event_type.AuthenticationEventType]
        """
        return self._event_type
    
    @event_type.setter
    def event_type(self,value: Optional[authentication_event_type.AuthenticationEventType] = None) -> None:
        """
        Sets the eventType property value. The type of authentication event that triggered the custom extension request. The possible values are: tokenIssuanceStart, pageRenderStart, unknownFutureValue.
        Args:
            value: Value to set for the event_type property.
        """
        self._event_type = value
    
    @property
    def executed_listener_id(self,) -> Optional[str]:
        """
        Gets the executedListenerId property value. ID of the Event Listener that was executed.
        Returns: Optional[str]
        """
        return self._executed_listener_id
    
    @executed_listener_id.setter
    def executed_listener_id(self,value: Optional[str] = None) -> None:
        """
        Sets the executedListenerId property value. ID of the Event Listener that was executed.
        Args:
            value: Value to set for the executed_listener_id property.
        """
        self._executed_listener_id = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import authentication_event_handler_result, authentication_event_type

        fields: Dict[str, Callable[[Any], None]] = {
            "eventType": lambda n : setattr(self, 'event_type', n.get_enum_value(authentication_event_type.AuthenticationEventType)),
            "executedListenerId": lambda n : setattr(self, 'executed_listener_id', n.get_str_value()),
            "handlerResult": lambda n : setattr(self, 'handler_result', n.get_object_value(authentication_event_handler_result.AuthenticationEventHandlerResult)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def handler_result(self,) -> Optional[authentication_event_handler_result.AuthenticationEventHandlerResult]:
        """
        Gets the handlerResult property value. The result from the listening client, such as an Azure Logic App and Azure Functions, of this authentication event.
        Returns: Optional[authentication_event_handler_result.AuthenticationEventHandlerResult]
        """
        return self._handler_result
    
    @handler_result.setter
    def handler_result(self,value: Optional[authentication_event_handler_result.AuthenticationEventHandlerResult] = None) -> None:
        """
        Sets the handlerResult property value. The result from the listening client, such as an Azure Logic App and Azure Functions, of this authentication event.
        Args:
            value: Value to set for the handler_result property.
        """
        self._handler_result = value
    
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
        writer.write_enum_value("eventType", self.event_type)
        writer.write_str_value("executedListenerId", self.executed_listener_id)
        writer.write_object_value("handlerResult", self.handler_result)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

