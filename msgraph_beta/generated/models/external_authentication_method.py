from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authentication_method import AuthenticationMethod

from .authentication_method import AuthenticationMethod

@dataclass
class ExternalAuthenticationMethod(AuthenticationMethod, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.externalAuthenticationMethod"
    # The configurationId property
    configuration_id: Optional[str] = None
    # The displayName property
    display_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ExternalAuthenticationMethod:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ExternalAuthenticationMethod
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ExternalAuthenticationMethod()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .authentication_method import AuthenticationMethod

        from .authentication_method import AuthenticationMethod

        fields: dict[str, Callable[[Any], None]] = {
            "configurationId": lambda n : setattr(self, 'configuration_id', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("configurationId", self.configuration_id)
        writer.write_str_value("displayName", self.display_name)
    

