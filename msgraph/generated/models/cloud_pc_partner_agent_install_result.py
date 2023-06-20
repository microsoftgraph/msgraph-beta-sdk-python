from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import cloud_pc_partner_agent_install_status, cloud_pc_partner_agent_name

@dataclass
class CloudPcPartnerAgentInstallResult(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The status of a partner agent installation. Possible values are: installed, installFailed, installing, uninstalling, uninstallFailed and licensed. Read-Only.
    install_status: Optional[cloud_pc_partner_agent_install_status.CloudPcPartnerAgentInstallStatus] = None
    # Indicates if the partner agent is a third party. When 'TRUE', the agent is a third-party (non-Microsoft) agent.  When 'FALSE', the agent is a Microsoft agent or is not known.  The default value is 'FALSE'.
    is_third_party_partner: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates the name of a partner agent and includes first-party and third-party. Currently, Citrix is the only third-party value. Read-Only.
    partner_agent_name: Optional[cloud_pc_partner_agent_name.CloudPcPartnerAgentName] = None
    # Indicates if the partner agent is a third party. When 'TRUE', the agent is a third-party (non-Microsoft) agent. When 'FALSE', the agent is a Microsoft agent or is not known. The default value is 'FALSE'.
    retriable: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CloudPcPartnerAgentInstallResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcPartnerAgentInstallResult
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return CloudPcPartnerAgentInstallResult()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import cloud_pc_partner_agent_install_status, cloud_pc_partner_agent_name

        from . import cloud_pc_partner_agent_install_status, cloud_pc_partner_agent_name

        fields: Dict[str, Callable[[Any], None]] = {
            "installStatus": lambda n : setattr(self, 'install_status', n.get_enum_value(cloud_pc_partner_agent_install_status.CloudPcPartnerAgentInstallStatus)),
            "isThirdPartyPartner": lambda n : setattr(self, 'is_third_party_partner', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "partnerAgentName": lambda n : setattr(self, 'partner_agent_name', n.get_enum_value(cloud_pc_partner_agent_name.CloudPcPartnerAgentName)),
            "retriable": lambda n : setattr(self, 'retriable', n.get_bool_value()),
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
        writer.write_enum_value("installStatus", self.install_status)
        writer.write_bool_value("isThirdPartyPartner", self.is_third_party_partner)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("partnerAgentName", self.partner_agent_name)
        writer.write_bool_value("retriable", self.retriable)
        writer.write_additional_data_value(self.additional_data)
    

