from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

teamwork_software_update_status = lazy_import('msgraph.generated.models.teamwork_software_update_status')

class TeamworkSoftwareUpdateHealth(AdditionalDataHolder, Parsable):
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
    def admin_agent_software_update_status(self,) -> Optional[teamwork_software_update_status.TeamworkSoftwareUpdateStatus]:
        """
        Gets the adminAgentSoftwareUpdateStatus property value. The software update available for the admin agent.
        Returns: Optional[teamwork_software_update_status.TeamworkSoftwareUpdateStatus]
        """
        return self._admin_agent_software_update_status
    
    @admin_agent_software_update_status.setter
    def admin_agent_software_update_status(self,value: Optional[teamwork_software_update_status.TeamworkSoftwareUpdateStatus] = None) -> None:
        """
        Sets the adminAgentSoftwareUpdateStatus property value. The software update available for the admin agent.
        Args:
            value: Value to set for the adminAgentSoftwareUpdateStatus property.
        """
        self._admin_agent_software_update_status = value
    
    @property
    def company_portal_software_update_status(self,) -> Optional[teamwork_software_update_status.TeamworkSoftwareUpdateStatus]:
        """
        Gets the companyPortalSoftwareUpdateStatus property value. The software update available for the company portal.
        Returns: Optional[teamwork_software_update_status.TeamworkSoftwareUpdateStatus]
        """
        return self._company_portal_software_update_status
    
    @company_portal_software_update_status.setter
    def company_portal_software_update_status(self,value: Optional[teamwork_software_update_status.TeamworkSoftwareUpdateStatus] = None) -> None:
        """
        Sets the companyPortalSoftwareUpdateStatus property value. The software update available for the company portal.
        Args:
            value: Value to set for the companyPortalSoftwareUpdateStatus property.
        """
        self._company_portal_software_update_status = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new teamworkSoftwareUpdateHealth and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The software update available for the admin agent.
        self._admin_agent_software_update_status: Optional[teamwork_software_update_status.TeamworkSoftwareUpdateStatus] = None
        # The software update available for the company portal.
        self._company_portal_software_update_status: Optional[teamwork_software_update_status.TeamworkSoftwareUpdateStatus] = None
        # The software update available for the firmware.
        self._firmware_software_update_status: Optional[teamwork_software_update_status.TeamworkSoftwareUpdateStatus] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The software update available for the operating system.
        self._operating_system_software_update_status: Optional[teamwork_software_update_status.TeamworkSoftwareUpdateStatus] = None
        # The software update available for the partner agent.
        self._partner_agent_software_update_status: Optional[teamwork_software_update_status.TeamworkSoftwareUpdateStatus] = None
        # The software update available for the Teams client.
        self._teams_client_software_update_status: Optional[teamwork_software_update_status.TeamworkSoftwareUpdateStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeamworkSoftwareUpdateHealth:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TeamworkSoftwareUpdateHealth
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TeamworkSoftwareUpdateHealth()
    
    @property
    def firmware_software_update_status(self,) -> Optional[teamwork_software_update_status.TeamworkSoftwareUpdateStatus]:
        """
        Gets the firmwareSoftwareUpdateStatus property value. The software update available for the firmware.
        Returns: Optional[teamwork_software_update_status.TeamworkSoftwareUpdateStatus]
        """
        return self._firmware_software_update_status
    
    @firmware_software_update_status.setter
    def firmware_software_update_status(self,value: Optional[teamwork_software_update_status.TeamworkSoftwareUpdateStatus] = None) -> None:
        """
        Sets the firmwareSoftwareUpdateStatus property value. The software update available for the firmware.
        Args:
            value: Value to set for the firmwareSoftwareUpdateStatus property.
        """
        self._firmware_software_update_status = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "admin_agent_software_update_status": lambda n : setattr(self, 'admin_agent_software_update_status', n.get_object_value(teamwork_software_update_status.TeamworkSoftwareUpdateStatus)),
            "company_portal_software_update_status": lambda n : setattr(self, 'company_portal_software_update_status', n.get_object_value(teamwork_software_update_status.TeamworkSoftwareUpdateStatus)),
            "firmware_software_update_status": lambda n : setattr(self, 'firmware_software_update_status', n.get_object_value(teamwork_software_update_status.TeamworkSoftwareUpdateStatus)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "operating_system_software_update_status": lambda n : setattr(self, 'operating_system_software_update_status', n.get_object_value(teamwork_software_update_status.TeamworkSoftwareUpdateStatus)),
            "partner_agent_software_update_status": lambda n : setattr(self, 'partner_agent_software_update_status', n.get_object_value(teamwork_software_update_status.TeamworkSoftwareUpdateStatus)),
            "teams_client_software_update_status": lambda n : setattr(self, 'teams_client_software_update_status', n.get_object_value(teamwork_software_update_status.TeamworkSoftwareUpdateStatus)),
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
    
    @property
    def operating_system_software_update_status(self,) -> Optional[teamwork_software_update_status.TeamworkSoftwareUpdateStatus]:
        """
        Gets the operatingSystemSoftwareUpdateStatus property value. The software update available for the operating system.
        Returns: Optional[teamwork_software_update_status.TeamworkSoftwareUpdateStatus]
        """
        return self._operating_system_software_update_status
    
    @operating_system_software_update_status.setter
    def operating_system_software_update_status(self,value: Optional[teamwork_software_update_status.TeamworkSoftwareUpdateStatus] = None) -> None:
        """
        Sets the operatingSystemSoftwareUpdateStatus property value. The software update available for the operating system.
        Args:
            value: Value to set for the operatingSystemSoftwareUpdateStatus property.
        """
        self._operating_system_software_update_status = value
    
    @property
    def partner_agent_software_update_status(self,) -> Optional[teamwork_software_update_status.TeamworkSoftwareUpdateStatus]:
        """
        Gets the partnerAgentSoftwareUpdateStatus property value. The software update available for the partner agent.
        Returns: Optional[teamwork_software_update_status.TeamworkSoftwareUpdateStatus]
        """
        return self._partner_agent_software_update_status
    
    @partner_agent_software_update_status.setter
    def partner_agent_software_update_status(self,value: Optional[teamwork_software_update_status.TeamworkSoftwareUpdateStatus] = None) -> None:
        """
        Sets the partnerAgentSoftwareUpdateStatus property value. The software update available for the partner agent.
        Args:
            value: Value to set for the partnerAgentSoftwareUpdateStatus property.
        """
        self._partner_agent_software_update_status = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("adminAgentSoftwareUpdateStatus", self.admin_agent_software_update_status)
        writer.write_object_value("companyPortalSoftwareUpdateStatus", self.company_portal_software_update_status)
        writer.write_object_value("firmwareSoftwareUpdateStatus", self.firmware_software_update_status)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("operatingSystemSoftwareUpdateStatus", self.operating_system_software_update_status)
        writer.write_object_value("partnerAgentSoftwareUpdateStatus", self.partner_agent_software_update_status)
        writer.write_object_value("teamsClientSoftwareUpdateStatus", self.teams_client_software_update_status)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def teams_client_software_update_status(self,) -> Optional[teamwork_software_update_status.TeamworkSoftwareUpdateStatus]:
        """
        Gets the teamsClientSoftwareUpdateStatus property value. The software update available for the Teams client.
        Returns: Optional[teamwork_software_update_status.TeamworkSoftwareUpdateStatus]
        """
        return self._teams_client_software_update_status
    
    @teams_client_software_update_status.setter
    def teams_client_software_update_status(self,value: Optional[teamwork_software_update_status.TeamworkSoftwareUpdateStatus] = None) -> None:
        """
        Sets the teamsClientSoftwareUpdateStatus property value. The software update available for the Teams client.
        Args:
            value: Value to set for the teamsClientSoftwareUpdateStatus property.
        """
        self._teams_client_software_update_status = value
    

