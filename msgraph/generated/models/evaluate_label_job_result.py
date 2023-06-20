from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import matching_label, responsible_policy, responsible_sensitive_type

@dataclass
class EvaluateLabelJobResult(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    # The responsiblePolicy property
    responsible_policy: Optional[responsible_policy.ResponsiblePolicy] = None
    # The responsibleSensitiveTypes property
    responsible_sensitive_types: Optional[List[responsible_sensitive_type.ResponsibleSensitiveType]] = None
    # The sensitivityLabel property
    sensitivity_label: Optional[matching_label.MatchingLabel] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EvaluateLabelJobResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EvaluateLabelJobResult
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return EvaluateLabelJobResult()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import matching_label, responsible_policy, responsible_sensitive_type

        from . import matching_label, responsible_policy, responsible_sensitive_type

        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "responsiblePolicy": lambda n : setattr(self, 'responsible_policy', n.get_object_value(responsible_policy.ResponsiblePolicy)),
            "responsibleSensitiveTypes": lambda n : setattr(self, 'responsible_sensitive_types', n.get_collection_of_object_values(responsible_sensitive_type.ResponsibleSensitiveType)),
            "sensitivityLabel": lambda n : setattr(self, 'sensitivity_label', n.get_object_value(matching_label.MatchingLabel)),
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("responsiblePolicy", self.responsible_policy)
        writer.write_collection_of_object_values("responsibleSensitiveTypes", self.responsible_sensitive_types)
        writer.write_object_value("sensitivityLabel", self.sensitivity_label)
        writer.write_additional_data_value(self.additional_data)
    

