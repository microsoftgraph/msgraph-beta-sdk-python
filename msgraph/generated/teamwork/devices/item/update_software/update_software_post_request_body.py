from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....models import teamwork_software_type

@dataclass
class UpdateSoftwarePostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The softwareType property
    software_type: Optional[teamwork_software_type.TeamworkSoftwareType] = None
    # The softwareVersion property
    software_version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UpdateSoftwarePostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UpdateSoftwarePostRequestBody
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return UpdateSoftwarePostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .....models import teamwork_software_type

        from .....models import teamwork_software_type

        fields: Dict[str, Callable[[Any], None]] = {
            "softwareType": lambda n : setattr(self, 'software_type', n.get_enum_value(teamwork_software_type.TeamworkSoftwareType)),
            "softwareVersion": lambda n : setattr(self, 'software_version', n.get_str_value()),
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
        writer.write_enum_value("softwareType", self.software_type)
        writer.write_str_value("softwareVersion", self.software_version)
        writer.write_additional_data_value(self.additional_data)
    

