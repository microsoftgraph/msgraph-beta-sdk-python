from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .content_properties import ContentProperties
    from .dlp_evaluation_input import DlpEvaluationInput

from .dlp_evaluation_input import DlpEvaluationInput

@dataclass
class DlpEvaluationWindowsDevicesInput(DlpEvaluationInput):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.dlpEvaluationWindowsDevicesInput"
    # The contentProperties property
    content_properties: Optional[ContentProperties] = None
    # The sharedBy property
    shared_by: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DlpEvaluationWindowsDevicesInput:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DlpEvaluationWindowsDevicesInput
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DlpEvaluationWindowsDevicesInput()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .content_properties import ContentProperties
        from .dlp_evaluation_input import DlpEvaluationInput

        from .content_properties import ContentProperties
        from .dlp_evaluation_input import DlpEvaluationInput

        fields: Dict[str, Callable[[Any], None]] = {
            "contentProperties": lambda n : setattr(self, 'content_properties', n.get_object_value(ContentProperties)),
            "sharedBy": lambda n : setattr(self, 'shared_by', n.get_str_value()),
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
        writer.write_object_value("contentProperties", self.content_properties)
        writer.write_str_value("sharedBy", self.shared_by)
    

