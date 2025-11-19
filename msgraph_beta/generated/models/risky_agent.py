from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .risky_agent_identity import RiskyAgentIdentity
    from .risky_agent_identity_blueprint_principal import RiskyAgentIdentityBlueprintPrincipal
    from .risky_agent_user import RiskyAgentUser
    from .risk_detail import RiskDetail
    from .risk_level import RiskLevel
    from .risk_state import RiskState

from .entity import Entity

@dataclass
class RiskyAgent(Entity, Parsable):
    # Name of the agent.  Supports $filter (eq, startsWith).
    agent_display_name: Optional[str] = None
    # Indicates whether the agent is deleted.
    is_deleted: Optional[bool] = None
    # Indicates whether the agent is enabled.
    is_enabled: Optional[bool] = None
    # Indicates whether an agent's risky state is processing in the backend.
    is_processing: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The riskDetail property
    risk_detail: Optional[RiskDetail] = None
    # The date and time that the risky agent was last updated. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.  Supports $filter (eq, le, and ge).
    risk_last_modified_date_time: Optional[datetime.datetime] = None
    # The riskLevel property
    risk_level: Optional[RiskLevel] = None
    # The riskState property
    risk_state: Optional[RiskState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RiskyAgent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RiskyAgent
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.riskyAgentIdentity".casefold():
            from .risky_agent_identity import RiskyAgentIdentity

            return RiskyAgentIdentity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.riskyAgentIdentityBlueprintPrincipal".casefold():
            from .risky_agent_identity_blueprint_principal import RiskyAgentIdentityBlueprintPrincipal

            return RiskyAgentIdentityBlueprintPrincipal()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.riskyAgentUser".casefold():
            from .risky_agent_user import RiskyAgentUser

            return RiskyAgentUser()
        return RiskyAgent()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .risky_agent_identity import RiskyAgentIdentity
        from .risky_agent_identity_blueprint_principal import RiskyAgentIdentityBlueprintPrincipal
        from .risky_agent_user import RiskyAgentUser
        from .risk_detail import RiskDetail
        from .risk_level import RiskLevel
        from .risk_state import RiskState

        from .entity import Entity
        from .risky_agent_identity import RiskyAgentIdentity
        from .risky_agent_identity_blueprint_principal import RiskyAgentIdentityBlueprintPrincipal
        from .risky_agent_user import RiskyAgentUser
        from .risk_detail import RiskDetail
        from .risk_level import RiskLevel
        from .risk_state import RiskState

        fields: dict[str, Callable[[Any], None]] = {
            "agentDisplayName": lambda n : setattr(self, 'agent_display_name', n.get_str_value()),
            "isDeleted": lambda n : setattr(self, 'is_deleted', n.get_bool_value()),
            "isEnabled": lambda n : setattr(self, 'is_enabled', n.get_bool_value()),
            "isProcessing": lambda n : setattr(self, 'is_processing', n.get_bool_value()),
            "riskDetail": lambda n : setattr(self, 'risk_detail', n.get_enum_value(RiskDetail)),
            "riskLastModifiedDateTime": lambda n : setattr(self, 'risk_last_modified_date_time', n.get_datetime_value()),
            "riskLevel": lambda n : setattr(self, 'risk_level', n.get_enum_value(RiskLevel)),
            "riskState": lambda n : setattr(self, 'risk_state', n.get_enum_value(RiskState)),
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
        writer.write_str_value("agentDisplayName", self.agent_display_name)
        writer.write_bool_value("isDeleted", self.is_deleted)
        writer.write_bool_value("isEnabled", self.is_enabled)
        writer.write_bool_value("isProcessing", self.is_processing)
        writer.write_enum_value("riskDetail", self.risk_detail)
        writer.write_datetime_value("riskLastModifiedDateTime", self.risk_last_modified_date_time)
        writer.write_enum_value("riskLevel", self.risk_level)
        writer.write_enum_value("riskState", self.risk_state)
    

