from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import authentication_event_listener, on_attribute_collection_handler

from . import authentication_event_listener

class OnAttributeCollectionListener(authentication_event_listener.AuthenticationEventListener):
    def __init__(self,) -> None:
        """
        Instantiates a new OnAttributeCollectionListener and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.onAttributeCollectionListener"
        # Required. Configuration for what to invoke if the event resolves to this listener. This lets us define potential handler configurations per-event.
        self._handler: Optional[on_attribute_collection_handler.OnAttributeCollectionHandler] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OnAttributeCollectionListener:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OnAttributeCollectionListener
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return OnAttributeCollectionListener()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import authentication_event_listener, on_attribute_collection_handler

        fields: Dict[str, Callable[[Any], None]] = {
            "handler": lambda n : setattr(self, 'handler', n.get_object_value(on_attribute_collection_handler.OnAttributeCollectionHandler)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def handler(self,) -> Optional[on_attribute_collection_handler.OnAttributeCollectionHandler]:
        """
        Gets the handler property value. Required. Configuration for what to invoke if the event resolves to this listener. This lets us define potential handler configurations per-event.
        Returns: Optional[on_attribute_collection_handler.OnAttributeCollectionHandler]
        """
        return self._handler
    
    @handler.setter
    def handler(self,value: Optional[on_attribute_collection_handler.OnAttributeCollectionHandler] = None) -> None:
        """
        Sets the handler property value. Required. Configuration for what to invoke if the event resolves to this listener. This lets us define potential handler configurations per-event.
        Args:
            value: Value to set for the handler property.
        """
        self._handler = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("handler", self.handler)
    

