from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .training_events_content import TrainingEventsContent
    from .training_notification_delivery import TrainingNotificationDelivery
    from .user_training_completion_summary import UserTrainingCompletionSummary

@dataclass
class TrainingCampaignReportOverview(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The OdataType property
    odata_type: Optional[str] = None
    # The trainingModuleCompletion property
    training_module_completion: Optional[TrainingEventsContent] = None
    # The trainingNotificationDeliveryStatus property
    training_notification_delivery_status: Optional[TrainingNotificationDelivery] = None
    # The userCompletionStatus property
    user_completion_status: Optional[UserTrainingCompletionSummary] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TrainingCampaignReportOverview:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TrainingCampaignReportOverview
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return TrainingCampaignReportOverview()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .training_events_content import TrainingEventsContent
        from .training_notification_delivery import TrainingNotificationDelivery
        from .user_training_completion_summary import UserTrainingCompletionSummary

        from .training_events_content import TrainingEventsContent
        from .training_notification_delivery import TrainingNotificationDelivery
        from .user_training_completion_summary import UserTrainingCompletionSummary

        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "trainingModuleCompletion": lambda n : setattr(self, 'training_module_completion', n.get_object_value(TrainingEventsContent)),
            "trainingNotificationDeliveryStatus": lambda n : setattr(self, 'training_notification_delivery_status', n.get_object_value(TrainingNotificationDelivery)),
            "userCompletionStatus": lambda n : setattr(self, 'user_completion_status', n.get_object_value(UserTrainingCompletionSummary)),
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("trainingModuleCompletion", self.training_module_completion)
        writer.write_object_value("trainingNotificationDeliveryStatus", self.training_notification_delivery_status)
        writer.write_object_value("userCompletionStatus", self.user_completion_status)
        writer.write_additional_data_value(self.additional_data)
    

