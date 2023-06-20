from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import tunnel_configuration_i_k_ev2_custom, tunnel_configuration_i_k_ev2_default

@dataclass
class TunnelConfiguration(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    # The preSharedKey property
    pre_shared_key: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TunnelConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TunnelConfiguration
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.tunnelConfigurationIKEv2Custom".casefold():
            from . import tunnel_configuration_i_k_ev2_custom

            return tunnel_configuration_i_k_ev2_custom.TunnelConfigurationIKEv2Custom()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.tunnelConfigurationIKEv2Default".casefold():
            from . import tunnel_configuration_i_k_ev2_default

            return tunnel_configuration_i_k_ev2_default.TunnelConfigurationIKEv2Default()
        return TunnelConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import tunnel_configuration_i_k_ev2_custom, tunnel_configuration_i_k_ev2_default

        from . import tunnel_configuration_i_k_ev2_custom, tunnel_configuration_i_k_ev2_default

        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "preSharedKey": lambda n : setattr(self, 'pre_shared_key', n.get_str_value()),
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("preSharedKey", self.pre_shared_key)
        writer.write_additional_data_value(self.additional_data)
    

