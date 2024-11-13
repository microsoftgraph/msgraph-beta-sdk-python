from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .custom_claim_transformation import CustomClaimTransformation
    from .transformation_trim_type import TransformationTrimType

from .custom_claim_transformation import CustomClaimTransformation

@dataclass
class TrimTransformation(CustomClaimTransformation, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.trimTransformation"
    # The type property
    type: Optional[TransformationTrimType] = None
    # The value to be used as part of the transformation.
    value: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TrimTransformation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TrimTransformation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TrimTransformation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .custom_claim_transformation import CustomClaimTransformation
        from .transformation_trim_type import TransformationTrimType

        from .custom_claim_transformation import CustomClaimTransformation
        from .transformation_trim_type import TransformationTrimType

        fields: Dict[str, Callable[[Any], None]] = {
            "type": lambda n : setattr(self, 'type', n.get_enum_value(TransformationTrimType)),
            "value": lambda n : setattr(self, 'value', n.get_str_value()),
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
        from .custom_claim_transformation import CustomClaimTransformation
        from .transformation_trim_type import TransformationTrimType

        writer.write_enum_value("type", self.type)
        writer.write_str_value("value", self.value)
    

