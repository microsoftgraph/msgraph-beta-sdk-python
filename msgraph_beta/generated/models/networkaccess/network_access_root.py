from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .connectivity import Connectivity
    from .forwarding_policy import ForwardingPolicy
    from .forwarding_profile import ForwardingProfile
    from .logs import Logs
    from .reports import Reports
    from .settings import Settings
    from .tenant_status import TenantStatus

from ..entity import Entity

@dataclass
class NetworkAccessRoot(Entity):
    # Connectivity represents all the connectivity components in Global Secure Access.
    connectivity: Optional[Connectivity] = None
    # A forwarding policy defines the specific traffic that is routed through the Global Secure Access Service. It's then added to a forwarding profile.
    forwarding_policies: Optional[List[ForwardingPolicy]] = None
    # A forwarding profile determines which types of traffic are routed through the Global Secure Access services and which ones are skipped. The handling of specific traffic is determined by the forwarding policies that are added to the forwarding profile.
    forwarding_profiles: Optional[List[ForwardingProfile]] = None
    # Represents network connections that are routed through Global Secure Access.
    logs: Optional[Logs] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Represents the status of the Global Secure Access services for the tenant.
    reports: Optional[Reports] = None
    # Global Secure Access settings.
    settings: Optional[Settings] = None
    # Represents the status of the Global Secure Access services for the tenant.
    tenant_status: Optional[TenantStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> NetworkAccessRoot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
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
        from ..entity import Entity
        from .connectivity import Connectivity
        from .forwarding_policy import ForwardingPolicy
        from .forwarding_profile import ForwardingProfile
        from .logs import Logs
        from .reports import Reports
        from .settings import Settings
        from .tenant_status import TenantStatus

        from ..entity import Entity
        from .connectivity import Connectivity
        from .forwarding_policy import ForwardingPolicy
        from .forwarding_profile import ForwardingProfile
        from .logs import Logs
        from .reports import Reports
        from .settings import Settings
        from .tenant_status import TenantStatus

        fields: Dict[str, Callable[[Any], None]] = {
            "connectivity": lambda n : setattr(self, 'connectivity', n.get_object_value(Connectivity)),
            "forwardingPolicies": lambda n : setattr(self, 'forwarding_policies', n.get_collection_of_object_values(ForwardingPolicy)),
            "forwardingProfiles": lambda n : setattr(self, 'forwarding_profiles', n.get_collection_of_object_values(ForwardingProfile)),
            "logs": lambda n : setattr(self, 'logs', n.get_object_value(Logs)),
            "reports": lambda n : setattr(self, 'reports', n.get_object_value(Reports)),
            "settings": lambda n : setattr(self, 'settings', n.get_object_value(Settings)),
            "tenantStatus": lambda n : setattr(self, 'tenant_status', n.get_object_value(TenantStatus)),
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
        writer.write_object_value("connectivity", self.connectivity)
        writer.write_collection_of_object_values("forwardingPolicies", self.forwarding_policies)
        writer.write_collection_of_object_values("forwardingProfiles", self.forwarding_profiles)
        writer.write_object_value("logs", self.logs)
        writer.write_object_value("reports", self.reports)
        writer.write_object_value("settings", self.settings)
        writer.write_object_value("tenantStatus", self.tenant_status)
    

