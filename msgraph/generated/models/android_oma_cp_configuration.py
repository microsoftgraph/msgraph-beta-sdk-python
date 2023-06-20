from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_configuration

from . import device_configuration

@dataclass
class AndroidOmaCpConfiguration(device_configuration.DeviceConfiguration):
    odata_type = "#microsoft.graph.androidOmaCpConfiguration"
    # Configuration XML that will be applied to the device. When it is read, it only provides a placeholder string since the original data is encrypted and stored.
    configuration_xml: Optional[bytes] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AndroidOmaCpConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AndroidOmaCpConfiguration
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AndroidOmaCpConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_configuration

        from . import device_configuration

        fields: Dict[str, Callable[[Any], None]] = {
            "configurationXml": lambda n : setattr(self, 'configuration_xml', n.get_bytes_value()),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_object_value("configurationXml", self.configuration_xml)
    

