from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cloud_pc_partner_agent_install_status import CloudPcPartnerAgentInstallStatus
    from .cloud_pc_partner_agent_name import CloudPcPartnerAgentName

@dataclass
class CloudPcPartnerAgentInstallResult(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The errorMessage property
    error_message: Optional[str] = None
    # The status of a partner agent installation. Possible values are: installed, installFailed, installing, uninstalling, uninstallFailed and licensed. Read-Only.
    install_status: Optional[CloudPcPartnerAgentInstallStatus] = None
    # Indicates if the partner agent is a third party. When 'TRUE' the agent is a third-party (non-Microsoft) agent and when 'FALSE' the agent is a Microsoft agent or isn't known.  The default value is 'FALSE'
    is_third_party_partner: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The name of the partner agent, whether first party or third party. Possible values for third-party partners are Citrix and VMware. Read-Only.
    partner_agent_name: Optional[CloudPcPartnerAgentName] = None
    # Indicates if the partner agent is a third party. When 'TRUE' the agent is a third-party (non-Microsoft) agent and when 'FALSE' the agent is a Microsoft agent or isn't known. The default value is 'FALSE'
    retriable: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CloudPcPartnerAgentInstallResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
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
        from .cloud_pc_partner_agent_install_status import CloudPcPartnerAgentInstallStatus
        from .cloud_pc_partner_agent_name import CloudPcPartnerAgentName

        from .cloud_pc_partner_agent_install_status import CloudPcPartnerAgentInstallStatus
        from .cloud_pc_partner_agent_name import CloudPcPartnerAgentName

        fields: Dict[str, Callable[[Any], None]] = {
            "errorMessage": lambda n : setattr(self, 'error_message', n.get_str_value()),
            "installStatus": lambda n : setattr(self, 'install_status', n.get_enum_value(CloudPcPartnerAgentInstallStatus)),
            "isThirdPartyPartner": lambda n : setattr(self, 'is_third_party_partner', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "partnerAgentName": lambda n : setattr(self, 'partner_agent_name', n.get_enum_value(CloudPcPartnerAgentName)),
            "retriable": lambda n : setattr(self, 'retriable', n.get_bool_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("errorMessage", self.error_message)
        writer.write_enum_value("installStatus", self.install_status)
        writer.write_bool_value("isThirdPartyPartner", self.is_third_party_partner)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("partnerAgentName", self.partner_agent_name)
        writer.write_bool_value("retriable", self.retriable)
        writer.write_additional_data_value(self.additional_data)
    

