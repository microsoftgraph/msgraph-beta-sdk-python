from __future__ import annotations
from datetime import datetime, timedelta
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class AttackSimulationInfo(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def attack_sim_date_time(self,) -> Optional[datetime]:
        """
        Gets the attackSimDateTime property value. The date and time of the attack simulation.
        Returns: Optional[datetime]
        """
        return self._attack_sim_date_time
    
    @attack_sim_date_time.setter
    def attack_sim_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the attackSimDateTime property value. The date and time of the attack simulation.
        Args:
            value: Value to set for the attackSimDateTime property.
        """
        self._attack_sim_date_time = value
    
    @property
    def attack_sim_duration_time(self,) -> Optional[Timedelta]:
        """
        Gets the attackSimDurationTime property value. The duration (in time) for the attack simulation.
        Returns: Optional[Timedelta]
        """
        return self._attack_sim_duration_time
    
    @attack_sim_duration_time.setter
    def attack_sim_duration_time(self,value: Optional[Timedelta] = None) -> None:
        """
        Sets the attackSimDurationTime property value. The duration (in time) for the attack simulation.
        Args:
            value: Value to set for the attackSimDurationTime property.
        """
        self._attack_sim_duration_time = value
    
    @property
    def attack_sim_id(self,) -> Optional[Guid]:
        """
        Gets the attackSimId property value. The activity ID for the attack simulation.
        Returns: Optional[Guid]
        """
        return self._attack_sim_id
    
    @attack_sim_id.setter
    def attack_sim_id(self,value: Optional[Guid] = None) -> None:
        """
        Sets the attackSimId property value. The activity ID for the attack simulation.
        Args:
            value: Value to set for the attackSimId property.
        """
        self._attack_sim_id = value
    
    @property
    def attack_sim_user_id(self,) -> Optional[str]:
        """
        Gets the attackSimUserId property value. The unique identifier for the user who got the attack simulation email.
        Returns: Optional[str]
        """
        return self._attack_sim_user_id
    
    @attack_sim_user_id.setter
    def attack_sim_user_id(self,value: Optional[str] = None) -> None:
        """
        Sets the attackSimUserId property value. The unique identifier for the user who got the attack simulation email.
        Args:
            value: Value to set for the attackSimUserId property.
        """
        self._attack_sim_user_id = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new attackSimulationInfo and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The date and time of the attack simulation.
        self._attack_sim_date_time: Optional[datetime] = None
        # The duration (in time) for the attack simulation.
        self._attack_sim_duration_time: Optional[Timedelta] = None
        # The activity ID for the attack simulation.
        self._attack_sim_id: Optional[Guid] = None
        # The unique identifier for the user who got the attack simulation email.
        self._attack_sim_user_id: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AttackSimulationInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AttackSimulationInfo
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AttackSimulationInfo()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "attack_sim_date_time": lambda n : setattr(self, 'attack_sim_date_time', n.get_datetime_value()),
            "attack_sim_duration_time": lambda n : setattr(self, 'attack_sim_duration_time', n.get_object_value(Timedelta)),
            "attack_sim_id": lambda n : setattr(self, 'attack_sim_id', n.get_object_value(Guid)),
            "attack_sim_user_id": lambda n : setattr(self, 'attack_sim_user_id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_datetime_value("attackSimDateTime", self.attack_sim_date_time)
        writer.write_object_value("attackSimDurationTime", self.attack_sim_duration_time)
        writer.write_object_value("attackSimId", self.attack_sim_id)
        writer.write_str_value("attackSimUserId", self.attack_sim_user_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

