from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ....models import custom_extension_authentication_configuration, custom_extension_endpoint_configuration

class ValidateAuthenticationConfigurationPostRequestBody(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new validateAuthenticationConfigurationPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The authenticationConfiguration property
        self._authentication_configuration: Optional[custom_extension_authentication_configuration.CustomExtensionAuthenticationConfiguration] = None
        # The endpointConfiguration property
        self._endpoint_configuration: Optional[custom_extension_endpoint_configuration.CustomExtensionEndpointConfiguration] = None
    
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
    def authentication_configuration(self,) -> Optional[custom_extension_authentication_configuration.CustomExtensionAuthenticationConfiguration]:
        """
        Gets the authenticationConfiguration property value. The authenticationConfiguration property
        Returns: Optional[custom_extension_authentication_configuration.CustomExtensionAuthenticationConfiguration]
        """
        return self._authentication_configuration
    
    @authentication_configuration.setter
    def authentication_configuration(self,value: Optional[custom_extension_authentication_configuration.CustomExtensionAuthenticationConfiguration] = None) -> None:
        """
        Sets the authenticationConfiguration property value. The authenticationConfiguration property
        Args:
            value: Value to set for the authentication_configuration property.
        """
        self._authentication_configuration = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ValidateAuthenticationConfigurationPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ValidateAuthenticationConfigurationPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ValidateAuthenticationConfigurationPostRequestBody()
    
    @property
    def endpoint_configuration(self,) -> Optional[custom_extension_endpoint_configuration.CustomExtensionEndpointConfiguration]:
        """
        Gets the endpointConfiguration property value. The endpointConfiguration property
        Returns: Optional[custom_extension_endpoint_configuration.CustomExtensionEndpointConfiguration]
        """
        return self._endpoint_configuration
    
    @endpoint_configuration.setter
    def endpoint_configuration(self,value: Optional[custom_extension_endpoint_configuration.CustomExtensionEndpointConfiguration] = None) -> None:
        """
        Sets the endpointConfiguration property value. The endpointConfiguration property
        Args:
            value: Value to set for the endpoint_configuration property.
        """
        self._endpoint_configuration = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ....models import custom_extension_authentication_configuration, custom_extension_endpoint_configuration

        fields: Dict[str, Callable[[Any], None]] = {
            "authenticationConfiguration": lambda n : setattr(self, 'authentication_configuration', n.get_object_value(custom_extension_authentication_configuration.CustomExtensionAuthenticationConfiguration)),
            "endpointConfiguration": lambda n : setattr(self, 'endpoint_configuration', n.get_object_value(custom_extension_endpoint_configuration.CustomExtensionEndpointConfiguration)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("authenticationConfiguration", self.authentication_configuration)
        writer.write_object_value("endpointConfiguration", self.endpoint_configuration)
        writer.write_additional_data_value(self.additional_data)
    

