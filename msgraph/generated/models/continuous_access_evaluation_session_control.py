from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .continuous_access_evaluation_mode import ContinuousAccessEvaluationMode

@dataclass
class ContinuousAccessEvaluationSessionControl(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Specifies continuous access evaluation settings. The possible values are: strictEnforcement, disabled, unknownFutureValue, strictLocation. Note that you must use the Prefer: include-unknown-enum-members request header to get the following value(s) in this evolvable enum: strictLocation.
    mode: Optional[ContinuousAccessEvaluationMode] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ContinuousAccessEvaluationSessionControl:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ContinuousAccessEvaluationSessionControl
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ContinuousAccessEvaluationSessionControl()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .continuous_access_evaluation_mode import ContinuousAccessEvaluationMode

        from .continuous_access_evaluation_mode import ContinuousAccessEvaluationMode

        fields: Dict[str, Callable[[Any], None]] = {
            "mode": lambda n : setattr(self, 'mode', n.get_enum_value(ContinuousAccessEvaluationMode)),
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
        writer.write_enum_value("mode", self.mode)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

