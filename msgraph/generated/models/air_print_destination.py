from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class AirPrintDestination(AdditionalDataHolder, BackedModel, Parsable):
    """
    Represents an AirPrint destination.
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # If true AirPrint connections are secured by Transport Layer Security (TLS). Default is false. Available in iOS 11.0 and later.
    force_tls: Optional[bool] = None
    # The IP Address of the AirPrint destination.
    ip_address: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The listening port of the AirPrint destination. If this key is not specified AirPrint will use the default port. Available in iOS 11.0 and later.
    port: Optional[int] = None
    # The Resource Path associated with the printer. This corresponds to the rp parameter of the ipps.tcp Bonjour record. For example: printers/CanonMG5300series, printers/XeroxPhaser7600, ipp/print, EpsonIPPPrinter.
    resource_path: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AirPrintDestination:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AirPrintDestination
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AirPrintDestination()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "forceTls": lambda n : setattr(self, 'force_tls', n.get_bool_value()),
            "ipAddress": lambda n : setattr(self, 'ip_address', n.get_str_value()),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "port": lambda n : setattr(self, 'port', n.get_int_value()),
            "resourcePath": lambda n : setattr(self, 'resource_path', n.get_str_value()),
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
        writer.write_bool_value("forceTls", self.force_tls)
        writer.write_str_value("ipAddress", self.ip_address)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_int_value("port", self.port)
        writer.write_str_value("resourcePath", self.resource_path)
        writer.write_additional_data_value(self.additional_data)
    

