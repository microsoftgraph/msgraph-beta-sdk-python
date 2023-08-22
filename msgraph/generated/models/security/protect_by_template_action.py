from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .information_protection_action import InformationProtectionAction

from .information_protection_action import InformationProtectionAction

@dataclass
class ProtectByTemplateAction(InformationProtectionAction):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.protectByTemplateAction"
    # The unique identifier for a protection template in Microsoft Purview Information Protection to apply to the content.
    template_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ProtectByTemplateAction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ProtectByTemplateAction
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ProtectByTemplateAction()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .information_protection_action import InformationProtectionAction

        from .information_protection_action import InformationProtectionAction

        fields: Dict[str, Callable[[Any], None]] = {
            "templateId": lambda n : setattr(self, 'template_id', n.get_str_value()),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("templateId", self.template_id)
    

