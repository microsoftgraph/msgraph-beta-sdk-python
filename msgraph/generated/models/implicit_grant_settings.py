from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class ImplicitGrantSettings(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Specifies whether this web application can request an access token using the OAuth 2.0 implicit flow.
    enable_access_token_issuance: Optional[bool] = None
    # Specifies whether this web application can request an ID token using the OAuth 2.0 implicit flow.
    enable_id_token_issuance: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ImplicitGrantSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ImplicitGrantSettings
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ImplicitGrantSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "enableAccessTokenIssuance": lambda n : setattr(self, 'enable_access_token_issuance', n.get_bool_value()),
            "enableIdTokenIssuance": lambda n : setattr(self, 'enable_id_token_issuance', n.get_bool_value()),
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
        writer.write_bool_value("enableAccessTokenIssuance", self.enable_access_token_issuance)
        writer.write_bool_value("enableIdTokenIssuance", self.enable_id_token_issuance)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

