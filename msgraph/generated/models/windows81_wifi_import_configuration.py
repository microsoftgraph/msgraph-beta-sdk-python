from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_configuration = lazy_import('msgraph.generated.models.device_configuration')

class Windows81WifiImportConfiguration(device_configuration.DeviceConfiguration):
    def __init__(self,) -> None:
        """
        Instantiates a new Windows81WifiImportConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windows81WifiImportConfiguration"
        # Payload. (UTF8 encoded byte array). This is the XML file saved on the device you used to connect to the Wi-Fi endpoint.
        self._payload: Optional[bytes] = None
        # Payload file name (.xml).
        self._payload_file_name: Optional[str] = None
        # Profile name displayed in the UI.
        self._profile_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Windows81WifiImportConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Windows81WifiImportConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Windows81WifiImportConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "payload": lambda n : setattr(self, 'payload', n.get_bytes_value()),
            "payload_file_name": lambda n : setattr(self, 'payload_file_name', n.get_str_value()),
            "profile_name": lambda n : setattr(self, 'profile_name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def payload(self,) -> Optional[bytes]:
        """
        Gets the payload property value. Payload. (UTF8 encoded byte array). This is the XML file saved on the device you used to connect to the Wi-Fi endpoint.
        Returns: Optional[bytes]
        """
        return self._payload
    
    @payload.setter
    def payload(self,value: Optional[bytes] = None) -> None:
        """
        Sets the payload property value. Payload. (UTF8 encoded byte array). This is the XML file saved on the device you used to connect to the Wi-Fi endpoint.
        Args:
            value: Value to set for the payload property.
        """
        self._payload = value
    
    @property
    def payload_file_name(self,) -> Optional[str]:
        """
        Gets the payloadFileName property value. Payload file name (.xml).
        Returns: Optional[str]
        """
        return self._payload_file_name
    
    @payload_file_name.setter
    def payload_file_name(self,value: Optional[str] = None) -> None:
        """
        Sets the payloadFileName property value. Payload file name (.xml).
        Args:
            value: Value to set for the payloadFileName property.
        """
        self._payload_file_name = value
    
    @property
    def profile_name(self,) -> Optional[str]:
        """
        Gets the profileName property value. Profile name displayed in the UI.
        Returns: Optional[str]
        """
        return self._profile_name
    
    @profile_name.setter
    def profile_name(self,value: Optional[str] = None) -> None:
        """
        Sets the profileName property value. Profile name displayed in the UI.
        Args:
            value: Value to set for the profileName property.
        """
        self._profile_name = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("payload", self.payload)
        writer.write_str_value("payloadFileName", self.payload_file_name)
        writer.write_str_value("profileName", self.profile_name)
    

