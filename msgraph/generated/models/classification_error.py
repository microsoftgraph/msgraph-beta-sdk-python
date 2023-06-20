from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import classifcation_error_base

from . import classifcation_error_base

@dataclass
class ClassificationError(classifcation_error_base.ClassifcationErrorBase):
    # The details property
    details: Optional[List[classifcation_error_base.ClassifcationErrorBase]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ClassificationError:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ClassificationError
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ClassificationError()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import classifcation_error_base

        from . import classifcation_error_base

        fields: Dict[str, Callable[[Any], None]] = {
            "details": lambda n : setattr(self, 'details', n.get_collection_of_object_values(classifcation_error_base.ClassifcationErrorBase)),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("details", self.details)
    

