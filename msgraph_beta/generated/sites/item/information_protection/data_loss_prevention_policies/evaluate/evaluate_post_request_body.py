from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ......models.dlp_evaluation_input import DlpEvaluationInput
    from ......models.dlp_notification import DlpNotification

@dataclass
class EvaluatePostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The evaluationInput property
    evaluation_input: Optional[DlpEvaluationInput] = None
    # The notificationInfo property
    notification_info: Optional[DlpNotification] = None
    # The target property
    target: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EvaluatePostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EvaluatePostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EvaluatePostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ......models.dlp_evaluation_input import DlpEvaluationInput
        from ......models.dlp_notification import DlpNotification

        from ......models.dlp_evaluation_input import DlpEvaluationInput
        from ......models.dlp_notification import DlpNotification

        fields: Dict[str, Callable[[Any], None]] = {
            "evaluationInput": lambda n : setattr(self, 'evaluation_input', n.get_object_value(DlpEvaluationInput)),
            "notificationInfo": lambda n : setattr(self, 'notification_info', n.get_object_value(DlpNotification)),
            "target": lambda n : setattr(self, 'target', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_object_value("evaluationInput", self.evaluation_input)
        writer.write_object_value("notificationInfo", self.notification_info)
        writer.write_str_value("target", self.target)
        writer.write_additional_data_value(self.additional_data)
    

