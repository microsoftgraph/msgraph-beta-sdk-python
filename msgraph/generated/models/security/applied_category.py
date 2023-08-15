from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .file_plan_descriptor_base import FilePlanDescriptorBase
    from .sub_category import SubCategory

from .file_plan_descriptor_base import FilePlanDescriptorBase

@dataclass
class AppliedCategory(FilePlanDescriptorBase):
    # The OdataType property
    odata_type: Optional[str] = None
    # Represents the file plan descriptor for a subcategory under a specific category, which has been assigned to a particular retention label.
    sub_category: Optional[SubCategory] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AppliedCategory:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AppliedCategory
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AppliedCategory()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .file_plan_descriptor_base import FilePlanDescriptorBase
        from .sub_category import SubCategory

        from .file_plan_descriptor_base import FilePlanDescriptorBase
        from .sub_category import SubCategory

        fields: Dict[str, Callable[[Any], None]] = {
            "subCategory": lambda n : setattr(self, 'sub_category', n.get_object_value(SubCategory)),
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
        writer.write_object_value("subCategory", self.sub_category)
    

