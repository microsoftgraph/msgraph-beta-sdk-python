from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

@dataclass
class AttackSimulationInfo(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The date and time of the attack simulation.
    attack_sim_date_time: Optional[datetime.datetime] = None
    # The duration (in time) for the attack simulation.
    attack_sim_duration_time: Optional[datetime.timedelta] = None
    # The activity ID for the attack simulation.
    attack_sim_id: Optional[UUID] = None
    # The unique identifier for the user who got the attack simulation email.
    attack_sim_user_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AttackSimulationInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AttackSimulationInfo
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AttackSimulationInfo()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "attackSimDateTime": lambda n : setattr(self, 'attack_sim_date_time', n.get_datetime_value()),
            "attackSimDurationTime": lambda n : setattr(self, 'attack_sim_duration_time', n.get_timedelta_value()),
            "attackSimId": lambda n : setattr(self, 'attack_sim_id', n.get_uuid_value()),
            "attackSimUserId": lambda n : setattr(self, 'attack_sim_user_id', n.get_str_value()),
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
        writer.write_datetime_value("attackSimDateTime", self.attack_sim_date_time)
        writer.write_timedelta_value("attackSimDurationTime", self.attack_sim_duration_time)
        writer.write_uuid_value("attackSimId", self.attack_sim_id)
        writer.write_str_value("attackSimUserId", self.attack_sim_user_id)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

