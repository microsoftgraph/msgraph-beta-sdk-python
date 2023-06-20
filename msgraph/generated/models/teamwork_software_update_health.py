from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import teamwork_software_update_status

@dataclass
class TeamworkSoftwareUpdateHealth(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The software update available for the admin agent.
    admin_agent_software_update_status: Optional[teamwork_software_update_status.TeamworkSoftwareUpdateStatus] = None
    # The software update available for the company portal.
    company_portal_software_update_status: Optional[teamwork_software_update_status.TeamworkSoftwareUpdateStatus] = None
    # The software update available for the firmware.
    firmware_software_update_status: Optional[teamwork_software_update_status.TeamworkSoftwareUpdateStatus] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The software update available for the operating system.
    operating_system_software_update_status: Optional[teamwork_software_update_status.TeamworkSoftwareUpdateStatus] = None
    # The software update available for the partner agent.
    partner_agent_software_update_status: Optional[teamwork_software_update_status.TeamworkSoftwareUpdateStatus] = None
    # The software update available for the Teams client.
    teams_client_software_update_status: Optional[teamwork_software_update_status.TeamworkSoftwareUpdateStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeamworkSoftwareUpdateHealth:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TeamworkSoftwareUpdateHealth
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return TeamworkSoftwareUpdateHealth()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import teamwork_software_update_status

        from . import teamwork_software_update_status

        fields: Dict[str, Callable[[Any], None]] = {
            "adminAgentSoftwareUpdateStatus": lambda n : setattr(self, 'admin_agent_software_update_status', n.get_object_value(teamwork_software_update_status.TeamworkSoftwareUpdateStatus)),
            "companyPortalSoftwareUpdateStatus": lambda n : setattr(self, 'company_portal_software_update_status', n.get_object_value(teamwork_software_update_status.TeamworkSoftwareUpdateStatus)),
            "firmwareSoftwareUpdateStatus": lambda n : setattr(self, 'firmware_software_update_status', n.get_object_value(teamwork_software_update_status.TeamworkSoftwareUpdateStatus)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "operatingSystemSoftwareUpdateStatus": lambda n : setattr(self, 'operating_system_software_update_status', n.get_object_value(teamwork_software_update_status.TeamworkSoftwareUpdateStatus)),
            "partnerAgentSoftwareUpdateStatus": lambda n : setattr(self, 'partner_agent_software_update_status', n.get_object_value(teamwork_software_update_status.TeamworkSoftwareUpdateStatus)),
            "teamsClientSoftwareUpdateStatus": lambda n : setattr(self, 'teams_client_software_update_status', n.get_object_value(teamwork_software_update_status.TeamworkSoftwareUpdateStatus)),
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
        writer.write_object_value("adminAgentSoftwareUpdateStatus", self.admin_agent_software_update_status)
        writer.write_object_value("companyPortalSoftwareUpdateStatus", self.company_portal_software_update_status)
        writer.write_object_value("firmwareSoftwareUpdateStatus", self.firmware_software_update_status)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("operatingSystemSoftwareUpdateStatus", self.operating_system_software_update_status)
        writer.write_object_value("partnerAgentSoftwareUpdateStatus", self.partner_agent_software_update_status)
        writer.write_object_value("teamsClientSoftwareUpdateStatus", self.teams_client_software_update_status)
        writer.write_additional_data_value(self.additional_data)
    

