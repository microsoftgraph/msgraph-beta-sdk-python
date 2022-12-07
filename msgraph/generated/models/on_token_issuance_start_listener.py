from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

authentication_event_listener = lazy_import('msgraph.generated.models.authentication_event_listener')
on_token_issuance_start_handler = lazy_import('msgraph.generated.models.on_token_issuance_start_handler')

class OnTokenIssuanceStartListener(authentication_event_listener.AuthenticationEventListener):
    def __init__(self,) -> None:
        """
        Instantiates a new OnTokenIssuanceStartListener and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.onTokenIssuanceStartListener"
        # The handler property
        self._handler: Optional[on_token_issuance_start_handler.OnTokenIssuanceStartHandler] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OnTokenIssuanceStartListener:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OnTokenIssuanceStartListener
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return OnTokenIssuanceStartListener()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "handler": lambda n : setattr(self, 'handler', n.get_object_value(on_token_issuance_start_handler.OnTokenIssuanceStartHandler)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def handler(self,) -> Optional[on_token_issuance_start_handler.OnTokenIssuanceStartHandler]:
        """
        Gets the handler property value. The handler property
        Returns: Optional[on_token_issuance_start_handler.OnTokenIssuanceStartHandler]
        """
        return self._handler
    
    @handler.setter
    def handler(self,value: Optional[on_token_issuance_start_handler.OnTokenIssuanceStartHandler] = None) -> None:
        """
        Sets the handler property value. The handler property
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
    

