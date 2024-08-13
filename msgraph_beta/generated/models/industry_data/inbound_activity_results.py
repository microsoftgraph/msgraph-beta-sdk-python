from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .industry_data_activity_statistics import IndustryDataActivityStatistics
    from .industry_data_run_entity_count_metric import IndustryDataRunEntityCountMetric
    from .industry_data_run_role_count_metric import IndustryDataRunRoleCountMetric

from .industry_data_activity_statistics import IndustryDataActivityStatistics

@dataclass
class InboundActivityResults(IndustryDataActivityStatistics):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.industryData.inboundActivityResults"
    # Number of errors encountered while processing the inbound flow.
    errors: Optional[int] = None
    # Counts of active and inactive groups processed by the inbound flow.
    groups: Optional[IndustryDataRunEntityCountMetric] = None
    # Number of people matched to a Microsoft Entra user, by role.
    matched_people_by_role: Optional[List[IndustryDataRunRoleCountMetric]] = None
    # Counts of active and inactive memberships processed by the inbound flow.
    memberships: Optional[IndustryDataRunEntityCountMetric] = None
    # Counts of active and inactive organizations processed by the inbound flow.
    organizations: Optional[IndustryDataRunEntityCountMetric] = None
    # Counts of active and inactive people processed by the inbound flow.
    people: Optional[IndustryDataRunEntityCountMetric] = None
    # Number of people not matched to a Microsoft Entra user, by role.
    unmatched_people_by_role: Optional[List[IndustryDataRunRoleCountMetric]] = None
    # Number of warnings encountered while processing the inbound flow.
    warnings: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> InboundActivityResults:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: InboundActivityResults
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return InboundActivityResults()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .industry_data_activity_statistics import IndustryDataActivityStatistics
        from .industry_data_run_entity_count_metric import IndustryDataRunEntityCountMetric
        from .industry_data_run_role_count_metric import IndustryDataRunRoleCountMetric

        from .industry_data_activity_statistics import IndustryDataActivityStatistics
        from .industry_data_run_entity_count_metric import IndustryDataRunEntityCountMetric
        from .industry_data_run_role_count_metric import IndustryDataRunRoleCountMetric

        fields: Dict[str, Callable[[Any], None]] = {
            "errors": lambda n : setattr(self, 'errors', n.get_int_value()),
            "groups": lambda n : setattr(self, 'groups', n.get_object_value(IndustryDataRunEntityCountMetric)),
            "matchedPeopleByRole": lambda n : setattr(self, 'matched_people_by_role', n.get_collection_of_object_values(IndustryDataRunRoleCountMetric)),
            "memberships": lambda n : setattr(self, 'memberships', n.get_object_value(IndustryDataRunEntityCountMetric)),
            "organizations": lambda n : setattr(self, 'organizations', n.get_object_value(IndustryDataRunEntityCountMetric)),
            "people": lambda n : setattr(self, 'people', n.get_object_value(IndustryDataRunEntityCountMetric)),
            "unmatchedPeopleByRole": lambda n : setattr(self, 'unmatched_people_by_role', n.get_collection_of_object_values(IndustryDataRunRoleCountMetric)),
            "warnings": lambda n : setattr(self, 'warnings', n.get_int_value()),
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
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
    

