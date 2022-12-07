from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class VpnDnsRule(AdditionalDataHolder, Parsable):
    """
    VPN DNS Rule definition.
    """
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def auto_trigger(self,) -> Optional[bool]:
        """
        Gets the autoTrigger property value. Automatically connect to the VPN when the device connects to this domain: Default False.
        Returns: Optional[bool]
        """
        return self._auto_trigger
    
    @auto_trigger.setter
    def auto_trigger(self,value: Optional[bool] = None) -> None:
        """
        Sets the autoTrigger property value. Automatically connect to the VPN when the device connects to this domain: Default False.
        Args:
            value: Value to set for the autoTrigger property.
        """
        self._auto_trigger = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new vpnDnsRule and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Automatically connect to the VPN when the device connects to this domain: Default False.
        self._auto_trigger: Optional[bool] = None
        # Name.
        self._name: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Keep this rule active even when the VPN is not connected: Default False
        self._persistent: Optional[bool] = None
        # Proxy Server Uri.
        self._proxy_server_uri: Optional[str] = None
        # Servers.
        self._servers: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> VpnDnsRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: VpnDnsRule
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return VpnDnsRule()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "auto_trigger": lambda n : setattr(self, 'auto_trigger', n.get_bool_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "persistent": lambda n : setattr(self, 'persistent', n.get_bool_value()),
            "proxy_server_uri": lambda n : setattr(self, 'proxy_server_uri', n.get_str_value()),
            "servers": lambda n : setattr(self, 'servers', n.get_collection_of_primitive_values(str)),
        }
        return fields
    
    @property
    def name(self,) -> Optional[str]:
        """
        Gets the name property value. Name.
        Returns: Optional[str]
        """
        return self._name
    
    @name.setter
    def name(self,value: Optional[str] = None) -> None:
        """
        Sets the name property value. Name.
        Args:
            value: Value to set for the name property.
        """
        self._name = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def persistent(self,) -> Optional[bool]:
        """
        Gets the persistent property value. Keep this rule active even when the VPN is not connected: Default False
        Returns: Optional[bool]
        """
        return self._persistent
    
    @persistent.setter
    def persistent(self,value: Optional[bool] = None) -> None:
        """
        Sets the persistent property value. Keep this rule active even when the VPN is not connected: Default False
        Args:
            value: Value to set for the persistent property.
        """
        self._persistent = value
    
    @property
    def proxy_server_uri(self,) -> Optional[str]:
        """
        Gets the proxyServerUri property value. Proxy Server Uri.
        Returns: Optional[str]
        """
        return self._proxy_server_uri
    
    @proxy_server_uri.setter
    def proxy_server_uri(self,value: Optional[str] = None) -> None:
        """
        Sets the proxyServerUri property value. Proxy Server Uri.
        Args:
            value: Value to set for the proxyServerUri property.
        """
        self._proxy_server_uri = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_bool_value("autoTrigger", self.auto_trigger)
        writer.write_str_value("name", self.name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_bool_value("persistent", self.persistent)
        writer.write_str_value("proxyServerUri", self.proxy_server_uri)
        writer.write_collection_of_primitive_values("servers", self.servers)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def servers(self,) -> Optional[List[str]]:
        """
        Gets the servers property value. Servers.
        Returns: Optional[List[str]]
        """
        return self._servers
    
    @servers.setter
    def servers(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the servers property value. Servers.
        Args:
            value: Value to set for the servers property.
        """
        self._servers = value
    

