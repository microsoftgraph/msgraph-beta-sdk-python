from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import connectivity, forwarding_policy, forwarding_profile, logs, reports, settings, tenant_status
    from .. import entity

from .. import entity

@dataclass
class NetworkAccessRoot(entity.Entity):
    # The connectivity property
    connectivity: Optional[connectivity.Connectivity] = None
    # The forwardingPolicies property
    forwarding_policies: Optional[List[forwarding_policy.ForwardingPolicy]] = None
    # The forwardingProfiles property
    forwarding_profiles: Optional[List[forwarding_profile.ForwardingProfile]] = None
    # The logs property
    logs: Optional[logs.Logs] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The reports property
    reports: Optional[reports.Reports] = None
    # The settings property
    settings: Optional[settings.Settings] = None
    # The tenantStatus property
    tenant_status: Optional[tenant_status.TenantStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> NetworkAccessRoot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: NetworkAccessRoot
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return NetworkAccessRoot()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import connectivity, forwarding_policy, forwarding_profile, logs, reports, settings, tenant_status
        from .. import entity

        from . import connectivity, forwarding_policy, forwarding_profile, logs, reports, settings, tenant_status
        from .. import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "connectivity": lambda n : setattr(self, 'connectivity', n.get_object_value(connectivity.Connectivity)),
            "forwardingPolicies": lambda n : setattr(self, 'forwarding_policies', n.get_collection_of_object_values(forwarding_policy.ForwardingPolicy)),
            "forwardingProfiles": lambda n : setattr(self, 'forwarding_profiles', n.get_collection_of_object_values(forwarding_profile.ForwardingProfile)),
            "logs": lambda n : setattr(self, 'logs', n.get_object_value(logs.Logs)),
            "reports": lambda n : setattr(self, 'reports', n.get_object_value(reports.Reports)),
            "settings": lambda n : setattr(self, 'settings', n.get_object_value(settings.Settings)),
            "tenantStatus": lambda n : setattr(self, 'tenant_status', n.get_object_value(tenant_status.TenantStatus)),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_object_value("connectivity", self.connectivity)
        writer.write_collection_of_object_values("forwardingPolicies", self.forwarding_policies)
        writer.write_collection_of_object_values("forwardingProfiles", self.forwarding_profiles)
        writer.write_object_value("logs", self.logs)
        writer.write_object_value("reports", self.reports)
        writer.write_object_value("settings", self.settings)
        writer.write_object_value("tenantStatus", self.tenant_status)
    

