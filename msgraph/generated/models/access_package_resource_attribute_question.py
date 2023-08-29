from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_package_question import AccessPackageQuestion
    from .access_package_resource_attribute_source import AccessPackageResourceAttributeSource

from .access_package_resource_attribute_source import AccessPackageResourceAttributeSource

@dataclass
class AccessPackageResourceAttributeQuestion(AccessPackageResourceAttributeSource):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.accessPackageResourceAttributeQuestion"
    # The question asked in order to get the value of the attribute
    question: Optional[AccessPackageQuestion] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessPackageResourceAttributeQuestion:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackageResourceAttributeQuestion
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AccessPackageResourceAttributeQuestion()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .access_package_question import AccessPackageQuestion
        from .access_package_resource_attribute_source import AccessPackageResourceAttributeSource

        from .access_package_question import AccessPackageQuestion
        from .access_package_resource_attribute_source import AccessPackageResourceAttributeSource

        fields: Dict[str, Callable[[Any], None]] = {
            "question": lambda n : setattr(self, 'question', n.get_object_value(AccessPackageQuestion)),
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
        writer.write_object_value("question", self.question)
    

