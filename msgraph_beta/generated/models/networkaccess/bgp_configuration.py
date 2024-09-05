from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class BgpConfiguration(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Specifies the ASN of the BGP.
    asn: Optional[int] = None
    # Specifies the BGP IP address.
    ip_address: Optional[str] = None
    # Specifies the BGP IP address of peer (Microsoft, in this case).
    local_ip_address: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Specifies the BGP IP address of customer's on-premise VPN router configuration.
    peer_ip_address: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BgpConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BgpConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return BgpConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "asn": lambda n : setattr(self, 'asn', n.get_int_value()),
            "ipAddress": lambda n : setattr(self, 'ip_address', n.get_str_value()),
            "localIpAddress": lambda n : setattr(self, 'local_ip_address', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "peerIpAddress": lambda n : setattr(self, 'peer_ip_address', n.get_str_value()),
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
        writer.write_int_value("asn", self.asn)
        writer.write_str_value("ipAddress", self.ip_address)
        writer.write_str_value("localIpAddress", self.local_ip_address)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("peerIpAddress", self.peer_ip_address)
        writer.write_additional_data_value(self.additional_data)
    

