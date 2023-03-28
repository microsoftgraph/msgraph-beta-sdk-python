from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import account_target_content

from . import account_target_content

class IncludeAllAccountTargetContent(account_target_content.AccountTargetContent):
    def __init__(self,) -> None:
        """
        Instantiates a new IncludeAllAccountTargetContent and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.includeAllAccountTargetContent"
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IncludeAllAccountTargetContent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IncludeAllAccountTargetContent
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return IncludeAllAccountTargetContent()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import account_target_content

        fields: Dict[str, Callable[[Any], None]] = {
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
    

