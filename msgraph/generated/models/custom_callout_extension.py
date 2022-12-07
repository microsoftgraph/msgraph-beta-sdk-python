from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

custom_extension_authentication_configuration = lazy_import('msgraph.generated.models.custom_extension_authentication_configuration')
custom_extension_client_configuration = lazy_import('msgraph.generated.models.custom_extension_client_configuration')
custom_extension_endpoint_configuration = lazy_import('msgraph.generated.models.custom_extension_endpoint_configuration')
entity = lazy_import('msgraph.generated.models.entity')

class CustomCalloutExtension(entity.Entity):
    """
    Provides operations to manage the collection of accessReviewDecision entities.
    """
    @property
    def authentication_configuration(self,) -> Optional[custom_extension_authentication_configuration.CustomExtensionAuthenticationConfiguration]:
        """
        Gets the authenticationConfiguration property value. Configuration for securing the API call to the logic app. For example, using OAuth client credentials flow.
        Returns: Optional[custom_extension_authentication_configuration.CustomExtensionAuthenticationConfiguration]
        """
        return self._authentication_configuration
    
    @authentication_configuration.setter
    def authentication_configuration(self,value: Optional[custom_extension_authentication_configuration.CustomExtensionAuthenticationConfiguration] = None) -> None:
        """
        Sets the authenticationConfiguration property value. Configuration for securing the API call to the logic app. For example, using OAuth client credentials flow.
        Args:
            value: Value to set for the authenticationConfiguration property.
        """
        self._authentication_configuration = value
    
    @property
    def client_configuration(self,) -> Optional[custom_extension_client_configuration.CustomExtensionClientConfiguration]:
        """
        Gets the clientConfiguration property value. HTTP connection settings that define how long Azure AD can wait for a connection to a logic app, how many times you can retry a timed-out connection and the exception scenarios when retries are allowed.
        Returns: Optional[custom_extension_client_configuration.CustomExtensionClientConfiguration]
        """
        return self._client_configuration
    
    @client_configuration.setter
    def client_configuration(self,value: Optional[custom_extension_client_configuration.CustomExtensionClientConfiguration] = None) -> None:
        """
        Sets the clientConfiguration property value. HTTP connection settings that define how long Azure AD can wait for a connection to a logic app, how many times you can retry a timed-out connection and the exception scenarios when retries are allowed.
        Args:
            value: Value to set for the clientConfiguration property.
        """
        self._client_configuration = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new customCalloutExtension and sets the default values.
        """
        super().__init__()
        # Configuration for securing the API call to the logic app. For example, using OAuth client credentials flow.
        self._authentication_configuration: Optional[custom_extension_authentication_configuration.CustomExtensionAuthenticationConfiguration] = None
        # HTTP connection settings that define how long Azure AD can wait for a connection to a logic app, how many times you can retry a timed-out connection and the exception scenarios when retries are allowed.
        self._client_configuration: Optional[custom_extension_client_configuration.CustomExtensionClientConfiguration] = None
        # Description for the customCalloutExtension object.
        self._description: Optional[str] = None
        # Display name for the customCalloutExtension object.
        self._display_name: Optional[str] = None
        # The type and details for configuring the endpoint to call the logic app's workflow.
        self._endpoint_configuration: Optional[custom_extension_endpoint_configuration.CustomExtensionEndpointConfiguration] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CustomCalloutExtension:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CustomCalloutExtension
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CustomCalloutExtension()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. Description for the customCalloutExtension object.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. Description for the customCalloutExtension object.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Display name for the customCalloutExtension object.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Display name for the customCalloutExtension object.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def endpoint_configuration(self,) -> Optional[custom_extension_endpoint_configuration.CustomExtensionEndpointConfiguration]:
        """
        Gets the endpointConfiguration property value. The type and details for configuring the endpoint to call the logic app's workflow.
        Returns: Optional[custom_extension_endpoint_configuration.CustomExtensionEndpointConfiguration]
        """
        return self._endpoint_configuration
    
    @endpoint_configuration.setter
    def endpoint_configuration(self,value: Optional[custom_extension_endpoint_configuration.CustomExtensionEndpointConfiguration] = None) -> None:
        """
        Sets the endpointConfiguration property value. The type and details for configuring the endpoint to call the logic app's workflow.
        Args:
            value: Value to set for the endpointConfiguration property.
        """
        self._endpoint_configuration = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "authentication_configuration": lambda n : setattr(self, 'authentication_configuration', n.get_object_value(custom_extension_authentication_configuration.CustomExtensionAuthenticationConfiguration)),
            "client_configuration": lambda n : setattr(self, 'client_configuration', n.get_object_value(custom_extension_client_configuration.CustomExtensionClientConfiguration)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "endpoint_configuration": lambda n : setattr(self, 'endpoint_configuration', n.get_object_value(custom_extension_endpoint_configuration.CustomExtensionEndpointConfiguration)),
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
        writer.write_object_value("authenticationConfiguration", self.authentication_configuration)
        writer.write_object_value("clientConfiguration", self.client_configuration)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("endpointConfiguration", self.endpoint_configuration)
    

