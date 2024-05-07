from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .health_issue_severity import HealthIssueSeverity
    from .health_issue_status import HealthIssueStatus
    from .health_issue_type import HealthIssueType

from ..entity import Entity

@dataclass
class HealthIssue(Entity):
    # Contains additional information about the issue, such as a list of items to fix.
    additional_information: Optional[List[str]] = None
    # The date and time of when the health issue was generated.
    created_date_time: Optional[datetime.datetime] = None
    # Contains more detailed information about the health issue.
    description: Optional[str] = None
    # The display name of the health issue.
    display_name: Optional[str] = None
    # A list of the fully qualified domain names of the domains or the sensors the health issue is related to.
    domain_names: Optional[List[str]] = None
    # The type of the health issue. The possible values are: sensor, global, unknownFutureValue. For a list of all health issues and their identifiers, see Microsoft Defender for Identity health issues.
    health_issue_type: Optional[HealthIssueType] = None
    # The type identifier of the health issue. For a list of all health issues and their identifiers, see Microsoft Defender for Identity health issues.
    issue_type_id: Optional[str] = None
    # The date and time of when the health issue was last updated.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # This field contains a list of recommended actions that can be taken to resolve the issue effectively and efficiently. These actions might include how to investigate the issue further. Not limited to prewritten responses.
    recommendations: Optional[List[str]] = None
    # Contains a list of commands from the product's PowerShell module that can be used to resolve the issue, if available. If there aren't any commands that can be used to solve the issue, this field is empty. The commands, if present, provide a quick and efficient way to address the issue. The commands run in order for the single recommended fix.
    recommended_action_commands: Optional[List[str]] = None
    # A list of the dns names of the sensors the health issue is related to.
    sensor_d_n_s_names: Optional[List[str]] = None
    # The severity of the health issue. The possible values are: low, medium, high, unknownFutureValue.
    severity: Optional[HealthIssueSeverity] = None
    # The status of the health issue. The possible values are: open, closed, suppressed, unknownFutureValue.
    status: Optional[HealthIssueStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> HealthIssue:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: HealthIssue
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return HealthIssue()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .health_issue_severity import HealthIssueSeverity
        from .health_issue_status import HealthIssueStatus
        from .health_issue_type import HealthIssueType

        from ..entity import Entity
        from .health_issue_severity import HealthIssueSeverity
        from .health_issue_status import HealthIssueStatus
        from .health_issue_type import HealthIssueType

        fields: Dict[str, Callable[[Any], None]] = {
            "additionalInformation": lambda n : setattr(self, 'additional_information', n.get_collection_of_primitive_values(str)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "domainNames": lambda n : setattr(self, 'domain_names', n.get_collection_of_primitive_values(str)),
            "healthIssueType": lambda n : setattr(self, 'health_issue_type', n.get_enum_value(HealthIssueType)),
            "issueTypeId": lambda n : setattr(self, 'issue_type_id', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "recommendations": lambda n : setattr(self, 'recommendations', n.get_collection_of_primitive_values(str)),
            "recommendedActionCommands": lambda n : setattr(self, 'recommended_action_commands', n.get_collection_of_primitive_values(str)),
            "sensorDNSNames": lambda n : setattr(self, 'sensor_d_n_s_names', n.get_collection_of_primitive_values(str)),
            "severity": lambda n : setattr(self, 'severity', n.get_enum_value(HealthIssueSeverity)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(HealthIssueStatus)),
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
        writer.write_collection_of_primitive_values("additionalInformation", self.additional_information)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_primitive_values("domainNames", self.domain_names)
        writer.write_enum_value("healthIssueType", self.health_issue_type)
        writer.write_str_value("issueTypeId", self.issue_type_id)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_collection_of_primitive_values("recommendations", self.recommendations)
        writer.write_collection_of_primitive_values("recommendedActionCommands", self.recommended_action_commands)
        writer.write_collection_of_primitive_values("sensorDNSNames", self.sensor_d_n_s_names)
        writer.write_enum_value("severity", self.severity)
        writer.write_enum_value("status", self.status)
    

