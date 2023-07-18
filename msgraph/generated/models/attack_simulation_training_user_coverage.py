from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .attack_simulation_user import AttackSimulationUser
    from .user_training_status_info import UserTrainingStatusInfo

@dataclass
class AttackSimulationTrainingUserCoverage(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # User in an attack simulation and training campaign.
    attack_simulation_user: Optional[AttackSimulationUser] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # List of assigned trainings and their statuses for the user.
    user_trainings: Optional[List[UserTrainingStatusInfo]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AttackSimulationTrainingUserCoverage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AttackSimulationTrainingUserCoverage
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AttackSimulationTrainingUserCoverage()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .attack_simulation_user import AttackSimulationUser
        from .user_training_status_info import UserTrainingStatusInfo

        from .attack_simulation_user import AttackSimulationUser
        from .user_training_status_info import UserTrainingStatusInfo

        fields: Dict[str, Callable[[Any], None]] = {
            "attackSimulationUser": lambda n : setattr(self, 'attack_simulation_user', n.get_object_value(AttackSimulationUser)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "userTrainings": lambda n : setattr(self, 'user_trainings', n.get_collection_of_object_values(UserTrainingStatusInfo)),
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
        writer.write_object_value("attackSimulationUser", self.attack_simulation_user)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("userTrainings", self.user_trainings)
        writer.write_additional_data_value(self.additional_data)
    

