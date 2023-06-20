from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import assignment_method, downgrade_justification, key_value_pair

@dataclass
class LabelingOptions(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The assignmentMethod property
    assignment_method: Optional[assignment_method.AssignmentMethod] = None
    # The downgrade justification object that indicates if downgrade was justified and, if so, the reason.
    downgrade_justification: Optional[downgrade_justification.DowngradeJustification] = None
    # Extended properties will be parsed and returned in the standard Microsoft Purview Information Protection labeled metadata format as part of the label information.
    extended_properties: Optional[List[key_value_pair.KeyValuePair]] = None
    # The GUID of the label that should be applied to the information.
    label_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> LabelingOptions:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: LabelingOptions
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return LabelingOptions()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import assignment_method, downgrade_justification, key_value_pair

        from . import assignment_method, downgrade_justification, key_value_pair

        fields: Dict[str, Callable[[Any], None]] = {
            "assignmentMethod": lambda n : setattr(self, 'assignment_method', n.get_enum_value(assignment_method.AssignmentMethod)),
            "downgradeJustification": lambda n : setattr(self, 'downgrade_justification', n.get_object_value(downgrade_justification.DowngradeJustification)),
            "extendedProperties": lambda n : setattr(self, 'extended_properties', n.get_collection_of_object_values(key_value_pair.KeyValuePair)),
            "labelId": lambda n : setattr(self, 'label_id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_enum_value("assignmentMethod", self.assignment_method)
        writer.write_object_value("downgradeJustification", self.downgrade_justification)
        writer.write_collection_of_object_values("extendedProperties", self.extended_properties)
        writer.write_str_value("labelId", self.label_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

