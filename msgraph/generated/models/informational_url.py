from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class InformationalUrl(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # CDN URL to the application's logo, Read-only.
    logo_url: Optional[str] = None
    # Link to the application's marketing page. For example, https://www.contoso.com/app/marketing
    marketing_url: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Link to the application's privacy statement. For example, https://www.contoso.com/app/privacy
    privacy_statement_url: Optional[str] = None
    # Link to the application's support page. For example, https://www.contoso.com/app/support
    support_url: Optional[str] = None
    # Link to the application's terms of service statement. For example, https://www.contoso.com/app/termsofservice
    terms_of_service_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> InformationalUrl:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: InformationalUrl
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return InformationalUrl()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "logoUrl": lambda n : setattr(self, 'logo_url', n.get_str_value()),
            "marketingUrl": lambda n : setattr(self, 'marketing_url', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "privacyStatementUrl": lambda n : setattr(self, 'privacy_statement_url', n.get_str_value()),
            "supportUrl": lambda n : setattr(self, 'support_url', n.get_str_value()),
            "termsOfServiceUrl": lambda n : setattr(self, 'terms_of_service_url', n.get_str_value()),
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
        writer.write_str_value("logoUrl", self.logo_url)
        writer.write_str_value("marketingUrl", self.marketing_url)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("privacyStatementUrl", self.privacy_statement_url)
        writer.write_str_value("supportUrl", self.support_url)
        writer.write_str_value("termsOfServiceUrl", self.terms_of_service_url)
        writer.write_additional_data_value(self.additional_data)
    

