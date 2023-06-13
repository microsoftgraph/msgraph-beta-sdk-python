from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_configuration

from . import device_configuration

@dataclass
class MacOSCustomAppConfiguration(device_configuration.DeviceConfiguration):
    odata_type = "#microsoft.graph.macOSCustomAppConfiguration"
    # Bundle id for targeting.
    bundle_id: Optional[str] = None
    # Configuration xml. (UTF8 encoded byte array)
    configuration_xml: Optional[bytes] = None
    # Configuration file name (.plist
    file_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MacOSCustomAppConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MacOSCustomAppConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MacOSCustomAppConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_configuration

        fields: Dict[str, Callable[[Any], None]] = {
            "bundleId": lambda n : setattr(self, 'bundle_id', n.get_str_value()),
            "configurationXml": lambda n : setattr(self, 'configuration_xml', n.get_bytes_value()),
            "fileName": lambda n : setattr(self, 'file_name', n.get_str_value()),
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
        writer.write_str_value("bundleId", self.bundle_id)
        writer.write_object_value("configurationXml", self.configuration_xml)
        writer.write_str_value("fileName", self.file_name)
    

