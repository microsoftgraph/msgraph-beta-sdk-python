from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authentication_event_handler_result import AuthenticationEventHandlerResult
    from .authentication_event_type import AuthenticationEventType

@dataclass
class AppliedAuthenticationEventListener(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The type of authentication event that triggered the custom authentication extension request. The possible values are: tokenIssuanceStart, pageRenderStart, unknownFutureValue.
    event_type: Optional[AuthenticationEventType] = None
    # ID of the authentication event listener that was executed.
    executed_listener_id: Optional[str] = None
    # The result from the listening client, such as an Azure Logic App and Azure Functions, of this authentication event.
    handler_result: Optional[AuthenticationEventHandlerResult] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AppliedAuthenticationEventListener:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AppliedAuthenticationEventListener
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AppliedAuthenticationEventListener()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .authentication_event_handler_result import AuthenticationEventHandlerResult
        from .authentication_event_type import AuthenticationEventType

        from .authentication_event_handler_result import AuthenticationEventHandlerResult
        from .authentication_event_type import AuthenticationEventType

        fields: Dict[str, Callable[[Any], None]] = {
            "eventType": lambda n : setattr(self, 'event_type', n.get_enum_value(AuthenticationEventType)),
            "executedListenerId": lambda n : setattr(self, 'executed_listener_id', n.get_str_value()),
            "handlerResult": lambda n : setattr(self, 'handler_result', n.get_object_value(AuthenticationEventHandlerResult)),
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
        writer.write_enum_value("eventType", self.event_type)
        writer.write_str_value("executedListenerId", self.executed_listener_id)
        writer.write_object_value("handlerResult", self.handler_result)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

