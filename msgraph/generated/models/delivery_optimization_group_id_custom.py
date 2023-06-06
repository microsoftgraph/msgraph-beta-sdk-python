from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import delivery_optimization_group_id_source

from . import delivery_optimization_group_id_source

@dataclass
class DeliveryOptimizationGroupIdCustom(delivery_optimization_group_id_source.DeliveryOptimizationGroupIdSource):
    odata_type = "#microsoft.graph.deliveryOptimizationGroupIdCustom"
    # Specifies an arbitrary group ID that the device belongs to
    group_id_custom: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeliveryOptimizationGroupIdCustom:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeliveryOptimizationGroupIdCustom
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeliveryOptimizationGroupIdCustom()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import delivery_optimization_group_id_source

        fields: Dict[str, Callable[[Any], None]] = {
            "groupIdCustom": lambda n : setattr(self, 'group_id_custom', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("groupIdCustom", self.group_id_custom)
    

