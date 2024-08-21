from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .education_synchronization_connection_settings import EducationSynchronizationConnectionSettings

from .education_synchronization_connection_settings import EducationSynchronizationConnectionSettings

@dataclass
class EducationSynchronizationOAuth2ClientCredentialsConnectionSettings(EducationSynchronizationConnectionSettings):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.educationSynchronizationOAuth2ClientCredentialsConnectionSettings"
    # The scope of the access request (see RFC6749).
    scope: Optional[str] = None
    # The URL to get access tokens for the data provider.
    token_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EducationSynchronizationOAuth2ClientCredentialsConnectionSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EducationSynchronizationOAuth2ClientCredentialsConnectionSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EducationSynchronizationOAuth2ClientCredentialsConnectionSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .education_synchronization_connection_settings import EducationSynchronizationConnectionSettings

        from .education_synchronization_connection_settings import EducationSynchronizationConnectionSettings

        fields: Dict[str, Callable[[Any], None]] = {
            "scope": lambda n : setattr(self, 'scope', n.get_str_value()),
            "tokenUrl": lambda n : setattr(self, 'token_url', n.get_str_value()),
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
        writer.write_str_value("scope", self.scope)
        writer.write_str_value("tokenUrl", self.token_url)
    

