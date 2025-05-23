from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .copilot_admin_limited_mode import CopilotAdminLimitedMode
    from .entity import Entity

from .entity import Entity

@dataclass
class CopilotAdminSetting(Entity, Parsable):
    # Represents a setting that controls whether users of Microsoft 365 Copilot in Teams meetings can receive responses to sentiment-related prompts. Read-only. Nullable.
    limited_mode: Optional[CopilotAdminLimitedMode] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CopilotAdminSetting:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CopilotAdminSetting
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CopilotAdminSetting()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .copilot_admin_limited_mode import CopilotAdminLimitedMode
        from .entity import Entity

        from .copilot_admin_limited_mode import CopilotAdminLimitedMode
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "limitedMode": lambda n : setattr(self, 'limited_mode', n.get_object_value(CopilotAdminLimitedMode)),
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
        writer.write_object_value("limitedMode", self.limited_mode)
    

