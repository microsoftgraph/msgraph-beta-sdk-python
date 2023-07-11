from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .assigned_training_info import AssignedTrainingInfo

@dataclass
class TrainingEventsContent(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # List of assigned trainings and their information in an attack simulation and training campaign.
    assigned_trainings_infos: Optional[List[AssignedTrainingInfo]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Number of users who were assigned trainings in an attack simulation and training campaign.
    trainings_assigned_user_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TrainingEventsContent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TrainingEventsContent
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return TrainingEventsContent()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .assigned_training_info import AssignedTrainingInfo

        from .assigned_training_info import AssignedTrainingInfo

        fields: Dict[str, Callable[[Any], None]] = {
            "assignedTrainingsInfos": lambda n : setattr(self, 'assigned_trainings_infos', n.get_collection_of_object_values(AssignedTrainingInfo)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "trainingsAssignedUserCount": lambda n : setattr(self, 'trainings_assigned_user_count', n.get_int_value()),
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
        writer.write_collection_of_object_values("assignedTrainingsInfos", self.assigned_trainings_infos)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("trainingsAssignedUserCount", self.trainings_assigned_user_count)
        writer.write_additional_data_value(self.additional_data)
    

