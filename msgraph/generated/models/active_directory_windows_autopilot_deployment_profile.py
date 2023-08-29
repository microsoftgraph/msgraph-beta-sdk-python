from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .windows_autopilot_deployment_profile import WindowsAutopilotDeploymentProfile
    from .windows_domain_join_configuration import WindowsDomainJoinConfiguration

from .windows_autopilot_deployment_profile import WindowsAutopilotDeploymentProfile

@dataclass
class ActiveDirectoryWindowsAutopilotDeploymentProfile(WindowsAutopilotDeploymentProfile):
    """
    Windows Autopilot Deployment Profile
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.activeDirectoryWindowsAutopilotDeploymentProfile"
    # Configuration to join Active Directory domain
    domain_join_configuration: Optional[WindowsDomainJoinConfiguration] = None
    # The Autopilot Hybrid Azure AD join flow will continue even if it does not establish domain controller connectivity during OOBE.
    hybrid_azure_a_d_join_skip_connectivity_check: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ActiveDirectoryWindowsAutopilotDeploymentProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ActiveDirectoryWindowsAutopilotDeploymentProfile
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ActiveDirectoryWindowsAutopilotDeploymentProfile()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .windows_autopilot_deployment_profile import WindowsAutopilotDeploymentProfile
        from .windows_domain_join_configuration import WindowsDomainJoinConfiguration

        from .windows_autopilot_deployment_profile import WindowsAutopilotDeploymentProfile
        from .windows_domain_join_configuration import WindowsDomainJoinConfiguration

        fields: Dict[str, Callable[[Any], None]] = {
            "domainJoinConfiguration": lambda n : setattr(self, 'domain_join_configuration', n.get_object_value(WindowsDomainJoinConfiguration)),
            "hybridAzureADJoinSkipConnectivityCheck": lambda n : setattr(self, 'hybrid_azure_a_d_join_skip_connectivity_check', n.get_bool_value()),
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
        writer.write_object_value("domainJoinConfiguration", self.domain_join_configuration)
        writer.write_bool_value("hybridAzureADJoinSkipConnectivityCheck", self.hybrid_azure_a_d_join_skip_connectivity_check)
    

