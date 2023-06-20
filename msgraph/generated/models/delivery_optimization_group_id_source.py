from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import delivery_optimization_group_id_custom, delivery_optimization_group_id_source_options

@dataclass
class DeliveryOptimizationGroupIdSource(AdditionalDataHolder, Parsable):
    """
    GroupId Support Types
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeliveryOptimizationGroupIdSource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeliveryOptimizationGroupIdSource
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deliveryOptimizationGroupIdCustom".casefold():
            from . import delivery_optimization_group_id_custom

            return delivery_optimization_group_id_custom.DeliveryOptimizationGroupIdCustom()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deliveryOptimizationGroupIdSourceOptions".casefold():
            from . import delivery_optimization_group_id_source_options

            return delivery_optimization_group_id_source_options.DeliveryOptimizationGroupIdSourceOptions()
        return DeliveryOptimizationGroupIdSource()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import delivery_optimization_group_id_custom, delivery_optimization_group_id_source_options

        from . import delivery_optimization_group_id_custom, delivery_optimization_group_id_source_options

        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_additional_data_value(self.additional_data)
    

