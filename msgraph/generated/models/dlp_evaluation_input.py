from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import current_label, discovered_sensitive_type, dlp_evaluation_windows_devices_input

@dataclass
class DlpEvaluationInput(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The currentLabel property
    current_label: Optional[current_label.CurrentLabel] = None
    # The discoveredSensitiveTypes property
    discovered_sensitive_types: Optional[List[discovered_sensitive_type.DiscoveredSensitiveType]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DlpEvaluationInput:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DlpEvaluationInput
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.dlpEvaluationWindowsDevicesInput":
                from . import dlp_evaluation_windows_devices_input

                return dlp_evaluation_windows_devices_input.DlpEvaluationWindowsDevicesInput()
        return DlpEvaluationInput()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import current_label, discovered_sensitive_type, dlp_evaluation_windows_devices_input

        fields: Dict[str, Callable[[Any], None]] = {
            "currentLabel": lambda n : setattr(self, 'current_label', n.get_object_value(current_label.CurrentLabel)),
            "discoveredSensitiveTypes": lambda n : setattr(self, 'discovered_sensitive_types', n.get_collection_of_object_values(discovered_sensitive_type.DiscoveredSensitiveType)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_object_value("currentLabel", self.current_label)
        writer.write_collection_of_object_values("discoveredSensitiveTypes", self.discovered_sensitive_types)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

