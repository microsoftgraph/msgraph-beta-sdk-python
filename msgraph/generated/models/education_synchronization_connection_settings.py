from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import education_synchronization_o_auth1_connection_settings, education_synchronization_o_auth2_client_credentials_connection_settings

class EducationSynchronizationConnectionSettings(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new educationSynchronizationConnectionSettings and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Client ID used to connect to the provider.
        self._client_id: Optional[str] = None
        # Client secret to authenticate the connection to the provider.
        self._client_secret: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def client_id(self,) -> Optional[str]:
        """
        Gets the clientId property value. Client ID used to connect to the provider.
        Returns: Optional[str]
        """
        return self._client_id
    
    @client_id.setter
    def client_id(self,value: Optional[str] = None) -> None:
        """
        Sets the clientId property value. Client ID used to connect to the provider.
        Args:
            value: Value to set for the client_id property.
        """
        self._client_id = value
    
    @property
    def client_secret(self,) -> Optional[str]:
        """
        Gets the clientSecret property value. Client secret to authenticate the connection to the provider.
        Returns: Optional[str]
        """
        return self._client_secret
    
    @client_secret.setter
    def client_secret(self,value: Optional[str] = None) -> None:
        """
        Sets the clientSecret property value. Client secret to authenticate the connection to the provider.
        Args:
            value: Value to set for the client_secret property.
        """
        self._client_secret = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EducationSynchronizationConnectionSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EducationSynchronizationConnectionSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.educationSynchronizationOAuth1ConnectionSettings":
                from . import education_synchronization_o_auth1_connection_settings

                return education_synchronization_o_auth1_connection_settings.EducationSynchronizationOAuth1ConnectionSettings()
            if mapping_value == "#microsoft.graph.educationSynchronizationOAuth2ClientCredentialsConnectionSettings":
                from . import education_synchronization_o_auth2_client_credentials_connection_settings

                return education_synchronization_o_auth2_client_credentials_connection_settings.EducationSynchronizationOAuth2ClientCredentialsConnectionSettings()
        return EducationSynchronizationConnectionSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import education_synchronization_o_auth1_connection_settings, education_synchronization_o_auth2_client_credentials_connection_settings

        fields: Dict[str, Callable[[Any], None]] = {
            "clientId": lambda n : setattr(self, 'client_id', n.get_str_value()),
            "clientSecret": lambda n : setattr(self, 'client_secret', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the odata_type property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("clientId", self.client_id)
        writer.write_str_value("clientSecret", self.client_secret)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

