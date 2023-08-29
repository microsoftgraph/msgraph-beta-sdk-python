from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .business_flow_settings import BusinessFlowSettings
    from .entity import Entity
    from .governance_policy import GovernancePolicy

from .entity import Entity

@dataclass
class GovernancePolicyTemplate(Entity):
    # The displayName property
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The policy property
    policy: Optional[GovernancePolicy] = None
    # The settings property
    settings: Optional[BusinessFlowSettings] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> GovernancePolicyTemplate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: GovernancePolicyTemplate
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return GovernancePolicyTemplate()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .business_flow_settings import BusinessFlowSettings
        from .entity import Entity
        from .governance_policy import GovernancePolicy

        from .business_flow_settings import BusinessFlowSettings
        from .entity import Entity
        from .governance_policy import GovernancePolicy

        fields: Dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "policy": lambda n : setattr(self, 'policy', n.get_object_value(GovernancePolicy)),
            "settings": lambda n : setattr(self, 'settings', n.get_object_value(BusinessFlowSettings)),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("policy", self.policy)
        writer.write_object_value("settings", self.settings)
    

