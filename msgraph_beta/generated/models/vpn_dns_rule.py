from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class VpnDnsRule(AdditionalDataHolder, BackedModel, Parsable):
    """
    VPN DNS Rule definition.
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Automatically connect to the VPN when the device connects to this domain: Default False.
    auto_trigger: Optional[bool] = None
    # Name.
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Keep this rule active even when the VPN is not connected: Default False
    persistent: Optional[bool] = None
    # Proxy Server Uri.
    proxy_server_uri: Optional[str] = None
    # Servers.
    servers: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> VpnDnsRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: VpnDnsRule
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return VpnDnsRule()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "autoTrigger": lambda n : setattr(self, 'auto_trigger', n.get_bool_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "persistent": lambda n : setattr(self, 'persistent', n.get_bool_value()),
            "proxyServerUri": lambda n : setattr(self, 'proxy_server_uri', n.get_str_value()),
            "servers": lambda n : setattr(self, 'servers', n.get_collection_of_primitive_values(str)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_bool_value("autoTrigger", self.auto_trigger)
        writer.write_str_value("name", self.name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_bool_value("persistent", self.persistent)
        writer.write_str_value("proxyServerUri", self.proxy_server_uri)
        writer.write_collection_of_primitive_values("servers", self.servers)
        writer.write_additional_data_value(self.additional_data)
    

