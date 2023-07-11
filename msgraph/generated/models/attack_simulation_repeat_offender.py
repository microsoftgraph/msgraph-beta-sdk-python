from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .attack_simulation_user import AttackSimulationUser

@dataclass
class AttackSimulationRepeatOffender(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The user in an attack simulation and training campaign.
    attack_simulation_user: Optional[AttackSimulationUser] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Number of repeat offences of the user in attack simulation and training campaigns.
    repeat_offence_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AttackSimulationRepeatOffender:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AttackSimulationRepeatOffender
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AttackSimulationRepeatOffender()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .attack_simulation_user import AttackSimulationUser

        from .attack_simulation_user import AttackSimulationUser

        fields: Dict[str, Callable[[Any], None]] = {
            "attackSimulationUser": lambda n : setattr(self, 'attack_simulation_user', n.get_object_value(AttackSimulationUser)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "repeatOffenceCount": lambda n : setattr(self, 'repeat_offence_count', n.get_int_value()),
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
        writer.write_int_value("repeatOffenceCount", self.repeat_offence_count)
        writer.write_additional_data_value(self.additional_data)
    

