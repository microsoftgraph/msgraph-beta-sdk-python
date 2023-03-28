from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import delivery_optimization_group_id_options_type, delivery_optimization_group_id_source

from . import delivery_optimization_group_id_source

class DeliveryOptimizationGroupIdSourceOptions(delivery_optimization_group_id_source.DeliveryOptimizationGroupIdSource):
    def __init__(self,) -> None:
        """
        Instantiates a new DeliveryOptimizationGroupIdSourceOptions and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.deliveryOptimizationGroupIdSourceOptions"
        # Possible values for the DeliveryOptimizationGroupIdOptionsType setting.
        self._group_id_source_option: Optional[delivery_optimization_group_id_options_type.DeliveryOptimizationGroupIdOptionsType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeliveryOptimizationGroupIdSourceOptions:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeliveryOptimizationGroupIdSourceOptions
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeliveryOptimizationGroupIdSourceOptions()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import delivery_optimization_group_id_options_type, delivery_optimization_group_id_source

        fields: Dict[str, Callable[[Any], None]] = {
            "groupIdSourceOption": lambda n : setattr(self, 'group_id_source_option', n.get_enum_value(delivery_optimization_group_id_options_type.DeliveryOptimizationGroupIdOptionsType)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def group_id_source_option(self,) -> Optional[delivery_optimization_group_id_options_type.DeliveryOptimizationGroupIdOptionsType]:
        """
        Gets the groupIdSourceOption property value. Possible values for the DeliveryOptimizationGroupIdOptionsType setting.
        Returns: Optional[delivery_optimization_group_id_options_type.DeliveryOptimizationGroupIdOptionsType]
        """
        return self._group_id_source_option
    
    @group_id_source_option.setter
    def group_id_source_option(self,value: Optional[delivery_optimization_group_id_options_type.DeliveryOptimizationGroupIdOptionsType] = None) -> None:
        """
        Sets the groupIdSourceOption property value. Possible values for the DeliveryOptimizationGroupIdOptionsType setting.
        Args:
            value: Value to set for the group_id_source_option property.
        """
        self._group_id_source_option = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("groupIdSourceOption", self.group_id_source_option)
    

