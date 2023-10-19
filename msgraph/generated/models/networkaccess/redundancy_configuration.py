from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .redundancy_tier import RedundancyTier

@dataclass
class RedundancyConfiguration(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The OdataType property
    odata_type: Optional[str] = None
    # The redundancyTier property
    redundancy_tier: Optional[RedundancyTier] = None
    # Indicate the specific IP address used for establishing the Border Gateway Protocol (BGP) connection with Microsoft's network.
    zone_local_ip_address: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RedundancyConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RedundancyConfiguration
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return RedundancyConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .redundancy_tier import RedundancyTier

        from .redundancy_tier import RedundancyTier

        fields: Dict[str, Callable[[Any], None]] = {
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "redundancyTier": lambda n : setattr(self, 'redundancy_tier', n.get_enum_value(RedundancyTier)),
            "zoneLocalIpAddress": lambda n : setattr(self, 'zone_local_ip_address', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_enum_value("redundancyTier", self.redundancy_tier)
        writer.write_str_value("zoneLocalIpAddress", self.zone_local_ip_address)
        writer.write_additional_data_value(self.additional_data)
    

