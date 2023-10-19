from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .current_label import CurrentLabel
    from .discovered_sensitive_type import DiscoveredSensitiveType
    from .dlp_evaluation_windows_devices_input import DlpEvaluationWindowsDevicesInput

@dataclass
class DlpEvaluationInput(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The currentLabel property
    current_label: Optional[CurrentLabel] = None
    # The discoveredSensitiveTypes property
    discovered_sensitive_types: Optional[List[DiscoveredSensitiveType]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DlpEvaluationInput:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DlpEvaluationInput
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.dlpEvaluationWindowsDevicesInput".casefold():
            from .dlp_evaluation_windows_devices_input import DlpEvaluationWindowsDevicesInput

            return DlpEvaluationWindowsDevicesInput()
        return DlpEvaluationInput()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .current_label import CurrentLabel
        from .discovered_sensitive_type import DiscoveredSensitiveType
        from .dlp_evaluation_windows_devices_input import DlpEvaluationWindowsDevicesInput

        from .current_label import CurrentLabel
        from .discovered_sensitive_type import DiscoveredSensitiveType
        from .dlp_evaluation_windows_devices_input import DlpEvaluationWindowsDevicesInput

        fields: Dict[str, Callable[[Any], None]] = {
            "currentLabel": lambda n : setattr(self, 'current_label', n.get_object_value(CurrentLabel)),
            "discoveredSensitiveTypes": lambda n : setattr(self, 'discovered_sensitive_types', n.get_collection_of_object_values(DiscoveredSensitiveType)),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_object_value("currentLabel", self.current_label)
        writer.write_collection_of_object_values("discoveredSensitiveTypes", self.discovered_sensitive_types)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

