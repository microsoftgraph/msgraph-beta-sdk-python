from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .share_point_migration_event import SharePointMigrationEvent

from .share_point_migration_event import SharePointMigrationEvent

@dataclass
class SharePointMigrationJobCancelledEvent(SharePointMigrationEvent, Parsable):
    # The isCancelledByUser property
    is_cancelled_by_user: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The totalRetryCount property
    total_retry_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SharePointMigrationJobCancelledEvent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SharePointMigrationJobCancelledEvent
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SharePointMigrationJobCancelledEvent()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .share_point_migration_event import SharePointMigrationEvent

        from .share_point_migration_event import SharePointMigrationEvent

        fields: dict[str, Callable[[Any], None]] = {
            "isCancelledByUser": lambda n : setattr(self, 'is_cancelled_by_user', n.get_bool_value()),
            "totalRetryCount": lambda n : setattr(self, 'total_retry_count', n.get_int_value()),
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
        writer.write_bool_value("isCancelledByUser", self.is_cancelled_by_user)
        writer.write_int_value("totalRetryCount", self.total_retry_count)
    

