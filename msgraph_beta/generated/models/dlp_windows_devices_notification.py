from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .dlp_notification import DlpNotification

from .dlp_notification import DlpNotification

@dataclass
class DlpWindowsDevicesNotification(DlpNotification):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.dlpWindowsDevicesNotification"
    # The contentName property
    content_name: Optional[str] = None
    # The lastModfiedBy property
    last_modfied_by: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DlpWindowsDevicesNotification:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DlpWindowsDevicesNotification
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DlpWindowsDevicesNotification()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .dlp_notification import DlpNotification

        from .dlp_notification import DlpNotification

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
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("contentName", self.content_name)
        writer.write_str_value("lastModfiedBy", self.last_modfied_by)
    

