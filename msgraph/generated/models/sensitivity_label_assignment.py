from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import sensitivity_label_assignment_method

@dataclass
class SensitivityLabelAssignment(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The assignmentMethod property
    assignment_method: Optional[sensitivity_label_assignment_method.SensitivityLabelAssignmentMethod] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The unique identifier for the sensitivity label assigned to the file.
    sensitivity_label_id: Optional[str] = None
    # The unique identifier for the tenant that hosts the file when this label is applied.
    tenant_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SensitivityLabelAssignment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SensitivityLabelAssignment
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SensitivityLabelAssignment()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import sensitivity_label_assignment_method

        fields: Dict[str, Callable[[Any], None]] = {
            "assignmentMethod": lambda n : setattr(self, 'assignment_method', n.get_enum_value(sensitivity_label_assignment_method.SensitivityLabelAssignmentMethod)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "sensitivityLabelId": lambda n : setattr(self, 'sensitivity_label_id', n.get_str_value()),
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_enum_value("assignmentMethod", self.assignment_method)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("sensitivityLabelId", self.sensitivity_label_id)
        writer.write_str_value("tenantId", self.tenant_id)
        writer.write_additional_data_value(self.additional_data)
    

