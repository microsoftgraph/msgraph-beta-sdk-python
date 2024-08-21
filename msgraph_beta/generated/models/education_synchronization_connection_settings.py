from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .education_synchronization_o_auth1_connection_settings import EducationSynchronizationOAuth1ConnectionSettings
    from .education_synchronization_o_auth2_client_credentials_connection_settings import EducationSynchronizationOAuth2ClientCredentialsConnectionSettings

@dataclass
class EducationSynchronizationConnectionSettings(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Client ID used to connect to the provider.
    client_id: Optional[str] = None
    # Client secret to authenticate the connection to the provider.
    client_secret: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EducationSynchronizationConnectionSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EducationSynchronizationConnectionSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.educationSynchronizationOAuth1ConnectionSettings".casefold():
            from .education_synchronization_o_auth1_connection_settings import EducationSynchronizationOAuth1ConnectionSettings

            return EducationSynchronizationOAuth1ConnectionSettings()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.educationSynchronizationOAuth2ClientCredentialsConnectionSettings".casefold():
            from .education_synchronization_o_auth2_client_credentials_connection_settings import EducationSynchronizationOAuth2ClientCredentialsConnectionSettings

            return EducationSynchronizationOAuth2ClientCredentialsConnectionSettings()
        return EducationSynchronizationConnectionSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .education_synchronization_o_auth1_connection_settings import EducationSynchronizationOAuth1ConnectionSettings
        from .education_synchronization_o_auth2_client_credentials_connection_settings import EducationSynchronizationOAuth2ClientCredentialsConnectionSettings

        from .education_synchronization_o_auth1_connection_settings import EducationSynchronizationOAuth1ConnectionSettings
        from .education_synchronization_o_auth2_client_credentials_connection_settings import EducationSynchronizationOAuth2ClientCredentialsConnectionSettings

        fields: Dict[str, Callable[[Any], None]] = {
            "clientId": lambda n : setattr(self, 'client_id', n.get_str_value()),
            "clientSecret": lambda n : setattr(self, 'client_secret', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("clientId", self.client_id)
        writer.write_str_value("clientSecret", self.client_secret)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

