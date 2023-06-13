from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import dlp_notification

from . import dlp_notification

@dataclass
class DlpWindowsDevicesNotification(dlp_notification.DlpNotification):
    odata_type = "#microsoft.graph.dlpWindowsDevicesNotification"
    # The contentName property
    content_name: Optional[str] = None
    # The lastModfiedBy property
    last_modfied_by: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DlpWindowsDevicesNotification:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DlpWindowsDevicesNotification
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DlpWindowsDevicesNotification()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import dlp_notification

        fields: Dict[str, Callable[[Any], None]] = {
            "contentName": lambda n : setattr(self, 'content_name', n.get_str_value()),
            "lastModfiedBy": lambda n : setattr(self, 'last_modfied_by', n.get_str_value()),
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
        writer.write_str_value("contentName", self.content_name)
        writer.write_str_value("lastModfiedBy", self.last_modfied_by)
    

