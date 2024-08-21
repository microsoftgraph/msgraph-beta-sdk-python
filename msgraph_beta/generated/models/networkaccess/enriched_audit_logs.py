from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .enriched_audit_logs_settings import EnrichedAuditLogsSettings

from ..entity import Entity

@dataclass
class EnrichedAuditLogs(Entity):
    # Exchange Online enriched audit logs settings.
    exchange: Optional[EnrichedAuditLogsSettings] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # SharePoint Online enriched audit logs settings.
    sharepoint: Optional[EnrichedAuditLogsSettings] = None
    # Teams enriched audit logs settings.
    teams: Optional[EnrichedAuditLogsSettings] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EnrichedAuditLogs:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EnrichedAuditLogs
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EnrichedAuditLogs()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .enriched_audit_logs_settings import EnrichedAuditLogsSettings

        from ..entity import Entity
        from .enriched_audit_logs_settings import EnrichedAuditLogsSettings

        fields: Dict[str, Callable[[Any], None]] = {
            "exchange": lambda n : setattr(self, 'exchange', n.get_object_value(EnrichedAuditLogsSettings)),
            "sharepoint": lambda n : setattr(self, 'sharepoint', n.get_object_value(EnrichedAuditLogsSettings)),
            "teams": lambda n : setattr(self, 'teams', n.get_object_value(EnrichedAuditLogsSettings)),
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
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_object_value("exchange", self.exchange)
        writer.write_object_value("sharepoint", self.sharepoint)
        writer.write_object_value("teams", self.teams)
    

