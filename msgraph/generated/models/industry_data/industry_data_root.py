from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from ..long_running_operation import LongRunningOperation
    from .inbound_flow import InboundFlow
    from .industry_data_connector import IndustryDataConnector
    from .industry_data_run import IndustryDataRun
    from .reference_definition import ReferenceDefinition
    from .role_group import RoleGroup
    from .source_system_definition import SourceSystemDefinition
    from .year_time_period_definition import YearTimePeriodDefinition

from ..entity import Entity

@dataclass
class IndustryDataRoot(Entity):
    # Set of connectors for importing data from source systems.
    data_connectors: Optional[List[IndustryDataConnector]] = None
    # Set of data import flow activities to bring data into the canonical store via a connector.
    inbound_flows: Optional[List[InboundFlow]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Set of ephemeral operations that the system runs currently. Read-only.
    operations: Optional[List[LongRunningOperation]] = None
    # Set of user modifiable system picker types.
    reference_definitions: Optional[List[ReferenceDefinition]] = None
    # Set of groups of individual roles that makes role-based admin simpler.
    role_groups: Optional[List[RoleGroup]] = None
    # Set of ephemeral runs which present the point-in-time that diagnostic state of activities performed by the system. Read-only.
    runs: Optional[List[IndustryDataRun]] = None
    # Set of source definitions that represents real-world external systems.
    source_systems: Optional[List[SourceSystemDefinition]] = None
    # Set of years represented in the system.
    years: Optional[List[YearTimePeriodDefinition]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IndustryDataRoot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IndustryDataRoot
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return IndustryDataRoot()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from ..long_running_operation import LongRunningOperation
        from .inbound_flow import InboundFlow
        from .industry_data_connector import IndustryDataConnector
        from .industry_data_run import IndustryDataRun
        from .reference_definition import ReferenceDefinition
        from .role_group import RoleGroup
        from .source_system_definition import SourceSystemDefinition
        from .year_time_period_definition import YearTimePeriodDefinition

        from ..entity import Entity
        from ..long_running_operation import LongRunningOperation
        from .inbound_flow import InboundFlow
        from .industry_data_connector import IndustryDataConnector
        from .industry_data_run import IndustryDataRun
        from .reference_definition import ReferenceDefinition
        from .role_group import RoleGroup
        from .source_system_definition import SourceSystemDefinition
        from .year_time_period_definition import YearTimePeriodDefinition

        fields: Dict[str, Callable[[Any], None]] = {
            "dataConnectors": lambda n : setattr(self, 'data_connectors', n.get_collection_of_object_values(IndustryDataConnector)),
            "inboundFlows": lambda n : setattr(self, 'inbound_flows', n.get_collection_of_object_values(InboundFlow)),
            "operations": lambda n : setattr(self, 'operations', n.get_collection_of_object_values(LongRunningOperation)),
            "referenceDefinitions": lambda n : setattr(self, 'reference_definitions', n.get_collection_of_object_values(ReferenceDefinition)),
            "roleGroups": lambda n : setattr(self, 'role_groups', n.get_collection_of_object_values(RoleGroup)),
            "runs": lambda n : setattr(self, 'runs', n.get_collection_of_object_values(IndustryDataRun)),
            "sourceSystems": lambda n : setattr(self, 'source_systems', n.get_collection_of_object_values(SourceSystemDefinition)),
            "years": lambda n : setattr(self, 'years', n.get_collection_of_object_values(YearTimePeriodDefinition)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("dataConnectors", self.data_connectors)
        writer.write_collection_of_object_values("inboundFlows", self.inbound_flows)
        writer.write_collection_of_object_values("operations", self.operations)
        writer.write_collection_of_object_values("referenceDefinitions", self.reference_definitions)
        writer.write_collection_of_object_values("roleGroups", self.role_groups)
        writer.write_collection_of_object_values("runs", self.runs)
        writer.write_collection_of_object_values("sourceSystems", self.source_systems)
        writer.write_collection_of_object_values("years", self.years)
    

