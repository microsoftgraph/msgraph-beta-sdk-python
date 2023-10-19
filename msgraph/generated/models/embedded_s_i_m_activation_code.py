from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class EmbeddedSIMActivationCode(AdditionalDataHolder, BackedModel, Parsable):
    """
    The embedded SIM activation code as provided by the mobile operator.
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The Integrated Circuit Card Identifier (ICCID) for this embedded SIM activation code as provided by the mobile operator.
    integrated_circuit_card_identifier: Optional[str] = None
    # The MatchingIdentifier (MatchingID) as specified in the GSMA Association SGP.22 RSP Technical Specification section 4.1.
    matching_identifier: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The fully qualified domain name of the SM-DP+ server as specified in the GSM Association SPG .22 RSP Technical Specification.
    smdp_plus_server_address: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EmbeddedSIMActivationCode:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EmbeddedSIMActivationCode
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return EmbeddedSIMActivationCode()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "integratedCircuitCardIdentifier": lambda n : setattr(self, 'integrated_circuit_card_identifier', n.get_str_value()),
            "matchingIdentifier": lambda n : setattr(self, 'matching_identifier', n.get_str_value()),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "smdpPlusServerAddress": lambda n : setattr(self, 'smdp_plus_server_address', n.get_str_value()),
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
        writer.write_str_value("integratedCircuitCardIdentifier", self.integrated_circuit_card_identifier)
        writer.write_str_value("matchingIdentifier", self.matching_identifier)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_str_value("smdpPlusServerAddress", self.smdp_plus_server_address)
        writer.write_additional_data_value(self.additional_data)
    

