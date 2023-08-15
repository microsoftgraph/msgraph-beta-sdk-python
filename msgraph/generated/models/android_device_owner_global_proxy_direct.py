from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .android_device_owner_global_proxy import AndroidDeviceOwnerGlobalProxy

from .android_device_owner_global_proxy import AndroidDeviceOwnerGlobalProxy

@dataclass
class AndroidDeviceOwnerGlobalProxyDirect(AndroidDeviceOwnerGlobalProxy):
    """
    Android Device Owner Global Proxy Direct.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.androidDeviceOwnerGlobalProxyDirect"
    # The excluded hosts
    excluded_hosts: Optional[List[str]] = None
    # The host name
    host: Optional[str] = None
    # The port
    port: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AndroidDeviceOwnerGlobalProxyDirect:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AndroidDeviceOwnerGlobalProxyDirect
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AndroidDeviceOwnerGlobalProxyDirect()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .android_device_owner_global_proxy import AndroidDeviceOwnerGlobalProxy

        from .android_device_owner_global_proxy import AndroidDeviceOwnerGlobalProxy

        fields: Dict[str, Callable[[Any], None]] = {
            "excludedHosts": lambda n : setattr(self, 'excluded_hosts', n.get_collection_of_primitive_values(str)),
            "host": lambda n : setattr(self, 'host', n.get_str_value()),
            "port": lambda n : setattr(self, 'port', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_primitive_values("excludedHosts", self.excluded_hosts)
        writer.write_str_value("host", self.host)
        writer.write_int_value("port", self.port)
    

