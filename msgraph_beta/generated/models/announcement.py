from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .change_announcement_change_type import ChangeAnnouncementChangeType
    from .change_item_base import ChangeItemBase

from .change_item_base import ChangeItemBase

@dataclass
class Announcement(ChangeItemBase, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.announcement"
    # Change announcement date. Supports $filter (eq, ne, gt, lt, le and ge on year(), month(), day(), hour(), minute(), and second() built in functions) and $orderby.
    announcement_date_time: Optional[datetime.datetime] = None
    # The changeType property
    change_type: Optional[ChangeAnnouncementChangeType] = None
    # Change impact URL. Supports $filter (eq, ne, in) and $orderby.
    impact_link: Optional[str] = None
    # Indicates whether the customer needs to take any action for this change. Supports $filter (eq, ne).
    is_customer_action_required: Optional[bool] = None
    # Date on which the change rolls out. Supports $filter (eq, ne, gt, lt, le and ge on year(), month(), day(), hour(), minute(), and second() built in functions) and $orderby.
    target_date_time: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Announcement:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Announcement
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Announcement()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .change_announcement_change_type import ChangeAnnouncementChangeType
        from .change_item_base import ChangeItemBase

        from .change_announcement_change_type import ChangeAnnouncementChangeType
        from .change_item_base import ChangeItemBase

        fields: Dict[str, Callable[[Any], None]] = {
            "announcementDateTime": lambda n : setattr(self, 'announcement_date_time', n.get_datetime_value()),
            "changeType": lambda n : setattr(self, 'change_type', n.get_enum_value(ChangeAnnouncementChangeType)),
            "impactLink": lambda n : setattr(self, 'impact_link', n.get_str_value()),
            "isCustomerActionRequired": lambda n : setattr(self, 'is_customer_action_required', n.get_bool_value()),
            "targetDateTime": lambda n : setattr(self, 'target_date_time', n.get_datetime_value()),
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
        from .change_announcement_change_type import ChangeAnnouncementChangeType
        from .change_item_base import ChangeItemBase

        writer.write_datetime_value("announcementDateTime", self.announcement_date_time)
        writer.write_enum_value("changeType", self.change_type)
        writer.write_str_value("impactLink", self.impact_link)
        writer.write_bool_value("isCustomerActionRequired", self.is_customer_action_required)
        writer.write_datetime_value("targetDateTime", self.target_date_time)
    

