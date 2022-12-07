from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_configuration = lazy_import('msgraph.generated.models.device_configuration')

class MacOSCustomAppConfiguration(device_configuration.DeviceConfiguration):
    @property
    def bundle_id(self,) -> Optional[str]:
        """
        Gets the bundleId property value. Bundle id for targeting.
        Returns: Optional[str]
        """
        return self._bundle_id
    
    @bundle_id.setter
    def bundle_id(self,value: Optional[str] = None) -> None:
        """
        Sets the bundleId property value. Bundle id for targeting.
        Args:
            value: Value to set for the bundleId property.
        """
        self._bundle_id = value
    
    @property
    def configuration_xml(self,) -> Optional[bytes]:
        """
        Gets the configurationXml property value. Configuration xml. (UTF8 encoded byte array)
        Returns: Optional[bytes]
        """
        return self._configuration_xml
    
    @configuration_xml.setter
    def configuration_xml(self,value: Optional[bytes] = None) -> None:
        """
        Sets the configurationXml property value. Configuration xml. (UTF8 encoded byte array)
        Args:
            value: Value to set for the configurationXml property.
        """
        self._configuration_xml = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new MacOSCustomAppConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.macOSCustomAppConfiguration"
        # Bundle id for targeting.
        self._bundle_id: Optional[str] = None
        # Configuration xml. (UTF8 encoded byte array)
        self._configuration_xml: Optional[bytes] = None
        # Configuration file name (.plist
        self._file_name: Optional[str] = None
    
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
    
    @property
    def file_name(self,) -> Optional[str]:
        """
        Gets the fileName property value. Configuration file name (.plist
        Returns: Optional[str]
        """
        return self._file_name
    
    @file_name.setter
    def file_name(self,value: Optional[str] = None) -> None:
        """
        Sets the fileName property value. Configuration file name (.plist
        Args:
            value: Value to set for the fileName property.
        """
        self._file_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "bundle_id": lambda n : setattr(self, 'bundle_id', n.get_str_value()),
            "configuration_xml": lambda n : setattr(self, 'configuration_xml', n.get_bytes_value()),
            "file_name": lambda n : setattr(self, 'file_name', n.get_str_value()),
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
    

