from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_management_troubleshooting_event = lazy_import('msgraph.generated.models.device_management_troubleshooting_event')

class AppleVppTokenTroubleshootingEvent(device_management_troubleshooting_event.DeviceManagementTroubleshootingEvent):
    def __init__(self,) -> None:
        """
        Instantiates a new AppleVppTokenTroubleshootingEvent and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Apple Volume Purchase Program Token Identifier.
        self._token_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AppleVppTokenTroubleshootingEvent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AppleVppTokenTroubleshootingEvent
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AppleVppTokenTroubleshootingEvent()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "token_id": lambda n : setattr(self, 'token_id', n.get_str_value()),
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
        writer.write_str_value("tokenId", self.token_id)
    
    @property
    def token_id(self,) -> Optional[str]:
        """
        Gets the tokenId property value. Apple Volume Purchase Program Token Identifier.
        Returns: Optional[str]
        """
        return self._token_id
    
    @token_id.setter
    def token_id(self,value: Optional[str] = None) -> None:
        """
        Sets the tokenId property value. Apple Volume Purchase Program Token Identifier.
        Args:
            value: Value to set for the tokenId property.
        """
        self._token_id = value
    

