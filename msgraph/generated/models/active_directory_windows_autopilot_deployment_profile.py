from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

windows_autopilot_deployment_profile = lazy_import('msgraph.generated.models.windows_autopilot_deployment_profile')
windows_domain_join_configuration = lazy_import('msgraph.generated.models.windows_domain_join_configuration')

class ActiveDirectoryWindowsAutopilotDeploymentProfile(windows_autopilot_deployment_profile.WindowsAutopilotDeploymentProfile):
    def __init__(self,) -> None:
        """
        Instantiates a new ActiveDirectoryWindowsAutopilotDeploymentProfile and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.activeDirectoryWindowsAutopilotDeploymentProfile"
        # Configuration to join Active Directory domain
        self._domain_join_configuration: Optional[windows_domain_join_configuration.WindowsDomainJoinConfiguration] = None
        # The Autopilot Hybrid Azure AD join flow will continue even if it does not establish domain controller connectivity during OOBE.
        self._hybrid_azure_a_d_join_skip_connectivity_check: Optional[bool] = None
    
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
    
    @property
    def domain_join_configuration(self,) -> Optional[windows_domain_join_configuration.WindowsDomainJoinConfiguration]:
        """
        Gets the domainJoinConfiguration property value. Configuration to join Active Directory domain
        Returns: Optional[windows_domain_join_configuration.WindowsDomainJoinConfiguration]
        """
        return self._domain_join_configuration
    
    @domain_join_configuration.setter
    def domain_join_configuration(self,value: Optional[windows_domain_join_configuration.WindowsDomainJoinConfiguration] = None) -> None:
        """
        Sets the domainJoinConfiguration property value. Configuration to join Active Directory domain
        Args:
            value: Value to set for the domainJoinConfiguration property.
        """
        self._domain_join_configuration = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "domain_join_configuration": lambda n : setattr(self, 'domain_join_configuration', n.get_object_value(windows_domain_join_configuration.WindowsDomainJoinConfiguration)),
            "hybrid_azure_a_d_join_skip_connectivity_check": lambda n : setattr(self, 'hybrid_azure_a_d_join_skip_connectivity_check', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def hybrid_azure_a_d_join_skip_connectivity_check(self,) -> Optional[bool]:
        """
        Gets the hybridAzureADJoinSkipConnectivityCheck property value. The Autopilot Hybrid Azure AD join flow will continue even if it does not establish domain controller connectivity during OOBE.
        Returns: Optional[bool]
        """
        return self._hybrid_azure_a_d_join_skip_connectivity_check
    
    @hybrid_azure_a_d_join_skip_connectivity_check.setter
    def hybrid_azure_a_d_join_skip_connectivity_check(self,value: Optional[bool] = None) -> None:
        """
        Sets the hybridAzureADJoinSkipConnectivityCheck property value. The Autopilot Hybrid Azure AD join flow will continue even if it does not establish domain controller connectivity during OOBE.
        Args:
            value: Value to set for the hybridAzureADJoinSkipConnectivityCheck property.
        """
        self._hybrid_azure_a_d_join_skip_connectivity_check = value
    
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
    

