from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

android_device_owner_global_proxy = lazy_import('msgraph.generated.models.android_device_owner_global_proxy')

class AndroidDeviceOwnerGlobalProxyDirect(android_device_owner_global_proxy.AndroidDeviceOwnerGlobalProxy):
    def __init__(self,) -> None:
        """
        Instantiates a new AndroidDeviceOwnerGlobalProxyDirect and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.androidDeviceOwnerGlobalProxyDirect"
        # The excluded hosts
        self._excluded_hosts: Optional[List[str]] = None
        # The host name
        self._host: Optional[str] = None
        # The port
        self._port: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AndroidDeviceOwnerGlobalProxyDirect:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AndroidDeviceOwnerGlobalProxyDirect
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AndroidDeviceOwnerGlobalProxyDirect()
    
    @property
    def excluded_hosts(self,) -> Optional[List[str]]:
        """
        Gets the excludedHosts property value. The excluded hosts
        Returns: Optional[List[str]]
        """
        return self._excluded_hosts
    
    @excluded_hosts.setter
    def excluded_hosts(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the excludedHosts property value. The excluded hosts
        Args:
            value: Value to set for the excludedHosts property.
        """
        self._excluded_hosts = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "excluded_hosts": lambda n : setattr(self, 'excluded_hosts', n.get_collection_of_primitive_values(str)),
            "host": lambda n : setattr(self, 'host', n.get_str_value()),
            "port": lambda n : setattr(self, 'port', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def host(self,) -> Optional[str]:
        """
        Gets the host property value. The host name
        Returns: Optional[str]
        """
        return self._host
    
    @host.setter
    def host(self,value: Optional[str] = None) -> None:
        """
        Sets the host property value. The host name
        Args:
            value: Value to set for the host property.
        """
        self._host = value
    
    @property
    def port(self,) -> Optional[int]:
        """
        Gets the port property value. The port
        Returns: Optional[int]
        """
        return self._port
    
    @port.setter
    def port(self,value: Optional[int] = None) -> None:
        """
        Sets the port property value. The port
        Args:
            value: Value to set for the port property.
        """
        self._port = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_primitive_values("excludedHosts", self.excluded_hosts)
        writer.write_str_value("host", self.host)
        writer.write_int_value("port", self.port)
    

