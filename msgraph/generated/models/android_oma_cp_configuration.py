from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_configuration = lazy_import('msgraph.generated.models.device_configuration')

class AndroidOmaCpConfiguration(device_configuration.DeviceConfiguration):
    @property
    def configuration_xml(self,) -> Optional[bytes]:
        """
        Gets the configurationXml property value. Configuration XML that will be applied to the device. When it is read, it only provides a placeholder string since the original data is encrypted and stored.
        Returns: Optional[bytes]
        """
        return self._configuration_xml
    
    @configuration_xml.setter
    def configuration_xml(self,value: Optional[bytes] = None) -> None:
        """
        Sets the configurationXml property value. Configuration XML that will be applied to the device. When it is read, it only provides a placeholder string since the original data is encrypted and stored.
        Args:
            value: Value to set for the configurationXml property.
        """
        self._configuration_xml = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new AndroidOmaCpConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.androidOmaCpConfiguration"
        # Configuration XML that will be applied to the device. When it is read, it only provides a placeholder string since the original data is encrypted and stored.
        self._configuration_xml: Optional[bytes] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AndroidOmaCpConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AndroidOmaCpConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AndroidOmaCpConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "configuration_xml": lambda n : setattr(self, 'configuration_xml', n.get_bytes_value()),
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
        writer.write_object_value("configurationXml", self.configuration_xml)
    

