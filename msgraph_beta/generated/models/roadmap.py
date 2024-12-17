from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .change_item_base import ChangeItemBase
    from .change_item_state import ChangeItemState
    from .roadmap_item_delivery_stage import RoadmapItemDeliveryStage

from .change_item_base import ChangeItemBase

@dataclass
class Roadmap(ChangeItemBase, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.roadmap"
    # Indicates the category with which this item is associated. Supports $filter (eq, ne, in) and $orderby.
    category: Optional[str] = None
    # The changeItemState property
    change_item_state: Optional[ChangeItemState] = None
    # The deliveryStage property
    delivery_stage: Optional[RoadmapItemDeliveryStage] = None
    # Link to the feature page in the Microsoft Entra admin center. Supports $filter (eq, ne, in) and $orderby.
    goto_link: Optional[str] = None
    # Feature planned release date. Supports $filter (eq, ne, gt, lt, le and ge on year(), month(), day(), hour(), minute(), and second() built in functions) and $orderby.
    published_date_time: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Roadmap:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Roadmap
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Roadmap()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .change_item_base import ChangeItemBase
        from .change_item_state import ChangeItemState
        from .roadmap_item_delivery_stage import RoadmapItemDeliveryStage

        from .change_item_base import ChangeItemBase
        from .change_item_state import ChangeItemState
        from .roadmap_item_delivery_stage import RoadmapItemDeliveryStage

        fields: Dict[str, Callable[[Any], None]] = {
            "category": lambda n : setattr(self, 'category', n.get_str_value()),
            "changeItemState": lambda n : setattr(self, 'change_item_state', n.get_enum_value(ChangeItemState)),
            "deliveryStage": lambda n : setattr(self, 'delivery_stage', n.get_enum_value(RoadmapItemDeliveryStage)),
            "gotoLink": lambda n : setattr(self, 'goto_link', n.get_str_value()),
            "publishedDateTime": lambda n : setattr(self, 'published_date_time', n.get_datetime_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        from .change_item_base import ChangeItemBase
        from .change_item_state import ChangeItemState
        from .roadmap_item_delivery_stage import RoadmapItemDeliveryStage

        writer.write_str_value("category", self.category)
        writer.write_enum_value("changeItemState", self.change_item_state)
        writer.write_enum_value("deliveryStage", self.delivery_stage)
        writer.write_str_value("gotoLink", self.goto_link)
        writer.write_datetime_value("publishedDateTime", self.published_date_time)
    

