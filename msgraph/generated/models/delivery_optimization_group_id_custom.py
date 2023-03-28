from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import delivery_optimization_group_id_source

from . import delivery_optimization_group_id_source

class DeliveryOptimizationGroupIdCustom(delivery_optimization_group_id_source.DeliveryOptimizationGroupIdSource):
    def __init__(self,) -> None:
        """
        Instantiates a new DeliveryOptimizationGroupIdCustom and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.deliveryOptimizationGroupIdCustom"
        # Specifies an arbitrary group ID that the device belongs to
        self._group_id_custom: Optional[str] = None
    
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
    
    @property
    def group_id_custom(self,) -> Optional[str]:
        """
        Gets the groupIdCustom property value. Specifies an arbitrary group ID that the device belongs to
        Returns: Optional[str]
        """
        return self._group_id_custom
    
    @group_id_custom.setter
    def group_id_custom(self,value: Optional[str] = None) -> None:
        """
        Sets the groupIdCustom property value. Specifies an arbitrary group ID that the device belongs to
        Args:
            value: Value to set for the group_id_custom property.
        """
        self._group_id_custom = value
    
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
    

