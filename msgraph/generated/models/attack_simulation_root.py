from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import attack_simulation_operation, entity, payload, simulation, simulation_automation

from . import entity

class AttackSimulationRoot(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new AttackSimulationRoot and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Represents an attack simulation training operation.
        self._operations: Optional[List[attack_simulation_operation.AttackSimulationOperation]] = None
        # Represents an attack simulation training campaign payload in a tenant.
        self._payloads: Optional[List[payload.Payload]] = None
        # Represents simulation automation created to run on a tenant.
        self._simulation_automations: Optional[List[simulation_automation.SimulationAutomation]] = None
        # Represents an attack simulation training campaign in a tenant.
        self._simulations: Optional[List[simulation.Simulation]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AttackSimulationRoot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AttackSimulationRoot
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AttackSimulationRoot()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import attack_simulation_operation, entity, payload, simulation, simulation_automation

        fields: Dict[str, Callable[[Any], None]] = {
            "operations": lambda n : setattr(self, 'operations', n.get_collection_of_object_values(attack_simulation_operation.AttackSimulationOperation)),
            "payloads": lambda n : setattr(self, 'payloads', n.get_collection_of_object_values(payload.Payload)),
            "simulations": lambda n : setattr(self, 'simulations', n.get_collection_of_object_values(simulation.Simulation)),
            "simulationAutomations": lambda n : setattr(self, 'simulation_automations', n.get_collection_of_object_values(simulation_automation.SimulationAutomation)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def operations(self,) -> Optional[List[attack_simulation_operation.AttackSimulationOperation]]:
        """
        Gets the operations property value. Represents an attack simulation training operation.
        Returns: Optional[List[attack_simulation_operation.AttackSimulationOperation]]
        """
        return self._operations
    
    @operations.setter
    def operations(self,value: Optional[List[attack_simulation_operation.AttackSimulationOperation]] = None) -> None:
        """
        Sets the operations property value. Represents an attack simulation training operation.
        Args:
            value: Value to set for the operations property.
        """
        self._operations = value
    
    @property
    def payloads(self,) -> Optional[List[payload.Payload]]:
        """
        Gets the payloads property value. Represents an attack simulation training campaign payload in a tenant.
        Returns: Optional[List[payload.Payload]]
        """
        return self._payloads
    
    @payloads.setter
    def payloads(self,value: Optional[List[payload.Payload]] = None) -> None:
        """
        Sets the payloads property value. Represents an attack simulation training campaign payload in a tenant.
        Args:
            value: Value to set for the payloads property.
        """
        self._payloads = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("operations", self.operations)
        writer.write_collection_of_object_values("payloads", self.payloads)
        writer.write_collection_of_object_values("simulations", self.simulations)
        writer.write_collection_of_object_values("simulationAutomations", self.simulation_automations)
    
    @property
    def simulation_automations(self,) -> Optional[List[simulation_automation.SimulationAutomation]]:
        """
        Gets the simulationAutomations property value. Represents simulation automation created to run on a tenant.
        Returns: Optional[List[simulation_automation.SimulationAutomation]]
        """
        return self._simulation_automations
    
    @simulation_automations.setter
    def simulation_automations(self,value: Optional[List[simulation_automation.SimulationAutomation]] = None) -> None:
        """
        Sets the simulationAutomations property value. Represents simulation automation created to run on a tenant.
        Args:
            value: Value to set for the simulation_automations property.
        """
        self._simulation_automations = value
    
    @property
    def simulations(self,) -> Optional[List[simulation.Simulation]]:
        """
        Gets the simulations property value. Represents an attack simulation training campaign in a tenant.
        Returns: Optional[List[simulation.Simulation]]
        """
        return self._simulations
    
    @simulations.setter
    def simulations(self,value: Optional[List[simulation.Simulation]] = None) -> None:
        """
        Sets the simulations property value. Represents an attack simulation training campaign in a tenant.
        Args:
            value: Value to set for the simulations property.
        """
        self._simulations = value
    

