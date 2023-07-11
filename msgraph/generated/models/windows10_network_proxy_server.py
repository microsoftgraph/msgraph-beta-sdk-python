from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class Windows10NetworkProxyServer(AdditionalDataHolder, Parsable):
    """
    Network Proxy Server Policy.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Address to the proxy server. Specify an address in the format [':']
    address: Optional[str] = None
    # Addresses that should not use the proxy server. The system will not use the proxy server for addresses beginning with what is specified in this node.
    exceptions: Optional[List[str]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Specifies whether the proxy server should be used for local (intranet) addresses.
    use_for_local_addresses: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Windows10NetworkProxyServer:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Windows10NetworkProxyServer
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Windows10NetworkProxyServer()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "address": lambda n : setattr(self, 'address', n.get_str_value()),
            "exceptions": lambda n : setattr(self, 'exceptions', n.get_collection_of_primitive_values(str)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "useForLocalAddresses": lambda n : setattr(self, 'use_for_local_addresses', n.get_bool_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("address", self.address)
        writer.write_collection_of_primitive_values("exceptions", self.exceptions)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_bool_value("useForLocalAddresses", self.use_for_local_addresses)
        writer.write_additional_data_value(self.additional_data)
    

