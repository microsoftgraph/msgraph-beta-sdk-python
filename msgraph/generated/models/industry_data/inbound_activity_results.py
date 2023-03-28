from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import industry_data_activity_statistics, industry_data_run_entity_count_metric, industry_data_run_role_count_metric

from . import industry_data_activity_statistics

class InboundActivityResults(industry_data_activity_statistics.IndustryDataActivityStatistics):
    def __init__(self,) -> None:
        """
        Instantiates a new InboundActivityResults and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.industryData.inboundActivityResults"
        # Number of errors encountered while processing the inbound flow.
        self._errors: Optional[int] = None
        # Counts of active and inactive groups processed by the inbound flow.
        self._groups: Optional[industry_data_run_entity_count_metric.IndustryDataRunEntityCountMetric] = None
        # Number of people matched to an Azure Active Directory user, by role.
        self._matched_people_by_role: Optional[List[industry_data_run_role_count_metric.IndustryDataRunRoleCountMetric]] = None
        # Counts of active and inactive memberships processed by the inbound flow.
        self._memberships: Optional[industry_data_run_entity_count_metric.IndustryDataRunEntityCountMetric] = None
        # Counts of active and inactive organizations processed by the inbound flow.
        self._organizations: Optional[industry_data_run_entity_count_metric.IndustryDataRunEntityCountMetric] = None
        # Counts of active and inactive people processed by the inbound flow.
        self._people: Optional[industry_data_run_entity_count_metric.IndustryDataRunEntityCountMetric] = None
        # Number of people not matched to an Azure Active Directory user, by role.
        self._unmatched_people_by_role: Optional[List[industry_data_run_role_count_metric.IndustryDataRunRoleCountMetric]] = None
        # Number of warnings encountered while processing the inbound flow.
        self._warnings: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> InboundActivityResults:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: InboundActivityResults
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return InboundActivityResults()
    
    @property
    def errors(self,) -> Optional[int]:
        """
        Gets the errors property value. Number of errors encountered while processing the inbound flow.
        Returns: Optional[int]
        """
        return self._errors
    
    @errors.setter
    def errors(self,value: Optional[int] = None) -> None:
        """
        Sets the errors property value. Number of errors encountered while processing the inbound flow.
        Args:
            value: Value to set for the errors property.
        """
        self._errors = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import industry_data_activity_statistics, industry_data_run_entity_count_metric, industry_data_run_role_count_metric

        fields: Dict[str, Callable[[Any], None]] = {
            "errors": lambda n : setattr(self, 'errors', n.get_int_value()),
            "groups": lambda n : setattr(self, 'groups', n.get_object_value(industry_data_run_entity_count_metric.IndustryDataRunEntityCountMetric)),
            "matchedPeopleByRole": lambda n : setattr(self, 'matched_people_by_role', n.get_collection_of_object_values(industry_data_run_role_count_metric.IndustryDataRunRoleCountMetric)),
            "memberships": lambda n : setattr(self, 'memberships', n.get_object_value(industry_data_run_entity_count_metric.IndustryDataRunEntityCountMetric)),
            "organizations": lambda n : setattr(self, 'organizations', n.get_object_value(industry_data_run_entity_count_metric.IndustryDataRunEntityCountMetric)),
            "people": lambda n : setattr(self, 'people', n.get_object_value(industry_data_run_entity_count_metric.IndustryDataRunEntityCountMetric)),
            "unmatchedPeopleByRole": lambda n : setattr(self, 'unmatched_people_by_role', n.get_collection_of_object_values(industry_data_run_role_count_metric.IndustryDataRunRoleCountMetric)),
            "warnings": lambda n : setattr(self, 'warnings', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def groups(self,) -> Optional[industry_data_run_entity_count_metric.IndustryDataRunEntityCountMetric]:
        """
        Gets the groups property value. Counts of active and inactive groups processed by the inbound flow.
        Returns: Optional[industry_data_run_entity_count_metric.IndustryDataRunEntityCountMetric]
        """
        return self._groups
    
    @groups.setter
    def groups(self,value: Optional[industry_data_run_entity_count_metric.IndustryDataRunEntityCountMetric] = None) -> None:
        """
        Sets the groups property value. Counts of active and inactive groups processed by the inbound flow.
        Args:
            value: Value to set for the groups property.
        """
        self._groups = value
    
    @property
    def matched_people_by_role(self,) -> Optional[List[industry_data_run_role_count_metric.IndustryDataRunRoleCountMetric]]:
        """
        Gets the matchedPeopleByRole property value. Number of people matched to an Azure Active Directory user, by role.
        Returns: Optional[List[industry_data_run_role_count_metric.IndustryDataRunRoleCountMetric]]
        """
        return self._matched_people_by_role
    
    @matched_people_by_role.setter
    def matched_people_by_role(self,value: Optional[List[industry_data_run_role_count_metric.IndustryDataRunRoleCountMetric]] = None) -> None:
        """
        Sets the matchedPeopleByRole property value. Number of people matched to an Azure Active Directory user, by role.
        Args:
            value: Value to set for the matched_people_by_role property.
        """
        self._matched_people_by_role = value
    
    @property
    def memberships(self,) -> Optional[industry_data_run_entity_count_metric.IndustryDataRunEntityCountMetric]:
        """
        Gets the memberships property value. Counts of active and inactive memberships processed by the inbound flow.
        Returns: Optional[industry_data_run_entity_count_metric.IndustryDataRunEntityCountMetric]
        """
        return self._memberships
    
    @memberships.setter
    def memberships(self,value: Optional[industry_data_run_entity_count_metric.IndustryDataRunEntityCountMetric] = None) -> None:
        """
        Sets the memberships property value. Counts of active and inactive memberships processed by the inbound flow.
        Args:
            value: Value to set for the memberships property.
        """
        self._memberships = value
    
    @property
    def organizations(self,) -> Optional[industry_data_run_entity_count_metric.IndustryDataRunEntityCountMetric]:
        """
        Gets the organizations property value. Counts of active and inactive organizations processed by the inbound flow.
        Returns: Optional[industry_data_run_entity_count_metric.IndustryDataRunEntityCountMetric]
        """
        return self._organizations
    
    @organizations.setter
    def organizations(self,value: Optional[industry_data_run_entity_count_metric.IndustryDataRunEntityCountMetric] = None) -> None:
        """
        Sets the organizations property value. Counts of active and inactive organizations processed by the inbound flow.
        Args:
            value: Value to set for the organizations property.
        """
        self._organizations = value
    
    @property
    def people(self,) -> Optional[industry_data_run_entity_count_metric.IndustryDataRunEntityCountMetric]:
        """
        Gets the people property value. Counts of active and inactive people processed by the inbound flow.
        Returns: Optional[industry_data_run_entity_count_metric.IndustryDataRunEntityCountMetric]
        """
        return self._people
    
    @people.setter
    def people(self,value: Optional[industry_data_run_entity_count_metric.IndustryDataRunEntityCountMetric] = None) -> None:
        """
        Sets the people property value. Counts of active and inactive people processed by the inbound flow.
        Args:
            value: Value to set for the people property.
        """
        self._people = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
    
    @property
    def unmatched_people_by_role(self,) -> Optional[List[industry_data_run_role_count_metric.IndustryDataRunRoleCountMetric]]:
        """
        Gets the unmatchedPeopleByRole property value. Number of people not matched to an Azure Active Directory user, by role.
        Returns: Optional[List[industry_data_run_role_count_metric.IndustryDataRunRoleCountMetric]]
        """
        return self._unmatched_people_by_role
    
    @unmatched_people_by_role.setter
    def unmatched_people_by_role(self,value: Optional[List[industry_data_run_role_count_metric.IndustryDataRunRoleCountMetric]] = None) -> None:
        """
        Sets the unmatchedPeopleByRole property value. Number of people not matched to an Azure Active Directory user, by role.
        Args:
            value: Value to set for the unmatched_people_by_role property.
        """
        self._unmatched_people_by_role = value
    
    @property
    def warnings(self,) -> Optional[int]:
        """
        Gets the warnings property value. Number of warnings encountered while processing the inbound flow.
        Returns: Optional[int]
        """
        return self._warnings
    
    @warnings.setter
    def warnings(self,value: Optional[int] = None) -> None:
        """
        Sets the warnings property value. Number of warnings encountered while processing the inbound flow.
        Args:
            value: Value to set for the warnings property.
        """
        self._warnings = value
    

