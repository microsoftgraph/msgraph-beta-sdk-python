from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import subject_alternative_name_type

@dataclass
class Windows10XCustomSubjectAlternativeName(AdditionalDataHolder, Parsable):
    """
    Base Profile Type for Authentication Certificates (SCEP or PFX Create)
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Custom SAN Name
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Subject Alternative Name Options.
    san_type: Optional[subject_alternative_name_type.SubjectAlternativeNameType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Windows10XCustomSubjectAlternativeName:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Windows10XCustomSubjectAlternativeName
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Windows10XCustomSubjectAlternativeName()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import subject_alternative_name_type

        from . import subject_alternative_name_type

        fields: Dict[str, Callable[[Any], None]] = {
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "sanType": lambda n : setattr(self, 'san_type', n.get_enum_value(subject_alternative_name_type.SubjectAlternativeNameType)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("name", self.name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("sanType", self.san_type)
        writer.write_additional_data_value(self.additional_data)
    

