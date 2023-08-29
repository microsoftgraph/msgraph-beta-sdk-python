from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .o_auth_app_scope import OAuthAppScope

@dataclass
class OAuthConsentAppDetail(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The appScope property
    app_scope: Optional[OAuthAppScope] = None
    # The displayLogo property
    display_logo: Optional[str] = None
    # The displayName property
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OAuthConsentAppDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OAuthConsentAppDetail
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return OAuthConsentAppDetail()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .o_auth_app_scope import OAuthAppScope

        from .o_auth_app_scope import OAuthAppScope

        fields: Dict[str, Callable[[Any], None]] = {
            "appScope": lambda n : setattr(self, 'app_scope', n.get_enum_value(OAuthAppScope)),
            "displayLogo": lambda n : setattr(self, 'display_logo', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_enum_value("appScope", self.app_scope)
        writer.write_str_value("displayLogo", self.display_logo)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

