from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class ProxiedDomain(AdditionalDataHolder, Parsable):
    """
    Proxied Domain
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The IP address or FQDN
    ip_address_or_f_q_d_n: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Proxy IP or FQDN
    proxy: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ProxiedDomain:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ProxiedDomain
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ProxiedDomain()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "ipAddressOrFQDN": lambda n : setattr(self, 'ip_address_or_f_q_d_n', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "proxy": lambda n : setattr(self, 'proxy', n.get_str_value()),
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
        writer.write_str_value("ipAddressOrFQDN", self.ip_address_or_f_q_d_n)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("proxy", self.proxy)
        writer.write_additional_data_value(self.additional_data)
    

