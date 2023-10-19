from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .evaluate_label_job_result import EvaluateLabelJobResult

@dataclass
class EvaluateLabelJobResultGroup(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The automatic property
    automatic: Optional[EvaluateLabelJobResult] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The recommended property
    recommended: Optional[EvaluateLabelJobResult] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EvaluateLabelJobResultGroup:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EvaluateLabelJobResultGroup
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return EvaluateLabelJobResultGroup()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .evaluate_label_job_result import EvaluateLabelJobResult

        from .evaluate_label_job_result import EvaluateLabelJobResult

        fields: Dict[str, Callable[[Any], None]] = {
            "automatic": lambda n : setattr(self, 'automatic', n.get_object_value(EvaluateLabelJobResult)),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "recommended": lambda n : setattr(self, 'recommended', n.get_object_value(EvaluateLabelJobResult)),
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
        writer.write_object_value("automatic", self.automatic)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_object_value("recommended", self.recommended)
        writer.write_additional_data_value(self.additional_data)
    

