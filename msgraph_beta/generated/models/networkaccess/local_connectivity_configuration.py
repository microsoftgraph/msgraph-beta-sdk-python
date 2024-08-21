from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .region import Region

@dataclass
class LocalConnectivityConfiguration(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Specifies ASN of one end of IPSec tunnel (local or peer).
    asn: Optional[int] = None
    # Specifies BGP IPv4 address of one end of IPSec tunnel (local or peer).
    bgp_address: Optional[str] = None
    # Specifies public IPv4 address of one end of IPSec tunnel (local or peer).
    endpoint: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The region property
    region: Optional[Region] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LocalConnectivityConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LocalConnectivityConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LocalConnectivityConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .region import Region

        from .region import Region

        fields: Dict[str, Callable[[Any], None]] = {
            "asn": lambda n : setattr(self, 'asn', n.get_int_value()),
            "bgpAddress": lambda n : setattr(self, 'bgp_address', n.get_str_value()),
            "endpoint": lambda n : setattr(self, 'endpoint', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "region": lambda n : setattr(self, 'region', n.get_enum_value(Region)),
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
        writer.write_str_value("bgpAddress", self.bgp_address)
        writer.write_str_value("endpoint", self.endpoint)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("region", self.region)
        writer.write_additional_data_value(self.additional_data)
    

