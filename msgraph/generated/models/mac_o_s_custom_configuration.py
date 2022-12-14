from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

apple_deployment_channel = lazy_import('msgraph.generated.models.apple_deployment_channel')
device_configuration = lazy_import('msgraph.generated.models.device_configuration')

class MacOSCustomConfiguration(device_configuration.DeviceConfiguration):
    def __init__(self,) -> None:
        """
        Instantiates a new MacOSCustomConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.macOSCustomConfiguration"
        # Indicates the channel used to deploy the configuration profile. Available choices are DeviceChannel, UserChannel
        self._deployment_channel: Optional[apple_deployment_channel.AppleDeploymentChannel] = None
        # Payload. (UTF8 encoded byte array)
        self._payload: Optional[bytes] = None
        # Payload file name (.mobileconfig
        self._payload_file_name: Optional[str] = None
        # Name that is displayed to the user.
        self._payload_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MacOSCustomConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MacOSCustomConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MacOSCustomConfiguration()
    
    @property
    def deployment_channel(self,) -> Optional[apple_deployment_channel.AppleDeploymentChannel]:
        """
        Gets the deploymentChannel property value. Indicates the channel used to deploy the configuration profile. Available choices are DeviceChannel, UserChannel
        Returns: Optional[apple_deployment_channel.AppleDeploymentChannel]
        """
        return self._deployment_channel
    
    @deployment_channel.setter
    def deployment_channel(self,value: Optional[apple_deployment_channel.AppleDeploymentChannel] = None) -> None:
        """
        Sets the deploymentChannel property value. Indicates the channel used to deploy the configuration profile. Available choices are DeviceChannel, UserChannel
        Args:
            value: Value to set for the deploymentChannel property.
        """
        self._deployment_channel = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "deployment_channel": lambda n : setattr(self, 'deployment_channel', n.get_enum_value(apple_deployment_channel.AppleDeploymentChannel)),
            "payload": lambda n : setattr(self, 'payload', n.get_bytes_value()),
            "payload_file_name": lambda n : setattr(self, 'payload_file_name', n.get_str_value()),
            "payload_name": lambda n : setattr(self, 'payload_name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def payload(self,) -> Optional[bytes]:
        """
        Gets the payload property value. Payload. (UTF8 encoded byte array)
        Returns: Optional[bytes]
        """
        return self._payload
    
    @payload.setter
    def payload(self,value: Optional[bytes] = None) -> None:
        """
        Sets the payload property value. Payload. (UTF8 encoded byte array)
        Args:
            value: Value to set for the payload property.
        """
        self._payload = value
    
    @property
    def payload_file_name(self,) -> Optional[str]:
        """
        Gets the payloadFileName property value. Payload file name (.mobileconfig
        Returns: Optional[str]
        """
        return self._payload_file_name
    
    @payload_file_name.setter
    def payload_file_name(self,value: Optional[str] = None) -> None:
        """
        Sets the payloadFileName property value. Payload file name (.mobileconfig
        Args:
            value: Value to set for the payloadFileName property.
        """
        self._payload_file_name = value
    
    @property
    def payload_name(self,) -> Optional[str]:
        """
        Gets the payloadName property value. Name that is displayed to the user.
        Returns: Optional[str]
        """
        return self._payload_name
    
    @payload_name.setter
    def payload_name(self,value: Optional[str] = None) -> None:
        """
        Sets the payloadName property value. Name that is displayed to the user.
        Args:
            value: Value to set for the payloadName property.
        """
        self._payload_name = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("deploymentChannel", self.deployment_channel)
        writer.write_object_value("payload", self.payload)
        writer.write_str_value("payloadFileName", self.payload_file_name)
        writer.write_str_value("payloadName", self.payload_name)
    

