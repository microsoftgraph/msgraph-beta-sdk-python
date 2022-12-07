from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

android_device_owner_global_proxy = lazy_import('msgraph.generated.models.android_device_owner_global_proxy')

class AndroidDeviceOwnerGlobalProxyAutoConfig(android_device_owner_global_proxy.AndroidDeviceOwnerGlobalProxy):
    def __init__(self,) -> None:
        """
        Instantiates a new AndroidDeviceOwnerGlobalProxyAutoConfig and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.androidDeviceOwnerGlobalProxyAutoConfig"
        # The proxy auto-config URL
        self._proxy_auto_config_u_r_l: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AndroidDeviceOwnerGlobalProxyAutoConfig:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AndroidDeviceOwnerGlobalProxyAutoConfig
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AndroidDeviceOwnerGlobalProxyAutoConfig()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "proxy_auto_config_u_r_l": lambda n : setattr(self, 'proxy_auto_config_u_r_l', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def proxy_auto_config_u_r_l(self,) -> Optional[str]:
        """
        Gets the proxyAutoConfigURL property value. The proxy auto-config URL
        Returns: Optional[str]
        """
        return self._proxy_auto_config_u_r_l
    
    @proxy_auto_config_u_r_l.setter
    def proxy_auto_config_u_r_l(self,value: Optional[str] = None) -> None:
        """
        Sets the proxyAutoConfigURL property value. The proxy auto-config URL
        Args:
            value: Value to set for the proxyAutoConfigURL property.
        """
        self._proxy_auto_config_u_r_l = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("proxyAutoConfigURL", self.proxy_auto_config_u_r_l)
    

