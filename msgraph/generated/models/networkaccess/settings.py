from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import conditional_access_settings, cross_tenant_access_settings, enriched_audit_logs, forwarding_options
    from .. import entity

from .. import entity

@dataclass
class Settings(entity.Entity):
    # The conditionalAccess property
    conditional_access: Optional[conditional_access_settings.ConditionalAccessSettings] = None
    # The crossTenantAccess property
    cross_tenant_access: Optional[cross_tenant_access_settings.CrossTenantAccessSettings] = None
    # The enrichedAuditLogs property
    enriched_audit_logs: Optional[enriched_audit_logs.EnrichedAuditLogs] = None
    # The forwardingOptions property
    forwarding_options: Optional[forwarding_options.ForwardingOptions] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Settings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Settings
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Settings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import conditional_access_settings, cross_tenant_access_settings, enriched_audit_logs, forwarding_options
        from .. import entity

        from . import conditional_access_settings, cross_tenant_access_settings, enriched_audit_logs, forwarding_options
        from .. import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "conditionalAccess": lambda n : setattr(self, 'conditional_access', n.get_object_value(conditional_access_settings.ConditionalAccessSettings)),
            "crossTenantAccess": lambda n : setattr(self, 'cross_tenant_access', n.get_object_value(cross_tenant_access_settings.CrossTenantAccessSettings)),
            "enrichedAuditLogs": lambda n : setattr(self, 'enriched_audit_logs', n.get_object_value(enriched_audit_logs.EnrichedAuditLogs)),
            "forwardingOptions": lambda n : setattr(self, 'forwarding_options', n.get_object_value(forwarding_options.ForwardingOptions)),
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
        writer.write_object_value("conditionalAccess", self.conditional_access)
        writer.write_object_value("crossTenantAccess", self.cross_tenant_access)
        writer.write_object_value("enrichedAuditLogs", self.enriched_audit_logs)
        writer.write_object_value("forwardingOptions", self.forwarding_options)
    

