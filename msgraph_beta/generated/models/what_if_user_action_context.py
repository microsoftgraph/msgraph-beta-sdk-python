from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .conditional_access_context import ConditionalAccessContext
    from .user_action import UserAction

from .conditional_access_context import ConditionalAccessContext

@dataclass
class WhatIfUserActionContext(ConditionalAccessContext):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.whatIfUserActionContext"
    # The userAction property
    user_action: Optional[UserAction] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WhatIfUserActionContext:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WhatIfUserActionContext
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WhatIfUserActionContext()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .conditional_access_context import ConditionalAccessContext
        from .user_action import UserAction

        from .conditional_access_context import ConditionalAccessContext
        from .user_action import UserAction

        fields: Dict[str, Callable[[Any], None]] = {
            "userAction": lambda n : setattr(self, 'user_action', n.get_enum_value(UserAction)),
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
        writer.write_enum_value("userAction", self.user_action)
    

