from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import inbound_flow, industry_data_connector, industry_data_run, reference_definition, role_group, source_system_definition, year_time_period_definition
    from .. import entity, long_running_operation

from .. import entity

class IndustryDataRoot(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new IndustryDataRoot and sets the default values.
        """
        super().__init__()
        # Set of connectors for importing data from source systems.
        self._data_connectors: Optional[List[industry_data_connector.IndustryDataConnector]] = None
        # Set of data import flow activities to bring data into the canonical store via a connector.
        self._inbound_flows: Optional[List[inbound_flow.InboundFlow]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Set of ephemeral operations that the system runs currently. Read-only.
        self._operations: Optional[List[long_running_operation.LongRunningOperation]] = None
        # Set of user modifiable system picker types.
        self._reference_definitions: Optional[List[reference_definition.ReferenceDefinition]] = None
        # Set of groups of individual roles that makes role-based admin simpler.
        self._role_groups: Optional[List[role_group.RoleGroup]] = None
        # Set of ephemeral runs which present the point-in-time that diagnostic state of activities performed by the system. Read-only.
        self._runs: Optional[List[industry_data_run.IndustryDataRun]] = None
        # Set of source definitions that represents real-world external systems.
        self._source_systems: Optional[List[source_system_definition.SourceSystemDefinition]] = None
        # Set of years represented in the system.
        self._years: Optional[List[year_time_period_definition.YearTimePeriodDefinition]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IndustryDataRoot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IndustryDataRoot
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return IndustryDataRoot()
    
    @property
    def data_connectors(self,) -> Optional[List[industry_data_connector.IndustryDataConnector]]:
        """
        Gets the dataConnectors property value. Set of connectors for importing data from source systems.
        Returns: Optional[List[industry_data_connector.IndustryDataConnector]]
        """
        return self._data_connectors
    
    @data_connectors.setter
    def data_connectors(self,value: Optional[List[industry_data_connector.IndustryDataConnector]] = None) -> None:
        """
        Sets the dataConnectors property value. Set of connectors for importing data from source systems.
        Args:
            value: Value to set for the data_connectors property.
        """
        self._data_connectors = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import inbound_flow, industry_data_connector, industry_data_run, reference_definition, role_group, source_system_definition, year_time_period_definition
        from .. import entity, long_running_operation

        fields: Dict[str, Callable[[Any], None]] = {
            "dataConnectors": lambda n : setattr(self, 'data_connectors', n.get_collection_of_object_values(industry_data_connector.IndustryDataConnector)),
            "inboundFlows": lambda n : setattr(self, 'inbound_flows', n.get_collection_of_object_values(inbound_flow.InboundFlow)),
            "operations": lambda n : setattr(self, 'operations', n.get_collection_of_object_values(long_running_operation.LongRunningOperation)),
            "referenceDefinitions": lambda n : setattr(self, 'reference_definitions', n.get_collection_of_object_values(reference_definition.ReferenceDefinition)),
            "roleGroups": lambda n : setattr(self, 'role_groups', n.get_collection_of_object_values(role_group.RoleGroup)),
            "runs": lambda n : setattr(self, 'runs', n.get_collection_of_object_values(industry_data_run.IndustryDataRun)),
            "sourceSystems": lambda n : setattr(self, 'source_systems', n.get_collection_of_object_values(source_system_definition.SourceSystemDefinition)),
            "years": lambda n : setattr(self, 'years', n.get_collection_of_object_values(year_time_period_definition.YearTimePeriodDefinition)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def inbound_flows(self,) -> Optional[List[inbound_flow.InboundFlow]]:
        """
        Gets the inboundFlows property value. Set of data import flow activities to bring data into the canonical store via a connector.
        Returns: Optional[List[inbound_flow.InboundFlow]]
        """
        return self._inbound_flows
    
    @inbound_flows.setter
    def inbound_flows(self,value: Optional[List[inbound_flow.InboundFlow]] = None) -> None:
        """
        Sets the inboundFlows property value. Set of data import flow activities to bring data into the canonical store via a connector.
        Args:
            value: Value to set for the inbound_flows property.
        """
        self._inbound_flows = value
    
    @property
    def operations(self,) -> Optional[List[long_running_operation.LongRunningOperation]]:
        """
        Gets the operations property value. Set of ephemeral operations that the system runs currently. Read-only.
        Returns: Optional[List[long_running_operation.LongRunningOperation]]
        """
        return self._operations
    
    @operations.setter
    def operations(self,value: Optional[List[long_running_operation.LongRunningOperation]] = None) -> None:
        """
        Sets the operations property value. Set of ephemeral operations that the system runs currently. Read-only.
        Args:
            value: Value to set for the operations property.
        """
        self._operations = value
    
    @property
    def reference_definitions(self,) -> Optional[List[reference_definition.ReferenceDefinition]]:
        """
        Gets the referenceDefinitions property value. Set of user modifiable system picker types.
        Returns: Optional[List[reference_definition.ReferenceDefinition]]
        """
        return self._reference_definitions
    
    @reference_definitions.setter
    def reference_definitions(self,value: Optional[List[reference_definition.ReferenceDefinition]] = None) -> None:
        """
        Sets the referenceDefinitions property value. Set of user modifiable system picker types.
        Args:
            value: Value to set for the reference_definitions property.
        """
        self._reference_definitions = value
    
    @property
    def role_groups(self,) -> Optional[List[role_group.RoleGroup]]:
        """
        Gets the roleGroups property value. Set of groups of individual roles that makes role-based admin simpler.
        Returns: Optional[List[role_group.RoleGroup]]
        """
        return self._role_groups
    
    @role_groups.setter
    def role_groups(self,value: Optional[List[role_group.RoleGroup]] = None) -> None:
        """
        Sets the roleGroups property value. Set of groups of individual roles that makes role-based admin simpler.
        Args:
            value: Value to set for the role_groups property.
        """
        self._role_groups = value
    
    @property
    def runs(self,) -> Optional[List[industry_data_run.IndustryDataRun]]:
        """
        Gets the runs property value. Set of ephemeral runs which present the point-in-time that diagnostic state of activities performed by the system. Read-only.
        Returns: Optional[List[industry_data_run.IndustryDataRun]]
        """
        return self._runs
    
    @runs.setter
    def runs(self,value: Optional[List[industry_data_run.IndustryDataRun]] = None) -> None:
        """
        Sets the runs property value. Set of ephemeral runs which present the point-in-time that diagnostic state of activities performed by the system. Read-only.
        Args:
            value: Value to set for the runs property.
        """
        self._runs = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("dataConnectors", self.data_connectors)
        writer.write_collection_of_object_values("inboundFlows", self.inbound_flows)
        writer.write_collection_of_object_values("operations", self.operations)
        writer.write_collection_of_object_values("referenceDefinitions", self.reference_definitions)
        writer.write_collection_of_object_values("roleGroups", self.role_groups)
        writer.write_collection_of_object_values("runs", self.runs)
        writer.write_collection_of_object_values("sourceSystems", self.source_systems)
        writer.write_collection_of_object_values("years", self.years)
    
    @property
    def source_systems(self,) -> Optional[List[source_system_definition.SourceSystemDefinition]]:
        """
        Gets the sourceSystems property value. Set of source definitions that represents real-world external systems.
        Returns: Optional[List[source_system_definition.SourceSystemDefinition]]
        """
        return self._source_systems
    
    @source_systems.setter
    def source_systems(self,value: Optional[List[source_system_definition.SourceSystemDefinition]] = None) -> None:
        """
        Sets the sourceSystems property value. Set of source definitions that represents real-world external systems.
        Args:
            value: Value to set for the source_systems property.
        """
        self._source_systems = value
    
    @property
    def years(self,) -> Optional[List[year_time_period_definition.YearTimePeriodDefinition]]:
        """
        Gets the years property value. Set of years represented in the system.
        Returns: Optional[List[year_time_period_definition.YearTimePeriodDefinition]]
        """
        return self._years
    
    @years.setter
    def years(self,value: Optional[List[year_time_period_definition.YearTimePeriodDefinition]] = None) -> None:
        """
        Sets the years property value. Set of years represented in the system.
        Args:
            value: Value to set for the years property.
        """
        self._years = value
    

