from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

education_synchronization_connection_settings = lazy_import('msgraph.generated.models.education_synchronization_connection_settings')

class EducationSynchronizationOAuth2ClientCredentialsConnectionSettings(education_synchronization_connection_settings.EducationSynchronizationConnectionSettings):
    def __init__(self,) -> None:
        """
        Instantiates a new EducationSynchronizationOAuth2ClientCredentialsConnectionSettings and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.educationSynchronizationOAuth2ClientCredentialsConnectionSettings"
        # The scope of the access request (see RFC6749).
        self._scope: Optional[str] = None
        # The URL to get access tokens for the data provider.
        self._token_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EducationSynchronizationOAuth2ClientCredentialsConnectionSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EducationSynchronizationOAuth2ClientCredentialsConnectionSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EducationSynchronizationOAuth2ClientCredentialsConnectionSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "scope": lambda n : setattr(self, 'scope', n.get_str_value()),
            "token_url": lambda n : setattr(self, 'token_url', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def scope(self,) -> Optional[str]:
        """
        Gets the scope property value. The scope of the access request (see RFC6749).
        Returns: Optional[str]
        """
        return self._scope
    
    @scope.setter
    def scope(self,value: Optional[str] = None) -> None:
        """
        Sets the scope property value. The scope of the access request (see RFC6749).
        Args:
            value: Value to set for the scope property.
        """
        self._scope = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("scope", self.scope)
        writer.write_str_value("tokenUrl", self.token_url)
    
    @property
    def token_url(self,) -> Optional[str]:
        """
        Gets the tokenUrl property value. The URL to get access tokens for the data provider.
        Returns: Optional[str]
        """
        return self._token_url
    
    @token_url.setter
    def token_url(self,value: Optional[str] = None) -> None:
        """
        Sets the tokenUrl property value. The URL to get access tokens for the data provider.
        Args:
            value: Value to set for the tokenUrl property.
        """
        self._token_url = value
    

