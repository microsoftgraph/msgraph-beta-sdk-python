from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import windows_autopilot_deployment_profile, windows_domain_join_configuration

from . import windows_autopilot_deployment_profile

@dataclass
class ActiveDirectoryWindowsAutopilotDeploymentProfile(windows_autopilot_deployment_profile.WindowsAutopilotDeploymentProfile):
    odata_type = "#microsoft.graph.activeDirectoryWindowsAutopilotDeploymentProfile"
    # Configuration to join Active Directory domain
    domain_join_configuration: Optional[windows_domain_join_configuration.WindowsDomainJoinConfiguration] = None
    # The Autopilot Hybrid Azure AD join flow will continue even if it does not establish domain controller connectivity during OOBE.
    hybrid_azure_a_d_join_skip_connectivity_check: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ActiveDirectoryWindowsAutopilotDeploymentProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ActiveDirectoryWindowsAutopilotDeploymentProfile
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ActiveDirectoryWindowsAutopilotDeploymentProfile()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import windows_autopilot_deployment_profile, windows_domain_join_configuration

        fields: Dict[str, Callable[[Any], None]] = {
            "domainJoinConfiguration": lambda n : setattr(self, 'domain_join_configuration', n.get_object_value(windows_domain_join_configuration.WindowsDomainJoinConfiguration)),
            "hybridAzureADJoinSkipConnectivityCheck": lambda n : setattr(self, 'hybrid_azure_a_d_join_skip_connectivity_check', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("domainJoinConfiguration", self.domain_join_configuration)
        writer.write_bool_value("hybridAzureADJoinSkipConnectivityCheck", self.hybrid_azure_a_d_join_skip_connectivity_check)
    

